"""Rentosertib phase 2a (Nat Med 2025): robustness of the FVC signal to missing-data assumptions, from published summary values.
Plan: analysis-plan.md (fixed before computing). Run: python analysis.py (numpy, scipy)."""
import csv
import json
import math
from pathlib import Path

import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
OUT.mkdir(exist_ok=True)
SEED, NSIM = 20261013, 100000
Z = stats.norm.ppf(0.975)
rows = {r["arm"]: r for r in csv.DictReader(open(HERE / "data/fvc_arms.csv", encoding="utf-8"))}
f = lambda a, k: float(rows[a][k])
n = lambda a, k: int(rows[a][k])
ARMS = ["placebo", "r30qd", "r30bid", "r60qd"]
out = {"seed": SEED}

# arm-level quantities
A = {}
for a in ARMS:
    no, nr, nm = n(a, "n_observed_w12"), n(a, "n_randomized"), n(a, "n_missing_w12")
    se_obs_norm = (f(a, "obs_ci_hi") - f(a, "obs_ci_lo")) / (2 * Z)
    # The published observed-case CIs are normal-based (the 60 mg QD interval is reproduced exactly from the Source Data with z=1.96; see source_data_check.py),
    # so the standard error and SD are recovered with z, not with the t quantile used in the first version of this script.
    se_obs_t = se_obs_norm
    se_mi = (f(a, "mi_ci_hi") - f(a, "mi_ci_lo")) / (2 * Z)
    A[a] = dict(nr=nr, no=no, nm=nm, mo=f(a, "obs_mean_ml"), mmi=f(a, "mi_mean_ml"), se_obs_norm=se_obs_norm, se_obs_t=se_obs_t,
                sd_obs=se_obs_t * math.sqrt(no), se_mi=se_mi, m_missing_implied=(nr * f(a, "mi_mean_ml") - no * f(a, "obs_mean_ml")) / nm)
out["arms"] = {a: {k: round(v, 2) if isinstance(v, float) else v for k, v in A[a].items()} for a in ARMS}


def diff(m1, s1, m0, s0):
    d, se = m1 - m0, math.hypot(s1, s0)
    return dict(diff=round(d, 1), se=round(se, 1), ci=[round(d - Z * se, 1), round(d + Z * se, 1)], p_gt0=round(float(stats.norm.cdf(d / se)), 3))


# E1, E2, E7
out["E1_observed_vs_placebo"] = {a: diff(A[a]["mo"], A[a]["se_obs_norm"], A["placebo"]["mo"], A["placebo"]["se_obs_norm"]) for a in ARMS[1:]}
out["E2_mar_mi_vs_placebo"] = {a: diff(A[a]["mmi"], A[a]["se_mi"], A["placebo"]["mmi"], A["placebo"]["se_mi"]) for a in ARMS[1:]}
# E1 with Welch t (added after review; the plan used the normal approximation)
def welch(a1, a0):
    s1, s0 = A[a1]["sd_obs"] ** 2 / A[a1]["no"], A[a0]["sd_obs"] ** 2 / A[a0]["no"]
    d, se = A[a1]["mo"] - A[a0]["mo"], math.sqrt(s1 + s0)
    df = (s1 + s0) ** 2 / (s1**2 / (A[a1]["no"] - 1) + s0**2 / (A[a0]["no"] - 1))
    tc = stats.t.ppf(0.975, df)
    return dict(diff=round(d, 1), se=round(se, 1), df=round(df, 1), ci=[round(d - tc * se, 1), round(d + tc * se, 1)], p_two_sided=round(float(2 * stats.t.sf(abs(d / se), df)), 3))


out["E1_welch_t_vs_placebo"] = {a: welch(a, "placebo") for a in ARMS[1:]}
out["E7_60qd_vs_30bid_observed"] = diff(A["r60qd"]["mo"], A["r60qd"]["se_obs_norm"], A["r30bid"]["mo"], A["r30bid"]["se_obs_norm"])
# E3 implied mean of missing participants under MAR
out["E3_implied_missing_mean"] = {a: round(A[a]["m_missing_implied"], 1) for a in ARMS}
# E4 tipping point (delta applied to active arms' missing participants)
base = out["E2_mar_mi_vs_placebo"]["r60qd"]
frac = A["r60qd"]["nm"] / A["r60qd"]["nr"]
grid = []
for d in range(0, 301, 25):
    r = diff(A["r60qd"]["mmi"] - frac * d, A["r60qd"]["se_mi"], A["placebo"]["mmi"], A["placebo"]["se_mi"])
    grid.append(dict(delta_ml=d, diff=r["diff"], ci=r["ci"], p_gt0=r["p_gt0"]))
z80 = stats.norm.ppf(0.80)
out["E4_tipping"] = dict(grid=grid, delta_point_estimate_zero=round(base["diff"] / frac, 1),
                         delta_p_gt0_0p80=round((base["diff"] - z80 * base["se"]) / frac, 1), delta_p_gt0_0p50=round(base["diff"] / frac, 1),
                         note="delta is subtracted from the MAR-imputed values of the active arms' missing participants; SE kept as published")
# E5 jump to placebo observed mean (parametric simulation)
rng = np.random.default_rng(SEED)
pl = A["placebo"]
mu_ref = rng.normal(pl["mo"], pl["se_obs_t"], NSIM)  # placebo observed mean (uncertain)
arm_means = {}
for a in ARMS:
    s = A[a]
    mo = rng.normal(s["mo"], s["se_obs_t"], NSIM) if a != "placebo" else mu_ref
    imp = s["nm"] * mu_ref + math.sqrt(s["nm"]) * pl["sd_obs"] * rng.standard_normal(NSIM)
    arm_means[a] = (s["no"] * mo + imp) / s["nr"]
e5 = {}
for a in ARMS[1:]:
    d = arm_means[a] - arm_means["placebo"]
    e5[a] = dict(mean_diff=round(float(d.mean()), 1), ci=[round(float(np.percentile(d, 2.5)), 1), round(float(np.percentile(d, 97.5)), 1)], p_gt0=round(float((d > 0).mean()), 3),
                 arm_mean=round(float(arm_means[a].mean()), 1))
out["E5_jump_to_placebo_reference"] = dict(placebo_arm_mean=round(float(arm_means["placebo"].mean()), 1), arms=e5)
# E6 missingness imbalance
cp = lambda k, nn: [round(float(x), 3) for x in (stats.beta.ppf(0.025, k, nn - k + 1) if k else 0.0, stats.beta.ppf(0.975, k + 1, nn - k) if k < nn else 1.0)]
out["E6_missingness"] = {a: dict(missing=A[a]["nm"], n=A[a]["nr"], rate=round(A[a]["nm"] / A[a]["nr"], 3), ci=cp(A[a]["nm"], A[a]["nr"]),
                                 ae_discontinuation=n(a, "n_ae_discontinuation")) for a in ARMS}
tab = [[A["r60qd"]["nm"], A["r60qd"]["no"]], [A["placebo"]["nm"], A["placebo"]["no"]]]
fe = stats.fisher_exact(tab)
p1, p0 = tab[0][0] / A["r60qd"]["nr"], tab[1][0] / A["placebo"]["nr"]
se_rd = math.sqrt(p1 * (1 - p1) / A["r60qd"]["nr"] + p0 * (1 - p0) / A["placebo"]["nr"])
out["E6_fisher_60qd_vs_placebo"] = dict(odds_ratio=round(float(fe[0]), 2), p=round(float(fe[1]), 3), risk_diff=round(p1 - p0, 3), rd_ci_wald=[round(p1 - p0 - Z * se_rd, 3), round(p1 - p0 + Z * se_rd, 3)])
# E8 sample size and assurance
za, zb = Z, stats.norm.ppf(0.80)
ss = {}
for sd in (100, 150, 200):
    ss[f"sd{sd}"] = {f"delta{dl}": dict(n_observed_per_arm=math.ceil(2 * (za + zb) ** 2 * sd**2 / dl**2),
                                          n_enrolled_per_arm_at_30pct_missing=math.ceil(2 * (za + zb) ** 2 * sd**2 / dl**2 / 0.7)) for dl in (50, 100, 150)}
out["E8_required_n"] = ss
SD = 150.0
prior_sd = 150.0


def assurance(d_hat, se_hat):
    prec = 1 / prior_sd**2 + 1 / se_hat**2
    pm, ps = (d_hat / se_hat**2) / prec, math.sqrt(1 / prec)
    res = dict(posterior_mean=round(pm, 1), posterior_sd=round(ps, 1), p_delta_gt0=round(float(stats.norm.cdf(pm / ps)), 3), assurance={})
    for nn in (30, 51, 60, 100, 200, 400):
        se_trial = SD * math.sqrt(2 / (0.7 * nn))
        res["assurance"][str(nn)] = round(float(1 - stats.norm.cdf((Z * se_trial - pm) / math.hypot(ps, se_trial))), 3)
    return res


e5d = e5["r60qd"]
e5_se = (e5d["ci"][1] - e5d["ci"][0]) / (2 * Z)
out["E8_assurance_sd150_prior_sd150"] = {
    "MAR_mi": assurance(base["diff"], base["se"]),
    "delta100": assurance(diff(A["r60qd"]["mmi"] - frac * 100, A["r60qd"]["se_mi"], A["placebo"]["mmi"], A["placebo"]["se_mi"])["diff"], base["se"]),
    "jump_to_placebo": assurance(e5d["mean_diff"], e5_se),
}
# rules
e1, e2 = out["E1_observed_vs_placebo"]["r60qd"], out["E2_mar_mi_vs_placebo"]["r60qd"]
out["rules"] = dict(R1_observed_ci_excludes0=bool(e1["ci"][0] > 0), R2_mar_ci_excludes0=bool(e2["ci"][0] > 0), R4_jump_ci_excludes0=bool(e5d["ci"][0] > 0),
                    R3_implied_missing_mean_60qd=out["E3_implied_missing_mean"]["r60qd"], R3_observed_mean_60qd=A["r60qd"]["mo"],
                    robust=bool(e1["ci"][0] > 0 and e2["ci"][0] > 0 and e5d["ci"][0] > 0))
(OUT / "summary.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, ensure_ascii=False))
