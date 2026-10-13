"""Same metric check as analysis.py, for other scPerturb datasets, with a streaming (low-memory) group-sum engine.
Plan: analysis-plan.md and analysis-plan-addendum.md (fixed before computing).
Run: python analysis_stream.py <h5ad> <control_label> <tag> [nsplit]
Verified against analysis.py on the Wessels data (tag wessels_stream)."""
import json
import sys
from pathlib import Path

import anndata as ad
import h5py
import numpy as np
from scipy import sparse, stats

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
PATH, CTRL, TAG = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
NSPLIT = int(sys.argv[4]) if len(sys.argv) > 4 else 10
SEED, MIN_CELLS, TOPK = 20261012, 50, 50
METRICS = ["mse", "pearson_all", "pearson_top50", "wmse", "nir"]
rng = np.random.default_rng(SEED)

a = ad.read_h5ad(PATH, backed="r")
lab = a.obs["perturbation"].astype(str).values
n_cells, n_genes = a.shape
with h5py.File(PATH, "r") as h:
    xg = h["X"]
    enc = dict(xg.attrs).get("encoding-type", "dense") if isinstance(xg, h5py.Group) else "dense"
print(TAG, enc, "cells", n_cells, "genes", n_genes, flush=True)

# pass 0: row totals (all genes) and per-gene detection counts
rowtot = np.zeros(n_cells, np.float64)
nz = np.zeros(n_genes, np.int64)
if enc == "csc_matrix":
    with h5py.File(PATH, "r") as h:
        ip = h["X/indptr"][:]
        for c0 in range(0, n_genes, 2000):
            c1 = min(c0 + 2000, n_genes)
            d = h["X/data"][ip[c0]:ip[c1]]
            ix = h["X/indices"][ip[c0]:ip[c1]]
            np.add.at(rowtot, ix, d)
        nz = np.diff(ip)
else:
    for s in range(0, n_cells, 5000):
        ch = a.X[s:s + 5000]
        ch = ch.toarray() if hasattr(ch, "toarray") else np.asarray(ch)
        rowtot[s:s + 5000] = ch.sum(1)
        nz += (ch > 0).sum(0)
G = np.where(nz / n_cells >= 0.01)[0]
nG = len(G)
print("analysed genes", nG, flush=True)

cnt = {}
index = {}
for i, l in enumerate(lab):
    cnt[l] = cnt.get(l, 0) + 1
    index.setdefault(l, []).append(i)
perts = sorted(l for l, c in cnt.items() if l != CTRL and c >= MIN_CELLS)
Q = len(perts)
# group layout: 0 control; 1..Q full; then per split s, pert i: A, B
NGR = 1 + Q + 2 * NSPLIT * Q
rows_i, cols_i = [], []


def add(group, idx):
    rows_i.extend(idx)
    cols_i.extend([group] * len(idx))


add(0, index[CTRL])
nsel = np.zeros(NGR)
nsel[0] = len(index[CTRL])
for i, p in enumerate(perts):
    idx = np.array(sorted(index[p]))
    n = len(idx)
    add(1 + i, idx.tolist())
    nsel[1 + i] = n
    for s in range(NSPLIT):
        perm = rng.permutation(n)
        h = n // 2
        ga = 1 + Q + 2 * (s * Q + i)
        add(ga, idx[perm[:h]].tolist())
        add(ga + 1, idx[perm[h:2 * h]].tolist())
        nsel[ga] = nsel[ga + 1] = h
M = sparse.csr_matrix((np.ones(len(rows_i), np.float32), (rows_i, cols_i)), shape=(n_cells, NGR))
Mfull = M[:, :1 + Q].tocsr()
S = np.zeros((NGR, nG), np.float32)
SS = np.zeros((1 + Q, nG), np.float64)


def norm_block(x, rows):
    x = x * (1e4 / np.maximum(rowtot[rows], 1))[:, None].astype(np.float32)
    np.log1p(x, out=x)
    return x


if enc == "csc_matrix":
    with h5py.File(PATH, "r") as h:
        ip = h["X/indptr"][:]
        for b0 in range(0, nG, 400):
            cols = G[b0:b0 + 400]
            x = np.zeros((n_cells, len(cols)), np.float32)
            for jj, c in enumerate(cols):
                lo, hi = ip[c], ip[c + 1]
                x[h["X/indices"][lo:hi], jj] = h["X/data"][lo:hi]
            x = norm_block(x, np.arange(n_cells))
            S[:, b0:b0 + len(cols)] = (M.T @ x)
            SS[:, b0:b0 + len(cols)] = (Mfull.T @ (x.astype(np.float64) ** 2))
            print("block", b0, "/", nG, flush=True)
else:
    for s in range(0, n_cells, 5000):
        ch = a.X[s:s + 5000]
        ch = ch.toarray() if hasattr(ch, "toarray") else np.asarray(ch)
        x = norm_block(ch[:, G].astype(np.float32), np.arange(s, s + ch.shape[0]))
        S += (M[s:s + 5000].T @ x)
        SS += (Mfull[s:s + 5000].T @ (x.astype(np.float64) ** 2))
        if (s // 5000) % 10 == 0:
            print("rows", s, "/", n_cells, flush=True)

mu_c = (S[0] / nsel[0]).astype(np.float32)
var_c = (SS[0] - nsel[0] * mu_c.astype(np.float64) ** 2) / (nsel[0] - 1)
F = (S[1:1 + Q] / nsel[1:1 + Q, None]).astype(np.float32)
VAR = (SS[1:] - nsel[1:1 + Q, None] * F.astype(np.float64) ** 2) / (nsel[1:1 + Q, None] - 1)
NF = nsel[1:1 + Q]
NH = NF // 2
VSUM = VAR.sum(1)
W, TOP, NDEG = {}, {}, np.zeros(Q)
for i in range(Q):
    se = np.sqrt(VAR[i] / NF[i] + var_c / nsel[0])
    t = np.divide(F[i] - mu_c, se, out=np.zeros_like(se), where=se > 0)
    pv = 2 * stats.norm.sf(np.abs(t))
    NDEG[i] = (pv < 0.05 / nG).sum()
    w = -np.log10(np.maximum(pv, 1e-300))
    W[i] = w / w.sum()
    TOP[i] = np.argsort(pv)[:TOPK]
D = F - mu_c
effect = np.linalg.norm(D, axis=1)
genes_of = [set(p.replace("+", "_").split("_")) for p in perts]
tot_sum = F.sum(0, dtype=np.float64)
share = None
if any(len(g) > 1 for g in genes_of):
    gi = {}
    for i, g in enumerate(genes_of):
        for x in g:
            gi.setdefault(x, []).append(i)
    share = [set(j for x in g for j in gi[x]) for g in genes_of]
n_clean = np.array([Q - len(share[i]) if share else Q - 1 for i in range(Q)])


def corr(u, v):
    return 0.0 if u.std() == 0 or v.std() == 0 else float(np.corrcoef(u, v)[0, 1])


rows = []
for s in range(NSPLIT):
    ga0 = 1 + Q + 2 * s * Q
    A_ = np.empty((Q, nG), np.float32)
    B = np.empty((Q, nG), np.float32)
    for i in range(Q):
        A_[i] = S[ga0 + 2 * i] / nsel[ga0 + 2 * i]
        B[i] = S[ga0 + 2 * i + 1] / nsel[ga0 + 2 * i + 1]
    DB = B - mu_c
    sq = (DB.astype(np.float64) ** 2).sum(1)
    for i in range(Q):
        truth = B[i]
        base = {"dup": A_[i], "mean": ((tot_sum - F[i]) / (Q - 1)).astype(np.float32), "ctrl": mu_c}
        if share and n_clean[i] >= 5:
            sub = np.zeros(nG)
            for j in share[i]:
                sub += F[j]
            base["mean_clean"] = ((tot_sum - sub) / n_clean[i]).astype(np.float32)
        for b, pred in base.items():
            d_pred, d_true = pred - mu_c, truth - mu_c
            dist = float(d_pred.astype(np.float64) @ d_pred) - 2 * (DB @ d_pred) + sq
            rank = 1 + np.sum(dist < dist[i]) + 0.5 * (np.sum(dist == dist[i]) - 1)
            rows.append((s, i, b, dict(mse=-float(((pred - truth) ** 2).mean()), pearson_all=corr(d_pred, d_true),
                                       pearson_top50=corr(d_pred[TOP[i]], d_true[TOP[i]]), wmse=-float((W[i] * (pred - truth) ** 2).sum()),
                                       nir=float(1 - (rank - 1) / (Q - 1)))))
    print("split", s, flush=True)
by = {}
for s, i, b, sc in rows:
    by.setdefault((s, i), {})[b] = sc
allv = list(by.values())
ter = np.quantile(effect, [1 / 3, 2 / 3])


def summarize(vs, ref):
    res = {}
    for m in METRICS:
        pairs = [(v["dup"][m], v[ref][m]) for v in vs if ref in v]
        if not pairs:
            continue
        win = np.mean([x > y for x, y in pairs])
        drf = [(-y - -x) / -y for x, y in pairs] if m in ("mse", "wmse") else [(x - y) / (1 - y) for x, y in pairs if y < 1]
        res[m] = dict(win_rate=round(float(win), 3), median_drf=round(float(np.median(drf)), 3), n=len(pairs))
    return res


out = {"tag": TAG, "seed": SEED, "n_split": NSPLIT, "n_pert": Q, "n_genes": int(nG), "median_ndeg": float(np.median(NDEG)), "mean_ndeg": round(float(NDEG.mean()), 2),
       "median_cells": float(np.median(NF)), "R1_R4_vs_mean": summarize(allv, "mean"), "sens_a_vs_mean_clean": summarize(allv, "mean_clean"), "R1_vs_ctrl": summarize(allv, "ctrl")}
by_t = {k: [] for k in range(3)}
for (s, i), v in by.items():
    by_t[int(np.searchsorted(ter, effect[i]))].append(v)
out["R3_by_effect_tercile_vs_mean"] = {f"tercile{k + 1}": summarize(by_t[k], "mean") for k in range(3)}
brng = np.random.default_rng(SEED + 1)
winmat = {m: np.array([np.mean([by[(s, i)]["dup"][m] > by[(s, i)]["mean"][m] for s in range(NSPLIT)]) for i in range(Q)]) for m in METRICS}
out["bootstrap_win_ci_perturbation_level"] = {m: [round(float(x), 3) for x in np.percentile([winmat[m][brng.integers(0, Q, Q)].mean() for _ in range(5000)], [2.5, 50, 97.5])] for m in METRICS}
shift2 = ((F - (tot_sum - F) / (Q - 1)) ** 2).sum(1) - VSUM / NF
crit = shift2 > VSUM / NH
obs = winmat["mse"] > 0.5
out["exploratory_mse_criterion"] = dict(agree=round(float(np.mean(crit == obs)), 3), base_rate_always_win=round(float(obs.mean()), 3), crit_true=int(crit.sum()), obs_true=int(obs.sum()), n=Q)
(OUT / f"summary_{TAG}.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1))
