Reference date: the facts in this article are as of 5 November 2026.

PERSEE (GFPC 01-2020; GFPC is a French thoracic oncology group), a phase 3 trial of first-line pembrolizumab alone versus pembrolizumab plus platinum-based chemotherapy in advanced non-small cell lung cancer with PD-L1 (an immune checkpoint molecule on tumor cells) expression of 50% or higher, was published in the Annals of Oncology in October 2026 and presented at the European Society for Medical Oncology (ESMO) 2026 ([1](#ref-1), [2](#ref-2)). Progression-free survival (PFS) by blinded central review had a median of 16.1 versus 6.9 months (hazard ratio 0.56), and overall survival (OS) had a median of 50.2 versus 29.9 months (hazard ratio 0.77, 95% confidence interval 0.56 to 1.05), a difference that was not statistically significant ([1](#ref-1)). This note puts the published numbers (medians, survival rates at fixed times, response rates, adverse events) in one table and recomputes from them how much of the PFS difference remains in OS, why a difference in medians differs from the hazard ratio, and how the adverse-event difference sits beside them. Of these numbers, the survival rates at fixed times and the response rates come from conference coverage and have not been checked against the paper. It is an organization of how to read the numbers, not a treatment recommendation.

## Scope and sources

For the Annals of Oncology paper I read only the abstract (Europe PMC record); the publisher's page refused the connection, so the full text could not be checked ([1](#ref-1)). Survival rates at fixed times, response rates, duration of response, subgroup hazard ratios and the date of the presentation come from articles reporting the ESMO 2026 presentation (OncoDaily and Targeted Oncology) ([2](#ref-2), [3](#ref-3)). These values have not been checked against the paper, and the data cut-off date is as stated in the coverage (7 April 2026). Individual patient data are not public. The numbers are of two kinds. Values reported by the paper and the coverage are quoted as printed. Values I calculated (hazard ratios back-calculated from survival rates at fixed times, approximate p values, intervals for differences) are marked as my calculation. The survival rates at fixed times are Kaplan–Meier estimates counted from randomization; they are not a landmark analysis in the usual sense (an analysis restricted to patients alive at a given time). Table 1 shows the main numbers and their sources.

Table 1. Published PERSEE numbers and sources ([1](#ref-1) abstract, [2](#ref-2) OncoDaily, [3](#ref-3) Targeted Oncology).

| Endpoint | Pembrolizumab + chemotherapy | Pembrolizumab alone | Reported effect | Source |
| --- | --- | --- | --- | --- |
| Patients randomized | 160 | 161 | 321 in total | [1] |
| PFS median (blinded central review) | 16.1 months | 6.9 months | HR 0.56 (95% CI 0.43 to 0.74) | [1] median and HR; [2] CI |
| PFS at 12 / 24 / 36 months | 54.6 / 45.2 / 39.2% | 33.9 / 24.9 / 20.8% | not reported | [2] |
| OS median | 50.2 months | 29.9 months | HR 0.77 (95% CI 0.56 to 1.05) | [1] |
| OS at 12 / 24 / 36 / 48 months | 78.8 / 64.4 / 55.4 / 50.9% | 73.3 / 56.2 / 44.9 / 38.9% | not reported | [2] |
| Objective response rate | 77.5% | 50.3% | CI not reported | [2], [3] |
| Median duration of response | 30.0 months | 15.6 months | CI not reported | [2] |
| Grade 3 or higher treatment-related AEs | 53.8% (abstract: 54%) | 19.3% (abstract: 19%) | not applicable | [1], [2] |
| Early progression (definition not stated) | 5.8% | 26.5% | not reported | [3] |

Table 1 notes: PFS is progression-free survival, OS overall survival, HR hazard ratio, CI confidence interval, AE adverse event.

## Discussion by issue

### The difference in medians looks larger than the hazard ratio

The difference in median PFS is 9.2 months and in OS 20.3 months. Only if survival times are exponential (constant hazard) does the ratio of medians fix the hazard ratio. In that case it would be 6.9 ÷ 16.1 = 0.43 for PFS and 29.9 ÷ 50.2 = 0.60 for OS (my calculation). The reported hazard ratios (0.56 and 0.77) are both closer to 1. This shows that the survival curves are not exponential in shape, but not that hazards are non-proportional: indeed, the PFS hazard ratios back-calculated below from the survival rates at fixed times are nearly constant. Also, the median OS of the combination arm (50.2 months) is longer than the median follow-up (38.7 months), so it is an unstable estimate, and no interval is given. The reported hazard ratio (an average effect over the whole trial) and the difference in medians are different quantities.

A hazard ratio can also be back-calculated from the survival rates at fixed times (under proportional hazards, from two survival probabilities as \(\ln S_1 / \ln S_0\), where \(S_1\) and \(S_0\) are the survival rates of the combination and the single-drug arms). For PFS it is 0.56 at 12 months, 0.57 at 24 months and 0.60 at 36 months, close to the reported 0.56 and nearly constant. For OS it is 0.77 at 12 months, 0.76 at 24, 0.74 at 36 and 0.72 at 48 (my calculation, Figure 1). The small decrease in the OS values is within rounding and the sampling error of the estimates at each time (no confidence intervals are reported), and cannot be called a trend.

![Figure 1. Reported survival rates at fixed times in PERSEE (Kaplan–Meier estimates counted from randomization). Left: PFS; right: OS. Points are the published values only; the shape of the curves is not estimated (my figure, published numbers).](shared/persee-pfs-os-landmarks/figures/01-landmark-rates.png)

### The difference in survival rates is constant for PFS and widens over time for OS

The differences between the arms in survival rates at fixed times (percentage points) are, for PFS, 20.7 at 12 months, 20.3 at 24 months and 18.4 at 36 months, nearly constant. For OS they widen: 5.5 at 12 months, 8.2 at 24, 10.5 at 36 and 12.0 at 48 (my calculation, Figure 2). Even if the OS hazard ratio were constant at 0.77, however, the difference in survival rates would widen over time. Applying the power 0.77 to the survival rate of the single-drug arm gives expected differences of 5.4, 8.0, 9.1 and 9.4, and the observed differences exceed these by 1.4 points at 36 months and 2.6 at 48 months (my calculation). This excess may lie within rounding and sampling error and is not evidence of a stronger effect later.

At 12 months the OS difference (5.5) is small against the PFS difference (20.7). Not every patient whose time to progression is extended shows a survival difference at the same time. Later treatment (including crossover) was not reported in what I could check; this comparison probably includes upfront combination versus sequential treatment with chemotherapy after progression, which can dilute the OS difference.

### The OS difference is not significant but cannot be called small

From the width of the 95% confidence interval of the OS hazard ratio of 0.77 (0.56 to 1.05), the standard error of the log hazard ratio is about 0.16, the test statistic z = −1.63 and the two-sided p value about 0.10 (my calculation, assuming the reported interval is symmetric on the log scale). The interval spans from a risk reduction of about 44% to an increase of about 5%. The coverage states that the trial was not powered to detect an OS difference (it was not designed around OS) ([2](#ref-2), [3](#ref-3)). It is therefore best read not as "no difference in OS" but as "a difference in OS was not established in this trial".

### Grade 3 or higher treatment-related adverse events are about 35 per 100 patients higher

The proportion of grade 3 or higher treatment-related adverse events is 53.8% versus 19.3%, a difference in proportions of 34.5 points (the abstract gives 54% versus 19%, a difference of 35). In the combination arm, 48% stopped chemotherapy because of adverse events ([3](#ref-3)). Grade 3 or higher immune-related events were the same in both arms, 13% ([1](#ref-1)). These values are cumulative proportions over the whole treatment and are of a different kind from the differences in survival rates at fixed times. Quality of life, grade 5 events and the toxicity of chemotherapy that the single-drug arm received later are not part of the numbers I could check. This note shows the two side by side but does not add and subtract them as benefit and harm in one unit (Figure 2).

![Figure 2. Differences between the arms in survival rates at fixed times (PFS and OS, differences of Kaplan–Meier estimates) and in the proportion of grade 3 or higher treatment-related adverse events (whole treatment). Descriptive (my calculation, published numbers; no PFS value is reported at 48 months).](shared/persee-pfs-os-landmarks/figures/02-landmark-differences-vs-toxicity.png)

### The response rate differs by 27 points and the duration of response about twofold

The response rate is 77.5% versus 50.3% ([2](#ref-2), [3](#ref-3)). From the percentages, the numbers of responders can be estimated as 124 (of 160) and 81 (of 161), though the denominator in the coverage may be evaluable patients and the actual numbers may differ; the difference is 27.2 points (95% interval 16.8 to 36.8, Newcombe method; my calculation). The median duration of response is 30.0 versus 15.6 months, about 1.9-fold. A larger response rate and a longer duration of response go in the same direction as the PFS difference. Early progression is reported as 5.8% versus 26.5%, but the coverage does not state its definition (time point) ([3](#ref-3)).

### What is not reported, and limits on interpretation

In what I could check, later therapy and crossover, the assumptions behind the sample size, the definition of early progression, patient-reported outcomes and details of discontinuation were not reported. The trial is open label; PFS was assessed by blinded central review, which reduces assessment bias but does not remove bias arising from how treatment is delivered. In PD-L1 subgroups, hazard ratios of 0.46 (50 to 74%), 0.62 (75 to 100%) and 0.60 (90 to 100%, upper bound of the interval 1.00) are reported, but the endpoint is not stated, the strata overlap (90 to 100% lies within 75 to 100%), the lowest stratum shows the largest effect, and no test of a difference in effect is reported, so they should be interpreted with caution ([2](#ref-2)).

## Overall assessment

What could be confirmed as fact is as follows. PFS was significantly prolonged, by 9.2 months in median and with a hazard ratio of 0.56, and the differences in survival rates at fixed times are nearly constant at about 20 points from 12 to 36 months. The OS difference in medians is 20.3 months and the hazard ratio 0.77 (interval 0.56 to 1.05), not established. The OS differences at fixed times widened from 5.5 to 12.0 points, close to the size by which they widen even under a constant hazard ratio. The proportion of grade 3 or higher treatment-related adverse events is 34.5 points higher.

By interpretation: differences in medians look like larger effects than the hazard ratio, so it is appropriate to read survival rates at fixed times together with the hazard ratio. The OS difference is not established, but the interval spans from benefit to a small disadvantage. How to weigh the increase in adverse events against the PFS improvement depends on patients' values and on later treatment and is outside this note. This article must not be used as a basis for an individual patient's treatment choice.

## Limitations

- The numbers are from the abstract and conference coverage. The full text could not be checked, and the coverage values (survival rates at fixed times, response rate and so on) have not been checked against the paper. The data cut-off date is as stated in the coverage.
- Without individual patient data, the survival curves were not reconstructed. Hazard ratios back-calculated from survival rates at fixed times depend on proportional hazards, on rounding and on sampling error (intervals are not reported).
- The approximate p value for OS is an estimate from the reported confidence interval, not the result of a test.
- Placing adverse events beside PFS and OS differences is a descriptive pairing of quantities of different kinds, not a comparison of benefit and harm.
- This note makes no treatment recommendation.
- The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

In the published PERSEE numbers, adding chemotherapy gives PFS rates about 20 points higher at 12 to 36 months, and the OS difference is not established. Differences in medians look larger than the hazard ratio. The proportion of grade 3 or higher treatment-related adverse events is about 35 points higher. The numbers are best read by survival rate at fixed times and hazard ratio, and the balance against adverse events is a separate judgement.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive (the distribution file of this article). Run with Python 3.12, NumPy 2.2, SciPy 1.14, pandas 2.2 and Matplotlib 3.9: `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`; the output can be compared with the tables in `results/`. The inputs are the numbers printed in the abstract and coverage, written at the top of the code. No random numbers are used. No individual patient data are used.

The full re-run materials are in the [companion archive](shared/persee-pfs-os-landmarks/persee-pfs-os-landmarks-companion.zip).


## References

<span id="ref-1"></span>1. Descourt R, Mogenet A, Consigny M, et al. Pembrolizumab with or without platinum-based chemotherapy as first-line treatment in advanced NSCLC expressing PD-L1 ≥50%: the PERSEE randomized phase III trial (GFPC 01-2020). Ann Oncol [Internet]. Epub ahead of print 2026 Oct 25 [cited 2026 Nov 5]. [doi:10.1016/j.annonc.2026.10.108](https://doi.org/10.1016/j.annonc.2026.10.108). Abstract read through the Europe PMC record (PMID 42927854); full text not available to the author.

<span id="ref-2"></span>2. OncoDaily. PERSEE: adding chemotherapy to pembrolizumab significantly extends PFS in PD-L1-high NSCLC [Internet]. 2026 Oct 25 [cited 2026 Nov 5]. Available from: [https://oncodaily.com/oncolibrary/lung-oncology/persee-esmo26](https://oncodaily.com/oncolibrary/lung-oncology/persee-esmo26). News coverage of the ESMO 2026 presentation (Madrid, 25 October 2026); values not checked against the paper.

<span id="ref-3"></span>3. Targeted Oncology. ESMO 2026: ADCs and new combinations advance lung cancer care [Internet]. 2026 Oct [cited 2026 Nov 5]. Available from: [https://www.targetedonc.com/view/esmo-2026-adcs-and-new-combinations-advance-lung-cancer-care](https://www.targetedonc.com/view/esmo-2026-adcs-and-new-combinations-advance-lung-cancer-care). News coverage of the ESMO 2026 presentation; values not checked against the paper.
