If olomorasib is given as 100 mg three times daily (TID) instead of 150 mg twice daily (BID), does the same 300 mg/day deliver more drug to the blood, or does mainly the shape of the concentration curve, its peak and its minimum, change? I estimated a small model from published measured pharmacokinetics (PK) to compare the two schedules.

The published data did not clearly support an increase in total exposure from smaller, more frequent doses. The predicted minimum concentration differed, however, between dosing every 8 hours and dosing with a 12-hour overnight gap. The plateau of exposure with dose and the dosing interval need to be considered separately.

## Introduction

Olomorasib (LY3537982) is a KRAS G12C inhibitor. In a monotherapy phase 1 study reported in 2026, 195 patients received 50, 100, 150 or 200 mg BID. The authors describe PK that increased dose-proportionally from 50 to 150 mg and plateaued between 150 and 200 mg, with a terminal half-life of approximately 3 hours ([1](#ref-1)). A phase 1/2 trial of olomorasib with pembrolizumab has also evaluated 50, 100 and 150 mg BID ([2](#ref-2)). This article is restricted to monotherapy PK.

Assuming absorption saturation from the word "plateau" alone would build the answer favoring smaller doses into the premise. I therefore compared a proportional model and a saturating model on the same measured exposure data.

The question of interest (QOI) is how the 1-day area under the concentration–time curve (AUC), maximum concentration (Cmax) and minimum concentration (Cmin) differ between 150 mg BID and 100 mg TID, and how far the published data support those predictions. The context of use (COU) is limited to forming hypotheses about doses and intervals for later PK comparisons. The analysis is not intended to predict changes in prescribing, maintenance of efficacy or improvement in safety.

## Methods

### Data

As reported by the original authors, Supplementary Fig. 2A and 2B show mean plasma concentrations at steady state and the 12-hour area under the curve (AUC12) for all doses ([3](#ref-3)). From the Source Data for that figure, I extracted the 36 mean concentrations in Supplementary Fig. 2A (4 doses × 9 time points) and the 212 steady-state AUC12 values in Supplementary Fig. 2B ([4](#ref-4)). The original authors calculated AUC by noncompartmental analysis ([1](#ref-1)). Concentrations are plasma ng/mL and AUC12 is ng·h/mL. Published numbers were used; no values were digitized from the figure by eye. The band based on the target effective concentration for 80% target inhibition (TEC80) is model-derived and was not used.

The following summaries and estimates are my recomputation.

Table 1. Published AUC12 summary by dose (BID). AUC12 is the steady-state 12-hour AUC in ng·h/mL; CV is the coefficient of variation.

| BID dose (mg) | AUC records | AUC geometric mean | AUC median | Geometric CV (%) |
| --- | ---: | ---: | ---: | ---: |
| 50 | 16 | 589 | 658 | 47.4 |
| 100 | 37 | 1,393 | 1,329 | 62.9 |
| 150 | 146 | 1,855 | 1,899 | 57.9 |
| 200 | 13 | 2,096 | 1,974 | 72.4 |

The record counts are not patient counts. The 212 records carry 201 distinct original ID labels, and 8 labels appear at more than one dose. No ID was duplicated at the same dose. The original text reports 15, 33, 134 and 13 patients starting 50, 100, 150 and 200 mg (195 in total) ([1](#ref-1)), which differs from the PK counts of 16, 37, 146 and 13. Complete information on dose changes and sampling occasions is unavailable, and the IDs could not be verified as independent patients.

Geometric CV was calculated as √(exp(V) − 1), where V is the sample variance of log AUC. Estimation uses the published AUC records, and resampling moves records sharing an original ID label together. The analysis is not a causal comparison adjusted for patient characteristics or dose modification in each dose group. The original design allowed intrapatient escalation after the initial 21-day evaluation, subject to safety review and approval ([1](#ref-1)). A label appearing at different doses is therefore compatible with the study design, but that provision does not resolve every public PK identifier or sampling occasion. The number of patients and the standard deviation (SD) at each time point of the mean concentration curves cannot be obtained from the published values, and individual concentrations were not estimated with a nonlinear mixed-effects model (NLME).

### Dose–exposure models

For the BID single dose D, two models were fitted. M0 is a proportional model through the origin and M1 is a two-parameter saturating model.

\[
M_0:\quad AUC_{12}(D)=aD
\]
\[
M_1:\quad AUC_{12}(D)=\frac{A_{\max}D}{D_{50}+D}.
\]

The sum of squared residuals of log AUC12 was minimized. Parameter a is the slope (ng·h/mL/mg), Amax the upper limit of the curve (ng·h/mL), and D50 the single dose (mg) at which half of that limit is reached. M1 is an empirical curve and does not identify an intestinal absorption mechanism. Because the number of records differs by dose, the 150 mg group, with the most records, contributes more.

### Time-course model

Concentration over time was described by a one-compartment model with absorption lag. Here k is the elimination rate constant and ka the first-order absorption rate constant.

\[
\dot A_g=-k_a A_g,\qquad
\dot C=k_a A_g-kC.
\]

In this formulation Ag is the gut amount converted to a concentration, and AUC12(D) × k is added after the lag time following each dose. Apparent volume of distribution and absolute bioavailability are not estimated separately. The values of k, ka and lag time were fitted to the 9 mean concentrations at 150 mg by log residuals. Because the concentration scale is also free, the AUC scale of the mean concentration curve and the geometric mean of individual AUC values were not forced to coincide as the same estimand.

For the other doses, k, ka and lag time were fixed and only the concentration scale was refitted. This check examines differences in shape.

### Periodic calculation of regimens and resampling

The periodic 24-hour steady state was calculated. Each dose is assumed to be absorbed independently and repeatedly, and dosing frequency itself is assumed not to change food conditions or the absorption mechanism. The data do not confirm that a dose–AUC curve derived from BID can be used for TID.

The regimens were 150 mg BID (0 and 12 h), 100 mg TID (0, 8 and 16 h), 100 mg TID with a long night interval (0, 6 and 12 h, leaving a 12-hour gap until the next day; 100TID_6_6_12), and 100 mg and 200 mg BID. The metrics are the 24-hour AUC (AUC24), Cmax and Cmin, expressed as ratios to 150 mg BID within each model. Cmin is a numerical approximation of the minimum searched over the full 24 hours, not a value at an arbitrary sampling time or immediately before a dose. Results superimpose the periodic steady state and do not describe the transition from the first dose.

Uncertainty was examined in two ways. First, I resampled original ID labels 1,000 times and re-estimated M1. This avoids separating different doses carrying the same label, but the identification of participants and dosing histories in the source was not verified. The upper bound of D50 in the optimization was 10,000,000 mg. Second, with M1 coefficients fixed at the point estimates, the centered log residuals of the dose model were resampled to 2,048 pairs as conditional exposure multipliers. Interindividual variability (IIV), differences between dosing occasions and measurement error cannot be separated in these multipliers.

For the shape sensitivity analysis, I used the endpoints of the 90% confidence interval of the original terminal half-life (2.79 h and 3.14 h), the model value, and 0.5, 1 and 2 times ka. The former reflects the precision of a population summary and the latter is an arbitrary change of assumption; neither represents patient IIV or a simultaneous 95% prediction interval.

The random seed was fixed (seed 20261024).

## Results

### Proportional and saturating dose–exposure models were not distinguished

Table 2. Fits of the dose–exposure models (log AUC12, all 212 records).

| Model | Estimated coefficients | Sum of squared log residuals |
| --- | --- | ---: |
| Proportional M0 | a = 12.452 ng·h/mL/mg | 62.867 |
| Saturating M1 | Amax = 14,587 ng·h/mL; D50 = 1,035 mg | 62.667 |

M1 has one more parameter, but the residual sum of squares decreased by only 0.32%. No significance test or AIC comparison premised on independent observations was performed, and this difference alone does not select either model. D50 is larger than the observed range of 50–200 mg and is not a value that directly captures strong saturation. The original description of a plateau between 150 and 200 mg is not contradicted by this analysis failing to exclude proportionality. One describes the observed exposure distributions; the other reflects weak discrimination between these two equations in groups with different sizes and backgrounds. Proportionality has not been established either.

![Measured mean concentrations and dose–exposure relationships estimated from individual AUC12 records.](shared/olomorasib-dose-fractionation/figures/data-and-models.png)

Figure 1. Left: mean plasma concentrations from the original report (points and colored lines, ng/mL). The black dashed line is a curve fitted only to the 9 points at 150 mg and is not a measured individual concentration. Right: geometric means of published AUC12 (points, ng·h/mL) and the M0 and M1 curves fitted to all AUC records. Record counts are given in Table 1.

### The time-course model from the 150 mg mean curve matched the shape at other doses only partly

From the 150 mg mean curve, I obtained k = 0.218 /h, ka = 0.946 /h and a lag time of 0.369 h. The model elimination half-life is 3.18 h, which does not fully agree with the geometric mean terminal half-life of 2.96 h (90% confidence interval 2.79–3.14, N = 140) reported by the original authors ([3](#ref-3)). This value approximates a 9-point mean curve with a small model and does not re-estimate individual terminal phases.

Table 3. Maximum relative difference between the time-course model and the mean concentration points (4 doses, 9 points each).

| Dose (mg) | Maximum relative difference from mean concentration points | Purpose |
| --- | ---: | --- |
| 50 | 38.8% | Shape check with rescaled concentration |
| 100 | 19.0% | Shape check with rescaled concentration |
| 150 | 20.9% | Used for estimation |
| 200 | 30.7% | Shape check with rescaled concentration |

Because only the concentration scale was refitted at the other doses, this is not an independent external validation of absolute concentration. With maximum relative differences of 19.0–38.8% remaining, the TID waveform is not treated as validated by measurement.

### The same daily dose gave opposite minimum-concentration predictions depending on timing

Table 4. 24-hour metrics for regimens (ratio to 150 mg BID within each model).

| Model | Regimen | Daily dose (mg) | AUC24 ratio | Cmax ratio | Cmin ratio |
| --- | --- | ---: | ---: | ---: | ---: |
| linear | 150BID | 300 | 1.000 | 1.000 | 1.000 |
| linear | 100TID | 300 | 1.000 | 0.775 | 1.785 |
| linear | 100BID | 200 | 0.667 | 0.667 | 0.667 |
| linear | 200BID | 400 | 1.333 | 1.333 | 1.333 |
| linear | 100TID_6_6_12 | 300 | 1.000 | 0.892 | 0.835 |
| sat | 150BID | 300 | 1.000 | 1.000 | 1.000 |
| sat | 100TID | 300 | 1.044 | 0.810 | 1.864 |
| sat | 100BID | 200 | 0.696 | 0.696 | 0.696 |
| sat | 200BID | 400 | 1.279 | 1.279 | 1.279 |
| sat | 100TID_6_6_12 | 300 | 1.044 | 0.931 | 0.872 |

"linear" corresponds to M0 and "sat" to M1. 150BID is dosed at 0 and 12 h, and 100TID at 0, 8 and 16 h.

In the proportional model, AUC24 is equal for the same daily dose. For 100TID in the saturating model, the AUC24 ratio was 1.044, the Cmax ratio 0.810 and the Cmin ratio 1.864. With the long night interval in 100TID_6_6_12, however, the Cmin ratio was 0.872. Three doses per day do not guarantee a higher minimum concentration at every dosing time.

![Comparison of dosing times and concentration metrics for the same 300 mg/day.](shared/olomorasib-dose-fractionation/figures/regimen-comparison.png)

Figure 2. Left: periodic curves with representative M1 coefficients. Right: ratios of evenly spaced TID to 150 mg BID. TID is a hypothetical regimen that was not measured.

### Resampling showed the spread of a 4% exposure increase but not model-selection uncertainty

The resampled distribution of the AUC ratio for 100 mg TID versus 150 mg BID had a median of 1.045 and a 2.5th–97.5th percentile range of 1.000–1.155 (1,000 replicates). In 226 of 1,000 replicates (22.6%), D50 exceeded 1,000,000 mg, a region approaching the proportional model.

When M1 is chosen, the ratio for the same daily dose is algebraically

\[
\frac{3AUC_{12}(100)}{2AUC_{12}(150)}
=\frac{D_{50}+150}{D_{50}+100}>1
\]

while the ratio is 1 in the proportional model. The direction of the increase is therefore part of the M1 assumption. A lower end of the distribution above 1 is not evidence of a TID advantage. The resampling percentile range is a conditional width with M1 fixed and does not include model-selection uncertainty.

![Resampling of M1 and distribution of conditional exposure multipliers.](shared/olomorasib-dose-fractionation/figures/uncertainty.png)

Figure 3. Left: AUC ratio (100 mg TID versus 150 mg BID) from 1,000 re-estimations. Right: median and 5th–95th percentiles (P5–P95) of AUC24 (ng·h/mL) using 2,048 pairs of conditional exposure multipliers, with coefficients fixed at point estimates. The left panel reflects coefficient estimation and the right panel an example of exposure variability, so they are not the same kind of uncertainty.

The multipliers in the right panel are common to all regimens and cancel in within-individual ratios. The analysis did not reconstruct 2,048 independent pharmacokinetic profiles or demonstrate individual differences in treatment effect.

In the shape sensitivity analysis (half-lives of 2.79 h, 3.14 h and the model value crossed with ka multipliers of 0.5, 1 and 2, nine combinations), the Cmin ratio for evenly spaced TID was 1.74–2.07 and the Cmax ratio was 0.78–0.85. The Cmin ratio for TID with a long night interval was 0.85–0.88. All are ratios to 150 mg BID. Within this range, changing the absorption rate did not make the 12-hour night condition equivalent to evenly spaced TID. Values for each condition are in the distributed tables.

## Discussion

The published PK did not support the conclusion that TID is advantageous because absorption plateaus above 150 mg. The proportional model and M1 were barely distinguishable by residual sum of squares (a 0.32% decrease), and the AUC increase for TID, about 4%, appears only if M1 is chosen. The direction of this difference is algebraically determined and is not an effect detected by the data.

Whether TID has an advantage also depended on dosing times. Evenly spaced TID gave a Cmin ratio of 1.74–2.07 and a Cmax ratio of 0.78–0.85, whereas TID with a 12-hour night gap gave a Cmin ratio of only 0.85–0.88. In this calculation, improvement of the minimum concentration depended on even spacing rather than on the number of doses. This conclusion rests on a calculation that transfers the dose–AUC relationship obtained with BID to TID and assumes that absorption does not change with dosing frequency.

Olomorasib is also a covalent KRAS G12C inhibitor ([1](#ref-1)). Plasma half-life and the duration of target occupancy are different quantities; this model does not describe target recovery after binding. The original TEC80 is model-derived, not a clinical threshold revalidated here. Raising calculated Cmin alone cannot determine whether additional efficacy follows when inhibition may already be sufficient.

The calculation does not predict efficacy or safety. Concentration differences cannot be read as better efficacy or lower toxicity, and a plateau in total exposure alone is not a reason to increase dosing frequency.

## Limitations

AUC12 record counts are not patient counts, and the independence of the original IDs could not be verified. D50 lies outside the observed range, and M1 is not an absorption-mechanism model. Shape verification is limited to a fit to 9 mean points at 150 mg and rescaling at other doses; the TID waveform was not measured. The sensitivity range reflects the precision of the half-life estimate and an arbitrary change of ka only. IIV, food and real variability in dosing times are not included.

## Conclusion

Splitting 150 mg BID into 100 mg TID did not yield support for an increase in total exposure from the published measured PK. Under M1, AUC24 rises by about 4% (ratio 1.044; resampled 2.5th–97.5th percentiles 1.000–1.155), but this direction is part of the M1 assumption. Minimum concentration rose to 1.86 times for evenly spaced 8-hourly TID (M1) and fell to 0.87 times for TID with a 12-hour night gap. These are assumption-based exposure comparisons, not predictions of clinical effect.

## Data and code availability

The archive contains input values, PK numbers extracted from the original report, six summary tables, three figures and the code for rerunning the analysis. Original IDs were replaced by block numbers, and personal information other than PK, the complete source workbook and the trial protocol are not included. Extracted values follow the original report's CC BY 4.0 license, with source and transformations stated ([License](https://creativecommons.org/licenses/by/4.0/)).

Nine numerical checks covered an independent ordinary differential equation (ODE) calculation of dosing events, periodic integration, grid width for minima and peaks, mass balance of the proportional model and cancellation of the multipliers. Agreement of the implementations does not imply clinical validation of TID. The original analysis checked sources on October 24, 2026; escalation rules, PK results and target-occupancy statements were rechecked on October 29, 2026.

[Analysis code, input values, summary tables and rerun instructions](shared/olomorasib-dose-fractionation/fractionation-analysis.zip)

## References {#references}

<span id="ref-1"></span>
1. Murciano-Goroff YR, Hollebecque A, Heist RS, Cassier PA, Han JY, Kim SY, et al. Pan-tumor activity of olomorasib, a next-generation KRAS G12C inhibitor in KRAS G12C-mutant advanced solid tumors: a first-in-human study. Nat Commun. 2026;17(1):3834. [doi:10.1038/s41467-026-69943-7](https://doi.org/10.1038/s41467-026-69943-7).

<span id="ref-2"></span>
2. Burns TF, Ammakkanavar NR, Hollebecque A, Lee DH, Koyama T, Cassier PA, et al. Efficacy and safety of olomorasib in combination with pembrolizumab in treatment of patients with KRAS G12C-mutant advanced NSCLC. J Thorac Oncol. 2026;21(4):103528. [doi:10.1016/j.jtho.2025.11.018](https://doi.org/10.1016/j.jtho.2025.11.018).

<span id="ref-3"></span>
3. Murciano-Goroff YR, Hollebecque A, Heist RS, Cassier PA, Han JY, Kim SY, et al. Supplementary Information for: Pan-tumor activity of olomorasib, a next-generation KRAS G12C inhibitor in KRAS G12C-mutant advanced solid tumors: a first-in-human study [Supplementary material]. Nat Commun; 2026. File 41467_2026_69943_MOESM1_ESM.pdf. [Supplementary Information](https://media.springernature.com/full/springer-static/esm/art%3A10.1038%2Fs41467-026-69943-7/MediaObjects/41467_2026_69943_MOESM1_ESM.pdf).

<span id="ref-4"></span>
4. Murciano-Goroff YR, Hollebecque A, Heist RS, Cassier PA, Han JY, Kim SY, et al. Source Data for: Pan-tumor activity of olomorasib, a next-generation KRAS G12C inhibitor in KRAS G12C-mutant advanced solid tumors: a first-in-human study [Dataset]. Nat Commun; 2026. File 41467_2026_69943_MOESM4_ESM.xlsx. [Source Data](https://media.springernature.com/full/springer-static/esm/art%3A10.1038%2Fs41467-026-69943-7/MediaObjects/41467_2026_69943_MOESM4_ESM.xlsx).
