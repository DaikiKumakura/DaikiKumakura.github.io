# Reproduce the five-reader calculation

Run `python analysis.py` with Python 3.10 or newer. The original run used Python 3.12.4. No third-party packages or random numbers are required.

The script enumerates possible binary classifications, not patient data. It writes `results/five-reader-patterns.csv` and `results/summary.json`. Assertions check the number of disagreeing pairs and the bounds obtained with 0.67 as a rounded, conditional input. The 32 patterns are not a uniform sampling distribution.

Expected bounds are 0.268 and 0.402. These are definition-based bounds, not confidence intervals. No reference truth, individual pathologist scores, treatment outcomes or diagnostic error rates are supplied or estimated. Python-version metadata may vary across environments.
