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
        a.bar(x - 0.18, [e[t]["ctrl_cpm"] for t in e], 0.36, color="#999999", label="Control (N)")
        a.bar(x + 0.18, [e[t]["kd_cpm"] for t in e], 0.36, color=COL[l], label="Triple knockdown (MHF)")
        a.set_yscale("log"); a.set_xticks(x); a.set_xticklabels(list(e))
        a.axhline(2, color="grey", lw=.7, ls=":")
        for i, t in enumerate(e):
            lab = "Not expressed" if not e[t]["expressed"] else f"−{e[t]['knockdown_pct']:.0f}%"
            a.text(i, max(e[t]["ctrl_cpm"], e[t]["kd_cpm"]) * 1.5, lab, ha="center", fontsize=9)
        a.set_title(l, fontsize=10)
    ax[0].set_ylabel("Expression (CPM, log scale; mean of 2 replicates)"); ax[2].legend(fontsize=7, frameon=False, loc="upper right")
    ax[0].set_ylim(0.01, 1200)
    fig.suptitle("Target expression and knockdown (dotted: CPM = 2 threshold)", fontsize=10)
    fig.tight_layout(); fig.savefig(F / "01-targets-knockdown.png", dpi=170); plt.close(fig)


def fig2():
    sets = [(MAIN, "Mature enterocytes\nTabula Sapiens"), ("Large Intestine-immature Enterocyte", "Immature enterocytes"), ("Panglao:Enterocytes", "Enterocytes: PanglaoDB"),
            ("HALLMARK_MYC_TARGETS_V1", "MYC targets V1"), ("HALLMARK_E2F_TARGETS", "E2F targets"), ("HALLMARK_G2M_CHECKPOINT", "G2M checkpoint"), ("HALLMARK_WNT_BETA_CATENIN_SIGNALING", "WNT/β-catenin")]
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    y = np.arange(len(sets))[::-1]
    for k, l in enumerate(LINES):
        z = [S["e2"][l][n]["z"] for n, _ in sets]
        ax.scatter(z, y + (k - 1) * 0.2, color=COL[l], s=38, label=l, zorder=3)
    ax.axvspan(-2, 2, color="#999999", alpha=.15); ax.axvline(0, color="grey", lw=.6)
    ax.set_yticks(y); ax.set_yticklabels([s for _, s in sets], fontsize=8)
    ax.set_xlabel("Gene-set z (MHF vs N; matched-size random sets; gray: |z| < 2)")
    ax.legend(fontsize=8, frameon=False, loc="lower right")
    ax.set_title("Enterocyte programs rise; proliferation changes differ by cell line", fontsize=9)
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
                a.text(0.98, zz,  f"Mature enterocytes z={zz:.1f} (top {S['e3_rank'][l][MAIN]['top_pct']}%)", transform=a.get_yaxis_transform(), ha="right", va="bottom", fontsize=8, fontweight="bold", bbox=dict(fc="white", ec="none", alpha=.85, pad=1), color=COL[l])
        a.set_title(f"{l} (cell-type sets: {len(z)})", fontsize=9); a.set_xlabel("Number of sets")
    ax[0].set_ylabel("Gene-set z (upregulation)")
    fig.suptitle("Enterocyte programs among all cell-type gene sets", fontsize=10)
    fig.tight_layout(); fig.savefig(F / "03-specificity-rank.png", dpi=170); plt.close(fig)


if __name__ == "__main__":
    fig1(); fig2(); fig3()
    print(sorted(p.name for p in F.glob("*.png")))
