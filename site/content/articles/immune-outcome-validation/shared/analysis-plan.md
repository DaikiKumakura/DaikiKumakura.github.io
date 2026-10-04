# Locked analysis plan — A09–A12

Fixed on 2026-10-04 after outcome counts/data availability audit, before model fitting or external performance assessment. This is a transparent analysis plan, not prospective preregistration or blinded validation.

QOI: Do two fixed immune-biology scores add reproducible information about reported objective response among checkpoint-inhibitor-treated urothelial cancer patients? COU: hypothesis prioritization for research; no treatment selection, causal benefit, dosing or individual risk decisions.

Primary outcome: reported CR/PR = 1 versus SD/PD = 0; NE/unknown excluded. Repeated RNA samples: mean TPM per patient after clinical consistency checks. Two unmapped external RNA columns excluded. Development and external source cohorts remain separate; anonymized identifiers do not establish absence of patient overlap.

Primary M0: intercept + ECOG >=1 + male sex. M1 adds Teff8 and bundle gene19 stromal score. A liver-adjusted sensitivity uses complete cases and the source liver fields, whose definitions differ. TMB is withheld because panels are not harmonized. OS/PFS are not analyzed because shared endpoint/unit/censoring definitions have not been established.

Each score is the mean within-sample percentile rank of its fixed genes among the 24,296 shared symbols. Duplicate gene symbols are summed after length-adjusted TPM calculation in development. This outcome-blind gene-universe intersection uses external annotation availability and is not a fully untouched validation pipeline. This is not an exact reproduction of published z-score or PanF-TBRS algorithms. No cross-cohort centering, gene selection or outcome-derived cutoff.

All features standardized using development training means and population SD; zero SD replaced by 1. Logistic regression minimizes summed negative log likelihood plus 0.5*sum(non-intercept coefficient squared), fixed ridge penalty 1, no tuning. Five stratified folds repeated ten times (seed 20261004); scaling refitted within training folds, patient identities never split. Report averaged out-of-fold patient probabilities; this is repeated-CV performance of aggregated predictions, not a prospective ensemble claim.

Fit both final models on development only and save coefficients, scales, gene definitions, universe hash and input/code hashes before external scoring. External coefficients and scales unchanged. Primary external complete-case comparison reports AUC, Brier and log loss, paired bootstrap 95% percentile intervals (2,000 resamples), conditioning on trained models. Calibration intercept (slope fixed 1), slope and intercept jointly are diagnostics, never applied to predictions. Their precision is limited by events. Liver sensitivity fixed now, fit only development, apply unchanged externally. No external model selection or recalibration.

Figures: patient flow, internal/external performance, fixed-probability calibration, score distribution shift. Full hashes, numerical checks, aggregate results and executed notebook retained; patient-level raw data excluded from release. Mirrored development source is pinned but not byte-verified against unavailable publisher server. This reassesses established biological hypotheses; it is not a new biomarker discovery or proven independent prospective validation.
