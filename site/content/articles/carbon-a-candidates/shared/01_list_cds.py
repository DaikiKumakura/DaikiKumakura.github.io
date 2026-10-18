"""List per-assembly prediction files in the Carbon-A GenBank annotation bucket.

Run: python 01_list_cds.py   (network; ~200 paged API requests)
Writes data/cds_listing.csv (one row per file) and data/cds_assemblies.csv (one row per assembly).
"""
from pathlib import Path
import csv
import json
import time
import urllib.request

ROOT = Path(__file__).resolve().parent
API = "https://huggingface.co/api/buckets/HuggingFaceBio/genbank-annotations/tree/cds?limit=1000&recursive=true&sort=path"


def fetch(url: str) -> tuple[list, str | None]:
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                link = r.headers.get("Link")
                data = json.loads(r.read())
            nxt = None
            if link and 'rel="next"' in link:
                nxt = link.split(";")[0].strip("<> ")
            return data, nxt
        except Exception as e:  # transient network errors
            print("retry", attempt, e)
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(url)


def main() -> None:
    rows, url, pages = [], API, 0
    while url:
        data, url = fetch(url)
        pages += 1
        rows += [dict(path=f["path"], size=f.get("size"), uploaded=f.get("uploadedAt")) for f in data if f["type"] == "file"]
        if pages % 20 == 0:
            print(pages, len(rows))
    out = ROOT / "data"
    with open(out / "cds_listing.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["path", "size", "uploaded"])
        w.writeheader()
        w.writerows(rows)
    asm: dict[tuple[str, str], dict] = {}
    for r in rows:
        parts = r["path"].split("/")
        if len(parts) != 4:
            continue
        _, division, acc, name = parts
        a = asm.setdefault((division, acc), dict(division=division, accession=acc))
        a[name.replace(".", "_")] = r["size"]
    with open(out / "cds_assemblies.csv", "w", newline="", encoding="utf-8") as fh:
        cols = ["division", "accession", "metadata_json", "annotations_gff3_gz", "cds_fna_gz", "proteins_faa_gz"]
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(asm.values())
    print(json.dumps(dict(pages=pages, files=len(rows), assemblies=len(asm)), indent=1))


if __name__ == "__main__":
    main()
