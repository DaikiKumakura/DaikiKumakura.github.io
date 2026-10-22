# Elranatamab step-up priming designs (public-model simulation)

Public research, not treatment advice. Parameters transcribed from the open-access paper
doi:10.1007/s40262-026-01663-z (main-text Table and equations; ESM Table S2 for the CRS logistic model).
No patient data are used or re-estimated.

Run: `python analysis/run_analysis.py` (numpy, scipy, pandas, matplotlib; seed 20261022; ~1-2 min)
Tests: `python -m unittest discover -s analysis -p "test_*.py"`

- `analysis/tmdd.py`: quasi-equilibrium sBCMA binding model (paper's equations), vectorised RK45.
- `analysis/model.py`: linear 2-compartment approximation (failed the benchmark; kept for the record).
- Outputs: `results/benchmark.csv`, `results/designs.csv`, `results/summary.json`, `figures/stepup_designs.png`.
Assumptions: covariates per paper equations (female CL x(1-0.492); Vc (WT/71.45)^1.017; ka (AGE/66)^-1.459); CV% -> lognormal omega^2 = ln(1+CV^2);
E-R coefficients treated as independent normals (covariance not published); intercept shifted -0.37 to match 79/183; design intervals use 500 coefficient/observed-rate draws on a 512-subject subset.
