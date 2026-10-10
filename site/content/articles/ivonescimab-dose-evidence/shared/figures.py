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
rd = lambda p: list(csv.DictReader(open(p, newline="")))
S = json.load(open(R / "summary.json", encoding="utf-8"))
COL = {"Q2W": "#c2622d", "Q3W": "#3b6ea8"}


def fig1():
    pk = rd(R / "pk_check.csv")
    ro = rd(HERE / "data/ro_trough.csv")
    fig, ax = plt.subplots(1, 3, figsize=(11.4, 3.7))
    names = [r["cohort"].replace("mgkg_", "\n") for r in pk]
    x = np.arange(len(pk))
    for a_, key, lim, lab in ((ax[0], "cmin_err_pct", 35, "定常状態トラフ Cmin,ss"), (ax[1], "cavg_err_pct", 20, "平均濃度 Cavg,ss")):
        v = [float(r[key]) for r in pk]
        a_.bar(x, v, color=[COL["Q3W"] if "Q3W" in r["cohort"] else COL["Q2W"] for r in pk])
        a_.axhspan(-lim, lim, color="#999999", alpha=.15)
        a_.axhline(0, color="grey", lw=.6)
        a_.set_xticks(x); a_.set_xticklabels(names, fontsize=8); a_.set_xlabel("用量（mg/kg）と間隔")
        a_.set_title(f"{lab}：予測の誤差（%）\n基準 ±{lim}%（灰色）", fontsize=9)
    ax[0].set_ylabel("予測 / 観測 − 1（%）")
    cm = [float(r["cmin_ss_ugml"]) for r in ro]
    rv = [float(r["ro_mean_pct"]) for r in ro]
    sd = [float(r["ro_sd_pct"]) for r in ro]
    ax[2].errorbar(cm, rv, yerr=sd, fmt="o", color="#333333", capsize=3)
    ax[2].set_xscale("log"); ax[2].set_ylim(60, 105); ax[2].axhline(80, color="grey", lw=.6, ls=":")
    ax[2].set_xlabel("定常状態トラフ Cmin,ss（µg/mL、対数軸）"); ax[2].set_ylabel("PD-1占有率（平均±SD、%）")
    ax[2].set_title("トラフ濃度が18倍違っても\n占有率は86〜96%", fontsize=9)
    fig.tight_layout(); fig.savefig(F / "01-pk-and-occupancy.png", dpi=170); plt.close(fig)


def fig2():
    raw = rd(R / "orr_raw.csv")
    post = np.load(R / "posterior_draws.npz")
    labels = {"P2_chemo_c1": "NSCLC 1次\n＋化学療法", "P2_chemo_c2": "NSCLC EGFR-TKI後\n＋化学療法", "P2_chemo_c3": "NSCLC 既治療\n＋化学療法",
              "P1b_mono": "NSCLC 1次 PD-L1陽性\n単剤", "P1b_sclc": "ES-SCLC 1次\n＋化学療法"}
    order = ["P2_chemo_c1", "P2_chemo_c2", "P2_chemo_c3", "P1b_sclc", "P1b_mono"]
    fig, ax = plt.subplots(1, 2, figsize=(11.4, 4.3), gridspec_kw={"width_ratios": [1.6, 1]})
    a_ = ax[0]
    for i, t in enumerate(order):
        rr = [r for r in raw if r["trial_id"] == t]
        xs = np.array([np.log2((float(r["dose_mgkg"]) / (float(r["interval_d"]) / 7)) / (10 / 3)) for r in rr])
        y = np.array([float(r["orr_pct"]) for r in rr]); lo = np.array([float(r["cp_lo"]) for r in rr]); hi = np.array([float(r["cp_hi"]) for r in rr])
        off = (i - 2) * 0.04
        derived = rr[0]["n_provenance"] == "derived"
        q3 = [k for k, r in enumerate(rr) if r["interval_d"] == "21"]
        q2 = [k for k, r in enumerate(rr) if r["interval_d"] == "14"]
        ordq3 = sorted(q3, key=lambda k: xs[k])
        c = f"C{i}"
        a_.plot(xs[ordq3] + off, y[ordq3], "s--" if derived else "o-", color=c, lw=1, ms=4, label=labels[t].replace(chr(10), " "))
        a_.errorbar(xs[ordq3] + off, y[ordq3], yerr=[y[ordq3] - lo[ordq3], hi[ordq3] - y[ordq3]], fmt="none", ecolor=c, capsize=2, lw=1)
        if q2:
            a_.errorbar(xs[q2] + off, y[q2], yerr=[y[q2] - lo[q2], hi[q2] - y[q2]], fmt="D", mfc="white", color=c, capsize=2, lw=1, ms=5)
    a_.set_xticks([-1.737, 0, 1, 1.585]); a_.set_xticklabels(["3\nQ3W", "10\nQ3W", "20\nQ3W", "20 Q2W\n30 Q3W"])
    a_.set_xlabel("用量（mg/kg）。横軸は週あたり用量強度の対数"); a_.set_ylabel("奏効率 ORR（%、Clopper–Pearson 95%区間）")
    a_.set_ylim(0, 105); a_.legend(fontsize=7, frameon=False, loc="lower right")
    a_.set_title("用量別の奏効率（四角の破線：nを報告値から導出、白抜きの菱形：Q2W）", fontsize=9)
    b = ax[1]
    d = post["d_new"]
    b.hist(d, bins=60, color="#7f7f7f", alpha=.8)
    b.axvline(0, color="black", lw=.8); b.axvline(10, color="#c2622d", lw=1, ls="--")
    q = np.percentile(d, [2.5, 50, 97.5])
    b.set_title(f"新しい設定での差（20 − 10 mg/kg Q3W、基準55%）\n中央値 {q[1]:+.1f}、95%信用区間 {q[0]:+.0f}〜{q[2]:+.0f} ポイント", fontsize=9)
    b.set_xlabel("ORRの差（%ポイント）"); b.set_yticks([])
    b.text(0.97, 0.9, f"P(≥ +10) = {S['e2_main']['p_delta_ge_10']:.2f}\nP(傾き > 0) = {S['e2_main']['p_mu_b_gt0']:.2f}", transform=b.transAxes, ha="right", fontsize=9)
    fig.tight_layout(); fig.savefig(F / "02-orr-dose-response.png", dpi=170); plt.close(fig)


def fig3():
    g = rd(R / "sample_size_grid.csv")
    n = [int(r["n_per_arm"]) for r in g]
    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    ax.plot(n, [float(r["expected_power_noninferiority_10_vs_20"]) for r in g], "o-", color="#3b6ea8", label="10 mg/kg の非劣性を示す（マージン10ポイント）")
    ax.plot(n, [float(r["expected_power_to_show_20_superior"]) for r in g], "s-", color="#c2622d", label="20 mg/kg の優位を示す")
    ax.axhline(S["e3_asymptote"]["p_true_diff_lt_10pts"], color="#3b6ea8", lw=.6, ls=":")
    ax.axhline(S["e3_asymptote"]["p_true_diff_gt_0"], color="#c2622d", lw=.6, ls=":")
    ax.set_xscale("log"); ax.set_ylim(0, 1); ax.set_xlabel("1群あたりの例数（対数軸）"); ax.set_ylabel("期待される成功確率（事後予測）")
    ax.set_title("例数を増やしても、真の差が不確かな限り\n成功確率は上限（点線）で頭打ち", fontsize=9)
    ax.legend(fontsize=7, frameon=False, loc="lower right")
    fig.tight_layout(); fig.savefig(F / "03-assurance.png", dpi=170); plt.close(fig)


if __name__ == "__main__":
    fig1(); fig2(); fig3()
    print(sorted(p.name for p in F.glob("*.png")))
