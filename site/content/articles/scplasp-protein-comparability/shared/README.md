# Per-cell counts and shared detections

Run `python analysis.py` with Python 3.10 or later. No third-party package or network is required. `table1.csv` is written next to the script.

All inputs are hypothetical. N=8000 defines an illustrative comparison universe, not a human proteome size or scpLASP coverage estimate. p=0.50, 0.75 and 0.90 are homogeneous per-item probabilities of detection in each cell. Detections of each item are independent across cells. The code evaluates N*p^m for m=1,2,10. It does not infer p from the reported median of 5655, or fit observed missingness.

The calculation concerns expectations, not observed counts, medians, biological variability, confidence intervals or power. Real abundance-dependent and treatment-dependent missingness is outside this model. Independence among different protein groups is not needed for the expected sum.

Checks cover both probability boundaries, monotonicity with cell count and explicit enumeration of the two-cell detection events. There is no random-number generation.

Archive contents: this README, `analysis.py`, generated `table1.csv` and `environment.txt`. No third-party data or source-study figures are included.
