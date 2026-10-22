# Divarasib dose and exposure-response from public dose-group responses

Public research, not treatment advice. Inputs (analysis/inputs.json) are transcribed from public reports of the phase I study
(NEJM 2023, via news reports; PMC12527784 long-term follow-up). No patient-level data.
Run: `python analysis/run_analysis.py` (numpy, scipy, pandas, matplotlib; seed 20261023)
Assumptions: dose-proportional PK; CL/F from 400 mg AUC_ss; AUC CV 35%; lower-dose mix 50:100:200 = 6:5:10 (sensitivity: all 200 / all 50);
flat priors on a grid for logistic E-R on ln(AUC/AUC_ref).
