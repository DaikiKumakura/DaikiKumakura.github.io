# Daraxonrasib target-inhibition recomputation

Public research, not treatment advice. Inputs transcribed from FDA NDA 220910 multidisciplinary review (Table 59 PopPK; pharmacology DUSP6 EC50/EC90; tumour/blood AUC ratio; applicant's dose-selection statement).
Run: `python analysis/run_analysis.py` (numpy, scipy, pandas, matplotlib; seed 20261023).
Assumptions: Emax form for time-dependent F; covariates fixed at reference; tumour concentration = R x whole-blood concentration; Hill from EC90/EC50; mouse PD transferred to human.
