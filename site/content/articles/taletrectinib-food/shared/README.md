# Taletrectinib dosing instruction and meal adherence (public-model simulation)

Public research, not treatment advice. Coefficients transcribed from the FDA NDA 219713 Multidisciplinary Review
(Table 74 PopPK, Table 88 Cox E-R for Grade>=3 ALT/AST, Table 79 ORR E-R, Table 77 Cavgss quartiles).
No patient data are used or re-estimated.

Run: `python analysis/run_analysis.py` (numpy, scipy, pandas, matplotlib; seed 20261023)
Test: `python -m unittest discover -s analysis -p "test_*.py"` (closed-form Cavg vs 3-compartment ODE)

Assumptions: WT reference 66 kg (not stated in the review); per-subject Frel random effect independent of food state;
'fed' effect (high-fat meal, healthy subjects) applied to standard meals, with sensitivity x0.9-1.3;
'no-meal' days treated as 10-h fast; only relative hazards (baseline hazard not public).
