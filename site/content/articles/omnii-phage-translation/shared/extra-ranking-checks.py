"""Extra arithmetic for the omnii-phage-translation deep pass.

Uses only counts quoted in the Radical Numerics technical report (2026-10-20):
top-100 hits 24, 97, 96; library fraction 4.5% (rounded) for the third strain.
Outputs Clopper-Pearson 95% intervals and the enrichment range implied by rounding.
"""
from scipy.stats import beta


def clopper_pearson(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    lo = 0.0 if k == 0 else beta.ppf(alpha / 2, k, n - k + 1)
    hi = 1.0 if k == n else beta.ppf(1 - alpha / 2, k + 1, n - k)
    return lo, hi


for k in (24, 97, 96):
    lo, hi = clopper_pearson(k, 100)
    print(f"{k}/100: {k/100:.3f}  CP95 [{lo:.3f}, {hi:.3f}]")
for base in (0.045, 0.0445, 0.0455):
    print(f"enrichment with library fraction {base:.4f}: {0.24/base:.2f}")
lo, hi = clopper_pearson(24, 100)
print(f"enrichment range using CP bounds vs 4.5%: {lo/0.045:.2f} to {hi/0.045:.2f}")
