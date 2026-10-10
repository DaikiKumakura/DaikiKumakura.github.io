"""Ivonescimab dose-evidence audit, implemented exactly as in analysis-plan.md (fixed 2026-10-10).
E1: PK check against published cohort means, PD-1 occupancy at trough, interval extrapolation.
E2: Bayesian hierarchical logistic dose-response of ORR (Metropolis within Gibbs, 4 chains).
E3: sample size for a randomized 10 vs 20 mg/kg Q3W comparison.
Run: python analysis.py   (writes results/*.csv, results/summary.json)
"""
import csv
import json
import math
from pathlib import Path

import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
D, R = HERE / "data", HERE / "results"
R.mkdir(exist_ok=True)
SEED = 20261010
rng = np.random.default_rng(SEED)
expit = lambda z: 1 / (1 + np.exp(-z))
logit = lambda p: np.log(p / (1 - p))
out = {}


def read(name):
    with open(D / name, newline="") as f:
        return list(csv.DictReader(f))


# ------------------------------------------------------------------ E1
pk = read("pk_cohorts.csv")
f = lambda r, k: float(r[k])
rows, ok_cmin, ok_cavg = [], 0, 0
for r in pk:
    dose = f(r, "dose_mgkg") * f(r, "weight_median_kg")
    cl, v, tau = f(r, "cl_single_mean"), f(r, "vz_single_mean"), f(r, "interval_d")
    k = cl / v
    cmin = dose / v * math.exp(-k * tau) / (1 - math.exp(-k * tau))
    cavg = dose / (cl * tau)
    e_min = cmin / f(r, "cmin_ss_mean") - 1
    e_avg = cavg / f(r, "cavg_ss_mean") - 1
    ok_cmin += abs(e_min) <= 0.35
    ok_cavg += abs(e_avg) <= 0.20
    rows.append(dict(cohort=r["cohort"], dose_mg=round(dose, 1), cmin_pred=round(cmin, 1), cmin_obs=f(r, "cmin_ss_mean"),
                     cmin_err_pct=round(100 * e_min, 1), cavg_pred=round(cavg, 1), cavg_obs=f(r, "cavg_ss_mean"),
                     cavg_err_pct=round(100 * e_avg, 1)))
with open(R / "pk_check.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
pk_pass = ok_cmin >= 5 and ok_cavg >= 5
out["pk_check"] = {"cmin_within_35pct": int(ok_cmin), "cavg_within_20pct": int(ok_cavg), "of": len(pk), "criterion_met": bool(pk_pass)}

ro = read("ro_trough.csv")
cm = [f(r, "cmin_ss_ugml") for r in ro]
rv = [f(r, "ro_mean_pct") for r in ro]
out["ro_trough"] = {"cmin_min": min(cm), "cmin_max": max(cm), "cmin_fold_range": round(max(cm) / min(cm), 1),
                    "ro_cohort_mean_min": min(rv), "ro_cohort_mean_max": max(rv)}

# interval extrapolation (only if the PK check passed)
n1 = np.array([f(r, "n_single") for r in pk])
wavg = lambda key: float(np.sum(n1 * np.array([f(r, key) for r in pk])) / n1.sum())
cl0, v0 = wavg("cl_single_mean"), wavg("vz_single_mean")
cv_cl = float(np.sum(n1 * np.array([f(r, "cl_single_sd") / f(r, "cl_single_mean") for r in pk])) / n1.sum())
cv_v = float(np.sum(n1 * np.array([f(r, "vz_single_sd") / f(r, "vz_single_mean") for r in pk])) / n1.sum())
out["pk_typical"] = {"cl_L_per_day": round(cl0, 3), "v_L": round(v0, 2), "cv_cl_computed": round(cv_cl, 3), "cv_v_computed": round(cv_v, 3),
                     "cv_used": {"cl": 0.23, "v": 0.20}}
THRESH = 10.3  # lowest tested steady-state trough (3 mg/kg Q2W), ug/mL
N_SIM = 10000
cl_s = cl0 * np.exp(rng.normal(-0.5 * np.log(1 + 0.23**2), np.sqrt(np.log(1 + 0.23**2)), N_SIM))
v_s = v0 * np.exp(rng.normal(-0.5 * np.log(1 + 0.20**2), np.sqrt(np.log(1 + 0.20**2)), N_SIM))
ext = []
if pk_pass:
    for dose_mgkg in (10, 20):
        for tau in (14, 21, 28, 35, 42):
            dose = dose_mgkg * 56.0
            k = cl_s / v_s
            cmin = dose / v_s * np.exp(-k * tau) / (1 - np.exp(-k * tau))
            ext.append(dict(dose_mgkg=dose_mgkg, interval_d=tau, cmin_median=round(float(np.median(cmin)), 1),
                            cmin_p05=round(float(np.percentile(cmin, 5)), 1), cmin_p95=round(float(np.percentile(cmin, 95)), 1),
                            p_below_tested_min=round(float(np.mean(cmin < THRESH)), 3)))
    with open(R / "interval_extrapolation.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(ext[0]))
        w.writeheader()
        w.writerows(ext)
out["interval_extrapolation"] = ext

# ------------------------------------------------------------------ E2
orr = read("orr_by_dose.csv")
settings = sorted({r["trial_id"] for r in orr})
sid = {s: i for i, s in enumerate(settings)}
S = len(settings)


def build(rows):
    wi = np.array([float(r["dose_mgkg"]) / (float(r["interval_d"]) / 7) for r in rows])
    return (np.array([sid[r["trial_id"]] for r in rows]), np.log2(wi / (10 / 3)), np.array([int(r["n"]) for r in rows]),
            np.array([int(r["responders"]) for r in rows]))


def logpost(theta, s, x, n, y):
    a, z, mu, lt = theta[:S], theta[S:2 * S], theta[2 * S], theta[2 * S + 1]
    tau = math.exp(lt)
    b = mu + tau * z
    eta = a[s] + b[s] * x
    ll = np.sum(y * eta - n * np.logaddexp(0, eta))
    lp = (-0.5 * np.sum(a**2) / 4 - 0.5 * np.sum(z**2) - 0.5 * mu**2
          - 0.5 * (tau / 0.5) ** 2 + lt)  # a~N(0,2^2), z~N(0,1), mu~N(0,1), tau~HalfNormal(0.5) with log-Jacobian
    return ll + lp


def run_chain(rows, seed, n_iter=4000, burn=1000):
    s, x, n, y = build(rows)
    r_ = np.random.default_rng(seed)
    d = 2 * S + 2
    th = r_.normal(0, 0.3, d)
    th[2 * S + 1] = math.log(0.3)
    scale = np.full(d, 0.5)
    lp = logpost(th, s, x, n, y)
    draws = np.empty((n_iter, d))
    acc = np.zeros(d)
    for it in range(n_iter):
        for j in range(d):
            prop = th.copy()
            prop[j] += r_.normal(0, scale[j])
            lp2 = logpost(prop, s, x, n, y)
            if math.log(r_.random()) < lp2 - lp:
                th, lp = prop, lp2
                acc[j] += 1
        if it < burn and (it + 1) % 100 == 0:
            rate = acc / (it + 1)
            scale *= np.where(rate < 0.2, 0.8, np.where(rate > 0.5, 1.25, 1.0))
        draws[it] = th
    return draws[burn:]


def rhat(chains):  # chains: (m, n)
    m, n = chains.shape
    w = chains.var(axis=1, ddof=1).mean()
    b = n * chains.mean(axis=1).var(ddof=1)
    return math.sqrt(((n - 1) / n * w + b / n) / w)


def ess(chains):  # chains: (m, n); Gelman et al. BDA3 multi-chain estimate, Geyer truncation
    m, n = chains.shape
    w = chains.var(axis=1, ddof=1).mean()
    b = n * chains.mean(axis=1).var(ddof=1)
    vhat = (n - 1) / n * w + b / n
    c = chains - chains.mean(axis=1, keepdims=True)
    f = np.fft.rfft(c, 2 * n, axis=1)
    acov = np.fft.irfft(f * np.conj(f), axis=1)[:, :n] / n
    rho = 1 - (w - acov.mean(axis=0)) / vhat
    tot = 0.0
    for k in range(0, n - 1, 2):
        pair = rho[k] + rho[k + 1]
        if pair < 0:
            break
        tot += pair
    return m * n / (-1 + 2 * tot)


def fit(rows, tag):
    ch = np.stack([run_chain(rows, SEED + 17 * c) for c in range(4)])  # (4, n, d)
    names = [f"a_{k}" for k in settings] + [f"z_{k}" for k in settings] + ["mu_b", "log_tau"]
    rh = {nm: rhat(ch[:, :, i]) for i, nm in enumerate(names)}
    allv = ch.reshape(-1, ch.shape[2])
    a, z, mu, lt = allv[:, :S], allv[:, S:2 * S], allv[:, 2 * S], allv[:, 2 * S + 1]
    tau = np.exp(lt)
    b = mu[:, None] + tau[:, None] * z
    b_new = rng.normal(mu, tau)
    base = logit(0.55)
    d_new = 100 * (expit(base + b_new) - 0.55)
    q = lambda v: [round(float(t), 3) for t in np.percentile(v, [2.5, 50, 97.5])]
    res = {"tag": tag, "max_rhat": round(max(rh.values()), 3),
           "ess_mu_b": round(float(ess(ch[:, :, 2 * S])), 0), "ess_log_tau": round(float(ess(ch[:, :, 2 * S + 1])), 0),
           "min_ess_all": round(float(min(ess(ch[:, :, i]) for i in range(ch.shape[2]))), 0), "mu_b": q(mu), "tau": q(tau), "p_mu_b_gt0": round(float(np.mean(mu > 0)), 3),
           "b_by_setting": {k: q(b[:, i]) for i, k in enumerate(settings)},
           "delta_orr_points_new_setting": q(d_new), "p_delta_ge_10": round(float(np.mean(d_new >= 10)), 3),
           "p_delta_le_minus10": round(float(np.mean(d_new <= -10)), 3)}
    p = res["p_mu_b_gt0"]
    res["verdict"] = ("supports 20 mg/kg Q3W gain" if p >= 0.90 else "points the other way" if p <= 0.10 else "inconclusive")
    return res, {"mu": mu, "tau": tau, "b_new": b_new, "d_new": d_new}


main, post = fit(orr, "main")
out["e2_main"] = main
sens = {}
sens["a_no_monotherapy"], _ = fit([r for r in orr if r["trial_id"] != "P1b_mono"], "a_no_mono")
sens["b_no_sclc"], _ = fit([r for r in orr if r["trial_id"] != "P1b_sclc"], "b_no_sclc")
sens["d_q3w_only"], _ = fit([r for r in orr if not (r["trial_id"] == "P1b_mono" and r["interval_d"] == "14")], "d_q3w_only")
# (c) wider tau prior: rerun with HalfNormal(1)
_orig = logpost


def logpost_wide(theta, s, x, n, y):
    return _orig(theta, s, x, n, y) + 0.5 * (math.exp(theta[2 * S + 1]) / 0.5) ** 2 - 0.5 * (math.exp(theta[2 * S + 1]) / 1.0) ** 2


logpost = logpost_wide
sens["c_tau_halfnormal1"], _ = fit(orr, "c_tau_wide")
logpost = _orig
out["e2_sensitivity"] = sens

# raw ORR with Clopper-Pearson, and crude per-setting 20 vs 10 comparisons
raw = []
for r in orr:
    n, y = int(r["n"]), int(r["responders"])
    lo = stats.beta.ppf(0.025, y, n - y + 1) if y > 0 else 0.0
    hi = stats.beta.ppf(0.975, y + 1, n - y) if y < n else 1.0
    raw.append(dict(trial_id=r["trial_id"], dose_mgkg=r["dose_mgkg"], interval_d=r["interval_d"], n=n, responders=y,
                    orr_pct=round(100 * y / n, 1), cp_lo=round(100 * lo, 1), cp_hi=round(100 * hi, 1), n_provenance=r["n_provenance"]))
with open(R / "orr_raw.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(raw[0]))
    w.writeheader()
    w.writerows(raw)
crude = {}
by = {}
for r in orr:
    by.setdefault(r["trial_id"], {})[(r["dose_mgkg"], r["interval_d"])] = (int(r["responders"]), int(r["n"]))
for t, d in by.items():
    if ("10", "21") in d and ("20", "21") in d:
        (y1, n1_), (y2, n2) = d[("10", "21")], d[("20", "21")]
        odds, p = stats.fisher_exact([[y2, n2 - y2], [y1, n1_ - y1]])
        crude[t] = dict(orr10=round(y1 / n1_, 3), orr20=round(y2 / n2, 3), diff_points=round(100 * (y2 / n2 - y1 / n1_), 1),
                        fisher_or=round(float(odds), 2), fisher_p=round(float(p), 3))
out["crude_20_vs_10_q3w"] = crude
# pooled chemotherapy-combination comparison (NSCLC phase 2, three cohorts) for reference
y10 = sum(int(r["responders"]) for r in orr if r["trial_id"].startswith("P2_") and r["dose_mgkg"] == "10")
n10 = sum(int(r["n"]) for r in orr if r["trial_id"].startswith("P2_") and r["dose_mgkg"] == "10")
y20 = sum(int(r["responders"]) for r in orr if r["trial_id"].startswith("P2_") and r["dose_mgkg"] == "20")
n20 = sum(int(r["n"]) for r in orr if r["trial_id"].startswith("P2_") and r["dose_mgkg"] == "20")
out["p2_pooled"] = {"orr10": f"{y10}/{n10}", "orr20": f"{y20}/{n20}"}

# ------------------------------------------------------------------ E3
za, zb, za1 = stats.norm.ppf(0.975), stats.norm.ppf(0.80), stats.norm.ppf(0.975)
p0 = 0.55
n_ni = math.ceil((za1 + zb) ** 2 * (2 * p0 * (1 - p0)) / 0.10**2)
sup = {}
for delta in (0.05, 0.10, 0.15):
    p1, p2 = p0, p0 + delta
    pbar = (p1 + p2) / 2
    sup[f"+{int(delta*100)}pts"] = math.ceil((za * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / delta**2)
out["e3_required_n_per_arm"] = {"noninferiority_margin10_true_diff0": n_ni, "detect_difference_80pct_power": sup}
d_new = post["d_new"] / 100  # change from 10 to 20 mg/kg (points/100), new setting
grid = []
for n in (50, 100, 200, 400, 800, 1600, 3200):
    pw_ni, pw_sup = [], []
    sel = rng.choice(len(d_new), 4000, replace=False)
    for dd in d_new[sel]:
        p20 = min(max(p0 + dd, 0.01), 0.99)  # true ORR at 20 mg/kg; 10 mg/kg = p0
        # non-inferiority of 10 vs 20: diff = p10 - p20, margin 0.10 (one-sided alpha 0.025)
        se = math.sqrt(p0 * (1 - p0) / n + p20 * (1 - p20) / n)
        pw_ni.append(1 - stats.norm.cdf((za1 * se - (p0 - p20 + 0.10)) / se))
        # superiority of 20 over 10, two-sided alpha 0.05
        pw_sup.append(1 - stats.norm.cdf((za * se - dd) / se))  # P(declare 20 mg/kg superior, two-sided alpha 0.05, upper side) for true difference dd
    grid.append(dict(n_per_arm=n, expected_power_noninferiority_10_vs_20=round(float(np.mean(pw_ni)), 3),
                     expected_power_to_show_20_superior=round(float(np.mean(pw_sup)), 3)))
with open(R / "sample_size_grid.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(grid[0]))
    w.writeheader()
    w.writerows(grid)
out["e3_expected_power_grid"] = grid
out["e3_asymptote"] = {"p_true_diff_lt_10pts": round(float(np.mean(post["d_new"] < 10)), 3), "p_true_diff_gt_0": round(float(np.mean(post["d_new"] > 0)), 3)}

np.savez(R / "posterior_draws.npz", mu=post["mu"], tau=post["tau"], d_new=post["d_new"])
# (e) added after review: mu_b prior sensitivity (N(0,0.5^2) and N(0,2^2)); runs after all other results so earlier random streams are unchanged
for sd_mu, tag in ((0.5, "e_mu_prior_sd0.5"), (2.0, "e_mu_prior_sd2")):
    def logpost_mu(theta, s, x, n, y, sd_mu=sd_mu):
        return _orig(theta, s, x, n, y) + 0.5 * theta[2 * S] ** 2 - 0.5 * (theta[2 * S] / sd_mu) ** 2
    logpost = logpost_mu
    out["e2_sensitivity"][tag], _ = fit(orr, tag)
logpost = _orig

(R / "summary.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2, ensure_ascii=False))
