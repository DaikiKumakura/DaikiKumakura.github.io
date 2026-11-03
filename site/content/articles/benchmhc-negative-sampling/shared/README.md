# Binary sequence-origin score example

Run `python analysis.py` with Python 3.10 or later. No external packages or network access are required. The script writes `table1.csv` into its own directory.

The inputs a=0.86/0.99 and b=0.12 are rounded proportions reported in the abstract of Borck et al., *BenchMHC: a reproducible framework for peptide-MHC presentation prediction*, bioRxiv v1 (2026-10-27), https://doi.org/10.64898/2026.10.22.760998. The original abstract was checked through the official bioRxiv API on 2026-11-03: https://api.biorxiv.org/details/biorxiv/10.64898/2026.10.22.760998 . The full paper was not accessed. They are conditional inputs, not a newly measured dataset. The matched and all-match scenarios are hypothetical controls.

The outcome is a theoretical ROC-AUC for an explicitly supplied binary sequence-origin score, not BenchMHC's measured performance. The feature need not be available to an actual predictor. No model training, sequence analysis, therapeutic evaluation or study-data reanalysis is performed.

The formula is checked by explicit enumeration of all four positive/decoy binary score pairs over a grid of probabilities. Equal-distribution and perfect/reversed-separation boundaries are also checked. No random number generator is used.

Archive contents: this README, `analysis.py`, generated `table1.csv`, and `environment.txt`. No third-party code, model, sequence data or figures are included.
