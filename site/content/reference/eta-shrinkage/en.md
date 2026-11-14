## Definition

Eta (η) is the individual deviation of a parameter from the population typical value. Shrinkage measures how much the individual estimates cluster toward zero: η-shrinkage = 1 − SD(η̂)/ω, where ω is the estimated standard deviation of the random effect. It is high when each patient contributes little information about that parameter.

## How it is used

It is reported with population PK results. High shrinkage, often flagged above about 20–30%, makes plots of individual estimates against covariates, and diagnostics built on them, less reliable. Epsilon (ε) shrinkage is a separate quantity for the residual error.

## Common pitfalls

- Concluding that no covariate relationship exists from plots of shrunken individual estimates.
- Treating the covariate model as unsupported without testing the covariate in the model fitted to the original concentrations.

## Related topics

- [Population PK and nonlinear mixed-effects (NLME) models](population-pk-nlme.html)
- [Inter-individual variability (IIV)](inter-individual-variability-iiv.html)

## References

- [FDA. Population Pharmacokinetics. 2022.](https://www.fda.gov/media/128793/download)
