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
LINES = ["HCT116", "CACO2", "HT29"]
COL = {"HCT116": "#0072B2", "CACO2": "#E69F00", "HT29": "#009E73"}
MAIN = "Large Intestine-mature Enterocyte"


def fig1():
    fig, ax = plt.subplots(1, 3, figsize=(11, 3.6), sharey=True)
    for a, l in zip(ax, LINES):
        e = S["e1_targets"][l]
        x = np.arange(3)
        a.bar(x - 0.18, [e[t]["ctrl_cpm"] for t in e], 0.36, color="#999999", label="対照（N）")
        a.bar(x + 0.18, [e[t]["kd_cpm"] for t in e], 0.36, color=COL[l], label="3つ同時ノックダウン（MHF）")
        a.set_yscale("log"); a.set_xticks(x); a.set_xticklabels(list(e))
        a.axhline(2, color="grey", lw=.7, ls=":")
        for i, t in enumerate(e):
            lab = "未発現" if not e[t]["expressed"] else f"−{e[t]['knockdown_pct']:.0f}%"
            a.text(i, max(e[t]["ctrl_cpm"], e[t]["kd_cpm"]) * 1.5, lab, ha="center", fontsize=9)
        a.set_title(l, fontsize=10)
    ax[0].set_ylabel("発現量 CPM（対数軸、2反復の平均）"); ax[2].legend(fontsize=7, frameon=False, loc="upper right")
    ax[0].set_ylim(0.01, 1200)
    fig.suptitle("3つの標的は、各細胞株で発現し、減っていたか（点線：発現の基準 CPM=2）", fontsize=10)
    fig.tight_layout(); fig.savefig(F / "01-targets-knockdown.png", dpi=170); plt.close(fig)


def fig2():
    sets = [(MAIN, "腸細胞（成熟）\nTabula Sapiens"), ("Large Intestine-immature Enterocyte", "腸細胞（未成熟）"), ("Panglao:Enterocytes", "腸細胞 PanglaoDB"),
            ("HALLMARK_MYC_TARGETS_V1", "MYC標的 V1"), ("HALLMARK_E2F_TARGETS", "E2F標的"), ("HALLMARK_G2M_CHECKPOINT", "G2Mチェックポイント"), ("HALLMARK_WNT_BETA_CATENIN_SIGNALING", "WNT/β-catenin")]
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    y = np.arange(len(sets))[::-1]
    for k, l in enumerate(LINES):
        z = [S["e2"][l][n]["z"] for n, _ in sets]
        ax.scatter(z, y + (k - 1) * 0.2, color=COL[l], s=38, label=l, zorder=3)
    ax.axvspan(-2, 2, color="#999999", alpha=.15); ax.axvline(0, color="grey", lw=.6)
    ax.set_yticks(y); ax.set_yticklabels([s for _, s in sets], fontsize=8)
    ax.set_xlabel("遺伝子セットのz（MHF対N。無作為な同数遺伝子との比較。灰色：|z|<2）")
    ax.legend(fontsize=8, frameon=False, loc="lower right")
    ax.set_title("腸細胞のプログラムは3株とも上がったが、増殖の変化は細胞株で違う", fontsize=9)
    fig.tight_layout(); fig.savefig(F / "02-set-scores.png", dpi=170); plt.close(fig)


def fig3():
    rows = list(csv.DictReader(open(R / "e3_all_z.csv", encoding="utf-8")))
    fig, ax = plt.subplots(1, 3, figsize=(11, 3.8), sharey=True)
    for a, l in zip(ax, LINES):
        z = np.array([float(r[l]) for r in rows if r[l] != ""])
        a.hist(z, bins=40, color="#bbbbbb", orientation="horizontal")
        for r in rows:
            if r["set"] == MAIN:
                zz = float(r[l]); a.axhline(zz, color=COL[l], lw=2)
                a.text(0.98, zz,  f"成熟腸細胞 z={zz:.1f}（上位{S['e3_rank'][l][MAIN]['top_pct']}%）", transform=a.get_yaxis_transform(), ha="right", va="bottom", fontsize=8, fontweight="bold", bbox=dict(fc="white", ec="none", alpha=.85, pad=1), color=COL[l])
        a.set_title(f"{l}（細胞種セット{len(z)}個）", fontsize=9); a.set_xlabel("セット数")
    ax[0].set_ylabel("セットのz（上がり方）")
    fig.suptitle("腸細胞のセットは、全細胞種セットの中でどこに位置するか", fontsize=10)
    fig.tight_layout(); fig.savefig(F / "03-specificity-rank.png", dpi=170); plt.close(fig)


if __name__ == "__main__":
    fig1(); fig2(); fig3()
    print(sorted(p.name for p in F.glob("*.png")))
