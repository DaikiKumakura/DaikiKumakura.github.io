**QOI: How far did the 26-patient second-line Phase 1 cohort constrain the Phase 3 response rate and survival in the RAS G12 population?**

**COU: Evaluate how much information a Phase 1 expansion cohort gave for a decision to proceed to Phase 3, and estimate the value of enlarging the cohort. This is a retrospective check and is not used for any decision itself.**

QOI (question of interest) is the question this article answers, and COU (context of use) is what the answer is used for. The subject is daraxonrasib, an RAS(ON) inhibitor (a drug that binds the active, GTP-bound form of RAS and suppresses its function). From the second-line (2L) RAS G12X cohort of 26 patients (9 responders, 300 mg once daily) disclosed by the company in September 2025 ([1](#ref-1)), the objective response rate (ORR) and survival in the RAS G12 population of the daraxonrasib arm of the Phase 3 trial RASolute 302, reported in 2026 ([2](#ref-2), [3](#ref-3)), were predicted and compared with the observed values. The answer is as follows. The 26 patients narrowed the Phase 3 ORR to about 18–55% (95% predictive interval, with no allowance for a shift between trials), and the observed 33.2% fell inside it. Allowing a shift between trials widened the interval to 12–66%, and enlarging the cohort barely narrowed it.

## Abstract

**Problem**　How much information did a small Phase 1 expansion cohort carry about the Phase 3 result? This is a retrospective check made now that the result is known: predictions were made from information public by the end of 2025 and compared with the observed values.

**Methods**　From the Phase 1 ORR of 9/26, a beta-binomial model gave the predictive distribution of the number of Phase 3 responders, and the size of the shift between trials τ (on the logit scale for the ORR) was varied over four scenarios (0, 0.25, 0.5, 0.75). For median progression-free survival (PFS) and median overall survival (OS), the standard error on the log scale was recovered from the reported 95% confidence interval. A simulation over Phase 1 cohort sizes (26–104) gave the width of the predictive interval and the probability of a "proceed" call. Mechanistic models were not fitted.

**Results**　The observed Phase 3 ORR of 33.2% (72/217; the count is back-calculated) fell inside the 95% predictive interval of 17.5–54.8% at τ = 0 and of 12.0–65.9% at τ = 0.5. The Phase 1-informed models had a log predictive score 1.1–1.8 nats better than a weak reference (Beta(0.5, 0.5)). Point extrapolation (using 9/26 as is) scored better still on this one pair (2.8 nats), but in repeated simulations it had the lowest coverage whether the true τ was 0 or 0.5. The observed median PFS of 7.3 months fell inside the predictive interval of 6.6–11.0 months and the observed median OS of 13.2 months inside 9.4–18.3 months; doubling the standard error widens the OS interval to 6.7–25.5 months, and because the Phase 3 follow-up is short the OS check is close to a trivial pass. Enlarging the Phase 1 cohort from 26 to 104 patients narrowed the width of the τ = 0.5 predictive interval only from 51 to 45 percentage points.

**Conclusion**　The 26 Phase 1 patients placed the Phase 3 ORR within 12–66%, depending on the assumed shift between trials, and the observed value was inside the interval. When the shift is large, enlarging the cohort barely narrows the predictive interval. The probability of a "proceed" call rose in some scenarios, but its size depends on the threshold, the rule and the assumed true ORR.

## Introduction

A Phase 1 expansion cohort often serves as the basis for deciding whether to proceed to Phase 3. For daraxonrasib, the company disclosed in a Form 8-K (a current report filed with the U.S. Securities and Exchange Commission) on 10 September 2025 an ORR of 35% (9/26), a median PFS of 8.5 months and a median OS of 13.1 months for 26 patients with RAS G12X disease in the 2L efficacy-evaluable population (a population the document does not define) ([1](#ref-1)). The Phase 3 trial RASolute 302 was reported later ([2](#ref-2), [3](#ref-3)), and the Phase 1 paper was published ([4](#ref-4)). Because of this time gap, information public by the end of 2025 can be separated from the 2026 observations, and a prediction can be checked against them.

This article counts how far the 26 patients constrained Phase 3 and what enlarging the cohort would have been worth. The check was designed with the observed values already known, so it is not blinded to them. No record exists to show that the models and benchmarks were fixed before the scripts were run. Benchmarks (b) and (c), the Beta(1,1) prior, the sensitivity analysis with doubled standard errors and the repeated-pair simulation were added after the first results were seen, as explanation. The choice of the end of 2025 as the training cutoff, and the classification of the 2026 Phase 1 paper as post hoc material, are also retrospective choices.

## Methods

### Training information and holdout information

Training information was limited to what was public by 31 December 2025. The input was the 8-K ([1](#ref-1)), with a 2L data cutoff of 30 June 2025. For RAS G12X, the ORR was 9/26 (35%), the median PFS 8.5 months (95% confidence interval 6.7–10.5), the median OS 13.1 months (10.9 to NE, not estimable) and the median follow-up 16.7 months (range 10.3–24.6). For RAS-mutant disease overall (G12X, G13X or Q61X) it was 11/38 (29%). ORR follows RECIST v1.1, the standard criteria for judging tumour shrinkage in solid tumours, and counts responses that were confirmed or still had the potential to be confirmed ([1](#ref-1)). The safety population of the 8-K (83 patients) is second line or later, whereas the efficacy cohort is labelled "2L efficacy evaluable" without a definition. The waterfall plot and the interim PFS and OS plots in the [8-K (Figures 1–3)](https://www.sec.gov/Archives/edgar/data/1628171/000119312525200078/d947102d8k.htm) are image files; they were not read or reproduced.

Holdout information is the RAS G12 population of the daraxonrasib arm in RASolute 302. Only the abstract of the original paper ([2](#ref-2)) could be read; the full text could not be retrieved. The G12 population values come from a secondary news report ([3](#ref-3)): ORR 33.2% (217 evaluable patients), median PFS 7.3 months (6.3–8.1), median OS 13.2 months (10.0 to NE), median follow-up 8.5 months (range 3.2–15.9; whole trial) and a data cutoff of 10 February 2026. The number of responders is not reported. The count of 72, back-calculated from 33.2% and 217, was used (72/217 = 33.2%, whereas 71 or 73 would not match the reported value). The count of 76, based on the 228 randomized patients, was a sensitivity analysis (76/228 = 33.3% does not reproduce the reported rounding, so it is only an approximation). The Phase 1 paper ([4](#ref-4)) and the FDA announcement ([5](#ref-5)) are dated after the end of 2025 and were used only for post hoc interpretation.

### Prediction of the response rate

From the Phase 1 responder count of 9/26, the posterior of the true ORR $p_1$ was Beta(0.5 + 9, 0.5 + 17) (Jeffreys prior; Beta(1,1) as a sensitivity analysis). The true Phase 3 ORR $p_3$ allowed a shift between trials $\delta$:

$$\operatorname{logit}(p_3)=\operatorname{logit}(p_1)+\delta,\qquad \delta\sim\mathcal{N}(0,\tau^2)$$

The number of Phase 3 responders $Y_3$ followed $\operatorname{Binomial}(217, p_3)$. $\tau$ (the size of the shift between trials) was placed at 0, 0.25, 0.5 and 0.75 as scenarios; these data cannot estimate $\tau$. A $\tau$ of 0.5 corresponds to one standard deviation moving the odds of response to about 1.65 times or 0.61 times the Phase 1 value. The predictive distribution was computed by numerical integration (4,000 quantile points of the beta posterior times 41 Gauss–Hermite nodes for $\delta$); no random numbers were used.

The evaluation used the predictive intervals (50, 80, 95%), the predictive probability of the observed count, the log predictive score (the natural logarithm of the predictive probability of the observed count; a strictly proper scoring rule ([6](#ref-6)); in nats, larger is better) and the probability integral transform (PIT). The PIT gives the position of the observation in the cumulative predictive distribution; a value near 0.5 means the centre of the prediction. For a discrete distribution the midpoint version was used: the cumulative probability just below the observed count plus half the probability of the observed count. This is the expectation of the randomized PIT ([7](#ref-7)). Three benchmarks were used: (a) point extrapolation, using 9/26 as is; (b) a weak reference that does not use Phase 1 ($p_3 \sim$ Beta(0.5, 0.5), a U-shaped distribution with mean 50% spread over 0–100%, not a realistic weakly informative prior for 2025); and (c) the 11/38 of the overall RAS-mutant cohort as the prior (it includes the G12X patients and is not independent).

### Median survival

Survival was handled at the summary level only. The reported median was taken as the estimate of the log median, and the standard error was recovered by assuming the 95% confidence interval is symmetric on the log scale: $\mathrm{se}=(\ln \mathrm{upper}-\ln \mathrm{lower})/(2\times1.96)$. For OS, whose upper bound is NE, the lower bound only was used, $\mathrm{se}=(\ln m-\ln \mathrm{lower})/1.96$. With 26 patients, an event-count standard error of $1/\sqrt{26}\approx0.20$ under an exponential assumption is larger than the recovered values (0.11 for PFS, 0.09 for OS), so sensitivity analyses used multipliers of 1.5 and 2 for OS and 2 for PFS. The log of the Phase 3 median was given the distribution $\mathcal{N}(\ln m_1,\ \mathrm{se}_1^2+\tau^2)$, and the observation error of the observed Phase 3 median (recovered in the same way from its confidence interval) was added to check whether the observed value fell inside the predictive interval. Here $\tau$ is on the log-median scale; it is a different quantity from the $\tau$ on the logit scale of the ORR model, so the same 0.5 means something different. Kaplan–Meier curves were not digitized.

### Simulation of information value

The Phase 1 cohort size $n_1$ was set to 26, 52, 78 and 104, the true ORR was set between 0.20 and 0.40, and the responder count $x_1\sim\operatorname{Binomial}(n_1,p)$ was generated (seed 20261110, 4,000 draws per condition). From the posterior Beta(0.5 + $x_1$, 0.5 + $n_1-x_1$), the width of the 95% credible interval for $p_1$ and the width of the 95% predictive interval for the true Phase 3 ORR at $\tau = 0$ and 0.5 were computed (the widths used 400 draws with 2,000 posterior draws each). The probability of a "proceed" call was computed under the rule "proceed if $P(p>T\mid \text{data})\ge 0.8$" with $T$ at 15, 20 and 25%. The thresholds are arbitrary scenarios, not clinical criteria. In the repeated-pair simulation, the true $p_1$ was drawn from the Phase 1 posterior and 3,000 pairs of a Phase 1 cohort of $n_1$ patients and a Phase 3 cohort of 217 patients were generated. The Monte Carlo error of the simulations was not quantified.

## Results

### Correspondence between training and holdout

Figure 1 shows when the information became public and how it is used here. Table 1 sets the training and holdout numbers side by side with the differences in their definitions.

![A timeline from June 2025 to August 2026 showing the Phase 1 data cutoff, the 8-K disclosure, the training cutoff, the Phase 3 data cutoff, the ASCO presentation and the FDA approval.](shared/daraxonrasib-phase1-phase3-information/figures/fig1_timeline.png)

Figure 1. When the information became public. Blue is the information through the end of 2025 used for training; orange is the holdout and post-cutoff material. The ASCO (American Society of Clinical Oncology) marker is placed at the date of the OncLive article (31 May 2026) ([3](#ref-3)). The date of the FDA approval (26 August 2026) is from the FDA page ([5](#ref-5)).

Table 1. Inputs for training (Phase 1) and holdout (Phase 3, daraxonrasib arm in the RAS G12 population).

| Item | Phase 1 (training) | Phase 3, RAS G12 (holdout) |
|---|---|---|
| Population | RAS G12X, 2L, 300 mg once daily, "2L efficacy evaluable" (undefined) | RAS G12, after one prior line ([5](#ref-5)), 300 mg once daily, randomized n = 228 |
| ORR | 35% (9/26) | 33.2% (72/217, count back-calculated) |
| Median PFS, months | 8.5 (6.7–10.5) | 7.3 (6.3–8.1) |
| Median OS, months | 13.1 (10.9–NE) | 13.2 (10.0–NE) |
| Median follow-up, months | 16.7 (range 10.3–24.6) | 8.5 (range 3.2–15.9), whole trial |
| Control-arm ORR (not usable in 2025) | Not applicable | 11.8% (evaluable n = 221) |
| ORR definition | RECIST v1.1, confirmed or potentially confirmable | Not stated in the sources read |
| ORR assessor | Not stated | Not stated in the sources read |
| Data cutoff | 2025-06-30 | 2026-02-10 |
| Sources | [1](#ref-1) | [2](#ref-2), [3](#ref-3), [5](#ref-5) |

Note: ORR, objective response rate; PFS, progression-free survival; OS, overall survival; NE, not estimable; 2L, second line; RECIST, Response Evaluation Criteria in Solid Tumors.

### Prediction of the response rate

Figure 2 shows the predictive distributions at $\tau = 0$ and 0.5 with the observed value. Figure 3 shows the predictive intervals and log predictive scores of all models. Table 2 gives the numbers.

![The predictive distribution of the Phase 3 ORR: two curves for the shift between trials τ = 0 and 0.5, and a vertical line at the observed 33.2%.](shared/daraxonrasib-phase1-phase3-information/figures/fig2_orr_predictive.png)

Figure 2. The distribution of the Phase 3 ORR predicted from the Phase 1 value of 9/26 (Jeffreys prior). Blue is τ = 0 and red is τ = 0.5. The vertical axis is the predictive probability per percentage point. The observed count of 72/217 for 33.2% is back-calculated.

![Predictive intervals at 50, 80 and 95% for each model (left) and the difference in log predictive score from the weak reference (b) (right).](shared/daraxonrasib-phase1-phase3-information/figures/fig3_orr_scenarios.png)

Figure 3. Predictive intervals and log predictive scores (observed 72/217). Blue is the Phase 1-informed models (by τ) and orange is benchmarks (a)–(c). Left: 50% (thick), 80% (medium) and 95% (thin) predictive intervals; the dashed line is the observed value. Right: the score difference from the weak reference (b), in nats (larger is better).

Table 2. Prediction of the Phase 3 ORR (observed 72/217; `analysis/01_orr_prediction.py`).

| Model | Mean ORR | 95% predictive interval | Predictive probability of 72 | Log score | PIT |
|---|---|---|---|---|---|
| Phase 1-informed, tau = 0 | 35.2% | 17.5–54.8% | 0.019 | −3.98 | 0.43 |
| Phase 1-informed, tau = 0.25 | 35.4% | 16.1–58.1% | 0.016 | −4.11 | 0.44 |
| Phase 1-informed, tau = 0.5 | 35.9% | 12.0–65.9% | 0.012 | −4.39 | 0.46 |
| Phase 1-informed, tau = 0.75 | 36.6% | 8.3–74.2% | 0.010 | −4.65 | 0.47 |
| (a) Point extrapolation 9/26 | 34.6% | 28.6–41.0% | 0.052 | −2.96 | 0.33 |
| (b) Weak reference Beta(0.5, 0.5) | 50.0% | 0–100% | 0.003 | −5.77 | 0.39 |
| (c) Any-RAS cohort 11/38 | 29.5% | 15.2–45.6% | 0.020 | −3.94 | 0.69 |

Note: tau, shift between trials (logit scale); log score, natural logarithm of the predictive probability of the observed count (nats; larger is better); PIT, probability integral transform (midpoint version; 0.5 means the centre of the prediction). The 80% predictive interval is shown in Figure 3.

The posterior of the Phase 1 ORR (Jeffreys) has a mean of 35.2% and a 95% credible interval of 18.7–53.7%. The Phase 3 observation lay inside both the 95% and the 80% predictive intervals (Figure 3) of every model that used Phase 1, and the PIT of 0.43–0.47 put it near the centre of the prediction. Relative to the weak reference (b), the log predictive score was 1.80 nats better at $\tau = 0$, 1.66 nats at $\tau = 0.25$, 1.39 nats at $\tau = 0.5$ and 1.12 nats at $\tau = 0.75$. The point extrapolation (a) was 2.82 nats better and had the highest score; (c) was 1.84 nats better.

Using 228 patients as the denominator (76 responders) lowered the log predictive scores by only about 0.05 nats and did not change the conclusion. With a Beta(1,1) prior the log predictive scores were −3.97 at $\tau = 0$ and −4.38 at $\tau = 0.5$, similar to Jeffreys.

The point extrapolation (a) scored highest because this single observation was close to 9/26. Whether the observation is close because the shift between trials $\tau$ is small or by chance cannot be distinguished from one pair. Repeated-pair simulations were therefore run with two assumed true values of $\tau$ (both are assumptions, not the actual $\tau$; the $\tau = 0$ simulation was added after the first results were seen). In each pair the true $p_1$ was drawn from the Phase 1 posterior, and a Phase 1 cohort of $n_1$ patients and a Phase 3 cohort of 217 patients were generated, 3,000 pairs each. With a true $\tau$ of 0.5, the 95% interval of (a) covered the truth in 33.5% of pairs at $n_1 = 26$ and 41.1% at $n_1 = 104$ (mean log predictive score −11.2 and −9.2); the prediction that allowed for $\tau = 0.5$ had coverage of 94.7–95.6% (−4.88 and −4.67), and the prediction that assumed $\tau = 0$ fell from 81.1% at $n_1 = 26$ to 64.1% at $n_1 = 104$. With a true $\tau$ of 0, (a) covered 48.1% at $n_1 = 26$ and 73.6% at $n_1 = 104$ (−7.40 and −4.43), the prediction that assumed $\tau = 0$ had 94.5–95.4% (−4.45 and −3.92), and the prediction that allowed for $\tau = 0.5$ had 99.6–100% (−4.60 and −4.30). Under either true $\tau$, (a) had the lowest coverage and the lowest mean score. That (a) was best on this one pair does not show that (a) is a good predictor.

### Median survival

Figure 4 and Table 3 show the predictive intervals for median survival and the observed values.

![Predictive intervals for the median PFS (left) and median OS (right) at each shift between trials τ, with vertical lines at the observed Phase 3 medians.](shared/daraxonrasib-phase1-phase3-information/figures/fig4_survival_medians.png)

Figure 4. Predictive intervals for the Phase 3 medians (95% predictive interval including the observation error of the observed median; log axis). Dark blue uses the standard error recovered from the confidence interval (lower bound only for OS) and light blue uses twice that value. The dashed vertical line is the observed median. τ is the shift between trials on the log-median scale.

Table 3. Check of median survival (`analysis/02_survival_medians.py`).

| Endpoint | Phase 1 median (months) | Phase 3 observed (months) | tau | 95% predictive interval for the observed median | z | PIT |
|---|---|---|---|---|---|---|
| PFS | 8.5 (6.7–10.5) | 7.3 (6.3–8.1) | 0 | 6.6–11.0 | −1.16 | 0.12 |
| PFS | | | 0.5 | 3.1–23.4 | −0.29 | 0.38 |
| PFS, se × 2 | | | 0 | 5.1–14.2 | −0.58 | 0.28 |
| OS | 13.1 (10.9–NE) | 13.2 (10.0–NE) | 0 | 9.4–18.3 | 0.05 | 0.52 |
| OS, se × 2 | | | 0 | 6.7–25.5 | 0.02 | 0.51 |
| OS | | | 0.5 | 4.7–36.9 | 0.01 | 0.51 |

Note: se, standard error of the log median recovered from the reported confidence interval; z, the observed log median minus the predicted log median, divided by the predictive standard deviation; PIT, normal cumulative probability of z. Phase 1 values in parentheses are the 95% confidence intervals reported in the 8-K.

The observed Phase 3 median PFS of 7.3 months was 0.86 times the Phase 1 value of 8.5 months and lay toward the lower side (PIT 0.12) of the 95% predictive interval at $\tau = 0$ (6.6–11.0 months). With the standard error doubled the interval widened to 5.1–14.2 months and the PIT was 0.28. The observed OS of 13.2 months was 1.01 times the Phase 1 value of 13.1 months. The z of OS was 0.01–0.05 under every setting of the standard error and $\tau$, so the observed value falls inside the interval whatever its width; the OS check is close to a trivial pass. The median follow-up in Phase 3 was 8.5 months, about half of the 16.7 months in Phase 1, so the Phase 3 median OS may depend on a few events in the later part of the curve. Recovering the standard error from a confidence interval whose upper bound is NE is also an uncertain assumption, so the OS check is weak.

### Information value

Figure 5 shows the width of the predictive interval and the probability of a "proceed" call against Phase 1 cohort size. Table 4 gives the call for the actual 9/26.

![Left: the width of the 95% predictive interval for the Phase 3 ORR against Phase 1 cohort size at τ = 0 and 0.5. Right: the probability of a proceed call at thresholds of 20% and 25%.](shared/daraxonrasib-phase1-phase3-information/figures/fig5_information_value.png)

Figure 5. Phase 1 cohort size and information. Left (true ORR 0.35): the expected width of the 95% predictive interval for the true Phase 3 ORR. Blue is τ = 0, red is τ = 0.5, and the dotted line is the width at τ = 0.5 as $n_1\to\infty$ (41.8 percentage points). Right: the probability of a proceed call under "proceed if $P(p>T)\ge0.8$". Colours are the true ORR (grey 0.25, orange 0.30, blue 0.35); solid lines are the threshold $T=25\%$ and dashed lines $T=20\%$. The thresholds are arbitrary.

The true ORR of 0.35 in the left panel was chosen after the fact as a value close to the observed 9/26; the results for 0.20–0.40 are in the distributed tables (`info_value_widths.csv`, `info_value_proceed.csv`). Increasing $n_1$ from 26 to 104 narrowed the width from 34.4 to 18.0 percentage points at $\tau = 0$, but only from 51.4 to 44.6 points at $\tau = 0.5$. Even with the Phase 1 ORR known exactly ($n_1\to\infty$), the width at $\tau = 0.5$ stopped at 41.8 points (16.6–58.4%). The floor widths at $\tau$ of 0.25 and 0.75 were 21.9 and 58.8 points.

For a threshold of 25% and a true ORR of 0.30, the probability of a proceed call was 0.37 at $n_1 = 26$, 0.50 at 52 and 0.64 at 104; for a true ORR of 0.35 it was 0.59, 0.78 and 0.93. When the true ORR was 0.25 (equal to the threshold) it barely changed, from 0.18 to 0.21. This call is a rule about the Phase 1 $p_1$, not the Phase 3 $p_3$, and it does not involve $\tau$.

Table 4. Calls for the actual Phase 1 result (9/26) under "proceed if $P(p>T)\ge0.8$".

| Threshold T | P(p > T given 9/26) | Proceed at 0.8 |
|---|---|---|
| 15% | 0.994 | Yes |
| 20% | 0.962 | Yes |
| 25% | 0.870 | Yes |
| 30% | 0.703 | No |

### Mechanistic inputs and their public status by the end of 2025

No mechanistic model (tumour dynamics or mechanistic PK/PD) was fitted. Table 5 sorts the main inputs of such a model by whether they were described in material public by the end of 2025, within the material read.

Table 5. Inputs of a mechanistic model and their public status by the end of 2025 (within the material read).

| Quantity | Described in material public by 2025-12-31? | Source and status |
|---|---|---|
| Preclinical PK/PD in mice (tumour exposure, DUSP6 inhibition, stasis threshold 158 nM in mice, about 80 nM human-equivalent) | Yes (2024 paper) | Cancer Discovery 2024 ([8](#ref-8)); the numbers come via an earlier article ([9](#ref-9)); the paper was not re-read here |
| Human population PK parameters | Not in the 8-K | Reported in the FDA review (2026, after the cutoff) ([9](#ref-9)) |
| Exposure–response for efficacy in patients | Not in the 8-K | FDA review (after the cutoff): no significant efficacy relation among patients at 300 mg ([9](#ref-9)) |
| Longitudinal tumour size per patient | Not found; the 8-K has a best-percentage-change plot as an image only | 8-K figure; not read |
| Tumour growth and resistance rates | Not found in the material read | Would need longitudinal lesion data |
| Target engagement in patients | Not found in the 8-K | Other public material was not searched |

Note: PK/PD, pharmacokinetics and pharmacodynamics; DUSP6, a downstream marker gene of RAS/MAPK signalling.

## Discussion

Predicting the Phase 3 ORR from the 26 Phase 1 patients, the observed value fell near the centre of the predictive interval. Calling this a successful prediction needs a condition. That the observation was close to the Phase 1 point estimate (34.6%) and had a PIT of 0.43–0.47 is a fact about one pair of observations. Whether the shift between trials $\tau$ is small or large cannot be distinguished from this one pair. That the point extrapolation scored highest on one pair does not separate chance closeness from a small $\tau$. In the repeated simulations the point extrapolation had the lowest coverage whether the true $\tau$ was 0 or 0.5, and at $n_1 = 26$ the sampling error of Phase 1 is not negligible. These simulations, however, assume the value of $\tau$.

That the observed value falls inside a 95% predictive interval of 17.5–54.8% is almost expected, because the interval is about 37 points wide; the word "narrowed" has to be read together with that width. That the observed value also fell inside the 80% interval is no stronger a confirmation, for the same reason. The log predictive score of benchmark (c), which uses the 11/38 of the overall RAS-mutant cohort, was almost the same as G12X at $\tau = 0$ (−3.94 versus −3.98), so the information value of restricting to G12X cannot be read from this one pair.

The value of enlarging the cohort differs between interval width and the call. Under $\tau = 0.5$, quadrupling Phase 1 barely narrows the predictive interval for the Phase 3 ORR. The width is set not by the Phase 1 sample size but by the shift between trials. When the true ORR is near the threshold (0.30 against a threshold of 25%), the probability of a proceed call rose from 0.37 to 0.64. This value depends on the threshold, the rule and the assumed true ORR (shown mainly around 0.30–0.35, close to the observation), and it barely changed when the true ORR equalled the threshold at 0.25 (0.18 to 0.21). It is a result within this frame and does not show a general value of adding patients to a Phase 1 cohort.

An actual decision involves another question. What Phase 1 would have needed to show is whether the ORR is higher than with chemotherapy. The control-arm ORR learned afterwards was 11.8% ([3](#ref-3)), but this number was not available in 2025, and the difference from the control arm was not modelled here. The thresholds of 15–25% are retrospective scenarios.

As for mechanistic models, within the material read, no input public by the end of 2025 from which to estimate patient-level tumour dynamics or exposure–response was found (Table 5). The population PK coefficients in the 2026 FDA review and the statement that the efficacy exposure–response was not significant ([9](#ref-9)) are information that became available later. This describes the range of material read and does not deny the value of mechanistic models in general.

## Limitations

- This is a retrospective check made after the result was known, not a blinded prediction. No record shows that the models and benchmarks were fixed before running; benchmarks (b) and (c), the sensitivity analyses and the repeated-pair simulation were added after the first results were seen. The training cutoff (end of 2025) and the treatment of the Phase 1 paper as post hoc material are also retrospective choices.
- The Phase 1 ORR counts responses that were confirmed or still potentially confirmable, and the Phase 3 response definition and assessor are not stated in the sources read. If Phase 3 counts confirmed responses only, the Phase 1 ORR is the more inclusive of the two, a difference that points to a higher Phase 1 value; this was not adjusted. The 2L efficacy-evaluable group may also be a post hoc subset, which could likewise raise the ORR.
- The favourable Phase 1 result drove the decision to proceed to Phase 3, and a selected favourable result may regress toward the mean in the next trial (winner's curse). The model here, with mean 0 for $\delta$, does not include this, and a shift in the negative direction is entirely possible.
- Phase 1 is a single-arm expansion cohort (the definition of 2L efficacy evaluable is unclear) ([1](#ref-1)), and Phase 3 is a randomized trial after one prior line ([5](#ref-5)), with different follow-up (16.7 versus 8.5 months), response definitions and evaluable sets.
- The Phase 3 G12 population values come from a secondary report ([3](#ref-3)). The full text of the NEJM paper could not be retrieved. The 72 responders are back-calculated from a reported percentage and an evaluable count of 217, they are not a reported number, and 217 itself rests on one report. The 76/228 case is an approximation that does not match the reported rounding.
- The shift between trials $\tau$ cannot be estimated from these data and was placed as scenarios. The width of the conclusions depends on $\tau$. $\tau = 0.5$ is an example and not an estimate of the real value. The $\tau$ for survival is on a different scale from that for the ORR.
- Survival uses an approximation that recovers standard errors from summary values, and depends on the confidence interval being symmetric on the log scale and on the upper bound of OS being NE. An event-count standard error is likely to be larger, so the doubled-standard-error sensitivity analysis is reported alongside. The Phase 3 median OS rests on immature follow-up.
- The thresholds and the 0.8 in the proceed-call simulation are arbitrary. The true $p_1$ in the repeated-pair simulation is drawn from the Phase 1 posterior and is not a real distribution. The Monte Carlo error of the simulations (4,000 draws per condition, 3,000 pairs) was not quantified.
- No mechanistic model was fitted. Table 5 reflects the public status within the material read, and other public sources were not searched.

## Conclusion

To the QOI (how far the 26-patient second-line Phase 1 cohort constrained the Phase 3 response rate and survival in the RAS G12 population), the public data support the following. For the ORR, the 95% predictive interval was 17.5–54.8% with no allowance for a shift between trials ($\tau = 0$) and 12.0–65.9% with one ($\tau = 0.5$), and the observed 33.2% was inside; because the interval is wide, this is not a strong confirmation. The observed medians of PFS and OS were also inside their predictive intervals, but given the doubled-standard-error sensitivity analysis and the short Phase 3 follow-up, the OS check is close to a trivial pass. Increasing the cohort from 26 to 104 patients barely narrowed the $\tau = 0.5$ predictive interval. This is a check made after the result was known and is not read as proof of predictive ability.

## Data and code availability

The materials needed to re-run the analysis (the `analysis/` scripts, the `inputs/` CSV files with the provenance record, and the `outputs/` tables, figures and logs) are included in the [companion archive](shared/daraxonrasib-phase1-phase3-information/daraxonrasib-phase1-phase3-information-companion.zip). The inputs are values transcribed from the 8-K ([1](#ref-1)) and the news report ([3](#ref-3)). To re-run: `python analysis/01_orr_prediction.py && python analysis/02_survival_medians.py && python analysis/03_information_value.py && python analysis/04_figures.py` (Windows 11, Python 3.12.4, numpy 2.2.6, pandas 2.2.2, scipy 1.14.0, matplotlib 3.9.1). The random seed is 20261110; the predictive distribution of the ORR uses no random numbers. `03_information_value.py` takes a few minutes to run.

## References

<span id="ref-1"></span>1. Revolution Medicines, Inc. Form 8-K: current report, daraxonrasib clinical data in pancreatic cancer [Internet]. U.S. Securities and Exchange Commission; 2025 Sep 10 [cited 2026 Nov 10]. Available from: [https://www.sec.gov/Archives/edgar/data/1628171/000119312525200078/d947102d8k.htm](https://www.sec.gov/Archives/edgar/data/1628171/000119312525200078/d947102d8k.htm). Read as text; the waterfall and survival figures are images and were not read.

<span id="ref-2"></span>2. O'Reilly EM, Wainberg ZA, Hendifar AE, Borad MJ, Pietrantonio F, Pant S, et al. Daraxonrasib or chemotherapy in previously treated metastatic pancreatic cancer. N Engl J Med. 2026;395(4):325–337. [doi:10.1056/NEJMoa2605555](https://doi.org/10.1056/NEJMoa2605555). Abstract level only; the full text was not available.

<span id="ref-3"></span>3. OncLive. Daraxonrasib meets all primary and key secondary efficacy end points in pretreated PDAC [Internet]. 2026 May 31 [cited 2026 Nov 10]. Secondary report of the ASCO 2026 presentation. Available from: [https://www.onclive.com/view/daraxonrasib-meets-all-primary-key-secondary-efficacy-end-points-in-pretreated-pdac](https://www.onclive.com/view/daraxonrasib-meets-all-primary-key-secondary-efficacy-end-points-in-pretreated-pdac)

<span id="ref-4"></span>4. Wolpin BM, Park W, Garrido-Laguna I, Spira A, Starodub A, Sommerhalder D, et al. Daraxonrasib in previously treated advanced RAS-mutated pancreatic cancer. N Engl J Med. 2026;394(18):1790–1802. [doi:10.1056/NEJMoa2505783](https://doi.org/10.1056/NEJMoa2505783). Abstract level only.

<span id="ref-5"></span>5. U.S. Food and Drug Administration. FDA approves daraxonrasib for metastatic pancreatic adenocarcinoma [Internet]. FDA; 2026 [cited 2026 Nov 10]. States the approval date (2026 Aug 26) and the RASolute 302 population (progression after one prior line); overall-population results only. Available from: [https://www.fda.gov/drugs/cancer-approvals/fda-approves-daraxonrasib-metastatic-pancreatic-adenocarcinoma](https://www.fda.gov/drugs/cancer-approvals/fda-approves-daraxonrasib-metastatic-pancreatic-adenocarcinoma)

<span id="ref-6"></span>6. Gneiting T, Raftery AE. Strictly proper scoring rules, prediction, and estimation. J Am Stat Assoc. 2007;102(477):359–378. [doi:10.1198/016214506000001437](https://doi.org/10.1198/016214506000001437)

<span id="ref-7"></span>7. Czado C, Gneiting T, Held L. Predictive model assessment for count data. Biometrics. 2009;65(4):1254–1261. [doi:10.1111/j.1541-0420.2009.01191.x](https://doi.org/10.1111/j.1541-0420.2009.01191.x)

<span id="ref-8"></span>8. Jiang J, Jiang L, Maldonato BJ, Wang Y, Holderfield M, Aronchik I, et al. Translational and therapeutic evaluation of RAS-GTP inhibition by RMC-6236 in RAS-driven cancers. Cancer Discov. 2024;14(6):994–1017. [doi:10.1158/2159-8290.CD-24-0027](https://doi.org/10.1158/2159-8290.CD-24-0027). Not re-read for this article.

<span id="ref-9"></span>9. Kumakura D. Recomputing daraxonrasib 300 mg target-inhibition predictions from FDA-published values [Internet]. Daiki Kumakura; 2026 Nov 22. Available from: [daraxonrasib-target-en.html](daraxonrasib-target-en.html). It summarizes the FDA multi-discipline review of NDA 220910 (2026), which is after the training cutoff.
