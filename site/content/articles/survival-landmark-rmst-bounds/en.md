When two survival curves share a median, their areas can still differ. How closely can we pin down restricted mean survival time (RMST) through month 18 if we also know survival at months 6 and 18? RMST is the area under the survival curve up to a specified time ([1](#ref-1)). I used hypothetical summaries to calculate what monotonicity alone permits.

## Bounding the area between landmarks

Set baseline survival to one, six-month survival to 0.70, and 18-month survival to 0.30. The median is month 12, the first time survival reaches 0.50 or below. Between months 6 and 12, survival is above 0.50 and at most 0.70. Between months 12 and 18, it is at most 0.50 and at least 0.30. A jump past 0.50 at month 12 is allowed. Multiplying by the six-month widths gives a lower limit of $6(0.70+0.50+0.30)=9.0$ months and an upper limit of $6(1+0.70+0.50)=13.2$ months. If survival at month 12 is additionally fixed at exactly 0.50, linear interpolation gives 11.1 months.

## Two curves with the same median

Both examples set survival at month 12 to exactly 0.50. The upper curve retains the left value until the next landmark and drops there. It first reaches 0.50 or below at month 12, with an area of 13.2 months. A curve close to the lower limit drops to 0.70 at month 0.001, to 0.501 at month 6.001, to 0.50 at month 12 and to 0.30 at month 12.001. Its median is still 12 months and its area is 9.0067 months. Moving the early drops towards the left endpoints and 0.501 down towards 0.50 preserves the median while approaching 9.0. Because survival is above 0.50 between months 6 and 12, the area never reaches 9.0. Table 1 shows the two cases.

**Table 1.** Two possible curves with the same hypothetical summaries.

| Curve | S(6) | S(12) | S(18) | Median (months) | RMST to 18 months (months) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Late drops | 0.70 | 0.50 | 0.30 | 12 | 13.2000 |
| Early drops | 0.70 | 0.50 | 0.30 | 12 | 9.0067 |

Two arms sharing these summaries can have an RMST difference of either sign, depending on which curve belongs to which arm. The interval from 9.0 to 13.2 months describes what the summaries permit, conditional on exact landmark values. Rounding or sampling error changes those constraints. This calculation does not recover censoring, event counts or hazard ratios.

## Data and code availability

The survival probabilities are hypothetical. The [companion ZIP](shared/survival-landmark-rmst-bounds/companion.zip) contains the rectangle sums and step-curve checks.

## References

1. <a id="ref-1"></a> Zhao L, Claggett B, Tian L, Uno H, Pfeffer MA, Solomon SD, et al. On the restricted mean survival time curve in survival analysis. Biometrics. 2016;72(1):215–221. [doi:10.1111/biom.12384](https://doi.org/10.1111/biom.12384).
