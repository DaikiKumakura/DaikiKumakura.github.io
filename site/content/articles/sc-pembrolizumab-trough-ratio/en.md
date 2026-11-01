Reference date: the facts in this article are as of 1 November 2026.

The phase 3 trial MK-3475A-D77 compared subcutaneous pembrolizumab (790 mg every 6 weeks) with intravenous pembrolizumab (400 mg every 6 weeks), randomizing 251 and 126 patients 2:1. The geometric mean ratio was 1.14 (96% CI 1.06–1.22) for the area under the concentration–time curve (AUC) in the first dosing cycle and 1.67 (94% CI 1.52–1.84) for the cycle-3 trough concentration (Ctrough). The non-inferiority margin was 0.8, and both ratios met it ([1](#ref-1), [2](#ref-2)). The AUC is 14% higher, yet the trough is 67% higher. This note tests whether slower absorption alone can explain that gap, using typical-patient calculations with the pharmacokinetic values in the prescribing information.

## Methods

The inputs are the subcutaneous bioavailability (about 60%), the time to peak concentration (stated only as peak concentrations "by approximately 4 days"), the volume of distribution (6 L) and the terminal half-life (22 days) from the prescribing information ([2](#ref-2)). The label values are means (with coefficients of variation) from a population analysis of the subcutaneous regimen, whereas the intravenous typical values used in Model B below ([3](#ref-3)) come from a different population, so the two sets are not guaranteed to be mutually consistent. The label also states that clearance falls over time (steady-state clearance 195 mL/day).

- Model A: one compartment with first-order absorption. The absorption rate constant ka was solved so that the time to peak is 4 days (0.857 per day). The label gives no statistic for "about 4 days"; treating it as the time to peak of a first-order model is an assumption.
- Model B: the two-compartment model of Ahamadi et al. ([3](#ref-3)) with typical values, plus a first-order absorption depot. ka was scanned.
- Regimens: subcutaneous 790 mg and intravenous 400 mg (30-minute infusion), both every 6 weeks. I computed the cycle-3 trough ratio (the concentration at the end of the third cycle), the steady-state trough ratio and the cycle-1 AUC ratio. Bioavailability was fixed at 0.60, and clearance was taken to be the same in both arms.
- Between-patient variability and time-varying clearance were not included.

The calculations use exact matrix-exponential solutions, and the cycle-1 AUC ratio was checked against a numerical solution of the differential equations.

## Results

With the label values (peak by about 4 days), the cycle-3 trough ratio was 1.23 in Model A. Model B gave 1.22 at the same ka (0.857 per day), but its own peak is then about 2 days; matching a 4-day peak in Model B needs ka of 0.35 per day and gives 1.28. The steady-state ratio equalled the cycle-3 ratio to two decimals in both models, because little of the dose remains unabsorbed after one 6-week interval. The label calls the cycle-3 trough steady state but also states that steady state is reached by 16 weeks ([2](#ref-2)). The steady-state AUC ratio equals the dose ratio times bioavailability, 790 × 0.60 / 400 = 1.185, independent of absorption speed. Model B gave a cycle-1 AUC ratio of 1.17, inside the reported 1.14 (1.06–1.22).

Slower absorption raises the trough ratio (Figure 1, Table 1). The reported 1.67 is reached at ka of about 0.10 per day in Model A (peak at about 17 days) and about 0.08 per day in Model B (Model B's own peak at about 16 days). Even the lower confidence limit of 1.52 needs ka of about 0.14 per day in Model A (peak at about 14 days) and about 0.12 per day in Model B (about 11 days).

![Figure 1. Cycle-3 trough ratio (subcutaneous 790 mg / intravenous 400 mg, every 6 weeks) versus the absorption rate constant, assuming bioavailability 0.60. The band is the 94% confidence interval of the reported ratio ([1](#ref-1)). Model A: one compartment. Model B: two compartments of Ahamadi et al. ([3](#ref-3)). Typical patient, no variability.](shared/sc-pembrolizumab-trough-ratio/figures/01-trough-ratio-vs-ka.png)

Table 1. Absorption rate constant ka and cycle-3 trough ratio (bioavailability 0.60, typical patient). The time to peak is that of the maximum concentration after a single dose in each model.

| ka (per day) | Model A peak (days) | Model A | Model B peak (days) | Model B |
| ---: | ---: | ---: | ---: | ---: |
| 0.08 | 19.2 | 1.76 | 16.0 | 1.68 |
| 0.20 | 11.0 | 1.41 | 6.4 | 1.37 |
| 0.60 | 5.2 | 1.25 | 2.7 | 1.24 |
| 0.857 | 4.0 | 1.23 | 2.1 | 1.22 |
| 1.40 | 2.8 | 1.21 | 1.5 | 1.21 |

The label's steady-state values also disagree with Model A in places ([2](#ref-2)). The mean concentration for the subcutaneous every-6-week regimen is 66.6 µg/mL (AUC 2,798 µg·day/mL over 42 days), and the trough of 39 µg/mL is 0.59 of it. The same ratio is 0.50 in Model A and about 0.5 in Model B. The label's accumulation ratio is 1.6, against 1.36 for a one-compartment model with a 22-day half-life. The AUC computed from the label's steady-state clearance of 195 mL/day is 2,431, and Model A gives 2,507, both 10–15% below the label's 2,798.

## Discussion

Results: absorption with a bioavailability of 0.60 and a peak by about 4 days gives a typical-patient trough ratio of 1.2–1.3. The reported 1.67 (1.52–1.84) was not reproduced by absorption alone. Reproducing it needs a model peak at 16–17 days, far from the label's statement of a peak by about 4 days.

Interpretation: slower absorption was not sufficient to explain 1.67 under assumptions consistent with the label. The remaining candidates were not tested here.

- The reported ratio is a geometric mean ratio estimated from trial patients, not a typical-patient calculation. Between-patient variability, differences between the pharmacokinetic-evaluable populations of the two arms, and a lower-than-typical intravenous trough are possible; a high subcutaneous trough is not the only way to obtain the ratio.
- The label's accumulation ratio (1.6) exceeds the 1.36 of a one-compartment model with a 22-day half-life. Slower late elimination, or absorption that is not first order, would raise the trough more than the AUC.
- The inputs mix subcutaneous means (label) with intravenous typical values (Ahamadi), and the steady-state AUC differs by about 10% (2,798 versus 2,507).
- Bioavailability was fixed at 0.60. At 0.70 the Model A ratio is 1.44.
- A 2026 corrigendum to the paper exists ([4](#ref-4)); I could not check its content, so whether it concerns the numbers cited here is unknown.

The main limit is that ka is not in the label and was back-calculated from the time to peak. The result is a consistency check on published summary values, not a reanalysis of trial data. The label values partly derive from the same trial, so they are not independent of the reported ratio. The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

With first-order absorption consistent with the label (bioavailability about 60%, peak by about 4 days), the cycle-3 trough ratio of subcutaneous pembrolizumab is 1.2–1.3 in a typical patient, lower than the reported model-based 1.67. Reaching 1.67 by absorption alone would need a model peak at 16–17 days, far from the label's description. The cause of the gap cannot be identified from this calculation.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive. Run with Python 3 (numpy, scipy, pandas, matplotlib): `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. All inputs are published literature and label values; no patient data were used.

The full re-run materials are in the [companion archive](shared/sc-pembrolizumab-trough-ratio/sc-pembrolizumab-trough-ratio-companion.zip).


## References

<span id="ref-1"></span>1. Felip E, Rojas CI, Schenker M, Kowalski DM, Casarini IA, Csöszi T, et al. Subcutaneous versus intravenous pembrolizumab, in combination with chemotherapy, for treatment of metastatic non-small-cell lung cancer: the phase III 3475A-D77 trial. Ann Oncol. 2025;36(7):775–785. [doi:10.1016/j.annonc.2025.03.012](https://doi.org/10.1016/j.annonc.2025.03.012)

<span id="ref-2"></span>2. Merck Sharp & Dohme LLC. KEYTRUDA QLEX (pembrolizumab and berahyaluronidase alfa-pmph) injection, for subcutaneous use. Prescribing information [Internet]. U.S. Food and Drug Administration; 2025 Sep [cited 2026 Nov 1]. Section 12.3. Available from: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/761467s000lbl.pdf

<span id="ref-3"></span>3. Ahamadi M, Freshwater T, Prohn M, Li CH, de Alwis DP, de Greef R, et al. Model-based characterization of the pharmacokinetics of pembrolizumab: a humanized anti-PD-1 monoclonal antibody in advanced solid tumors. CPT Pharmacometrics Syst Pharmacol. 2017;6(1):49–57. [doi:10.1002/psp4.12139](https://doi.org/10.1002/psp4.12139)

<span id="ref-4"></span>4. Corrigendum to: Subcutaneous versus intravenous pembrolizumab, in combination with chemotherapy, for treatment of metastatic non-small-cell lung cancer: the phase III 3475A-D77 trial. Ann Oncol. 2026;37(9):1312. [doi:10.1016/j.annonc.2026.02.002](https://doi.org/10.1016/j.annonc.2026.02.002) [content not checked]
