Reference date: the facts in this article are as of 1 November 2026.

The prescribing information for subcutaneous pembrolizumab (Keytruda Qlex) gives steady-state values for 790 mg every 6 weeks and 395 mg every 3 weeks, together with a terminal half-life of 22 days ([1](#ref-1)). The steady-state values include the area under the concentration–time curve (AUC), the trough concentration (Ctrough) and the accumulation ratio. A terminal half-life alone does not uniquely determine population steady-state means. Under an assumed one-compartment model with first-order absorption, this note finds the elimination half-life that reproduces the label's values and compares it with 22 days. A discrepancy under this model alone is not evidence of an error in the label. It then examines how the result changes when the between-patient variability reported in the label is included.

## Methods

The label inputs are in Table 1. Subcutaneous bioavailability is about 60% (coefficient of variation 14%), peak concentration occurs by about 4 days, steady-state clearance is 195 mL/day (coefficient of variation 40%) and the volume of distribution is 6 L. The tabulated values are means ([1](#ref-1)). The half-life computed from 6 L and 195 mL/day is about 21 days, consistent with 22 days.

Table 1. Steady-state label values after subcutaneous dosing (means) ([1](#ref-1)). The average concentration is the AUC divided by the dosing interval.

| Regimen | AUC (µg·day/mL) | Average concentration (µg/mL) | Ctrough (µg/mL) | Ctrough / average | Accumulation ratio |
| --- | ---: | ---: | ---: | ---: | ---: |
| 790 mg every 6 weeks | 2,798 (0–6 weeks) | 66.6 | 39 | 0.585 | 1.6 |
| 395 mg every 3 weeks | 1,343 (0–3 weeks) | 64.0 | 49 | 0.766 | 2.5 |

- Typical-patient model: one compartment with first-order absorption. The model half-life is the elimination half-life ln 2 / k from the elimination rate constant k, which is not necessarily defined as the label's terminal half-life. The absorption rate constant was set so that the time to peak is 4 days. The label says only "approximately 4 days"; this reading is an assumption. Clearance was constant.
- The label text I read does not define the accumulation ratio. I took it as the steady-state AUC over one dosing interval divided by the AUC of the first dosing interval (computed exactly for a model with first-order absorption).
- Model with variability (an analysis added after seeing the label values): clearance log-normally distributed (mean set by the 22-day half-life and 6 L, coefficient of variation 40%) and bioavailability log-normally distributed (mean 0.60, coefficient of variation 14%), for 20,000 simulated patients (random seed 20261101). I computed ratios of means, which correspond to the label's means. The coefficients of variation are the label's values and were not adjusted. The label does not say whether 22 days (clearance 195 mL/day) refers to the mean or the median of individual clearances. I took it as the mean in the main analysis and as the median (mean clearance about 1.08 times the median) in a sensitivity analysis.
- Outputs: for the typical-patient model, the half-life that reproduces the accumulation ratio and Ctrough / average separately; for the model with variability, the values at a half-life of 22 days.

The calculation is in closed form, and the first-interval AUC and the steady-state average concentration were checked against numerical integration.

## Results

The typical-patient model with a half-life of 22 days did not reproduce the label values (Figure 1). Ctrough / average was 0.50 for every 6 weeks (label 0.585) and 0.73 for every 3 weeks (label 0.766); the accumulation ratio was 1.38 for every 6 weeks (label 1.6) and 2.15 for every 3 weeks (label 2.5).

![Figure 1. Typical-patient model values versus half-life. Left: steady-state Ctrough / average concentration. Right: accumulation ratio. Solid lines: model; dashed lines: label values; dotted line: the label half-life of 22 days. One-compartment model with bioavailability 0.60 and a 4-day peak.](shared/pembrolizumab-sc-label-halflife/figures/01-half-life-consistency.png)

The half-lives that reproduce the four label values (two regimens × two indices) were 25.7–28.9 days (Table 2).

Table 2. Half-life (days) at which the typical-patient model reproduces label values.

| Regimen | From accumulation ratio | From Ctrough / average |
| --- | ---: | ---: |
| 790 mg every 6 weeks | 28.9 | 28.1 |
| 395 mg every 3 weeks | 27.0 | 25.7 |

Including between-patient variability in clearance brought the values close to the label at a half-life of 22 days (Table 3), when 22 days was taken to correspond to mean clearance. With a coefficient of variation of 40%, Ctrough / average was 0.57 for every 6 weeks and 0.77 for every 3 weeks, the accumulation ratios were 1.56 and 2.48, and the mean Ctrough for every 6 weeks was 39 µg/mL, close to the label's 0.585, 0.766, 1.6, 2.5 and 39. With a coefficient of variation of 20%, the values stayed near those of the typical-patient model. When 22 days was taken to correspond to median clearance, even a coefficient of variation of 40% gave 0.54 and 0.75, accumulation ratios of 1.50 and 2.35, and a mean Ctrough of 34.7 µg/mL for every 6 weeks, short of the label values.

Table 3. Model at a half-life of 22 days with between-patient variability (ratios of means and means, 20,000 patients) and the label values ([1](#ref-1)). CV: coefficient of variation of clearance. The "median" column is a sensitivity analysis taking 22 days to correspond to median clearance.

| Index | Typical patient | Clearance CV 20% | CV 40% | CV 40% (median) | Label |
| --- | ---: | ---: | ---: | ---: | ---: |
| Ctrough / average, every 6 weeks | 0.50 | 0.52 | 0.57 | 0.54 | 0.585 |
| Ctrough / average, every 3 weeks | 0.73 | 0.74 | 0.77 | 0.75 | 0.766 |
| Accumulation ratio, every 6 weeks | 1.38 | 1.43 | 1.56 | 1.50 | 1.6 |
| Accumulation ratio, every 3 weeks | 2.15 | 2.23 | 2.48 | 2.35 | 2.5 |
| Average concentration (µg/mL) | 59.6 | 62.0 | 69.1 | 64.1 | 66.6 (6 weeks), 64.0 (3 weeks) |
| Ctrough, every 6 weeks (µg/mL) | 29.7 | 32.1 | 39.1 | 34.7 | 39 |
| Ctrough, every 3 weeks (µg/mL) | 43.7 | 46.0 | 53.1 | 48.3 | 49 |

Some differences remain. The average concentration in the model with variability (mean-clearance reading) is the same for the two regimens, which have equal dose intensity (69.1 µg/mL), and is 3.7% and 8.0% higher than the label's 66.6 and 64.0; the every-3-weeks Ctrough was 53.1 against 49.

## Discussion

The typical-patient model could not reproduce the four label values at a half-life of 22 days and needed about 26–29 days. When between-patient variability in clearance (coefficient of variation 40%) was included, the label's Ctrough / average, accumulation ratios and mean Ctrough for every 6 weeks came closer at 22 days if 22 days corresponds to mean clearance; if it corresponds to median clearance, they came closer but fell short.

A substantial part of the apparent inconsistency may be explained by comparing the label's means with a typical-patient model while ignoring between-patient variability. The mean AUC is pulled upward by patients with low clearance, so it exceeds the typical-patient value. However, the coefficients of variation were taken from the label, so the agreement is not independent evidence, and the result depends on whether 22 days refers to mean or median clearance. The following were also not tested.

- Whether the every-3-weeks and every-6-weeks values come from the same population and analysis. The 4% and 8% differences in average concentration and the difference in every-3-weeks Ctrough (53.1 and 49) could reflect differences in population or analysis.
- The effect of clearance falling over time. The label does not regard it as clinically meaningful ([1](#ref-1)), but it acts to increase the accumulation ratio.
- The effect of non-first-order absorption, of the accumulation-ratio definition (an AUC-based definition was assumed), and of correlation between clearance and bioavailability.

This also bears on how to read the cycle-3 trough ratio of 1.67 for subcutaneous (790 mg) versus intravenous (400 mg) dosing every 6 weeks reported in the label ([1](#ref-1)). In the same typical-patient model (bioavailability 0.60, peak at 4 days) with the same half-life in both arms, changing the half-life from 22 to 26–30 days only lowers this ratio from 1.23 to 1.22–1.21 (`results/cycle3-trough-ratio-by-half-life.csv`). The trial's report, however, is an estimated geometric mean ratio, and the effect of variability does not enter it in the same way as for the means here. How variability affects 1.67 was not examined in this note.

The limits are that the coefficients of variation were assumed to be log-normal and bioavailability and clearance independent, and that the label's accumulation ratios (1.6 and 2.5) are rounded, so the back-calculated half-lives have a range. Beyond "means", the label does not say whether its values are arithmetic or geometric; I assumed arithmetic. The result is a consistency check on published summary values, not a reanalysis of trial data.

## Conclusion

In a typical-patient one-compartment model, the 22-day half-life in the subcutaneous pembrolizumab label could not reproduce the steady-state values in the same label, and the half-life that does is about 26–29 days. When between-patient variability in clearance (the label's coefficient of variation of 40%) was included, Ctrough / average, the accumulation ratio and the mean Ctrough for every 6 weeks came closer at a half-life of 22 days (taking 22 days to correspond to mean clearance; taking it as median clearance, the mean Ctrough for every 6 weeks is 34.7 µg/mL, below the label's 39). Comparing the label's means with a typical-patient model can make the half-life appear longer.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive. Run with Python 3 (numpy, scipy, pandas, matplotlib): `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The inputs are published label values; no patient data were used. The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

The full re-run materials are in the [companion archive](shared/pembrolizumab-sc-label-halflife/pembrolizumab-sc-label-halflife-companion.zip).


Update, 2 November 2026: The introduction was clarified. Terminal half-life alone does not determine population mean exposure; this comparison depends on the assumed model. Calculated results are unchanged.

## References

<span id="ref-1"></span>1. Merck Sharp & Dohme LLC. KEYTRUDA QLEX (pembrolizumab and berahyaluronidase alfa-pmph) injection, for subcutaneous use. Prescribing information [Internet]. U.S. Food and Drug Administration; 2025 Sep [cited 2026 Nov 1]. Section 12.3. Available from: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/761467s000lbl.pdf
