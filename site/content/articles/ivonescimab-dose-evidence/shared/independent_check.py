"""Independent check of the E2 hierarchical logistic model: deterministic grid integration (no MCMC).
Same model as analysis.py: responders ~ Bin(n, p), logit p = a_s + b_s*x, a_s~N(0,2^2), b_s~N(mu,tau^2), mu~N(0,1), tau~HalfNormal(0.5).
Run: python independent_check.py (numpy, scipy). Compare with results/summary.json."""
import csv
import json
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.special import expit, gammaln

HERE = Path(__file__).resolve().parent
rows = list(csv.DictReader(open(HERE / "data/orr_by_dose.csv", encoding="utf-8")))
settings = sorted({r["trial_id"] for r in rows})
A = np.linspace(-9, 9, 361)
B = np.linspace(-7, 7, 561)
dA, dB = A[1] - A[0], B[1] - B[0]
MU = np.linspace(-3, 3, 241)
TAU = np.linspace(0.004, 3.0, 400)
logLb = []  # per setting: log of integral over a of likelihood * prior(a), as a function of b
for s in settings:
    rs = [r for r in rows if r["trial_id"] == s]
    ll = np.zeros((len(A), len(B)))
    for r in rs:
        x = np.log2((float(r["dose_mgkg"]) / (float(r["interval_d"]) / 7)) / (10 / 3))
        n, y = int(r["n"]), int(r["responders"])
        eta = A[:, None] + B[None, :] * x
        ll += y * eta - n * np.logaddexp(0, eta)  # binomial coefficient is constant across parameters
    mx = ll.max()
    lik = np.exp(ll - mx) * stats.norm.pdf(A, 0, 2)[:, None] * dA
    logLb.append(np.log(lik.sum(0)) + mx)
logLb = np.array(logLb)  # (S, nB)
# integrate over b ~ N(mu, tau^2) by Gauss-Hermite quadrature on the interpolated per-setting profile (a grid over b under-resolves small tau)
zq, wq = np.polynomial.hermite_e.hermegauss(96)
wq = wq / wq.sum()
logpost = np.zeros((len(MU), len(TAU)))
for i, mu in enumerate(MU):
    for j, tau in enumerate(TAU):
        bq = np.clip(mu + tau * zq, B[0], B[-1])
        tot = 0.0
        for s in range(len(settings)):
            lq = np.interp(bq, B, logLb[s])
            m = lq.max()
            tot += m + np.log(np.sum(wq * np.exp(lq - m)))
        logpost[i, j] = tot
logpost += stats.norm.logpdf(MU, 0, 1)[:, None] + stats.halfnorm.logpdf(TAU, scale=0.5)[None, :]
post = np.exp(logpost - logpost.max())
post /= post.sum()
pm, pt = post.sum(1), post.sum(0)
q = lambda grid, p, qs: [round(float(np.interp(v, np.cumsum(p) / p.sum(), grid)), 3) for v in qs]
out = {"mu_b": q(MU, pm, [.025, .5, .975]), "tau": q(TAU, pt, [.025, .5, .975]), "p_mu_b_gt0": round(float(pm[MU > 0].sum()), 3)}
rng = np.random.default_rng(1)
idx = rng.choice(post.size, size=400000, p=post.ravel())
mu_s, tau_s = MU[idx // len(TAU)], TAU[idx % len(TAU)]
d = 100 * (expit(np.log(.55 / .45) + rng.normal(mu_s, tau_s)) - .55)
out["delta_orr_points_new_setting"] = [round(float(v), 2) for v in np.percentile(d, [2.5, 50, 97.5])]
out["p_delta_ge_10"], out["p_delta_le_minus10"] = round(float((d >= 10).mean()), 3), round(float((d <= -10).mean()), 3)
S = json.load(open(HERE / "results/summary.json", encoding="utf-8"))["e2_main"]
out["mcmc_in_analysis_py"] = {k: S[k] for k in ("mu_b", "tau", "p_mu_b_gt0", "delta_orr_points_new_setting", "p_delta_ge_10", "p_delta_le_minus10")}
(HERE / "results/independent_check.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1))
