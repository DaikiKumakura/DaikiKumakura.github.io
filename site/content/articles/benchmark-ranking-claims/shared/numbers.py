"""Arithmetic on figures transcribed from public sources (no raw data exist).

Inputs are the published numbers listed in INPUTS; the script only computes
ratios and binomial intervals so the article's derived numbers are traceable.
Run: python numbers.py   -> results/summary.json
"""
from __future__ import annotations

import json
from math import comb, sqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
Z = 1.959964  # 95% normal quantile

INPUTS = {
    "pxr": {"mae_rank1": 0.4061, "pm_rank1": 0.0280, "mae_rank2": 0.4092, "pm_rank2": 0.0281,
            "n_activity_entries_pairwise": 100, "pairwise_reported": 4950, "tier1_activity": 28},
    "lifescibench": {"n_tasks": 750,
                     "pass_rate": {"GPT-Rosalind": 0.361, "GPT-5.5": 0.257, "Gemini 3.1 Pro": 0.236,
                                   "GPT-5.4": 0.207, "Grok 4.3": 0.130}},
    "aintibody": {"best_ai_pM": 94.7, "best_lab_pM": 113.0, "random_beats_model_pct": 39.0},
}


def wilson(p: float, n: int) -> tuple[float, float]:
    centre = (p + Z**2 / (2 * n)) / (1 + Z**2 / n)
    half = Z * sqrt(p * (1 - p) / n + Z**2 / (4 * n**2)) / (1 + Z**2 / n)
    return centre - half, centre + half


def diff_ci(p1: float, p2: float, n: int) -> tuple[float, float]:
    """Unpaired difference of two proportions on the same n tasks (paired data are not public)."""
    se = sqrt(p1 * (1 - p1) / n + p2 * (1 - p2) / n)
    d = p1 - p2
    return d - Z * se, d + Z * se


def main() -> None:
    px = INPUTS["pxr"]
    assert comb(px["n_activity_entries_pairwise"], 2) == px["pairwise_reported"]
    gap = px["mae_rank2"] - px["mae_rank1"]
    out: dict = {"pxr": {
        "gap_rank1_rank2_mae": round(gap, 4),
        "gap_over_rank1_spread": round(gap / px["pm_rank1"], 3),
        "pairwise_comparisons_check": comb(px["n_activity_entries_pairwise"], 2),
    }}
    lsb = INPUTS["lifescibench"]
    n = lsb["n_tasks"]
    pr = lsb["pass_rate"]
    out["lifescibench"] = {
        "wilson_95": {k: [round(x, 3) for x in wilson(v, n)] for k, v in pr.items()},
        "unpaired_diff_95": {
            "Rosalind-GPT5.5": [round(x, 3) for x in diff_ci(pr["GPT-Rosalind"], pr["GPT-5.5"], n)],
            "GPT5.5-Gemini3.1": [round(x, 3) for x in diff_ci(pr["GPT-5.5"], pr["Gemini 3.1 Pro"], n)],
        },
        "note": "task-sampling uncertainty only; unpaired approximation (paired per-task results not public); "
                "pass rates are rounded to 0.1 point",
    }
    a = INPUTS["aintibody"]
    out["aintibody"] = {
        "ratio_lab_over_ai": round(a["best_lab_pM"] / a["best_ai_pM"], 3),
        "relative_improvement_pct": round(100 * (1 - a["best_ai_pM"] / a["best_lab_pM"]), 1),
    }
    out["inputs"] = INPUTS
    (HERE / "results").mkdir(exist_ok=True)
    (HERE / "results" / "summary.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k != "inputs"}, indent=1))


if __name__ == "__main__":
    main()
