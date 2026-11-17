## Abstract {#article-abstract}

In a randomized trial of two doses, the dose can be chosen from the response rates of the two arms, or from an exposure–response (E–R) model that also uses each patient's exposure. I compared the two in simulated trials with 20 to 100 patients per arm, including trials in which disease severity raises clearance and lowers response. The correct dose was defined from the true rates: the high dose is correct only if its response gain is at least 0.08 and its toxicity is at most 25%. The severity effects are assumed values, not estimates for any drug. With exposure not confounded and 40 patients per arm, the arm-level rule picked the correct dose in 80.0% of 2,000 trials when the high dose was better, against 88.1% for the E–R model; with a nearly flat response the two gave 71.5% and 73.8%. When severity raised clearance, the E–R model's share rose to 95.6% against 75.0% where the high dose was better, but with a nearly flat response it picked the correct low dose in 25.4% of trials at 40 per arm and 11.9% at 100 per arm, while the arm-level rule gave 73.0% and 77.0%. In diagnostic runs, the fitted exposure slope averaged 0.87 against a true 0.2, and adding the true severity removed the bias (0.23); a noisy severity marker removed part of it. The failure belongs to an E–R model that estimates its slope from exposure differences without the confounder; randomization protects the arm comparison, not that slope.

## Introduction {#article-introduction}

The final FDA guidance on dosage optimization in oncology recommends a randomized, parallel dose-response trial when several dosages are compared, because randomization makes the patients on each dosage comparable and so limits bias in the estimated dose–response and exposure–response (E–R) relationships ([1](#ref-1)). The same guidance states that this trial need not be powered to show superiority of one dosage or non-inferiority among dosages at the error rates of a registrational trial, and that population pharmacokinetic and E–R analyses should be considered together with safety, tolerability and activity when a dosage is selected ([1](#ref-1)). Trials sized this way are small. The randomized optimal selection (ROSE) design, a selection design for dose optimization, reports that 15 to 40 patients per dose arm typically gives a probability of 60% to 70% of selecting the optimal dose ([2](#ref-2)). That figure is stated in the abstract of the preprint; I did not reproduce the design here.

Two sources of information are available at that sample size. One is the response and toxicity rate of each arm. The other is the exposure of each patient, which varies within an arm because clearance varies, and which an E–R model can use to estimate the rate at each dose from all patients rather than from one arm at a time. The second source carries a risk, because exposure is not randomized even when the dose is. Confounding of E–R relationships by prognostic factors has been described for monoclonal antibodies in oncology, with multiple dose levels among the proposed mitigations ([3](#ref-3)). The mechanism assumed here is disease severity that both raises clearance and lowers response. This is an assumption, not a finding of this study, and that reference concerns survival endpoints whereas this study uses binary response and toxicity.

The question is a decision question: **in a randomized two-dose trial of 20 to 100 patients per arm, does selecting the dose from an E–R model rather than from the arm-level rates raise the probability of selecting the correct dose, and does it still do so when severity drives both clearance and response?** The answer is measured by simulation, with a true best dose defined in advance so that every selection can be scored.

## Methods {#article-methods}

### Simulated trials

Each trial randomized the same number of patients (20, 30, 40, 60 or 100 per arm) to a low and a high dose of relative size 1 and 2. A patient had a severity S drawn from a standard normal distribution and a clearance deviation η with standard deviation (SD) 0.30, unrelated to severity. The log exposure was log(dose) − η − κS. With κ = 0 severity did not affect exposure (the not-confounded condition). With κ = 0.4 one SD of severity raised clearance by 49% (the confounded condition). The probability of response was a logistic function of intercept plus slope × log exposure − 0.6 × S, so worse disease lowered response. The probability of toxicity was a logistic function of intercept plus slope × log exposure, with no severity term. The intercepts were set so that the low-dose response and toxicity rates equalled the values in Table 1 in the whole simulated population, and the true rates at the high dose were computed from 400,000 simulated patients. Responses and toxicities were drawn independently given exposure and severity. A severity marker, equal to S plus normal noise with SD 0.8 (reliability 0.61), was available to the analysis; S was not.

**Table 1.** Scenarios and true rates (not confounded / confounded).

| Scenario | Slope on log exposure (response, toxicity) | Response at low dose → high dose | Toxicity at low dose → high dose | Correct dose |
| --- | --- | --- | --- | --- |
| S1 high dose better | 1.4, 0.8 | 0.250 → 0.444 / 0.416 | 0.100 → 0.162 / 0.161 | High |
| S2 near plateau | 0.2, 0.8 | 0.350 → 0.380 / 0.379 | 0.100 → 0.162 / 0.161 | Low |
| S3 high-dose toxicity above the cap | 1.4, 1.6 | 0.250 → 0.444 / 0.416 | 0.150 → 0.339 / 0.325 | Low |

The correct dose was defined from these true rates. The high dose is correct if its true toxicity is at most 25% and its true response is at least 0.08 higher than at the low dose; otherwise the low dose is correct. The 0.08 gain and the 25% cap are assumed values and applied identically to every rule below. In S2 the true gain is about 0.03.

### Selection rules

R1 used the observed arm rates: choose the high dose if its observed toxicity is at most 25% and its observed response is at least 0.08 above that of the low dose. R2 fitted logistic regressions of response and of toxicity on log exposure in all patients pooled. It recovered each patient's low-dose exposure by subtracting log 2 for high-dose patients, and computed the rate at each dose as the mean fitted probability after setting every patient's log exposure to that dose; the same thresholds then decided. R2 therefore uses more structure than R1: exposure proportional to dose, exposure measured without error, and a fitted E–R form that equals the true form. R3 was R2 with the noisy severity marker added to both regressions. R1 is a decision boundary of the kind used in selection designs for dose optimization, not the calibrated ROSE design ([2](#ref-2)). I chose it to isolate the effect of using exposure.

Each combination of condition, scenario and sample size was simulated 2,000 times (seed 20261117, R 4.5.3 ([4](#ref-4))). The estimand was the probability of selecting the correct dose; its Monte Carlo standard error (SE) is at most 0.012 and is shown as 95% intervals in Figure 1. All rules were applied to the same simulated trials. I did not compute paired differences between rules; for two rules treated as independent, the Monte Carlo SE of a difference is at most 0.016, and I did not interpret differences smaller than 0.03 as a ranking.

### Diagnostic runs

To check why R2 failed in some scenarios, I repeated S1 and S2 at 40 and 100 patients per arm in both conditions (1,000 trials each, seed 20261118) and saved, for the response model only, the fitted exposure slope and the estimated gain (response at the high dose minus at the low dose) of R1 (the arm difference), R2, R3 and RO. RO was R2 with the true severity S in the model; it is an oracle that an analyst cannot have, included to show what the bias would be without the confounder. The diagnostic runs did not change the decisions of the main simulation.

## Results {#article-results}

![Probability of selecting the correct dose by rule and scenario, with and without confounding](shared/randomized-dose-selection-exposure-response/figures/figure-1-selection.png)

**Figure 1.** Probability of selecting the correct dose (vertical axis) by patients per arm (horizontal axis). Columns are the scenarios S1 (high dose better), S2 (near plateau, true response gain about 0.03) and S3 (high-dose toxicity above the 25% cap); rows are the conditions without and with confounding of exposure by severity. R1 is the response-rate difference, R2 the E–R model and R3 the E–R model with a noisy severity marker. Bars are 95% intervals (±1.96 binomial SE) from 2,000 simulated trials per point; the grey line marks 0.8.

**Table 2.** Probability of selecting the correct dose by patients per arm (2,000 trials each; Monte Carlo SE at most 0.012).

| Condition | Scenario | Rule | 20 | 30 | 40 | 60 | 100 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Not confounded | S1 | R1 | 0.726 | 0.755 | 0.800 | 0.897 | 0.943 |
| Not confounded | S1 | R2 | 0.761 | 0.833 | 0.881 | 0.941 | 0.979 |
| Not confounded | S1 | R3 | 0.756 | 0.832 | 0.876 | 0.940 | 0.981 |
| Not confounded | S2 | R1 | 0.643 | 0.703 | 0.715 | 0.706 | 0.747 |
| Not confounded | S2 | R2 | 0.704 | 0.726 | 0.738 | 0.791 | 0.838 |
| Not confounded | S2 | R3 | 0.718 | 0.734 | 0.749 | 0.794 | 0.843 |
| Not confounded | S3 | R1 | 0.775 | 0.874 | 0.869 | 0.924 | 0.963 |
| Not confounded | S3 | R2 | 0.840 | 0.877 | 0.911 | 0.958 | 0.983 |
| Not confounded | S3 | R3 | 0.841 | 0.875 | 0.910 | 0.956 | 0.983 |
| Confounded | S1 | R1 | 0.666 | 0.696 | 0.750 | 0.839 | 0.904 |
| Confounded | S1 | R2 | 0.874 | 0.936 | 0.956 | 0.981 | 0.997 |
| Confounded | S1 | R3 | 0.807 | 0.905 | 0.931 | 0.973 | 0.995 |
| Confounded | S2 | R1 | 0.662 | 0.685 | 0.730 | 0.708 | 0.770 |
| Confounded | S2 | R2 | 0.382 | 0.302 | 0.254 | 0.189 | 0.119 |
| Confounded | S2 | R3 | 0.566 | 0.547 | 0.522 | 0.519 | 0.497 |
| Confounded | S3 | R1 | 0.770 | 0.853 | 0.862 | 0.886 | 0.944 |
| Confounded | S3 | R2 | 0.791 | 0.843 | 0.883 | 0.930 | 0.976 |
| Confounded | S3 | R3 | 0.802 | 0.843 | 0.874 | 0.921 | 0.969 |

R1, response-rate difference; R2, E–R model; R3, E–R model with a noisy severity marker. Columns give patients per arm.

### Without confounding the E–R model helps when the high dose is better

When exposure was not confounded and the high dose was better (S1), the E–R model chose the correct dose more often than the arm-level rule at every sample size: 0.761 against 0.726 at 20 per arm, 0.881 against 0.800 at 40 and 0.979 against 0.943 at 100 (Table 2). When the high dose was too toxic (S3) the values were 0.911 against 0.869 at 40 per arm. When the response was nearly flat (S2), the E–R rules were ahead of the arm-level rule by 0.06 to 0.08 at 20 per arm (0.704 and 0.718 against 0.643), within 0.04 of it at 30 and 40 per arm (0.738 and 0.749 against 0.715 at 40), and ahead by 0.08 to 0.10 at 60 and 100 per arm (0.791 and 0.794 against 0.706 at 60; 0.838 and 0.843 against 0.747 at 100). No rule reached 0.80 at 40 per arm in S2, because the true gain (about 0.03) lay about 0.05 below the 0.08 boundary, a distance smaller than the sampling error of an arm difference (SD about 0.11 at 40 per arm, 0.07 at 100 per arm).

### When severity drives clearance the same model fails near a plateau

Under confounding the E–R model's share was larger where the high dose was better: 0.956 against 0.750 at 40 per arm (Table 2). In the nearly flat scenario the pattern reversed. The E–R model chose the correct (low) dose in 0.382 of trials at 20 per arm, 0.254 at 40 and 0.119 at 100, so it chose the high dose more often as the trial grew. The arm-level rule improved from 0.662 to 0.770 over the same range. Adding the noisy severity marker (R3) raised the correct share to 0.566, 0.522 and 0.497, about half of the trials and below the arm-level rule at every sample size. The same marker lowered the share where the high dose was better (0.874 to 0.807 at 20 per arm and 0.956 to 0.931 at 40). When the high dose was too toxic (S3) confounding changed little: the three rules were within 0.021 of each other at 40 per arm (0.862, 0.883 and 0.874).

### Fitted slopes and estimated gains

The diagnostic runs show the bias directly (Table 3). With confounding and a nearly flat response, the E–R model's exposure slope averaged 0.87 at 40 per arm against a true 0.2, and its estimated gain averaged 0.128 against a true 0.029; the estimated gain reached 0.08 or more in 80.1% of trials. With the true severity in the model (RO) the slope averaged 0.23, the gain 0.032 and the share at or above 0.08 was 26.2%, which matches the value without confounding (26.3%). The arm difference (R1) was unbiased (0.028). The noisy marker (R3) was in between (slope 0.58, gain 0.082, share 51.7%). The slope bias did not shrink with 100 patients per arm (0.84 for R2). Where the high dose was better, the gain was also overestimated by R2 (0.248 against a true 0.166), but the arm difference was unbiased (0.167) and the true-severity model gave a share of 89.4% at or above 0.08 against 75.9% for the arm difference, so part of the E–R model's advantage there does not depend on the bias.

**Table 3.** Fitted exposure slope (response model), estimated response gain of the high dose over the low dose, and share of trials with an estimated gain of at least 0.08 (1,000 trials per row).

| Condition | Scenario | Patients per arm | Method | Mean fitted slope | Mean estimated gain | Share with gain ≥ 0.08 |
| --- | --- | --- | --- | --- | --- | --- |
| Not confounded | S2 | 40 | R1 | n/a | 0.025 (true 0.030) | 0.258 |
| Not confounded | S2 | 40 | R2 | 0.18 (true 0.2) | 0.028 (true 0.030) | 0.265 |
| Not confounded | S2 | 40 | R3 | 0.19 (true 0.2) | 0.028 (true 0.030) | 0.265 |
| Not confounded | S2 | 40 | RO | 0.20 (true 0.2) | 0.029 (true 0.030) | 0.263 |
| Confounded | S1 | 40 | R1 | n/a | 0.167 (true 0.166) | 0.759 |
| Confounded | S1 | 40 | R2 | 2.09 (true 1.4) | 0.248 (true 0.166) | 0.999 |
| Confounded | S1 | 40 | R3 | 1.85 (true 1.4) | 0.210 (true 0.166) | 0.987 |
| Confounded | S1 | 40 | RO | 1.52 (true 1.4) | 0.168 (true 0.166) | 0.894 |
| Confounded | S2 | 40 | R1 | n/a | 0.028 (true 0.029) | 0.282 |
| Confounded | S2 | 40 | R2 | 0.87 (true 0.2) | 0.128 (true 0.029) | 0.801 |
| Confounded | S2 | 40 | R3 | 0.58 (true 0.2) | 0.082 (true 0.029) | 0.517 |
| Confounded | S2 | 40 | RO | 0.23 (true 0.2) | 0.032 (true 0.029) | 0.262 |
| Confounded | S2 | 100 | R1 | n/a | 0.027 (true 0.029) | 0.215 |
| Confounded | S2 | 100 | R2 | 0.84 (true 0.2) | 0.126 (true 0.029) | 0.906 |
| Confounded | S2 | 100 | R3 | 0.55 (true 0.2) | 0.080 (true 0.029) | 0.502 |
| Confounded | S2 | 100 | RO | 0.21 (true 0.2) | 0.029 (true 0.029) | 0.163 |

R1, arm difference; R2, E–R model; R3, E–R model with a noisy severity marker; RO, E–R model with the true severity (not available in practice).

## Discussion {#article-discussion}

The two sources of information are exposed to different biases. The arm-level rule compares randomized groups, so its error comes from sampling only, and that error was large: at 40 per arm in S2 without confounding, it chose the correct dose in 71.5% of trials, because the true gain of about 0.03 was not reliably separated from the 0.08 boundary. This is a success probability of a different design and endpoint than the 60% to 70% reported for ROSE at 15 to 40 patients per arm ([2](#ref-2)), and I give the two figures for orientation only.

The E–R model also uses the differences in exposure between patients of the same arm. When those differences carry information about severity, and severity also changes response, the fitted slope absorbs the effect of severity. The diagnostic runs measured this: the slope averaged 0.87 against a true 0.2, and adding the true severity brought it to 0.23 (Table 3). This is omitted-variable bias, which the guidance's reason for randomizing, comparability of patients on each dosage ([1](#ref-1)), does not address, because comparability of arms does not extend to patients with different exposures inside one arm. A steeper slope predicts a larger gain from the high dose, so the model selected the high dose when the true gain was 0.03, and more often as the trial grew, because the bias does not shrink with sample size and the estimate converges on the wrong value. Where the high dose was better, the same bias inflated the estimated gain, which gave the right decision for a partly wrong reason, but the true-severity model also beat the arm difference (89.4% against 75.9% of trials with a gain at or above 0.08), so the E–R model's advantage there has a genuine component from using all patients. The two components were separated in the estimated gains and not in the decision metric.

The failure is a property of an E–R model that estimates its slope from exposure differences without the confounder. I did not test an E–R model that includes the dose arm as a covariate. Because exposure is a deterministic function of dose in this simulation, the arm and the exposure effect cannot be separated in such a model without additional structure, and I did not examine it. The conclusion about randomization is therefore limited to the pooled model used here.

How much of the bias a real analysis removes depends on how well the confounder is measured. In these simulations the true severity removed it, and a marker with reliability 0.61 removed part of it (slope 0.58 against 0.87 for no adjustment). The marker also reduced the share of correct decisions where the high dose was better, because the bias had helped there. I did not test other marker reliabilities, so the proportion removed is specific to this setting. Confounding of E–R relationships by prognostic factors has been described for antibodies ([3](#ref-3)); I read that reference only through its abstract, and I do not claim that these rates describe a particular drug. How strongly severity moves clearance and response is assumed here (κ = 0.4 and 0.6 on the logit scale) and was not estimated.

### Limitations

Only two doses were compared, so every dose decision was one comparison. The E–R form in the data and in the analysis was the same logistic form with log exposure, so R2 and R3 had a correctly specified model, and the clean-condition advantage of R2 over R1 depends on that and on the proportionality and error-free measurement of exposure; a misspecified form or noisy exposure would reduce it. Every patient contributed one response and one toxicity indicator. The confounding strength (κ and the severity effect on response) and the marker reliability were assumed values tested at one setting each, so the size of the E–R failure depends on them. The failure near a plateau is also amplified by the decision boundary: a gain of 0.03 sits 0.05 below the 0.08 boundary, and I did not vary the boundary, the true gain in S2 or the toxicity cap. The 0.08 gain boundary and the 25% toxicity cap were assumed and used for every rule. R1 is a simple boundary, not the ROSE design with its calibrated boundary and sample size ([2](#ref-2)). I read the relevant passages of the FDA guidance in full text and the ROSE preprint only through its abstract page. Adaptive stopping, three or more doses, crossover and time-to-event endpoints were not studied.

## Conclusion {#article-conclusion}

In a simulated randomized two-dose trial with 20 to 100 patients per arm, selecting the dose from an E–R model picked the correct dose more often than the arm-level response rates when exposure was not confounded and the high dose was better (0.881 against 0.800 at 40 per arm); with a nearly flat response the two gave 0.738 and 0.715 at 40 per arm, and the E–R model was ahead at 100 per arm (0.838 against 0.747). When severity raised clearance and lowered response, the pooled E–R model overestimated the exposure slope (0.87 against a true 0.2) and chose the high dose in 74.7% of near-plateau trials at 40 per arm (0.254 correct, 0.119 at 100 per arm). Adding the true severity removed the bias, and a noisy marker removed part of it (0.522 correct at 40 per arm). Randomizing the dose protects the comparison between arms but not an exposure slope estimated from exposure differences within the trial. These results hold for the assumed severity effects, the two-dose design and the pooled model.

## Data and code availability {#reproduce}

No patient data were used. The companion contains the simulation script (`simulate.R`), the diagnostic script (`simulate_extra.R`), the figure script (`figure1.R`), the aggregate results (`results/summary.csv` and `results/diagnostics.csv`) and the session information. The seeds are 20261117 (`Rscript simulate.R 2000`, about 11 minutes on a desktop computer) and 20261118 (`Rscript simulate_extra.R 1000`, about 1.5 minutes).

[Download the companion: code and aggregate results](shared/randomized-dose-selection-exposure-response/randomized-dose-selection-exposure-response-companion.zip)

## References {#article-references}

1. <span id="ref-1"></span>U.S. Food and Drug Administration. Optimizing the dosage of human prescription drugs and biological products for the treatment of oncologic diseases: guidance for industry [Internet]. 2024 Aug [cited 2026 Nov 17]. Docket FDA-2022-D-2827. Available from: [FDA guidance page](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/optimizing-dosage-human-prescription-drugs-and-biological-products-treatment-oncologic-diseases)
2. <span id="ref-2"></span>Wang S, Yuan Y, Liu S. ROSE: randomized optimal selection design for dose optimization [Preprint]. arXiv; 2025. Version 4, 21 Aug 2025. [doi:10.48550/arXiv.2505.03898](https://doi.org/10.48550/arXiv.2505.03898)
3. <span id="ref-3"></span>Kawakatsu S, Bruno R, Kågedal M, Li C, Girish S, Joshi A, et al. Confounding factors in exposure–response analyses and mitigation strategies for monoclonal antibodies in oncology. Br J Clin Pharmacol. 2021;87(6):2493–2501. [doi:10.1111/bcp.14662](https://doi.org/10.1111/bcp.14662)
4. <span id="ref-4"></span>R Core Team. R: A language and environment for statistical computing [Software]. 2026. Version 4.5.3. [R Project](https://www.r-project.org/)
