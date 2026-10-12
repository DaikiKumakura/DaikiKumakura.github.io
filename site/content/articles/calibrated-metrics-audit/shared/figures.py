"""Figures from results/ (aggregate only). Run after analysis.py: python figures.py"""
import csv
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
M = ["mse", "pearson_all", "pearson_top50", "wmse", "nir"]
LAB = {"mse": "MSE", "pearson_all": "Pearson\n（全遺伝子Δ）", "pearson_top50": "Pearson\n（上位50遺伝子Δ）", "wmse": "重みつきMSE", "nir": "順位（NIR）"}
OKI = {"mean": "#0072B2", "clean": "#E69F00", "ctrl": "#999999"}


def fig1():
    fig, ax = plt.subplots(figsize=(8.2, 4))
    x = np.arange(len(M))
    for k, (key, lab, col) in enumerate((("R1_R4_vs_mean", "平均ベースライン（既定）", OKI["mean"]),
                                         ("sens_a_vs_mean_clean", "平均ベースライン（遺伝子を共有する摂動を除く）", OKI["clean"]),
                                         ("R1_vs_ctrl", "何もしない（control）", OKI["ctrl"]))):
        ax.bar(x + (k - 1) * 0.27, [S[key][m]["win_rate"] for m in M], 0.27, color=col, label=lab)
    ax.axhline(0.9, color="black", lw=.8, ls="--"); ax.text(len(M) - 0.5, 0.91, "較正の基準 0.90", ha="right", fontsize=8)
    ax.set_xticks(x); ax.set_xticklabels([LAB[m] for m in M], fontsize=8); ax.set_ylim(0.5, 1.12)
    ax.set_ylabel("技術的な重複が勝つ割合"); ax.legend(fontsize=7, frameon=False, loc="upper left")
    ax.set_title(f"同じ摂動の半分の細胞（陽性対照）が、基準より良いと判定される割合（{S['n_pert']}摂動×{S['n_split']}分割）", fontsize=9)
    fig.tight_layout(); fig.savefig(F / "01-win-rate.png", dpi=170); plt.close(fig)


def fig2():
    fig, ax = plt.subplots(figsize=(6.8, 4))
    for m, c in zip(M, ["#D55E00", "#CC79A7", "#009E73", "#0072B2", "#999999"]):
        y = [S["R3_by_effect_tercile_vs_mean"][f"tercile{k}"][m]["win_rate"] for k in (1, 2, 3)]
        ax.plot([1, 2, 3], y, "o-", color=c, label=LAB[m].replace("\n", ""))
    ax.axhline(0.9, color="black", lw=.8, ls="--")
    ax.set_xticks([1, 2, 3]); ax.set_xticklabels(["効果が小さい\n（下位1/3）", "中間", "効果が大きい\n（上位1/3）"])
    ax.set_ylabel("技術的な重複が平均ベースラインに勝つ割合"); ax.legend(fontsize=7, frameon=False, loc="lower right")
    ax.set_title("摂動の効果の大きさ別に見た判定の割合", fontsize=9)
    fig.tight_layout(); fig.savefig(F / "02-effect-size.png", dpi=170); plt.close(fig)


def fig3():
    rows = list(csv.DictReader(open(R / "per_perturbation.csv", encoding="utf-8")))
    fig, ax = plt.subplots(figsize=(7.4, 4))
    data = [[float(r[f"{m}_drf_vs_mean"]) for r in rows] for m in M]
    ax.boxplot(data, showfliers=False, tick_labels=[LAB[m] for m in M]); ax.axhline(0, color="grey", lw=.6)
    ax.tick_params(axis="x", labelsize=8)
    ax.set_ylabel("動的範囲の割合 DRF（摂動ごとの中央値）")
    ax.set_title("陽性対照が、陰性対照から理想までの差のどれだけを埋めるか（1が理想）", fontsize=9)
    fig.tight_layout(); fig.savefig(F / "03-dynamic-range.png", dpi=170); plt.close(fig)


if __name__ == "__main__":
    fig1(); fig2(); fig3()
    print(sorted(p.name for p in F.glob("*.png")))
