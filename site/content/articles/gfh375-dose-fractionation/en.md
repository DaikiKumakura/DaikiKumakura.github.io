GFH375 (VS-7375) is an oral inhibitor that targets both the ON state (GTP-bound) and the OFF state (GDP-bound) of KRAS G12D. The phase I report appeared in 2026, and the recommended phase II dose was declared as 600 mg once daily (QD) ([1](#ref-1)).

Would splitting that 600 mg into 300 mg twice daily (BID) lower the maximum concentration (Cmax) while maintaining the concentration before the next dose? A linear pharmacokinetic (PK) model readily predicts this pattern: when elimination is first order, concentrations are proportional to dose and superposition holds ([2](#ref-2)), so splitting the same daily dose leaves the AUC unchanged, lowers the peak and raises the trough. For GFH375, however, 300 mg BID has already been tested in a small cohort, and its mean concentration profile is public ([1](#ref-1), [Extended Data Figure 1](https://www.nature.com/articles/s41591-026-04559-4/figures/4)). The prediction can therefore be checked against that profile.

I digitized public figures and fitted a small model to the 600 mg QD mean concentration profile. In 2,048 paired virtual individuals, the within-individual Cmax ratio of 300 mg BID to 600 mg QD had a median of 0.583. The public BID profile, a mean of three patients that was not used in the fit, showed a 2 h concentration of approximately 393 ng/mL, well above the predicted 203 ng/mL, and its predose and 12 h concentrations (approximately 54 and 46 ng/mL) were below the predicted 73 ng/mL. A three-patient mean carries too little information to reject the model, but the fit to 600 mg QD gave no basis for predicting a peak reduction with split dosing.

## Introduction {#_1}

There are two questions. How does splitting the same 600 mg/day change the peak and minimum concentrations? Is that prediction consistent with the public BID profile?

This analysis explores, from public aggregate data alone, whether the prediction for split dosing is consistent with the public BID profile. It is not a model for choosing treatment or trial doses. It fits published aggregate curves and does not estimate a new nonlinear mixed-effects (NLME) model from individual-level data.

The compared regimens are 600 mg QD, BID with 300 mg every 12 h, BID with uneven 8 h and 16 h intervals, and 400 mg QD. The 400 mg QD regimen is not a split dose; it reduces the daily dose to two thirds.

## Methods

### Public sources and digitization {#_2}

The sources were the public abstract, the Extended Data figures and legends, and the supplement (protocol and adverse-event table). The article body requires a subscription and was not read. According to the abstract, 74 patients received GFH375 orally once or twice daily, and the recommended phase II dose was declared as 600 mg once daily ([1](#ref-1)). The legend of Extended Data Figure 1 states that the figure shows mean plasma concentration–time curves at steady state. Error bars on the mean profiles are standard errors of the mean (SEM), not standard deviations (SD), and cannot directly represent between-person variability ([1](#ref-1), [Extended Data Figure 1](https://www.nature.com/articles/s41591-026-04559-4/figures/4)).

Table 1. Mean profiles and AUC distributions in the public figures. AUC0–24 is the area under the concentration–time curve from 0 to 24 h, and IQR is the interquartile range. N and n are the sample sizes shown in the original figures.

| Public material | Population | Use in this analysis |
| --- | --- | --- |
| Mean PK curve, 600 mg QD | Figure N=24 | Model fit, 9 time points |
| Mean PK curve, 400 mg QD | N=27 | Check not used in the fit, 9 time points |
| Mean PK curve, 750 mg QD | N=4 | Check not used in the fit, 9 time points |
| Mean PK curve, 300 mg BID | N=3 | Check not used in the fit, 0–12 h, 8 time points |
| AUC0–24 distribution, 600 mg QD | n=25 | Approximate variability scale from the IQR |
| AUC0–24 distribution, 400 mg QD | n=26 | Structural sensitivity of variability |

Curve and AUC sample sizes differ, so they are not treated as records of the same individuals ([1](#ref-1), [Extended Data Figure 2](https://www.nature.com/articles/s41591-026-04559-4/figures/5)). The numbers of patients in Supplementary Table 1 are 29 for 400 mg QD, 29 for 600 mg QD, 8 for 750 mg QD and 3 for 300 mg BID ([1](#ref-1), [Supplementary Table 1](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-026-04559-4/MediaObjects/41591_2026_4559_MOESM1_ESM.pdf)), so the curve Ns (27, 24, 4, 3) are smaller except for 300 mg BID. The legend does not say how patients were selected for the curves.

I calibrated the axes of the original figures and recorded the center of each point and the quartiles of the AUC boxes as pixel coordinates. The concentration axis is logarithmic, and the distributed code converts vertical pixel positions into concentrations, with the coordinate CSV files. In the calibration, the interval from 100 ng/mL to 1,000 ng/mL spans 164 pixels, so a vertical shift of ±2 pixels corresponds to about ±2.8% in concentration. Digitization of graphed data has shown high intercoder reliability and validity with a web-based tool, but that study used single-case line graphs ([3](#ref-3)), and the same precision need not apply to the log-axis mean profiles and box plots used here. These readings do not have the precision of the original clinical data.

The 600 mg QD AUC0–24 median was approximately 2,597 ng·h/mL, and the first to third quartiles (Q1–Q3) were approximately 1,549–3,271 ng·h/mL. Treating all AUC variability as clearance variability, I defined an approximate log-scale variability by the following equation, where log is the natural logarithm and \(\Phi^{-1}\) is the standard normal quantile function.

\[
\sigma=\frac{\log Q_3-\log Q_1}{2\Phi^{-1}(0.75)}=0.554
\]

The box is not perfectly log-symmetric, so this does not mean that a lognormal distribution reproduces the full distribution.

### Model and estimation {#_3}

I kept the model as small as would still describe the peak. I first tried a one-compartment model with first-order absorption, then a two-compartment model with first-order absorption. Because the former fit poorly and the latter gave unstable coefficients (Table 3), I adopted a model with two preabsorption states and central and peripheral distribution states. Both absorption stages share the rate \(k_a\); no second absorption rate is estimated. A chain of compartments with a common rate corresponds to the structure of transit compartment models for absorption delay ([4](#ref-4)). Population PK primers also note that too many compartments can let the parameters of a peripheral compartment drift to values with little influence on the concentrations and be estimated with poor precision ([2](#ref-2)).

\[
\dot A_{g1}=-k_aA_{g1},\qquad
\dot A_{g2}=k_aA_{g1}-k_aA_{g2},
\]
\[
\dot A_c=k_aA_{g2}-\frac{CL+Q}{V_c}A_c+\frac{Q}{V_p}A_p,
\qquad
\dot A_p=\frac{Q}{V_c}A_c-\frac{Q}{V_p}A_p,
\]
\[
C(t)=1000A_c(t)/V_c.
\]

\(A_{g1}\) and \(A_{g2}\) are the amounts in the two preabsorption states, \(A_c\) is the central amount, and \(A_p\) is the peripheral amount. \(CL\) is clearance, \(Q\) is intercompartmental clearance, and \(V_c\) and \(V_p\) are the central and peripheral volumes of distribution. Time is in h, amounts in mg, concentration in ng/mL, CL and Q in L/h, and V in L. Because the data come from oral dosing only, CL and V are treated as apparent CL/F and V/F, where F is bioavailability. Each dose adds its amount to \(A_{g1}\), and steady-state profiles are computed by superposition.

Between-individual variability is restricted to \(CL_i=CL\exp(\eta_i),\eta_i\sim N(0,\sigma^2)\). Describing between-individual variability through normally distributed individual deviations \(\eta\) is the standard framework of population PK ([2](#ref-2)). Variability in V or absorption, and their correlations, are not estimated. When fitting the mean profile, the arithmetic mean of individual profiles under this assumption is computed by Gauss–Hermite quadrature. A box median is not fitted directly to the mean profile.

Five coefficients (CL/F, Vc/F, Q/F, Vp/F and \(k_a\)) were estimated by minimizing the residual sum of squares of log concentrations over the nine 600 mg QD points. Error correlations between time points and the exact number of patients at each time point are unknown, so SEM was not used as an independent precision weight. These coefficients are a conditional approximation specific to this analysis, not the final coefficients of a published population PK model. There are only four more points than fitted coefficients. Unknown correlation between times prevents treating this count as residual degrees of freedom for a test. The goodness of fit in Table 3 shows how well the 600 mg QD profile was described and is not a validation.

Models were compared by the log-residual sum of squares, the largest relative discrepancy at a time point, and the condition number of the Jacobian matrix. A larger condition number indicates less stable coefficient estimation.

For regimen comparisons, the random seed was fixed at 20261023 and all regimens were applied to 2,048 paired virtual individuals. Each regimen was computed in the same individual as 600 mg QD, and within-individual ratios were taken. The main assumption is that input is proportional to the dose and that absorption and distribution estimated at 600 mg transfer to 300 mg. As a sensitivity analysis of this assumption, the effective input at dose D was set to \(600(D/600)^\beta\). \(\beta\) is not a coefficient estimated from observations; it is a scenario that varies the unknown dose dependence.

Sensitivity to digitization was examined by shifting vertical pixel positions uniformly within ±2 pixels and refitting 160 times. Sensitivity to the variability assumption was examined by refitting with \(\sigma\) set to 0, to 0.554, and to 0.808 derived from the 400 mg QD AUC distribution.

## Results

### Fit to the mean profile

Table 2. Conditional coefficients estimated from the mean profile.

| Conditional coefficient | Estimate |
| --- | ---: |
| CL/F | 216.9 L/h |
| Vc/F | 742.0 L |
| Q/F | 160.7 L/h |
| Vp/F | 2,015 L |
| Each two-stage absorption rate ka | 0.871 /h |

Table 3. Comparison of fits to the mean profile. The largest relative discrepancy is the largest relative difference from the digitized value among the nine 600 mg QD time points.

| Model | Log-residual sum of squares | Largest relative discrepancy at a time point | Interpretation |
| --- | ---: | ---: | --- |
| First-order absorption, 1 compartment | 0.381 | 36.1% | Systematic shape mismatch remains |
| First-order absorption, 2 compartments | 0.201 | 26.4% | Unstable distribution coefficients |
| Two-stage absorption, 2 compartments | 0.0253 | 11.7% | Adopted to describe the conditional profile |

The one-compartment model underestimated the 2 h mean concentration by approximately 29%, and its later residuals retained a systematic shape. The two-compartment first-order absorption model gave a large peripheral volume and a Jacobian condition number of approximately 8,771. The condition numbers were approximately 6.6 for the one-compartment model and 50.9 for the adopted model.

The adopted model gave an AUC median of approximately 2,766 ng·h/mL, 6.5% above the digitized value of approximately 2,597 ng·h/mL. Because the variability scale was borrowed from the same public figure, this comparison is not independent patient-level validation.

Two quantities could be checked against the PK statements in the supplementary protocol. The first is the terminal half-life. Computed as an eigenvalue of the system matrix from the Table 2 coefficients, the terminal half-life after a single dose is about 16 h, which is about 12–25% shorter than the single-dose half-life of 18.5–21.6 h that the protocol reports for 400–900 mg QD ([1](#ref-1), [supplement and protocol: RP2D rationale](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-026-04559-4/MediaObjects/41591_2026_4559_MOESM1_ESM.pdf)). The half-life was not part of the fitting objective, so this is only a rough consistency check. The second is the predose concentration. The protocol gives the mean trough concentration above 400 mg as 34.4–50.2 ng/mL. The digitized 600 mg QD concentrations at 0 h and 24 h are about 54 and 56 ng/mL, and those for 750 mg QD are about 61 and 76 ng/mL, all above this range. The protocol statement rests on an earlier summary of 33 patients as of January 17, 2025, and may differ from Extended Data Figure 1 in patients and time point. A digitization error of ±2.8% alone hardly explains the excess of about 8–11% for 600 mg QD, but the public sources contain no information to isolate the cause.

![Fit to the 600 mg QD mean profile and checks at other doses and BID](shared/gfh375-dose-fractionation/figures/fit-and-heldout.png)

Figure 1. Left: digitized 600 mg QD mean profile (black circles, N=24) with curves from the one-compartment first-order absorption model (1comp-first) and the two-compartment two-stage absorption model (2comp-two-stage). Right: digitized mean profiles not used in the fit for 400 mg QD (N=27), 750 mg QD (N=4) and 300 mg BID (N=3) (points), with predictions from the 600 mg QD coefficients (lines). Concentrations are plasma concentrations in ng/mL. The right panel compares different cohorts, not within-patient regimen changes. Large mismatches remain for 750 mg QD and BID. This is the author's re-plot of digitized values; the original figure images are not reproduced.

### Predictions for split dosing in virtual individuals {#_4}

Table 4. Regimen comparison relative to 600 mg QD. Medians of within-individual ratios (5th–95th percentiles) in the same 2,048 virtual individuals.

| Regimen | Cmax within-individual ratio | Minimum-concentration within-individual ratio | AUC24 within-individual ratio |
| --- | ---: | ---: | ---: |
| 300 mg every 12 h | 0.583 (0.525–0.696) | 1.43 (1.23–1.61) | 1.000 |
| 300 mg at 8/16 h intervals | 0.615 (0.539–0.737) | 1.21 (1.12–1.32) | 1.000 |
| 400 mg QD | 0.667 | 0.667 | 0.667 |

Parentheses show conditional between-individual 5th–95th percentiles, not confidence intervals of the coefficients. Minimum concentration is the lowest value within 24 h, and AUC24 is the area under the curve over 24 h.

With linear input, splitting lowers the peak and raises the minimum concentration. With 8/16 h intervals the peak is higher and the trough lower than with equal intervals. Equal AUC at the same daily dose follows from linear mass balance and is not evidence of preserved efficacy or clinical predictive accuracy.

![Regimen comparison in the same virtual individuals](shared/gfh375-dose-fractionation/figures/conditional-regimens.png)

Figure 2. Predictions under the assumption that the model transfers correctly. Points are medians of within-individual ratios in the same 2,048 virtual individuals, error bars are 5th–95th percentiles, and dashed lines mark 1.0, the same value as 600 mg QD. Ratios are relative to 600 mg QD. Error bars are not visible for 400 mg QD because the ratio is identical in every individual. cmax is Cmax, cmin is the minimum concentration within 24 h, and auc24 is AUC24. Because of the mismatch with observed BID, this figure alone does not justify choosing split dosing.

### Comparison with observed BID {#bid}

The highest mean concentration read from each public profile was compared with the model prediction at the same time.

Table 5. Highest mean concentration in each cohort and the model prediction at the same time. Concentrations are in ng/mL.

| Cohort | Figure N | Time of highest mean | Digitized value | Model prediction at the same time |
| --- | ---: | ---: | ---: | ---: |
| 600 mg QD (fit) | 24 | 2 h | 351 | 326 |
| 400 mg QD (check) | 27 | 2 h | 269 | 217 |
| 750 mg QD (check) | 4 | 4 h | 285 | 395 |
| 300 mg BID (check) | 3 | 2 h | 393 | 203 |

The values in Table 5 are maxima of mean profiles, not means of individual Cmax values.

The 2 h prediction for 300 mg BID was approximately 48% below the digitized mean. In the public figure the highest mean concentration for BID exceeds that for 600 mg QD, so the observation does not support the predicted peak reduction. However, the BID cohort is a separate group of three patients, and background, individual absorption and food are not matched. This comparison alone also cannot establish that BID causally raises the peak.

The trough prediction also failed. The digitized 300 mg BID concentrations at 0 h and 12 h are about 54 and 46 ng/mL, below the model value of about 73 ng/mL (the same at 0 h and 12 h); the ratios of digitized value to prediction are 0.74 and 0.63. The linear prediction was a higher trough (median within-individual ratio 1.43), but the trough of the public BID profile did not exceed the 24 h value of 600 mg QD (about 56 ng/mL). The peak-to-trough ratios from the digitized values are about 7.2–8.6 for BID (393/54, 393/46) and about 6.3 for 600 mg QD (351/56), the opposite of the prediction that BID would be flatter. These are ratios of mean-profile readings, not individual-level ratios.

The effect of the three-patient mean could not be separated quantitatively. In the virtual individuals, the individual Cmax for 300 mg BID has a 5th–95th percentile range of about 111–374 ng/mL (median about 200 ng/mL), and the digitized three-patient mean of about 393 ng/mL lies above its upper end. An individual-level quantile range is not a prediction interval for a three-patient mean; this comparison does not calculate a discrepancy probability. However, that variability is a clearance-only approximation and is far narrower than the geometric CV of 111–127% for Cmax and AUC that the supplementary protocol reports for the 400 mg QD cohort. A lognormal distribution with a geometric CV of 111% has a 5th–95th percentile ratio of about 19, whereas the virtual Cmax for 600 mg QD spans only about 2.5-fold (537/211 ng/mL). If real variability is large, a three-patient mean has more room to depart from the prediction. Only means are public and individual values for the three patients are not, so how much sampling variability explains the mismatch could not be calculated ([1](#ref-1), [supplement and protocol: RP2D rationale](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-026-04559-4/MediaObjects/41591_2026_4559_MOESM1_ESM.pdf)).

For 750 mg QD, the dose-proportional prediction overestimated the highest mean concentration. The RP2D rationale in the supplementary protocol states that exposure increased with dose over 100–400 mg but not markedly over 400–900 mg ([1](#ref-1), [supplement and protocol: RP2D rationale](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-026-04559-4/MediaObjects/41591_2026_4559_MOESM1_ESM.pdf)). RP2D is the recommended phase II dose. Transferring the absorption and input estimated at 600 mg unchanged to another dose risks error in both directions, overestimation and underestimation.

Trapezoidal integration of the mean profiles gave approximately 3,273 ng·h/mL for 600 mg QD over 0–24 h, 2,184 ng·h/mL for 400 mg QD, 2,924 ng·h/mL for 750 mg QD, and 1,604 ng·h/mL for 300 mg BID over 0–12 h. Assuming that BID repeats the same 12 h profile and doubling it gives a daily AUC ratio of approximately 0.98. The AUC divided by dose was about 5.5 for 400 mg QD, 5.5 for 600 mg QD, 3.9 for 750 mg QD, and 5.3 ng·h/mL/mg for 300 mg BID (converted to a daily dose). That dose-normalized AUC is independent of dose is a classical indicator of linearity ([2](#ref-2)). In these readings, exposure was close to linear across 400–600 mg QD and BID, and a drop appeared only at 750 mg QD (four patients). This disagrees with the protocol statement that the increase was not marked over 400–900 mg, but differences in patients and time point cannot be separated. All of this is a description based on integrating sparse mean points and a repetition assumption, not a comparison of published individual AUCs or proof of equivalence. A similar AUC does not imply that the peak prediction is correct. Indeed, the BID mismatch appeared in the shape of the curve (peak and trough) rather than in the total exposure.

### Sensitivity to the input assumption {#_5}

Table 6. Sensitivity to the dose-dependent input assumption. Between-individual variability \(\sigma\)=0.554; medians of within-individual ratios of 300 mg BID to 600 mg QD.

| Input assumption | β | Median Cmax ratio for 300 mg BID | Median minimum-concentration ratio | AUC24 ratio |
| --- | ---: | ---: | ---: | ---: |
| Higher input efficiency at smaller doses | 0.5 | 0.824 | 2.02 | 1.414 |
| Dose proportionality | 1.0 | 0.583 | 1.43 | 1.000 |
| Lower input efficiency at smaller doses | 1.5 | 0.412 | 1.01 | 0.707 |

Allowing dose-dependent input breaks the equality of AUC at the same 600 mg/day. Changing \(\beta\) rescales the input but does not explain the sharp observed BID peak. The amount and the shape of the input are separate issues.

![Sensitivity to dose-dependent input and the mismatch with the observed BID peak](shared/gfh375-dose-fractionation/figures/sensitivity-and-bid-check.png)

Figure 3. Left: ratios of 300 mg BID to 600 mg QD for Cmax, minimum concentration and AUC24 (medians; legend cmax_ratio, cmin_ratio, auc24_ratio) as the assumed \(\beta\) varies. The dashed line at 1.0 marks equality. Right: digitized mean concentrations of 300 mg BID (N=3; points) and the prediction from the 600 mg QD coefficients (line). Concentrations are plasma concentrations in ng/mL. The points on the right are readings from a three-patient mean profile, not individual-level predictive validation.

Shifting vertical pixel positions by ±2 pixels and refitting 160 times gave a 5th–95th percentile range of approximately 0.578–0.586 for the BID/QD peak ratio at \(\eta=0\). This is sensitivity to the digitized position, not a patient-resampling bootstrap or a clinical confidence interval. Pixel-position error alone did not explain the large mismatch with observed BID. A shift of ±2 pixels is about ±2.8% in concentration, much smaller than the roughly 48% by which the 2 h BID prediction falls below the digitized value.

When variability was set to 0, or replaced by the wider log-IQR scale of the 400 mg group (0.808), and the model was refitted, the median linear BID peak ratios were approximately 0.610 and 0.557. Changing the assumed variability is a separate matter from verifying whether the absorption structure transfers to BID.

## Discussion {#_6}

The 600 mg QD mean profile predicted a lower peak and a higher trough with 300 mg BID. The public BID profile, which was not used in the fit, had a higher peak than predicted (about 393 versus 203 ng/mL) and a lower trough (about 54 and 46 ng/mL at 0 h and 12 h versus 73 ng/mL). This result does not support the assumption that the QD absorption and distribution transfer to BID. It does not refute the assumption either, because the comparator is the mean of a separate three-patient cohort, individual values are not available, and sampling variability cannot be calculated.

This analysis cannot identify the cause of the mismatch. Candidates are sampling variability in a three-patient mean (including the possibility that the model's between-individual variability is narrower than the real one), differences in background, food or sampling day, differences in absorption with dose or dosing frequency, and digitization error. Digitization error of ±2 pixels (about ±2.8%) did not explain it. Moving \(\beta\), which represents the input efficiency per dose, from 0.5 to 1.5 gives median BID/QD Cmax ratios of only 0.41–0.82, short of the ratio of about 1.12 (393/351) between the highest mean concentrations in the figure. The former is a median of within-individual ratios and the latter a ratio of maxima of mean profiles, so the statistics differ. The ratio of mean values that the model gives at the same times is about 0.62 (203/326), and the gap is not closed by the difference in statistics. Because total exposure was nearly linear in dose-normalized AUC, it is natural to read the mismatch as one of curve shape, that is, of the time course of absorption, rather than of magnitude; this is a hypothesis that this analysis did not test.

The 400 mg QD regimen differs from split dosing in that it also reduces the daily dose. A linear prediction lowers all exposure to two thirds. The trapezoidal AUC of the digitized mean profile was about 0.67 times that of 600 mg QD (2,184/3,273), which agreed with the prediction. This does not confirm that the shape of the peak and trough also agrees; in Table 5 the 2 h prediction for 400 mg QD is about 19% below the digitized value.

### Implications {#implications}

On reading the source study. In Extended Data Figure 1 the peak of the 300 mg BID mean profile appears higher than that of 600 mg QD, but this compares separate cohorts of three and 24 patients rather than dosing schedules within individuals, and it does not show that BID raises the peak. The supplement states that Grade 2 diarrhea and vomiting in the 300 mg BID cohort (three patients) were 33.3% and 66.7%, higher than in the 600 mg QD cohort ([1](#ref-1), [supplement and protocol: RP2D rationale](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-026-04559-4/MediaObjects/41591_2026_4559_MOESM1_ESM.pdf)). That is one and two of three patients and does not measure the effect of split dosing. The chain in which splitting lowers the peak and thereby reduces gastrointestinal adverse events is confirmed by neither the public PK summaries nor the adverse-event counts.

On reading the prediction. That AUC matches at the same daily dose follows from mass balance and does not confirm the model. Here, AUC and dose-normalized AUC looked close to linear, yet the peak and trough did not match. A split-dosing prediction judged by AUC alone therefore gives no basis for extrapolating to the peak or trough. The median Cmax ratio of 0.583 also moves between 0.41 and 0.82 with the assumed \(\beta\), so it is conditional on dose-dependent input magnitude as well as fixed absorption rates and distribution structure.

Individual BID concentrations, sampling days and food conditions were unavailable, preventing separation of absorption differences from cohort sampling. Sample size alone was not used to calculate power. This information gap neither validates the present prediction nor identifies a causal effect of dosing frequency.

## Limitations

- The inputs are mean values digitized from public figures, not individual-level data. Their precision is lower than that of the original clinical data.
- The variability scale is a clearance-only approximation borrowed from the same public figure; variability in V or absorption and their correlations are not estimated.
- Observed BID is the mean of a separate cohort of three patients, not matched to the other cohorts for background, food or absorption.
- The dose dependence \(\beta\) is an assumed scenario and was not estimated from observations.
- The article body was not read; the analysis is limited to the public abstract, Extended Data and supplement.
- The digitized predose concentrations are higher than the trough range given in the protocol, and the cause was not isolated.
- The numbers of patients in the safety analysis (Supplementary Table 1) differ from the Ns of the curves, and the basis for including patients in the curves is not known.
- Efficacy, toxicity and target binding are not modeled.

## Conclusion

Does splitting 600 mg into 300 mg BID lower the peak and keep the trough? In the prediction obtained by transferring the 600 mg QD mean profile linearly, the peak falls (median Cmax ratio 0.583) and the trough rises (1.43). The public three-patient mean for 300 mg BID did not match this prediction. The 2 h concentration of approximately 393 ng/mL was well above the predicted 203 ng/mL, and the concentrations at 0 h and 12 h (approximately 54 and 46 ng/mL) were below the predicted 73 ng/mL. A three-patient mean carries too little information to refute the prediction, but no public observation supports it. This analysis therefore concludes neither that split dosing lowers the peak nor that it does not. The prediction cannot be used as a basis for choosing split dosing or for expecting a peak reduction. The AUC of the mean profiles was close to linear for 400–600 mg QD and BID, so the mismatch appeared in the shape of the curve rather than in total exposure, but this analysis cannot identify its cause.

## Data and code availability {#_7}

The [analysis code, inputs, aggregate tables and rerun instructions](shared/gfh375-dose-fractionation/fractionation-analysis.zip) contain the digitized coordinates, analysis and checking code, nine aggregate CSV files, three figures, the results JSON and records of the execution environment. The README steps (`python analysis/run_analysis.py` and `python -m unittest discover -s analysis -p "test_model.py" -q`) need neither a network connection nor the original PDF. The random seed is 20261023. The code is under the MIT license, and the figures are author-made plots from digitized values. Original paper images, PDFs and individual clinical records are not redistributed. Eight checks that compare the closed-form calculations with independent matrix exponentials, numerical integration and fine time grids verify the implementation, not clinical predictions. In the text, the terminal half-life (an eigenvalue computed from the Table 2 coefficients), the dose-normalized AUC and the 5th–95th percentile ratio corresponding to a geometric CV are arithmetic on the distributed coefficients and tables and are not outputs of the distributed code. The BID trough values and the virtual-individual Cmax distribution are in the distributed curve-checks.csv and absolute-conditional-metrics.csv. The public sources were checked on October 23, 2026.

## References {#article-references}

1. <span id="ref-1"></span>Ai X, Song Z, Wu L, Zhou A, Cheng D, Zong H, et al. Oral KRAS G12D inhibitor GFH375 for previously treated advanced solid tumors with KRASG12D mutations: a phase 1 trial. Nat Med. 2026;32(9):3302–3312. [doi:10.1038/s41591-026-04559-4](https://doi.org/10.1038/s41591-026-04559-4); [Extended Data Figure 1](https://www.nature.com/articles/s41591-026-04559-4/figures/4); [Extended Data Figure 2](https://www.nature.com/articles/s41591-026-04559-4/figures/5); [supplement and protocol](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-026-04559-4/MediaObjects/41591_2026_4559_MOESM1_ESM.pdf). Abstract, Extended Data and supplement used; article body not read.
2. <span id="ref-2"></span>Mould DR, Upton RN. Basic concepts in population modeling, simulation, and model-based drug development-part 2: introduction to pharmacokinetic modeling methods. CPT Pharmacometrics Syst Pharmacol. 2013;2(4):e38. [doi:10.1038/psp.2013.14](https://doi.org/10.1038/psp.2013.14).
3. <span id="ref-3"></span>Drevon D, Fursa SR, Malcolm AL. Intercoder reliability and validity of WebPlotDigitizer in extracting graphed data. Behav Modif. 2017;41(2):323–339. [doi:10.1177/0145445516673998](https://doi.org/10.1177/0145445516673998).
4. <span id="ref-4"></span>Savic RM, Jonker DM, Kerbusch T, Karlsson MO. Implementation of a transit compartment model for describing drug absorption in pharmacokinetic studies. J Pharmacokinet Pharmacodyn. 2007;34(5):711–726. [doi:10.1007/s10928-007-9066-0](https://doi.org/10.1007/s10928-007-9066-0).
