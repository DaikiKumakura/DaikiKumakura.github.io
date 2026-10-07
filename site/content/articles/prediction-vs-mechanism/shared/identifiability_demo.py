"""Synthetic identifiability example for an indirect-response (turnover) model.

Run: python identifiability_demo.py
Writes results/*.csv, results/summary.json and figures/identifiability.png.
Simulation only; no clinical or experimental data are used.

Model (Jusko indirect response model IV with a linear drug effect):
    dR/dt = kin - kout * (1 + S * C(t)) * R,  R(0) = R0 = kin / kout,
so that k_drug = S * kout in the notation of the article.
"""
from pathlib import Path
import csv
import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar

ROOT = Path(__file__).resolve().parent

# Analysis parameters (time unit: day)
SEED = 20261024
R0 = 100.0  # baseline response, assumed known
V = 5.0  # volume, L
KE = 0.1  # elimination rate, 1/day (half-life about 6.9 days)
DOSE = 100.0  # mg, observed design: one IV bolus
TRUE_KOUT = 2.0  # 1/day
TRUE_S = 0.075  # L/mg (k_drug = 0.15 L/mg/day)
LOG_SD = 0.10  # residual SD on log scale, assumed known
OBS_TIMES = np.array([1, 2, 4, 7, 14, 21, 28.0])
EARLY_TIMES = np.array([0.125, 0.25])  # 3 h and 6 h, alternative design only
KOUT_GRID = np.geomspace(0.1, 1000.0, 81)
S_GRID = np.linspace(0.03, 0.15, 121)
CHI2_95_1DF = 3.841  # 95% threshold for 2 * delta NLL, 1 df
NEW_REGIMEN = [(7.0 * k, 25.0) for k in range(12)]  # 25 mg once weekly, 12 doses
NEW_END = 84.0
EARLY_HOURS = 6.0
STEP = 0.002  # integration step, day
OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#000000", "#999999"]


def conc(t: np.ndarray, doses: list[tuple[float, float]]) -> np.ndarray:
    """One-compartment IV bolus concentration (mg/L)."""
    c = np.zeros_like(t)
    for td, a in doses:
        c += np.where(t >= td, a / V * np.exp(-KE * np.clip(t - td, 0.0, None)), 0.0)
    return c


def simulate(kout: float, s: float, doses: list[tuple[float, float]], t_end: float) -> tuple[np.ndarray, np.ndarray]:
    """Return (grid, R). The equation is linear in R: over each step the loss rate
    a = kout (1 + S C) is held at its midpoint value and the step is solved exactly."""
    n = int(np.ceil(t_end / STEP))
    grid = np.arange(n + 1) * STEP
    a = kout * (1.0 + s * conc(grid[:-1] + STEP / 2, doses))
    decay = np.exp(-a * STEP)
    gain = kout * R0 * (1.0 - decay) / a
    r = np.empty(n + 1)
    r[0] = R0
    for i in range(n):
        r[i + 1] = r[i] * decay[i] + gain[i]
    return grid, r


def at(times: np.ndarray, grid: np.ndarray, r: np.ndarray) -> np.ndarray:
    return np.interp(times, grid, r)


def direct_effect(s: float, times: np.ndarray, doses: list[tuple[float, float]]) -> np.ndarray:
    """Quasi-steady-state (direct-effect) limit: R = R0 / (1 + S C)."""
    return R0 / (1.0 + s * conc(times, doses))


def nll(pred: np.ndarray, y_obs: np.ndarray) -> float:
    return float(np.sum((np.log(y_obs) - np.log(pred)) ** 2) / (2 * LOG_SD**2))


def grid_nll(y_obs: np.ndarray, times: np.ndarray) -> np.ndarray:
    """Negative log-likelihood on the (kout, S) grid."""
    out = np.empty((KOUT_GRID.size, S_GRID.size))
    for i, kout in enumerate(KOUT_GRID):
        for j, s in enumerate(S_GRID):
            grid, r = simulate(float(kout), float(s), [(0.0, DOSE)], float(times.max()))
            out[i, j] = nll(at(times, grid, r), y_obs)
    return out


def kout_profile(y_obs: np.ndarray, times: np.ndarray) -> np.ndarray:
    """Profile NLL over kout, optimizing S continuously at each grid value."""
    prof = np.empty(KOUT_GRID.size)
    for i, kout in enumerate(KOUT_GRID):
        res = minimize_scalar(
            lambda s: nll(at(times, *simulate(float(kout), s, [(0.0, DOSE)], float(times.max()))), y_obs),
            bounds=(1e-4, 1.0), method="bounded", options={"xatol": 1e-7})
        prof[i] = res.fun
    return prof


def crossing_below(x: np.ndarray, y: np.ndarray, level: float) -> float | None:
    """Smallest x (log-linear interpolation) where y falls to the level, scanning upward."""
    for i in range(len(x) - 1):
        if y[i] > level >= y[i + 1]:
            w = (y[i] - level) / (y[i] - y[i + 1])
            return float(np.exp(np.log(x[i]) + w * (np.log(x[i + 1]) - np.log(x[i]))))
    return None


def crossing_above(x: np.ndarray, y: np.ndarray, level: float) -> float | None:
    """Largest x where y rises above the level after the minimum; None if it never does."""
    k = int(np.argmin(y))
    for i in range(k, len(x) - 1):
        if y[i] <= level < y[i + 1]:
            w = (level - y[i]) / (y[i + 1] - y[i])
            return float(np.exp(np.log(x[i]) + w * (np.log(x[i + 1]) - np.log(x[i]))))
    return None


def main() -> None:
    rng = np.random.default_rng(SEED)
    g, r = simulate(TRUE_KOUT, TRUE_S, [(0.0, DOSE)], 28.0)
    y_true = at(OBS_TIMES, g, r)
    y_obs = y_true * np.exp(rng.normal(0.0, LOG_SD, y_true.size))
    y_early = at(EARLY_TIMES, g, r) * np.exp(rng.normal(0.0, LOG_SD, EARLY_TIMES.size))

    # 2D grid: joint likelihood set used for derived quantities and predictions.
    surface = grid_nll(y_obs, OBS_TIMES)
    prof = kout_profile(y_obs, OBS_TIMES)
    sd = direct_effect_fit(y_obs, OBS_TIMES)
    best = min(float(surface.min()), float(prof.min()), sd["nll"])
    two_d = 2 * (surface - best)
    inside = np.argwhere(two_d <= CHI2_95_1DF)
    assert len(inside) > 10, "likelihood set too small"
    assert not two_d[:, 0].min() <= CHI2_95_1DF and not two_d[:, -1].min() <= CHI2_95_1DF, "S grid too narrow"

    t_new = np.arange(0.0, NEW_END + 1e-9, STEP)
    rows = []
    for i, j in inside:
        kout, s = float(KOUT_GRID[i]), float(S_GRID[j])
        gn, rn = simulate(kout, s, NEW_REGIMEN, NEW_END)
        ge, re = simulate(kout, s, [(0.0, DOSE)], 1.0)
        rows.append(dict(kout=kout, S=s, k_drug=kout * s, two_delta_nll=float(two_d[i, j]),
                         new_trough_day84=float(rn[-1]), new_min=float(rn.min()),
                         r_at_6h=float(at(np.array([EARLY_HOURS / 24]), ge, re)[0])))

    def span(key: str) -> list[float]:
        return [min(r[key] for r in rows), max(r[key] for r in rows)]

    # Alternative design with 3 h and 6 h samples added.
    times_alt = np.concatenate([EARLY_TIMES, OBS_TIMES])
    y_alt = np.concatenate([y_early, y_obs])
    prof_alt = kout_profile(y_alt, times_alt)
    two_alt = 2 * (prof_alt - prof_alt.min())

    # Noise-free data: is the upper flatness a property of the design?
    prof_free = kout_profile(y_true, OBS_TIMES)
    two_free = 2 * (prof_free - prof_free.min())

    two_prof = 2 * (prof - best)
    # Spread attributable to kout alone: S fixed at the grid value nearest the direct-effect estimate.
    s_fix = float(S_GRID[int(np.argmin(abs(S_GRID - sd["S"])))])
    summary = dict(
        seed=SEED, true_kout=TRUE_KOUT, true_S=TRUE_S, true_k_drug=TRUE_KOUT * TRUE_S, log_sd=LOG_SD,
        obs_times_day=OBS_TIMES.tolist(), observed=[round(float(v), 3) for v in y_obs],
        grid=dict(kout=[float(KOUT_GRID[0]), float(KOUT_GRID[-1]), KOUT_GRID.size],
                  S=[float(S_GRID[0]), float(S_GRID[-1]), S_GRID.size]),
        best_nll_turnover_grid=float(min(surface.min(), prof.min())),
        best_nll_direct_effect=sd["nll"], direct_effect_S=sd["S"],
        kout_at_profile_min=float(KOUT_GRID[int(np.argmin(prof))]),
        kout_lower_95=crossing_below(KOUT_GRID, two_prof, CHI2_95_1DF),
        kout_upper_95=crossing_above(KOUT_GRID, two_prof, CHI2_95_1DF),
        n_grid_points_in_set=len(rows),
        S_range_95=span("S"), new_trough_day84_range_95=span("new_trough_day84"),
        new_min_range_95=span("new_min"), r_at_6h_range_95=span("r_at_6h"),
        early_design_kout_lower_95=crossing_below(KOUT_GRID, two_alt, CHI2_95_1DF),
        early_design_kout_upper_95=crossing_above(KOUT_GRID, two_alt, CHI2_95_1DF),
        s_fixed=s_fix, kout_only_spans_at_s_fixed=dict(
            new_trough_day84=span_at(rows, s_fix, "new_trough_day84"), new_min=span_at(rows, s_fix, "new_min"),
            r_at_6h=span_at(rows, s_fix, "r_at_6h")),
        noise_free_two_delta_nll_at_kout_max=float(two_free[-1]),
        noise_free_kout_lower_95=crossing_below(KOUT_GRID, two_free, CHI2_95_1DF),
        noise_free_upper_95=crossing_above(KOUT_GRID, two_free, CHI2_95_1DF),
        note="Ranges are min/max over 2D grid points with 2*dNLL <= 3.841 (grid approximation of "
             "profile-likelihood intervals for each quantity).",
    )
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    with open(out / "likelihood_set.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    with open(out / "kout_profile.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["kout", "two_delta_nll_observed_design", "two_delta_nll_with_3h_6h", "two_delta_nll_noise_free"])
        for row in zip(KOUT_GRID, two_prof, two_alt, two_free):
            w.writerow([f"{v:.6g}" for v in row])
    (out / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    old = out / "profile.csv"
    if old.exists():
        old.unlink()
    plot(rows, y_obs, two_prof, two_alt, sd)
    print(json.dumps(summary, indent=2))


def span_at(rows: list[dict], s: float, key: str) -> list[float]:
    vals = [r[key] for r in rows if abs(r["S"] - s) < 1e-9]
    return [min(vals), max(vals)]


def direct_effect_fit(y_obs: np.ndarray, times: np.ndarray) -> dict:
    res = minimize_scalar(lambda s: nll(direct_effect(s, times, [(0.0, DOSE)]), y_obs),
                          bounds=(1e-4, 1.0), method="bounded", options={"xatol": 1e-9})
    return dict(S=float(res.x), nll=float(res.fun))


def plot(rows: list[dict], y_obs: np.ndarray, two_prof: np.ndarray, two_alt: np.ndarray, sd: dict) -> None:
    by_k = sorted(rows, key=lambda r: (r["kout"], r["two_delta_nll"]))
    low = min((r for r in rows if r["kout"] == by_k[0]["kout"]), key=lambda r: r["two_delta_nll"])
    mid = min(rows, key=lambda r: (abs(np.log(r["kout"] / TRUE_KOUT)), r["two_delta_nll"]))
    high = min((r for r in rows if r["kout"] == by_k[-1]["kout"]), key=lambda r: r["two_delta_nll"])
    picks = [low, mid, high]
    fig, ax = plt.subplots(2, 2, figsize=(10.5, 7.8), constrained_layout=True)
    for color, r in zip(OKABE_ITO, picks):
        label = f"turnover: k_out = {r['kout']:.2f}/day, S = {r['S']:.3f} L/mg"
        g, y = simulate(r["kout"], r["S"], [(0.0, DOSE)], 28.0)
        ax[0, 0].plot(g, y, color=color, label=label)
        g, y = simulate(r["kout"], r["S"], NEW_REGIMEN, NEW_END)
        ax[1, 0].plot(g, y, color=color)
        g, y = simulate(r["kout"], r["S"], [(0.0, DOSE)], 1.0)
        ax[1, 1].plot(g * 24, y, color=color)
    t = np.arange(0.0, 28.0 + 1e-9, 0.01)
    ax[0, 0].plot(t, direct_effect(sd["S"], t, [(0.0, DOSE)]), color=OKABE_ITO[5], ls="--",
                  label=f"direct effect (no turnover): S = {sd['S']:.3f} L/mg")
    ax[0, 0].scatter(OBS_TIMES, y_obs, color=OKABE_ITO[4], zorder=3, label=f"synthetic observations (n = {len(y_obs)})")
    ax[0, 0].set(title="a. Observed design: 100 mg once, sampling from day 1", xlabel="Time (day)",
                 ylabel="Response R (% of baseline)")
    ax[0, 0].legend(fontsize=7.5, frameon=False, loc="lower right")
    ax[0, 1].plot(KOUT_GRID, two_prof, color=OKABE_ITO[0], label="observed design (day 1–28)")
    ax[0, 1].plot(KOUT_GRID, two_alt, color=OKABE_ITO[3], label="with 3 h and 6 h samples added")
    ax[0, 1].axhline(CHI2_95_1DF, color=OKABE_ITO[4], ls="--", lw=1, label="95% threshold (3.84)")
    ax[0, 1].axvline(TRUE_KOUT, color=OKABE_ITO[1], ls=":", lw=1, label="true k_out (simulation)")
    ax[0, 1].set(xscale="log", ylim=(-1, 40), title="b. Profile likelihood of k_out",
                 xlabel="k_out (1/day, log scale)", ylabel="2 × Δ negative log-likelihood")
    ax[0, 1].legend(fontsize=7.5, frameon=False)
    ax[1, 0].set(title="c. Unobserved regimen: 25 mg once weekly × 12", xlabel="Time (day)",
                 ylabel="Response R (% of baseline)")
    ax[1, 1].set(title="d. Unobserved window: first 24 h after the 100 mg dose", xlabel="Time after dose (h)",
                 ylabel="Response R (% of baseline)")
    ax[1, 1].axvline(EARLY_HOURS, color=OKABE_ITO[5], lw=0.8)
    for a in ax.flat:
        a.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Synthetic example: parameter sets inside the 95% likelihood set (colors) are all compatible with the data", fontsize=11)
    (ROOT / "figures").mkdir(exist_ok=True)
    fig.savefig(ROOT / "figures" / "identifiability.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    main()
