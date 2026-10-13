"""Independent re-computation (separate code path: grid posterior and Monte Carlo trial simulation instead of closed forms).
Run: python independent_check.py (numpy, scipy). Compares with results/summary.json (analysis.py)."""
import csv
import json
import math
from pathlib import Path

import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
R = {r["arm"]: r for r in csv.DictReader(open(HERE / "data/fvc_arms.csv", encoding="utf-8"))}
S = json.load(open(HERE / "results/summary.json", encoding="utf-8"))
rng = np.random.default_rng(4242)
g = lambda a, k: float(R[a][k])
# MAR difference by Monte Carlo over the two arms' published CIs (normal, independent arms)
se = lambda a: (g(a, "mi_ci_hi") - g(a, "mi_ci_lo")) / (2 * 1.959964)
d_mar, se_mar = g("r60qd", "mi_mean_ml") - g("placebo", "mi_mean_ml"), math.hypot(se("r60qd"), se("placebo"))
out = {"mar_diff": [round(d_mar, 1), round(se_mar, 1)]}
# tipping point: delta at which the point estimate of the difference is 0, by root finding on a grid
frac = int(R["r60qd"]["n_missing_w12"]) / int(R["r60qd"]["n_randomized"])
dg = np.linspace(0, 400, 400001)
diff = d_mar - frac * dg
out["delta_point_zero"] = round(float(dg[np.argmin(np.abs(diff))]), 1)
p = stats.norm.cdf(diff / se_mar)
out["delta_p0.80"] = round(float(dg[np.argmin(np.abs(p - 0.80))]), 1)
# grid posterior for the true difference with the N(0,150^2) prior (no closed form used)
grid = np.linspace(-600, 600, 24001)
def assurance(dhat, n_enrolled, sd=150.0):
    post = stats.norm.pdf(grid, 0, 150.0) * stats.norm.pdf(dhat, grid, se_mar)
    post /= post.sum()
    se_trial = sd * math.sqrt(2 / (0.7 * n_enrolled))
    draws = rng.choice(grid, size=400000, p=post)
    est = rng.normal(draws, se_trial)
    return round(float(np.mean(est / se_trial > 1.959964)), 3), round(float(post[grid > 0].sum()), 3)
res = {}
for n in (30, 51, 100, 200, 400):
    res[str(n)] = {"MAR": assurance(d_mar, n)[0], "delta100": assurance(d_mar - frac * 100, n)[0]}
out["assurance_mc"] = res
out["p_delta_gt0_grid"] = {"MAR": assurance(d_mar, 51)[1], "delta100": assurance(d_mar - frac * 100, 51)[1]}
out["analysis_py"] = {"delta_point_zero": S["E4_tipping"]["delta_point_estimate_zero"], "delta_p0.80": S["E4_tipping"]["delta_p_gt0_0p80"],
                      "assurance_MAR": S["E8_assurance_sd150_prior_sd150"]["MAR_mi"]["assurance"], "assurance_delta100": S["E8_assurance_sd150_prior_sd150"]["delta100"]["assurance"]}
(HERE / "results/independent_check.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1))
