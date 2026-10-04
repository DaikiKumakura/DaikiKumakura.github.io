# Paired immune-expression change during nivolumab

Completed research analysis, 2026-10-04. Fixed scores and selected paired-cohort response associations; no pretreatment predictor, survival landmark model or clinical assay is qualified.

## Reproduce

Python 3.12 with numpy, pandas, scipy, matplotlib, nbformat, nbclient, ipykernel and IPython:

1. `python acquire.py` — official GSE91061 SOFT, FPKM and raw-count matrices, pinned SHA-256.
2. `python analyze.py` — audit pairs, scores, bootstrap and patient-separated association diagnostics.
3. `python validate.py` — independent score, AUC, Brier, median and source checks.
4. Execute `analysis.ipynb` top to bottom.

Exactly one Pre and On sample is required. Unknown response remains in change descriptions. Raw matrices, participant metadata/scores, fold assignments and prediction rows remain local and are excluded from the public companion. Original participant data are not redistributed; retrieval scripts are supplied instead. Public availability does not imply blanket permission for clinical-data redistribution.

Study-level biopsy timing is available, but individual actual biopsy/event dates are absent in these files. Conditional resampling does not include model-refitting uncertainty or repair second-biopsy selection. The FPKM adaptation differs from published TPM CYT. The secondary six-gene mean is not the published clinical assay. No survival, PK-linked exposure–response, or causal treatment-effect claim.

Sources: Riaz et al., DOI 10.1016/j.cell.2017.09.028; NCBI GEO GSE91061; Rooney et al., DOI 10.1016/j.cell.2014.12.033; Ayers et al., DOI 10.1172/JCI91190.
