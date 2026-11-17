At extended follow-up in DeLLphi-304, median overall survival (OS) was 13.6 months with tarlatamab and 8.4 months with chemotherapy, a difference of 5.2 months. If the quantity of interest is average survival through month 24, how much can that difference and the two survival probabilities in the Annals of Oncology abstract tell us? The randomized trial assigned 254 patients with small-cell lung cancer progressing on or after platinum-based chemotherapy to tarlatamab and 255 to chemotherapy. The data cutoff was February 18, 2026 ([1](#ref-1)).

## Bounding the area from the published summary

Restricted mean survival time (RMST) through month 24 is the area under the survival curve from randomization to that time ([2](#ref-2)). Reported survival at months 12 and 24 was 55.9% and 30.3% with tarlatamab and 39.0% and 14.9% with chemotherapy ([1](#ref-1)). I treat those reported values as fixed and assume survival starts at 1 and is nonincreasing. The median is the first time survival reaches or falls below 0.5. A drop past 0.5 at the median is allowed.

Split follow-up at the median and the available landmarks. A lower bound for survival in each interval is the largest known survival probability to its right, with a floor of 0.5 before the median. The upper bound is the smallest known probability to its left, with a ceiling of 0.5 after the median. Multiply each bound by the interval width and sum the areas. For tarlatamab, for example, the lower bound is $12(0.559)+1.6(0.5)+10.4(0.303)=10.6592$ months.

**Table 1.** Bounds for RMST through month 24 as published summary values are added. The difference subtracts chemotherapy from tarlatamab.

| Information used | Tarlatamab (months) | Chemotherapy (months) | Difference (months) |
| --- | ---: | ---: | ---: |
| Median only | 6.80 to 18.80 | 4.20 to 16.20 | −9.40 to 14.60 |
| Median and 12-month OS | 7.51 to 18.09 | 5.60 to 14.88 | −7.37 to 12.49 |
| Median and 12- and 24-month OS | 10.66 to 18.09 | 7.39 to 14.88 | −4.22 to 10.70 |

In Table 1, adding survival at months 12 and 24 narrows the range for the difference from 24.0 to 14.9 months. The range still includes zero. The lower limit subtracts the upper bound for chemotherapy from the lower bound for tarlatamab. The upper limit uses the other pair. Step functions with drops near the interval endpoints approach the limits. When a premedian interval has a lower bound of 0.5, approach it with survival just above 0.5. Further landmarks or information about the curve could narrow the range.

These bounds are conditional on the rounded published values and do not constitute a confidence interval. It measures information lost by replacing the curve with a few summaries. The inclusion of zero describes the limits of those summaries and addresses a different question from the trial’s reported OS result. [Figure 1A in the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13718749/#F1) shows the Kaplan–Meier curves, which are outside this calculation ([1](#ref-1)). A 24-month RMST contrast calls for integrating the curves or consulting a trial-based estimate and its uncertainty. The 5.2-month difference between medians answers a different question.

## Data and code availability

The inputs are median and landmark survival values from the paper. I used no individual patient data. [The reproducibility ZIP](shared/survival-landmark-rmst-bounds/companion.zip) contains the Python code and output.

## References

1. <a id="ref-1"></a> Rudin CM, Ahn MJ, Schuler M, Blackhall FH, Mountzios G, Yoshida T, et al. Extended follow-up of tarlatamab in patients with small-cell lung cancer after platinum-based chemotherapy in the randomized phase III DeLLphi-304 study. Ann Oncol. 2026. [doi:10.1016/j.annonc.2026.10.095](https://doi.org/10.1016/j.annonc.2026.10.095).
2. <a id="ref-2"></a> Zhao L, Claggett B, Tian L, Uno H, Pfeffer MA, Solomon SD, et al. On the restricted mean survival time curve in survival analysis. Biometrics. 2016;72(1):215–221. [doi:10.1111/biom.12384](https://doi.org/10.1111/biom.12384).
