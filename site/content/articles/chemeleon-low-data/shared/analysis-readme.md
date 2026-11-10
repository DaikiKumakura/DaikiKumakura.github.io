# Reproducing the CheMeleon low-data reanalysis

Independent reanalysis of released benchmark scores, not model training or inference. Source publication: Burns et al., arXiv:2506.15792v2. Formal publication DOI: 10.1021/acs.jcim.6c01546. Methods were inspected in arXiv v2 and public code; formal publisher full text was inaccessible.

## Run

Python 3.12.4 with numpy 2.2.6, pandas 2.2.2 and matplotlib 3.9.1. Install these packages in your own environment. Extract the archive; run `python fetch_public_inputs.py` (internet required), then `python analysis.py`. The downloader fetches six pinned author result files plus 30 assay tables and verifies SHA256. It executes no downloaded code. Original molecular data and third-party code are not bundled.

Fixed commits: CheMeleon b5e5bd88a7070c3f278e7e65e85b792617bf125c; MoleculeACE 7e6de0bd2968c56589c580f2a397f01c531ede26. Manifests retain exact URLs and hashes. analysis.py verifies every entry in both manifests.

Outputs: results.json, run-results.csv, task-results.csv, task-ratios PNG/SVG and aggregate-size PNG/SVG. The derived run/task tables are generated locally, not bundled. Floating-point output may vary slightly across numerical library versions; compare numerical values with a suitable tolerance, not figure metadata hashes.

## Estimand and uncertainty

Thirty released fixed-test-set activity-regression tasks; five seeds per task/model. Read precise cliff/noncliff RMSE from summary dictionaries and reconstruct each run's total RMSE as square root of count-weighted squared subgroup errors. Compare with rounded Markdown total RMSE (absolute tolerance 5.1e-6), and subgroup summaries with the plot-input CSV. Counts and train/test labels come from pinned assay tables. Training size is the full released training pool before early-stopping partition.

Average five per-run RMSEs within a task/model before forming the ratio. Average log ratios equally across tasks and exponentiate. This differs from a ratio of pooled molecule-level errors or a mean of per-seed ratios. Main RF denotes RF.md; RF_Morgan.md and RF_Mordred.md remain separate sensitivities, since historical feature-to-result mapping is not completely established.

Task-bootstrap percentile 95% intervals, 10,000 draws, numpy default_rng seed 20261110. Keep all models/subgroups/repetitions of each sampled task together. Seeds are not independent external test splits. All main comparisons use the same draws. Activity-cliff interaction is the geometric mean of (CheMeleon/RF cliff)/(CheMeleon/RF noncliff). It compares relative gains, not absolute activity changes.

Exploratory size strata at <=1,000 and >1,000 compounds are cross-task comparisons, not learning curves or causal data-efficiency estimates. No unselected candidate experimental success, new-scaffold or temporal validation is claimed. Task-bootstrap independence is imperfect when targets/chemistry are shared. Leave-one-task-out and equal-name-prefix sensitivities do not prove biological independence.

## Checks and attribution

Assertions verify checksums, model/task/seed uniqueness, positive finite RMSE, complete 30-task/5-seed coverage, source subgroup agreement, split labels, unique assay SMILES and correct pooled RMSE. Private independent numerical implementation reproduces all reported main estimates and intervals; this package contains the independently authored production analysis only.

The new analysis code and original figures are MIT licensed (LICENSE). Input results and datasets retain their original attribution and terms; consult their source repositories and studies. No original paper figures are redistributed.
