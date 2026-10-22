"""Taletrectinib dosing instructions and meal adherence: steady-state exposure and relative ALT/AST risk.

Run: python analysis/run_analysis.py -> results/*.csv, results/summary.json, figures/*.png
All coefficients are transcribed from the FDA multidisciplinary review (analysis/inputs.json).
Linear PK: steady-state Cavg = F_rel(food) * Dose / (CL/F * 24). Day-to-day meal states enter through the
average F_rel over days (exact for linear PK). The time course (figure A) uses the 3-compartment model with lag.
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
N_UNC = 2000
OKABE = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#0072B2", "#D55E00", "#CC79A7"]


def gm(x):
    return float(np.exp(np.mean(np.log(x))))


def frel_factors(pk, shift_fast2=0.0, shift_fed=0.0):
    return {"fast10": 1.0, "fast2": np.exp(pk["Frel_fast2_exp"] + shift_fast2), "fed": np.exp(pk["Frel_fed_exp"] + shift_fed)}


def regimens(meal_ratio_std_vs_fast2: float = None):
    """Each regimen: dose (mg) and fraction of days in each food state."""
    return {
        "A 600 mg, 2 h fast (label)": (600, {"fast2": 1.0}),
        "B 400 mg with meal, always": (400, {"fed": 1.0}),
        "C 400 mg with meal, 20% of days fasted": (400, {"fed": 0.8, "fast10": 0.2}),
        "D 400 mg with meal, 50% of days fasted": (400, {"fed": 0.5, "fast10": 0.5}),
        "E 600 mg with meal (off-label)": (600, {"fed": 1.0}),
        "F 600 mg, strict overnight fast": (600, {"fast10": 1.0}),
    }


def main() -> None:
    inp = json.loads((ROOT / "analysis" / "inputs.json").read_text(encoding="utf-8"))
    pk, pop, er = inp["pk"], inp["population"], inp["er_alt_ast_g3"]
    obs = inp["observed_cavgss_600mg_quartiles_ng_ml"]
    rng = np.random.default_rng(SEED)
    asian = rng.random(N) < pop["asian_fraction"]
    m, sd = pop["weight_mean_sd_kg"]
    s2 = np.log(1 + (sd / m) ** 2)
    wt = np.clip(np.exp(rng.normal(np.log(m) - s2 / 2, np.sqrt(s2), N)), *pop["weight_range_kg"])
    om = pk["omega2"]
    cl = pk["CL_L_h"] * (wt / pk["WT_ref_kg_assumed"]) ** pk["CL_WT_power"] * np.exp(pk["CL_asian_exp"] * asian) * np.exp(rng.normal(0, np.sqrt(om["CL"]), N))
    eta_f = rng.normal(0, np.sqrt(om["FREL"]), N)  # between-subject F; assumed constant across food states for a subject
    beta = np.log(er["hr_per_ng_ml_cavgss"])
    se_beta = (np.log(er["hr_ci"][1]) - np.log(er["hr_ci"][0])) / 3.92
    se_f2 = (pk["Frel_fast2_ci"][1] - pk["Frel_fast2_ci"][0]) / 3.92
    se_fed = (pk["Frel_fed_ci"][1] - pk["Frel_fed_ci"][0]) / 3.92
    out: dict = {"seed": SEED, "n": N}

    def cavg(dose, mix, fac):
        f = sum(frac * fac[state] for state, frac in mix.items())
        return f * np.exp(eta_f) * dose * 1e6 / (cl * 1000 * 24)  # ng/mL

    fac = frel_factors(pk)
    regs = regimens()
    ref = cavg(*regs["A 600 mg, 2 h fast (label)"], fac)
    # Benchmark: label regimen vs observed quartiles of Cavgss in the E-R dataset (mostly 600 mg, 2 h fast).
    q = np.percentile(ref, [25, 50, 75])
    out["benchmark_label_600_fast2"] = {"model_q1_median_q3": [round(float(x), 1) for x in q],
                                        "observed_q1_median_q3": [obs["q1"], obs["median"], obs["q3"]],
                                        "model_p1_p99": [round(float(x), 1) for x in np.percentile(ref, [1, 99])],
                                        "observed_min_max": [obs["min"], obs["max"]]}
    # Draws for uncertainty: beta and the two food-effect thetas.
    bd = rng.normal(beta, se_beta, N_UNC)
    f2d = rng.normal(0, se_f2, N_UNC)
    fdd = rng.normal(0, se_fed, N_UNC)
    rows = []
    for name, (dose, mix) in regs.items():
        c = cavg(dose, mix, fac)
        for grp, msk in (("all", np.ones(N, bool)), ("Asian", asian), ("non-Asian", ~asian)):
            # relative hazard vs the label regimen in the same subjects, population-averaged hazard ratio
            rh = float(np.mean(np.exp(beta * c[msk])) / np.mean(np.exp(beta * ref[msk])))
            rhs = []
            for i in range(0, N_UNC, 4):
                fk = frel_factors(pk, f2d[i], fdd[i])
                ci_ = cavg(dose, mix, fk)[msk]
                cr = cavg(*regs["A 600 mg, 2 h fast (label)"], fk)[msk]
                rhs.append(np.mean(np.exp(bd[i] * ci_)) / np.mean(np.exp(bd[i] * cr)))
            rows.append(dict(regimen=name, group=grp, cavg_median=float(np.median(c[msk])), cavg_p5=float(np.percentile(c[msk], 5)),
                             cavg_p95=float(np.percentile(c[msk], 95)), ratio_median_vs_label=float(np.median(c[msk]) / np.median(ref[msk])),
                             share_below_obs_min=float(np.mean(c[msk] < obs["min"])), share_below_obs_q1=float(np.mean(c[msk] < obs["q1"])),
                             share_above_obs_q3=float(np.mean(c[msk] > obs["q3"])),
                             rel_hazard_alt_ast=rh, rel_hazard_2_5=float(np.percentile(rhs, 2.5)), rel_hazard_97_5=float(np.percentile(rhs, 97.5))))
    df = pd.DataFrame(rows)
    (ROOT / "results").mkdir(exist_ok=True)
    df.round(4).to_csv(ROOT / "results" / "regimens.csv", index=False)
    out["regimens"] = df.round(4).to_dict(orient="records")

    # Sensitivity: standard meals may raise F above the high-fat-derived 'fed' value relative to 2 h fast
    # (FDA: six patients showed a stepwise rise; effect not robustly estimated). Scale fed F by r relative to model.
    sens = []
    for r in (0.9, 1.0, 1.15, 1.3):
        fk = dict(fac); fk["fed"] = fac["fed"] * r
        c = cavg(400, {"fed": 1.0}, fk)
        sens.append(dict(fed_F_multiplier=r, cavg_median=float(np.median(c)), ratio_vs_label=float(np.median(c) / np.median(ref)),
                         rel_hazard=float(np.mean(np.exp(beta * c)) / np.mean(np.exp(beta * ref)))))
    pd.DataFrame(sens).round(4).to_csv(ROOT / "results" / "sensitivity_meal_effect.csv", index=False)
    out["sensitivity_meal_effect"] = pd.DataFrame(sens).round(4).to_dict(orient="records")
    # Dose that matches the label median exposure when taken with meals (exposure matching, linear PK).
    out["dose_matching_label_with_meal_mg"] = round(600 * fac["fast2"] / fac["fed"], 1)
    out["frel_factors"] = {k: round(float(v), 3) for k, v in fac.items()}
    (ROOT / "results" / "summary.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Figure. A: typical non-Asian 66 kg time course (3-cmt, lag) at steady state for A, B, F. B: Cavgss distributions.
    (ROOT / "figures").mkdir(exist_ok=True)
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 5.0))
    vc = pk["Vc_L"] * np.exp(pk["VC_cancer_exp"])

    def course(dose, state):
        ka = pk["ka_per_h"] * np.exp({"fast10": 0.0, "fast2": pk["ka_fast2_exp"], "fed": pk["ka_fed_exp"]}[state])
        f = fac[state]
        k10, k12, k21, k13, k31 = pk["CL_L_h"] / vc, pk["Q3_L_h"] / vc, pk["Q3_L_h"] / pk["V3_L"], pk["Q4_L_h"] / vc, pk["Q4_L_h"] / pk["V4_L"]

        def rhs(t, y):
            d, c, p1, p2 = y
            return [-ka * d, ka * d - (k10 + k12 + k13) * c + k21 * p1 + k31 * p2, k12 * c - k21 * p1, k13 * c - k31 * p2]
        y = np.zeros(4); ts, cs = [], []
        for day in range(21):
            t0 = day * 24.0
            sol = solve_ivp(rhs, (t0, t0 + pk["alag_h"]), y, max_step=0.1); y = sol.y[:, -1].copy(); y[0] += f * dose * 1e6
            sol = solve_ivp(rhs, (t0 + pk["alag_h"], t0 + 24), y, t_eval=np.linspace(t0 + pk["alag_h"], t0 + 24, 60), max_step=0.25)
            y = sol.y[:, -1].copy()
            if day == 20:
                ts, cs = sol.t - t0, sol.y[1] / (vc * 1000)
        return ts, cs
    for i, (lab, dose, state) in enumerate([("A 600 mg, 2 h fast", 600, "fast2"), ("B 400 mg with meal", 400, "fed"), ("F 600 mg, overnight fast", 600, "fast10")]):
        t, c = course(dose, state)
        ax[0].plot(t, c, color=OKABE[i + 1], label=lab)
    ax[0].set_xlabel("Hours after dose (day 21, steady state)"); ax[0].set_ylabel("Taletrectinib (ng/mL), typical non-Asian 66 kg")
    ax[0].set_title("A. Typical steady-state profiles"); ax[0].legend(fontsize=8)
    names = list(regs)
    data = [cavg(*regs[n], fac) for n in names]
    ax[1].boxplot(data, vert=False, whis=(5, 95), showfliers=False, medianprops=dict(color="black", lw=1.5))
    ax[1].set_yticks(range(1, len(names) + 1), [n.split(" (")[0] for n in names], fontsize=8)
    ax[1].axvspan(obs["q1"], obs["q3"], color=OKABE[2], alpha=0.25, label="observed IQR (600 mg, n=312)")
    ax[1].axvline(obs["min"], color="grey", ls=":", lw=1, label="observed minimum")
    ax[1].set_xscale("log"); ax[1].set_xlabel("Cavg at steady state (ng/mL)")
    ax[1].set_xticks([100, 200, 300, 500, 1000], ["100", "200", "300", "500", "1000"]); ax[1].minorticks_off()
    ax[1].set_title(f"B. Virtual patients (n={N}; box: IQR, whiskers: 5-95%)", fontsize=10); ax[1].invert_yaxis(); ax[1].legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2)
    fig.tight_layout(); fig.savefig(ROOT / "figures" / "food_regimens.png", dpi=150); plt.close(fig)
    print(json.dumps({k: out[k] for k in ("benchmark_label_600_fast2", "frel_factors", "dose_matching_label_with_meal_mg", "sensitivity_meal_effect")}, indent=1))
    print(df.round(3).to_string())


if __name__ == "__main__":
    main()
