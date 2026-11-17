## Abstract {#article-abstract}

Exposure–response models for a dose decision often start from many candidate covariates. Shrinkage priors such as the horseshoe ([1](#ref-1)) keep the covariate list short, but a short list is not the goal; the dose is. This article asks whether the covariate strategy changes a dose decision, in simulated randomized dose-ranging trials with 20 candidate covariates, three dose levels and a toxicity limit. Three covariates affected response directly and two affected toxicity; the remaining covariates, including two that changed clearance, had no direct effect on either endpoint. Across 150 trials per sample size, backward stepwise selection kept on average 3.6 (response) and 4.2 (toxicity) inactive covariates at 120 patients, against 0.11 and 0.07 for a horseshoe-prior probit model, but the latter detected only 34% and 13% of the true effects (stepwise 86% and 72%). The probability of choosing the best feasible dose, the one with the highest response among doses with toxicity at most 25%, was 74% (full model), 77% (stepwise) and 77% (horseshoe) at 120 patients, and 88%, 87% and 89% at 300; the differences were within sampling error (paired difference horseshoe minus full model +2.7 percentage points, SE 3.8, at 120 patients). The horseshoe model estimated the exposure effect on toxicity best (true 0.90; at 120 patients mean estimates of 1.51 for the full model, 1.28 for stepwise and 0.98 for horseshoe, medians 1.35, 1.10 and 0.94), and its posterior probability that dose 2 was the best feasible dose exceeded 0.8 in 8.7% of trials at 120 patients and 46% at 300. With a toxicity margin of 5.7 percentage points, shrinkage cleaned the covariate list and gave the estimate of the exposure effect closest to the truth, but it did not measurably improve the population dose decision. With a margin of 2.0 points, in separate simulations that also included a lasso and a Firth-type penalty, the horseshoe model selected the best feasible dose more often than the full model and stepwise selection (+12.0 and +13.3 percentage points at 120 patients; SE 4.2 and 3.9).

## Introduction {#article-introduction}

A dose-selection analysis rarely starts with the covariates that matter. It starts with a long list of baseline factors, and the analyst must decide which ones belong in a response model and a toxicity model before the dose is compared. Stepwise selection keeps whatever improves a criterion in the data at hand, so with many candidates it keeps some that do nothing. The horseshoe prior shrinks inactive effects strongly toward zero while leaving large effects almost untouched, and it comes with a posterior distribution rather than a yes–no list ([1](#ref-1)). Efficient Gibbs samplers exist for it ([2](#ref-2)).

That the horseshoe prior gives a cleaner list is expected. The question here is whether it changes what the analysis is for: **when response and toxicity models both carry many candidate covariates, does the choice of covariate strategy change which dose is selected, and how certain the analysis is about it?** The context of use is a population-level decision, choosing, among three candidate doses, the one with the highest response rate whose grade 3 or worse toxicity rate is at most 25%. A wrong choice is a dose that is either too low, losing response, or too high, exceeding the toxicity limit. The study uses simulated trials, so the true dose-specific rates are known and the decision can be scored. The conclusions are limited to the design described below.

## Methods {#article-methods}

### Simulated trials {#simulated-trials}

Each trial randomized 120 or 300 patients with equal probability to relative doses 1, 2 and 3. Each patient had 20 candidate baseline covariates x₁ to x₂₀, standard normal with correlation 0.25 between every pair. The log clearance was 0.30 x₁ − 0.20 x₂ plus normal variability (SD 0.30), and the log exposure was ln(dose) minus the log clearance. Response and grade 3 or worse toxicity followed probit models in the log exposure and the covariates:

response: P = Φ(a_r + 0.45 · ln exposure + 0.50 x₃ − 0.40 x₄ + 0.30 x₅);
toxicity: P = Φ(a_s + 0.90 · ln exposure + 0.40 x₆ − 0.30 x₇),

where Φ is the standard normal distribution function. All other covariates, including x₁ and x₂, had no direct effect on either endpoint. The intercepts were set so that the population response and toxicity rates at relative dose 1 were 25% and 8%. The true dose-specific rates were computed from 400,000 simulated patients (Table 1). Relative dose 2 is the best feasible dose: it has the highest response among doses with toxicity at most 25%, with a toxicity margin of 5.7 percentage points to the limit; relative dose 3 exceeds the limit.

**Table 1. True population rates by relative dose.**

| Endpoint | Dose 1 | Dose 2 | Dose 3 |
| --- | --- | --- | --- |
| Response | 25.0% | 33.9% | 39.6% |
| Grade ≥ 3 toxicity | 8.0% | 19.3% | 29.1% |

### Covariate strategies {#covariate-strategies}

Each endpoint was analyzed separately with a probit model containing the log exposure (the exposure of each patient was taken as known) and the 20 covariates, in three ways. (a) The full model fitted by maximum likelihood. (b) Backward stepwise selection by Akaike's information criterion starting from the full model, with the log exposure always kept (`stepAIC`, MASS 7.3-65) ([3](#ref-3)). (c) A Bayesian probit model with a horseshoe prior on the 20 covariate effects, a normal prior with SD 2 on the exposure effect and SD 10 on the intercept, fitted by Gibbs sampling with data augmentation for the probit link ([4](#ref-4)) and the inverse-gamma scale mixture of the horseshoe ([2](#ref-2)). I wrote the sampler in base R for this study. Each fit used 1,200 iterations, discarding the first 400. The three methods analyzed the same data in each trial.

For every method, the predicted response and toxicity rate at each dose were averaged over 3,000 new simulated patients (their exposures at each dose computed from their clearances). The selected dose was the one with the highest predicted response among those with predicted toxicity at most 25%; if none qualified, the lowest dose. For the horseshoe model, 200 posterior draws gave a posterior probability that dose 2 was the best feasible dose.

### Metrics {#metrics}

The dose decision was scored as the share of trials selecting dose 2. Prediction accuracy was the mean absolute error of the six predicted rates (three doses, two endpoints, separately). For covariate selection, a covariate was declared important if p < 0.05 (full model), if it remained in the final model (stepwise), or if its 90% credible interval excluded 0 (horseshoe); the counts were the number of inactive covariates declared important (17 for response, 18 for toxicity) and the share of true covariates declared important. These criteria are different thresholds, not matched operating points. Each sample size had 150 trials (seed 20261115), so the standard error of a share near 0.8 is about 3.5 percentage points. Paired differences between methods use the same trials. SE is the standard error and SD the standard deviation.

### Further comparisons {#further-comparisons}

Two further simulations of 150 trials per sample size, with new data (seeds 20261118 and 20261119), added a lasso (glmnet 5.2, logit link, exposure left unpenalized, the penalty chosen by five-fold cross-validation at the largest value within one standard error of the minimum) ([5](#ref-5)) and a Jeffreys-penalized probit (a Firth-type penalty, maximized with BFGS) ([6](#ref-6)) to the three original methods. They used two toxicity configurations: the original one (toxicity 8.0%, 19.3% and 29.1% at doses 1 to 3; margin 5.7 points) and a narrower one (toxicity 10.1%, 23.0% and 33.6%, response 25.1%, 34.0% and 39.7%; margin 2.0 points). Dose 2 is the best feasible dose in both. The lasso predicts with its logit model, so its exposure coefficients are not on the probit scale and are not compared. One Jeffreys-penalized fit that returned no rates (120 patients, original configuration) was excluded from that method's results.

### Checking the sampler {#sampler-checks}

The Gibbs sampler was checked in two ways. In one dataset of 20,000 patients, where the prior is negligible, its posterior means differed from the maximum likelihood probit estimates by about 0.013 at most across all 22 coefficients. In 20 datasets of 120 patients fitted with two chains, the largest potential scale reduction factor was 1.02 for the exposure effect, 1.06 for the covariate x₃ and 1.02 for the inactive covariate x₁₀; for the global scale governing covariate shrinkage it was 1.11. The scale estimate itself was not a primary metric. The same checks for the toxicity endpoint gave a difference of 0.017 at 20,000 patients and largest factors of 1.02 (exposure effect), 1.07 (covariate x₆), 1.02 (x₁₀) and 1.26 (global scale). R 4.5.3 was used ([7](#ref-7)). The full run raised 28 warnings. In a 25-trial rerun, every warning was the message that fitted probabilities were numerically 0 or 1, from the full-model fit, which indicates separation in small samples; those fits are included in the results. The cited methods papers were used for the methods they introduce; their full texts were not re-read for this article.

## Results {#article-results}

### Covariate selection {#covariate-selection}

![False inclusions and detected true effects](shared/sparse-covariate-exposure-response/figures/figure-1-selection.png)

**Figure 1.** Mean number of inactive covariates declared important, and share of true covariates declared important, per trial (150 trials per sample size).

At 120 patients, backward stepwise selection kept on average 3.63 inactive covariates for response and 4.19 for toxicity, against 1.27 and 1.75 declared by the full model (p < 0.05) and 0.11 and 0.07 by the horseshoe model. The horseshoe model paid for this with power: it declared 34% of the true response covariates and 13% of the true toxicity covariates, against 86% and 72% for stepwise selection and 69% and 52% for the full model. At 300 patients the false inclusions were 2.89 and 3.26 (stepwise), 0.98 and 1.13 (full) and 0.16 and 0.11 (horseshoe), with power of 98% and 97% (stepwise), 96% and 90% (full) and 85% and 61% (horseshoe) (Figure 1, Table 2).

### Dose decision {#dose-decision}

![Share of trials choosing the best feasible dose](shared/sparse-covariate-exposure-response/figures/figure-2-dose-decision.png)

**Figure 2.** Share of trials selecting relative dose 2, the best feasible dose, by covariate strategy and sample size. Error bars show the 95% Wald interval for the share, given 150 trials.

**Table 2. Covariate strategy and dose decision.** Values are given as response / toxicity where two values appear. False inclusions are inactive covariates declared important. Exposure effect: mean estimate (true 0.45 / 0.90). Error: mean absolute error of the predicted rates over the three doses, in percentage points. Best feasible dose chosen: share of trials selecting relative dose 2. n: patients per trial; AIC: Akaike's information criterion.

| n | Method | False inclusions | True covariates detected | Exposure effect | Error (points) | Best feasible dose chosen |
| --- | --- | --- | --- | --- | --- | --- |
| 120 | Full model | 1.27 / 1.75 | 69% / 52% | 0.62 / 1.51 | 4.3 / 3.5 | 74.0% |
| 120 | Backward stepwise (AIC) | 3.63 / 4.19 | 86% / 72% | 0.57 / 1.28 | 4.1 / 3.1 | 76.7% |
| 120 | Horseshoe prior | 0.11 / 0.07 | 34% / 13% | 0.48 / 0.98 | 4.0 / 2.7 | 76.7% |
| 300 | Full model | 0.98 / 1.13 | 96% / 90% | 0.48 / 1.02 | 2.6 / 2.1 | 88.0% |
| 300 | Backward stepwise (AIC) | 2.89 / 3.26 | 98% / 97% | 0.46 / 0.97 | 2.5 / 2.1 | 87.3% |
| 300 | Horseshoe prior | 0.16 / 0.11 | 85% / 61% | 0.45 / 0.93 | 2.4 / 2.0 | 88.7% |

The share of trials selecting the best feasible dose was 74.0% (full model), 76.7% (stepwise) and 76.7% (horseshoe) at 120 patients (Figure 2, Table 2), and 88.0%, 87.3% and 88.7% at 300. The paired difference between the horseshoe and the full model was +2.7 percentage points (SE 3.8) at 120 patients and +0.7 (SE 1.8) at 300; against stepwise selection it was 0.0 (SE 3.4) and +1.3 (SE 1.6). No difference was distinguishable from sampling error. Wrong choices at 120 patients were dose 3 in 13–19% of trials and dose 1 in 5–11%; at 300 patients they were dose 3 in 11–13% and dose 1 in at most 0.7%.

The predicted rates themselves were more accurate with the horseshoe model, by small amounts. The paired difference in mean absolute error was −0.29 points (SE 0.12) against the full model and −0.17 (SE 0.09) against stepwise selection for response at 120 patients, and −0.81 (SE 0.13) and −0.38 (SE 0.11) for toxicity; at 300 patients they were −0.20 (SE 0.05) and −0.09 (SE 0.04) for response and −0.08 (SE 0.05) and −0.05 (SE 0.04) for toxicity. These gains are much smaller than the toxicity margin of 5.7 points.

### Exposure effect {#exposure-effect}

The exposure effect on toxicity was overestimated at 120 patients by the full model (mean 1.51, median 1.35; true 0.90) and by stepwise selection (1.28, median 1.10), and was close to the truth with the horseshoe model (0.98, median 0.94). The corresponding exposure effects on response were 0.62, 0.57 and 0.48 (medians 0.58, 0.57 and 0.46; true 0.45). At 300 patients all three means were within 0.12 of the truth (toxicity 1.02, 0.97, 0.93; response 0.48, 0.46, 0.45).

A separate check of 150 further trials of 120 patients (seed 20261117) estimated the exposure effect with four models: the full model, a model with the exposure alone, the horseshoe model, and a Bayesian model with a fixed normal prior (SD 1) on all covariate effects. The medians for toxicity (true 0.90) were 1.35 (full model), 0.83 (exposure alone), 0.95 (horseshoe) and 1.46 (normal prior); for response (true 0.45) they were 0.59, 0.35, 0.44 and 0.65. One full-model fit diverged under separation, which makes its mean meaningless, so medians are reported.

### Certainty about the dose {#certainty}

![Posterior probability that dose 2 is the best feasible dose](shared/sparse-covariate-exposure-response/figures/figure-3-posterior-certainty.png)

**Figure 3.** Posterior probability, from the horseshoe model, that relative dose 2 is the best feasible dose, in 150 trials per sample size. Dose 2 is the true best feasible dose in every trial.

The mean posterior probability was 0.56 at 120 patients and 0.74 at 300. It was at least 0.8 in 8.7% and 46% of trials, and at most 0.2 in 2.7% and 2.0% of trials, which are trials in which the analysis was confident against the true best dose (Figure 3). A point-estimate method chooses a dose in every trial, but it gives no statement of this certainty.

### Lasso, Firth-type penalty and a narrower toxicity margin {#further-results}

**Table 3. Share of trials selecting the best feasible dose in the further simulations.** Values are percentages of 150 trials (binomial standard error in parentheses). The margin is the distance between the toxicity of dose 2 and the 25% limit.

| Margin | n | Method | Best feasible dose chosen |
| --- | --- | --- | --- |
| 5.7 points | 120 | Full model | 64.7% (3.9) |
| 5.7 points | 120 | Backward stepwise (AIC) | 67.3% (3.8) |
| 5.7 points | 120 | Horseshoe prior | 62.0% (4.0) |
| 5.7 points | 120 | Lasso (cross-validated) | 68.0% (3.8) |
| 5.7 points | 120 | Jeffreys-penalized probit | 63.1% (4.0) |
| 5.7 points | 300 | Full model | 86.7% (2.8) |
| 5.7 points | 300 | Backward stepwise (AIC) | 86.7% (2.8) |
| 5.7 points | 300 | Horseshoe prior | 85.3% (2.9) |
| 5.7 points | 300 | Lasso (cross-validated) | 90.7% (2.4) |
| 5.7 points | 300 | Jeffreys-penalized probit | 92.7% (2.1) |
| 2.0 points | 120 | Full model | 56.7% (4.0) |
| 2.0 points | 120 | Backward stepwise (AIC) | 55.3% (4.1) |
| 2.0 points | 120 | Horseshoe prior | 68.7% (3.8) |
| 2.0 points | 120 | Lasso (cross-validated) | 63.3% (3.9) |
| 2.0 points | 120 | Jeffreys-penalized probit | 36.7% (3.9) |
| 2.0 points | 300 | Full model | 76.7% (3.5) |
| 2.0 points | 300 | Backward stepwise (AIC) | 79.3% (3.3) |
| 2.0 points | 300 | Horseshoe prior | 83.3% (3.0) |
| 2.0 points | 300 | Lasso (cross-validated) | 81.3% (3.2) |
| 2.0 points | 300 | Jeffreys-penalized probit | 62.0% (4.0) |

With the original margin, the share of trials selecting dose 2 was 62–68% at 120 patients and 85–93% at 300 (Table 3), against 74–77% and 87–89% in the main run, so the level varied by up to 15 points between runs of 150 trials. The methods stayed close at 120 patients (paired difference of the horseshoe model minus the full model −2.7 points, SE 4.2), and the lasso and the Firth-type penalty did as well or better than the horseshoe model (horseshoe minus lasso −6.0, SE 2.5 at 120 patients and −5.3, SE 1.8 at 300; minus the Firth-type penalty −1.3, SE 5.6 and −7.3, SE 2.5). The lasso kept on average 0.45 inactive covariates in the response model and 0.11 in the toxicity model at 120 patients, detecting 38% and 5% of the true effects (0.50 and 0.09 inactive, 84% and 24% detected at 300 patients).

With the narrow margin, the horseshoe model selected dose 2 in 68.7% of trials at 120 patients and 83.3% at 300, more often than the full model (+12.0 points, SE 4.2; +6.7, SE 2.6), backward stepwise selection (+13.3, SE 3.9; +4.0, SE 1.9) and the Firth-type penalty (+32.0, SE 4.9; +21.3, SE 3.6). The difference from the lasso was +5.3 (SE 2.8) and +2.0 (SE 1.8).

## Discussion {#article-discussion}

The covariate strategy changed the covariate list far more than it changed the dose. Across the three methods in the main simulation the share of trials selecting the best feasible dose was within about three percentage points between methods (the 95% interval of the paired difference at 120 patients, about −5 to +10 points against the full model, does not establish equivalence), with a sampling error of 3.5 at 120 patients, although the average number of inactive covariates declared important differed by a factor of 18 to 60 between stepwise selection and the horseshoe model. One explanation is that, in a randomized dose-ranging trial, the covariates are balanced across dose arms, so the predicted population rate at each dose depends mostly on the exposure effect and the dose arms, and covariate errors that average out across patients matter little. I did not test this explanation by varying the balance of covariates. The smaller prediction errors with the horseshoe model were consistent in direction but small beside the margin to the toxicity limit, which is what determined the decision.

The further comparisons qualify this result. With the 5.7-point margin no strategy was consistently ahead, and the difference in level between two runs was as large as the differences between methods. With a 2.0-point margin, where the choice rests on small differences in predicted toxicity, the horseshoe model selected the best dose more often than the full model and stepwise selection (by 12 to 13 points at 120 patients), so in this design the covariate strategy matters when the margin is narrow. The Firth-type penalty did worst there (36.7% at 120 patients); I did not investigate why, and a penalty that also shrinks the exposure effect may be responsible, which I did not test.

The exposure slope differed between methods. With 22 parameters and a modest number of toxicity events, the full model and stepwise selection overestimated the exposure effect on toxicity by 68% and 42% at 120 patients. Among the three methods in the main simulation, the horseshoe estimate was closest to the true value at both sample sizes (0.98 and 0.93 against 0.90). The exposure term had a normal prior with SD 2 and was outside the horseshoe hierarchy. In the further check, the overestimate by the full model persisted in the medians, so it was not caused only by a few separated fits, and a normal prior with SD 1 on the covariates did not remove it (median 1.46), whereas the horseshoe prior (0.95) and the model with the exposure alone (0.83) came close to 0.90. The comparison suggests that estimating the 20 covariate effects jointly with the exposure effect may contribute to the overestimation. The exposure-alone model underestimated the response effect (0.35 against 0.45), which is consistent with omitting prognostic covariates from a probit model, so it is not a general remedy. At 300 patients the three estimates were closer to each other, within 0.12 of the truth.

The horseshoe model's low false-inclusion count came with low power at 120 patients (34% and 13% for response and toxicity), probably because a 90% credible interval criterion is conservative when the data carry little information about any single covariate. Another threshold would be expected to move it along the same trade-off, so the comparison with stepwise selection is of two operating points, not of two curves. The posterior probability of the best dose was low at 120 patients (mean 0.56) and moderate at 300 (0.74); the analysis reported its uncertainty about a decision that point-estimate methods report as a single answer.

The simulation has limits that bear on the conclusions. The true effects were sparse by construction, which favors the horseshoe prior; many small effects would reduce its advantage. Dose was randomized. Exposure depended on covariates through clearance, so the unadjusted exposure–outcome association can reflect those covariates. Exposure was known without error, and all baseline factors used to generate the data were included as candidates. The probit link and equicorrelated normal covariates are simple assumptions. Only two toxicity margins (5.7 and 2.0 points) were examined. Only one horseshoe prior specification was used, with no tuning of its global scale, and the regularized horseshoe prior was not compared; the lasso used a logit link for data generated from probit models. The sampler used one chain of 800 retained draws per fit; convergence and agreement with maximum likelihood were checked for both endpoints on 20 datasets and one large dataset each, not for every trial, and no simulation-based calibration was run. A single truth configuration was used, covariate effects were population-level, and individual-level prediction was not assessed.

## Conclusion {#article-conclusion}

With 20 candidate covariates, backward stepwise selection kept 3 to 4 inactive covariates per model while a horseshoe-prior model kept almost none. With a toxicity margin of 5.7 percentage points, the strategies selected the best feasible dose at similar rates (74–77% at 120 patients and 87–89% at 300 in the main run) and none was consistently ahead in a replicate that included a lasso and a Firth-type penalty. With a margin of 2.0 points the horseshoe model selected the best dose more often than the full model and stepwise selection (+12.0 and +13.3 points at 120 patients). The horseshoe model also gave the estimate of the exposure effect on toxicity closest to the truth at 120 patients and a posterior statement of how certain the dose choice was. Whether the covariate strategy changes a population-level dose decision therefore depends on how close the best dose is to the toxicity limit. The result applies to this sparse, randomized, probit design and was not tested against other designs.

## Data and code availability {#reproduce}

No patient data were used. The companion contains the shared definitions and the Gibbs sampler (`common.R`), the simulations (`simulate.R`, `simulate_extra.R`), the sampler and exposure-estimate checks (`validate.R`, `exposure_check.R`), the summary and figure scripts, the aggregate results and the session information. The seed is 20261115; `Rscript simulate.R 150 1200` takes about 12 minutes on a desktop computer, and `Rscript simulate_extra.R orig` and `Rscript simulate_extra.R narrow` (seeds 20261118 and 20261119) about 40 minutes each. The per-trial results (about 0.2 MB) are included, so the summaries can be reproduced without rerunning the simulation.

[Download the companion: code and results](shared/sparse-covariate-exposure-response/sparse-covariate-exposure-response-companion.zip)

## References {#article-references}

1. <span id="ref-1"></span>Carvalho CM, Polson NG, Scott JG. The horseshoe estimator for sparse signals. Biometrika. 2010;97(2):465–480. [doi:10.1093/biomet/asq017](https://doi.org/10.1093/biomet/asq017)
2. <span id="ref-2"></span>Makalic E, Schmidt DF. A simple sampler for the horseshoe estimator. IEEE Signal Process Lett. 2016;23(1):179–182. [doi:10.1109/LSP.2015.2503725](https://doi.org/10.1109/LSP.2015.2503725)
3. <span id="ref-3"></span>Venables WN, Ripley BD. Modern applied statistics with S. 4th ed. New York: Springer; 2002. [doi:10.1007/978-0-387-21706-2](https://doi.org/10.1007/978-0-387-21706-2)
4. <span id="ref-4"></span>Albert JH, Chib S. Bayesian analysis of binary and polychotomous response data. J Am Stat Assoc. 1993;88(422):669–679. [doi:10.1080/01621459.1993.10476321](https://doi.org/10.1080/01621459.1993.10476321)
5. <span id="ref-5"></span>Friedman J, Hastie T, Tibshirani R. Regularization paths for generalized linear models via coordinate descent. J Stat Softw. 2010;33(1):1–22. [doi:10.18637/jss.v033.i01](https://doi.org/10.18637/jss.v033.i01)
6. <span id="ref-6"></span>Firth D. Bias reduction of maximum likelihood estimates. Biometrika. 1993;80(1):27–38. [doi:10.1093/biomet/80.1.27](https://doi.org/10.1093/biomet/80.1.27)
7. <span id="ref-7"></span>R Core Team. R: A language and environment for statistical computing [Software]. 2026. Version 4.5.3. [R Project](https://www.r-project.org/)
