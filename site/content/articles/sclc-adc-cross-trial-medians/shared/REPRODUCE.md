# Reproduce the aggregate-median arithmetic

Run `python analysis.py` with Python 3.12.4 (standard library only). No random numbers or external network calls are used. The script reads `cohort-medians.csv` and writes `summary.json`.

The CSV contains selected published aggregate results, transcribed on November 1, 2026. It is not patient-level data. Confidence bounds are copied from reports; they are not recalculated. NE means not estimable and NR means not reached.

- Ifinatamab deruxtecan: https://doi.org/10.1200/JCO-25-02142, Tables 2/4 and efficacy text. All-line 12 mg/kg cohort n=137 and its second-line n=32 subgroup. Cutoff March 3, 2025.
- ABBV-706: https://doi.org/10.1038/s41591-026-04452-0, Table 3, 1.8 mg/kg cohort n=41 and its second-line n=17 subgroup. Cutoff September 27, 2025. The mixed-dose n=124 cohort is not the paired comparator here. The June 29, 2026 author correction concerns references.
- Sacituzumab govitecan: https://doi.org/10.1016/j.jtho.2024.12.028, original abstract, second-line n=43, investigator-assessed PFS. No mixed-line comparator extracted.
- Izalontamab brengitecan: https://doi.org/10.1200/JCO-26-00243, original abstract, n=52 and its second-line n=22 subgroup, data as of December 5, 2024.
- IDE849: October 23, 2026 official disclosure linked in the CSV; cutoff August 21, 2026. The release labels the all previously treated median results n=101, while reporting 103 SCLC patients enrolled and a denominator of 102 for total survival events. The CSV preserves the disclosed median-result labels. Do not assume all analysis sets are identical.

The five second-line point estimates span PFS 4.40–6.90 and OS 12.0–17.4 months. The four paired OS differences (second-line minus parent cohort) are 1.70, 1.84, 2.80 and 2.70 months. Values retain decimal arithmetic; string trailing zero counts may differ from the article's uniform presentation.

Subgroups overlap their parent cohorts, and treatment line is not randomized. These differences are not treatment effects or independent comparisons. No pooling, hazard-ratio estimation, equivalence test or adjusted indirect comparison is performed.
