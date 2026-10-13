"""Independent re-computation of the set-level z (gene-set permutation) with separate code and a different RNG.
Run: python independent_check.py (numpy, pandas). Compares with results/summary.json (analysis.py)."""
import gzip
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
RS = np.random.RandomState(777)
NP = 20000
S = json.load(open(HERE / "results/summary.json", encoding="utf-8"))["e2"]
gmt = {l.split("\t")[0]: set(l.split("\t")[2:]) for l in (HERE / "data/genesets/hallmark_v2023.2.gmt").read_text(encoding="utf-8").splitlines()}
ts = {l.split("\t")[0]: {g.split(",")[0] for g in l.split("\t")[2:] if g} for l in (HERE / "data/genesets/enrichr_Tabula_Sapiens.txt").read_text(encoding="utf-8").splitlines()}
sets = {"Large Intestine-mature Enterocyte": ts["Large Intestine-mature Enterocyte"], "HALLMARK_E2F_TARGETS": gmt["HALLMARK_E2F_TARGETS"],
        "HALLMARK_MYC_TARGETS_V1": gmt["HALLMARK_MYC_TARGETS_V1"], "HALLMARK_G2M_CHECKPOINT": gmt["HALLMARK_G2M_CHECKPOINT"]}
out = {}
for line in ("HCT116", "CACO2", "HT29"):
    df = pd.read_csv(HERE / f"data/raw/GSE327208_{line}_count.tsv.gz", sep="\t", index_col=0)
    cpm = df / df.sum() * 1e6
    ctrl, ko = cpm[["N_1", "N_2"]].mean(axis=1), cpm[["MHF_1", "MHF_2"]].mean(axis=1)
    keep = (ctrl >= 1) | (ko >= 1)
    lfc = np.log2((ko[keep] + 0.5) / (ctrl[keep] + 0.5))
    dec = pd.qcut(ctrl[keep].rank(method="first"), 10, labels=False)  # decile by control CPM (rank-based; ties broken by order)
    for name, mem in sets.items():
        m = lfc.index.isin(list(mem))
        obs = lfc[m].mean()
        acc = np.zeros(NP)
        for d in range(10):
            pool = lfc[dec == d].values
            k = int((m & (dec == d).values).sum())
            if k:
                acc += np.array([RS.choice(pool, k, replace=False).sum() for _ in range(NP)])
        null = acc / m.sum()
        z = (obs - null.mean()) / null.std(ddof=1)
        out[f"{line}|{name}"] = dict(z_independent=round(float(z), 2), z_analysis_py=round(float(S[line][name]["z"]), 2), n=int(m.sum()))
(HERE / "results/independent_check.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
for k, v in out.items(): print(k, v)
