Vepdegestrant is an oral proteolysis-targeting chimera (PROTAC) that degrades the estrogen receptor (ER), with a US-approved dose of 200 mg once daily (QD) with food ([1](#ref-1)). After an interruption and restart at the same dose, how does plasma exposure approach continued dosing?

I reused a published human population pharmacokinetic (PopPK) model to calculate exposure after omitting 2, 3, or 7 scheduled doses. With representative parameters and 28 preceding doses, first-day ratios of the area under the concentration–time curve (AUC) versus uninterrupted dosing were approximately 0.63, 0.56, and 0.50. Rapid early convergence was followed by a slower residual difference. However, model accumulation did not agree with label summaries. These are conditional calculations for considering restart PK measurements, not clinically validated recovery times.

## Question and time definitions

The question is how daily AUC, peak, and predose concentration approach an uninterrupted trajectory after restarting 200 mg QD. The intended use is planning PK measurements with a public model, not selecting a patient's restart day or dose or determining efficacy/safety recovery. Label-directed toxicity modifications are not recreated.

Assume 28 doses every 24 hours before interruption. The first omitted dose is at time 0 and the last administered dose at −24 hours. Omitting two doses skips times 0 and 24, with restart at 48 hours.

**Table 1.** Omitted doses and elapsed time from last dose to restart.

| Omitted scheduled doses | Last dose to restart | Restart dose |
| --- | --- | --- |
| 2 | 72 h | 200 mg QD |
| 3 | 96 h | 200 mg QD |
| 7 | 192 h | 200 mg QD |

Subsequent figures reset zero to restart. Day 1 denotes AUC over 0–24 hours, day 3 over 48–72, and day 7 over 144–168. The comparator is the same hypothetical individual continuing through the same calendar times. Food, concomitant treatment, and coefficients remain unchanged; physiological changes causing interruption are absent.

## The public human model

The 2026 paper models 3,625 PK samples from 452 participants using two compartments ([2](#ref-2)). Individual records are unavailable. I use the precision of [FDA Table 75, PDF p. 234](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/219835Orig1s000MultidisciplineR.pdf#page=234), printed p. 233 ([3](#ref-3)), corresponding to rounded coefficients in [original Table 1](https://doi.org/10.1002/jcph.70252).

**Table 2.** Reused coefficients and published bootstrap intervals.

| Parameter | Value | Bootstrap 95% interval | Unit |
| --- | ---: | --- | --- |
| CL/F | 11.759 | 10.9134–12.645 | L/h |
| Vc/F | 477.912 | 349.119–527.623 | L |
| Q/F | 2.556 | 1.814–5.5636 | L/h |
| Vp/F | 3061.81 | 975.264–7369.18 | L |
| ka | 0.803 | 0.3494–1.2241 | /h |
| D1 | 2.778 | 1.9757–3.3792 | h |

Clearances and volumes are apparent oral parameters. A dose D supplies the gut compartment at D/D1 for D1 hours, while first-order absorption into the central compartment also occurs during input.

\[
\dot A_g=R_g(t)-k_aA_g,
\]

\[
\dot A_c=k_aA_g-\frac{CL+Q}{V_c}A_c+\frac{Q}{V_p}A_p,
\qquad
\dot A_p=\frac{Q}{V_c}A_c-\frac{Q}{V_p}A_p,
\]

\[
C(t)=1000A_c(t)/V_c.
\]

Time is h, amounts mg, and plasma concentration ng/mL. Zero-order input enters the gut, not the central compartment.

## Steady exposure alone does not validate restart predictions

A periodic state is the mathematical limit of prolonged dosing, not automatically the label's clinical statement of steady state in approximately seven days.

**Table 3.** Representative-parameter outputs and label summaries.

| Metric | Representative model | Label summary |
| --- | ---: | ---: |
| Periodic Cmax, ng/mL | 858 | 926 |
| Periodic 24-hour AUC, ng·h/mL | 17,008 | 17,155 |
| Periodic/first-dose Cmax | 2.35 | Accumulation approximately 1.3-fold |
| Periodic/first-dose AUC | 2.58 | Accumulation approximately 1.4-fold |

Steady AUC is close but accumulation differs. Representative parameters and clinical population summaries are different quantities, and matching populations, conditions, and ratio definitions were not established. The unresolved discrepancy prevents claiming validated restart prediction.

![Label-summary comparisons and approach to periodic AUC](shared/vepdegestrant-restart/figures/model-context.png)

**Figure 1.** Left, model/label ratios, not a formal external prediction-error estimate. Right, daily AUC relative to the periodic limit. The seven-day line marks the label statement and was not fitted.

Fast distribution and slowest model half-lives are approximately 23 and 1,016 hours, distinct from the label's effective 19-hour half-life and the 56-hour terminal value cited in the paper. A slow mathematical phase does not establish new observations validating that concentration range. Peripheral-volume uncertainty is also broad, 975–7,369 L.

## Subtracting omitted-dose contributions

Linearity permits subtracting missed-dose contributions from uninterrupted dosing. With single-dose concentration Cs, the restarted trajectory is

\[
C_{\mathrm{restart}}(t)=C_{\mathrm{continuous}}(t)
-\sum_{j=1}^{n}C_s(t+24j)
\]

Here n is omitted doses. Residual gut, central, and peripheral amounts are preserved rather than reset to zero; no additional loading dose is given. Let J(t) be cumulative single-dose AUC through t and m=0 denote the first restart day. Daily AUC deficit is

\[
\Delta AUC_m=J\{24(m+n+1)\}-J\{24(m+1)\}
\]

This avoids repeatedly integrating every dose history on a fine grid. Independent matrix-exponential dosing-event calculations provide a check.

![Restart profiles and daily AUC ratios versus continued dosing](shared/vepdegestrant-restart/figures/restart-profiles.png)

**Figure 2.** Solid lines show restart and same-colored dashed lines the matched uninterrupted trajectory. Right shows history-matched within-individual ratios. These are calculations, not observations in interrupted patients.

## Daily AUC, peak, and predose concentration differ

**Table 4.** Daily exposure ratios after restart.

| Omitted doses | 24-hour interval after restart | AUC ratio | Cmax ratio | End-interval predose ratio |
| --- | ---: | ---: | ---: | ---: |
| 2 | 1 | 0.625 | 0.638 | 0.661 |
| 2 | 3 | 0.907 | 0.911 | 0.914 |
| 2 | 7 | 0.989 | 0.990 | 0.988 |
| 2 | 14 | 0.995 | 0.996 | 0.993 |
| 2 | 28 | 0.996 | 0.997 | 0.995 |
| 3 | 1 | 0.564 | 0.580 | 0.605 |
| 3 | 3 | 0.890 | 0.895 | 0.898 |
| 3 | 7 | 0.986 | 0.987 | 0.984 |
| 3 | 14 | 0.992 | 0.994 | 0.990 |
| 3 | 28 | 0.994 | 0.995 | 0.992 |
| 7 | 1 | 0.503 | 0.524 | 0.547 |
| 7 | 3 | 0.867 | 0.874 | 0.873 |
| 7 | 7 | 0.974 | 0.978 | 0.969 |
| 7 | 14 | 0.982 | 0.986 | 0.977 |
| 7 | 28 | 0.986 | 0.989 | 0.982 |

Missing carryover reduces first-day exposure despite restarting the same 200 mg. Differences shrink by days 3 and 7, but after seven omissions day-28 AUC remains approximately 0.986. Near-convergence over a short period differs from equality of every model state. Predose concentration is evaluated at the next scheduled dose, not the strict minimum during the interval. Similar plasma exposure does not establish similar tumor concentration, ER degradation, or efficacy.

## Individual variation and a definition of return

Published log variances for CL/F and Vc/F are 0.192 and 0.251. The cross term 0.089 is accompanied by both omega-squared and correlation terminology, so its definition was not asserted without the control file. The primary scenario treats it as covariance, implying correlation approximately 0.405. Alternatives use correlation 0.089 or zero. This does not reconstruct the original full Omega. Other random effects are absent and residual errors are not added to latent exposure.

I use 2,048 paired individuals, seed 20261024, with identical histories across conditions. First daily AUC ratios reaching 90% or 95% of uninterrupted dosing are descriptive benchmarks without efficacy or safety justification.

**Table 5.** Daily intervals first reaching descriptive exposure benchmarks.

| Omitted doses | First daily AUC ratio at least 90% | First at least 95% |
| --- | --- | --- |
| 2 | Day 3 (days 2–5) | Day 4 (days 2–7) |
| 3 | Day 4 (days 2–6) | Day 5 (days 2–8) |
| 7 | Day 4 (days 2–7) | Day 5 (days 3–11) |

These are medians and 5th–95th percentiles under the primary scenario, not patient-resampling confidence intervals. Day k is a numbered 24-hour interval, not continuous-time threshold crossing. All simulated individuals reached both benchmarks within 60 days.

![Conditional daily AUC ratios in virtual individuals](shared/vepdegestrant-restart/figures/virtual-return.png)

**Figure 3.** With 0.089 as covariance, lines show medians and shading 5th–95th percentiles, excluding much coefficient uncertainty and clinical predictive uncertainty.

**Table 6.** Cross-term sensitivity after seven omitted doses, for the 95% benchmark.

| Cross-term assumption | Median | 5th–95th percentiles |
| --- | --- | --- |
| 0.089 as covariance | Day 5 | Days 3–11 |
| 0.089 as correlation | Day 5 | Days 2–12 |
| Correlation 0 | Day 5 | Days 2–13 |

Moving six fixed effects individually to published 95% endpoints gives day-7 AUC ratios of 0.941–0.984 after seven omissions; this is not a simultaneous interval. Prior histories of 7, 28, 84 doses and the periodic limit give day-7 ratios 0.973–0.976. Parameter and history uncertainty differs from interindividual variation.

## Conclusion

With the representative parameters of the public model, daily AUC after restarting 200 mg QD relative to uninterrupted dosing was 0.625, 0.564, and 0.503 on day 1 after omitting 2, 3, and 7 doses, and 0.989, 0.986, and 0.974 on day 7 (Table 4). Among 2,048 virtual individuals, the median first daily interval with an AUC ratio of at least 90% was day 3 or 4, and at least 95% was day 4 or 5. After seven omissions, the upper 5th–95th percentile bound for reaching 95% was day 11 in the primary scenario and day 13 under the alternative cross-term readings (Tables 5 and 6). The difference from uninterrupted dosing shrank in the same direction for AUC, peak, and predose concentration.

These are model-internal exposure ratios, not observed PK after restart. The unresolved disagreement between label and model accumulation (Table 3) means that a recovery time in days has not been validated. The 90% and 95% benchmarks are descriptive and do not imply that day 4 or day 5 is sufficient for efficacy or safety. The analysis covers plasma PK only and excludes ER degradation and recovery. A nonsignificant exposure–response association in the published analysis ([2](#ref-2)) does not establish that interruption has no effect. Recovery of plasma exposure does not determine when drug action recovers or what restart dose to use. Optimal sampling times and required sample size were not estimated.

## Data and code availability

The [code, parameters, histories, eight CSV summaries, and three figures](shared/vepdegestrant-restart/restart-analysis.zip) exclude source PDFs, figures, and individual records. Ten implementation tests cover gut input, single-dose/finite-history/periodic solutions, omitted-dose differences, daily AUC, and time grids. Passing them is distinct from clinical validation. Sources were checked on October 24, 2026.

## References

1. <span id="ref-1"></span>US Food and Drug Administration. Veppanu (vepdegestrant): US prescribing information. 2026. [Label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/219835Orig1s000lbl.pdf).

2. <span id="ref-2"></span>Yang DZ, Masters JC, Wang H, Tran L, Zhang Y, Lee KC, et al. Population Pharmacokinetics and Exposure–Response Analyses of Vepdegestrant, a First‐in‐Class PROteolysis‐TArgeting Chimera Estrogen Receptor Degrader. J Clin Pharmacol. 2026;66(8):e70252. [doi:10.1002/jcph.70252](https://doi.org/10.1002/jcph.70252).

3. <span id="ref-3"></span>US Food and Drug Administration. Vepdegestrant, NDA 219835: multidisciplinary review. 2026. Table 75, PDF p. 234. [Review](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/219835Orig1s000MultidisciplineR.pdf).
