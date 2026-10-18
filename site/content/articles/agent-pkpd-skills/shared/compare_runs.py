"""Collect key estimates (from agent_tables/, aggregate outputs of each run) from the four agent runs and compare them with the reference warfarin-pkpd analysis.

Run: python compare_runs.py
Writes results/comparison.csv and figures/agent_runs.png.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
RUNS = ROOT / "agent_tables"  # aggregate tables copied from each run directory
# Reference (warfarin-pkpd note, 2026-10-04): allometric 1-cmt PK without lag (fits-primary/weight-refined) and turnover PD with
# gamma fixed to 1 after allometric PK (weight-turn); exp of the stored thetas. Optimiser warnings: no interval available.
REFERENCE = {"CL/F (L/h)": 0.1360, "V/F (L)": 7.921, "IC50 (mg/L)": 1.149, "kout (1/h)": 0.05136}
INTERVAL = {"S1": "bootstrap (FOCEi)", "S2": "bootstrap (FOCEi)", "N1": "bootstrap (SAEM refits)", "N2": "asymptotic (sandwich)"}
MARKER = {"S1": "o", "S2": "o", "N1": "s", "N2": "^"}
OKABE_ITO = {"S1": "#0072B2", "S2": "#56B4E9", "N1": "#D55E00", "N2": "#E69F00"}


def row(df: pd.DataFrame, col: str, key: str) -> pd.Series:
    hit = df[df[col] == key]
    assert len(hit) == 1, (col, key)
    return hit.iloc[0]


def collect() -> pd.DataFrame:
    rec = []
    t = pd.read_csv(RUNS / "S1/outputs/final_parameter_table.csv")
    d = row(pd.read_csv(RUNS / "S1/outputs/cv_prediction_differences.csv").query("group == 'all'"), "contrast", "PK24 - POP")
    for name, key in [("CL/F (L/h)", "CL/F (70 kg)"), ("V/F (L)", "V/F (70 kg)"), ("IC50 (mg/L)", "IC50"), ("kout (1/h)", "kout")]:
        r = row(t, "parameter", key)
        rec.append(dict(run="S1", quantity=name, estimate=r.estimate, lo=r.boot_CI_low, hi=r.boot_CI_high))
    rec.append(dict(run="S1", quantity="dRMSE early PK - population", estimate=d.mean_diff_subject_RMSE, lo=d.boot95_low, hi=d.boot95_high,
                    n_improved=d.n_improved))
    b = pd.read_csv(RUNS / "S2/outputs/bootstrap_summary.csv")
    d = row(pd.read_csv(RUNS / "S2/outputs/early_pk_paired_comparisons.csv").query("setting == 'LOSO all'"), "comparison", "B - A")
    for name, key in [("CL/F (L/h)", "tcl"), ("V/F (L)", "tv"), ("IC50 (mg/L)", "tic50"), ("kout (1/h)", "tkout")]:
        r = row(b, "parameter", key)
        rec.append(dict(run="S2", quantity=name, estimate=r.estimate_natural, lo=r["boot_p2.5"], hi=r["boot_p97.5"]))
    rec.append(dict(run="S2", quantity="dRMSE early PK - population", estimate=d.mean_diff_RMSE, lo=d.ci_low, hi=d.ci_high, n_improved=d.n_improved))
    t = pd.read_csv(RUNS / "N1/tables_final_parameters.csv")
    d = row(pd.read_csv(RUNS / "N1/tables_earlypk_comparison.csv").query("comparison == 'EARLYPK vs POP'"), "subset", "all")
    for name, key in [("CL/F (L/h)", "CL (L/h, 70 kg)"), ("V/F (L)", "V (L, 70 kg)"), ("IC50 (mg/L)", "IC50 (mg/L)"), ("kout (1/h)", "kout (1/h)")]:
        r = row(t, "parameter", key)
        rec.append(dict(run="N1", quantity=name, estimate=r.estimate, lo=r.lo95, hi=r.hi95))
    rec.append(dict(run="N1", quantity="dRMSE early PK - population", estimate=d.mean_diff, lo=d.ci_lo, hi=d.ci_hi, n_improved=d.n_improved))
    pk = pd.read_csv(RUNS / "N2/outputs/pk_final_params.csv")
    pd_ = pd.read_csv(RUNS / "N2/outputs/pd_final_params.csv")
    d = row(pd.read_csv(RUNS / "N2/outputs/q5_paired_loo.csv"), "comparison", "B - A (early PK vs population)")
    for name, tab, key in [("CL/F (L/h)", pk, "tcl"), ("V/F (L)", pk, "tv"), ("IC50 (mg/L)", pd_, "tic50"), ("kout (1/h)", pd_, "tkout")]:
        r = row(tab, "param", key)  # asymptotic (sandwich) CI: N2 ran no bootstrap
        rec.append(dict(run="N2", quantity=name, estimate=r["Back-transformed"], lo=r["CI Lower"], hi=r["CI Upper"]))
    rec.append(dict(run="N2", quantity="dRMSE early PK - population", estimate=d["mean"], lo=d.lo, hi=d.hi, n_improved=d.n_better))
    # N2 chose a 2-cmt model: compare total volume V1 + Vp (no interval available for the sum)
    v_tot = row(pk, "param", "tv")["Back-transformed"] + row(pk, "param", "tvp")["Back-transformed"]
    rec = [r for r in rec if not (r["run"] == "N2" and r["quantity"] == "V/F (L)")]
    rec.append(dict(run="N2", quantity="V/F (L)", estimate=v_tot, lo=np.nan, hi=np.nan, note="V1 + Vp of a 2-cmt model"))
    out = pd.DataFrame(rec)
    out["reference"] = out["quantity"].map(REFERENCE)
    out["pct_vs_reference"] = 100 * (out["estimate"] / out["reference"] - 1)
    return out


def plot(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.2), constrained_layout=True, gridspec_kw=dict(width_ratios=[1.4, 1]))
    qs = list(REFERENCE)
    runs = ["S1", "S2", "N1", "N2"]
    for j, r in enumerate(runs):
        s = df[(df.run == r) & df.quantity.isin(qs)].set_index("quantity").loc[qs]
        x = np.arange(len(qs)) + (j - 1.5) * 0.15
        ref = s["reference"].to_numpy()
        lo = ((s["estimate"] - s["lo"]) / ref).fillna(0).to_numpy()
        hi = ((s["hi"] - s["estimate"]) / ref).fillna(0).to_numpy()
        ax[0].errorbar(x, s["estimate"] / ref, yerr=[lo, hi], fmt=MARKER[r], color=OKABE_ITO[r], capsize=3,
                       label=f"{r}: {INTERVAL[r]}")
    ax[0].axhline(1, color="#555555", lw=0.8)
    ax[0].axhspan(0.8, 1.2, color="#999999", alpha=0.12, lw=0)
    ax[0].set_xticks(range(len(qs)), qs, fontsize=9)
    ax[0].set(ylabel="Estimate / reference analysis", ylim=(0.5, 1.6),
              title="a. Key estimates vs the reference (band: +/-20%)")
    ax[0].legend(fontsize=7, frameon=False, ncol=2, loc="upper left")
    s = df[df.quantity == "dRMSE early PK - population"].set_index("run").loc[runs]
    y = np.arange(len(runs))[::-1]
    ax[1].errorbar(s["estimate"], y, xerr=[s["estimate"] - s["lo"], s["hi"] - s["estimate"]], fmt="none", capsize=3,
                   ecolor="#333333")
    for yi, r in zip(y, runs):
        ax[1].plot(s.loc[r, "estimate"], yi, MARKER[r], color=OKABE_ITO[r], ms=7)
    ax[1].axvline(0, color="#555555", lw=0.8)
    ax[1].set_yticks(y, [f"{r} ({int(s.loc[r, 'n_improved'])} of 32 improved)" for r in runs], fontsize=9)
    ax[1].set(xlabel="Per-subject RMSE difference (PCA %)\nearly PK - population (negative = early PK helps)",
              title="b. Early-PK question")
    for a in ax:
        a.spines[["top", "right"]].set_visible(False)
    (ROOT / "figures").mkdir(exist_ok=True)
    fig.savefig(ROOT / "figures" / "agent_runs.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    df = collect()
    (ROOT / "results").mkdir(exist_ok=True)
    df.to_csv(ROOT / "results" / "comparison.csv", index=False)
    print(df.round(4).to_string(index=False))
    plot(df)
