"""Download the public inputs (not redistributed here) and check them against results/plan-and-data-sha256.txt.
Run first: python fetch_data.py   (needs network; ~1 MB)"""
import hashlib
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
GEO = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE327nnn/GSE327208/suppl/GSE327208_{}_count.tsv.gz"
ENRICHR = "https://maayanlab.cloud/Enrichr/geneSetLibrary?mode=text&libraryName={}"
MSIGDB = "https://data.broadinstitute.org/gsea-msigdb/msigdb/release/2023.2.Hs/h.all.v2023.2.Hs.symbols.gmt"
JOBS = [(GEO.format(c), HERE / f"data/raw/GSE327208_{c}_count.tsv.gz") for c in ("CACO2", "HCT116", "HT29")]
JOBS += [(ENRICHR.format("Tabula_Sapiens"), HERE / "data/genesets/enrichr_Tabula_Sapiens.txt"),
         (ENRICHR.format("PanglaoDB_Augmented_2021"), HERE / "data/genesets/enrichr_PanglaoDB_Augmented_2021.txt"),
         (MSIGDB, HERE / "data/genesets/hallmark_v2023.2.gmt")]
expected = {}
for line in (HERE / "results/plan-and-data-sha256.txt").read_text().splitlines():
    h, name = line.split(None, 1)
    expected[name.strip().lstrip("*")] = h
for url, dest in JOBS:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(urllib.request.urlopen(url, timeout=120).read())
    got = hashlib.sha256(dest.read_bytes()).hexdigest()
    rel = dest.relative_to(HERE).as_posix()
    print(rel, "OK" if expected.get(rel) == got else "HASH DIFFERS (the source may have been updated)")
