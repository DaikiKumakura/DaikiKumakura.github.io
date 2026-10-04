# Warfarin PK/PD — A05–A08

Independent reanalysis of a publicly distributed historical single-dose PK/PCA dataset. Research only; PCA is not an INR or bleeding prediction. See `analysis-plan.md`, `results/data-dictionary.md`, `article.md` and the executed `analysis.ipynb`.

## Reproduce

From the workspace/reproduction bundle root containing `writings/warfarin-pkpd`:

```text
python writings/warfarin-pkpd/acquire.py
Rscript writings/warfarin-pkpd/export_data.R
python writings/warfarin-pkpd/audit.py
Rscript writings/warfarin-pkpd/fit.R
Rscript writings/warfarin-pkpd/weight_pd.R
python writings/warfarin-pkpd/analyze.py
python writings/warfarin-pkpd/scenarios.py
python writings/warfarin-pkpd/prepare_release.py
```

Dependencies: R 4.5.1, nlmixr2est 7.1.0, rxode2 5.1.8, nlmixr2data 2.0.10; Python numpy, pandas, scipy, matplotlib, nbformat, nbclient, ipykernel and Markdown. Exact R session is saved in `results/sessionInfo.txt`. Install R packages using CRAN in an independent environment. A C/C++ toolchain (Rtools on Windows) is required for nlmixr model compilation. The optional local library path is used only when it exists. No credentials are needed. Data acquisition requires internet access; fitting is local. Seed: 20261004.

Pinned nlmixr2data commit and upstream file hashes are saved in `raw/source-manifest.json`; the separately downloaded university original is audited by hash and numerical equality. Upstream package declares GPL-3; acquire upstream data/license rather than redistributing patient files. Our figures and aggregate results are not the original trial database; patient-level completeness, baseline assay uncertainty and replicate provenance remain unresolved.

`fits/` contains preserved exploratory fits including baseline-normalized time-zero observations. **`fits-primary/` is the final source**, excludes normalized time-zero PD from the likelihood because baseline was used as an input. Primary PD includes 188 postbaseline records in 30 subjects, PK 251 records in 32. Old fits are retained privately, not shipped. Every final fit has model/input/control RDS, theta, omega, diagnostics and full warnings. Resume checks reuse completed fits; after changing the model or control, use a new output directory rather than silently reusing old output.

The executed notebook reviews saved aggregate outputs and recreates figures; it does not silently rerun all estimation jobs. The commands above reproduce the full analysis. `analyze.py` requires private acquired observations and fit tables. Publication staging excludes raw observations, RDS, subject predictions, libraries and exploratory fits. `release/` is a review artifact, not a deployment. No publication date was assigned.

The PK optimizer warning prevents strong model qualification and formal parameter confidence intervals. Subject-bootstrap validation intervals condition on fitted folds. Parameter-resampling dose results are warning-dependent sensitivity, not validated clinical uncertainty. Allometry is prespecified; sex/age/genotypes are not searched. Sequential PD uses conditional PK EBEs, not a simultaneous PK/PD likelihood.

An intermediate resampling loop was invalidated in QA because fitting can reset R's RNG. Its `boot-*` folders are preserved privately and excluded from every final summary. Final `resample-*` datasets are generated as a complete list before any fitting and mapped in `results/bootstrap-sampling.csv`; uniqueness is verified. Corrected fits and analysis files are the only source of publication staging. This prevents identical resamples from masquerading as uncertainty estimates.
