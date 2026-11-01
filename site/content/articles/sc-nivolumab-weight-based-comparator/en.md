Reference date: the facts in this article are as of 1 November 2026.

Subcutaneous nivolumab (Opdivo Qvantig, 1,200 mg every 4 weeks) was approved on the basis of the phase 3 trial CheckMate-67T (248 subcutaneous and 247 intravenous patients), which compared its exposure with intravenous nivolumab 3 mg/kg every 2 weeks. According to the prescribing information, the geometric mean ratio (90% CI) of the time-averaged concentration (Cavg) was 2.10 (2.00–2.20) over 28 days and 1.98 (1.87–2.11) at steady state, and that of the minimum concentration (Cmin) was 1.60 (1.49–1.72) at 28 days and 1.77 (1.63–1.93) at steady state ([1](#ref-1)). Subcutaneous exposure is about twice the intravenous exposure. The size of the ratio is not set by the formulation alone, because the intravenous comparator is dosed by body weight. Using the pharmacokinetic values in the label, this note calculates the comparator body weight to which each of the four ratios corresponds. Cavg is the average concentration over a period (the area under the concentration-time curve divided by the period) and Cmin is the minimum concentration.

## Methods

The inputs are label values: subcutaneous bioavailability of 74% (coefficient of variation 14%), peak concentration by about 6 days, steady-state clearance of 8.2 mL/h, a half-life of 25 days, steady state reached by 16 weeks, and an accumulation ratio of 2.3 ([1](#ref-1)).

- Model: a typical patient with one compartment and first-order absorption. The absorption rate constant was set so that the time to peak is 6 days (0.515 per day). The label says only "around 6 days"; this reading is an assumption. Intravenous doses were treated as boluses. The ratios do not depend on the volume of distribution, so it was not used; the elimination rate constant came from the 25-day half-life (taking it from the clearance-to-volume ratio, 8.2 mL/h / 6.8 L, gives nearly the same result: a steady-state Cmin ratio of 1.68).
- Regimens: subcutaneous 1,200 mg every 4 weeks; intravenous 3 mg/kg × body weight every 2 weeks. Clearance was assumed to be the same in both arms and constant over time. The label states that body weight has no clinically significant effect on clearance, but also that clearance falls by up to 24.5% over time ([1](#ref-1)); the assumption therefore disagrees with the label.
- Outputs: the ratios of Cavg and Cmin over 28 days (Cmin taken as the concentration on day 28, which for the intravenous arm is just before the third dose) and the same ratios at steady state. I solved for the body weight that reproduces each reported ratio and the two ends of its confidence interval. The reported ratios are ratios of geometric means estimated from trial patients; the weights solved for here are conversion values linking a typical-patient model to those ratios.

The calculation is in closed form, and the closed-form AUC was checked against numerical integration.

## Results

The weights corresponding to the four ratios at their point estimates were 84, 75, 79 and 71 kg, which do not coincide (Figure 1, Table 1).

![Figure 1. Body weight of the intravenous comparator at which the subcutaneous 1,200 mg every 4 weeks / intravenous 3 mg/kg every 2 weeks ratio equals each reported value. Dots: point estimates of the reported ratios; bars: 90% confidence intervals. Bioavailability 0.74, typical-patient model.](shared/sc-nivolumab-weight-based-comparator/figures/01-implied-weight.png)

Table 1. Reported ratios and the model ratios at 75 kg (Cavg: time-averaged concentration; Cmin: minimum concentration; bioavailability 0.74, peak at 6 days). The last column gives the weight that reproduces the reported ratio and the weights at the two ends of its confidence interval.

| Ratio | Reported (90% CI) | Model at 75 kg | Corresponding weight (kg) |
| --- | --- | ---: | ---: |
| Cavg, 28 days | 2.10 (2.00–2.20) | 2.35 | 84 (80–88) |
| Cavg, steady state | 1.98 (1.87–2.11) | 1.97 | 75 (70–79) |
| Cmin, 28 days | 1.60 (1.49–1.72) | 1.69 | 79 (74–85) |
| Cmin, steady state | 1.77 (1.63–1.93) | 1.69 | 71 (66–78) |

The steady-state Cavg ratio is simply the dose ratio: 1,200 mg × 0.74 divided by the intravenous amount per 4 weeks (6 mg/kg × 75 kg = 450 mg) gives 1.97. At 75 kg, the two steady-state ratios and the 28-day Cmin ratio fell inside their reported intervals, but the model's 28-day Cavg ratio of 2.35 exceeded the reported upper limit of 2.20. Even a constant-clearance model gives different Cavg ratios at 28 days (2.35) and at steady state (1.97).

Slower absorption did not reconcile all four. At 75 kg with a 12-day peak, the 28-day Cavg ratio was 2.11, matching the report, but the 28-day Cmin ratio became 1.85, above the reported upper limit of 1.72. In this model the 28-day and steady-state Cmin ratios are almost identical (1.85 and 1.86 at a 12-day peak), so the reported rise from 1.60 to 1.77 did not appear. This rise in Cmin is what was not reproduced. Changing bioavailability moves the corresponding weight in proportion (75 kg becomes about 61 kg at 0.60 and about 86 kg at 0.85).

## Discussion

The steady-state Cavg ratio of about 2 is consistent with an effective subcutaneous amount of about 890 mg per 4 weeks against an intravenous amount of about 420–480 mg per 4 weeks (body weight 70–80 kg). The weight solved for here was matched to the steady-state Cavg ratio, so it is a conversion value, not an independent estimate of a typical weight.

The four ratios could not be explained with one body weight and one absorption model; in particular, the rise of the Cmin ratio from 28 days to steady state remained. The remaining candidates were not tested here.

- The reported ratios are ratios of geometric means estimated from trial patients and include the weight distribution and between-patient variability, which one typical weight cannot represent.
- According to the label, nivolumab clearance falls by up to 24.5% over time, and anti-drug antibodies were found in 23% of the 202 evaluable subcutaneous patients and 7% of the 215 intravenous patients, with about 26% higher clearance in antibody-positive patients ([1](#ref-1)). The label does not consider these changes clinically relevant, but they could contribute to the difference between the 28-day and steady-state ratios.
- The label inputs are summary values, and the label text does not define Cavg and Cmin. The effect of the distribution phase after the first intravenous doses on the 28-day Cmin, and non-linear clearance, are not in this calculation either.

The limits are that I did not read the original trial paper and did not check the patients' weight distribution. The weights solved for here are conversion values linking the model and the ratios, not the trial's actual weights.

## Conclusion

With the label's bioavailability of 74% and the doses, the subcutaneous nivolumab exposure ratio of about 2 is consistent with a difference from an intravenous comparator of about 75 kg, a value matched to the steady-state Cavg ratio. The weights corresponding to the four 28-day and steady-state ratios, 71–84 kg, do not coincide, and a constant-clearance one-compartment model could not reproduce all four ratios at once. This calculation cannot identify the reason.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive. Run with Python 3 (numpy, scipy, pandas, matplotlib): `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The inputs are published label values; no patient data were used. The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

The full re-run materials are in the [companion archive](shared/sc-nivolumab-weight-based-comparator/sc-nivolumab-weight-based-comparator-companion.zip).


## References

<span id="ref-1"></span>1. Bristol-Myers Squibb Company. OPDIVO QVANTIG (nivolumab and hyaluronidase-nvhy) injection, for subcutaneous use. Prescribing information [Internet]. U.S. Food and Drug Administration; 2024 Dec [cited 2026 Nov 1]. Sections 12.3 and 14.1. Reference ID 5503239. Available from: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/761381s000lbl.pdf
