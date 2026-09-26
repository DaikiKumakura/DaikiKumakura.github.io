"""Rebuild and copy generated pages into the parent repository. Does not push."""
from pathlib import Path
import json
import shutil
import build

def stage(destination):
    destination=Path(destination).resolve()
    if not (destination/'.git').exists():
        raise ValueError('Destination must be a Git checkout')
    build.build(strict_translations=True)
    previous=destination/'_portfolio'/'published-files.json'
    old=json.loads(previous.read_text(encoding='utf-8')) if previous.exists() else []
    names=json.loads((build.BASE/'dist/.generated.json').read_text(encoding='utf-8'))
    # Preserve existing branch publishing with Jekyll excluding the maintenance source.
    names=[n for n in names if n!='.nojekyll']
    for name in set(old)-set(names):
        target=(destination/build.safe_relative(name)).resolve()
        if not target.is_relative_to(destination): raise ValueError('Outside repository')
        if target.is_file():target.unlink()
    for name in names:
        target=(destination/build.safe_relative(name)).resolve()
        if not target.is_relative_to(destination): raise ValueError('Outside repository')
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(build.BASE/'dist'/name,target)
    previous.parent.mkdir(parents=True,exist_ok=True)
    previous.write_text(json.dumps(names,indent=2)+'\n',encoding='utf-8')
    print(f'Staged {len(names)} generated files; review git diff before committing.')

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('destination',nargs='?',default=str(build.BASE.parent))
    stage(parser.parse_args().destination)
