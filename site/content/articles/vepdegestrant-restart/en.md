Vepdegestrant is an oral proteolysis-targeting chimera (PROTAC) that degrades the estrogen receptor (ER), with a US-approved dose of 200 mg once daily (QD) with food ([1](#ref-1)). After an interruption and restart at the same dose, how does plasma exposure approach continued dosing?

I reused a published human population pharmacokinetic (PopPK) model to calculate exposure after omitting 2, 3, or 7 scheduled doses. With representative parameters and 28 preceding doses, first-day ratios of the area under the concentration–time curve (AUC) versus uninterrupted dosing were approximately 0.63, 0.56, and 0.50. Rapid early convergence was followed by a slower residual difference. However, model accumulation did not agree with label summaries. These are conditional calculations for considering restart PK measurements, not clinically validated recovery times.

I checked the text of the original paper as posted in PMC (not its supplementary material), the FDA label, Table 75 and related pages of the FDA review, and the abstracts of phase 1 studies of the same drug. I did not check the paper's supplementary tables (S1–S4) or the original control files.

## Question and time definitions

The question is how daily AUC, peak, and predose concentration approach an uninterrupted trajectory after restarting 200 mg QD. The intended use is planning PK measurements with a public model, not selecting a patient's restart day or dose or determining efficacy/safety recovery. Label-directed toxicity modifications are not recreated.

For reactions other than QTc prolongation, the label advises considering interruption for grade 2; after a first grade 3 reaction, treatment is interrupted and resumed after recovery at the same or a reduced dose; after a first grade 4 reaction, resumption is at the reduced dose. Recurrences have separate provisions including discontinuation, and QTc prolongation has its own rules. After a missed or vomited dose, the next dose is taken at the regular time. Interruption for an adverse reaction occurred in 14% of patients ([1](#ref-1)). In the sections I read, the label does not describe concentrations after restart.

Assume 28 doses every 24 hours before interruption. The first omitted dose is at time 0 and the last administered dose at −24 hours. Omitting two doses skips times 0 and 24, with restart at 48 hours.

**Table 1.** Omitted doses and elapsed time from last dose to restart.

| Omitted scheduled doses | Last dose to restart | Restart dose |
| --- | --- | --- |
| 2 | 72 h | 200 mg QD |
| 3 | 96 h | 200 mg QD |
| 7 | 192 h | 200 mg QD |

Subsequent figures reset zero to restart. Day 1 denotes AUC over 0–24 hours, day 3 over 48–72, and day 7 over 144–168. The comparator is the same hypothetical individual continuing through the same calendar times. Food, concomitant treatment, and coefficients remain unchanged; physiological changes causing interruption are absent. The label reports that administration with a high-fat meal increased AUC 2.9-fold and Cmax 3.2-fold ([1](#ref-1)), so a change in food conditions at restart would break this assumption.

## The public human model

The 2026 paper fits a linear-elimination two-compartment model to 3,625 PK samples from 452 participants pooled from phase 1/2 study ARV-471-mBC-101 (total daily doses 30–500 mg) and the 200-mg arm of VERITAC-2. Absorption is zero-order input into the gut followed by first-order absorption. Samples below the limit of quantification (4.1%) were excluded. No covariate was retained in the stepwise covariate search (SCM), so the base model became the final model. The paper reports a slight underprediction of the absorption profile on Day 1 and high eta-shrinkage for Vc/F (the degree to which individual estimates shrink toward zero), about 39% ([2](#ref-2)). Individual records are unavailable. I use the precision of [FDA Table 75, PDF p. 234](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/219835Orig1s000MultidisciplineR.pdf#page=234), printed p. 233 ([3](#ref-3)), corresponding to rounded coefficients in [original Table 1](https://doi.org/10.1002/jcph.70252).

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

The label values are means (coefficients of variation) in patients at steady state on 200 mg QD ([1](#ref-1)). The FDA review gives the mean observed accumulation ratio as 1.42 (43%) for AUC and 1.27 (43%) for Cmax ([3](#ref-3), PDF p. 92), and states that the 19-hour effective half-life after multiple dosing describes actual accumulation in the phase 3 study better than the 56-hour terminal half-life calculated from a mass-balance study ([3](#ref-3), PDF p. 86). The paper reports the terminal half-life of about 56 hours citing a single-dose relative bioavailability study in 52 healthy adults ([2](#ref-2), [4](#ref-4)). Sampling in that study ran to 168 hours, too short to observe directly the model's slowest phase (about 1,016 hours).

Abstracts of phase 1 studies of 200 mg QD report geometric means after the first dose and after repeated dosing. In 6 Japanese patients, AUC was 10,400 and 18,310 ng·h/mL and Cmax 630.9 and 1,056 ng/mL. In 9 Chinese patients (repeated dosing on day 15), AUC was 9,575 and 18,340 ng·h/mL and Cmax 633.2 and 1,035 ng/mL ([5](#ref-5), [6](#ref-6)). The repeated-to-first-dose ratios are 1.76 and 1.92 for AUC and 1.67 and 1.63 for Cmax. By contrast, the representative-parameter model gives a first-dose 24-hour AUC of 6,599 ng·h/mL and Cmax of 366 ng/mL, which are 0.63–0.69 and 0.58 times the observed geometric means. Periodic AUC was 0.93 times and Cmax 0.81–0.83 times the observed repeated-dose values. The model's accumulation ratios (AUC 2.58, Cmax 2.35) are large mainly because first-dose exposure is low. I checked only the abstracts, so food conditions and sampling details are unknown, and these are geometric means from small studies of 6 and 9 patients (model values: `outputs/results.json`; ratios are my calculation). The [comparison script](shared/vepdegestrant-restart/extra-exposure-checks.py) reproduces these ratios and inverse accumulation values. Run `python extra-exposure-checks.py` from the extracted original ZIP folder.

Accumulation ratios thus differ among sources: about 1.4 on the label (1.42 observed in the FDA review), 1.76–1.92 from the phase 1 geometric-mean ratios, and 2.58 in the model. Within the sources examined, nothing resolves the discrepancy. There are at least three candidates. First, the representative parameters (an individual-free central value) and the label means or phase 1 geometric means are different quantities. If clearance is lognormal with variance 0.192, the population arithmetic mean AUC is about exp(0.096) = 1.10 times the central-value AUC; if the label values are arithmetic means, the closeness to the central value may be a coincidence. Second, accumulation ratios are defined differently (mean of individual ratios, ratio of means, ratio of geometric means). Third, the model's slow phase depends on Vp/F, whose relative standard error is large at 45.6% ([2](#ref-2)), and on a lack of observations beyond 168 hours. Which one explains the discrepancy has not been determined.

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

Missing carryover reduces first-day exposure despite restarting the same 200 mg. Differences shrink by days 3 and 7, but after seven omissions day-28 AUC remains approximately 0.986. Near-convergence over a short period differs from equality of every model state. The shortfall of about 1.4% that remains through day 28 after seven omissions arises from the model's slow phase. That phase is not directly observed, as described above, and the FDA considers the 19-hour effective half-life a better description of actual accumulation ([3](#ref-3)). I do not read this residual as an observed persistent exposure reduction. Predose concentration is evaluated at the next scheduled dose, not the strict minimum during the interval. Similar plasma exposure does not establish similar tumor concentration, ER degradation, or efficacy.

## Individual variation and a definition of return

Published log variances for CL/F and Vc/F are 0.192 and 0.251. The cross term 0.089 is accompanied by both omega-squared and correlation terminology, so its definition was not asserted without the control file. Table 1 of the paper also lists a CV of 30% on this row, which equals the square root of 0.089 (0.298); the diagonal entries 0.192 and 0.251 give 44% and 50% by the same transformation. Within that table, 0.089 was therefore probably treated on the same variance or covariance scale. This is circumstantial evidence from consistency of reporting, not confirmation of the definition. The eta-shrinkage for Vc/F is about 39%, above the 20–30% level at which diagnostics based on individual estimates become unreliable ([7](#ref-7)). The bootstrap intervals are wide: 0.16–0.50 for the variance 0.251 and 0.03–0.23 for the cross term ([2](#ref-2)). The primary scenario treats it as covariance, implying correlation approximately 0.405. Alternatives use correlation 0.089 or zero. This does not reconstruct the original full Omega. Other random effects are absent and residual errors are not added to latent exposure.

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

## Discussion

With dosing history and other conditions fixed in this linear model, the daily AUC deficit can be calculated from cumulative single-dose AUC, J(t). For a linear model with fixed parameters and identical dosing conditions, the reciprocal of steady-state interval AUC divided by first-dose interval AUC equals the fraction of total single-dose AUC realized within 24 hours. That fraction is 1/2.58 = 0.39 in the model, about 0.71 from the label's approximately 1.4-fold accumulation, and 0.52–0.57 from the phase 1 geometric-mean ratios (1.76–1.92). These conversions depend on comparable populations, summaries, and attainment of steady state. The cross-source discrepancy does not establish a different J(t) for the same individual.

A larger fraction of single-dose AUC within 24 hours leaves a smaller total fraction thereafter. It does not determine how that remaining exposure is distributed across days, so it does not ensure earlier convergence on every restart day, even with identical AUC∞ (dose/CL). The day-1 ratio includes the exposure produced by the restarted dose in its first 24 hours, and the cross-source first-dose differences raise a validation concern without establishing the direction of bias in this ratio. The values in Tables 4 and 5 are therefore central estimates not checked against observations and, within the external information used here, subject to unvalidated uncertainty in recovery speed. The size of the bias cannot be estimated from these sources because food conditions, populations, and the correspondence between geometric means and central values are not aligned.

The paper's exposure–response analysis used average concentration in cycle 1 (Cavg, cycle1), derived from recorded dosing history, in 132 patients with ESR1 mutations in the 200-mg arm of VERITAC-2. The hazard ratio for log Cavg was 0.95 (95% confidence interval 0.44–2.04, p = 0.887) ([2](#ref-2)). The FDA also states that, because the efficacy analysis rests on a single dose level, exposure–response has not been fully characterized ([3](#ref-3), PDF p. 254). The wide interval excludes neither no relationship nor a large one. A 28-day average also does not distinguish a transient shortfall that resolves in days from persistently low exposure. In the present calculation, omitting 2–7 doses reduces day-1 AUC to 0.50–0.63 of uninterrupted dosing. The effect of a transient shortfall of this size cannot be read from the paper's “no significant relationship.”

I did not find a study comparing observed PK after restart with predictions in the top 30 titles from a Europe PMC search combining vepdegestrant with terms such as pharmacokinetics, simulation, and interruption. Given the limits of the search, this does not prove that none exists. The paper's purpose was to evaluate covariates and exposure–response, not to predict the course after interruption. This article does not dispute the paper's conclusions; it shows what remains unvalidated when published coefficients are used for a different question.

## Conclusion

With the representative parameters of the public model, daily AUC after restarting 200 mg QD relative to uninterrupted dosing was 0.625, 0.564, and 0.503 on day 1 after omitting 2, 3, and 7 doses, and 0.989, 0.986, and 0.974 on day 7 (Table 4). Among 2,048 virtual individuals, the median first daily interval with an AUC ratio of at least 90% was day 3 or 4, and at least 95% was day 4 or 5. After seven omissions, the upper 5th–95th percentile bound for reaching 95% was day 11 in the primary scenario and day 13 under the alternative cross-term readings (Tables 5 and 6). The difference from uninterrupted dosing shrank in the same direction for AUC, peak, and predose concentration. The phase 1 geometric means exceed the model's first-dose exposures, but the direction and size of bias in restart predictions remain undetermined (Discussion).

These are model-internal exposure ratios, not observed PK after restart. The unresolved disagreement between label and model accumulation (Table 3) means that a recovery time in days has not been validated. The 90% and 95% benchmarks are descriptive and do not imply that day 4 or day 5 is sufficient for efficacy or safety. The analysis covers plasma PK only and excludes ER degradation and recovery. A nonsignificant exposure–response association in the published analysis ([2](#ref-2)) does not establish that interruption has no effect. Recovery of plasma exposure does not determine when drug action recovers or what restart dose to use. Optimal sampling times and required sample size were not estimated.

## Data and code availability

The [code, parameters, histories, eight CSV summaries, and three figures](shared/vepdegestrant-restart/restart-analysis.zip) exclude source PDFs, figures, and individual records. Ten implementation tests cover gut input, single-dose/finite-history/periodic solutions, omitted-dose differences, daily AUC, and time grids. Passing them is distinct from clinical validation. Sources were checked on October 24, 2026. The paper's text (PMC), the label, the relevant pages of the review, and the phase 1 abstracts were rechecked on October 29, 2026.

## References

1. <span id="ref-1"></span>US Food and Drug Administration. Veppanu (vepdegestrant): US prescribing information. 2026. [Label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/219835Orig1s000lbl.pdf).

2. <span id="ref-2"></span>Yang DZ, Masters JC, Wang H, Tran L, Zhang Y, Lee KC, et al. Population Pharmacokinetics and Exposure–Response Analyses of Vepdegestrant, a First‐in‐Class PROteolysis‐TArgeting Chimera Estrogen Receptor Degrader. J Clin Pharmacol. 2026;66(8):e70252. [doi:10.1002/jcph.70252](https://doi.org/10.1002/jcph.70252).

3. <span id="ref-3"></span>US Food and Drug Administration. Vepdegestrant, NDA 219835: multidisciplinary review. 2026. Table 75, PDF p. 234. [Review](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/219835Orig1s000MultidisciplineR.pdf).

4. <span id="ref-4"></span>Yang DZ, Matschke KT, Winton JA, Lee KC, Zhang Y, Tan W. A relative bioavailability study of vepdegestrant tablets in healthy adult participants. Eur J Drug Metab Pharmacokinet. 2026;51(5):613–621. [doi:10.1007/s13318-026-01018-w](https://doi.org/10.1007/s13318-026-01018-w).

5. <span id="ref-5"></span>Iwata H, Naito Y, Hattori M, Yoshimura A, Yonemori K, Aizawa M, et al. Safety and pharmacokinetics of vepdegestrant in Japanese patients with ER+ advanced breast cancer: a phase 1 study. Int J Clin Oncol. 2025;30(1):72–82. [doi:10.1007/s10147-024-02648-3](https://doi.org/10.1007/s10147-024-02648-3).

6. <span id="ref-6"></span>Xu B, Yang J, Zhang P, Wang W, Zhang L, Zhao X, et al. A phase 1, open-label study evaluating the pharmacokinetics, safety, and tolerability of vepdegestrant in Chinese patients with ER+/HER2- advanced breast cancer. Cancer Chemother Pharmacol. 2026;96(1):90. [doi:10.1007/s00280-026-04921-w](https://doi.org/10.1007/s00280-026-04921-w).

7. <span id="ref-7"></span>Savic RM, Karlsson MO. Importance of shrinkage in empirical Bayes estimates for diagnostics: problems and solutions. AAPS J. 2009;11(3):558–569. [doi:10.1208/s12248-009-9133-0](https://doi.org/10.1208/s12248-009-9133-0).
