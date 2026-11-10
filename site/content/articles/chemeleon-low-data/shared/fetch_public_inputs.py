"""Retrieve fixed public result/assay inputs and verify SHA256; execute no downloaded code."""
from pathlib import Path
import hashlib,json,urllib.request
ROOT=Path(__file__).resolve().parent
count=0
for name in ['source-manifest.json','assay-manifest.json']:
    manifest=json.loads((ROOT/name).read_text())
    for row in manifest['files']:
        dest=ROOT/'source'/row['path']
        if dest.exists() and hashlib.sha256(dest.read_bytes()).hexdigest()==row['sha256']:
            count+=1;continue
        data=urllib.request.urlopen(row['url'],timeout=60).read()
        assert hashlib.sha256(data).hexdigest()==row['sha256'],row['path']
        dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data);count+=1
print('Verified',count,'fixed public inputs.')
