## Abstract {#summary}

A curve can fit PSA measurements without identifying a distinct regrowth rate. It can also outperform an overly rigid decay model while adding little to the latest observed PSA. Those are different claims and require different checks.

Using 400 patients in a public PSA/survival example dataset, I compared early predictions from a constant last value, a linear hierarchy, a single-decay model, and a decline–regrowth hierarchy. Each prediction used only the patient's history available at 6, 12, 18 or 24 weeks. The target was the observed, uncensored, on-treatment PSA in the following 12 weeks.

The two-component model improved on the fitted linear and single-decay candidates. Its advantage over the last-value benchmark was uncertain at 6 and 12 weeks; at 24 weeks the last value was better in the paired test-cohort comparison. Regrowth remained weakly informed under the implemented approximate hierarchical estimator, with its population mean at the lower parameter bound at every landmark. This is a failure to qualify a regrowth-based early decision rule, rather than evidence that regrowth never occurs.

<span id="_1"></span>

## Introduction {#question-and-context-of-use}

The question of interest is: how much observation is needed before separating PSA decline and regrowth adds reliable predictive information beyond simple extrapolation?

The context of use is: retrospective evaluation of measurement and modeling design. The analysis does not select an individual treatment, compare drug effects, estimate resistant-cell fractions, or qualify PSA as an overall-survival surrogate.

The relevant comparison is an honest prediction benchmark at the same landmark. Fitting all available follow-up and then claiming an early prediction would answer a different question.

## Methods {#public-data-and-the-audit-that-changed-the-analysis}

The official downloadable example ([1](#ref-1)) contains 400 patients, 6,627 PSA rows and 286 deaths. It is the original publication's training subset from the VENICE comparator treated with docetaxel/prednisone. The separate original validation subset is not included in this download. I split the 400 again for internal evaluation; this is **not external validation** ([2](#ref-2)).

Three details matter before fitting:

1. **The supplied observation is transformed.** The CSV's PSA values are on the natural-log `log(PSA+1)` scale, consistent with the original observation equation. All 165 below-quantification rows equal `log(1.1)`, matching the documented 0.1 ng/mL threshold. Treating that column as raw ng/mL would fit the wrong model.
2. **Repeated dates are not identical duplicates.** Two same-day PSA groups contain slightly different values. I average each group on the supplied transformed scale, leaving 6,625 distinct patient/date PSA records. I do not silently keep one arbitrary value.
3. **Treatment time and survival are separate records.** The CSV includes treatment-end time and two survival rows per patient: a time-zero record and a final event/censoring record. PSA after treatment end is excluded from the main target. It remains available for a separate sensitivity analysis.

The original protocol scheduled PSA approximately every 21 days during treatment and every 84 days afterwards. Actual visit times are used rather than forcing measurements onto those schedules. Pre-treatment records are retained for the audit but excluded from this on-treatment shape model ([2](#ref-2)).

The raw CSV is publicly offered without account registration. It is not bundled with the companion: public availability does not establish unrestricted redistribution rights. The acquisition script downloads the official file and checks its recorded SHA256. All figures here are original aggregate figures.

### Model structure and estimator {#models-separate-the-shape-from-the-estimation-method}

Let the latent on-treatment PSA be

\[
S_i(t)=B_i\left[A_i e^{-d_i t}+(1-A_i)e^{g_i t}\right],
\qquad 0<A_i<1,\ d_i,g_i>0,
\]

and the observation model be

\[
y_{ij}=\log\{1+S_i(t_{ij})\}+\epsilon_{ij}.
\]

Dividing the latent response by \(B_i\) gives exactly one at time zero. This avoids doubling the baseline by summing two unweighted exponentials. Estimating a latent baseline also avoids treating every noisy ratio to the first measurement as independent.

The transformed parameters \(z_i=(\log B_i,\log d_i,\log g_i,\operatorname{logit}A_i)\) have a diagonal Gaussian hierarchy. The comparator candidates are the latest measured value, a hierarchical linear predictor on the supplied scale, and a single exponential decline. Here \(d\), \(g\) and \(A\) describe PSA shape; they are not directly measured tumor-cell growth, mutation or resistant fractions.

**The estimator is deliberately explicit about its approximation.** Population parameters maximize a first-order Gaussian marginal likelihood,

\[
f(z_i,t)\approx f(\mu,t)+J(\mu,t)(z_i-\mu),
\qquad V_i=J_i\operatorname{diag}(\omega^2)J_i^\top+\sigma^2I.
\]

The linear candidate has an exact Gaussian marginal likelihood; the nonlinear candidates use a Taylor approximation. Individual predictions use nonlinear empirical-Bayes MAP estimation. This is neither SAEM nor exact nonlinear marginal maximum likelihood, and it does not reproduce the original mechanistic ODE/survival model. Three population starts, optimizer diagnostics and numerical bounds are supplied with the results.

Population fitting uses uncensored measurements. Individual MAP calculations include a Gaussian CDF contribution for below-quantification observations. This hybrid is a limitation: an individual censoring term does not make the population estimator a fully censored NLME likelihood. Predictive checks and sensitivity analyses are needed before relying on it, and parameter qualification would require a more complete estimator.

### Prediction design {#prediction-design}

The split is fixed at **240 training, 80 calibration and 80 test patients**, using seed 20261004. For each landmark, eligibility requires continued treatment and follow-up plus at least two prior on-treatment PSA measurements spanning 14 days. Population fitting uses only eligible training patients and their history through that landmark. Test predictions use each test patient's prior history; their future measurements do not enter fitting.

The main target is an **observed-target window**: uncensored PSA measured while still on treatment during the next 84 days. It is not an exact visit-time target, and it does not represent patients with no subsequent measurement. Errors are calculated within patient and then averaged across patients, so frequent measurement does not make one patient dominate the MAE.

For prediction intervals, each calibration patient contributes one score: the largest absolute prediction error over that patient's observed target window. The finite-sample 90% split-conformal quantile gives a common radius on the supplied scale. Test coverage means all the patient's observed targets fall inside their intervals. It is separate from per-measurement coverage. This construction requires exchangeability of selected calibration/test patients and does not give a guarantee for missing measurements or after a shift in clinical setting ([3](#ref-3)).

![Eligibility and observed-target availability by landmark](shared/psa-early-observation/figures/target-availability.png)

**Figure 1.** The denominator changes with landmark. Of the assigned 80 test patients, 69, 69, 53 and 43 contribute main prediction targets. Falling error over time therefore cannot be attributed solely to gaining more observations; later assessment also selects a different treatment-continuing population.

## Results {#results-a-complex-model-needs-a-strong-simple-benchmark}

All MAEs below are in `log(PSA+1)` units and are patient-weighted. They are not ng/mL errors, percentages or response probabilities.

**Table 1. Patient-weighted prediction error on the observed target sets**

| Landmark | Test patients / targets | Last value MAE | Linear MAE | Decay MAE | Two-component MAE |
| --- | --- | --- | --- | --- | --- |
| 6 weeks | 69 / 234 | 0.472 | 0.543 | 0.565 | 0.429 |
| 12 weeks | 69 / 213 | 0.395 | 0.536 | 0.511 | 0.365 |
| 18 weeks | 53 / 163 | 0.325 | 0.583 | 0.555 | 0.354 |
| 24 weeks | 43 / 118 | 0.249 | 0.515 | 0.477 | 0.327 |

![Prediction accuracy and paired differences from the latest-value benchmark](shared/psa-early-observation/figures/prediction-comparison.png)

**Figure 2.** Left: point estimates on each landmark's observed target set. Right: two-component minus last-value MAE with a paired, patient-resampling 95% interval. Negative differences favor the two-component candidate. The resampling is conditional on the fitted models, and the four landmarks are not independent confirmatory tests.

**Table 2. Paired differences from last-value prediction**

| Landmark | Two-component − last MAE | Paired bootstrap 95% interval |
| --- | --- | --- |
| 6 weeks | -0.043 | [-0.108, +0.024] |
| 12 weeks | -0.030 | [-0.070, +0.006] |
| 18 weeks | +0.029 | [-0.015, +0.074] |
| 24 weeks | +0.078 | [+0.016, +0.153] |

Figure 2 and Tables 1–2 show that the two-component model's smaller error than the declining candidates is consistent with its ability to flatten as the declining component becomes small. However, **the fitted regrowth component is nearly flat**. Calling the improvement proof of detected regrowth would confuse flexibility with mechanism identification.

The differences from the last-value benchmark at 6 and 12 weeks are small and their resampling intervals cross zero. At 24 weeks, the two-component candidate is worse on this paired held-out comparison. No parameter or prior was selected using these test errors. The results do not justify discarding the simple benchmark or choosing a universal optimal observation duration.

### Prediction-interval calibration {#calibration-is-not-the-same-as-a-narrow-interval}

**Table 3. Patient-level prediction-interval coverage**

| Landmark | Calibration patients | Two-component patient coverage | Full width | Last-value patient coverage |
| --- | --- | --- | --- | --- |
| 6 weeks | 59 | 95.7% | 3.483 | 97.1% |
| 12 weeks | 67 | 98.6% | 2.988 | 98.6% |
| 18 weeks | 57 | 90.6% | 2.121 | 98.1% |
| 24 weeks | 45 | 88.4% | 1.496 | 95.3% |

Full width is on the supplied transformed scale. The nominal patient-level target is 90%, and coverage is evaluated over all observed on-treatment targets per patient in the 12-week window.

![Patient-level interval coverage and full width](shared/psa-early-observation/figures/interval-calibration.png)

**Figure 3.** A separate calibration set adjusts the interval radius; the test set assesses it. High early coverage comes with broad intervals. At 24 weeks the two-component candidate covers 88.4% of test patients, compared with 95.3% for the last-value predictor. These finite-test estimates have sampling uncertainty; neither number establishes clinical acceptability.

Figure 3 and Table 3 show the interval trade-off. For scale, a radius of 1.742 at 6 weeks means a roughly 5.7-fold factor on `PSA+1`, not a precise prediction. Coverage alone would conceal that lack of resolution. These calibrated prediction intervals are not confidence intervals for \(g\) or tumor biology.

### Regrowth identification {#identification-the-prior-must-not-supply-the-conclusion}

**Table 4. Local information diagnostics in eligible test patients**

| Landmark | Eligible test patients | Data rank <4 | Data condition >10⁶ | Median g SD ratio |
| --- | --- | --- | --- | --- |
| 6 weeks | 70 | 70 | 70 | 0.999999 |
| 12 weeks | 72 | 18 | 72 | 1.000000 |
| 18 weeks | 61 | 1 | 61 | 0.999989 |
| 24 weeks | 48 | 0 | 46 | 0.999966 |

The SD ratio is the local conditional standard deviation of log regrowth rate divided by its fitted prior SD. It is based on an uncensored Gauss–Newton approximation and is a diagnostic, not a qualified posterior interval.

![Local information diagnostics for decline and regrowth](shared/psa-early-observation/figures/regrowth-identification.png)

**Figure 4.** Regrowth SD ratios remain approximately one. The data-only information matrix is singular or ill-conditioned for most eligible test patients. Its rank improves with more observations, but full algebraic rank alone does not mean a reliable rate estimate.

Figure 4 and Table 4 show weak regrowth information. Every two-component population fit places mean log regrowth at the specified lower bound, \(-10\). Most individual fits also have a bound-active parameter. All population starts report convergence and closely agreeing objectives, but numerical convergence does not turn a bound-active estimate into an identifiable biological quantity. At 6 weeks all 70 eligible test patients have data-only rank below four; even at 24 weeks 46 of 48 have condition number above \(10^6\).

I therefore do not publish individually definitive growth/decline estimates or convert these parameters into treatment recommendations. The supported statement concerns this bounded model and this first-order estimator. It does **not** establish that regrowth is unidentifiable under every likelihood, a richer mechanistic model, a longer complete series, or a fully joint analysis.

### Sensitivity to shrinkage and treatment boundaries {#sensitivity-shrinkage-and-treatment-boundaries-matter}

**Table 5. Two-component MAE under prior and target-window sensitivities**

| Landmark | Prior SD ×0.5 | Primary | Prior SD ×2 | Including post-treatment targets |
| --- | --- | --- | --- | --- |
| 6 weeks | 0.504 | 0.429 | 0.388 | 0.451 |
| 12 weeks | 0.392 | 0.365 | 0.359 | 0.399 |
| 18 weeks | 0.380 | 0.354 | 0.345 | 0.361 |
| 24 weeks | 0.361 | 0.327 | 0.301 | 0.392 |

The prior-scale columns use the same primary target patients; the post-treatment column changes the target set and is not a paired treatment-effect comparison.

![Prior-scale sensitivity and aggregate residual checks](shared/psa-early-observation/figures/prediction-sensitivity.png)

**Figure 5.** Left: changing individual prior SD changes predictions without changing the population fit. Right: mean residuals in equal-count prediction bins expose remaining errors. Only aggregate bins are shown; no participant trajectories or IDs are published.

In Figure 5 and Table 5, doubling individual prior SD reduces two-component MAE at 6 weeks from 0.429 to 0.388; halving it increases MAE to 0.504. This is evidence of sensitivity, not permission to choose the doubled prior after viewing the test set. At 24 weeks the observed post-treatment sensitivity has MAE 0.392 across 44 patients, compared with 0.327 across 43 patients in the primary target. Extrapolation across treatment cessation changes the interpretation and availability.

Omitting individual BLQ history gives the same main test errors here because test patients contributing the main prediction errors have no BLQ in their landmark histories. This statement does not include eligible patients without observed prediction targets. That sensitivity is uninformative about handling BLQ in general. Future BLQ targets are excluded from the main errors, and uncensored-only population fitting remains a limitation. A 42-day forecast-window analysis is also included in the companion with its own target counts.

## Discussion {#what-can-be-decided}

This analysis supports keeping the latest-value predictor as a serious benchmark, separating predictive accuracy from regrowth identification, and auditing risk-set changes before interpreting improvement with time. It also shows the exact conditions under which this implemented hierarchy adds little or loses predictive performance.

It does **not** establish a minimum observation period for a regrowth-based treatment decision. None of the examined windows resolves the identified rate-estimation problem under this estimator, and landmark comparisons involve different selected patients. Nor does it evaluate a future trial's benefit–risk or prove PSA surrogacy for survival.

These results cannot be transferred as a validated cutoff to another therapy.

### Limitations {#limits-and-reproducibility}

This is one publicly distributed treatment-group subset with internal validation. It lacks the original independent validation patients, detailed dose histories and treatment-switch causes. Treatment cessation, death and measurement availability create selection that is not solved by splitting patients or adding a conformal interval. Missing-not-at-random behavior is not identified. Small later test groups and the fixed split limit precision.

The first-order population approximation, diagonal random-effects hierarchy, numerical bounds, partly omitted censoring likelihood and local information approximation are substantial methodological limits. Their effect on apparent regrowth cannot be separated completely here. A full nonlinear/joint model and genuinely independent cohort would be needed for stronger parameter and clinical claims. No such completed analysis is implied.

## Conclusion {#article-conclusion}

The implemented two-component hierarchy did not establish reliable regrowth identification or an early decision threshold. Its uncertain advantage over the last-value benchmark, bound-active rate estimates and changing observed-target populations require predictive accuracy and parameter identification to be judged separately.

## Data and code availability {#availability}

The companion contains the acquisition/hash check, transformation and audit code, fixed protocol, model implementation, aggregate results, five original figures, verification tests and an executed notebook. Raw data and individual parameters are not redistributed. The notebook reruns the analysis from the official download. All tables are generated from the saved results rather than manually transcribed.


[Download original code, aggregate results and executed notebook](shared/psa-early-observation/psa-early-observation-companion.zip)

## References {#references}

1. <span id="ref-1"></span>MonolixSuite documentation. PSA and survival data set [Dataset and documentation]. Version 2024R1; updated 2024 Oct 24. Public CSV accessed 2026 Oct 4. [Official example](https://monolixsuite.slp-software.com/monolix/2024R1/psa-and-survival-data-set). The acquired file’s SHA-256 is recorded in the companion.
2. <span id="ref-2"></span>Desmée S, Mentré F, Veyrat-Follet C, Sébastien B, Guedj J. Using the SAEM algorithm for mechanistic joint models characterizing the relationship between nonlinear PSA kinetics and survival in prostate cancer patients. Biometrics. 2017;73(1):305–312. [doi:10.1111/biom.12537](https://doi.org/10.1111/biom.12537). [Open author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC5654727/). Data provenance and observation definition; the estimator used here differs.
3. <span id="ref-3"></span>Angelopoulos AN, Bates S. A gentle introduction to conformal prediction and distribution-free uncertainty quantification. arXiv [Preprint]. 2021; revised 2022 Dec 7. arXiv:2107.07511. [doi:10.48550/arXiv.2107.07511](https://doi.org/10.48550/arXiv.2107.07511). [Version 6](https://arxiv.org/abs/2107.07511v6). Background for finite-sample split calibration; selection assumptions remain necessary here.
