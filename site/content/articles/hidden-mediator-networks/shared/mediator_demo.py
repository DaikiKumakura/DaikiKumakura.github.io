"""Synthetic example for the essay on hidden mediators (no experimental data).

True system (linear, no direct x -> y term):
    dm/dt = a x(t) - lam m,     dy/dt = b m - gam y
An analyst who does not observe m fits a direct model to (x, y):
    dy/dt = k x(t) - g y
We compare a fast mediator (lam large: quasi-steady state holds) with a slow one, and two interventions:
    (1) doubling the upstream input x            -> total effect, mediator untouched
    (2) speeding up mediator removal (lam x 5)   -> acts on the hidden layer only
Run: python mediator_demo.py   (writes results/summary.json, results/fits.csv, figures/*.png)
"""
import csv
import json
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
(HERE / "results").mkdir(exist_ok=True)
(HERE / "figures").mkdir(exist_ok=True)
SEED = 20261008
A, B, GAM = 1.0, 1.0, 0.5            # production, action, decay of y (per day)
LAM = {"fast": 10.0, "slow": 0.3}    # mediator removal rate (per day)
T_END, DT_OBS, NOISE_SD = 60.0, 1.0, 0.02
T_OBS = np.arange(0.0, T_END + 1e-9, DT_OBS)


def x_input(t, scale=1.0):
    """Upstream signal: pulses of 3 days every 10 days, smoothed edges (abundance of the upstream organism)."""
    phase = np.mod(t, 10.0)
    return scale * (0.2 + 0.8 / (1 + np.exp(-8 * (phase - 1))) / (1 + np.exp(8 * (phase - 4))))


def true_system(lam, x_scale=1.0, lam_factor=1.0, t_eval=T_OBS):
    l = lam * lam_factor
    m0 = A * x_input(0.0, x_scale) / l
    y0 = B * m0 / GAM

    def rhs(t, z):
        m, y = z
        return [A * x_input(t, x_scale) - l * m, B * m - GAM * y]

    s = solve_ivp(rhs, (0, t_eval[-1]), [m0, y0], t_eval=t_eval, rtol=1e-10, atol=1e-12, max_step=0.05)
    return s.y[0], s.y[1]


def direct_model(k, g, y0, x_scale=1.0, t_eval=T_OBS):
    s = solve_ivp(lambda t, y: [k * x_input(t, x_scale) - g * y[0]], (0, t_eval[-1]), [y0], t_eval=t_eval,
                  rtol=1e-10, atol=1e-12, max_step=0.05)
    return s.y[0]


def multistart(residual, starts):
    """Least squares from several starting points; returns the best fit and how many starts reached it."""
    fits = [least_squares(residual, x0=x0, method="lm") for x0 in starts]
    ok = [f for f in fits if f.success]
    assert ok, "no start converged"
    best = min(ok, key=lambda f: f.cost)
    n_best = sum(abs(f.cost - best.cost) <= 1e-6 * max(best.cost, 1e-12) for f in ok)
    return best, n_best, len(starts)


def fit_direct(y_obs):
    starts = [[np.log(k), np.log(g), y_obs[0]] for k in (0.05, 0.5, 5.0) for g in (0.05, 0.5, 2.0)]
    best, n_best, n = multistart(lambda p: direct_model(np.exp(p[0]), np.exp(p[1]), p[2]) - y_obs, starts)
    return np.exp(best.x[0]), np.exp(best.x[1]), best.x[2], n_best, n


def two_step_model(c, r1, r2, x_scale=1.0, t_eval=T_OBS):
    """Hidden compartment: dm/dt = c x - r1 m, dy/dt = m - r2 y, started at the steady state for x(0)."""
    m0 = c * x_input(0.0, x_scale) / r1
    s = solve_ivp(lambda t, z: [c * x_input(t, x_scale) - r1 * z[0], z[0] - r2 * z[1]], (0, t_eval[-1]),
                  [m0, m0 / r2], t_eval=t_eval, rtol=1e-10, atol=1e-12, max_step=0.05)
    return s.y[1]


def fit_two_step(y_obs):
    starts = [[np.log(c), np.log(r1), np.log(r2)] for c in (0.3, 3.0) for r1, r2 in ((0.1, 1.0), (1.0, 0.1), (0.5, 5.0), (3.0, 0.3))]
    best, n_best, n = multistart(lambda p: two_step_model(*np.exp(p)) - y_obs, starts)
    c, r1, r2 = np.exp(best.x)
    return c, r1, r2, n_best, n


def r2(obs, pred):
    return 1 - np.sum((obs - pred) ** 2) / np.sum((obs - obs.mean()) ** 2)


def main():
    rng = np.random.default_rng(SEED)
    out, rows, curves = {}, [], {}
    last = T_OBS >= T_END - 20      # compare interventions after transients: mean level and peak-to-trough amplitude
    mean_ = lambda v: v[last].mean()
    amp_ = lambda v: v[last].max() - v[last].min()
    for name, lam in LAM.items():
        _, y = true_system(lam)
        y_obs = y * np.exp(rng.normal(0, NOISE_SD, y.size))
        k, g, y0, nb_d, n_d = fit_direct(y_obs)
        fit = direct_model(k, g, y0)
        c, r_a, r_b, nb_t, n_t = fit_two_step(y_obs)
        fit2 = two_step_model(c, r_a, r_b)
        _, y_x2 = true_system(lam, x_scale=2.0)
        _, y_lam5 = true_system(lam, lam_factor=5.0)
        pred_x2 = direct_model(k, g, 2 * y0, x_scale=2.0)
        # the two rates of the two-step model are interchangeable in y; either one may be the mediator's removal rate
        fast_r, slow_r = max(r_a, r_b), min(r_a, r_b)
        lab_true = (r_a, r_b) if abs(r_a - lam) < abs(r_b - lam) else (r_b, r_a)     # (mediator rate, y rate)
        lab_swap = (lab_true[1], lab_true[0])
        pred_true_label = two_step_model(c, lab_true[0] * 5, lab_true[1])
        pred_swap_label = two_step_model(c, lab_swap[0] * 5, lab_swap[1])
        res = {"lam": lam, "gam": GAM,
               "direct": {"k": k, "g": g, "r2": r2(y_obs, fit), "starts_reaching_best": f"{nb_d}/{n_d}",
                          "gain_k_over_g": k / g, "gain_true_ab_over_lam_gam": A * B / (lam * GAM),
                          "k_qss_ab_over_lam": A * B / lam},
               "two_step": {"c_ab": c, "rates": sorted([float(r_a), float(r_b)]), "r2": r2(y_obs, fit2),
                            "starts_reaching_best": f"{nb_t}/{n_t}",
                            "swap_max_abs_diff": float(np.max(np.abs(two_step_model(c, r_b, r_a) - fit2)))},
               "lag_days_peak": float(np.argmax(np.correlate(y - y.mean(), x_input(T_OBS) - x_input(T_OBS).mean(), "full"))
                                      - (T_OBS.size - 1)) * DT_OBS,
               "double_x": {"true_mean_ratio": mean_(y_x2) / mean_(y), "direct_mean_ratio": mean_(pred_x2) / mean_(fit)},
               "mediator_removal_x5": {
                   "true": {"mean_ratio": mean_(y_lam5) / mean_(y), "amplitude_ratio": amp_(y_lam5) / amp_(y)},
                   "two_step_correct_label": {"mean_ratio": mean_(pred_true_label) / mean_(fit2),
                                              "amplitude_ratio": amp_(pred_true_label) / amp_(fit2)},
                   "two_step_swapped_label": {"mean_ratio": mean_(pred_swap_label) / mean_(fit2),
                                              "amplitude_ratio": amp_(pred_swap_label) / amp_(fit2)},
                   "direct_model": "no parameter represents mediator removal; the fitted direct model alone cannot express this intervention"}}
        out[name] = res
        curves[name] = dict(y=y, y_obs=y_obs, fit=fit, fit2=fit2, y_lam5=y_lam5, p_true=pred_true_label, p_swap=pred_swap_label)
        for t, a_, b_, b2, c_ in zip(T_OBS, y_obs, fit, fit2, y):
            rows.append(dict(scenario=name, t=t, y_observed=a_, direct_fit=b_, two_step_fit=b2, y_true=c_))
    (HERE / "results/summary.json").write_text(json.dumps(out, indent=2) + chr(10))
    with open(HERE / "results/fits.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    figure(curves, out)
    print(json.dumps(out, indent=2))


def figure(curves, out):
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    try:
        plt.rcParams["font.family"] = ["Yu Gothic", "Meiryo", "sans-serif"]
    except Exception:
        pass
    fig, axes = plt.subplots(2, 2, figsize=(10, 6.6), sharex=True)
    t_fine = np.linspace(0, T_END, 601)
    for j, name in enumerate(["fast", "slow"]):
        c, r = curves[name], out[name]
        ax = axes[0, j]
        ax.plot(t_fine, x_input(t_fine) * (max(c["y"]) / 1.0) * 0.9, color="#bbbbbb", lw=1, label="上流 x（縮尺は任意）")
        ax.plot(T_OBS, c["y_obs"], "o", ms=3, color="#333333", label="観測 y")
        ax.plot(T_OBS, c["fit"], color="#d55e00", lw=1.6, label="直接モデルの当てはめ")
        ax.plot(T_OBS, c["fit2"], ":", color="#009e73", lw=1.8, label="隠れた区画を1つ入れた2段モデルの当てはめ")
        lab = "速い媒介（λ = 10/日）" if name == "fast" else "遅い媒介（λ = 0.3/日）"
        ax.set_title(f"{lab}　R²：直接 {r['direct']['r2']:.3f}、2段 {r['two_step']['r2']:.3f}", fontsize=10)
        ax.set_ylabel("y")
        ax = axes[1, j]
        ax.plot(T_OBS, c["y"], color="#333333", lw=1.4, label="真の系：介入なし")
        ax.plot(T_OBS, c["y_lam5"], color="#0072b2", lw=1.8, label="真の系：媒介物の除去を5倍に")
        ax.plot(T_OBS, c["p_true"], "--", color="#009e73", lw=1.4, label="2段モデルの予測：媒介物の速度を正しく選んだ場合")
        ax.plot(T_OBS, c["p_swap"], ":", color="#cc79a7", lw=2.0, label="2段モデルの予測：もう一方の速度を媒介物と取り違えた場合")
        ax.set_xlabel("時間（日）")
        ax.set_ylabel("y")
    h0, l0 = axes[0, 0].get_legend_handles_labels(); h1, l1 = axes[1, 0].get_legend_handles_labels()
    fig.legend(h0, l0, loc="upper center", ncol=2, frameon=False, fontsize=9, bbox_to_anchor=(0.5, 1.0))
    fig.legend(h1, l1, loc="lower center", ncol=2, frameon=False, fontsize=9, bbox_to_anchor=(0.5, 0.0))
    fig.set_size_inches(10, 7.4)
    fig.tight_layout(rect=(0, 0.08, 1, 0.92))
    fig.savefig(HERE / "figures/mediator-fit-and-intervention.png", dpi=170)
    plt.close(fig)

    # schematic of the three structures
    fig, axes = plt.subplots(1, 3, figsize=(10, 2.4))
    specs = [("直接", [("X", 0.1), ("Y", 0.9)], [(0, 1, "")]),
             ("媒介", [("X", 0.1), ("M", 0.5), ("Y", 0.9)], [(0, 1, ""), (1, 2, "")]),
             ("交絡", [("X", 0.1), ("U", 0.5), ("Y", 0.9)], [(1, 0, ""), (1, 2, "")])]
    for ax, (title, nodes, edges) in zip(axes, specs):
        ax.set_xlim(0, 1); ax.set_ylim(0.15, 0.95); ax.set_aspect("equal"); ax.axis("off"); ax.set_title(title)
        pos = {}
        for i, (lab, x) in enumerate(nodes):
            y = 0.75 if lab == "U" else 0.35
            pos[i] = (x, y)
            dashed = lab in ("M", "U")
            ax.add_patch(plt.Circle((x, y), 0.09, fill=False, lw=1.5, ls="--" if dashed else "-",
                                    color="#0072b2" if dashed else "#333333"))
            ax.text(x, y, lab, ha="center", va="center", fontsize=13)
        for s, e, _ in edges:
            (x0, y0), (x1, y1) = pos[s], pos[e]
            v = np.array([x1 - x0, y1 - y0]); v = v / np.linalg.norm(v)
            ax.annotate("", xy=(x1 - 0.1 * v[0], y1 - 0.1 * v[1]), xytext=(x0 + 0.1 * v[0], y0 + 0.1 * v[1]),
                        arrowprops=dict(arrowstyle="->", lw=1.5))
    fig.text(0.5, 0.02, "破線の丸：観測されないことの多い変数", ha="center", fontsize=9, color="#0072b2")
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(HERE / "figures/three-structures.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    main()
