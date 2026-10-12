"""Re-analysis of public RNA-seq (GSE327208): triple knockdown of MYB, HDAC2, FOXA2 in three colorectal cancer lines.
Plan: analysis-plan.md (fixed before computing). Run: python analysis.py  (numpy, scipy)."""
import csv
import gzip
import json
from pathlib import Path

import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
RAW, GS, OUT = HERE / "data/raw", HERE / "data/genesets", HERE / "results"
OUT.mkdir(exist_ok=True)
SEED, NPERM = 20261012, 10000
LINES = ["HCT116", "CACO2", "HT29"]
TARGETS = ["MYB", "HDAC2", "FOXA2"]
MAIN = ["Large Intestine-mature Enterocyte", "Large Intestine-immature Enterocyte"]
HALL = ["HALLMARK_MYC_TARGETS_V1", "HALLMARK_MYC_TARGETS_V2", "HALLMARK_E2F_TARGETS", "HALLMARK_G2M_CHECKPOINT", "HALLMARK_WNT_BETA_CATENIN_SIGNALING"]
GUT = ["Large Intestine-intestinal Crypt Stem Cell", "Large Intestine-goblet Cell", "Large Intestine-transit Amplifying Cell Of Large Intestine",
       "Large Intestine-paneth Cell Of Epithelium Of Large Intestine", "Large Intestine-intestinal Enteroendocrine Cell"]
rng = np.random.default_rng(SEED)


def load(line):
    rows = [l.split("\t") for l in gzip.open(RAW / f"GSE327208_{line}_count.tsv.gz", "rt").read().splitlines()]
    assert rows[0][1:] == ["N_1", "N_2", "MHF_1", "MHF_2"], rows[0]
    genes = [r[0] for r in rows[1:]]
    assert len(set(genes)) == len(genes)
    return genes, np.array([[int(x) for x in r[1:]] for r in rows[1:]], dtype=float)


def read_sets():
    sets = {}
    for l in (GS / "hallmark_v2023.2.gmt").read_text(encoding="utf-8").splitlines():
        p = l.split("\t")
        sets[p[0]] = set(p[2:])
    for f, pre in (("enrichr_Tabula_Sapiens.txt", ""), ("enrichr_PanglaoDB_Augmented_2021.txt", "Panglao:")):
        for l in (GS / f).read_text(encoding="utf-8").splitlines():
            p = l.split("\t")
            sets[pre + p[0]] = {g.split(",")[0] for g in p[2:] if g}
    return sets


SETS = read_sets()


def set_scores(lfc, genes_idx, members, strata, nperm, ctrl_cpm_decile):
    """Mean log2FC of members; null by decile-stratified resampling of the analysed genes."""
    idx = [genes_idx[g] for g in sorted(members) if g in genes_idx]
    if len(idx) < 10:
        return None
    obs = lfc[idx].mean()
    dec = ctrl_cpm_decile[idx]
    null = np.empty(nperm)
    pools = {d: strata[d] for d in np.unique(dec)}
    counts = {d: int((dec == d).sum()) for d in pools}
    for k in range(nperm):
        pick = np.concatenate([rng.choice(pools[d], size=counts[d], replace=False if counts[d] <= len(pools[d]) else True) for d in pools])
        null[k] = lfc[pick].mean()
    z = (obs - null.mean()) / null.std(ddof=1)
    p = (1 + np.sum(np.abs(null - null.mean()) >= abs(obs - null.mean()))) / (nperm + 1)
    return dict(n=len(idx), score=float(obs), z=float(z), p=float(p))


out = {"seed": SEED, "nperm": NPERM, "e1_targets": {}, "e2": {}, "e3_rank": {}, "r4_pairs": {}, "r5_spearman": {}}
LFC = {}
ALLZ = {}
for line in LINES:
    genes, c = load(line)
    cpm = c / c.sum(axis=0) * 1e6
    ctrl, ko = cpm[:, :2].mean(1), cpm[:, 2:].mean(1)
    gi = {g: i for i, g in enumerate(genes)}
    out["e1_targets"][line] = {t: dict(ctrl_cpm=round(float(ctrl[gi[t]]), 2), kd_cpm=round(float(ko[gi[t]]), 2),
                                       expressed=bool(ctrl[gi[t]] >= 2), knockdown_pct=round(float(100 * (1 - ko[gi[t]] / ctrl[gi[t]])), 1) if ctrl[gi[t]] > 0 else None,
                                       kd_pct_by_replicate=[round(float(100 * (1 - cpm[gi[t], 2 + r] / cpm[gi[t], r])), 1) if cpm[gi[t], r] > 0 else None for r in (0, 1)]) for t in TARGETS}
    keep = np.where((ctrl >= 1) | (ko >= 1))[0]
    lfc_all = np.log2((ko + 0.5) / (ctrl + 0.5))
    lfc_pair = [np.log2((cpm[:, 2 + r] + 0.5) / (cpm[:, r] + 0.5)) for r in (0, 1)]
    LFC[line] = (genes, lfc_all, keep)
    sub_gi = {genes[i]: j for j, i in enumerate(keep)}
    sub, subp = lfc_all[keep], [p[keep] for p in lfc_pair]
    edges = np.quantile(ctrl[keep], np.linspace(0, 1, 11)[1:-1])
    dec = np.searchsorted(edges, ctrl[keep])
    strata = {d: np.where(dec == d)[0] for d in range(10)}
    res, pairs = {}, {}
    names = [n for n in SETS if n in MAIN + HALL + ["Panglao:Enterocytes"]]
    for n in names:
        res[n] = set_scores(sub, sub_gi, SETS[n], strata, NPERM, dec)
        pairs[n] = [float(subp[r][[sub_gi[g] for g in sorted(SETS[n]) if g in sub_gi]].mean()) for r in (0, 1)]
    out["e2"][line] = res
    out["r4_pairs"][line] = pairs
    # E3: all Tabula Sapiens sets, z (fewer permutations for speed)
    zs = {}
    for n, mem in SETS.items():
        if n.startswith("Panglao:") or n.startswith("HALLMARK"):
            continue
        r = set_scores(sub, sub_gi, mem, strata, 1000, dec)
        if r and r["n"] >= 15:
            zs[n] = r["z"]
    order = sorted(zs, key=lambda k: -zs[k])
    ALLZ[line] = zs
    out["e3_rank"][line] = {"n_sets": len(zs), **{n: dict(z=round(zs[n], 2), rank=order.index(n) + 1, top_pct=round(100 * (order.index(n) + 1) / len(zs), 1)) for n in MAIN + GUT if n in zs},
                            "top5": [(k, round(zs[k], 2)) for k in order[:5]], "bottom5": [(k, round(zs[k], 2)) for k in order[-5:]]}
    out["e2_n_analysed_genes"] = out.get("e2_n_analysed_genes", {}) | {line: int(len(keep))}
# R5: Spearman of gene-level log2FC between lines
for a, b in (("HCT116", "CACO2"), ("HCT116", "HT29"), ("CACO2", "HT29")):
    ga, la, ka = LFC[a]
    gb, lb, kb = LFC[b]
    common = sorted(set(ga[i] for i in ka) & set(gb[i] for i in kb))
    da, db = {g: la[i] for i, g in enumerate(ga)}, {g: lb[i] for i, g in enumerate(gb)}
    rho = stats.spearmanr([da[g] for g in common], [db[g] for g in common])
    out["r5_spearman"][f"{a}_{b}"] = dict(n_genes=len(common), rho=round(float(rho.statistic), 3))
# decision rules
e2, e3 = out["e2"], out["e3_rank"]
m = MAIN[0]
out["rules"] = {
    "R1_enterocyte_up_all_lines": all(e2[l][m]["z"] > 2 and e2[l][m]["p"] < 0.05 for l in LINES),
    "R2_specific_top10pct_in_ge2_lines": sum(e3[l][m]["top_pct"] <= 10 for l in LINES) >= 2,
    "R3_proliferation_down_by_line": {l: all(e2[l][h]["z"] < -2 for h in ("HALLMARK_MYC_TARGETS_V1", "HALLMARK_E2F_TARGETS", "HALLMARK_G2M_CHECKPOINT")) for l in LINES},
    "R4_pair_sign_agree": {l: {n: (out["r4_pairs"][l][n][0] > 0) == (out["r4_pairs"][l][n][1] > 0) for n in [m] + HALL[:3]} for l in LINES},
}
with open(OUT / "e3_all_z.csv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["set"] + LINES)
    for n in ALLZ[LINES[0]]:
        w.writerow([n] + [f"{ALLZ[l][n]:.3f}" if n in ALLZ[l] else "" for l in LINES])
(OUT / "summary.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, ensure_ascii=False))
