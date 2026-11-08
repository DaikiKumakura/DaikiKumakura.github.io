Sacituzumab tirumotecan (sac-TMT, MK-2870, SKB264) is an antibody–drug conjugate (ADC) that targets TROP2 and carries the topoisomerase I inhibitor payload KL610023. In its phase 1/2 trial, expansion cohorts in metastatic triple-negative breast cancer (TNBC) received 4 mg/kg or 5 mg/kg every 2 weeks ([1](#ref-1)). A dose increase is expected to carry a possible gain in antitumor activity, together with a concern about more myelosuppression and other toxicities.

**QOI (Question of Interest): Is it worth increasing from 4 mg/kg to 5 mg/kg?**

**COU (Context of Use): To compare the efficacy and toxicity of the increase using public data.**

**Answer:** The public data cannot tell whether the increase raises the objective response rate (ORR). The ORR difference (5 mg/kg − 4 mg/kg) is 3.9 points as a point estimate, with a wide 95% credible interval of −21.0 to 27.7 points. Grade ≥3 decreased neutrophil count (2/23 versus 13/36 patients) and any-grade stomatitis (6/23 versus 21/36) were observed more often at 5 mg/kg. These are, however, two of ten exploratory comparisons; the Bonferroni-adjusted p values are 0.30 and 0.18, so they are not significant after adjustment. The two groups were not randomized, and these are not causal effects of the increase. For the value of the increase, the most that can be said is "no benefit confirmed, and an increase in toxicity observed."

## Abstract

In supplementary Table S3 of phase 1 (solid tumors) ([2](#ref-2)), the ratio of group-mean ADC AUC (area under the concentration–time curve, 0–336 hours; 5 mg/kg over 4 mg/kg, 7 patients each) was 1.05 (95% interval 0.87–1.30), a point estimate below the dose ratio of 1.25. The interval includes 1.25, and whether the shortfall reflects small-sample variability or true non-proportionality cannot be distinguished. Across the five dose levels from 2 to 6 mg/kg the slope was 0.98 (0.72–1.25), compatible with proportionality (slope 1), but the interval is wide and proportionality is not confirmed. In the phase 2 TNBC population (23 patients at 4 mg/kg and 36 at 5 mg/kg), the posterior probability that the ORR difference is positive was 0.62, and the Grade 3–4 treatment-related adverse event (TRAE) difference was 14.2 points (−10.6 to 38.6), with an interval that includes 0. The intervals for neutrophil count and stomatitis exclude 0, but these come from ten exploratory comparisons and are not significant after multiplicity adjustment. PK (phase 1) and the clinical comparison (phase 2) come from different populations, and the analysis does not link exposure to toxicity or response.

## Introduction

In the published phase 2 TNBC population, the 4 mg/kg group (23 patients) had an ORR of 34.8% and Grade 3–4 TRAEs in 12/23 patients; the 5 mg/kg group (36 patients) had an ORR of 38.9% and Grade 3–4 TRAEs in 24/36 ([1](#ref-1), [Table 4](https://jhoonline.biomedcentral.com/articles/10.1186/s13045-025-01705-2#Tab4), [Table 5](https://jhoonline.biomedcentral.com/articles/10.1186/s13045-025-01705-2#Tab5)). The two groups were not randomized, and a causal effect of the increase has not been established. This article sets out how far published human pharmacokinetic (PK) summaries and clinical tallies can answer the question. The mathematical model serves to relate exposure to observations and to show what can be judged.

The analysis plan was not fixed before computing. The dose-proportionality check of the PK, the endpoint-by-endpoint comparison of adverse events and the sensitivity analysis for non-exchangeability were added while looking at the result tables, so they are exploratory.

## Methods

### Data

PK came from supplementary Table S3 of the original article (cycle 1 day 1, phase 1 dose escalation; mean ± SD and number of patients per dose) ([2](#ref-2)). The patients had solid tumors and were not the TNBC expansion cohorts. The 4 mg/kg and 5 mg/kg groups had 7 patients each, and the number evaluated was 6–7 depending on the PK item. According to the table footnote, the concentration unit is µg/mL for ADC and total antibody and ng/mL for free payload (KL610023); the column headers read µg/mL, so the footnote was followed (the record is in `inputs/PROVENANCE.md`). AUC is the value from 0 to 336 hours. Individual concentration–time data appear only as an image in supplementary Figure S2 and were not used. The clinical tallies are the numbers of responders (CR, complete response, plus PR, partial response) and of adverse events transcribed from Table 4 and Table 5 of the original article for the phase 2 TNBC cohorts (4 mg/kg, 23 patients; 5 mg/kg, 36 patients) ([1](#ref-1)). Median progression-free survival (PFS) and overall survival (OS) are quoted from the text only; the curves were not reconstructed.

### Analysis of the PK summaries

The sampling distribution of each group mean was taken as $\mathcal{N}(\bar{x}, \mathrm{SD}^2/n)$, and the ratio of the 5 mg/kg mean to the 4 mg/kg mean was obtained with a parametric bootstrap of 200,000 draws (seed 20261107); intervals are the 2.5th and 97.5th percentiles. Dose proportionality was assessed by weighted regression of ln(group mean) on ln(dose) over the five dose levels. Weights were the inverse of the delta-method variance of ln(mean), $\mathrm{SD}^2/(n\bar{x}^2)$, and intervals used a t distribution with 3 degrees of freedom. A slope of 1 is dose proportional. The analysis rests only on published means ± SD, not individual data. For free payload, whose SD is close to the mean, the normal approximation is inappropriate (the denominator can approach 0), and the ratio intervals are only indicative.

A linked compartment model of ADC, total antibody and free payload was not fitted. The concentration–time data needed for fitting are not published as numbers, so the model cannot be identified. The analysis was reduced to group-wise exposure summaries and a proportionality check.

### Bayesian estimation of response and toxicity

The number of patients $Y_j$ in group $j$ was modeled as $Y_j \sim \mathrm{Binomial}(n_j, p_j)$ with a Beta(0.5, 0.5) (Jeffreys) prior on $p_j$, treating the 4 mg/kg and 5 mg/kg groups independently (no borrowing across groups). Posteriors were summarized with 200,000 draws. Beta(1, 1) was used as a sensitivity prior. As frequentist references, Fisher's exact test and the Newcombe (Wilson-score) 95% interval were computed (the Newcombe intervals for all endpoints are in `outputs/tables/risk_difference.csv` of the companion archive). The ten endpoints were ORR, Grade 3–4 TRAE, Grade ≥3 anemia, decreased white blood cell (WBC) count, decreased neutrophil count and decreased platelet count, any-grade stomatitis, and TRAEs leading to interruption, dose reduction or discontinuation. For multiplicity, the Bonferroni adjustment (Fisher p multiplied by 10, capped at 1) is shown as a reference.

For the two-dimensional comparison of benefit and risk, posteriors for ORR and Grade 3–4 TRAE were drawn independently. The joint distribution within the same patients is not published, so independence is an assumption for display (a positive correlation between ORR and TRAE would change the joint probabilities). The thresholds, nine combinations of an ORR gain of at least 0, 5 or 10 points and a TRAE increase of at most 0, 10 or 20 points, were chosen arbitrarily for illustration and are not clinically derived tolerances.

For the sensitivity to non-exchangeability, a shift $b$ was subtracted from the logit of the 5 mg/kg cohort's probability, and the posterior probability that the true 5 mg/kg probability exceeds the 4 mg/kg probability was computed for $b$ from −1.0 to 1.0 in steps of 0.25. $b > 0$ is a bias under which the observed 5 mg/kg probability is higher than the true one. This looks favorable to the increase for ORR and unfavorable to the increase for toxicity. $b < 0$ is the reverse. The size of $b$ has no external basis; it is an assumed value that stands for compound confounding as one constant.

## Results

### Dose proportionality of exposure and the 4 versus 5 mg/kg difference

Figure 1 shows dose-normalized group-mean exposure. Table 1 gives the ratio of the 5 mg/kg group mean to the 4 mg/kg group mean.

![Dose-normalized group means with 95% intervals for ADC AUC, ADC Cmax and free payload AUC, with the 4 mg/kg and 5 mg/kg groups in different colors.](shared/sacituzumab-tirumotecan-dose-comparison/figures/fig1_dose_normalised_exposure.png)

Figure 1. Dose-normalized exposure (cycle 1 day 1, phase 1; mean ± 1.96 SE; blue is 4 mg/kg and orange is 5 mg/kg). Cmax is the maximum concentration. Computed from the means, SDs and numbers in supplementary Table S3 ([2](#ref-2), [Table S3](https://static-content.springer.com/esm/art%3A10.1186%2Fs13045-025-01705-2/MediaObjects/13045_2025_1705_MOESM1_ESM.docx)).

Table 1. Ratio of exposure in the 5 mg/kg group to the 4 mg/kg group (`analysis/01_pk_dose_proportionality.py`). The dose ratio is 1.25. P(ratio ≥ 1.25) is the share of bootstrap draws in which the ratio is at least 1.25.

| Analyte | Parameter | Mean at 4 mg/kg (n) | Mean at 5 mg/kg (n) | Ratio (95% interval) | P(ratio ≥ 1.25) |
| --- | --- | --- | --- | --- | ---: |
| ADC | AUC0–336h, h·µg/mL | 5,170 (7) | 5,410 (7) | 1.05 (0.87–1.30) | 0.05 |
| ADC | Cmax, µg/mL | 88.4 (7) | 111 (7) | 1.26 (1.07–1.48) | 0.52 |
| Total antibody | AUC0–336h, h·µg/mL | 5,930 (7) | 5,780 (7) | 0.97 (0.79–1.25) | 0.03 |
| Total antibody | Cmax, µg/mL | 89.2 (7) | 111 (7) | 1.24 (1.03–1.54) | 0.48 |
| Free payload* | AUC0–336h, h·ng/mL | 1,050 (7) | 946 (6) | 0.90 (0.43–3.04) | 0.23 |
| Free payload* | Cmax, ng/mL | 30.6 (7) | 31.3 (7) | 1.02 (0.41–2.50) | 0.31 |

*Intervals for free payload are indicative values from a normal approximation.

The Cmax ratios for ADC and total antibody are compatible with the dose ratio of 1.25. The AUC ratios of 1.05 and 0.97 are point estimates below it. The interval of the ADC AUC ratio includes 1.25 (P(ratio ≥ 1.25) = 0.05). The dose-normalized AUC of the 4 mg/kg group (1,293 h·µg/mL per mg/kg) is the highest of the five dose levels and that of the 5 mg/kg group (1,082) is the lowest (Figure 1). Slopes across the five dose levels are 0.98 for AUC and 0.93 for Cmax, with intervals that include 1 (Table 2). The intervals are not narrow enough to exclude non-proportionality of 25% or more.

Table 2. Dose-proportionality slopes (five dose levels; 1 is proportional; `analysis/01_pk_dose_proportionality.py`).

| Analyte | Parameter | Slope (95% interval) | Includes 1 |
| --- | --- | --- | --- |
| ADC | AUC | 0.98 (0.72–1.25) | Yes |
| ADC | Cmax | 0.93 (0.66–1.19) | Yes |
| Total antibody | AUC | 1.01 (0.72–1.29) | Yes |
| Total antibody | Cmax | 0.99 (0.81–1.18) | Yes |
| Free payload | AUC | 1.19 (0.11–2.26) | Yes |
| Free payload | Cmax | 0.89 (−1.06 to 2.84) | Yes |

Figure 2 shows the intervals of the ratios.

![Ratio of 5 mg/kg group mean to 4 mg/kg group mean with 95% intervals for AUC and Cmax of ADC, total antibody and free payload, with a line at the dose ratio of 1.25.](shared/sacituzumab-tirumotecan-dose-comparison/figures/fig2_exposure_ratio.png)

Figure 2. Ratio of group means, 5 mg/kg over 4 mg/kg (95% bootstrap intervals; 6–7 patients per group). The dotted line is 1 and the dashed line is the dose ratio of 1.25.

Free payload shows large between-patient variability (the SD of AUC at 4 mg/kg is about equal to the mean), and it cannot be determined whether payload exposure at 5 mg/kg is higher than at 4 mg/kg. Payload AUC per dose is not monotonic across the five levels, with the lowest at 5.5 mg/kg (Figure 1, right).

As fact, these summaries do not reject the hypothesis that ADC exposure is proportional to dose from 2 to 6 mg/kg. This is not a confirmation of proportionality (3 degrees of freedom and wide slope intervals). As interpretation, it cannot be distinguished whether the AUC ratio of 1.05 falling below the dose ratio of 1.25 reflects between-patient variability with 7 patients per group (the coefficient of variation of AUC is about 25% at 4 mg/kg) or true non-proportionality (nonlinear clearance, patient characteristics, body weight or tumor burden). Cmax depends strongly on plasma volume and tends to be nearly dose proportional, so it is a weak indicator of tissue delivery. Whether body weight or tumor burden differed between groups cannot be checked from the supplementary table.

### Response difference and hematologic toxicity

Figure 3 shows the posteriors of ORR, Grade 3–4 TRAE and Grade ≥3 decreased neutrophil count.

![Posterior probability densities for the 4 mg/kg and 5 mg/kg groups of response rate, Grade 3-4 treatment-related adverse events and Grade 3 or higher decreased neutrophil count.](shared/sacituzumab-tirumotecan-dose-comparison/figures/fig3_posteriors.png)

Figure 3. Beta-binomial posteriors (Jeffreys prior; phase 2 TNBC). Legend numbers are events/patients.

Table 3. Events by dose group in phase 2 TNBC and differences (5 mg/kg − 4 mg/kg; `analysis/02_bayes_efficacy_safety.py`). P(difference > 0) is the posterior probability that the difference in true probabilities of the two observed cohorts is positive; it is not the probability that the increase works.

| Endpoint | 4 mg/kg, n/N (%) | 5 mg/kg, n/N (%) | Difference, median (95% credible interval), points | P(difference > 0) | Fisher exact p |
| --- | --- | --- | --- | ---: | ---: |
| ORR (CR + PR) | 8/23 (34.8) | 14/36 (38.9) | 3.9 (−21.0 to 27.7) | 0.62 | 0.79 |
| Grade 3–4 TRAE | 12/23 (52.2) | 24/36 (66.7) | 14.2 (−10.6 to 38.6) | 0.87 | 0.29 |
| Grade ≥3 anemia | 4/23 (17.4) | 9/36 (25.0) | 7.2 (−14.5 to 27.0) | 0.75 | 0.54 |
| Grade ≥3 WBC decreased | 3/23 (13.0) | 11/36 (30.6) | 16.7 (−4.6 to 36.2) | 0.94 | 0.21 |
| Grade ≥3 neutrophil decreased | 2/23 (8.7) | 13/36 (36.1) | 26.3 (5.9 to 44.8) | 0.99 | 0.030 |
| Grade ≥3 platelet decreased | 3/23 (13.0) | 8/36 (22.2) | 8.7 (−11.7 to 27.1) | 0.81 | 0.50 |
| Stomatitis, any grade | 6/23 (26.1) | 21/36 (58.3) | 31.4 (6.5 to 53.2) | 0.99 | 0.018 |
| TRAE led to interruption | 9/23 (39.1) | 21/36 (58.3) | 18.8 (−6.8 to 42.5) | 0.93 | 0.19 |
| TRAE led to dose reduction | 2/23 (8.7) | 6/36 (16.7) | 7.3 (−10.7 to 23.9) | 0.81 | 0.46 |
| TRAE led to discontinuation | 1/23 (4.3) | 2/36 (5.6) | 0.8 (−13.2 to 12.5) | 0.56 | 1.00 |

The posterior median ORR difference is 3.9 points with a wide interval from −21.0 to 27.7 points; the probability that the difference exceeds 5 points is 0.47 and that it exceeds 10 points is 0.31. Changing the prior to Beta(1, 1) barely changes this: the posterior median ORR difference is 3.6 points and the probability that it is positive is 0.61. On the toxicity side, the probability that the Grade 3–4 TRAE difference is positive is 0.87 but the interval includes 0. The intervals for anemia, decreased WBC count and decreased platelet count also include 0.

By item, the credible intervals of the difference exclude 0 for Grade ≥3 decreased neutrophil count and for any-grade stomatitis (the Newcombe intervals, 4.8 to 44.9 and 6.3 to 52.1 points, are nearly the same). These two are two of ten items chosen after seeing the results, and their thresholds differ (Grade ≥3 for blood counts, any grade for stomatitis). The Bonferroni-adjusted values, the Fisher p values (0.030, 0.018) multiplied by 10, are 0.30 and 0.18 and are not significant after adjustment. They are therefore exploratory. Decreased neutrophil count and decreased WBC count reflect the same myelosuppression and are not two independent items.

The proportion with ECOG (performance status) 1 was lower in the 5 mg/kg group than in the 4 mg/kg group (67% versus 87%), and the proportion with five or more prior regimens was 36% versus 43% ([1](#ref-1), [Table 3](https://jhoonline.biomedcentral.com/articles/10.1186/s13045-025-01705-2#Tab3) of the original article). Median treatment exposure was 5.3 months in the 4 mg/kg group and 3.6 months in the 5 mg/kg group ([1](#ref-1)). Median PFS is reported as 5.8 and 5.5 months, and median OS as 12.1 and 17.1 months ([1](#ref-1), [Figure 3](https://jhoonline.biomedcentral.com/articles/10.1186/s13045-025-01705-2#Fig3) of the original article). These are descriptive values without intervals, and because maturity of follow-up also differs between non-randomized cohorts they cannot be used for evaluation and were not used in the analysis. A longer OS in the 5 mg/kg group is not inconsistent with the increase in toxicity and cannot be used to judge whether there is a benefit.

### Two-dimensional comparison of benefit and toxicity increase

Figure 4 plots posterior draws of the ORR difference against the Grade 3–4 TRAE difference.

![Scatter plot of posterior draws of the ORR difference and the Grade 3-4 treatment-related adverse event difference. Most points lie to the upper right and the spread is large.](shared/sacituzumab-tirumotecan-dose-comparison/figures/fig4_benefit_risk_plane.png)

Figure 4. Benefit–risk plane (independent posterior draws; 8,000 of 200,000 shown). The black point is the posterior median. The joint distribution within the same patients is not published, so independence was assumed.

In posterior probability, the chance that ORR increases (difference > 0) and the Grade 3–4 TRAE increase is 10 points or less is 0.23, and the chance that the ORR gain is 10 points or more with a TRAE increase of 10 points or less is 0.12. The chance that both differences are positive is 0.54. The probabilities for all nine threshold combinations are in `outputs/tables/benefit_risk_probs.csv` of the companion archive (0.42 for a positive ORR difference with a TRAE increase of 20 points or less). The thresholds are arbitrary, so these are illustrative numbers that depend on them.

### Sensitivity to non-exchangeability

Figure 5 shows posterior probabilities when a bias is assumed for the 5 mg/kg cohort.

![Posterior probability that the true 5 mg/kg rate exceeds the 4 mg/kg rate for response rate, Grade 3-4 treatment-related adverse events and decreased neutrophil count, as a function of an assumed logit-scale bias in the 5 mg/kg cohort.](shared/sacituzumab-tirumotecan-dose-comparison/figures/fig5_bias_sensitivity.png)

Figure 5. Sensitivity to non-exchangeability. The horizontal axis $b$ is the logit-scale shift subtracted from the observed 5 mg/kg probability (0 is no bias). $b > 0$ means the observed probability is higher than the true one: ORR looks better for the increase and toxicity looks worse. $b < 0$ is the reverse.

The posterior probability that the ORR difference is positive moves from 0.62 with no bias to 0.28 at $b$ = 0.5 and 0.07 at $b$ = 1.0, and is 0.98 at $b$ = −1.0 (the observed 5 mg/kg ORR lower than the true value). The probability that the neutrophil difference is positive is 0.83 even at $b$ = 1.0, a bias under which toxicity looks higher than it really is, and 1.00 at $b$ = −1.0. For Grade 3–4 TRAE it falls below 0.5 at $b$ around 0.6. Over the range examined ($b$ from −1.0 to 1.0) the sign of the neutrophil difference did not change, whereas the sign of the ORR difference reverses at $b$ around 0.2. The size of $b$ is an assumed value without basis, and this result is not a guarantee of robustness.

## Discussion

From the public data, no gain in ORR could be confirmed with the increase, and an increase in hematologic toxicity (Grade ≥3 decreased neutrophil count) and stomatitis was observed. These two items are, however, part of ten exploratory comparisons and are not significant after adjustment. The ORR difference is a small 3.9 points as a point estimate and its credible interval spans more than 40 points, so the data neither show nor rule out a benefit of the increase. The original article also states that 5 mg/kg may be associated with slightly higher toxicity than 4 mg/kg ([1](#ref-1)).

On PK, exposure is compatible with dose proportionality from 2 to 6 mg/kg, but the slope intervals are wide and proportionality is not confirmed. The ADC Cmax in the 5 mg/kg group is about 26% higher than in the 4 mg/kg group. Whether the AUC ratio of 1.05 reflects small-sample variability or true non-proportionality cannot be distinguished. Whether free payload exposure rises with the increase cannot be determined. PK is from phase 1 patients with solid tumors, whereas toxicity and response are from phase 2 TNBC patients, so these are different populations. The analysis does not link exposure to toxicity or response, and one cannot read that because PK is proportional the increase in toxicity is due to the dose. Examining at the individual level whether payload exposure is linked to toxicity or response would require data that pair individual PK with adverse events. The public data do not contain it, and this article does not estimate it.

On non-exchangeability, the 5 mg/kg cohort had a lower proportion with ECOG 1 and a shorter treatment exposure. A lower proportion with ECOG 1 may make the ORR of the 5 mg/kg group look higher. On the toxicity side, the longer exposure in the 4 mg/kg group means that cumulative adverse events may be observed more often in that group. Conversely, a shorter follow-up in the 5 mg/kg group could cause missed adverse events, and differences in supportive care by enrollment period are also conceivable. Biases can run in several directions. Because the timing of events is not published, their size cannot be assessed. In the sensitivity analysis the sign of the ORR difference reversed at $b$ around 0.2.

The original article states that the randomized phase 3 OptiTROP-Breast01, which used 5 mg/kg, reported an ORR of 44% versus 13% with chemotherapy, a PFS hazard ratio of 0.31 and an OS hazard ratio of 0.53 ([1](#ref-1)). That result shows efficacy of 5 mg/kg but is not a comparison with 4 mg/kg and so does not answer the dose question.

## Limitations

- **Comparison between cohorts:** the 4 mg/kg and 5 mg/kg groups were not randomized and differ in patient characteristics and treatment exposure, and may differ in enrollment period. The differences seen here are not called effects of the increase.
- **PK population and numbers:** PK is from phase 1 patients with solid tumors (7 per group; 6–7 evaluated), not exposure in the phase 2 TNBC cohorts. Ratios and intervals are approximations that treat the published mean ± SD as the sampling distribution of an arithmetic mean. For free payload, whose SD is close to the mean, the normal approximation is inappropriate and the intervals are only indicative.
- **Models:** because concentration–time data are not published as numbers, no linked PK model and no exposure–response model was fitted. Exposure was not linked to efficacy or toxicity at the individual level. A time-series model of myelosuppression (neutrophil count) was not run for lack of data.
- **Independence assumption and thresholds:** the benefit–risk plane treats ORR and TRAE as independent for display; it is not a joint probability within patients. The thresholds are arbitrary.
- **Assumed bias:** $b$ in the sensitivity analysis is an assumed value without external basis and does not indicate the actual size of confounding.
- **Multiplicity and exploration:** no correction was applied across the 10 endpoints (the Bonferroni-adjusted values are shown for reference). Item-wise p values and credible intervals are exploratory. The analysis plan was not fixed in advance.
- **Sources not used:** the original sources of the phase 3 OptiTROP-Breast01 and of the ESMO 2025 endometrial cohort were not read. Statements about phase 3 are limited to the description in the original article ([1](#ref-1)). PFS and OS curves were not reconstructed; only the medians in the text are quoted.
- **Uncertainty:** the intervals do not include uncertainty from data acquisition, assessors or differences in follow-up.

## Conclusion

On the QOI (is it worth increasing from 4 mg/kg to 5 mg/kg), the public data support the following. An ORR gain at 5 mg/kg cannot be identified: the point estimate is a small 3.9 points and uncertainty is large. Grade ≥3 decreased neutrophil count (9% at 4 mg/kg versus 36% at 5 mg/kg) and any-grade stomatitis (26% versus 58%) were observed more often at 5 mg/kg, but these come from ten exploratory comparisons and are not significant after adjustment. Over the biases examined ($b$ from −1.0 to 1.0) the sign of the neutrophil difference was preserved, whereas the sign of the ORR difference reverses under moderate bias; the size of $b$ is an assumed value. Exposure is compatible with dose proportionality from 2 to 6 mg/kg, but proportionality is not confirmed, and PK (phase 1) and the clinical comparison (phase 2) come from different populations. These are non-randomized comparisons between cohorts and not causal effects of the increase. The judgment on the value of the increase stays at "no benefit confirmed, and an increase in toxicity observed."

## Data and code availability

The re-run materials (scripts in `analysis/`, input CSVs and the provenance record in `inputs/`, tables, figures and logs in `outputs/`) are in the [companion archive](shared/sacituzumab-tirumotecan-dose-comparison/sacituzumab-tirumotecan-dose-comparison-companion.zip). `pk_tableS3.csv` holds the values extracted from Table S3 of the supplementary material ([2](#ref-2)) with `analysis/00_extract_pk_table_s3.py`; the original Word file is not bundled. The clinical counts were transcribed from the tables of the original article ([1](#ref-1)). Re-run: `python analysis/01_pk_dose_proportionality.py && python analysis/02_bayes_efficacy_safety.py && python analysis/03_figures.py` (Windows 11, Python 3.12.4, numpy 2.2.6, pandas 2.2.2, scipy 1.14.0, matplotlib 3.9.1). The random seed is 20261107.

## References

<span id="ref-1"></span>1. Ouyang Q, Rodon J, Liang Y, Wu X, Li Q, Song L, et al. Results of a phase 1/2 study of sacituzumab tirumotecan in patients with unresectable locally advanced or metastatic solid tumors refractory to standard therapies. J Hematol Oncol. 2025;18:61. [doi:10.1186/s13045-025-01705-2](https://doi.org/10.1186/s13045-025-01705-2).

<span id="ref-2"></span>2. Ouyang Q, Rodon J, Liang Y, Wu X, Li Q, Song L, et al. Additional file 1: Supplementary Tables S1–S3 and Figures S1–S3 [Supplementary material]. In: Results of a phase 1/2 study of sacituzumab tirumotecan in patients with unresectable locally advanced or metastatic solid tumors refractory to standard therapies. J Hematol Oncol. 2025;18:61. File 13045_2025_1705_MOESM1_ESM.docx. Available from: [https://static-content.springer.com/esm/art%3A10.1186%2Fs13045-025-01705-2/MediaObjects/13045_2025_1705_MOESM1_ESM.docx](https://static-content.springer.com/esm/art%3A10.1186%2Fs13045-025-01705-2/MediaObjects/13045_2025_1705_MOESM1_ESM.docx)
