## Abstract {#article-abstract}

An exposure–response (E–R) analysis of a monoclonal antibody can report that higher exposure prolongs survival when the dose has no effect, because patients with more severe disease clear the antibody faster and also die sooner. This article measures that error in simulated randomized dose-ranging trials (400 patients, relative doses 1, 2 and 4, 1,000 trials per scenario). The severity effects are assumed, not estimated from any drug. When the drug had no effect and severity raised clearance by 28% and the hazard of death by 35% per standard deviation (SD), a Cox model of baseline exposure reported a protective effect in 37.6% of trials (2.5% expected by chance), with a mean hazard ratio of 0.90 per doubling of exposure. Adjusting for a noisy severity marker lowered the rate to 9.6%. Adjusting for the true severity, or analyzing the randomized dose, gave 1.6% and 2.1%. With stronger confounding (hazard 82% higher per SD) the rates were 87.6%, 26.4%, 2.3% and 2.1%. Time-varying exposure was biased more than baseline exposure in every confounded scenario. Analyzing the randomized dose kept the error rate at its nominal level, at a cost in power (53% versus 64% when the true hazard ratio was 0.84 per doubling and severity was unrelated to clearance). Enlarging the trial to 1,000 patients did not reduce the bias; the false-positive rate of the unadjusted analysis rose to 75%.

## Introduction {#article-introduction}

Dose decisions for antibodies in oncology draw on E–R analyses of survival ([1](#ref-1)). That inference is fragile because exposure is not assigned. It is the dose divided by clearance, and clearance carries information about the patient. Turner and colleagues examined three pembrolizumab studies and reported that overall survival did not depend on dose between 2 and 10 mg/kg (hazard ratio 0.98 in melanoma and in non-small-cell lung cancer), while baseline clearance was strongly associated with survival (unadjusted hazard ratios 2.56 and 2.64; 1.64 and 1.88 after adjustment for prognostic factors) ([2](#ref-2)). They read the clearance association as a marker of disease severity, not as an effect of exposure ([2](#ref-2)). Liu and colleagues described time-varying nivolumab clearance that followed disease dynamics and concluded, from simulation and trial data, that exposure metrics from the first dose agreed better with the true E–R relationship than steady-state metrics ([3](#ref-3)). Dai and colleagues organized the problem into baseline-driven and response-driven components of an apparent E–R relationship, and proposed single-dose pharmacokinetic metrics and multiple dose levels as ways to separate them ([4](#ref-4)). Kawakatsu and colleagues argued that E–R analyses of trials with a single dose level are limited and that earlier trials should study more dose levels ([1](#ref-1)).

These papers describe the mechanism and the remedies. The question here is quantitative and tied to a decision: **in a trial where severity raises both clearance and the hazard of death, how often does each common estimator report that higher exposure improves survival when it does not, how large is its error when the drug does work, and what does the one estimator that randomization protects, the analysis of the randomized dose, give up?** The decision at stake is whether to keep or raise a dose because an E–R slope looks favorable. A wrong decision here is a higher dose, with its toxicity, for no survival benefit. The simulation does not estimate how large the severity effects are for any real antibody; those values are assumptions, varied over a range.

## Methods {#article-methods}

### Simulated trials {#simulated-trials}

Each trial randomized 400 patients with equal probability to relative doses 1, 2 and 4. Patient *i* has a baseline severity S₀ (standard normal; one unit is one SD) that worsens by a patient-specific drift *g* per month (mean 0.04, SD 0.03), so that S(t) = S₀ + *g*t. The relative steady-state concentration C(t) = dose / clearance at monthly visits follows

ln C(t) = ln D − κ S(t) − η, with η ~ N(0, 0.25²),

where D is the randomized relative dose, κ is the effect of severity on log clearance, and η is between-patient variability unrelated to severity. Measured concentrations carry a log-scale residual error with SD 0.10. The monthly hazard of death was

h(t) = 0.04 · exp(γ S(t) + β ln C(t)),

where γ is the log hazard ratio per unit of severity and β is the true effect of log exposure on the log hazard. The hazard depends on the true concentration, so the drug acts through exposure, which is the effect an E–R analysis aims to estimate. An event occurred in a month with probability 1 − exp(−h(t)), at a time uniform within that month. Patients dropped out independently at 1% per month, and follow-up ended at 24 months. Between 205 and 257 of the 400 patients had an event on average, depending on the scenario (Table 1). The assumed causal structure is shown in Figure 1. A baseline severity marker B = S₀ + noise (SD 0.8; reliability 0.61) stood for an imperfect clinical measure of disease burden available to the analyst; S₀ itself was not.

**Table 1. Scenarios.** κ = 0.25 raises clearance by 28% per SD of severity. γ = 0.3 and 0.6 raise the hazard of death by 35% and 82% per SD. β = −0.25 corresponds to a hazard ratio of 0.84 per doubling of exposure.

| Scenario | Drug effect (β) | Severity effect on hazard (γ) | Other changes |
| --- | --- | --- | --- |
| A1 | 0 | 0 | None |
| A2 | 0 | 0.3 | None |
| A3 | 0 | 0.6 | None |
| B1 | −0.25 | 0 | None |
| B2 | −0.25 | 0.3 | None |
| B3 | −0.25 | 0.6 | None |
| S1 | 0 | 0.3 | 1,000 patients |
| S2 | 0 | 0.3 | κ = 0.5 |
| S3 | 0 | 0.3 | κ = 0.1 |
| S4 | 0 | 0.3 | Marker SD 0.3 (reliability 0.92) |
| S5 | 0 | 0.3 | Doses 1, 1.5 and 2 (two-fold span) |
| S6 | 0 | 0.3 | Pharmacokinetic residual error SD 0.3 |
| S7 | 0 | 0.3 | Clearance variability SD 0.5 (unrelated to severity) |
| S8 | 0 | 0.3 | No severity drift (mean 0) |

### Estimators and metrics {#estimators-and-metrics}

Five Cox models were fitted to every simulated trial. (a) Baseline exposure: ln C at the first visit as the only covariate. (b) The same, adjusted for the noisy marker B. (c) The same, adjusted for the true S₀, which no real analysis has. (d) Time-varying exposure: ln C at the latest monthly visit as a time-dependent covariate. (e) Randomized dose: ln D as the covariate. Because exposure is proportional to dose in this model, the coefficient of ln D estimates β on the same scale. For each model, the hazard ratio per doubling of exposure is exp(coefficient · ln 2). Each scenario used 1,000 trials with seed 20261115 (S5–S8 were run separately with seed 20261116) (the standard error of the mean bias was at most 0.004 on the log-hazard scale). Reported are the mean hazard ratio and the central 95% range of the estimates across trials, the coverage of the 95% Wald interval, and the share of trials in which the model declared a protective effect (z < −1.96, which happens by chance in 2.5% of trials when the true effect is zero). The first four estimators use the observed exposure; the fifth uses only the assigned dose.

The framing in the Introduction rests on the abstracts and bibliographic records of the four papers cited there; their full texts were not read. The simulation was run in R 4.5.3 with the survival package 3.8-6 ([5](#ref-5), [6](#ref-6)).

## Results {#article-results}

![Assumed causal structure](shared/exposure-response-severity-clearance/figures/figure-1-dag.png)

**Figure 1.** Assumed causal structure. The randomized dose is independent of severity, whereas exposure inherits severity through clearance.

### Without severity effects, all estimators agree {#without-confounding}

With no drug effect and no severity effect on the hazard (scenario A1), all five estimators were unbiased (mean hazard ratio 1.00 per doubling) and covered the truth in 94–95% of trials. Declared protective effects ranged from 2.9% to 3.7%, slightly above the 2.5% expected by chance (Monte Carlo SE about 0.5 percentage points). With a true hazard ratio of 0.84 per doubling (B1), the estimators that used observed exposure detected it in 59–64% of trials, and the randomized-dose analysis detected it in 53%.

### A drug with no effect {#a-drug-with-no-effect}

![Estimated hazard ratios per doubling of exposure](shared/exposure-response-severity-clearance/figures/figure-2-estimates.png)

**Figure 2.** Hazard ratio of death per doubling of exposure for each estimator, across 1,000 simulated trials per scenario. Points are means; bars are the central 95% range of the estimates. The dashed line is the true value.

**Table 2. Performance in the main confounded scenarios.** Hazard ratio (HR) per doubling of exposure, mean and central 95% range across 1,000 trials; coverage of the 95% interval; share of trials declaring a protective effect (z < −1.96); mean bias of the coefficient on the log-hazard scale (Monte Carlo standard error, SE).

| Scenario | Estimator | HR per doubling (95% range) | Coverage | Declared protective | Bias (SE) |
| --- | --- | --- | --- | --- | --- |
| A2 (no drug effect, γ = 0.3) | Baseline exposure, unadjusted | 0.90 (0.79–1.03) | 62% | 37.6% | −0.156 (0.003) |
| A2 | Baseline exposure, adjusted for severity marker | 0.96 (0.84–1.10) | 90% | 9.6% | −0.066 (0.003) |
| A2 | Baseline exposure, adjusted for true severity | 1.00 (0.88–1.15) | 95% | 1.6% | +0.003 (0.003) |
| A2 | Time-varying exposure | 0.89 (0.78–1.01) | 54% | 45.7% | −0.173 (0.003) |
| A2 | Randomized dose | 1.00 (0.86–1.16) | 96% | 2.1% | −0.001 (0.004) |
| A3 (no drug effect, γ = 0.6) | Baseline exposure, unadjusted | 0.82 (0.73–0.93) | 12% | 87.6% | −0.288 (0.003) |
| A3 | Baseline exposure, adjusted for severity marker | 0.91 (0.80–1.04) | 74% | 26.4% | −0.130 (0.003) |
| A3 | Baseline exposure, adjusted for true severity | 1.00 (0.88–1.16) | 95% | 2.3% | −0.001 (0.003) |
| A3 | Time-varying exposure | 0.80 (0.71–0.91) | 8% | 92.5% | −0.317 (0.003) |
| A3 | Randomized dose | 1.00 (0.87–1.17) | 95% | 2.1% | +0.001 (0.004) |
| B2 (true HR 0.84, γ = 0.3) | Baseline exposure, unadjusted | 0.76 (0.66–0.87) | 69% | 97.9% | −0.151 (0.003) |
| B2 | Baseline exposure, adjusted for severity marker | 0.80 (0.70–0.93) | 91% | 86.7% | −0.064 (0.003) |
| B2 | Baseline exposure, adjusted for true severity | 0.84 (0.73–0.98) | 95% | 63.5% | +0.002 (0.003) |
| B2 | Time-varying exposure | 0.75 (0.66–0.86) | 64% | 98.6% | −0.168 (0.003) |
| B2 | Randomized dose | 0.84 (0.72–1.00) | 95% | 54.1% | +0.006 (0.004) |

When the drug had no effect and severity moderately raised the hazard (A2), baseline exposure analyzed alone gave a mean hazard ratio of 0.90 per doubling (Figure 2) and declared a protective effect in 37.6% of trials, far above the 2.5% expected by chance; the interval covered the truth in 62%. Strong confounding (A3) raised the rate to 87.6% (coverage 12%). Adjusting for the noisy marker reduced the bias from −0.156 to −0.066 in A2 and from −0.288 to −0.130 in A3, but not to zero; the error rates stayed at 9.6% and 26.4%. Adjusting for the true severity removed the bias, and the randomized-dose analysis was unbiased in the same scenarios (Figure 3, Table 2).

![Share of trials declaring a protective effect](shared/exposure-response-severity-clearance/figures/figure-3-decisions.png)

**Figure 3.** Share of 1,000 simulated trials in which each estimator declared a protective exposure effect (z < −1.96). Left: no drug effect (false positives, 2.5% expected by chance). Right: true hazard ratio 0.84 per doubling (power).

Time-varying exposure was biased more than baseline exposure in all eight scenarios in which severity affected the hazard (A2 −0.173 against −0.156; A3 −0.317 against −0.288; the values for B2 are in Table 2 and those for B3 and S1–S4 are in the companion summary; Monte Carlo SE 0.003 each, unpaired), in the direction of the first-dose finding of Liu and colleagues ([3](#ref-3)). The difference persisted when the severity drift was removed (S8), and no change in clearance caused by the response was simulated. The difference between the two estimators was small beside the bias that both shared.

### A drug with an effect {#a-drug-with-an-effect}

With a true hazard ratio of 0.84 per doubling and moderate confounding (B2), baseline exposure analyzed alone gave 0.76, so the benefit of doubling the exposure was overstated (24% against 16% lower hazard), and a protective effect was declared in 97.9% of trials. Part of that power was spurious: with the true severity in the model the rate was 63.5%. The randomized-dose analysis estimated 0.84, with a rate of 54.1%. Under strong confounding (B3), the randomized-dose analysis showed a small attenuation (0.87, bias +0.048, SE 0.004, coverage 93%), while adjustment for the true severity gave 0.85 (bias +0.016, SE 0.003). I did not investigate this attenuation. Its size is what unmeasured heterogeneity in severity would produce in a marginal hazard ratio, but I did not test that as the cause.

### Cost of using the randomized dose {#cost-of-the-randomized-dose}

The randomized-dose analysis was valid without any assumption about severity, but its estimates were less precise. The SD of its coefficient was 0.12 against 0.10 for the models using observed exposure (A1 and B1, 400 patients), which lowered power from 59–64% to 53% when the true hazard ratio was 0.84 per doubling and severity was unrelated to clearance (B1). The loss was 6 to 11 percentage points at this dose range (a four-fold span) and was larger with a narrower range: the SD of the coefficient was 0.23 at a two-fold span (S5).

### Sensitivity analyses {#sensitivity}

The bias did not shrink with sample size. With 1,000 patients (S1), the unadjusted baseline analysis was no less biased (−0.158 against −0.156 at 400 patients), so it was wrong more often: it declared a protective effect in 75.0% of trials (37.6% at 400 patients), against 2.5% for the randomized-dose analysis. A larger effect of severity on clearance (κ = 0.5, S2) raised the unadjusted false-positive rate to 81.8%; a smaller one (κ = 0.1, S3) lowered it to 8.9%. A better marker (SD 0.3, reliability 0.92; S4) made the marker-adjusted analysis behave like the true-severity analysis (2.3%). A narrower dose span (S5: doses 1, 1.5 and 2) left the randomized-dose analysis unbiased (0.99) but doubled the SD of its coefficient (0.229 against 0.113 at the four-fold span), while the unadjusted baseline analysis became more biased (−0.339) and declared a protective effect in 69.1% of trials. Larger pharmacokinetic error (SD 0.3; S6) and larger clearance variability unrelated to severity (SD 0.5; S7) lowered the false-positive rate of the unadjusted analysis to 31.4% and 27.6%. Removing the severity drift (S8) left it at 36.3%, and time-varying exposure remained more biased than baseline exposure (−0.179 against −0.163).

## Discussion {#article-discussion}

Within the assumptions, a slope of 0.90 per doubling of exposure, which would look like a moderate dose–benefit relationship, arose with no drug effect in more than a third of simulated trials. The error does not come from a small sample. It comes from a causal structure in which the exposure measure carries the patient's severity, so a larger trial only makes the wrong answer more certain. Adjustment helped more with the better marker (reliability 0.92: 2.3% in S4) than with the marker used in the main scenarios (reliability 0.61), which removed more than half of the bias but left false-positive rates of 9.6% to 26.4%; only two reliabilities were tried. This matches the mechanism and the mitigation strategies described in the reviews ([1](#ref-1), [4](#ref-4)). The simulation adds the size of the error under stated conditions and the power given up by the protected analysis.

The randomized-dose analysis held its error rate at the nominal level in every scenario without a drug effect, because assignment is independent of severity; with a drug effect it was unbiased in B1 and B2 and slightly attenuated in B3. Its price was lower power, and it requires at least two dose levels with a useful span. In a trial with one dose level the randomized-dose estimator does not exist, and none of the other four can separate the drug effect from the severity effect without an untestable assumption such as no unmeasured confounding. I did not evaluate tumor-growth-inhibition-to-survival models or the other approaches discussed in the literature ([1](#ref-1)), so the simulation says nothing about whether they behave better.

The limits of the simulation bear on how far these numbers can travel. Severity is one continuous latent factor, and everything that distorts the real relationship is folded into it. The hazard depends only on the current concentration, and the effect of exposure is log-linear with proportional hazards. No dose reductions, interruptions, cumulative exposure or competing prognostic factors were simulated. Clearance is proportional to dose, which the randomized-dose estimator needs, and dropout is non-informative. The dose span, the pharmacokinetic noise, the between-patient variability in clearance and the severity drift were each changed once (S5–S8), not in combination. The severity effects on clearance and on the hazard are assumed values; the real sizes differ by drug and indication, and these simulations do not estimate them. The Cox model estimates marginal hazard ratios, which can differ from conditional ones when heterogeneity is large (B3).

## Conclusion {#article-conclusion}

With severity raising both clearance and the hazard of death, a Cox model of exposure reported a protective effect of a drug with no effect in 37.6% of simulated trials under moderate confounding and 87.6% under strong confounding, against 2.5% expected by chance. Time-varying exposure was worse than baseline exposure, and adjustment for an imperfect severity marker reduced but did not remove the error. Only the analysis of the randomized dose kept the error rate nominal (2.1%), at the cost of some power. Whether these error rates describe a particular antibody depends on how strongly severity moves its clearance and its hazard, which these simulations assume and do not measure.

## Data and code availability {#reproduce}

No patient data were used. The companion contains the simulation script (`simulate.R`), the summary and figure scripts, the aggregate results for every scenario, and the session information. The seed is 20261115 and one run of `Rscript simulate.R 1000` takes about 15 minutes on a desktop computer; the per-trial estimates (about 6 MB) are regenerated by the script and are not distributed.

[Download the companion: code and aggregate results](shared/exposure-response-severity-clearance/exposure-response-severity-clearance-companion.zip)

## References {#article-references}

1. <span id="ref-1"></span>Kawakatsu S, Bruno R, Kågedal M, Li C, Girish S, Joshi A, et al. Confounding factors in exposure–response analyses and mitigation strategies for monoclonal antibodies in oncology. Br J Clin Pharmacol. 2021;87(6):2493–2501. [doi:10.1111/bcp.14662](https://doi.org/10.1111/bcp.14662)
2. <span id="ref-2"></span>Turner DC, Kondic AG, Anderson KM, Robinson AG, Garon EB, Riess JW, et al. Pembrolizumab exposure–response assessments challenged by association of cancer cachexia and catabolic clearance. Clin Cancer Res. 2018;24(23):5841–5849. [doi:10.1158/1078-0432.CCR-18-0415](https://doi.org/10.1158/1078-0432.CCR-18-0415)
3. <span id="ref-3"></span>Liu C, Yu J, Li H, Liu J, Xu Y, Song P, et al. Association of time-varying clearance of nivolumab with disease dynamics and its implications on exposure response analysis. Clin Pharmacol Ther. 2017;101(5):657–666. [doi:10.1002/cpt.656](https://doi.org/10.1002/cpt.656)
4. <span id="ref-4"></span>Dai HI, Vugmeyster Y, Mangal N. Characterizing exposure–response relationship for therapeutic monoclonal antibodies in immuno-oncology and beyond: challenges, perspectives, and prospects. Clin Pharmacol Ther. 2020;108(6):1156–1170. [doi:10.1002/cpt.1953](https://doi.org/10.1002/cpt.1953)
5. <span id="ref-5"></span>R Core Team. R: A language and environment for statistical computing [Software]. 2026. Version 4.5.3. [R Project](https://www.r-project.org/)
6. <span id="ref-6"></span>Therneau TM. survival: Survival Analysis [Software]. Version 3.8-6. [CRAN record](https://cran.r-project.org/package=survival)
