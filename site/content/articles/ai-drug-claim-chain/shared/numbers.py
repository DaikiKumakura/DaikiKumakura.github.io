"""Arithmetic on figures transcribed from public sources (no raw data exist).

8 of 117: attributed in a trade-press article to a LinkedIn post (denominator = all tracked AI-enabled assets).
4 of 10: example of "about 40% on a limited sample" for Phase II (Jayatunga et al. 2024 abstract gives only ~40%;
the 10 and 4 come from a secondary account and were not checked against the original table).
Run: python numbers.py   -> results/summary.json
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUTS = {"tracked_assets": 117, "completed_phase1": 60, "cleared_phase2": 8, "phase2_completed_example": 10, "phase2_success_example": 4}


def binom_cdf(k: int, n: int, p: float) -> float:
    return sum(comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(k + 1))


def clopper_pearson(x: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    def bisect(f, lo=0.0, hi=1.0):
        for _ in range(200):
            mid = (lo + hi) / 2
            if f(mid) > 0:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    lower = 0.0 if x == 0 else bisect(lambda p: alpha / 2 - (1 - binom_cdf(x - 1, n, p)))
    upper = 1.0 if x == n else bisect(lambda p: binom_cdf(x, n, p) - alpha / 2)
    return lower, upper


def main() -> None:
    i = INPUTS
    cp = clopper_pearson(i["phase2_success_example"], i["phase2_completed_example"])
    out = {
        "share_completed_phase1_of_tracked": round(i["completed_phase1"] / i["tracked_assets"], 4),
        "share_cleared_phase2_of_tracked": round(i["cleared_phase2"] / i["tracked_assets"], 4),
        "example_phase2_rate": i["phase2_success_example"] / i["phase2_completed_example"],
        "example_phase2_cp95": [round(cp[0], 3), round(cp[1], 3)],
        "note": "8/117 and 4/10 have different denominators (all assets that entered trials, including ongoing ones, vs completed Phase 2 trials); they are not comparable. 8/60 is also not a success rate (snapshot, ongoing assets censored).",
        "inputs": i,
    }
    (HERE / "results").mkdir(exist_ok=True)
    (HERE / "results" / "summary.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
