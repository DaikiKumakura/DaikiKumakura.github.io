"""Download eight pinned public prediction tables; execute no downloaded code."""
import hashlib,json,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'source-manifest.json').read_text())
for row in manifest['files']:
    dest=ROOT/'source'/row['path']
    if dest.exists() and hashlib.sha256(dest.read_bytes()).hexdigest()==row['sha256']:continue
    data=urllib.request.urlopen(row['url'],timeout=60).read()
    assert hashlib.sha256(data).hexdigest()==row['sha256'],row['path']
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_bytes(data)
print('Verified',len(manifest['files']),'pinned input tables.')
