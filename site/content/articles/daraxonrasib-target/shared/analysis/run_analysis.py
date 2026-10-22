"""Daraxonrasib: how many patients keep >=90% predicted tumour RAS-pathway (DUSP6) inhibition at trough, by dose?

Run: python analysis/run_analysis.py -> results/*.csv, results/summary.json, figures/*.png
PK: FDA review Table 59 (2-compartment, first-order absorption with lag, time-dependent relative F), IIV with CL-Vc covariance,
covariates at the reference patient. PD: preclinical tumour DUSP6 inhibition vs tumour concentration (EC50 54 nM, EC90 966 nM,
Imax 0.99, Hill exponent from EC90/EC50), tumour concentration = R x blood concentration (R from tumour/blood AUC ratio 4-7).
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261023
N = 4096
DAYS = 28
DOSES = [120, 160, 200, 240, 300]
R_VALUES = [1.0, 4.0, 5.5, 7.0]
OKABE = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#0072B2", "#D55E00", "#CC79A7"]


def simulate(dose_mg: float, p: dict, t_eval: np.ndarray) -> np.ndarray:
    """Whole-blood concentration (ng/mL), shape (n, len(t_eval)); QD dosing from t=0 for DAYS days."""
    n = len(p["CL"])
    k10, k12, k21 = p["CL"] / p["Vc"], p["Q"] / p["Vc"], p["Q"] / p["Vp"]

    def rhs(t, y):
        a, c, pp = y[:n], y[n:2 * n], y[2 * n:]
        return np.concatenate([-p["ka"] * a, p["ka"] * a - (k10 + k12) * c + k21 * pp, k12 * c - k21 * pp])
    y = np.zeros(3 * n)
    out = np.full((n, len(t_eval)), np.nan)
    for day in range(DAYS):
        t0 = 24.0 * day
        f = 1 - p["EM"] * day / (p["ET50"] + day)
        seg = [(t0, t0 + p["tlag"], False), (t0 + p["tlag"], t0 + 24.0, True)]
        for a_, b_, dosed in seg:
            if dosed:
                y[:n] += f * dose_mg * 1e6  # ng into depot
            m = (t_eval >= a_) & (t_eval < b_)
            te = np.unique(np.concatenate([t_eval[m], [b_]]))
            sol = solve_ivp(rhs, (a_, b_), y, t_eval=te, method="RK45", rtol=1e-7, atol=1e-3)
            idx = np.searchsorted(te, t_eval[m])
            out[:, m] = sol.y[n:2 * n][:, idx] / (p["Vc"][:, None] * 1000)
            y = sol.y[:, -1].copy()
    return out


def inhibition(c_blood_ng_ml: np.ndarray, r: float, pd_: dict, mw: float) -> np.ndarray:
    hill = np.log(9) / np.log(pd_["EC90_nM_tumor"] / pd_["EC50_nM_tumor"])
    c_t = r * c_blood_ng_ml / mw * 1000  # nM
    return pd_["Imax"] * c_t ** hill / (pd_["EC50_nM_tumor"] ** hill + c_t ** hill)


def main() -> None:
    inp = json.loads((ROOT / "analysis" / "inputs.json").read_text(encoding="utf-8"))
    pk, pd_, mw = inp["pk_table59"], inp["preclinical_pd"], inp["mw_g_mol"]
    rng = np.random.default_rng(SEED)
    om = pk["omega2"]
    cov = np.array([[om["CL"], om["cov_CL_Vc"], 0], [om["cov_CL_Vc"], om["Vc"], 0], [0, 0, om["ka"]]])
    eta = rng.multivariate_normal(np.zeros(3), cov, N)
    p = {"CL": pk["CL_L_h"] * np.exp(eta[:, 0]), "Vc": pk["Vc_L"] * np.exp(eta[:, 1]), "ka": pk["ka_per_h"] * np.exp(eta[:, 2]),
         "Q": np.full(N, pk["Q_L_h"]), "Vp": np.full(N, pk["Vp_L"]), "EM": pk["EM"], "ET50": pk["ET50_day"], "tlag": pk["tlag_h"]}
    t_last = np.linspace(24 * (DAYS - 1), 24 * DAYS - 1e-6, 241)
    out: dict = {"seed": SEED, "n": N, "hill": round(float(np.log(9) / np.log(pd_["EC90_nM_tumor"] / pd_["EC50_nM_tumor"])), 3)}
    rows, conc = [], {}
    for d in DOSES:
        pd_dose = dict(p)
        if d <= 160:  # Table 59: DOSE<=160 mg effect on ka, P = theta x (1 + 1.49)
            pd_dose["ka"] = p["ka"] * (1 + 1.49)
        c = simulate(d, pd_dose, t_last)
        conc[d] = c
        cmin, cmax, cavg = c[:, -1], c.max(1), c.mean(1)
        for r in R_VALUES:
            inh_tr = inhibition(cmin, r, pd_, mw)
            inh_avg = inhibition(c, r, pd_, mw).mean(1)
            rows.append(dict(dose_mg=d, tumor_blood_ratio=r, cmin_median=float(np.median(cmin)), cmax_median=float(np.median(cmax)),
                             auc24_median=float(np.median(cavg * 24)), trough_inhib_median=float(np.median(inh_tr)),
                             share_trough_ge90=float(np.mean(inh_tr >= 0.90)), share_trough_ge95=float(np.mean(inh_tr >= 0.95)),
                             share_avg_ge90=float(np.mean(inh_avg >= 0.90))))
    df = pd.DataFrame(rows)
    (ROOT / "results").mkdir(exist_ok=True)
    df.round(4).to_csv(ROOT / "results" / "target_attainment.csv", index=False)
    out["target_attainment"] = df.round(4).to_dict(orient="records")
    b = df[(df.dose_mg == 300) & (df.tumor_blood_ratio == 4.0)].iloc[0]
    out["benchmark_300mg_day28"] = {"cmax_median": round(b.cmax_median, 1), "auc24_median": round(b.auc24_median, 1),
                                    "fda_review_total_cmax_300mg": 391, "note": "FDA review states total Cmax at 300 mg 391 ng/mL (0.48 uM); model median vs reported value"}
    # Ratio R needed for the applicant's claim (100% >=90% at 300 mg): smallest R with >=99% of patients >=90% at trough.
    cmin300 = conc[300][:, -1]
    rr = np.linspace(1, 80, 1581)
    share = np.array([np.mean(inhibition(cmin300, r, pd_, mw) >= 0.9) for r in rr])
    for q in (0.5, 0.9, 0.99):
        out[f"R_needed_{int(q*100)}pct_ge90_at_300"] = float(rr[np.argmax(share >= q)]) if share.max() >= q else None
    cavg300 = conc[300]
    share_avg = np.array([np.mean(inhibition(cavg300, r, pd_, mw).mean(1) >= 0.9) for r in rr[::10]])
    rr10 = rr[::10]
    for q in (0.5, 0.9, 0.99):
        out[f"R_needed_{int(q*100)}pct_avg_ge90_at_300"] = float(rr10[np.argmax(share_avg >= q)]) if share_avg.max() >= q else None
    r99 = out["R_needed_99pct_avg_ge90_at_300"]
    if r99:
        out["share200_avg_ge90_at_that_R"] = float(np.mean(inhibition(conc[200], r99, pd_, mw).mean(1) >= 0.9))
    share200 = np.array([np.mean(inhibition(conc[200][:, -1], r, pd_, mw) >= 0.9) for r in rr])
    out["share200_at_R_where_300_reaches_99pct"] = float(share200[np.argmax(share >= 0.99)]) if share.max() >= 0.99 else None
    # Blood-only threshold (no tumour enrichment) for reference.
    out["blood_trough_needed_for_90pct_inhibition_R1_nM"] = round(float(pd_["EC50_nM_tumor"] * (0.9 / (pd_["Imax"] - 0.9)) ** (1 / out["hill"])), 1)
    (ROOT / "results" / "summary.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Figure: A) day-28 profiles (median and 5-95%) for 200 and 300 mg in nM tumour-equivalent at R=5.5;
    # B) share with trough inhibition >=90% vs dose for each R.
    (ROOT / "figures").mkdir(exist_ok=True)
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.6))
    th = t_last - t_last[0]
    for i, d in enumerate([200, 300]):
        cn = conc[d] / mw * 1000
        ax[0].plot(th, np.median(cn, 0), color=OKABE[i + 1], label=f"{d} mg QD (median)")
        ax[0].fill_between(th, np.percentile(cn, 5, 0), np.percentile(cn, 95, 0), color=OKABE[i + 1], alpha=0.2)
    ec90_blood = pd_["EC90_nM_tumor"]
    for r, ls in ((4.0, "--"), (7.0, ":")):
        ax[0].axhline(out["blood_trough_needed_for_90pct_inhibition_R1_nM"] / r, color="grey", ls=ls, lw=1, label=f"90% inhibition if tumour = {r:g} x blood")
    ax[0].set_yscale("log"); ax[0].set_yticks([20, 50, 100, 200, 500], ["20", "50", "100", "200", "500"]); ax[0].minorticks_off(); ax[0].set_xlabel("Hours after dose on day 28"); ax[0].set_ylabel("Whole-blood daraxonrasib (nM)")
    ax[0].set_title(f"A. Day-28 profiles (n={N}; band 5-95%)", fontsize=10); ax[0].legend(fontsize=7)
    for j, r in enumerate(R_VALUES):
        s = df[df.tumor_blood_ratio == r]
        ax[1].plot(s.dose_mg, s.share_trough_ge90, "o-", color=OKABE[j + 3], label=f"tumour/blood = {r:g}")
    ax[1].scatter([300, 200], [1.00, 0.91], marker="*", s=120, color="black", zorder=5, label="applicant's model (FDA review)")
    ax[1].set_ylim(0, 1.05); ax[1].set_xlabel("Dose (mg once daily)"); ax[1].set_ylabel("Share with trough inhibition >= 90%")
    ax[1].set_title("B. Predicted target attainment at trough", fontsize=10); ax[1].legend(fontsize=7, loc="center left")
    fig.tight_layout(); fig.savefig(ROOT / "figures" / "daraxonrasib_target.png", dpi=150); plt.close(fig)
    print(json.dumps({k: out[k] for k in ("hill", "benchmark_300mg_day28", "R_needed_50pct_ge90_at_300", "R_needed_90pct_ge90_at_300", "R_needed_99pct_ge90_at_300", "R_needed_50pct_avg_ge90_at_300", "R_needed_90pct_avg_ge90_at_300", "R_needed_99pct_avg_ge90_at_300", "share200_avg_ge90_at_that_R", "share200_at_R_where_300_reaches_99pct", "blood_trough_needed_for_90pct_inhibition_R1_nM")}, indent=1))
    print(df.round(3).to_string())


if __name__ == "__main__":
    main()
