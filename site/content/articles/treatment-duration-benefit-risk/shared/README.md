# Treatment duration and benefit–risk: aggregate SCOT evidence

Completed research analysis, 2026-10-04. Aggregate randomized duration evidence, not individual participant reanalysis or clinical treatment advice.

## Reproduce

Python 3.12 with numpy, matplotlib, nbformat, nbclient, ipykernel and IPython:

1. `python acquire.py` — official Europe PMC XML for the 2018 and 2026 reports.
2. `python analyze.py` — table extraction, risk differences, uncertainty and missingness bounds.
3. `python validate.py` — source identity and independent arithmetic checks.
4. Execute `analysis.ipynb` top to bottom.

Public companion includes extracted aggregate inputs, results, code and executed notebook. It excludes downloaded article XML. Source manifests retain retrieval URLs and hashes. Published survival intervals are used directly; censoring is not ignored by treating Kaplan–Meier estimates as binomial counts. Safety-subset missingness bounds do not apply to everyone randomized. Different efficacy/safety populations and unobserved joint endpoints prevent qualified individual net-benefit inference.

Original report: Iveson et al., DOI 10.1016/S1470-2045(18)30093-7, CC BY 4.0. Final results: DOI 10.1200/JCO-25-00621. The final-report abstract/main-text OS interval discrepancy is recorded.
