"""Step-up priming designs for elranatamab: Day-4 free exposure and first-step CRS probability.

Run: python analysis/run_analysis.py  -> results/*.csv, results/summary.json, figures/*.png
All parameters are transcribed from the public paper (analysis/inputs.json); nothing is re-estimated from patient data.
PK: quasi-equilibrium sBCMA binding model (analysis/tmdd.py). E-R: logistic model for any-grade CRS after the first
step-up dose (ESM Table S2), driven by the free concentration on Day 4 (before the second step-up dose).
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

import model
import tmdd

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261022
N_SUBJECTS = 4096
N_COEF_DRAWS = 2000
N_PROB_DRAWS = 500  # coefficient draws used for design-probability intervals (512-subject subset)
N_SUBSET = 512
DAY4 = 3.0  # first dose at t=0 (Day 1); Day 4 is t=3, just before the second step-up dose
CL_DROPOUT = 0.3  # L/day; the paper's VPC excluded simulated subjects above this CL after ~84 days (dropout)
OKABE = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#0072B2", "#D55E00", "#CC79A7"]


def gm(x: np.ndarray) -> float:
    return float(np.exp(np.nanmean(np.log(x))))


def logistic(c, tb, b0, btb, bc):
    return 1 / (1 + np.exp(-(b0 + btb * tb + bc * np.log(c))))


def main() -> None:
    inp = json.loads((ROOT / "analysis" / "inputs.json").read_text(encoding="utf-8"))
    er = inp["er_crs_first_stepup"]
    rng = np.random.default_rng(SEED)
    p = tmdd.sample(inp, N_SUBJECTS, rng)
    out: dict = {"seed": SEED, "n_subjects": N_SUBJECTS}
    (ROOT / "results").mkdir(exist_ok=True)
    (ROOT / "figures").mkdir(exist_ok=True)

    # 1. Benchmark against the paper's geometric means of free elranatamab (approved 12/32/76 mg then QW).
    appr = [(0.0, 12.0), (3.0, 32.0)] + [(7.0 + 7 * k, 76.0) for k in range(23)]
    t8, tss = np.linspace(7, 14, 141), np.linspace(161, 168, 141)
    c = tmdd.simulate(appr, p, np.concatenate([t8, tss]))
    a, b = c[:, :141], c[:, 141:]
    keep = p["CL"] <= CL_DROPOUT
    bench = inp["benchmarks_free_gm_ng_ml"]
    rows = [
        ("Day 8-15 Cmax", gm(a.max(1)), np.nan, bench["first_full_dose_day8"]["Cmax"]),
        ("Day 8-15 Cavg", gm(a.mean(1)), np.nan, bench["first_full_dose_day8"]["Cavg"]),
        ("Week 24 QW Cavg", gm(b.mean(1)), gm(b[keep].mean(1)), bench["SS_QW_week24"]["Cavg"]),
        ("Week 24 QW Ctrough", gm(b[:, -1]), gm(b[keep, -1]), bench["SS_QW_week24"]["Ctrough"]),
    ]
    bdf = pd.DataFrame(rows, columns=["metric", "model_all", "model_CL_le_0.3", "paper"])
    bdf["ratio_all"] = bdf.model_all / bdf.paper
    bdf["ratio_CL_le_0.3"] = bdf["model_CL_le_0.3"] / bdf.paper
    bdf.round(3).to_csv(ROOT / "results" / "benchmark.csv", index=False)
    out["benchmark"] = bdf.round(3).replace({np.nan: None}).to_dict(orient="records")
    out["share_CL_le_0.3"] = round(float(keep.mean()), 3)

    # Linear approximation (recorded failure): same subjects, binding ignored.
    lin = {k: p[k][:, None] for k in ("CL", "Vc", "Vp", "Q", "ka")}
    lin["F"] = p["F"]
    cl8 = model.concentration(t8, appr, lin) * 1000
    out["linear_approx_day8_cmax_ratio_to_paper"] = round(gm(cl8.max(1)) / bench["first_full_dose_day8"]["Cmax"], 3)

    # 2. Calibration: predicted first-step CRS rate under 12 mg vs observed 79/183.
    designs = {k: [tuple(map(float, x)) for x in v] for k, v in inp["regimens_mg"].items()}
    t_obs = np.array([DAY4, 7.0 - 1e-6] + list(np.linspace(0, 21, 211)))
    sims = {k: tmdd.simulate(v, p, t_obs) for k, v in designs.items()}
    c4 = {k: s[:, 0] for k, s in sims.items()}
    tb = p["high_tb"].astype(float)
    p12 = logistic(c4["approved_12_32_76"], tb, er["intercept"], er["tb_high"], er["log_ctrough"])
    target = er["events"] / er["n"]
    shift = brentq(lambda d: logistic(c4["approved_12_32_76"], tb, er["intercept"] + d, er["tb_high"], er["log_ctrough"]).mean() - target, -5, 5)
    out["calibration"] = {"predicted_mean_crs_12mg": round(float(p12.mean()), 3), "observed": round(target, 3),
                          "observed_95ci_jeffreys": [round(float(x), 3) for x in __import__("scipy.stats", fromlist=["beta"]).beta.ppf([0.025, 0.975], er["events"] + 0.5, er["n"] - er["events"] + 0.5)], "intercept_shift_to_match": round(float(shift), 3),
                          "intercept_95ci_published": er["intercept_ci"],
                          "day4_gm_ng_ml": round(gm(c4["approved_12_32_76"]), 1),
                          "day4_p5_p95": [round(float(x), 1) for x in np.percentile(c4["approved_12_32_76"], [5, 95])]}

    # 3. Designs by tumour burden, with uncertainty from E-R coefficient draws (independent normal approx of profile CIs;
    #    covariance not published) and the calibrated intercept as the main scenario.
    def se(ci):
        return (ci[1] - ci[0]) / 3.92
    draws_bc = rng.normal(er["log_ctrough"], se(er["log_ctrough_ci"]), N_COEF_DRAWS)
    draws_tb = rng.normal(er["tb_high"], se(er["tb_high_ci"]), N_COEF_DRAWS)
    sub = rng.choice(N_SUBJECTS, N_SUBSET, replace=False)
    # observed first-step CRS rate also uncertain: Jeffreys beta draws for 79/183
    target_draws = rng.beta(er["events"] + 0.5, er["n"] - er["events"] + 0.5, N_PROB_DRAWS)
    drows = []
    for name, reg in designs.items():
        for tbv, lab in ((0.0, "low/intermediate"), (1.0, "high")):
            cc = c4[name]
            point = {}
            for scen, b0 in (("published", er["intercept"]), ("calibrated", er["intercept"] + shift)):
                point[scen] = float(logistic(cc, tbv, b0, er["tb_high"], er["log_ctrough"]).mean())
            # odds ratio vs approved for the same tumour-burden stratum, propagated over draws (intercept cancels approx.)
            ref = c4["approved_12_32_76"]
            # calibrated-intercept probability uncertainty: recalibrate intercept per draw so the 12 mg rate stays at observed
            probs = []
            for i in range(N_PROB_DRAWS):
                bc, btb, tg = draws_bc[i], draws_tb[i], target_draws[i]
                sh = brentq(lambda d: logistic(ref[sub], tb[sub], d, btb, bc).mean() - tg, -40, 20)
                probs.append(float(logistic(cc[sub], tbv, sh, btb, bc).mean()))
            drows.append(dict(design=name, first_dose_mg=reg[0][1], tumor_burden=lab,
                              p_published=point["published"], p_calibrated=point["calibrated"],
                              p_cal_2_5=np.percentile(probs, 2.5), p_cal_97_5=np.percentile(probs, 97.5),
                              day4_gm_ng_ml=gm(cc)))
        drows.append(dict(design=name, first_dose_mg=reg[0][1], tumor_burden="all",
                          day4_gm_ng_ml=gm(c4[name]), day8_predose_gm_ng_ml=gm(sims[name][:, 1]),
                          day8_predose_vs_approved=gm(sims[name][:, 1]) / gm(sims["approved_12_32_76"][:, 1])))
    ddf = pd.DataFrame(drows)
    ddf.round(4).to_csv(ROOT / "results" / "designs.csv", index=False)
    out["designs"] = ddf.round(4).replace({np.nan: None}).to_dict(orient="records")

    # 4. First dose for high tumour burden giving the same predicted odds as 12 mg in low burden.
    def dose_match(btb, bc):
        target_logc = np.log(gm(c4["approved_12_32_76"])) - btb / bc
        return float(np.exp(target_logc))
    c_target = dose_match(er["tb_high"], er["log_ctrough"])
    grid = np.array([2, 3, 4, 5, 6, 7, 8, 10, 12], float)
    gm_grid = []
    for d in grid:
        gm_grid.append(gm(tmdd.simulate([(0.0, float(d))], {k: (v[sub] if isinstance(v, np.ndarray) else v) for k, v in p.items()}, np.array([DAY4]))[:, 0]))
    gm_grid = np.array(gm_grid)
    dose_eq = float(np.interp(np.log(c_target), np.log(gm_grid), grid))
    eqs = [float(np.interp(np.log(dose_match(draws_tb[i], draws_bc[i])), np.log(gm_grid), grid, left=np.nan, right=np.nan)) for i in range(N_COEF_DRAWS)]
    out["tb_equivalent_first_dose"] = {"dose_mg": round(dose_eq, 2), "concentration_ratio": round(float(np.exp(er["tb_high"] / er["log_ctrough"])), 3),
                                       "dose_2_5_97_5": [round(float(np.nanpercentile(eqs, q)), 2) for q in (2.5, 97.5)],
                                       "share_draws_below_grid_min_2mg": round(float(np.mean(np.isnan(eqs))), 3),
                                       "dose_day4_linearity": dict(zip([int(x) for x in grid], [round(float(v), 1) for v in gm_grid]))}
    # Probability-matching alternative: first dose for high burden whose mean predicted P equals low burden at 12 mg.
    p_ref = float(logistic(c4["approved_12_32_76"], 0.0, er["intercept"] + shift, er["tb_high"], er["log_ctrough"]).mean())
    sp = {k: (v[sub] if isinstance(v, np.ndarray) else v) for k, v in p.items()}
    pg = [float(logistic(tmdd.simulate([(0.0, float(d))], sp, np.array([DAY4]))[:, 0], 1.0, er["intercept"] + shift, er["tb_high"], er["log_ctrough"]).mean()) for d in grid]
    out["tb_equivalent_first_dose"]["prob_matching_dose_mg"] = round(float(np.interp(p_ref, pg, grid)), 2)
    out["tb_equivalent_first_dose"]["p_ref_low_tb_12mg"] = round(p_ref, 3)
    (ROOT / "results" / "summary.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Figure: A) typical-subject profiles, B) first-step CRS probability by design and tumour burden (calibrated, 95% band).
    typ = tmdd.typical(inp)
    t = np.linspace(0, 21, 421)
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.4))
    labels = {"approved_12_32_76": "12/32/76 mg (approved)", "mm1_4_20_76": "4/20/76 mg (MagnetisMM-1 Part 2)",
              "tb_adapted_5_32_76": "5/32/76 mg (hypothetical)", "single_32_76": "32/76 mg (hypothetical)"}
    for i, (name, reg) in enumerate(designs.items()):
        ax[0].plot(t + 1, tmdd.simulate(reg, typ, t)[0], color=OKABE[i + 1], label=labels[name])
    ax[0].axvline(DAY4 + 1, color="grey", ls=":", lw=1)
    ax[0].set_yscale("log"); ax[0].set_ylim(10, 2e4)
    ax[0].set_xlabel("Day (first dose on Day 1)"); ax[0].set_ylabel("Free elranatamab (ng/mL), typical male")
    ax[0].set_title("A. Step-up designs (dotted line: Day 4)"); ax[0].legend(fontsize=8)
    s = ddf[ddf.tumor_burden != "all"]
    names = list(designs)
    for j, lab in enumerate(["low/intermediate", "high"]):
        r = s[s.tumor_burden == lab].set_index("design").loc[names]
        x = np.arange(len(names)) + (j - 0.5) * 0.38
        ax[1].bar(x, r.p_calibrated, 0.38, color=OKABE[2 + 3 * j], label=f"{lab} tumour burden")
        ax[1].errorbar(x, r.p_calibrated, yerr=[r.p_calibrated - r.p_cal_2_5, r.p_cal_97_5 - r.p_calibrated], fmt="none", ecolor="black", lw=1)
    ax[1].set_xticks(np.arange(len(names)), [labels[n].split(" (")[0] for n in names], fontsize=8)
    ax[1].set_ylim(0, 1); ax[1].set_ylabel("Predicted P(any-grade CRS) after first dose")
    ax[1].set_title(f"B. First-step CRS, calibrated to 79/183 (n={N_SUBJECTS}; 95% bars: {N_SUBSET} subset)", fontsize=10); ax[1].legend(fontsize=8, loc="upper left")
    fig.tight_layout(); fig.savefig(ROOT / "figures" / "stepup_designs.png", dpi=150); plt.close(fig)

    print(json.dumps({k: out[k] for k in ("benchmark", "share_CL_le_0.3", "linear_approx_day8_cmax_ratio_to_paper", "calibration", "tb_equivalent_first_dose")}, indent=1))
    print(ddf.round(3).to_string())


if __name__ == "__main__":
    main()
