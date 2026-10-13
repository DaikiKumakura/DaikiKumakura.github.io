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




def fig4():
    """Three datasets: win rates by metric and MSE win rate by effect tercile (needs summary_*.json from analysis_stream.py)."""
    names = [("wessels_stream", "Wessels（THP-1、Cas13）"), ("norman", "Norman（K562、CRISPRa）"), ("replogle_essential", "Replogle essential（K562、CRISPRi）")]
    D = {k: json.load(open(R / f"summary_{k}.json", encoding="utf-8")) for k, _ in names}
    cols = ["#0072B2", "#E69F00", "#009E73"]
    fig, ax = plt.subplots(1, 2, figsize=(11, 4), gridspec_kw={"width_ratios": [1.6, 1]})
    x = np.arange(len(M))
    for k, ((key, lab), c) in enumerate(zip(names, cols)):
        ax[0].bar(x + (k - 1) * 0.27, [D[key]["R1_R4_vs_mean"][m]["win_rate"] for m in M], 0.27, color=c,
                  label=f"{lab}：差次発現遺伝子数の中央値 {D[key]['median_ndeg']:.0f}")
    ax[0].axhline(0.9, color="black", lw=.8, ls="--")
    ax[0].set_xticks(x); ax[0].set_xticklabels([LAB[m] for m in M], fontsize=8); ax[0].set_ylim(0, 1.25)
    ax[0].set_ylabel("技術的な重複が平均ベースラインに勝つ割合"); ax[0].legend(fontsize=7, frameon=False, loc="upper left")
    ax[0].set_title("同じ点検を3つのデータで行った結果", fontsize=9)
    for (key, lab), c in zip(names, cols):
        ax[1].plot([1, 2, 3], [D[key]["R3_by_effect_tercile_vs_mean"][f"tercile{t}"]["mse"]["win_rate"] for t in (1, 2, 3)], "o-", color=c, label=lab.split("（")[0])
    ax[1].axhline(0.9, color="black", lw=.8, ls="--"); ax[1].set_ylim(0, 1.02)
    ax[1].set_xticks([1, 2, 3]); ax[1].set_xticklabels(["効果が小さい", "中間", "効果が大きい"], fontsize=8)
    ax[1].set_ylabel("MSEでの勝率"); ax[1].legend(fontsize=7, frameon=False, loc="lower right"); ax[1].set_title("MSEは、効果の大きさで、勝率が大きく変わる", fontsize=9)
    fig.tight_layout(); fig.savefig(F / "04-three-datasets.png", dpi=170); plt.close(fig)


if __name__ == "__main__":
    fig1(); fig2(); fig3()
    if all((R / f"summary_{k}.json").exists() for k in ("wessels_stream", "norman", "replogle_essential")):
        fig4()
    print(sorted(p.name for p in F.glob("*.png")))
