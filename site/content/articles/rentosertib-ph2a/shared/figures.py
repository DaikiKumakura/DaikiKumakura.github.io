"""Figures from results/ (aggregate only). Run after analysis.py: python figures.py"""
import json
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
R, F = HERE / "results", HERE / "figures"
F.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "font.family": ["Yu Gothic", "Meiryo", "sans-serif"]})
S = json.load(open(R / "summary.json", encoding="utf-8"))
ARMS = ["placebo", "r30qd", "r30bid", "r60qd"]
LAB = {"placebo": "プラセボ", "r30qd": "30 mg QD", "r30bid": "30 mg BID", "r60qd": "60 mg QD"}
COL = {"obs": "#0072B2", "mar": "#E69F00", "ref": "#009E73"}


def fig1():
    fig, ax = plt.subplots(1, 2, figsize=(11, 4), gridspec_kw={"width_ratios": [1.5, 1]})
    a = ax[0]
    x = np.arange(4)
    A, Z = S["arms"], 1.96
    obs = [(A[k]["mo"], A[k]["se_obs_norm"]) for k in ARMS]
    mar = [(A[k]["mmi"], A[k]["se_mi"]) for k in ARMS]
    ref = [(S["E5_jump_to_placebo_reference"]["placebo_arm_mean"] if k == "placebo" else S["E5_jump_to_placebo_reference"]["arms"][k]["arm_mean"], None) for k in ARMS]
    a.errorbar(x - 0.2, [m for m, _ in obs], yerr=[Z * s for _, s in obs], fmt="o", color=COL["obs"], capsize=3, label="観測された人（完了例）")
    a.errorbar(x + 0.2, [m for m, _ in mar], yerr=[Z * s for _, s in mar], fmt="s", color=COL["mar"], capsize=3, label="全員、欠測はMAR（多重補完）")
    a.plot(x, [m for m, _ in ref], "^", color=COL["ref"], label="全員、欠測は「プラセボの経過」")
    a.axhline(0, color="grey", lw=.6)
    a.set_xticks(x); a.set_xticklabels([f"{LAB[k]}\n観測 {A[k]['no']}／割付 {A[k]['nr']}" for k in ARMS], fontsize=8)
    a.set_ylabel("12週目のFVC変化（mL、平均と95%CI）"); a.legend(fontsize=7, frameon=False, loc="upper left")
    a.set_title("欠測の仮定で、群の平均は変わる", fontsize=9)
    b = ax[1]
    e1, e2 = S["E1_observed_vs_placebo"]["r60qd"], S["E2_mar_mi_vs_placebo"]["r60qd"]
    e5 = S["E5_jump_to_placebo_reference"]["arms"]["r60qd"]
    ys = [(e1["diff"], e1["ci"], COL["obs"], "観測された人"), (e2["diff"], e2["ci"], COL["mar"], "MAR（多重補完）"), (e5["mean_diff"], e5["ci"], COL["ref"], "プラセボの経過")]
    for i, (d, ci, c, lab) in enumerate(ys):
        b.errorbar([d], [i], xerr=[[d - ci[0]], [ci[1] - d]], fmt="o", color=c, capsize=3)
        b.text(ci[1] + 6, i, f"{d:+.0f}（{ci[0]:+.0f}〜{ci[1]:+.0f}）", va="center", fontsize=8)
    b.axvline(0, color="black", lw=.8); b.set_yticks(range(3)); b.set_yticklabels([y[3] for y in ys], fontsize=8)
    b.set_xlim(-60, 380); b.invert_yaxis(); b.set_xlabel("60 mg QD − プラセボ（mL、95%CI）")
    b.set_title("どの仮定でも、差のCIは0を含む", fontsize=9)
    fig.tight_layout(); fig.savefig(F / "01-estimates-by-assumption.png", dpi=170); plt.close(fig)


def fig2():
    t = S["E4_tipping"]["grid"]
    d = np.array([g["delta_ml"] for g in t]); diff = np.array([g["diff"] for g in t]); lo = np.array([g["ci"][0] for g in t]); hi = np.array([g["ci"][1] for g in t]); p = np.array([g["p_gt0"] for g in t])
    fig, ax = plt.subplots(figsize=(7.4, 4))
    ax.fill_between(d, lo, hi, color=COL["mar"], alpha=.2); ax.plot(d, diff, color=COL["mar"], lw=2)
    ax.axhline(0, color="black", lw=.8)
    ax.axvline(S["E4_tipping"]["delta_p_gt0_0p80"], color="grey", ls="--", lw=.8); ax.text(S["E4_tipping"]["delta_p_gt0_0p80"] + 3, ax.get_ylim()[1] * 0.9, f"P(差>0)=0.80\nδ={S['E4_tipping']['delta_p_gt0_0p80']:.0f}", fontsize=8)
    ax.axvline(S["E4_tipping"]["delta_point_estimate_zero"], color="grey", ls="--", lw=.8); ax.text(S["E4_tipping"]["delta_point_estimate_zero"] + 3, ax.get_ylim()[1] * 0.6, f"点推定=0\nδ={S['E4_tipping']['delta_point_estimate_zero']:.0f}", fontsize=8)
    ax.set_xlabel("δ：実薬群の欠測の人に、MARの補完値から引く量（mL）"); ax.set_ylabel("60 mg QD − プラセボ（mL、95%CI）")
    ax2 = ax.twinx(); ax2.plot(d, p, color="#0072B2", lw=1.2, ls=":"); ax2.set_ylim(0, 1); ax2.set_ylabel("P(差 > 0)", color="#0072B2"); ax2.spines["right"].set_visible(True)
    ax.set_title("欠測の人が悪化する方向に仮定を動かしたときの差", fontsize=9)
    fig.tight_layout(); fig.savefig(F / "02-tipping-point.png", dpi=170); plt.close(fig)


def fig3():
    a = S["E8_assurance_sd150_prior_sd150"]
    ns = [30, 60, 100, 200, 400]
    fig, ax = plt.subplots(figsize=(6.4, 4))
    for key, lab, c in (("MAR_mi", "欠測はMAR", COL["mar"]), ("jump_to_placebo", "欠測は「プラセボの経過」", COL["ref"]), ("delta100", "δ=100 mL", "#D55E00")):
        ax.plot(ns, [a[key]["assurance"][str(n)] for n in ns], "o-", color=c, label=f"{lab}（事後でΔ>0の確率 {a[key]['p_delta_gt0']:.2f}）")
        ax.axhline(a[key]["p_delta_gt0"], color=c, lw=.5, ls=":")
    ax.set_xscale("log"); ax.set_xticks(ns); ax.set_xticklabels([str(n) for n in ns]); ax.minorticks_off(); ax.set_ylim(0, 1); ax.set_xlabel("1群あたりの割り付け人数（対数軸、欠測30%）"); ax.set_ylabel("期待される成功確率（事後予測）")
    ax.legend(fontsize=7, frameon=False, loc="lower right"); ax.set_title("例数を増やしても、成功確率は事後の確率で頭打ち（点線）", fontsize=9)
    fig.tight_layout(); fig.savefig(F / "03-assurance.png", dpi=170); plt.close(fig)


if __name__ == "__main__":
    fig1(); fig2(); fig3()
    print(sorted(p.name for p in F.glob("*.png")))
