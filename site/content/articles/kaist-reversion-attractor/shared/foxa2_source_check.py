"""Check where FOXA2, MYB and HDAC2 are detected in the model's source single-cell data (GSE125970, human ileum/colon/rectum).
Run after downloading GSE125970_cell_info.txt.gz and GSE125970_raw_UMIcounts.txt.gz (NCBI GEO, ftp.ncbi.nlm.nih.gov/geo/series/GSE125nnn/GSE125970/suppl/) into data/raw_tmp/. Output: results/foxa2_source_check.json"""
import collections
import gzip
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RAW = HERE / "data/raw_tmp"
GENES = ["FOXA2", "MYB", "HDAC2", "KRT20", "LGR5"]
info = [l.split("\t") for l in gzip.open(RAW / "GSE125970_cell_info.txt.gz", "rt").read().splitlines()[1:]]
cid = {r[0]: (r[1], r[2]) for r in info}
f = gzip.open(RAW / "GSE125970_raw_UMIcounts.txt.gz", "rt")
cells = f.readline().rstrip("\n").split("\t")[1:]
assert len(cells) == len(info) and all(c in cid for c in cells)
tot = np.zeros(len(cells))
rows = {}
for line in f:
    p = line.rstrip("\n").split("\t")
    v = np.array(p[1:], dtype=np.float32)
    tot += v
    if p[0] in GENES:
        rows[p[0]] = v
site = np.array([cid[c][0].split("-")[0] for c in cells])
ctype = np.array([cid[c][1] for c in cells])
out = {"n_cells": len(cells), "note": "detected = UMI>0; mean_cp10k = mean of counts/total*1e4", "by_site_and_type": {}}
for s in ("Colon", "Rectum", "Ileum"):
    for t in sorted(set(ctype)):
        m = (site == s) & (ctype == t)
        if m.sum() < 20:
            continue
        out["by_site_and_type"][f"{s}|{t}"] = dict(n=int(m.sum()), **{g: dict(detected_pct=round(float((rows[g][m] > 0).mean() * 100), 1), mean_cp10k=round(float((rows[g][m] / tot[m] * 1e4).mean()), 2)) for g in GENES})
(HERE / "results/foxa2_source_check.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
for k, v in out["by_site_and_type"].items():
    print(k, v["n"], {g: (v[g]["detected_pct"], v[g]["mean_cp10k"]) for g in GENES})
