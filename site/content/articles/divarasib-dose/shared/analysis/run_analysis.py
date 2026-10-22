"""Divarasib 400 mg vs lower doses: exposure-response for confirmed ORR estimated from public dose-group counts.

Run: python analysis/run_analysis.py -> results/*.csv, results/summary.json, figures/*.png
PK: one-compartment oral model scaled to the published 400 mg steady-state AUC and half-life; dose-proportional (assumed).
E-R: logit P(response) = a + b * ln(AUC_ss / AUC_ref). Group response rates are the average over virtual patients of each
dose group, and (a, b) are estimated on a grid by the binomial likelihood of the published counts (flat priors).
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import brentq
from scipy.stats import binom, norm

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261023
N = 4096
OKABE = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#0072B2", "#D55E00", "#CC79A7"]
A_GRID = np.linspace(-5, 4, 361)
B_GRID = np.linspace(-3, 8, 441)
DOSES = [50, 100, 200, 300, 400]


def main() -> None:
    inp = json.loads((ROOT / "analysis" / "inputs.json").read_text(encoding="utf-8"))
    pk = inp["pk_400mg_steady_state"]
    rng = np.random.default_rng(SEED)
    auc_mean, auc_sd = pk["AUC0_24_mean_sd_ng_h_ml"]
    cv = auc_sd / auc_mean
    s2 = np.log(1 + cv ** 2)
    auc400 = np.exp(rng.normal(np.log(auc_mean) - s2 / 2, np.sqrt(s2), N))  # per-patient AUC_ss at 400 mg
    out: dict = {"seed": SEED, "n": N, "auc_cv": round(cv, 3)}

    # One-compartment check of Cmax and accumulation implied by the published half-life and tmax.
    ke = np.log(2) / pk["t_half_single_dose_h"][0]
    ka = brentq(lambda k: np.log(k / ke) / (k - ke) - pk["tmax_median_h"], ke * 1.01, 50)  # single-dose tmax
    tau = 24.0
    cl = 400e6 / auc_mean  # mL/h
    v = cl / ke
    f_ss = lambda t: (400e6 * ka / (v * (ka - ke))) * (np.exp(-ke * t) / (1 - np.exp(-ke * tau)) - np.exp(-ka * t) / (1 - np.exp(-ka * tau)))
    tt = np.linspace(0, 24, 2401)
    css = f_ss(tt)
    out["pk_check"] = {"ka_per_h": round(float(ka), 3), "CL_F_L_h": round(cl / 1000, 2), "V_F_L": round(v / 1000, 1),
                       "Cmax_ss_typical_ng_ml": round(float(css.max()), 1), "Cmax_ss_published_mean": pk["Cmax_mean_sd_ng_ml"][0],
                       "accumulation_ratio_model": round(float(1 / (1 - np.exp(-ke * tau))), 2),
                       "accumulation_published": pk["accumulation_auc"][0]}

    mix = inp["lower_dose_mix_assumed"]
    mix = {k: v_ for k, v_ in mix.items() if k.isdigit()}
    wts = {int(k): v_ / sum(mix.values()) for k, v_ in mix.items()}

    def group_prob(a, b, doses_weights):
        # average response probability over virtual patients and the dose mix; AUC_ref = 400 mg mean
        p = 0.0
        for d, w in doses_weights.items():
            x = np.log(auc400 * d / 400 / auc_mean)
            p = p + w * np.mean(1 / (1 + np.exp(-(a + b * x))))
        return p

    # Precompute group probabilities on the grid efficiently: use quantiles of x to reduce cost.
    qx = np.log(np.quantile(auc400, (np.arange(200) + 0.5) / 200) / auc_mean)

    def gp(a, b, dw):
        return sum(w * np.mean(1 / (1 + np.exp(-(a[..., None] + b[..., None] * (qx + np.log(d / 400)))) ), axis=-1) for d, w in dw.items())

    AA, BB = np.meshgrid(A_GRID, B_GRID, indexing="ij")
    rows, curves = [], {}
    for tumour, cnt in [(k, v_) for k, v_ in inp["orr_nejm_2023"].items() if isinstance(v_, dict)]:
        for mix_name, dw in (("assumed mix (50:100:200 = 6:5:10)", wts), ("all lower = 200 mg", {200: 1.0}), ("all lower = 50 mg", {50: 1.0})):
            p400 = gp(AA, BB, {400: 1.0})
            plow = gp(AA, BB, dw)
            k4, n4 = cnt["400mg"]
            kl, nl = cnt["lower"]
            ll = binom.logpmf(k4, n4, np.clip(p400, 1e-9, 1 - 1e-9)) + binom.logpmf(kl, nl, np.clip(plow, 1e-9, 1 - 1e-9))
            post = np.exp(ll - ll.max()); post /= post.sum()
            # posterior draws
            idx = rng.choice(post.size, 4000, p=post.ravel())
            a_s, b_s = AA.ravel()[idx], BB.ravel()[idx]
            pred = {d: gp(a_s, b_s, {d: 1.0}) for d in DOSES}
            diff = pred[400] - pred[200]
            rows.append(dict(tumour=tumour, lower_dose_mix=mix_name, b_median=float(np.median(b_s)), b_2_5=float(np.percentile(b_s, 2.5)),
                             b_97_5=float(np.percentile(b_s, 97.5)), p_b_le_0=float(np.mean(b_s <= 0)),
                             **{f"orr_{d}": float(np.median(pred[d])) for d in DOSES},
                             orr_200_2_5=float(np.percentile(pred[200], 2.5)), orr_200_97_5=float(np.percentile(pred[200], 97.5)),
                             orr_400_2_5=float(np.percentile(pred[400], 2.5)), orr_400_97_5=float(np.percentile(pred[400], 97.5)),
                             diff_400_200_median=float(np.median(diff)), diff_2_5=float(np.percentile(diff, 2.5)), diff_97_5=float(np.percentile(diff, 97.5)),
                             p_diff_gt_10pt=float(np.mean(diff > 0.10)), p_diff_lt_5pt=float(np.mean(diff < 0.05))))
            if mix_name.startswith("assumed"):
                curves[tumour] = (a_s, b_s)
    df = pd.DataFrame(rows)
    (ROOT / "results").mkdir(exist_ok=True)
    df.round(4).to_csv(ROOT / "results" / "er_estimates.csv", index=False)
    out["er_estimates"] = df.round(4).to_dict(orient="records")

    # Sample size for a randomised 200 vs 400 mg comparison (two-sided 5%, 80% power), using posterior-median ORRs.
    ss = []
    for _, r in df[df.lower_dose_mix.str.startswith("assumed")].iterrows():
        p1, p2 = r["orr_400"], r["orr_200"]
        za, zb = norm.ppf(0.975), norm.ppf(0.8)
        d = abs(p1 - p2)
        n_sup = ((za + zb) ** 2 * (p1 * (1 - p1) + p2 * (1 - p2)) / d ** 2) if d > 0 else np.inf
        # non-inferiority with a 10-point margin, one-sided 2.5%, assuming true difference = posterior median
        margin = 0.10
        n_ni = ((za + zb) ** 2 * (p1 * (1 - p1) + p2 * (1 - p2)) / (margin - d) ** 2) if margin > d else np.inf
        ss.append(dict(tumour=r["tumour"], orr_400=p1, orr_200=p2, n_per_arm_superiority=float(np.ceil(n_sup)), n_per_arm_ni_10pt=float(np.ceil(n_ni))))
    sdf = pd.DataFrame(ss)
    sdf.round(3).to_csv(ROOT / "results" / "sample_size.csv", index=False)
    out["sample_size"] = sdf.round(3).to_dict(orient="records")
    (ROOT / "results" / "summary.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Figure: A) typical steady-state profiles for 200/400 mg; B) posterior predicted ORR vs dose with observed groups.
    (ROOT / "figures").mkdir(exist_ok=True)
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.6))
    for i, d in enumerate([100, 200, 400]):
        ax[0].plot(tt, css * d / 400, color=OKABE[i + 1], label=f"{d} mg once daily")
    ax[0].set_xlabel("Hours after dose (steady state)"); ax[0].set_ylabel("Divarasib (ng/mL), typical patient")
    ax[0].set_title("A. Steady-state profiles (dose-proportional, assumed)", fontsize=10); ax[0].legend(fontsize=8)
    dgrid = np.linspace(25, 400, 40)
    for j, (tumour, (a_s, b_s)) in enumerate(curves.items()):
        sub = rng.choice(len(a_s), 600, replace=False)
        pr = np.array([gp(a_s[sub], b_s[sub], {d: 1.0}) for d in dgrid])
        col = OKABE[2 + 3 * j]
        ax[1].plot(dgrid, np.median(pr, 1), color=col, label=f"{tumour} (n={inp['orr_nejm_2023'][tumour]['all'][1]}): posterior median")
        ax[1].fill_between(dgrid, np.percentile(pr, 2.5, 1), np.percentile(pr, 97.5, 1), color=col, alpha=0.2)
        cnt = inp["orr_nejm_2023"][tumour]
        ax[1].errorbar([400], [cnt["400mg"][0] / cnt["400mg"][1]], fmt="o", color=col)
        ax[1].errorbar([sum(int(k) * w for k, w in wts.items())], [cnt["lower"][0] / cnt["lower"][1]], fmt="s", color=col)
    ax[1].set_xlabel("Dose (mg once daily)"); ax[1].set_ylabel("Confirmed ORR (proportion)")
    ax[1].set_ylim(0, 1); ax[1].set_title("B. Estimated E-R (band: 95%); points: observed groups", fontsize=10)
    ax[1].legend(fontsize=8, loc="upper left")
    fig.tight_layout(); fig.savefig(ROOT / "figures" / "divarasib_er.png", dpi=150); plt.close(fig)
    print(json.dumps(out["pk_check"], indent=1)); print(df.round(3).to_string()); print(sdf.round(1).to_string())


if __name__ == "__main__":
    main()
