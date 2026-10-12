"""Download the public input (not redistributed here, ~219 MB) and check it against results/data-sha256.txt.
Run first: python fetch_data.py"""
import hashlib
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
URL = "https://zenodo.org/api/records/13350497/files/WesselsSatija2023.h5ad/content"
dest = HERE / "data/raw/WesselsSatija2023.h5ad"
dest.parent.mkdir(parents=True, exist_ok=True)
with urllib.request.urlopen(URL, timeout=600) as r, open(dest, "wb") as fh:
    while chunk := r.read(1 << 20):
        fh.write(chunk)
sha = hashlib.sha256(dest.read_bytes()).hexdigest()
expected = (HERE / "results/data-sha256.txt").read_text().split()[0]
print(dest.name, "OK" if sha == expected else "HASH DIFFERS (the source may have been updated)")
