"""Additional summaries quoted in the article (not part of run.py's tables).

Run `python analysis/run.py` first inside the unpacked analysis folder; then:
    python extra-fold-checks.py <unpacked tce-antigen-effector-prediction folder>
Reads outputs/fold-parameters.json (written by run.py) and outputs/tables/descriptive-curve-fits.csv.
Prints: (1) ranges of the covariate coefficients over the leave-one-group-out fits
(cell-line fits: 14 held-out lines, training_groups=13; E:T fits: 4 held-out ratios, training_groups=3);
(2) the Spearman correlation between antigen amount and the descriptive EC50.
Parameter order (src/models.py): [log EC50, log Hill, logit max effect, potency covariate, max-effect covariate].
"""
import csv
import json
import sys
from pathlib import Path

from scipy.stats import spearmanr

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
records = json.loads((root / "outputs" / "fold-parameters.json").read_text(encoding="utf-8"))


def rng(model, groups, index):
    v = [r["parameters"][index] for r in records if r["model"] == model and r["training_groups"] == groups]
    return len(v), min(v), max(v)


for label, model, groups, index in (
    ("cell lines, potency: antigen coefficient", "potency", 13, 3),
    ("cell lines, both: antigen coefficient on potency", "both", 13, 3),
    ("cell lines, both: antigen coefficient on maximum effect", "both", 13, 4),
    ("E:T ratios, potency: E:T coefficient", "potency", 3, 3),
):
    n, lo, hi = rng(model, groups, index)
    print(f"{label}: n fits = {n}, range = {lo:.3f} to {hi:.3f}")

with (root / "outputs" / "tables" / "descriptive-curve-fits.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
rho = spearmanr([float(r["antigen"]) for r in rows], [float(r["ec50_nm"]) for r in rows])
print(f"Spearman, antigen vs descriptive EC50: n = {len(rows)}, rho = {rho.statistic:.5f}, two-sided p = {rho.pvalue:.5f}")
