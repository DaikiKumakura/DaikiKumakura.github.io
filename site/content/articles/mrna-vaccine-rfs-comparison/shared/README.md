# INTerpath-001 arithmetic and illustrative timing curves

Author: Daiki Kumakura.

Run `python analysis.py` with Python 3.12.4 and Matplotlib 3.9.1 (the versions used for the article). Outputs are written to `results/` and `figures/`. No random numbers are used.

Inputs: the printed 24-month recurrence-free survival estimates 0.822 and 0.700 from the [22 October 2026 official INTerpath-001 announcement](https://www.merck.com/news/merck-and-moderna-will-present-results-from-landmark-phase-3-interpath-001-trial-for-intismeran-autogene-plus-keytruda-pembrolizumab-at-esmo-2026-presidential-symposium/).

The script subtracts and divides these rounded estimates. It also constructs two hypothetical exponential/piecewise exponential treatment curves with the same two-year endpoint, using a constant hypothetical control hazard. The curves are not digitized or reconstructed trial curves, do not estimate the trial Cox hazard ratio, and contain no patient data. No confidence intervals for differences or number needed to treat are estimated.
