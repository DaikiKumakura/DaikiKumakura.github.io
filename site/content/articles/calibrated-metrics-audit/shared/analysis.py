"""Do evaluation metrics separate a technical duplicate from a mean baseline? (Wessels et al. Cas13 Perturb-seq, scPerturb)
Plan: analysis-plan.md (fixed before computing). Run: python analysis.py  (numpy, scipy, anndata). Needs data/raw/WesselsSatija2023.h5ad."""
import csv
import json
from pathlib import Path

import anndata as ad
import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
OUT.mkdir(exist_ok=True)
SEED, NSPLIT, MIN_CELLS, TOPK = 20261012, 10, 50, 50
METRICS = ["mse", "pearson_all", "pearson_top50", "wmse", "nir"]
rng = np.random.default_rng(SEED)

a = ad.read_h5ad(HERE / "data/raw/WesselsSatija2023.h5ad")
X = a.X.tocsr().astype(np.float32)
assert X.shape == (30707, 21052)
tot = np.asarray(X.sum(1)).ravel()
X = X.multiply(1e4 / tot[:, None]).tocsr()
X.data = np.log1p(X.data)
frac = np.asarray((X > 0).mean(0)).ravel()
G = np.where(frac >= 0.01)[0]
X = X[:, G].tocsr()
lab = a.obs["perturbation"].astype(str).values
cnt = {l: int((lab == l).sum()) for l in set(lab)}
perts = sorted(l for l, n in cnt.items() if l != "control" and n >= MIN_CELLS)
Q = len(perts)
print("genes", len(G), "perturbations", Q, "control cells", cnt["control"])


def dense(label):
    return X[np.where(lab == label)[0]].toarray()


xc = dense("control")
mu_c, var_c, n_c = xc.mean(0), xc.var(0, ddof=1), xc.shape[0]
full, pval, top, Atab, Btab = {}, {}, {}, np.empty((NSPLIT, Q, len(G)), np.float32), np.empty((NSPLIT, Q, len(G)), np.float32)
F = np.empty((Q, len(G)), np.float32)
VSUM, NHALF, NFULL = np.zeros(Q), np.zeros(Q), np.zeros(Q)
for i, p in enumerate(perts):
    xp = dense(p)
    n = xp.shape[0]
    mu, var = xp.mean(0), xp.var(0, ddof=1)
    F[i] = mu
    VSUM[i], NHALF[i], NFULL[i] = var.sum(), n // 2, n
    se = np.sqrt(var / n + var_c / n_c)
    t = np.divide(mu - mu_c, se, out=np.zeros_like(se), where=se > 0)
    pv = 2 * stats.norm.sf(np.abs(t))
    pval[p] = pv
    top[p] = np.argsort(pv)[:TOPK]
    for s in range(NSPLIT):
        perm = rng.permutation(n)
        h = n // 2
        Atab[s, i] = xp[perm[:h]].mean(0)
        Btab[s, i] = xp[perm[h:2 * h]].mean(0)
D = F - mu_c  # full-cell delta
effect = np.linalg.norm(D, axis=1)
genes_of = [set(p.split("_")) for p in perts]
share = np.array([[bool(genes_of[i] & genes_of[j]) for j in range(Q)] for i in range(Q)])
tot_sum = F.sum(0)
n_clean = Q - share.sum(1)
W = {p: (-np.log10(np.maximum(pval[p], 1e-300))) for p in perts}
W = {p: w / w.sum() for p, w in W.items()}


def corr(u, v):
    if u.std() == 0 or v.std() == 0:
        return 0.0
    return float(np.corrcoef(u, v)[0, 1])


def scores(i, pred, truth, DB):
    """Higher is better for all returned values. DB: (Q,G) deltas of every perturbation's held-out half."""
    d_pred, d_true = pred - mu_c, truth - mu_c
    p = perts[i]
    dist = ((d_pred[None, :] - DB) ** 2).mean(1)
    rank = 1 + np.sum(dist < dist[i]) + 0.5 * (np.sum(dist == dist[i]) - 1)
    return dict(mse=-float(((pred - truth) ** 2).mean()), pearson_all=corr(d_pred, d_true),
                pearson_top50=corr(d_pred[top[p]], d_true[top[p]]), wmse=-float((W[p] * (pred - truth) ** 2).sum()),
                nir=float(1 - (rank - 1) / (Q - 1)))


rows = []
for s in range(NSPLIT):
    DB = Btab[s] - mu_c
    for i, p in enumerate(perts):
        truth = Btab[s, i]
        base = {"dup": Atab[s, i], "mean": (tot_sum - F[i]) / (Q - 1), "ctrl": mu_c}
        if n_clean[i] >= 5:
            base["mean_clean"] = (tot_sum - share[i] @ F) / n_clean[i]
        for b, pred in base.items():
            sc = scores(i, pred, truth, DB)
            rows.append(dict(split=s, pert=p, base=b, effect=float(effect[i]), n_cells=cnt[p], **sc))

by = {}
for r in rows:
    by.setdefault((r["split"], r["pert"]), {})[r["base"]] = r
ter = np.quantile(effect, [1 / 3, 2 / 3])
out = {"seed": SEED, "n_split": NSPLIT, "n_pert": Q, "n_genes": int(len(G)), "n_clean_median": float(np.median(n_clean)),
       "n_pert_with_clean_mean": int((n_clean >= 5).sum()), "metrics": {}}


def summarize(vs, ref):
    res = {}
    for m in METRICS:
        pairs = [(v["dup"][m], v[ref][m]) for v in vs if ref in v]
        win = np.mean([x > y for x, y in pairs])
        if m in ("mse", "wmse"):
            drf = [(-y - -x) / -y for x, y in pairs]  # (err_ref - err_dup)/err_ref
        else:
            drf = [(x - y) / (1 - y) for x, y in pairs if y < 1]
        res[m] = dict(win_rate=round(float(win), 3), median_drf=round(float(np.median(drf)), 3), n=len(pairs))
    return res


allv = list(by.values())
out["R1_R4_vs_mean"] = summarize(allv, "mean")
out["sens_a_vs_mean_clean"] = summarize(allv, "mean_clean")
out["R1_vs_ctrl"] = summarize(allv, "ctrl")
tcl = lambda v: int(np.searchsorted(ter, v["dup"]["effect"]))
out["R3_by_effect_tercile_vs_mean"] = {f"tercile{k + 1}": summarize([v for v in allv if tcl(v) == k], "mean") for k in range(3)}
out["R3_tercile_effect_bounds"] = [round(float(x), 3) for x in ter]
# R5: control vs mean, who is better (per metric)
out["R5_mean_beats_ctrl_rate"] = {m: round(float(np.mean([v["mean"][m] > v["ctrl"][m] for v in allv])), 3) for m in METRICS}
out["R2_calibrated_metrics"] = [m for m in METRICS if out["R1_R4_vs_mean"][m]["win_rate"] >= 0.90]
# per-perturbation table (median across splits)
with open(OUT / "per_perturbation.csv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["pert", "n_cells", "effect_l2"] + [f"{m}_win_vs_mean" for m in METRICS] + [f"{m}_drf_vs_mean" for m in METRICS])
    for i, p in enumerate(perts):
        vs = [by[(s, p)] for s in range(NSPLIT)]
        def drf1(v, m):
            x, y = v["dup"][m], v["mean"][m]
            if m in ("mse", "wmse"):
                return (-y - -x) / -y
            return (x - y) / (1 - y) if y < 1 else float("nan")
        w.writerow([p, cnt[p], round(float(effect[i]), 3)] + [round(float(np.mean([v["dup"][m] > v["mean"][m] for v in vs])), 2) for m in METRICS]
                   + [round(float(np.nanmedian([drf1(v, m) for v in vs])), 3) for m in METRICS])
# Exploratory (added after seeing the main result; not in the fixed plan): does a simple noise-vs-shift criterion predict the MSE win?
mean_loo = (tot_sum - F) / (Q - 1)
shift2 = ((F - mean_loo) ** 2).sum(1) - VSUM / NFULL  # bias-corrected squared shift of the perturbation from the mean baseline
crit = shift2 > VSUM / NHALF  # dup beats mean on MSE iff shift^2 > sum(var)/h  (expected values)
obs_win = np.array([np.mean([by[(s, p)]["dup"]["mse"] > by[(s, p)]["mean"]["mse"] for s in range(NSPLIT)]) > 0.5 for p in perts])
out["exploratory_mse_criterion"] = dict(agree=round(float(np.mean(crit == obs_win)), 3), crit_true=int(crit.sum()), obs_true=int(obs_win.sum()),
                                        both=int((crit & obs_win).sum()), n=int(Q))
with open(OUT / "mse_criterion.csv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["pert", "n_cells", "shift2_corrected", "noise_half", "criterion_true", "observed_majority_win"])
    for i, p in enumerate(perts):
        w.writerow([p, int(NFULL[i]), round(float(shift2[i]), 3), round(float(VSUM[i] / NHALF[i]), 3), int(crit[i]), int(obs_win[i])])
# Added after review: perturbation-level bootstrap for the win rates (the 10 splits of one perturbation are not independent) and the base rate of the MSE criterion
brng = np.random.default_rng(SEED + 1)
winmat = {m: np.array([np.mean([by[(s, p)]["dup"][m] > by[(s, p)]["mean"][m] for s in range(NSPLIT)]) for p in perts]) for m in METRICS}
out["bootstrap_win_ci_perturbation_level"] = {}
for m in METRICS:
    bs = [winmat[m][brng.integers(0, Q, Q)].mean() for _ in range(5000)]
    out["bootstrap_win_ci_perturbation_level"][m] = [round(float(x), 3) for x in np.percentile(bs, [2.5, 50, 97.5])]
out["exploratory_mse_criterion"]["base_rate_always_win"] = round(float(obs_win.mean()), 3)
(OUT / "summary.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, ensure_ascii=False))
