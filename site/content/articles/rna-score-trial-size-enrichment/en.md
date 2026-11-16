**QOI: Suppose the published POPLAR result for an RNA foundation-model patient score (12-month progression-free survival by score half and arm) holds. How much does that score reduce the number of patients a confirmatory trial needs, and through which route: prognostic adjustment, enrichment, or an interaction test?**

**COU: To read the claim that "an AI score can make clinical trials smaller" by separating the design types and their assumptions. This is not a performance evaluation of Ladon and not advice on any particular trial plan.**

QOI (question of interest) is the question this article answers, and COU (context of use) is what the answer is used for.

**Answer: if the four published percentages hold, the reduction comes mainly from enrichment (enrolling only high-score patients), not from prognostic adjustment. Enrichment is also a design that restricts the claim being tested to the effect in the high-score group.** For a difference in 12-month progression-free survival (PFS12) at 80% power, the all-comers design needs 3,305 patients, the analysis adjusted for the score needs 3,220 (2.6% fewer), and the design that randomises only high-score patients needs 258 (516 patients tested for the score). The size and the meaning of the enrichment effect differ from those of adjustment. The conclusion depends strongly on the assumption that the four percentages were estimated from samples of about 48 patients per cell. With that sampling error included (Beta draws with a uniform prior), the enriched design's required number is 284 at the median, but exceeds 800 with probability one in four. If the positive predictive value (the share of called-positive patients who truly belong to the high-benefit group) falls below about 0.57, or if the effect in the high-score group shrinks to about 0.365 of the published value (5.1 points), the number tested for the score exceeds the all-comers sample size. For a control PFS12 of 0.14 and a 10-point difference, prognostic adjustment alone needs a score with a within-arm AUC (area under the receiver operating characteristic curve) of about 0.80 to 0.86 to cut 20 to 30%.

Abbreviations and symbols: PFS12 is progression-free survival at 12 months (alive and progression-free at that time), ATEZO is atezolizumab, DOCE is docetaxel, AUC is the area under the receiver operating characteristic curve, AUROC is the name for the same measure when used as predictive performance, OR is the odds ratio, $H$ and $L$ are the high-score and low-score groups, EMA is the European Medicines Agency, CHMP is its Committee for Medicinal Products for Human Use, and FDA is the U.S. Food and Drug Administration. $\delta$ is the difference in PFS12 (experimental minus control), in percentage points ("points" below; pp in tables). The positive predictive value (PPV) is the share of called-positive patients who truly belong to the high-benefit group.

## Introduction

The technical report on Ladon, an RNA foundation model from Blank Bio, states that it predicts patient outcome and treatment response from RNA expression ([1](#ref-1), [2](#ref-2)), and names "smaller, more efficient trials" as a goal ([1](#ref-1)). The report text, however, contains no power or sample-size calculation ([1](#ref-1)).

The report applies a score that represents differences in treatment effect to the POPLAR trial, a randomised phase 2 trial of atezolizumab versus docetaxel in previously treated non-small-cell lung cancer (144 patients randomised to atezolizumab, 143 to docetaxel) ([3](#ref-3)). The score was trained on five other trials, including OAK ([4](#ref-4)) ([1](#ref-1)). In the report text, 28% of atezolizumab-treated patients with high scores and 6% of those with low scores were progression-free at 12 months. In the docetaxel arm the figures were 14% and 13%, nearly the same ([1](#ref-1)). These four percentages are called the "anchors" below.

A score can change the size of a trial through at least three routes. The first is adjusting for prognostic covariates to improve precision; the U.S. FDA guidance has the efficiency gain from prognostic covariates as its main subject ([5](#ref-5)). PROCOVA, on which the EMA's CHMP issued a qualification opinion, is a linear adjustment using a prognostic score built from historical control data, and it applies to continuous outcomes ([6](#ref-6)). In a study of linear adjustment, prognostic models explaining a clinically realistic share of the variance were reported to reduce sample size by 10 to 30% ([7](#ref-7)). For binary outcomes, averaging the covariate-adjusted estimate over the covariates gives a marginal effect, and adjustment can then raise efficiency ([8](#ref-8)). The second route is enrichment, which enrols only patients expected to benefit; an FDA guidance exists ([9](#ref-9)). Simon and Maitournam derived formulas comparing enriched and all-comers designs in both the number randomised and the number screened ([10](#ref-10), [11](#ref-11)). The third route is a trial that tests the score-by-treatment interaction; detecting an interaction of the same size as the overall effect with the same power is said to need four times the sample size ([12](#ref-12)). The PATH statement distinguishes risk modelling (using a predicted risk to stratify treatment effect) from effect modelling (building treatment interactions into the prediction model) ([13](#ref-13)).

Each of these results comes from a different population and setting. This article puts the anchors, an actual set of published numbers, into the three routes, puts them on one scale, and computes how much each moves the sample size and how uncertain the numbers are. It does not propose a new statistical method; it applies known formulas.

## Methods

### Input: four percentages and assumptions

The only inputs are four percentages and one count read from the text of the Ladon technical report (retrieved 14 November 2026; the original figure was not viewed). PFS12 is 0.28 for the high-score group and 0.06 for the low-score group in the ATEZO arm, and 0.14 and 0.13 in the DOCE arm ([1](#ref-1)). The score threshold is the median over all 192 patients with RNA measurements, shared by the two arms ([1](#ref-1)). The share of the high group was therefore set to 0.5.

The report text does not give the number of patients in each of the four groups, confidence intervals or test results. It states that the POPLAR RNA-profiled subset has 192 patients and that a figure includes 87 of the 95 ATEZO-treated patients with an evaluable response, but it could not be confirmed whether the latter is the denominator of the PFS12 figure ([1](#ref-1)). Each cell was therefore assumed to hold $192/4=48$ patients, and 24 to 96 were also tried. This assumption is an input of this article, not a value from the report.

### Endpoint and designs

The endpoint is binary: progression-free or not at 12 months, assuming that every patient is followed for 12 months so that the status is known (the effect of censoring is evaluated separately below). The estimand is the marginal risk difference in PFS12 in the analysed population, $\delta=p_1-p_0$ ($p_1$ and $p_0$ are PFS12 in the experimental and control arms). The two-sided significance level is 5%, power 80%, allocation 1:1, and the normal approximation was used. Let $z=z_{0.975}+z_{0.8}$.

D1 (all-comers, unadjusted) needs, from the standard error of the difference of two proportions, the following number per arm.

$$n_{\mathrm{arm}}=\frac{z^2\,[\,p_1(1-p_1)+p_0(1-p_0)\,]}{\delta^2}\tag{1}$$

D2 (all-comers, adjusted for the score) estimates the proportions within each score group and averages over the score distribution to obtain the marginal effect, which corresponds to the procedure of averaging the covariate-adjusted estimate over the covariates to obtain the marginal effect ([8](#ref-8), [14](#ref-14)). The composition of the score groups is random from sample to sample, and the averaging weights are the observed shares. With $S$ the score group ($H$ or $L$) and $p_a(S)$ the PFS12 by score group, the variance coefficient per arm is

$$V_{\mathrm{adj}}=\mathrm{E}_S\bigl[p_1(S)(1-p_1(S))\bigr]+\mathrm{E}_S\bigl[p_0(S)(1-p_0(S))\bigr]+\tfrac12\,\mathrm{Var}_S\bigl(p_1(S)-p_0(S)\bigr)\tag{2}$$

Its difference from the bracket of Equation (1) ($V_{\mathrm{unadj}}$) is $\mathrm{Var}_S(p_1)+\mathrm{Var}_S(p_0)-\tfrac12\mathrm{Var}_S(p_1-p_0)$. The last term expresses that when the treatment effect varies with the score (an interaction), the variance of the averaging step that produces the marginal effect eats into the precision gained. The term vanishes if the weights used to average over score groups are fixed in advance. Stratified randomisation balances treatment within score groups but does not itself fix the relative sizes of those groups.

D3 (all-comers, test of the interaction) tests the interaction contrast $\psi=(p_{H1}-p_{H0})-(p_{L1}-p_{L0})$ with patients allocated equally to the four cells. The total sample size is

$$N_{\mathrm{int}}=\frac{4\,z^2\,\sum_{\text{4 cells}}p(1-p)}{\psi^2}\tag{3}$$

D4 (enrichment, high-score group only, unadjusted) applies Equation (1) to the two proportions of the high group. The number tested (screened) is the number randomised divided by the share of the high group $\pi$ and the assay success rate $1-f$.

### Uncertainty and sensitivity

The sampling error of the four proportions was propagated by drawing 200,000 times from independent Beta distributions (uniform prior; proportion times number of patients taken as the event count, kept non-integer). Cell sizes of 24, 36, 48, 72 and 96 were tried. Besides the uniform prior, a Jeffreys prior (adding 0.5) and event counts rounded to integers (13, 3, 7 and 6) were also drawn. The following were then varied and the required numbers recalculated: (a) the PPV $\rho$ lowered from 1 to 0.5 ($\rho=1$ is the published high group itself; $\rho=0.5$ means the score carries no information, and enrichment and all-comers give the same contrast; wrongly included patients are given the low-group proportions); (b) the factor by which the effect in the high group shrinks from 14 percentage points; (c) the share of patients called positive; and (d) the assay failure rate.

The effect of purely prognostic adjustment was swept under a separate setup. The score $S$ is standard normal, the logit of PFS12 is $\alpha_a+\gamma S$ (the same slope in both arms, no interaction), the marginal PFS12 is 0.14 in the control arm and 0.24 in the experimental arm (a 10-point difference). With $\gamma$ moved from 0 to 3, the within-arm AUC and the ratio of required sample sizes were computed by numerical integration (Gauss–Hermite, 200 nodes).

### Checks

The sample sizes of D1 and D4 (Equation (1)) were also checked with the power function of a statistics library (statsmodels; a test that pools the variance under the null). The sample sizes of D2 (Equation (2)) and D3 (Equation (3)) were not checked with this library. For all four designs, Monte Carlo simulation with binomial cell counts (40,000 runs each; sample sizes rounded up per cell, 3,306 for D1 and 352 for D3) checked power, the type I error rate under the null, and the coverage of the 95% interval. The prognostic-adjustment formula was checked by running the standardised logistic-regression estimator in 20,000 trials and comparing the variances. The effect of censoring was evaluated with Kaplan–Meier estimation of PFS12, with exponential event times and 10% or 20% of patients dropping out before 12 months, 6,000 runs each. All of these are checks by code the same author wrote after the derivation; they are neither blinded nor pre-registered.

## Results

### Required patients by design

Table 1 gives the sample sizes if the anchors hold. The average effect in the all-comers population is only 3.5 points (when the high group's share is 0.5). Groups with opposite directions cancel: $+14$ points in the high group ($0.28$ versus $0.14$) and $-7$ points in the low group ($0.06$ versus $0.13$). The all-comers design therefore needs 3,305 patients (Figure 1a).

Table 1. Patients needed to detect the PFS12 difference at the anchors with 80% power. Randomised is the total over both arms (not per arm). The 350 patients for D3 give the specified power for the interaction contrast. Power for the treatment effect in the high group is a separate question.

| Design | Effect used (pp of PFS12) | Randomised | Screened for the score |
|---|---|---|---|
| D1 all-comers, unadjusted | 3.5 | 3,305 | 3,305 (no score needed) |
| D2 all-comers, adjusted for score | 3.5 | 3,220 | 3,220 |
| D3 all-comers, interaction test | 21.0 (contrast) | 350 | 350 |
| D4 enriched (high score) | 14.0 | 258 | 516 |

![Required patients by design (a) and the distribution of required patients when the sampling error of the four proportions is included (b).](shared/rna-score-trial-size-enrichment/figures/fig1_designs_and_uncertainty.png)

Figure 1. Required patients by design (a, log axis) and the distribution of required patients with sampling error included, assuming 48 patients per cell (b; the first 20,000 draws are plotted, and the median and the probability of never reaching power in the legend are from all 200,000).

D2, adjusted for the score, needs only 2.6% (85 patients) fewer than D1. In the decomposition of Equation (2), the anchors give $\mathrm{Var}_S(p_1)=0.0121$, $\mathrm{Var}_S(p_0)=0.000025$ and $\mathrm{Var}_S(p_1-p_0)=0.0110$, so the interaction removes somewhat under half (45%) of the prognostic explanatory power (the sum of the first two terms, 0.0121) through half of the last term (0.0055). D4 needs about 1/12.8 of D1 (258 patients), and about 1/6.4 counted as patients tested (516). The squared ratio of effects, $(14/3.5)^2=16$, is the ratio of randomised numbers under equal variances and is the simple case of the framework compared by Simon and Maitournam ([10](#ref-10), [11](#ref-11)) (only the abstracts were read, not their formula); the binary variance is larger in the high group, so the ratio here is smaller. D3 needs 350, about 0.11 times D1. The interaction contrast (21 points) is six times the overall effect (3.5 points), so the condition differs from the fourfold rule of Brookes et al., which is for an interaction of the same size as the overall effect ([12](#ref-12)).

The within-arm AUC of the score computed from the anchors (for the binary high/low split) is 0.69 in the ATEZO arm and 0.51 in the DOCE arm. A score that relates to outcome in the treated arm but not in the control arm has the pattern of a score for treatment-effect differences rather than a prognostic score.

### What prognostic adjustment saves

For a purely prognostic score, the reduction is set by the score's explanatory power (Table 2, Figure 2). A within-arm AUC of 0.70 gives about 8%, 0.75 about 13%, 0.83 about 23% and 0.88 about 33%, so a 20 to 30% reduction needs an AUC of about 0.80 to 0.86. This range is of the same order as the 10 to 30% reported for linear adjustment ([7](#ref-7)). The numbers are specific to the setting (control PFS12 0.14, a 10-point difference, a normally distributed score); a higher control PFS12 gives a larger reduction for the same AUC. The 2.6% at the anchors lies near the curve for purely prognostic scores when the AUC is taken as the mean of the two arms (0.60), but the two arise from different mechanisms (prognosis and interaction), so the agreement is coincidental. For a test of the conditional odds ratio in logistic regression under the same generating conditions, the reduction was about the same (rightmost column of Table 2; relative to a test of the unadjusted marginal odds ratio).

Table 2. Reduction in randomised patients for a purely prognostic score (control PFS12 0.14, experimental 0.24). OR in the rightmost column: a test of the conditional odds ratio compared with a test of the unadjusted marginal odds ratio.

| Logit slope gamma | Within-arm AUC (control) | Outcome variance explained (control) | Reduction, risk difference (%) | Reduction, conditional OR test (%) |
|---|---|---|---|---|
| 0.5 | 0.636 | 3.0% | 3.6 | 3.5 |
| 0.75 | 0.696 | 6.6% | 7.8 | 7.5 |
| 1.0 | 0.747 | 11.2% | 12.8 | 12.3 |
| 1.5 | 0.826 | 21.6% | 23.4 | 22.4 |
| 2.0 | 0.878 | 31.6% | 33.1 | 31.5 |
| 3.0 | 0.934 | 47.3% | 47.7 | 44.9 |

![Within-arm AUC of a purely prognostic score and the percentage reduction in required patients, with the position of the anchors.](shared/rna-score-trial-size-enrichment/figures/fig2_prognostic_adjustment.png)

Figure 2. Within-arm AUC of a purely prognostic score (the same logit slope in both arms) and the percentage reduction in randomised patients (standardised estimator, risk difference). The square is the value computed from the anchors (AUC taken as the mean of the two arms).

### Uncertainty of the four percentages

With 48 patients per cell, the sampling error of the four proportions alone gives a Beta-draw 90% interval of 3.5 to 36.9 points for the interaction contrast (21 points) (Table 3). The normal-approximation 95% interval is 1.2 to 40.8 points. The probabilities below are proportions of the Beta draws under the uniform prior. The probability that the effect in the high group (14 points) is zero or below is 4.9%, and the probability that the all-comers average effect is zero or below is 25.4%. With a Jeffreys prior these are 4.6% and 24.8%, and with event counts rounded to integers (13, 3, 7 and 6) 7.0% and 27.7%; the median required number for the enriched design was then 265 and 357, and the 75th percentile 738 and 1,211. In terms of required patients, the number randomised for the enriched (high-group-only) design is 71 at the 5th percentile, 284 at the median, 804 at the 75th percentile and about 5,600 at the 90th percentile, and the 95th percentile is not a meaningful value (about 5% of draws have a high-group effect near zero; "never reaching power" is defined in the direction of benefit). The all-comers median is 3,739, and its 75th percentile is not finite. The point estimate (258) is close to the median (284), but the upper end of the distribution extends extremely far.

Table 3. Uncertainty when the four proportions are drawn according to cell size (200,000 draws, Beta distributions, uniform prior). Probabilities are proportions of the draws.

| Patients per cell | Interaction contrast, 90% interval (pp) | P(high-group effect ≤ 0) | P(all-comers effect ≤ 0) | Enriched, randomised: median (5th percentile) |
|---|---|---|---|---|
| 24 | −4.3 to 43.3 | 12.7% | 32.4% | 307 (52) |
| 36 | 0.6 to 39.3 | 7.7% | 28.5% | 291 (62) |
| 48 | 3.5 to 36.9 | 4.9% | 25.4% | 284 (71) |
| 72 | 6.8 to 34.2 | 2.0% | 20.4% | 274 (84) |
| 96 | 8.8 to 32.4 | 0.9% | 17.1% | 271 (94) |

### How far the enriched design tolerates a degraded score

When the PPV $\rho$ falls from 1 to 0.9, 0.8, 0.7 and 0.6, the number randomised rises from 258 to 345, 489, 758 and 1,365, and the number tested from 516 to 690, 978, 1,517 and 2,729. At $\rho=0.5$ (no information) it returns to 3,305 (all-comers). The $\rho$ at which the number tested equals the all-comers number randomised (3,305) is 0.574 (a comparison that treats the cost of testing and of randomising as equal). When the effect in the high group shrinks to 0.75, 0.5 and 0.35 of 14 points, the number randomised is 435, 917 and 1,789 and the number tested 870, 1,834 and 3,579; the break-even is 0.365 times (5.1 points); at 0.36 times the number tested is 3,393 and at 0.37 times 3,222 (Figure 3).

![How the required patients of the enriched design change with purity of the positive call, shrinkage of the effect in the high group, and assay failure.](shared/rna-score-trial-size-enrichment/figures/fig3_enrichment_sensitivity.png)

Figure 3. Randomised and tested patients for the enriched (high-group-only) design. (a) PPV of the positive call, (b) shrinkage of the effect in the high group, (c) assay failure. The dashed line is the number randomised in the all-comers design at the anchors (3,305).

With the number randomised and the assay success rate held fixed, the number tested is inversely proportional to the share called positive. With shares of 0.2, 0.35, 0.5, 0.65 and 0.8, the number tested is 1,289, 737, 516, 397 and 322 (cell risks kept at the anchors). With assay failure of 10, 20, 30 and 40%, the number tested rises to 573, 645, 737 and 860. The all-comers average effect is a function of the high group's share $\pi$, $\delta(\pi)=0.21\pi-0.07$, which is zero at $\pi=1/3$. At a share of 0.35 the average effect is 0.35 points and the required number is about 300,000, and for $\pi<1/3$ the average effect is negative. The all-comers number changes extremely even when the high-score share departs only modestly from 0.5.

### Results of the checks

At the anchor sample sizes, the power in 40,000 Monte Carlo runs was 80.1% for D1, 79.3% for D2, 80.7% for D3 (352 patients) and 80.3% for D4, and the 95% interval coverage was 95.2%, 95.2%, 94.9% and 94.8% (the 79.3% of D2 was 79.9% in a separate 400,000-run check, which is taken as chance). Under the null (no effect, score prognostic), the type I error rate was 5.0 to 5.4% with 300 or more randomised patients and 5.7 to 5.9% with 100. The statistics library's power function gave 0.799 for D1 and 0.792 for D4. The prognostic-adjustment formula and the variance of the standardised logistic-regression estimator agreed within 2% over 20,000 trials (variance ratios 0.961 versus 0.964, 0.879 versus 0.873, and 0.677 versus 0.669).

With 10% dropping out before 12 months, the Kaplan–Meier estimate of PFS12 needs about 7% more patients (D4 from 258 to 276, D1 from 3,306 to 3,540), and with 20% about 15 to 16% more (298 and 3,818). The power at the increased sample sizes was 80.2 to 80.7% in every case.

## Discussion

If the anchors hold, enrichment is what moves the sample size. It does so not because the score is prognostic but because it expresses a difference in treatment effect (PFS12 separates only in the ATEZO arm). Adjusting for the same score cuts only 2.6%. The effect of prognostic adjustment grows with the score's explanatory power (Table 2), but cutting 20 to 30% needs, in this setting, a score with an AUC of about 0.80 to 0.86. An AUC alone does not determine the sample size. A score with a within-arm AUC around 0.7 saves about 8% if it is purely prognostic, but can give about 1/12.8 under enrichment if it expresses a difference in treatment effect. An AUC can be converted to a sample size only once the design, endpoint and control-arm proportion are fixed. The AUROC in the technical report is for response prediction and is not an input here.

The effect of enrichment is obtained by changing the estimand. D4 detects the effect in the high-score group, not the all-comers average (3.5 points). Patients in the low-score group (0.06 versus 0.13) are by design not enrolled. This is not a saving of patients but a change in the claim being tested. The comparison should be read as "a different claim with fewer patients", not "the same claim with fewer patients".

The uncertainty results show that the point-estimate numbers should not be used directly in planning. The sampling error of four proportions with 48 patients per cell alone gives a 4.9% probability that the high-group effect is zero or below, and a 25% probability that the required number exceeds 800. In a new trial the score threshold, population and assay will not match the report, and if the PPV $\rho$ falls below about 0.57 or the effect shrinks to about 0.365 of the published value, the number tested for enrichment exceeds the all-comers sample size (a comparison that treats the cost of testing and of randomising as equal). This break-even is the structure shown by Simon and Maitournam, in which the advantage of enrichment depends on the share of patients with an effect and the accuracy of the assay ([10](#ref-10), [11](#ref-11)), applied to these anchors. Novelty is not claimed.

The subject of the EMA's qualification opinion on PROCOVA is continuous outcomes, linear covariate adjustment and a score built from independent historical control data ([6](#ref-6)). The PFS12 here is binary, and the score's training data were from trials other than POPLAR (including OAK), but enrichment and interaction tests as design types are not within that framework. For the FDA adjustment guidance, only the web summary was read, and the guidance text was not ([5](#ref-5)).

## Limitations

- The four proportions are numbers read from the text of the technical report. The original figure was not viewed, and the number of patients per group and the confidence intervals are not reported. The 48 patients per cell is an assumption and affects every required number and probability. Whether the four proportions reached the figure through choices of threshold or display (a bias toward favourable values) cannot be assessed from the text.
- According to the technical report, the model of treatment-effect differences (the benefit head) was trained on five trials including OAK and applied to POPLAR. POPLAR is not part of that model's training, but the score threshold was set at the median of all 192 POPLAR patients, so the high/low split is in-sample for POPLAR. Whether POPLAR is in the encoder's pretraining data could not be confirmed from the text ([1](#ref-1)). This article did not re-evaluate the validity of the score. The report's methods describe a censoring-weighted logistic regression, but whether the four proportions come from that method or from Kaplan–Meier estimation could not be confirmed. These points bear on every conclusion that takes the four proportions as input.
- The endpoint is binary PFS12, assuming that every patient's 12-month status is known. Real trials often use time-to-event analysis (hazard ratio, log-rank test, restricted mean survival time), and the required sample size for those needs a separate calculation. The effect of dropout was evaluated only at 10% and 20%, assuming non-informative dropout. This bears on the absolute required numbers.
- The analysis uses a discrete score split into high and low. Choosing a threshold on a continuous score, re-tuning the threshold, and searching over several thresholds were not treated.
- Uncertainty covers only the sampling error of the four proportions, with independence assumed. A Jeffreys prior and rounding the event counts to integers were also tried (medians 265 and 357), but no other choices. Differences in population and assay in a new trial are represented by the sensitivity to $\rho$ and to shrinkage of the effect. The break-even treats the cost of testing and of randomising as equal. These bear on the conclusions about uncertainty and the break-even.
- The checks are by code the same author wrote after the derivation, not an independent implementation. There is no pre-registration.
- The sample sizes here are indices for comparing designs, not planned values for any particular trial.

## Conclusion

If the four 12-month PFS percentages from POPLAR hold, what moves the sample size substantially is enrichment (258 randomised and 516 tested, against 3,305 for all-comers, about 1/12.8 and 1/6.4). Prognostic adjustment gives 2.6%, and, for a control PFS12 of 0.14 and a 10-point difference, cutting 20 to 30% needs a score with a within-arm AUC of about 0.80 to 0.86. The sampling error of the four proportions alone, however, gives the enriched design a median of 284 required patients against 804 at the 75th percentile, and a 4.9% probability that the effect is zero or below, and if the PPV of the score falls below about 0.57 or the effect shrinks to about 0.365 of the published value, the number tested exceeds the all-comers sample size. The claim enrichment tests is limited to the effect in the high-score group. The claim that "a score can make trials smaller" holds once it is settled which design, which estimand, and under which uncertainty.

## Data and code availability

The material for re-running (the scripts in `analysis/`, the tables, figures and logs in `outputs/`, the hash list `MANIFEST_SHA256.txt`, and the record of input sources `inputs/PROVENANCE.md`) is included in the [companion archive](shared/rna-score-trial-size-enrichment/rna-score-trial-size-enrichment-companion.zip). The only input is four percentages and one count read from the technical report; no patient-level data, model weights or access-controlled data were used. The environment is Python 3.12.4 ([15](#ref-15)), NumPy 2.2.6 ([16](#ref-16)), SciPy 1.14.0 ([17](#ref-17)), pandas 2.2.2 ([18](#ref-18)), Matplotlib 3.9.1 ([19](#ref-19)) and statsmodels 0.14.2 ([20](#ref-20)), and the random seed is 20261114. Run `python -X utf8 analysis/01_anchor_designs.py`, `02_prognostic_adjustment.py`, `03_design_simulation.py`, `04_figures_and_crosscheck.py` and `05_manifest.py` in order, and compare the table hashes with `05_manifest.py --check`.

## References

<span id="ref-1"></span>1. Byeon GW, Fradkin P, Hsu J, Nguyen V, Shi I, Tu W, Zhang M. Ladon: an RNA foundation model for predicting patient outcomes [Internet]. Blank Bio; 2026 [cited 2026 Nov 14]. Technical report (not peer reviewed). doi:10.5281/zenodo.24157116 (DOI as given for the report; resolves to Zenodo). Available from: [https://www.blank.bio/ladon-technical-report](https://www.blank.bio/ladon-technical-report). Text read through a fetch tool that returns the passages asked for; the figures were not viewed.

<span id="ref-2"></span>2. Blank Bio. Introducing Ladon: an RNA foundation model for predicting patient outcomes [Internet]. Substack; 2026 Nov 12 [cited 2026 Nov 14]. Available from: [https://blankbio.substack.com/p/introducing-ladon-an-rna-foundation](https://blankbio.substack.com/p/introducing-ladon-an-rna-foundation)

<span id="ref-3"></span>3. Fehrenbacher L, Spira A, Ballinger M, Kowanetz M, Vansteenkiste J, Mazieres J, et al. Atezolizumab versus docetaxel for patients with previously treated non-small-cell lung cancer (POPLAR): a multicentre, open-label, phase 2 randomised controlled trial. Lancet. 2016;387(10030):1837–1846. [doi:10.1016/S0140-6736(16)00587-0](https://doi.org/10.1016/S0140-6736(16)00587-0). Abstract read.

<span id="ref-4"></span>4. Rittmeyer A, Barlesi F, Waterkamp D, Park K, Ciardiello F, von Pawel J, et al. Atezolizumab versus docetaxel in patients with previously treated non-small-cell lung cancer (OAK): a phase 3, open-label, multicentre randomised controlled trial. Lancet. 2017;389(10066):255–265. [doi:10.1016/S0140-6736(16)32517-X](https://doi.org/10.1016/S0140-6736(16)32517-X). Abstract read.

<span id="ref-5"></span>5. U.S. Food and Drug Administration. Adjusting for covariates in randomized clinical trials for drugs and biological products: guidance for industry [Internet]. 2023 May [cited 2026 Nov 14]. Available from: [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/adjusting-covariates-randomized-clinical-trials-drugs-and-biological-products](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/adjusting-covariates-randomized-clinical-trials-drugs-and-biological-products). Web page summary read; the guidance text was not read.

<span id="ref-6"></span>6. European Medicines Agency, Committee for Medicinal Products for Human Use. Qualification opinion for prognostic covariate adjustment (PROCOVA) [Internet]. EMADOC-1700519818-907465; adopted 2022 Sep 15 [cited 2026 Nov 14]. Available from: [https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/qualification-opinion-prognostic-covariate-adjustment-procovatm_en.pdf](https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/qualification-opinion-prognostic-covariate-adjustment-procovatm_en.pdf). Statement and conclusion section read.

<span id="ref-7"></span>7. Schuler A, Walsh D, Hall D, Walsh J, Fisher C. Increasing the efficiency of randomized trial estimates via linear adjustment for a prognostic score. Int J Biostat. 2022;18(2):329–356. [doi:10.1515/ijb-2021-0072](https://doi.org/10.1515/ijb-2021-0072). Abstract read.

<span id="ref-8"></span>8. Moore KL, van der Laan MJ. Covariate adjustment in randomized trials with binary outcomes: targeted maximum likelihood estimation. Stat Med. 2009;28(1):39–64. [doi:10.1002/sim.3445](https://doi.org/10.1002/sim.3445). Abstract read.

<span id="ref-9"></span>9. U.S. Food and Drug Administration. Enrichment strategies for clinical trials to support approval of human drugs and biological products: guidance for industry (title as in the web page heading; the page body gives the final title with "Demonstration of Effectiveness") [Internet]. 2019 Mar [cited 2026 Nov 14]. Available from: [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/enrichment-strategies-clinical-trials-support-approval-human-drugs-and-biological-products](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/enrichment-strategies-clinical-trials-support-approval-human-drugs-and-biological-products). Web page read (title, date, status); the guidance text was not read.

<span id="ref-10"></span>10. Simon R, Maitournam A. Evaluating the efficiency of targeted designs for randomized clinical trials. Clin Cancer Res. 2004;10(20):6759–6763. [doi:10.1158/1078-0432.CCR-04-0496](https://doi.org/10.1158/1078-0432.CCR-04-0496). Abstract read.

<span id="ref-11"></span>11. Maitournam A, Simon R. On the efficiency of targeted clinical trials. Stat Med. 2005;24(3):329–339. [doi:10.1002/sim.1975](https://doi.org/10.1002/sim.1975). Abstract read.

<span id="ref-12"></span>12. Brookes ST, Whitely E, Egger M, Smith GD, Mulheran PA, Peters TJ. Subgroup analyses in randomized trials: risks of subgroup-specific analyses; power and sample size for the interaction test. J Clin Epidemiol. 2004;57(3):229–236. [doi:10.1016/j.jclinepi.2003.08.009](https://doi.org/10.1016/j.jclinepi.2003.08.009). Abstract read.

<span id="ref-13"></span>13. Kent DM, Paulus JK, van Klaveren D, D'Agostino R, Goodman S, Hayward R, et al. The Predictive Approaches to Treatment effect Heterogeneity (PATH) Statement. Ann Intern Med. 2020;172(1):35–45. [doi:10.7326/M18-3667](https://doi.org/10.7326/M18-3667). Abstract read.

<span id="ref-14"></span>14. Daniel R, Zhang J, Farewell D. Making apples from oranges: comparing noncollapsible effect estimators and their standard errors after adjustment for different covariate sets. Biom J. 2021;63(3):528–557. [doi:10.1002/bimj.201900297](https://doi.org/10.1002/bimj.201900297). Abstract read.

<span id="ref-15"></span>15. Python Software Foundation. Python [Software]. Version 3.12.4. 2024. Available from: [https://www.python.org/](https://www.python.org/)

<span id="ref-16"></span>16. Harris CR, Millman KJ, van der Walt SJ, Gommers R, Virtanen P, Cournapeau D, et al. Array programming with NumPy [Software, version 2.2.6]. Nature. 2020;585(7825):357–362. [doi:10.1038/s41586-020-2649-2](https://doi.org/10.1038/s41586-020-2649-2)

<span id="ref-17"></span>17. Virtanen P, Gommers R, Oliphant TE, Haberland M, Reddy T, Cournapeau D, et al. SciPy 1.0: fundamental algorithms for scientific computing in Python [Software, version 1.14.0]. Nat Methods. 2020;17(3):261–272. [doi:10.1038/s41592-019-0686-2](https://doi.org/10.1038/s41592-019-0686-2)

<span id="ref-18"></span>18. McKinney W. Data structures for statistical computing in Python [Software: pandas, version 2.2.2]. In: Proceedings of the 9th Python in Science Conference. 2010. p. 56–61. [doi:10.25080/Majora-92bf1922-00a](https://doi.org/10.25080/Majora-92bf1922-00a)

<span id="ref-19"></span>19. Hunter JD. Matplotlib: a 2D graphics environment [Software, version 3.9.1]. Comput Sci Eng. 2007;9(3):90–95. [doi:10.1109/MCSE.2007.55](https://doi.org/10.1109/MCSE.2007.55)

<span id="ref-20"></span>20. Seabold S, Perktold J. Statsmodels: econometric and statistical modeling with Python [Software, version 0.14.2]. In: Proceedings of the 9th Python in Science Conference. 2010. p. 92–96. [doi:10.25080/Majora-92bf1922-011](https://doi.org/10.25080/Majora-92bf1922-011)
