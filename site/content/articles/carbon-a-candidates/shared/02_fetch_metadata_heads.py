"""Fetch the first bytes of every per-assembly metadata.json (HTTP range request) and parse summary fields.

Run: python 02_fetch_metadata_heads.py   (network; one ~1 kB range request per assembly, cached)
Writes data/metadata_heads.csv.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import csv
import json
import re
import time
import urllib.request

ROOT = Path(__file__).resolve().parent
BASE = "https://huggingface.co/buckets/HuggingFaceBio/genbank-annotations/resolve/cds"
HEAD_BYTES = 1199
WORKERS = 8
CACHE = ROOT / "data" / "metadata_heads.jsonl"
FIELDS = {
    "paired_refseq_accession": r'"paired_refseq_accession":\s*"([^"]*)"',
    "paired_assembly_comparison": r'"paired_assembly_comparison":\s*"([^"]*)"',
    "organism_name": r'"organism_name":\s*"([^"]*)"',
    "taxid": r'"taxid":\s*(\d+)',
    "annotated_bases": r'"annotated_bases":\s*(\d+)',
    "gene_count": r'"gene_count":\s*(\d+)',
}


def head(division: str, acc: str) -> dict:
    url = f"{BASE}/{division}/{acc}/metadata.json"
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"Range": f"bytes=0-{HEAD_BYTES}"})
            with urllib.request.urlopen(req, timeout=60) as r:
                txt = r.read().decode("utf-8", "replace")
            rec = dict(division=division, accession=acc)
            for k, pat in FIELDS.items():
                m = re.search(pat, txt)
                rec[k] = m.group(1) if m else None
            return rec
        except Exception as e:
            time.sleep(3 * (attempt + 1))
            err = str(e)
    return dict(division=division, accession=acc, error=err)


def main() -> None:
    with open(ROOT / "data" / "cds_assemblies.csv", encoding="utf-8") as fh:
        todo = [(r["division"], r["accession"]) for r in csv.DictReader(fh)]
    done = {}
    if CACHE.exists():
        for line in CACHE.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            if "error" not in r:
                done[(r["division"], r["accession"])] = r
    todo = [t for t in todo if t not in done]
    print("to fetch", len(todo), "cached", len(done))
    with open(CACHE, "a", encoding="utf-8") as out, ThreadPoolExecutor(WORKERS) as ex:
        for i, rec in enumerate(ex.map(lambda t: head(*t), todo)):
            out.write(json.dumps(rec) + "\n")
            if i % 2000 == 0:
                print(i)
    recs = {}
    for line in CACHE.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        if "error" not in r:
            recs[(r["division"], r["accession"])] = r
    cols = ["division", "accession", *FIELDS]
    with open(ROOT / "data" / "metadata_heads.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(recs.values())
    print("parsed", len(recs))


if __name__ == "__main__":
    main()
