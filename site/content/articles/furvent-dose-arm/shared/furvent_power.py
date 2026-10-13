"""FURVENT: how much did the second dose arm cost the primary comparison?

Run: python furvent_power.py
Uses only numbers reported in the sponsor's 2026-10-06 topline release and the registry.
Writes results/summary.json, results/power_curves.csv and figures/*.png.
"""
from pathlib import Path
import csv
import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

ROOT = Path(__file__).resolve().parent

# Reported (topline press release, 2026-10-06; ClinicalTrials.gov NCT05607550)
N_ENROLLED = 398  # three arms, planned 1:1:1
BICR = {"240": dict(hr=0.75, lo=0.55, hi=1.02, p=0.0654, med=11.0), "160": dict(hr=0.91, lo=0.67, hi=1.25, med=8.4)}
INV = {"240": dict(hr=0.61, lo=0.46, hi=0.81, med=11.1), "160": dict(hr=0.86, lo=0.65, hi=1.14, med=8.3)}
MED_CONTROL = dict(bicr=9.5, inv=7.1)
ORR = {"bicr": {"240": 0.60, "160": 0.35, "control": 0.33}, "inv": {"240": 0.61, "160": 0.41, "control": 0.28}}
# WU-KONG28 (sunvozertinib vs chemotherapy, 2 arms 1:1, n = 324; Zhou et al. NEJM 2026)
WUKONG28 = dict(hr=0.65, lo=0.50, hi=0.85, p=0.0008, n=324, med_control=7.5)
# Meta-analysis of 49 Roche trials: HR_BICR / HR_local, open-label comparisons (Lian et al. 2023)
HRR_OPEN_LABEL = dict(est=1.062, lo=1.016, hi=1.110)

# Analysis settings
Z975 = norm.ppf(0.975)
HR_GRID = np.round(np.arange(0.50, 1.0001, 0.01), 2)
OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#000000", "#999999"]


def se_from_ci(lo: float, hi: float) -> float:
    return float((np.log(hi) - np.log(lo)) / (2 * Z975))


def events_from_se(se: float) -> float:
    """Schoenfeld approximation for 1:1 allocation: Var(log HR) = 4 / D."""
    return 4 / se**2


def power(hr: float, events: float, alpha: float) -> float:
    """Two-sided log-rank power (Schoenfeld, 1:1), counting only the favorable tail."""
    return float(norm.cdf(abs(np.log(hr)) * np.sqrt(events) / 2 - norm.ppf(1 - alpha / 2)))


def events_needed(hr: float, alpha: float, pw: float) -> float:
    return float(4 * (norm.ppf(1 - alpha / 2) + norm.ppf(pw)) ** 2 / np.log(hr) ** 2)


def main() -> None:
    se240_ci = se_from_ci(BICR["240"]["lo"], BICR["240"]["hi"])
    se240_p = float(abs(np.log(BICR["240"]["hr"])) / norm.ppf(1 - BICR["240"]["p"] / 2))
    se160_ci = se_from_ci(BICR["160"]["lo"], BICR["160"]["hi"])
    d240 = events_from_se(se240_ci)
    d160 = events_from_se(se160_ci)
    assert abs(se240_ci - se240_p) / se240_p < 0.05, "CI and p-value disagree"

    # Two-arm counterfactual: same enrolment, 240 mg vs control only (1:1), same event rate per patient.
    n_pair = N_ENROLLED * 2 / 3
    scale = N_ENROLLED / n_pair
    d_two_arm = d240 * scale

    # Rounding: reported CI limits carry two decimals, so each limit may be off by up to 0.005.
    se_range = [se_from_ci(BICR["240"]["lo"] + 0.005, BICR["240"]["hi"] - 0.005),
                se_from_ci(BICR["240"]["lo"] - 0.005, BICR["240"]["hi"] + 0.005)]
    d240_range = sorted(events_from_se(s) for s in se_range)
    hr_boundary = {a: float(np.exp(-norm.ppf(1 - a / 2) * 2 / np.sqrt(d240))) for a in (0.05, 0.025)}
    detectable = {pw: float(np.exp(-(Z975 + norm.ppf(pw)) * 2 / np.sqrt(d240))) for pw in (0.8, 0.9)}
    wk_se_ci = se_from_ci(WUKONG28["lo"], WUKONG28["hi"])
    wk_se_p = float(abs(np.log(WUKONG28["hr"])) / norm.ppf(1 - WUKONG28["p"] / 2))
    wk_events = sorted([events_from_se(wk_se_ci), events_from_se(wk_se_p)])

    rows = [dict(true_hr=float(hr), power_three_arm_a05=power(hr, d240, 0.05),
                 power_three_arm_a025=power(hr, d240, 0.025), power_two_arm_a05=power(hr, d_two_arm, 0.05))
            for hr in HR_GRID]

    # 240 mg vs 160 mg (shared control): equal events per arm within each pairwise comparison;
    # the control-arm variance cancels in the contrast of the two log HRs.
    var_diff = 1 / (d240 / 2) + 1 / (d160 / 2)
    log_ratio = np.log(BICR["240"]["hr"]) - np.log(BICR["160"]["hr"])
    se_diff = float(np.sqrt(var_diff))
    hr_240_vs_160 = dict(est=float(np.exp(log_ratio)), lo=float(np.exp(log_ratio - Z975 * se_diff)),
                         hi=float(np.exp(log_ratio + Z975 * se_diff)))

    # ORR difference 240 vs 160 (BICR), arms assumed equal in size (N/3)
    n_arm = N_ENROLLED / 3
    p1, p2 = ORR["bicr"]["240"], ORR["bicr"]["160"]
    se_orr = float(np.sqrt(p1 * (1 - p1) / n_arm + p2 * (1 - p2) / n_arm))
    orr_diff = dict(est=p1 - p2, lo=p1 - p2 - Z975 * se_orr, hi=p1 - p2 + Z975 * se_orr)

    summary = dict(
        se_log_hr_240_from_ci=se240_ci, se_log_hr_240_from_p=se240_p,
        implied_events_240_vs_control=d240, implied_events_160_vs_control=d160,
        implied_events_240_rounding_range=d240_range, significance_boundary_hr=hr_boundary,
        detectable_hr_with_implied_events={"power_0.8": detectable[0.8], "power_0.9": detectable[0.9]},
        wukong28_implied_events_from_ci_and_p=wk_events,
        two_arm_scale=scale, implied_events_two_arm=d_two_arm,
        power_at_hr_0_75=dict(three_arm_a05=power(0.75, d240, 0.05), three_arm_a025=power(0.75, d240, 0.025),
                              two_arm_a05=power(0.75, d_two_arm, 0.05)),
        power_at_hr_0_65=dict(three_arm_a05=power(0.65, d240, 0.05), three_arm_a025=power(0.65, d240, 0.025),
                              two_arm_a05=power(0.65, d_two_arm, 0.05)),
        power_at_hr_0_60=dict(three_arm_a05=power(0.60, d240, 0.05), two_arm_a05=power(0.60, d_two_arm, 0.05)),
        events_needed_hr_0_75=dict(p80_a05=events_needed(0.75, 0.05, 0.8), p90_a05=events_needed(0.75, 0.05, 0.9)),
        events_needed_hr_0_65=dict(p80_a05=events_needed(0.65, 0.05, 0.8), p90_a05=events_needed(0.65, 0.05, 0.9)),
        hr_240_vs_160_bicr=hr_240_vs_160, orr_diff_240_vs_160_bicr=orr_diff,
        hr_ratio_bicr_over_inv={arm: BICR[arm]["hr"] / INV[arm]["hr"] for arm in ("240", "160")},
        hrr_open_label_meta=HRR_OPEN_LABEL,
        median_shift_inv_minus_bicr=dict(arm240=INV["240"]["med"] - BICR["240"]["med"],
                                         arm160=INV["160"]["med"] - BICR["160"]["med"],
                                         control=MED_CONTROL["inv"] - MED_CONTROL["bicr"]),
        assumptions=["Schoenfeld approximation with 1:1 allocation within each pairwise comparison",
                     "two-arm counterfactual keeps total enrolment and per-patient event rate",
                     "arms of equal size (N/3) for ORR; the trial's multiplicity rule is not public"],
    )
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    with open(out / "power_curves.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    (out / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    plot_power(rows, d240, d_two_arm)
    plot_assessment()
    print(json.dumps(summary, indent=2))


def plot_power(rows: list[dict], d3: float, d2: float) -> None:
    hr = [r["true_hr"] for r in rows]
    fig, ax = plt.subplots(figsize=(7.4, 4.6), constrained_layout=True)
    ax.plot(hr, [r["power_three_arm_a05"] for r in rows], color=OKABE_ITO[0],
            label=f"Actual 3-arm trial: ~{d3:.0f} events (240 mg vs chemo), two-sided α 0.05")
    ax.plot(hr, [r["power_three_arm_a025"] for r in rows], color=OKABE_ITO[0], ls="--",
            label="Same, if α were split over the two dose arms (0.025)")
    ax.plot(hr, [r["power_two_arm_a05"] for r in rows], color=OKABE_ITO[1],
            label=f"Hypothetical 2-arm trial, same enrolment: ~{d2:.0f} events, α 0.05")
    ax.axvline(0.75, color=OKABE_ITO[5], lw=0.8)
    ax.text(0.755, 0.03, "FURVENT observed HR 0.75", fontsize=8, color="#555555")
    ax.axvline(0.65, color=OKABE_ITO[5], lw=0.8, ls="--")
    ax.text(0.655, 0.10, "WU-KONG28 observed HR 0.65", fontsize=8, color="#555555")
    ax.axhline(0.8, color=OKABE_ITO[4], lw=0.6, ls=":")
    ax.set(xlabel="Assumed true hazard ratio, 240 mg vs chemotherapy", ylabel="Power of the primary comparison",
           ylim=(0, 1), xlim=(0.5, 1.0), title="Power of the 240 mg vs chemotherapy comparison")
    ax.legend(fontsize=7.5, frameon=False, loc="upper right")
    ax.spines[["top", "right"]].set_visible(False)
    (ROOT / "figures").mkdir(exist_ok=True)
    fig.savefig(ROOT / "figures" / "power.png", dpi=160)
    plt.close(fig)


def plot_assessment() -> None:
    fig, ax = plt.subplots(1, 2, figsize=(9.4, 3.9), constrained_layout=True)
    labels = ["240 mg vs chemo", "160 mg vs chemo"]
    for k, (src, name, color) in enumerate([(BICR, "Central review (BICR, primary)", OKABE_ITO[0]),
                                            (INV, "Investigator", OKABE_ITO[1])]):
        for i, arm in enumerate(("240", "160")):
            y = i + (-0.12 if k == 0 else 0.12)
            ax[0].errorbar(src[arm]["hr"], y,
                           xerr=[[src[arm]["hr"] - src[arm]["lo"]], [src[arm]["hi"] - src[arm]["hr"]]],
                           fmt="o", color=color, capsize=3, label=name if i == 0 else None)
    ax[0].axvline(1, color=OKABE_ITO[5], lw=0.8)
    ax[0].set(xscale="log", yticks=[0, 1], yticklabels=labels, xlabel="PFS hazard ratio (95% CI, log scale)",
              title="a. Reported PFS hazard ratios", ylim=(1.5, -0.5))
    ax[0].set_xticks([0.5, 0.75, 1.0, 1.25])
    ax[0].set_xticklabels(["0.5", "0.75", "1", "1.25"])
    ax[0].minorticks_off()
    ax[0].legend(fontsize=8, frameon=False, loc="lower left")
    arms = ["240 mg", "160 mg", "Chemotherapy"]
    b = [BICR["240"]["med"], BICR["160"]["med"], MED_CONTROL["bicr"]]
    inv = [INV["240"]["med"], INV["160"]["med"], MED_CONTROL["inv"]]
    x = np.arange(3)
    ax[1].bar(x - 0.18, b, 0.36, color=OKABE_ITO[0], label="BICR")
    ax[1].bar(x + 0.18, inv, 0.36, color=OKABE_ITO[1], label="Investigator")
    for xi, (u, v) in enumerate(zip(b, inv)):
        ax[1].text(xi - 0.18, u + 0.15, f"{u}", ha="center", fontsize=8)
        ax[1].text(xi + 0.18, v + 0.15, f"{v}", ha="center", fontsize=8)
    ax[1].set(xticks=x, xticklabels=arms, ylabel="Median PFS (months)", ylim=(0, 13), title="b. Median PFS by assessor")
    ax[1].legend(fontsize=8, frameon=False, loc="upper right")
    for a in ax:
        a.spines[["top", "right"]].set_visible(False)
    fig.suptitle(f"FURVENT topline as reported by the sponsor (n = {N_ENROLLED} enrolled, 3 arms)", fontsize=10)
    fig.savefig(ROOT / "figures" / "assessment.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    main()
