"""What does a "human dose from measured in vitro ADME" depend on? ExpansionRx test set, potency fixed.

Run: python dose_decomposition.py
Reads data/expansion_data_{train,test,raw}.csv (OpenADMET-ExpansionRx, CC BY 4.0; place them in data/ first).
Writes results/summary.json, results/*.csv and figures/dose_decomposition.png.
The dose models are transparent textbook models (simplified from Page 2016), not Inductive Bio's undisclosed equations.
"""
from pathlib import Path
import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm, spearmanr

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"

# Parameters
SEED = 20261014
N_REP = 500
N_BOOT = 2000
QH = 20.7  # hepatic blood flow, mL/min/kg
BW = 70.0  # kg
TAU = 24.0  # h, once daily
KA = 1.0  # 1/h, first-order absorption for the Cmin configurations
IC50_NM = 10.0  # reference potency used by Inductive for ExpansionRx (a constant does not affect ranks or fold ratios)
COVER = 9.0  # IC90 = 9 x IC50 for a Hill slope of 1
FU_FLOOR = 0.001
MIC_PROTEIN = 0.5  # mg/mL microsomal protein assumed for the fu,mic correction (Hallifax & Houston 2006 equation)
PAPP_HALF = 1.0  # 1e-6 cm/s; illustrative Fa = 1 - exp(-Papp / PAPP_HALF)
MW_ILLUSTRATION = 450.0  # g/mol, only to show mg/day
OT = dict(vp=0.0436, ve=0.151, vr=0.380, re_i=1.4)  # Oie-Tozer physiological volumes, L/kg
SIGMAS = np.round(np.arange(0.0, 0.81, 0.05), 2)  # log10 SD of prediction error
BIASES = [0.0, 0.3]  # log10 systematic offset of predictions
POTENCY_SDS = [0.0, 0.25, 0.5, 0.75, 1.0]  # log10 SD of IC50 across compounds
PAIR_FOLD = 3.0  # pairs whose reference doses differ >= 3-fold
BEACON = dict(spearman=0.79, fold_error=2.4, n=325, programs_spearman=0.61, programs_pair_accuracy=0.81)
OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#D55E00", "#999999"]
COL = {"clint": "HLM CLint", "mppb": "MPPB", "mgmb": "MGMB", "logd": "LogD",
       "papp": "Caco-2 Permeability Papp A>B", "efflux": "Caco-2 Permeability Efflux"}
CONFIG_LABELS = {
    "A": "Cavg, minimal (fu in WSM, Fa = 1, no fu,mic)",
    "A_fumic": "Cavg, + fu,mic from LogD",
    "A_nobind": "Cavg, no plasma binding in WSM (as Page 2016 for bases)",
    "A_fa": "Cavg, + Fa from Caco-2 Papp",
    "A_full": "Cavg, + fu,mic + Fa",
    "B_bolus": "Cmin, bolus, Vss 1 L/kg (extreme)",
    "B_abs": "Cmin, ka 1/h, Vss 1 L/kg",
    "B_abs_v3": "Cmin, ka 1/h, Vss 3 L/kg",
}


def fu_mic(logd: np.ndarray) -> np.ndarray:
    """Hallifax & Houston (2006) microsomal unbound fraction from lipophilicity."""
    return 1 / (1 + MIC_PROTEIN * 10 ** (0.072 * logd ** 2 + 0.067 * logd - 1.126))


def fa_from_papp(papp: np.ndarray) -> np.ndarray:
    return 1 - np.exp(-np.asarray(papp) / PAPP_HALF)


def clh(clint_u: np.ndarray, fu_wsm: np.ndarray) -> np.ndarray:
    """Well-stirred hepatic clearance, mL/min/kg (blood:plasma = 1)."""
    return QH * fu_wsm * clint_u / (QH + fu_wsm * clint_u)


def cmin_per_dose(cl: np.ndarray, v: np.ndarray, f: np.ndarray, ka: float | None) -> np.ndarray:
    """Steady-state trough per unit dose (one compartment), bolus if ka is None."""
    k = cl / v
    if ka is None:
        return f / v * np.exp(-k * TAU) / -np.expm1(-k * TAU)
    k = np.where(np.abs(ka - k) < 1e-6, k * (1 + 1e-4), k)
    return f * ka / (v * (ka - k)) * (np.exp(-k * TAU) / -np.expm1(-k * TAU) - np.exp(-ka * TAU) / -np.expm1(-ka * TAU))


def dose(cfg: str, clint: np.ndarray, fu: np.ndarray, logd: np.ndarray, papp: np.ndarray) -> np.ndarray:
    """umol/day keeping the unbound concentration (Cavg or Cmin) at COVER x IC50."""
    clint_u = clint / fu_mic(logd) if cfg in ("A_fumic", "A_full") else clint
    fu_wsm = np.ones_like(fu) if cfg == "A_nobind" else fu
    h = clh(clint_u, fu_wsm)
    fa = fa_from_papp(papp) if cfg in ("A_fa", "A_full") else 1.0
    f = fa * (1 - h / QH)
    cl = h * 0.06 * BW  # L/h
    c_tot = COVER * IC50_NM / 1000 / fu  # umol/L total plasma
    if cfg.startswith("A"):
        return c_tot * cl * TAU / f
    v = (3.0 if cfg == "B_abs_v3" else 1.0) * BW
    return c_tot / cmin_per_dose(cl, v, f, None if cfg == "B_bolus" else KA)


def vss_oie_tozer(fu: np.ndarray, fut: np.ndarray) -> np.ndarray:
    return OT["vp"] * (1 + OT["re_i"]) + fu * OT["vp"] * (OT["ve"] / OT["vp"] - OT["re_i"]) + OT["vr"] * fu / fut


def aafe(pred: np.ndarray, ref: np.ndarray) -> float:
    """Absolute average fold error, 10 ** mean(|log10(pred / ref)|)."""
    return float(10 ** np.mean(np.abs(np.log10(pred / ref))))


def rho(a: np.ndarray, b: np.ndarray) -> float:
    return float(spearmanr(a, b).statistic)


def spearman_ci(r: float, n: int) -> tuple[float, float]:
    """Fisher z with the Bonett-Wright standard error."""
    se = np.sqrt((1 + r ** 2 / 2) / (n - 3))
    z = np.arctanh(r)
    return float(np.tanh(z - 1.96 * se)), float(np.tanh(z + 1.96 * se))


def pair_accuracy(pred: np.ndarray, ref: np.ndarray, fold: float = PAIR_FOLD) -> float:
    lr, lp = np.log10(ref), np.log10(pred)
    i, j = np.triu_indices(len(ref), 1)
    keep = np.abs(lr[i] - lr[j]) >= np.log10(fold)
    return float(np.mean(np.sign(lp[i] - lp[j])[keep] == np.sign(lr[i] - lr[j])[keep]))


def inputs(d: pd.DataFrame) -> tuple[np.ndarray, ...]:
    return (d[COL["clint"]].to_numpy(float), d["fu"].to_numpy(float),
            d[COL["logd"]].to_numpy(float), d[COL["papp"]].to_numpy(float))


def select(df: pd.DataFrame, log: dict, prefix: str) -> pd.DataFrame:
    d = df.dropna(subset=[COL["clint"], COL["mppb"]]).copy()
    log[f"{prefix}_with_hlm_and_mppb"] = len(d)
    log[f"{prefix}_clint_zero_dropped"] = int((d[COL["clint"]] <= 0).sum())  # log10 undefined
    d = d[d[COL["clint"]] > 0]
    d = d.dropna(subset=[COL["logd"], COL["papp"], COL["efflux"]]).copy()
    log[f"{prefix}_with_logd_and_caco2"] = len(d)
    d["fu"] = np.maximum(d[COL["mppb"]] / 100, FU_FLOOR)
    return d


def load() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict]:
    test = pd.read_csv(DATA / "expansion_data_test.csv", encoding="utf-8")
    train = pd.read_csv(DATA / "expansion_data_train.csv", encoding="utf-8")
    raw = pd.read_csv(DATA / "expansion_data_raw.csv", dtype=str, encoding="utf-8")
    assert test["Molecule Name"].is_unique and train["Molecule Name"].is_unique
    assert not set(test["Molecule Name"]) & set(train["Molecule Name"])
    log = {"test_rows": len(test), "train_rows": len(train)}
    d = select(test, log, "test")
    tr = select(train, log, "train")
    # Out-of-range HLM CLint in the test split (qualifier '<' or '>'), kept for a sensitivity analysis
    s = raw.set_index("Molecule Name").loc[lambda x: x.index.isin(test["Molecule Name"]), COL["clint"]].dropna().str.strip()
    qual = s[s.str[0].isin(["<", ">"])]
    log["test_clint_out_of_range_lt"] = int((qual.str[0] == "<").sum())
    log["test_clint_out_of_range_gt"] = int((qual.str[0] == ">").sum())
    cens = test.set_index("Molecule Name").loc[qual.index].copy()
    cens["qual"] = qual.str[0]
    cens["bound"] = qual.str[1:].str.strip().astype(float)
    cens = cens.dropna(subset=[COL["mppb"], COL["logd"], COL["papp"], COL["efflux"]])
    cens["fu"] = np.maximum(cens[COL["mppb"]] / 100, FU_FLOOR)
    log["censored_with_other_inputs_lt"] = int((cens["qual"] == "<").sum())
    log["censored_with_other_inputs_gt"] = int((cens["qual"] == ">").sum())
    log["censored_lt_bounds"] = sorted(cens.loc[cens["qual"] == "<", "bound"].unique().tolist())
    assert d["fu"].between(FU_FLOOR, 1).all()
    return d, tr, cens, log


def calibrated_pred(ref_log: np.ndarray, r: float, rng: np.random.Generator) -> np.ndarray:
    """Regression-calibrated prediction with Pearson r on the log scale (shrunk towards the mean)."""
    mu, sd = ref_log.mean(), ref_log.std()
    return mu + r ** 2 * (ref_log - mu) + r * np.sqrt(1 - r ** 2) * sd * rng.normal(size=len(ref_log))


def main() -> None:
    rng = np.random.default_rng(SEED)
    d, tr, cens, log = load()
    print(json.dumps(log, indent=2))
    n = len(d)
    clint, fu, logd, papp = inputs(d)
    ref = {c: dose(c, clint, fu, logd, papp) for c in CONFIG_LABELS}
    # Config A identity: oral CL/F = fu * CLint, so the unbound-Cavg dose is proportional to CLint alone
    assert np.allclose(ref["A"], COVER * IC50_NM / 1000 * clint * 0.06 * BW * TAU, rtol=1e-10)
    ref_train = {c: dose(c, *inputs(tr)) for c in CONFIG_LABELS}

    # 1. What the reference dose depends on
    dependence = {}
    for c, x in ref.items():
        ld = np.log10(x)
        boot = [rho(d[COL["logd"]].to_numpy()[idx], x[idx]) for idx in rng.integers(0, n, (N_BOOT, n))]
        dependence[c] = dict(
            label=CONFIG_LABELS[c],
            spearman_vs_hlm_clint=rho(x, clint), spearman_vs_fu=rho(x, fu),
            r2_logdose_on_logclint=float(np.corrcoef(ld, np.log10(clint))[0, 1] ** 2),
            spearman_vs_config_A=rho(x, ref["A"]),
            log10_dose_sd=float(ld.std(ddof=1)),
            dose_mg_median_at_mw450=float(np.median(x) * MW_ILLUSTRATION / 1000),
            dose_mg_p5_p95_at_mw450=(np.percentile(x, [5, 95]) * MW_ILLUSTRATION / 1000).tolist(),
            frac_over_1g_at_mw450=float(np.mean(x * MW_ILLUSTRATION / 1000 > 1000)),
            constant_dose_aafe_train_median=aafe(np.full(n, np.median(ref_train[c])), x),
            constant_dose_aafe_test_median_oracle=aafe(np.full(n, np.median(x)), x),
            measured_logd_spearman=rho(d[COL["logd"]], x),
            measured_logd_spearman_boot95=np.percentile(boot, [2.5, 97.5]).tolist(),
            measured_mlm_n=int(d["MLM CLint"].notna().sum()),
            measured_mlm_spearman=rho(d.loc[d["MLM CLint"].notna(), "MLM CLint"], x[d["MLM CLint"].notna().to_numpy()]))
    sub = d.dropna(subset=[COL["mgmb"]])
    sub = sub[sub[COL["mgmb"]] > 0]
    c_s, f_s = sub[COL["clint"]].to_numpy(float), sub["fu"].to_numpy(float)
    vss = vss_oie_tozer(f_s, np.maximum(sub[COL["mgmb"]].to_numpy() / 100, FU_FLOOR))
    h = clh(c_s, f_s)
    dose_ot = COVER * IC50_NM / 1000 / f_s / cmin_per_dose(h * 0.06 * BW, vss * BW, 1 - h / QH, KA)
    dependence["B_abs_oie_tozer_subset"] = dict(
        n=len(sub), spearman_vs_hlm_clint=rho(dose_ot, c_s), vss_median=float(np.median(vss)),
        vss_p5_p95=np.percentile(vss, [5, 95]).tolist())
    dependence["spearman_logd_vs_hlm_clint"] = rho(logd, clint)
    dependence["fu_mic_p5_median_p95"] = np.percentile(fu_mic(logd), [5, 50, 95]).tolist()
    dependence["fa_p5_median_p95"] = np.percentile(fa_from_papp(papp), [5, 50, 95]).tolist()

    # 2. Out-of-range HLM CLint: add them back at the bound (or half the lower bound), config A
    censoring = {}
    for name, lt_factor in (("at_bound", 1.0), ("half_lower_bound", 0.5)):
        cl_c = np.where(cens["qual"] == "<", cens["bound"] * lt_factor, cens["bound"])
        x = np.concatenate([ref["A"], dose("A", cl_c, cens["fu"].to_numpy(), cens[COL["logd"]].to_numpy(),
                                           cens[COL["papp"]].to_numpy())])
        censoring[name] = dict(n=len(x), log10_dose_sd=float(np.log10(x).std(ddof=1)),
                               constant_dose_aafe_test_median_oracle=aafe(np.full(len(x), np.median(x)), x))

    # 3. Error propagation: log-normal error on CLint (and independently on fu), with an optional bias
    rows = []
    for c in ("A", "A_full", "B_abs"):
        for target in ("clint_only", "clint_and_fu"):
            for bias in BIASES:
                for sigma in SIGMAS:
                    vals = []
                    for _ in range(N_REP):
                        c_hat = clint * 10 ** (rng.normal(0, sigma, n) + bias)
                        f_hat = np.clip(fu * 10 ** rng.normal(0, sigma, n), FU_FLOOR, 1.0) if target == "clint_and_fu" else fu
                        p = dose(c, c_hat, f_hat, logd, papp)
                        vals.append((rho(p, ref[c]), aafe(p, ref[c]), pair_accuracy(p, ref[c])))
                    v = np.array(vals)
                    rows.append(dict(config=c, error_on=target, bias_log10=bias, sigma_log10=float(sigma),
                                     spearman_mean=v[:, 0].mean(), spearman_p2_5=np.percentile(v[:, 0], 2.5),
                                     spearman_p97_5=np.percentile(v[:, 0], 97.5), aafe_mean=v[:, 1].mean(),
                                     pair_accuracy_3fold_mean=v[:, 2].mean()))
    prop = pd.DataFrame(rows)
    ci = spearman_ci(BEACON["spearman"], BEACON["n"])

    def interp(c: str, target: str, bias: float, xcol: str, ycol: str, value: float) -> float:
        s = prop[(prop.config == c) & (prop.error_on == target) & (prop.bias_log10 == bias)].sort_values("sigma_log10")
        x, y = s[xcol].to_numpy(), s[ycol].to_numpy()
        if ycol == "spearman_mean":  # Spearman decreases with sigma: invert to get sigma for a given Spearman
            return float(np.interp(value, y[::-1], x[::-1]))
        return float(np.interp(value, x, y))

    matching = {}
    for c in ("A", "A_full", "B_abs"):
        for target in ("clint_only", "clint_and_fu"):
            sig = {lab: interp(c, target, 0.0, "sigma_log10", "spearman_mean", r)
                   for lab, r in (("point", BEACON["spearman"]), ("ci_low", ci[0]), ("ci_high", ci[1]))}
            s0 = prop[(prop.config == c) & (prop.error_on == target) & (prop.bias_log10 == 0.0)].sort_values("sigma_log10")
            matching[f"{c}_{target}"] = dict(
                sigma_for_spearman_0_79=sig["point"], sigma_range_for_ci=[sig["ci_high"], sig["ci_low"]],
                aafe_at_that_sigma={f"bias_{b}": interp(c, target, b, "sigma_log10", "aafe_mean", sig["point"]) for b in BIASES},
                pair_accuracy_at_that_sigma=interp(c, target, 0.0, "sigma_log10", "pair_accuracy_3fold_mean", sig["point"]),
                sigma_for_aafe_2_4_no_bias=float(np.interp(BEACON["fold_error"], s0["aafe_mean"], s0["sigma_log10"])),
                pair_accuracy_at_spearman_0_61=interp(c, target, 0.0, "sigma_log10", "pair_accuracy_3fold_mean",
                                                      interp(c, target, 0.0, "sigma_log10", "spearman_mean", BEACON["programs_spearman"])))
    # Regression-calibrated predictions (shrunk towards the mean) with Spearman about 0.79, config A
    lref = np.log10(ref["A"])
    calib = []
    for r in np.round(np.arange(0.70, 0.90, 0.01), 2):
        v = [(rho(p := 10 ** calibrated_pred(lref, r, rng), ref["A"]), aafe(p, ref["A"])) for _ in range(N_REP)]
        calib.append(dict(pearson_r=float(r), spearman_mean=float(np.mean([a for a, _ in v])),
                          aafe_mean=float(np.mean([b for _, b in v]))))
    calib = pd.DataFrame(calib)
    calib_match = float(np.interp(BEACON["spearman"], calib.spearman_mean, calib.aafe_mean))

    # 4. Potency: potency-fixed reference dose versus a dose that also varies with potency (reference vs reference)
    pot_rows = []
    for psd in POTENCY_SDS:
        for c in ("A", "A_full", "B_abs"):
            r = [rho(ref[c], ref[c] * 10 ** rng.normal(0, psd, n)) for _ in range(N_REP)]
            pot_rows.append(dict(potency_sd_log10=psd, config=c, spearman_potency_fixed_vs_full=float(np.mean(r)),
                                 p2_5=float(np.percentile(r, 2.5)), p97_5=float(np.percentile(r, 97.5))))
    pot = pd.DataFrame(pot_rows)

    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    prop.to_csv(out / "error_propagation.csv", index=False)
    pot.to_csv(out / "potency_sweep.csv", index=False)
    calib.to_csv(out / "calibrated_predictions.csv", index=False)
    summary = dict(counts=log, beacon2_reported=BEACON, beacon2_spearman_ci95=ci,
                   parameters=dict(qh=QH, bw=BW, tau=TAU, ka=KA, ic50_nm=IC50_NM, cover=COVER,
                                   mic_protein=MIC_PROTEIN, papp_half=PAPP_HALF, seed=SEED, n_rep=N_REP),
                   dependence=dependence, censoring_sensitivity_config_A=censoring,
                   sigma_matching_beacon=matching, calibrated_aafe_at_spearman_0_79_config_A=calib_match,
                   potency_sweep=pot_rows)
    (out / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("beacon2_spearman_ci95", "dependence", "censoring_sensitivity_config_A",
                                              "sigma_matching_beacon", "calibrated_aafe_at_spearman_0_79_config_A")}, indent=2))
    print(pot.to_string(index=False))
    plot(d, ref, prop, pot, dependence)


def replot() -> None:
    """Redraw the figure from saved results without rerunning the simulations."""
    d, _, _, _ = load()
    ref = {c: dose(c, *inputs(d)) for c in CONFIG_LABELS}
    summary = json.loads((ROOT / "results/summary.json").read_text(encoding="utf-8"))
    plot(d, ref, pd.read_csv(ROOT / "results/error_propagation.csv"), pd.read_csv(ROOT / "results/potency_sweep.csv"),
         summary["dependence"])


def plot(d: pd.DataFrame, ref: dict, prop: pd.DataFrame, pot: pd.DataFrame, dep: dict) -> None:
    fig, ax = plt.subplots(2, 2, figsize=(10.5, 8.6), constrained_layout=True)
    ax = ax.ravel()
    x = d[COL["clint"]]
    styles = {"A": (OKABE_ITO[0], "A: Cavg, minimal"), "A_full": (OKABE_ITO[2], "A': Cavg, + fu,mic + Fa"),
              "B_abs": (OKABE_ITO[1], "B: Cmin, Vss 1 L/kg")}
    for c, (color, lab) in styles.items():
        ax[0].scatter(x, ref[c] * MW_ILLUSTRATION / 1000, s=9, color=color, alpha=0.55, label=lab)
    ax[0].axhline(1000, color=OKABE_ITO[5], lw=0.8, ls="--")
    ax[0].text(0.12, 1300, "1 g/day", fontsize=8, color="#555555")
    ax[0].set(xscale="log", yscale="log", xlabel="Measured HLM CLint (mL/min/kg)",
              ylabel="Dose from measured inputs (mg/day, MW 450)", title=f"a. Reference dose vs HLM CLint (n = {len(d)})")
    ax[0].legend(fontsize=8, frameon=False)
    for c, (color, lab) in styles.items():
        s = prop[(prop.config == c) & (prop.error_on == "clint_only") & (prop.bias_log10 == 0.0)]
        ax[1].plot(s.sigma_log10, s.spearman_mean, color=color, marker="o", ms=3, label=lab)
        ax[1].fill_between(s.sigma_log10, s.spearman_p2_5, s.spearman_p97_5, color=color, alpha=0.15)
        if c == "B_abs":  # B's fold errors are off this scale; reported in summary.json
            continue
        ax[2].plot(s.sigma_log10, s.aafe_mean, color=color, marker="o", ms=3, label=f"{lab}, no bias")
        sb = prop[(prop.config == c) & (prop.error_on == "clint_only") & (prop.bias_log10 == 0.3)]
        ax[2].plot(sb.sigma_log10, sb.aafe_mean, color=color, ls=":", label=f"{lab}, 2-fold bias")
    ax[1].axhline(BEACON["spearman"], color=OKABE_ITO[5], lw=0.8)
    ax[1].text(0.45, BEACON["spearman"] + 0.015, "Beacon-2 reported 0.79", fontsize=8, color="#555555")
    ax[1].set(xlabel="SD of CLint prediction error (log10)", ylabel="Spearman vs measured-input dose",
              ylim=(0, 1.02), title="b. CLint error -> dose rank agreement")
    ax[1].legend(fontsize=8, frameon=False, loc="lower left")
    ax[2].axhline(BEACON["fold_error"], color=OKABE_ITO[5], lw=0.8)
    ax[2].axhline(dep["A"]["constant_dose_aafe_train_median"], color=OKABE_ITO[0], lw=0.8, ls="--")
    ax[2].text(0.55, BEACON["fold_error"] * 0.9, "Beacon-2 reported 2.4x", fontsize=8, color="#555555")
    ax[2].text(0.0, dep["A"]["constant_dose_aafe_train_median"] * 1.04,
               "A: same dose for all (train median)", fontsize=8, color=OKABE_ITO[0])
    ax[2].set(yscale="log", ylim=(1, 6), xlabel="SD of CLint prediction error (log10)",
              ylabel="Absolute average fold error (AAFE)", title="c. CLint error -> dose fold error (A, A')")
    ax[2].set_yticks([1, 1.5, 2, 3, 5], labels=["1", "1.5", "2", "3", "5"])
    ax[2].minorticks_off()
    ax[2].legend(fontsize=8, frameon=False, loc="upper left")
    for c, (color, lab) in styles.items():
        s = pot[pot.config == c]
        ax[3].errorbar(s.potency_sd_log10, s.spearman_potency_fixed_vs_full,
                       yerr=[s.spearman_potency_fixed_vs_full - s.p2_5, s.p97_5 - s.spearman_potency_fixed_vs_full],
                       color=color, marker="o", ms=4, capsize=3, label=lab)
    ax[3].set(xlabel="SD of potency across compounds (log10 IC50)",
              ylabel="Spearman: potency-fixed vs potency-varying dose", ylim=(0, 1.02),
              title="d. What fixing potency at 10 nM leaves out")
    ax[3].legend(fontsize=8, frameon=False, loc="lower left")
    for a in ax:
        a.spines[["top", "right"]].set_visible(False)
    (ROOT / "figures").mkdir(exist_ok=True)
    fig.savefig(ROOT / "figures/dose_decomposition.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    import sys

    replot() if "--replot" in sys.argv else main()
