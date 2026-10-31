In August 2026, the orexin 2 receptor agonist oveporexton (development code TAK-861) was approved in Japan for adults with narcolepsy type 1 (narcolepsy with cataplexy). The product name is ORZEYFUL. According to the approval announcement, the usual dose is 1 mg twice daily, and the dose may be increased to 2 mg twice daily only when the 1 mg dose is well tolerated but efficacy is insufficient ([1](#ref-1)). Of the two phase 3 trials conducted before approval, one tested 2 mg only and the other included both 1 mg and 2 mg groups. How much do efficacy and adverse events differ between 1 mg and 2 mg? And how consistent is the effect of the same 2 mg twice-daily regimen across trials?

This article recounts the posted results of three trials registered on ClinicalTrials.gov (one phase 2b and two phase 3) to address these two questions ([2](#ref-2), [3](#ref-3), [4](#ref-4)). Dose decisions for patients rest with physicians, and this article is no substitute for them. The reference date is October 30, 2026; facts and numbers reflect public information as of that date. Later updates to the registry records and changes in approval status are not reflected.

## Abstract

- In the FirstLight trial (12 weeks, twice daily), the change in sleep latency on the maintenance of wakefulness test (MWT), expressed as the difference from placebo, was 13.8 minutes for 1 mg and 17.2 minutes for 2 mg. The difference between the 2 mg and 1 mg groups is 3.4 minutes. The 95% confidence interval was −0.1 to 6.8 minutes under an approximation treating the two groups as independent, and 0.5 to 6.2 minutes under an approximation back-calculated with a shared placebo group, so whether the interval includes 0 depends on the approximation chosen.
- Among the eight adverse events posted for FirstLight (reporting threshold 5% or more), point estimates were similar at the two doses for insomnia, pollakiuria, micturition urgency and salivary hypersecretion (insomnia 53% with 1 mg and 58% with 2 mg). Headache, however, was higher with 2 mg: 7% (4/60) versus 15% (10/66). The intervals for differences are wide. Serious adverse events were posted for 1/60 (1 mg) and 1/66 (2 mg), too few to judge a dose difference.
- The MWT change under the same 2 mg twice-daily regimen differed across trials: 23.5 minutes in phase 2b, 15.9 in FirstLight and 19.1 in RadiantLight. The posted summaries cannot identify the cause.
- In a post hoc, exploratory comparison, the MWT change in the phase 2b 7 mg once-daily group was 8.5 minutes (3.0 to 14.1) smaller than in the 2 mg twice-daily group.

## Introduction

The three registered trials have the following arm structures. Only FirstLight includes a 1 mg group.

- NCT05687903: phase 2b, 8 weeks, 112 participants enrolled. Five arms: placebo, 0.5 mg twice daily, 2 mg twice daily, 2 mg followed by 5 mg (twice daily) and 7 mg once daily ([2](#ref-2)).
- NCT06470828 (FirstLight): phase 3, 12 weeks, 168 enrolled. Three arms: placebo, 1 mg twice daily and 2 mg twice daily ([3](#ref-3)).
- NCT06505031 (RadiantLight): phase 3, 12 weeks, 105 enrolled. Two arms: placebo and 2 mg twice daily ([4](#ref-4)).

Only FirstLight therefore allows a randomized comparison within one trial between a group corresponding to the usual Japanese dose (1 mg twice daily) and a group corresponding to the escalation dose (2 mg twice daily). There are two questions. (i) In FirstLight, how much did 2 mg twice daily add to 1 mg twice daily in MWT, the Epworth Sleepiness Scale (ESS), cataplexy and adverse events? (ii) Was the effect of the same 2 mg twice-daily regimen consistent across the three trials?

I did not have access to the regulatory review report, so the basis of the approval is not examined here. The approved contents rely on the company announcement ([1](#ref-1)).

## Methods

### Data

I used the posted results on ClinicalTrials.gov as retrieved on October 30, 2026 (`inputs/`). No values were entered by hand; only the mapping of arm names to doses is written in a table in `analysis.py`. The posted data are group-level summaries, not individual participant data.

- MWT: change from baseline in sleep latency (minutes). Longer means better maintenance of wakefulness.
- ESS: change from baseline in the sleepiness score (points). Smaller (more negative) means less sleepiness.
- Cataplexy: attacks per week.
- Adverse events: other (non-serious) adverse events at the 5% reporting threshold or above and serious adverse events, as posted in the results. Eight events are posted for FirstLight.

Group means are least-squares (LS) means, adjusted for baseline and other factors by the trial's statistical model. The per-group weekly cataplexy values, however, are unadjusted arithmetic means (observed values) in FirstLight and RadiantLight and LS means in phase 2b; the statistics differ. Comparisons with placebo are reported as incidence rate ratios (IRRs).

### Analysis

- Dose difference: I computed the difference between the LS means of two groups within FirstLight and combined the standard errors assuming independence, as sqrt(SE1^2 + SE2^2) (independence approximation). The covariance used in the trial analysis is not posted, so this interval is an approximation. As a sensitivity analysis, I back-calculated standard errors from the posted 95% intervals for each dose versus placebo (z = 1.96) and also computed an interval that accounts for the shared placebo variance, with the standard error of the difference sqrt(SE_A^2 + SE_B^2 - 2 Var_placebo) (shared-placebo approximation, `results/increment-sensitivity-shared-placebo.csv`). Because the latter uses the difference between the placebo contrasts rather than the difference between LS means, its point estimate differs by 0.01 minutes (3.37 vs 3.36; a rounding difference). Neither interval is the trial's own analysis interval.
- Adverse events: proportions are shown with Wilson confidence intervals, and intervals for differences in proportions use the Wald method.
- Between-trial differences: I lined up the LS means for the same 2 mg twice-daily regimen across the three trials and computed a fixed-effect homogeneity Q test with weights 1/SE^2 and I², a measure of the share of variability due to between-trial differences. The groups differ in population, duration (8 versus 12 weeks) and the MWT outcome definition (in the registry, average sleep latency in phase 2b and the mean of four MWT wake trials in phase 3). They do not satisfy the premise of a meta-analysis (that the same effect is being measured), so this test is a reference value.
- Dosing frequency: for phase 2b, I computed the difference in LS-mean MWT change between 7 mg once daily and 2 mg twice daily, with an independence-approximation interval.

The analysis plan was not fixed before computation. I determined the scope while examining the structure of the registered results, and points decided after seeing the results are labelled post hoc. The post hoc decisions are the dosing-frequency comparison (phase 2b, 7 mg once daily versus 2 mg twice daily) and the restriction of the intervals for differences in proportions to four adverse events: insomnia, pollakiuria, micturition urgency and salivary hypersecretion. The analysis plan records that these four were chosen to match the labelling description; I did not re-check the labelling for this article. The frequencies of all eight events are shown in Table 2.

## Results

### 1 mg versus 2 mg in FirstLight

Table 1. The 1 mg and 2 mg twice-daily groups in FirstLight (12 weeks).

| Item | Placebo | 1 mg twice daily | 2 mg twice daily | 2 mg minus 1 mg (95% CI, independence approximation) |
|---|---|---|---|---|
| n (MWT and ESS analyses) | 41 | 61 | 66 | |
| MWT change (minutes, LS mean) | −1.32 | 12.51 | 15.87 | 3.36 (−0.09 to 6.81) |
| ESS change (points, LS mean) | −1.42 | −9.42 | −11.17 | −1.75 (−3.55 to 0.05) |
| Cataplexy attacks per week (arithmetic mean, observed) | 34.04 | 11.50 | 12.80 | |
| IRR versus placebo (95% CI) | | 0.34 (0.20 to 0.57) | 0.38 (0.23 to 0.61) | |

Note: n is the efficacy analysis set. The registry lists 60 participants in the 1 mg group for adverse events; the reason for the difference in denominators from the efficacy analysis could not be confirmed from the registry.

The differences from placebo were 13.83 minutes (10.23 to 17.44) for 1 mg and 17.20 minutes (13.66 to 20.73) for 2 mg in MWT. The additional effect of 2 mg is about 3 minutes in MWT and about 2 points in ESS. The interval for the MWT difference was −0.1 to 6.8 minutes under the independence approximation and 0.5 to 6.2 minutes under the shared-placebo approximation. The interval for the ESS difference was −3.55 to 0.05 points under the independence approximation and −3.18 to −0.32 points under the shared-placebo approximation. For both outcomes, the lower bound is near 0, and whether the interval includes 0 depends on the approximation. For cataplexy, the IRR intervals of the 2 mg and 1 mg groups overlap substantially, and no tendency for 2 mg to be better than 1 mg was seen.

The difference from placebo in the 1 mg group, 13.83 minutes, is about 80% of that in the 2 mg group, 17.20 minutes (13.83/17.20). This is a ratio of point estimates and does not account for the intervals.

Table 2. Frequency of the eight adverse events posted for FirstLight (reporting threshold 5% or more).

| Event | Placebo (n = 41) | 1 mg twice daily (n = 60) | 2 mg twice daily (n = 66) |
|---|---|---|---|
| Insomnia | 0/41 (0%) | 32/60 (53%) | 38/66 (58%) |
| Pollakiuria | 3/41 (7%) | 32/60 (53%) | 36/66 (55%) |
| Micturition urgency | 1/41 (2%) | 9/60 (15%) | 12/66 (18%) |
| Nasopharyngitis | 6/41 (15%) | 6/60 (10%) | 10/66 (15%) |
| Headache | 5/41 (12%) | 4/60 (7%) | 10/66 (15%) |
| Salivary hypersecretion | 0/41 (0%) | 5/60 (8%) | 4/66 (6%) |
| Weight increased | 3/41 (7%) | 2/60 (3%) | 4/66 (6%) |
| Migraine | 3/41 (7%) | 0/60 (0%) | 1/66 (2%) |

Insomnia, pollakiuria, micturition urgency and salivary hypersecretion occurred at similar frequencies in the 2 mg and 1 mg groups. The differences in proportions (Wald 95% confidence intervals) were 4.2 percentage points (−13 to +22) for insomnia and 1.2 percentage points (−16 to +19) for pollakiuria. The intervals are wide, and the group sizes (60 and 66 in the active arms) are too small to show that the dose-related difference is small. Among the remaining four events, headache was higher with 2 mg (15%) than with 1 mg (7%), and the point estimates for nasopharyngitis and weight increased were also higher with 2 mg. Migraine was most frequent in the placebo group. Intervals for these differences were not computed.

Serious adverse events in the registry results (`inputs/NCT06470828.json`) were 0/41 with placebo, 1/60 with 1 mg (ureterolithiasis) and 1/66 with 2 mg (non-specific chest pain); no deaths were reported in any group. With so few events, a dose difference cannot be judged. Reasons for discontinuation and frequencies by severity were not examined.

![Difference in MWT from placebo plotted against total daily dose, by trial and dosing schedule](shared/oveporexton-orexin-dose/figures/01-mwt-dose.png)

Figure 1. Change in MWT sleep latency as a difference from placebo (minutes) with 95% confidence intervals, plotted against total daily dose (mg). Colour denotes trial; marker denotes dosing schedule (circle, twice daily; square, once daily; triangle, 2 mg followed by 5 mg). Point positions are `vs_placebo` in `results/arms-outcomes.csv`; group sizes are 19 to 70. Comparisons across trials include differences in population.

### Between-trial differences for the same 2 mg twice-daily regimen

Table 3. MWT change (LS mean) in the 2 mg twice-daily group in three trials.

| Trial | n (2 mg group) | MWT change (minutes) | Standard error (minutes) | Placebo-group change (minutes) |
|---|---|---|---|---|
| Phase 2b (8 weeks) | 21 | 23.50 | 2.042 | −1.16 |
| FirstLight (12 weeks) | 66 | 15.87 | 1.205 | −1.32 |
| RadiantLight (12 weeks) | 70 | 19.09 | 1.254 | −1.01 |

The difference between the largest and smallest values was 7.6 minutes. The homogeneity Q test gave Q = 10.9 (2 degrees of freedom), p = 0.004 and I² = 82%. For ESS, Q = 5.0 (2 degrees of freedom), p = 0.08 and I² = 60%. With only three trials, I² is unstable. The placebo-group changes were similar across the three trials, from −1.0 to −1.3 minutes. The posted summaries cannot establish which of patient severity, baseline values, test conditions, trial duration (8 versus 12 weeks) or chance in the small phase 2b trial produced the difference.

![Frequencies of insomnia and pollakiuria by trial and group](shared/oveporexton-orexin-dose/figures/02-adverse-events.png)

Figure 2. Percentage of participants reporting insomnia (left) and pollakiuria (right), by trial and group. Each point is `rate` in `results/adverse-events.csv`; confidence intervals are not shown. Denominators are `at_risk` in the same file (21 to 70). Limited to events at or above the 5% reporting threshold; comparisons across trials include differences in population and duration.

### Dosing frequency in phase 2b (post hoc, exploratory)

Table 4. MWT by group in phase 2b (8 weeks).

| Group (n for MWT) | Total daily dose (mg) | MWT difference from placebo (minutes, 95% CI) |
|---|---|---|
| 0.5 mg twice daily (19) | 1 | 13.65 (7.74 to 19.57) |
| 2 mg twice daily (21) | 4 | 24.67 (18.87 to 30.46) |
| 2 mg followed by 5 mg (twice daily) (20), note | 7 | 26.58 (20.81 to 32.35) |
| 7 mg once daily (23) | 7 | 16.13 (10.49 to 21.76) |

Note: the total of 7 mg is an interpretation of the registry arm name ("2 mg and 5 mg") and its description (2 mg followed by 5 mg, twice daily).

The 7 mg once-daily group (with placebo as the second dose) had an MWT change 8.5 minutes smaller than the 2 mg twice-daily group (total 4 mg); the 95% confidence interval was 3.0 to 14.1 minutes under the independence approximation. The total dose was 7 mg versus 4 mg, and the group with the higher total dose given once daily had the smaller effect. Whether this reflects dosing frequency cannot be determined from this comparison. Each group had about 20 participants, blood concentration data were not used, and the comparison was added after the results were seen.

## Discussion

The MWT difference between 1 mg and 2 mg was about 3 minutes; the difference from placebo was about 14 minutes with 1 mg and about 17 minutes with 2 mg. The point estimate that the placebo difference with 1 mg is about 80% of that with 2 mg is consistent with the reading that most of the effect is obtained at 1 mg. The 95% interval for the difference was −0.1 to 6.8 minutes under the independence approximation and 0.5 to 6.2 minutes under the shared-placebo approximation. The two approximations can be regarded as bracketing the true interval, but because the covariance of the trial's model is not posted, it cannot be judged which is closer. At the upper end (6.2 to 6.8 minutes), the effect of 1 mg could be clearly smaller than that of 2 mg; at the lower end (−0.1 to 0.5 minutes), there could be almost no difference. A lower bound near 0 means that almost no additional effect cannot be excluded; it is not evidence that 2 mg is slightly more effective. The interval excludes neither an additional effect of about 3 minutes nor almost none. Why the usual Japanese dose is 1 mg is not examined here, because I did not read the review documents.

For insomnia, pollakiuria, micturition urgency and salivary hypersecretion, point estimates were similar at the two doses; headache, nasopharyngitis and weight increased were higher with 2 mg. The intervals are wide and exclude neither small nor large differences. Serious adverse events were one case at each dose; discontinuations and severity were not examined, so whether safety is equivalent at the two doses cannot be judged from these data.

The MWT change under the same 2 mg twice-daily regimen differed by 7.6 minutes between trials, and the Q test (p = 0.004) indicates that chance variation alone does not readily explain it. This Q test, however, lines up group means from different populations, durations and outcome definitions, and is weak grounds for quantifying differences between trials. The placebo-group changes are similar across the three trials, but the cause of the difference in the drug groups cannot be identified. The numbers for a dose in the trials where it was used therefore cannot, on their own, describe the magnitude of effect at the approved dose.

The dosing-frequency comparison is limited to the observation that the once-daily group had the smaller effect, and the mechanism is not examined. The timing of MWT measurement relative to drug exposure may confound the comparison, but this was not examined because blood concentration data are unavailable.

## Limitations

- A comparison between groups has the protection of randomization only within each trial. Comparisons across trials include differences in population.
- The confidence interval for the 2 mg versus 1 mg difference is an approximation. Two versions are shown, the independence approximation and the shared-placebo approximation. Neither is the trial's own analysis interval, and because the covariance of the trial's model is not posted, it cannot be judged which is closer to the true interval. The choice of approximation changes whether the lower bound includes 0.
- The 2 mg versus 1 mg comparison lies outside the trials' primary comparisons (each dose versus placebo), and no power was designed for it.
- Adverse events are limited to events at or above the 5% reporting threshold and the serious adverse events posted in the registry (0 to 1 case per group). Frequencies by severity and reasons for discontinuation were not examined. Intervals for differences in proportions were computed for four events only, and that selection was post hoc.
- The dosing-frequency comparison is post hoc and exploratory, with about 20 participants per group and no blood concentration data.
- The approved contents of the Japanese labelling rely on the company announcement ([1](#ref-1)). The review report could not be examined.
- The check of the calculations is a reimplementation in R by the same author (`validate.R`), not third-party confirmation. Its scope is limited to the 2 mg versus 1 mg MWT difference (independence approximation) and the between-trial Q test; ESS, Wilson intervals, differences in proportions, the dosing-frequency comparison and I² were not cross-checked by the reimplementation.
- The article was written with an AI (Claude) and reviewed three times by AI reviewers commissioned by the same author; this is not confirmation by a human third party.

## Conclusion

In FirstLight, 2 mg twice daily added about 3 minutes in MWT and about 2 points in ESS (a negative change is an improvement) relative to 1 mg twice daily, but for both outcomes the interval reaches close to 0, and whether it includes 0 depends on the approximation chosen. For insomnia, pollakiuria, micturition urgency and salivary hypersecretion the point estimates were similar, and headache was higher with 2 mg. The intervals are wide. The MWT change under the same 2 mg twice-daily regimen differed across the three trials, 15.9 to 23.5 minutes, and the cause cannot be determined. The phase 2b once-daily 7 mg group had an 8.5-minute smaller effect than the twice-daily 2 mg group, in a post hoc, exploratory comparison. Whether the difference between 1 mg and 2 mg is clinically meaningful, and whether safety is equivalent, cannot be judged from these data.

## Data and code availability

The inputs (JSON files of the registered ClinicalTrials.gov results), analysis code, result tables and figures are included in the rerun package. The registered results are public data and contain no individual participant data. Run as follows (Python 3.12 with numpy, pandas, scipy and matplotlib; R 4.5.3 with jsonlite). No random numbers are used.

```bash
python -m pytest -q test_analysis.py && python analysis.py && python figures.py && Rscript validate.R
```

`analysis.py` produces the tables (`results/`), `test_analysis.py` (4 tests) checks them, and `figures.py` produces the figures. `validate.R` recomputes the MWT increment and the Q test and records agreement in `results/validation.json`.

The full re-run materials are in the [companion archive](shared/oveporexton-orexin-dose/oveporexton-orexin-dose-companion.zip).


## References

<span id="ref-1"></span>1. Takeda. ORZEYFUL Approved in Japan to Treat Narcolepsy Type 1 [Internet]. Takeda; 2026 Aug 24 [cited 2026 Oct 30]. Available from: [https://www.takeda.com/newsroom/newsreleases/2026/orzeyful-approved-japan-narcolepsy/](https://www.takeda.com/newsroom/newsreleases/2026/orzeyful-approved-japan-narcolepsy/).

<span id="ref-2"></span>2. Takeda. A Study of TAK-861 in Participants With Narcolepsy Type 1 [Dataset; ClinicalTrials.gov identifier NCT05687903]. ClinicalTrials.gov; results first posted 2025 Jan 9 [cited 2026 Oct 30]. Available from: [https://clinicaltrials.gov/study/NCT05687903](https://clinicaltrials.gov/study/NCT05687903).

<span id="ref-3"></span>3. Takeda. A Study of TAK-861 for the Treatment of Narcolepsy Type 1 [Dataset; ClinicalTrials.gov identifier NCT06470828]. ClinicalTrials.gov; results first posted 2026 Aug 31 [cited 2026 Oct 30]. Available from: [https://clinicaltrials.gov/study/NCT06470828](https://clinicaltrials.gov/study/NCT06470828).

<span id="ref-4"></span>4. Takeda. A Study of TAK-861 in People With Narcolepsy Type 1 [Dataset; ClinicalTrials.gov identifier NCT06505031]. ClinicalTrials.gov; results first posted 2026 Jul 16 [cited 2026 Oct 30]. Available from: [https://clinicaltrials.gov/study/NCT06505031](https://clinicaltrials.gov/study/NCT06505031).
