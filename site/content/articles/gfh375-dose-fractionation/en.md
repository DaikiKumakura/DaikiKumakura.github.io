GFH375 (VS-7375) is an oral inhibitor that targets both the ON state (GTP-bound) and the OFF state (GDP-bound) of KRAS G12D. The phase I report appeared in 2026, and the recommended phase II dose was declared as 600 mg once daily (QD) ([1](#ref-1)).

Would splitting that 600 mg into 300 mg twice daily (BID) lower the maximum concentration (Cmax) while maintaining the concentration before the next dose? A linear pharmacokinetic (PK) model readily predicts this pattern. For GFH375, however, 300 mg BID has already been tested in a small cohort, and its mean concentration profile is public ([1](#ref-1), [Extended Data Figure 1](https://www.nature.com/articles/s41591-026-04559-4/figures/4)). The prediction can therefore be checked against that profile.

I digitized public figures and fitted a small model to the 600 mg QD mean concentration profile. In 2,048 paired virtual individuals, the within-individual Cmax ratio of 300 mg BID to 600 mg QD had a median of 0.583. The public BID profile, a mean of three patients that was not used in the fit, showed a 2 h concentration of approximately 393 ng/mL, well above the predicted 203 ng/mL. This mismatch means that the fit to 600 mg QD gave no basis for predicting a peak reduction with split dosing.

## Introduction {#_1}

There are two questions. How does splitting the same 600 mg/day change the peak and minimum concentrations? Is that prediction consistent with the public BID profile?

This analysis explores, from public aggregate data alone, whether the prediction for split dosing is consistent with the public BID profile. It is not a model for choosing treatment or trial doses. It fits published aggregate curves and does not estimate a new nonlinear mixed-effects (NLME) model from individual-level data.

The compared regimens are 600 mg QD, BID with 300 mg every 12 h, BID with uneven 8 h and 16 h intervals, and 400 mg QD. The 400 mg QD regimen is not a split dose; it reduces the daily dose to two thirds.

## Methods

### Public sources and digitization {#_2}

The sources were the public abstract, the Extended Data, and the supplement with the protocol. The article body was not checked. Concentrations are plasma concentrations. Error bars on the mean profiles are standard errors of the mean (SEM), not standard deviations (SD), and cannot directly represent between-person variability ([1](#ref-1), [Extended Data Figure 1](https://www.nature.com/articles/s41591-026-04559-4/figures/4)).

Table 1. Mean profiles and AUC distributions in the public figures. AUC0–24 is the area under the concentration–time curve from 0 to 24 h, and IQR is the interquartile range. N and n are the sample sizes shown in the original figures.

| Public material | Population | Use in this analysis |
| --- | --- | --- |
| Mean PK curve, 600 mg QD | Figure N=24 | Model fit, 9 time points |
| Mean PK curve, 400 mg QD | N=27 | Check not used in the fit, 9 time points |
| Mean PK curve, 750 mg QD | N=4 | Check not used in the fit, 9 time points |
| Mean PK curve, 300 mg BID | N=3 | Check not used in the fit, 8 time points over 0–12 h |
| AUC0–24 distribution, 600 mg QD | n=25 | Approximate variability scale from the IQR |
| AUC0–24 distribution, 400 mg QD | n=26 | Structural sensitivity of variability |

Curve and AUC sample sizes differ, so they are not treated as records of the same individuals ([1](#ref-1), [Extended Data Figure 2](https://www.nature.com/articles/s41591-026-04559-4/figures/5)).

I calibrated the axes of the original figures and recorded the center of each point and the quartiles of the AUC boxes as pixel coordinates. The concentration axis is logarithmic, and the distributed code converts vertical pixel positions into concentrations, with the coordinate CSV files. These readings do not have the precision of the original clinical data.

The 600 mg QD AUC0–24 median was approximately 2,597 ng·h/mL, and the first to third quartiles (Q1–Q3) were approximately 1,549–3,271 ng·h/mL. Treating all AUC variability as clearance variability, I defined an approximate log-scale variability by the following equation, where log is the natural logarithm and \(\Phi^{-1}\) is the standard normal quantile function.

\[
\sigma=\frac{\log Q_3-\log Q_1}{2\Phi^{-1}(0.75)}=0.554
\]

The box is not perfectly log-symmetric, so this does not mean that a lognormal distribution reproduces the full distribution.

### Model and estimation {#_3}

I kept the model as small as would still describe the peak. I first tried a one-compartment model with first-order absorption, then a two-compartment model with first-order absorption. Because the former fit poorly and the latter gave unstable coefficients (Table 3), I adopted a model with two preabsorption states and central and peripheral distribution states. Both absorption stages share the rate \(k_a\); no second absorption rate is estimated.

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

Between-individual variability is restricted to \(CL_i=CL\exp(\eta_i),\eta_i\sim N(0,\sigma^2)\). Variability in V or absorption, and their correlations, are not estimated. When fitting the mean profile, the arithmetic mean of individual profiles under this assumption is computed by Gauss–Hermite quadrature. A box median is not fitted directly to the mean profile.

Five coefficients (CL/F, Vc/F, Q/F, Vp/F and \(k_a\)) were estimated by minimizing the residual sum of squares of log concentrations over the nine 600 mg QD points. Error correlations between time points and the exact number of patients at each time point are unknown, so SEM was not used as an independent precision weight. These coefficients are a conditional approximation specific to this analysis, not the final coefficients of a published population PK model.

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

For 750 mg QD, the dose-proportional prediction overestimated the highest mean concentration. The supplementary protocol describes attenuated exposure increases at high doses ([1](#ref-1), [supplement and protocol: RP2D rationale](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-026-04559-4/MediaObjects/41591_2026_4559_MOESM1_ESM.pdf)). RP2D is the recommended phase II dose. Transferring the absorption and input estimated at 600 mg unchanged to another dose risks error in both directions, overestimation and underestimation.

Trapezoidal integration of the mean profiles gave approximately 3,273 ng·h/mL for 600 mg QD over 0–24 h and approximately 1,604 ng·h/mL for 300 mg BID over 0–12 h. Assuming that BID repeats the same 12 h profile and doubling it gives a daily AUC ratio of approximately 0.98. This is a description based on integrating sparse mean points and a repetition assumption, not a comparison of published individual AUCs or proof of equivalence. A similar AUC does not imply that the peak prediction is correct.

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

Shifting vertical pixel positions by ±2 pixels and refitting 160 times gave a 5th–95th percentile range of approximately 0.578–0.586 for the BID/QD peak ratio at \(\eta=0\). This is sensitivity to the digitized position, not a patient-resampling bootstrap or a clinical confidence interval. Pixel-position error alone did not explain the large mismatch with observed BID.

When variability was set to 0, or replaced by the wider log-IQR scale of the 400 mg group (0.808), and the model was refitted, the median linear BID peak ratios were approximately 0.610 and 0.557. Changing the assumed variability is a separate matter from verifying whether the absorption structure transfers to BID.

## Discussion {#_6}

The 600 mg QD mean profile predicted a lower peak with 300 mg BID, but the prediction did not match the observed BID profile near its peak, which was not used in the fit. This analysis cannot identify the cause of the mismatch. Candidates are the separate three-patient cohort, differences in background or food, differences in absorption with dose or dosing frequency, and digitization error; the sensitivity analysis showed that pixel position alone did not explain it. The assumption that QD input transfers to BID is not supported, and the prediction gives no basis for preferring BID.

The 400 mg QD regimen differs from split dosing in that it also reduces the daily dose. A linear prediction lowers all exposure metrics to two thirds, but cohort differences and dose nonlinearity prevent a judgment about retained efficacy. Adverse-event comparisons for BID in the public supplement involve small nonrandomized groups and do not isolate a safety benefit mediated by a lower peak ([1](#ref-1), [Supplementary Table 1](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-026-04559-4/MediaObjects/41591_2026_4559_MOESM1_ESM.pdf)).

## Limitations

- The inputs are mean values digitized from public figures, not individual-level data. Their precision is lower than that of the original clinical data.
- The variability scale is a clearance-only approximation borrowed from the same public figure; variability in V or absorption and their correlations are not estimated.
- Observed BID is the mean of a separate cohort of three patients, not matched to the other cohorts for background, food or absorption.
- The dose dependence \(\beta\) is an assumed scenario and was not estimated from observations.
- The article body was not read; the analysis is limited to the public abstract, Extended Data and supplement.
- Efficacy, toxicity and target binding are not modeled.

## Conclusion

The fit to the 600 mg QD mean profile predicted a lower peak with 300 mg BID in virtual individuals (median Cmax ratio 0.583). The public 2 h mean concentration with 300 mg BID (approximately 393 ng/mL), however, was well above that prediction (approximately 203 ng/mL). The fit to the 600 mg QD mean profile did not reproduce the peak of the BID profile that was not used in the fit. The prediction cannot be used as a basis for choosing split dosing or for expecting a peak reduction.

## Data and code availability {#_7}

The [analysis code, inputs, aggregate tables and rerun instructions](shared/gfh375-dose-fractionation/fractionation-analysis.zip) contain the digitized coordinates, analysis and checking code, nine aggregate CSV files, three figures, the results JSON and records of the execution environment. The README steps (`python analysis/run_analysis.py` and `python -m unittest discover -s analysis -p "test_model.py" -q`) need neither a network connection nor the original PDF. The random seed is 20261023. The code is under the MIT license, and the figures are author-made plots from digitized values. Original paper images, PDFs and individual clinical records are not redistributed. Eight checks that compare the closed-form calculations with independent matrix exponentials, numerical integration and fine time grids verify the implementation, not clinical predictions. The public sources were checked on October 23, 2026.

## References {#article-references}

1. <span id="ref-1"></span>Ai X, Song Z, Wu L, Zhou A, Cheng D, Zong H, et al. Oral KRAS G12D inhibitor GFH375 for previously treated advanced solid tumors with KRASG12D mutations: a phase 1 trial. Nat Med. 2026;32(9):3302–3312. [doi:10.1038/s41591-026-04559-4](https://doi.org/10.1038/s41591-026-04559-4); [Extended Data Figure 1](https://www.nature.com/articles/s41591-026-04559-4/figures/4); [Extended Data Figure 2](https://www.nature.com/articles/s41591-026-04559-4/figures/5); [supplement and protocol](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-026-04559-4/MediaObjects/41591_2026_4559_MOESM1_ESM.pdf). Abstract, Extended Data and supplement used; article body not read.
