"""Download the NCBI taxonomy table shipped with the Carbon-A Database Explorer Space.

Run: python 00_fetch_explorer_taxonomy.py   (network, ~27 MB)
Writes data/explorer_taxonomy.sqlite (tables: taxa, assemblies, metadata).
"""
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent
URL = "https://huggingface.co/spaces/HuggingFaceBio/carbon-a-database-explorer/resolve/main/data/taxonomy.sqlite"

if __name__ == "__main__":
    dest = ROOT / "data" / "explorer_taxonomy.sqlite"
    dest.parent.mkdir(exist_ok=True)
    urllib.request.urlretrieve(URL, dest)
    print(dest, dest.stat().st_size)
