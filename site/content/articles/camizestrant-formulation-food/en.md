Even at the same dose, formulation and food can change how much drug reaches circulation and how quickly. I re-examined public crossover data on camizestrant (1) to separate formulation and food effects.

At 75 mg in this study, adjusted geometric-mean ratios were 0.962–0.995 between formulations and 1.062–1.098 for fed versus fasting (1). These population comparisons are consistent with the formulation change and administration without additional food restrictions. Individual exposure changes and absorption rates, however, are not identified by the published summaries alone. Small models make that distinction explicit.

## Comparing single-dose total exposure and peak concentration {#auc}

The question is how formulation and food affect total and peak exposure at 75 mg, and whether these comparisons support individual predictions. The intended use is planning pharmacokinetic comparisons using public information, not food-based dose reduction, individualized prediction in breast cancer or efficacy and safety assessment.

Sykes et al. reported a randomized crossover study in 32 healthy postmenopausal women ([1](#ref-1)). This was a single-dose study, not repeated dosing with anticancer combinations. Population and comparison details appear in [Tables 1–4 of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12820339/) ([1](#ref-1), Tables 1–4).

The focus is the 75 mg phase 1 tablet, solution and phase 3 prototype tablet, and fasting versus high-fat-fed administration of the prototype. The 300 mg comparisons remain supplementary comparisons at a different dose. The prototype is not interchangeable with every future formulation or product change.

Area under the concentration–time curve (AUC) here is extrapolated to infinity, distinct from AUC0–t to the last sample. Peak concentration is Cmax. The original log-transformed mixed model included regimen, period and sequence as fixed effects and participant nested within sequence as a random effect ([1](#ref-1), Section 2.8). Individual data were not obtained and that model was not refitted.

Table 1. Adjusted geometric-mean ratios and 90% confidence intervals (CI) from the original paper. AUC is extrapolated to infinity; Cmax is peak concentration.

| Comparison | Adjusted AUC ratio (90% CI) | Adjusted Cmax ratio (90% CI) |
| --- | --- | --- |
| 75 mg: phase 3 prototype / phase 1 tablet | 0.974 (0.926–1.025) | 0.987 (0.874–1.115) |
| 75 mg: phase 3 prototype / solution | 0.995 (0.946–1.046) | 0.962 (0.853–1.087) |
| 300 mg: phase 3 prototype / phase 1 tablet | 1.004 (0.962–1.049) | 0.966 (0.869–1.075) |
| 75 mg: fed / fasting | 1.098 (1.044–1.155) | 1.062 (0.943–1.197) |
| 300 mg: fed / fasting | 1.023 (0.980–1.068) | 1.159 (1.043–1.287) |

Ratios were extracted from [Tables 3–4 of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12820339/) ([1](#ref-1), Tables 3–4). The overall 32 participants are not the sample size of every contrast. At 75 mg fed, Cmax had 16 participants and AUC 15; other principal 75 mg comparisons had 15. Fasting rows repeated between the two source tables were not counted twice.

![Adjusted ratios and 90% confidence intervals by formulation and food condition](shared/camizestrant-formulation-food/figures/adjusted-contrasts.png)

Figure 1. Points are the original adjusted geometric-mean ratios; lines are their 90% CI. The vertical line denotes ratio 1. These are not individual prediction intervals.

At 75 mg, the fed/fasting ratio was 1.098 (90% CI 1.044–1.155) for AUC and 1.062 (0.943–1.197) for Cmax. The AUC interval excludes 1 and the Cmax interval includes 1. Magnitude and precision need separate interpretation. The 300 mg Cmax upper bound of 1.287 should not be transferred to 75 mg, nor should clinical importance be inferred from a single boundary.

The current US prescribing information (ETCAMAH, generic name camizestrant) specifies 75 mg once daily with or without food ([2](#ref-2), Section 2.3). These calculations examine evidence interpretation rather than proposing another administration method.

## Ratios of geometric means do not reproduce the crossover contrast {#_1}

I compared simple ratios of published group geometric means with the adjusted ratios.

Table 2. Simple ratios of group summaries and original adjusted ratios.

| Comparison | Metric | Simple ratio of group geometric means | Adjusted ratio |
| --- | --- | ---: | ---: |
| 75 mg: phase 3 prototype / phase 1 tablet | AUC | 0.948 | 0.974 |
| 75 mg: phase 3 prototype / phase 1 tablet | Cmax | 0.950 | 0.987 |
| 75 mg: phase 3 prototype / solution | AUC | 0.924 | 0.995 |
| 75 mg: phase 3 prototype / solution | Cmax | 0.892 | 0.962 |
| 75 mg: fed / fasting | AUC | 1.099 | 1.098 |
| 75 mg: fed / fasting | Cmax | 1.101 | 1.062 |

For example, the phase 3 prototype / phase 1 tablet AUC ratio from 636/671 differs from the adjusted 0.974. This does not immediately indicate an error: group summaries and estimates accounting for period, sequence and comparable participants are different quantities. Their contributions to the discrepancy cannot be partitioned from aggregate data.

Subsequent population contrasts use adjusted ratios. A model built from simple ratios is not a reproduction of the original crossover analysis.

## Stopping before interpreting absorption rates {#_2}

I first considered a one-compartment model with first-order absorption and elimination. With elimination rate constant k and absorption rate constant ka, concentration after a single dose is

\[
C(t)=AUC\,\frac{k k_a}{k_a-k}\left(e^{-kt}-e^{-k_at}\right),
\qquad k=\frac{\log 2}{t_{1/2}}.
\]

Its peak time is

\[
t_{\max}=\frac{\log(k_a/k)}{k_a-k}.
\]

I fixed k from the reported half-life, set the scale using AUC and solved numerically for ka matching the time to peak concentration (Tmax), using the non-absorption-limited branch ka > k. Cmax was reserved for checking rather than fitting.

For the fasting 75 mg prototype, AUC 636 ng·h/mL, half-life 23.3 h and median Tmax 4 h gave ka = 0.875 /h and calculated Cmax = 16.8 ng/mL, 45.1% below the reported 30.6 ng/mL.

Fine adjustment of ka cannot resolve this. Even if all drug entered the central compartment instantaneously, the same model satisfies

\[
C_{\max}\leq k\,AUC
\]

The upper bound under these conditions is only 18.9 ng/mL.

![Published summaries and a one-compartment adequacy check](shared/camizestrant-formulation-food/figures/absorption-gate.png)

Figure 2. Left: published and calculated Cmax under four conditions. Black crosses mark conditional upper bounds with k fixed from reported half-life. Right: the fasting prototype example. The cross combines median Tmax and geometric-mean Cmax; it is not an observed concentration point from one participant. The curve is not fitted to an observed time series.

I therefore did not interpret formulation differences in absorption rates from this model or predict repeated-dose trajectories. Adding distribution compartments might match the summaries, but a few aggregate indicators do not uniquely identify a more complex model.

Half-life, AUC and Cmax are geometric means, whereas Tmax is a median; they do not describe the same person or representative curve. The mismatch alone does not prove that the drug violates one-compartment kinetics. It means that the published summaries cannot validate a concentration curve for this intended use.

## Population ratios and individual ratios {#_3}

Conditional comparisons of exposure endpoints remain possible without a time curve. AUC and Cmax are modeled separately as lognormal variables:

\[
\log Y_0=\mu+\sigma_0 Z_1,
\]
\[
\log Y_1=\mu+\theta+
\sigma_1\{\rho Z_1+\sqrt{1-\rho^2}Z_2\}.
\]

Y0 denotes fasting and Y1 fed exposure (AUC or Cmax). Theta is the logarithm of the adjusted ratio. Sigma is converted from the reported geometric coefficient of variation (CV) as sqrt(log(1 + CV²)). Rho is the within-person correlation between log exposures under the two conditions; it cannot be recovered exactly from these summaries. I first set it to 0, 0.5 and 0.9 to isolate its influence. These scenarios use marginal CV and the geometric-mean-ratio (GMR) point estimate; they are not simultaneously calibrated to the reported GMR CI and are not treated as equally plausible reconstructions of the trial.

Fed mean levels are shifted from the fasting geometric mean using the adjusted ratio. The resulting fed geometric mean therefore need not reproduce the unadjusted tabulated mean. These synthetic populations do not reconstruct the original participants.

The variance of the within-person log ratio is

\[
\operatorname{Var}\{\log(Y_1/Y_0)\}
=\sigma_0^2+\sigma_1^2-2\rho\sigma_0\sigma_1.
\]

Identical mean ratios and marginal CVs can yield different individual-ratio distributions when rho changes. I generated 2,048 pairs and compared them with this theoretical distribution. No correlation linking AUC and Cmax was specified, so I did not calculate the fraction simultaneously satisfying criteria for both endpoints.

Table 3. Assumed between-condition correlation and individual-ratio distributions. P5 and P95 denote the 5th and 95th percentiles.

| Metric | Assumed rho | Theoretical individual-ratio P5–P95 | Calculated P5–P95 in 2,048 pairs |
| --- | ---: | --- | --- |
| AUC | 0 | 0.50–2.43 | 0.48–2.32 |
| AUC | 0.5 | 0.63–1.92 | 0.62–1.87 |
| AUC | 0.9 | 0.85–1.41 | 0.85–1.41 |
| Cmax | 0 | 0.42–2.71 | 0.40–2.58 |
| Cmax | 0.5 | 0.55–2.06 | 0.54–1.98 |
| Cmax | 0.9 | 0.78–1.44 | 0.78–1.42 |

![Exposure ratios in hypothetical pairs with different between-condition correlations](shared/camizestrant-formulation-food/figures/pairing-sensitivity.png)

Figure 3. Conditional calculations using the same random pairs. Correlations 0, 0.5 and 0.9 were not fitted to the original CI. Green denotes theoretical values from the simple paired-comparison approximation below, not a generated population. Points and lines show synthetic medians and P5–P95; short horizontal marks show formula-based P5 and P95. These are neither patient prediction intervals nor GMR confidence intervals. Finite samples need not match theoretical quantiles exactly.

The GMR CI is not wholly uninformative about correlation. Under a simple fully paired comparison, the standard error (SE) of the mean log ratio constrains

\[
\operatorname{Var}\{\log(Y_1/Y_0)\}\approx n\,SE^2
\]

Assuming 15 complete pairs (n = 15), I compared a normal approximation dividing the log-CI width by 2 × 1.645 with an approximation using a t quantile with 14 degrees of freedom. The latter is a sensitivity assumption, not a verified degree of freedom from the original mixed model.

Table 4. Sensitivity of CI conversion assuming a complete paired comparison.

| Metric | CI conversion assumption | Approximate rho combined with marginal CVs | Theoretical individual-ratio P5–P95 |
| --- | --- | ---: | --- |
| AUC | normal | 0.939 | 0.90–1.34 |
| AUC | t14 | 0.947 | 0.91–1.32 |
| Cmax | normal | 0.760 | 0.67–1.69 |
| Cmax | t14 | 0.791 | 0.69–1.63 |

The narrow published CI corresponds more closely to these high-correlation approximations than to the broad individual distribution with rho = 0. However, the original mixed model adjusts for period and sequence, with missingness and sample size differing by metric. This does not recover the actual correlation or validate patient prediction intervals. It also assumes marginal CVs and adjusted CIs arise from a compatible variance model.

A CI describes population-comparison precision, not each person's variation. Through assumptions about study design, it can nevertheless constrain within-person differences. These two roles must remain separate.

## Cross-sectional food-condition variance is not an individual change {#_4}

Cross-sectional log variance in a mixture of fed and fasting conditions separates into within-condition and between-condition components. If the fed fraction is p,

\[
\operatorname{Var}(\log Y)=
(1-p)\sigma_0^2+p\sigma_1^2+p(1-p)\theta^2.
\]

With equal fed and fasting proportions, the within-condition AUC variance was 0.1162 and the added between-condition term 0.0022. Under this assumption, standardizing food condition would leave most of the log variance. This is a population-mixture calculation, not a trajectory for one patient changing food conditions daily.

Marginal CVs do not contain covariance between an individual's paired values. This mixture decomposition therefore cannot identify individual exposure changes after switching food conditions.

## Limitations {#_5}

The conclusions depend on published summaries from single doses in healthy adults. Effects of concomitant medicines, disease and repeated dosing were not estimated. Without individual data, the original mixed model was not refitted and within-person correlation cannot be recovered. I did not fit observed concentration–time series or re-estimate population pharmacokinetics (PopPK). Sources were checked on October 24, 2026.

## Conclusion

For single 75 mg doses, adjusted AUC and Cmax ratios were 0.962–0.995 between formulations and 1.062–1.098 for fed versus fasting, with 90% CI in Table 1. Within this population comparison, the public information is consistent with formulation change and administration without additional food restrictions. How many-fold an individual's exposure changes and formulation differences in absorption rate could not be determined from the published summaries and the one-compartment model. Individual changes would need matched individual data or additional assumptions about between-condition correlation.

## Data and code availability

The package contains inputs, seven types of summary CSV, three figures and code, excluding original individual data and source figures. Nine checks covered independent ordinary differential equation (ODE) calculations, AUC integration, peak bounds, CI conversion, log-distribution formulas, mixture variance and random-number reproducibility. These check implementation, not clinical prediction validity. Run `python analysis/run_analysis.py`; the random seed is 20261024.

[Analysis code, inputs, summary tables and reproduction instructions](shared/camizestrant-formulation-food/bridging-analysis.zip)

## References {#article-references}

1. <span id="ref-1"></span> Sykes A, Engman H, Taylor N, Brier T, Maudsley R, Kirova B, et al. [Open-label study assessing relative and absolute bioavailability of oral camizestrant formulations and food effects in healthy postmenopausal women](https://doi.org/10.1111/cts.70475). Clin Transl Sci. 2026;19(2):e70475. Tables 3–4 and Section 2.8 were used.
2. <span id="ref-2"></span> US Food and Drug Administration. ETCAMAH (camizestrant) tablets, for oral use: prescribing information [Internet]. Silver Spring (MD): FDA; revised 2026 Sep [cited 2026 Oct 24]. Sections 2.3 and 12.3. Available from: [https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/220359Orig1s000lbl.pdf](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/220359Orig1s000lbl.pdf).
