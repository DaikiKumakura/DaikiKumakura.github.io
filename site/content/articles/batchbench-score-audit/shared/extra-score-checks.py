"""Extra descriptive check for batchbench-score-audit (deep pass 2026-10-29).

Uses only the mean +/- sample SD (n = 3 seeds) printed in Table 2 of arXiv:2610.30104v1.
Seeds are treated as independent between methods (unpaired Welch comparison); within a method,
group accuracies are treated as perfectly positively correlated (an upper bound on weighted-sum SD for fixed marginals, not guaranteed conservative interval coverage).
Descriptive only: n = 3, SD rounded to 3 decimals, no seed-level predictions available.
"""
import numpy as np
from scipy import stats

N = 3
# method: (poscon, sd, target, sd, rest, sd)
T2 = {
    "ResNet18": (0.465, 0.036, 0.012, 0.004, 0.002, 0.000),
    "deepCORAL": (0.502, 0.024, 0.034, 0.006, 0.007, 0.002),
    "AdaBN": (0.646, 0.005, 0.019, 0.005, 0.002, 0.001),
}
TEST = np.array([16691, 25352, 4107], float)
w = TEST / TEST.sum()
print("test n =", int(TEST.sum()), "weights", w.round(4))


def welch(m1, s1, m2, s2):
    v1, v2 = s1**2 / N, s2**2 / N
    se = np.sqrt(v1 + v2)
    df = (v1 + v2) ** 2 / (v1**2 / (N - 1) + v2**2 / (N - 1))
    t = stats.t.ppf(0.975, df)
    d = m1 - m2
    return d, se, df, d - t * se, d + t * se


def ws(m, wt):
    a = T2[m]
    mean = wt[0] * a[0] + wt[1] * a[2] + wt[2] * a[4]
    sd = wt[0] * a[1] + wt[1] * a[3] + wt[2] * a[5]  # perfect-correlation upper bound
    return mean, sd


for label, i in (("AdaBN-ResNet18 POSCON", 0), ("AdaBN-ResNet18 TARGET", 2), ("AdaBN-ResNet18 REST", 4)):
    a, b = T2["AdaBN"], T2["ResNet18"]
    d, se, df, lo, hi = welch(a[i], a[i + 1], b[i], b[i + 1])
    print(f"{label}: diff {d*100:.2f} pts, SE {se*100:.2f}, df {df:.1f}, 95% CI {lo*100:.2f} to {hi*100:.2f}")
# overall (test-set weighted) AdaBN - ResNet18
m1, s1 = ws("AdaBN", w)
m0, s0 = ws("ResNet18", w)
d, se, df, lo, hi = welch(m1, s1, m0, s0)
print(f"AdaBN-ResNet18 weighted overall: {d*100:.2f} pts, 95% CI {lo*100:.2f} to {hi*100:.2f} (df {df:.1f})")

wn = np.array([0, w[1], w[2]]) / (w[1] + w[2])
print("non-POSCON weights", wn.round(4))
a_m, a_s = ws("AdaBN", wn)
c_m, c_s = ws("deepCORAL", wn)
print(f"non-POSCON AdaBN {a_m*100:.2f} (SD<= {a_s*100:.2f}), deepCORAL {c_m*100:.2f} (SD<= {c_s*100:.2f})")
d, se, df, lo, hi = welch(c_m, c_s, a_m, a_s)
print(f"deepCORAL-AdaBN non-POSCON: {d*100:.2f} pts, SE {se*100:.2f}, df {df:.1f}, 95% CI {lo*100:.2f} to {hi*100:.2f}")
print("uniform-random expected accuracy 1/2000 = 0.05%; not a class-frequency baseline")

# --- subgroup contribution shares for each method vs no adaptation (same weights as analysis.py) and TARGET diffs ---
FULL = {
    "ResNet18": (0.465, 0.036, 0.012, 0.004, 0.002, 0.000),
    "deepCORAL": (0.502, 0.024, 0.034, 0.006, 0.007, 0.002),
    "AdaBN": (0.646, 0.005, 0.019, 0.005, 0.002, 0.001),
    "TENT": (0.661, 0.011, 0.017, 0.005, 0.002, 0.001),
    "CS-ARM-BN": (0.660, 0.005, 0.031, 0.004, 0.004, 0.001),
    "ARM-BN": (0.665, 0.003, 0.035, 0.002, 0.004, 0.001),
}
print("\nContribution shares vs ResNet18 (test weights):")
b = FULL["ResNet18"]
for m, a in FULL.items():
    if m == "ResNet18":
        continue
    c = [(a[i] - b[i]) * w[k] for k, i in enumerate((0, 2, 4))]
    tot = sum(c)
    d, se, df, lo, hi = welch(a[2], a[3], b[2], b[3])
    print(f"{m}: total {tot*100:.2f} pts; POSCON {c[0]/tot*100:.1f}% TARGET {c[1]/tot*100:.1f}% REST {c[2]/tot*100:.1f}%; "
          f"TARGET diff {d*100:.2f} pts CI {lo*100:.2f} to {hi*100:.2f}")

# --- ARM-BN vs TENT: where does the overall difference come from? ---
a, b = FULL["ARM-BN"], FULL["TENT"]
c = [(a[i] - b[i]) * w[k] for k, i in enumerate((0, 2, 4))]
tot = sum(c)
print(f"\nARM-BN - TENT weighted total {tot*100:.2f} pts; POSCON {c[0]/tot*100:.1f}% TARGET {c[1]/tot*100:.1f}% REST {c[2]/tot*100:.1f}%")
for lab, i in (("POSCON", 0), ("TARGET", 2)):
    d, se, df, lo, hi = welch(a[i], a[i + 1], b[i], b[i + 1])
    print(f"  {lab} diff {d*100:.2f} pts, 95% CI {lo*100:.2f} to {hi*100:.2f}")
print("REST mean correct count across runs (not per-run observed counts; rounded 0.002 of 4107):", 0.0015 * 4107, 0.0025 * 4107, "chance", 4107 / 2000)
