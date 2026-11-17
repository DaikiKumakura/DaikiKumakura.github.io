How much of an exposure–response slope can repeated sampling recover? Averaging reduces errors that change from one measurement to the next. Any error shared by a patient's measurements survives the average. Repeated blood-pressure measurements have been used to correct regression dilution in vascular risk studies ([1](#ref-1)). A hypothetical exposure–response model shows what repeated measurements can identify.

## Errors that averaging leaves behind

Let $X$ be true exposure and $Y=α+βX+ε$ the response. Patient-level measurement $j$ is $W_j=X+b+u_j$, where $b$ is shared within a patient and $u_j$ varies independently by measurement. Assume $X$, $b$, each $u_j$, and $ε$ are mutually independent. The variances of $X$ and $u_j$ are both 1. In a simple regression on the mean of $m$ measurements, the covariance with $Y$ is $β$ and the variance of the mean exposure is $1+Var(b)+1/m$. If the true slope is nonzero, the ratio to it is the reciprocal of that variance.

**Table 1. Population regression slope divided by the true slope**

| Measurements | No shared error | Shared error variance 0.25 |
| --- | ---: | ---: |
| 1 | 0.500 | 0.444 |
| 4 | 0.800 | 0.667 |
| 16 | 0.941 | 0.762 |
| Infinite | 1.000 | 0.800 |

In the right-hand column of Table 1, the correlation between two measurements is $1.25/2.25=0.556$. Dividing the single-measurement slope by that correlation still recovers only 80% of the true slope. True exposure accounts for only 1 of the 1.25 variance units shared across measurements. Repeating the same assay captures the combined variance of true exposure and shared error. A second method for the same exposure can separate them through the cross-method covariance if its errors are uncorrelated with true exposure and with the first method’s errors.

These are population coefficients from a linear model. The ratios do not carry over directly to time-varying concentration, outcome-dependent error, or a nonlinear drug response.

## Data and code availability

The calculation uses hypothetical inputs. [Download the Python code and output](shared/exposure-repeat-shared-error/companion.zip).

## References

1. <a id="ref-1"></a> [MacMahon S, Peto R, Cutler J, Collins R, Sorlie P, Neaton J, et al. Blood pressure, stroke, and coronary heart disease. Part 1, Prolonged differences in blood pressure: prospective observational studies corrected for the regression dilution bias. Lancet. 1990;335(8692):765–774.](https://doi.org/10.1016/0140-6736(90)90878-9)
