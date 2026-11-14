## Definition

A BLQ record is a concentration below the lower limit of quantification (LLOQ) of the assay. The true value lies between zero and the LLOQ; it is censored, not zero.

## How it is used

The likelihood-based approach known as the M3 method (Beal, 2001) models the probability that a concentration falls below the LLOQ, and keeps the record in the fit. Simpler options, such as dropping the record or imputing half the LLOQ, are also seen; each changes the estimates differently. Report how many records were BLQ and how they were handled.

## Common pitfalls

- Setting every BLQ record to zero can distort the terminal phase and the estimated residual variability.
- Dropping BLQ records after a dose biases the terminal half-life upward when the omitted late samples are the lowest ones.

## Related topics

- [Population PK and nonlinear mixed-effects (NLME) models](population-pk-nlme.html)
- [Residual variability in population PK](residual-variability.html)

## References

- [FDA. Population Pharmacokinetics. 2022.](https://www.fda.gov/media/128793/download)
