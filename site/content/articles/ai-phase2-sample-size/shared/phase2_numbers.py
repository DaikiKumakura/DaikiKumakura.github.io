"""How many Phase II readouts are needed to say AI-discovered drugs succeed more often?

Run: python phase2_numbers.py
Binomial calculations only. Writes results/summary.json, results/required_n.csv and figures/*.png.
"""
from pathlib import Path
import csv
import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta, binom, binomtest

ROOT = Path(__file__).resolve().parent

# Inputs
AI_SUCCESS, AI_N = 4, 10  # illustration: ~40% Phase II on a small sample (Jayatunga et al. 2024); 10 readouts assumed
BASELINE = 0.289  # BIO/Informa/QLS 2011-2020, Phase II transition success (n = 4,933)
ALPHA = 0.05
POWER = 0.80
TRUE_RATES = [0.35, 0.40, 0.45, 0.50, 0.55, 0.60]
DESIGN_EFFECTS = [1.0, 1.5, 2.0]
EQUIV_MARGIN = 0.10  # equivalence margin around the baseline (absolute), for "no difference" claims
COMPARATOR_RATIOS = [5, 30]  # comparator group k times larger than the AI group  # inflation for programmes clustered within companies/targets
OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#000000", "#999999"]


def clopper_pearson(k: int, n: int, alpha: float = ALPHA) -> tuple[float, float]:
    lo = 0.0 if k == 0 else beta.ppf(alpha / 2, k, n - k + 1)
    hi = 1.0 if k == n else beta.ppf(1 - alpha / 2, k + 1, n - k)
    return float(lo), float(hi)


def exact_power_one_sample(p_true: float, p0: float, n: int, alpha: float = ALPHA) -> float:
    """Power of the two-sided exact binomial test of H0: p = p0, counting rejections in the upper tail."""
    ks = np.arange(n + 1)
    pvals = np.array([binomtest(int(k), n, p0, alternative="two-sided").pvalue for k in ks])
    reject_upper = (pvals < alpha) & (ks / n > p0)
    return float(binom.pmf(ks[reject_upper], n, p_true).sum())


def min_n_one_sample(p_true: float, p0: float, power: float = POWER, n_max: int = 2000) -> int:
    """Smallest n with power >= target, requiring the power to stay above target for the next 10 n (exact tests saw-tooth)."""
    for n in range(5, n_max):
        if all(exact_power_one_sample(p_true, p0, m) >= power for m in range(n, n + 10)):
            return n
    return -1


def first_n_reaching(p_true: float, p0: float, power: float = POWER, n_max: int = 2000) -> int:
    for n in range(5, n_max):
        if exact_power_one_sample(p_true, p0, n) >= power:
            return n
    return -1


def n_equivalence(p0: float, margin: float = EQUIV_MARGIN, power: float = POWER, alpha: float = ALPHA) -> int:
    """One-sample TOST vs a fixed baseline, true rate equal to the baseline (normal approximation)."""
    from scipy.stats import norm
    return int(np.ceil((norm.ppf(1 - alpha) + norm.ppf(1 - (1 - power) / 2)) ** 2 * p0 * (1 - p0) / margin ** 2))


def n_ai_unbalanced(p1: float, p0: float, k: float, power: float = POWER, alpha: float = ALPHA) -> int:
    """AI-group n when the comparator group is k times larger (normal approximation)."""
    from scipy.stats import norm
    za, zb = norm.ppf(1 - alpha / 2), norm.ppf(power)
    pbar = (p1 + k * p0) / (1 + k)
    num = (za * np.sqrt(pbar * (1 - pbar) * (1 + 1 / k)) + zb * np.sqrt(p1 * (1 - p1) + p0 * (1 - p0) / k)) ** 2
    return int(np.ceil(num / (p1 - p0) ** 2))


def n_two_sample(p1: float, p0: float, power: float = POWER, alpha: float = ALPHA) -> int:
    """Per-group n for a two-proportion comparison with a matched comparator of equal size (normal approximation)."""
    from scipy.stats import norm
    za, zb = norm.ppf(1 - alpha / 2), norm.ppf(power)
    pbar = (p1 + p0) / 2
    num = (za * np.sqrt(2 * pbar * (1 - pbar)) + zb * np.sqrt(p1 * (1 - p1) + p0 * (1 - p0))) ** 2
    return int(np.ceil(num / (p1 - p0) ** 2))


def main() -> None:
    ci = clopper_pearson(AI_SUCCESS, AI_N)
    test = binomtest(AI_SUCCESS, AI_N, BASELINE, alternative="two-sided")
    power_now = {f"{p:.2f}": exact_power_one_sample(p, BASELINE, AI_N) for p in TRUE_RATES}
    rows = []
    for p in TRUE_RATES:
        n1 = min_n_one_sample(p, BASELINE)
        n2 = n_two_sample(p, BASELINE)
        rows.append(dict(true_ai_rate=p, n_one_sample_vs_fixed_baseline=n1, n_first_reaching_80=first_n_reaching(p, BASELINE),
                         **{f"n_ai_comparator_{k}x": n_ai_unbalanced(p, BASELINE, k) for k in COMPARATOR_RATIOS},
                         n_per_group_vs_matched_comparator=n2,
                         **{f"n_one_sample_design_effect_{de}": int(np.ceil(n1 * de)) for de in DESIGN_EFFECTS[1:]}))
    widths = [dict(n=n, k=round(0.4 * n), lo=clopper_pearson(round(0.4 * n), n)[0], hi=clopper_pearson(round(0.4 * n), n)[1])
              for n in (10, 20, 30, 50, 100, 200)]
    summary = dict(ai_success=AI_SUCCESS, ai_n=AI_N, ai_rate=AI_SUCCESS / AI_N, ai_ci95_clopper_pearson=ci,
                   baseline=BASELINE, exact_binomial_p_vs_baseline=float(test.pvalue),
                   power_with_n10_by_true_rate=power_now, required_n=rows,
                   n_equivalence_margin_10pt=n_equivalence(BASELINE),
                   min_n_rule="smallest n whose exact power stays >= 80% for that n and the next 9 values (exact tests saw-tooth)", ci_at_40pct_by_n=widths,
                   notes=["exact binomial (Clopper-Pearson / binomtest); two-sample n uses the normal approximation",
                          "design effect multiplies n for clustered programmes; values are illustrative"])
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    with open(out / "required_n.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    (out / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    plot(rows, widths)
    print(json.dumps(summary, indent=2))


def plot(rows: list[dict], widths: list[dict]) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(10.2, 4.2), constrained_layout=True)
    n = [w["n"] for w in widths]
    ax[0].fill_between(n, [w["lo"] for w in widths], [w["hi"] for w in widths], color=OKABE_ITO[0], alpha=0.25,
                       label="95% CI if 40% of readouts succeed")
    ax[0].plot(n, [0.4] * len(n), color=OKABE_ITO[0])
    ax[0].axhline(BASELINE, color=OKABE_ITO[1], ls="--", label=f"Industry Phase II baseline {BASELINE:.1%}")
    ax[0].set(xscale="log", xticks=n, xticklabels=[str(v) for v in n], ylim=(0, 0.8),
              xlabel="Number of completed Phase II readouts", ylabel="Phase II success rate",
              title="a. Uncertainty around an observed 40%")
    ax[0].legend(fontsize=8, frameon=False, loc="upper right")
    p = [r["true_ai_rate"] for r in rows]
    ax[1].plot(p, [r["n_one_sample_vs_fixed_baseline"] for r in rows], marker="o", color=OKABE_ITO[0],
               label="vs a fixed industry baseline")
    ax[1].plot(p, [r["n_one_sample_design_effect_2.0"] for r in rows], marker="o", ls=":", color=OKABE_ITO[0],
               label="same, programmes clustered (design effect 2)")
    ax[1].plot(p, [r["n_per_group_vs_matched_comparator"] for r in rows], marker="s", color=OKABE_ITO[2],
               label="vs a matched non-AI group (per group)")
    ax[1].axhline(10, color=OKABE_ITO[5], lw=0.8)
    ax[1].text(0.352, 11.5, "readouts available (~10)", fontsize=8, color="#555555")
    ax[1].set(yscale="log", xlabel="Assumed true Phase II success rate of AI-discovered drugs",
              ylabel="Readouts needed for 80% power", title=f"b. Readouts needed to detect a difference from {BASELINE:.1%}")
    ax[1].legend(fontsize=8, frameon=False)
    for a in ax:
        a.spines[["top", "right"]].set_visible(False)
    (ROOT / "figures").mkdir(exist_ok=True)
    fig.savefig(ROOT / "figures/phase2_numbers.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    main()
