# Nimotuzumab PopPK: reproducible research companion

This is a research article companion. It contains code, aggregate outputs and figures; no patient-level table or RDS fit. It does not reproduce the complete original trial and is not a clinical dosing tool.

## Fast review without patient data

Open `article.md` or `preview.html`. Run `review.ipynb` with Python 3.11+, numpy, pandas, scipy, matplotlib, nbformat, nbclient and ipykernel. It verifies checksums, recalculates comparisons and independently propagates the M1 reference scenario from exported parameters. It does not rerun nonlinear mixed-effects estimation. Aggregate outputs retain convergence-screen failures; no bootstrap CI is supported.

## Full refitting in a fresh copy

Run commands from the extracted archive ROOT, which contains `writings/`. Python 3.11+ and R 4.5.1 are required. Estimation used nlmixr2est 7.1.0, rxode2 5.1.8 and nlmixr2data 2.0.10. `a02/renv.lock` records package versions; restoring that lock on a fresh machine has not been verified. Install compatible R dependencies before proceeding; the optional setup script installs current binaries rather than promising exact-version restoration. Preserve original archived results and use a new copy for refitting.

```
python writings/nimotuzumab-poppk/acquire.py
Rscript writings/nimotuzumab-poppk/export_data.R
Rscript writings/nimotuzumab-poppk/run_a02.R M1
Rscript writings/nimotuzumab-poppk/run_a02.R M2
Rscript writings/nimotuzumab-poppk/run_a02.R M3
Rscript writings/nimotuzumab-poppk/refine_a02.R M2
Rscript writings/nimotuzumab-poppk/refine_a02.R M3
python writings/nimotuzumab-poppk/verify_a02_likelihood.py
Rscript writings/nimotuzumab-poppk/run_a03.R M1
Rscript writings/nimotuzumab-poppk/run_a03.R M2
Rscript writings/nimotuzumab-poppk/run_a03.R M3
Rscript writings/nimotuzumab-poppk/rescue_a03.R M1
Rscript writings/nimotuzumab-poppk/audit_run_info_a03.R
python writings/nimotuzumab-poppk/analyze_a03.py diagnose
python writings/nimotuzumab-poppk/analyze_a03.py exposure
python writings/nimotuzumab-poppk/allometry_a03.py
python writings/nimotuzumab-poppk/summarize_a03.py
python writings/nimotuzumab-poppk/validate_a03.py
python writings/nimotuzumab-poppk/validate_loso_mc_a03.py
python writings/nimotuzumab-poppk/influence_a03.py
```

These are long-running estimation/simulation commands. They refit 9 SAEM starts, 6 FOCEi refinements, 874 A03 fits including an optimizer sensitivity, plus VPC (1000) and paired simulation (10000 per scenario). Recreating fixed version inputs is separate from guaranteeing identical fits across operating systems, compilers and estimator versions. Fresh environment installation and full cold rerun were not tested; the source analysis executed these calculations and this companion's review notebook was executed in isolation without raw data/RDS.

## Inputs, rights and limitations

Pinned source: nlmixr2data commit f2cfb01ade88d4d30e66f56b19efce2a2c6e26bd. `raw/source-manifest.json` records every original SHA-256. Acquire checks hashes and refuses to overwrite a differing source. The data package declares GPL (>=3); the included license text documents that declaration. Patient-level source data are fetched from the upstream distribution and are not redistributed here. Package licensing does not establish all original clinical data rights or consent scope. Original article text/figures are not redistributed. Analysis code is supplied with GPL-3.0-or-later terms, without warranty.

Prediction bands in exposure tables represent IIV conditional on point estimates. VPC bands represent uncertainty in simulated bin quantiles. They are not parameter CIs. Bootstrap screening passed 9/200, 9/200, 11/200 for bobyqa M1/M2/M3 and 44/200 for nlminb-M1; all fall below 80%. LOSO uses all finite fold outputs with warnings and is an exploratory internal check after full-data candidate selection. No external validation, efficacy, RO or toxicity prediction is provided.
