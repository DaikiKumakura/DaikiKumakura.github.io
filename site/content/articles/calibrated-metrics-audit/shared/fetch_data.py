"""Download the public inputs (not redistributed here) and check them against the recorded hashes.
Run first: python fetch_data.py          (Wessels, ~219 MB)
           python fetch_data.py all      (also Norman ~0.7 GB and Replogle K562 essential ~1.5 GB)"""
import hashlib
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = "https://zenodo.org/api/records/13350497/files/{}/content"
FILES = [("WesselsSatija2023.h5ad", HERE / "results/data-sha256.txt", 0)]
if len(sys.argv) > 1 and sys.argv[1] == "all":
    FILES += [("NormanWeissman2019_filtered.h5ad", HERE / "results/data-sha256-other.txt", 0),
              ("ReplogleWeissman2022_K562_essential.h5ad", HERE / "results/data-sha256-other.txt", 1)]
for name, hashfile, _ in FILES:
    dest = HERE / "data/raw" / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(BASE.format(name), timeout=600) as r, open(dest, "wb") as fh:
        while chunk := r.read(1 << 20):
            fh.write(chunk)
    sha = hashlib.sha256()
    with open(dest, "rb") as fh:
        while chunk := fh.read(1 << 22):
            sha.update(chunk)
    ok = any(line.split()[0] == sha.hexdigest() for line in hashfile.read_text().splitlines() if line.strip())
    print(name, "OK" if ok else "HASH DIFFERS (the source may have been updated)")
