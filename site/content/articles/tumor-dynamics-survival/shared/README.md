# Early tumor measurements and subsequent survival

Completed analysis and article, 2026-10-04. This is a research demonstration, not a treatment rule or qualified surrogate.

## Reproduce

1. Python 3.12+: `python acquire.py` (official CRAN source, pinned SHA-256).
2. R 4.5.1: `Rscript export.R`.
3. R survival 3.8-3: `Rscript analyze.R`.
4. Python standard library: `python validate.py`.
5. Execute `analysis.ipynb` using Python with nbformat/nbclient/ipykernel and IPython. The notebook invokes R and independently verifies results. `audit.ipynb` records the earlier source audit.

`results/heldout-private.csv` and original participant data remain local and are not shipped in the companion. All public result tables are aggregate outputs. The acquisition script retrieves participant data from the official source for local reanalysis; check underlying rights before any redistribution.

The source has a post-terminal measurement anomaly, a documentation age-category discrepancy, and floor-censored transformed tumor values. See `data-audit.md` and `article.md`. The primary model is an observed-feature landmark Cox comparison, not a mechanistic or censored-longitudinal model. Conditional bootstrap intervals do not include model refitting uncertainty. No independent external cohort was available.
