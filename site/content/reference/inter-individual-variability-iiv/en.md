## Definition

**Inter-individual variability (IIV, also between-subject variability)** is how much a PK parameter such as clearance differs between patients. In a population model it is a random effect, usually log-normal: the individual's parameter is the typical value times exp(η), with η normally distributed with variance **ω²**.

## Conversion to a coefficient of variation

For a log-normal distribution, **CV ≈ √(exp(ω²) − 1)**. A variance of 0.134 corresponds to a CV of about 38%.

## Not residual error

IIV describes differences between patients in the parameters. **Residual error** describes the remaining difference between each observation and the model prediction for that patient. They are estimated separately.

## On this site

The reimplemented pembrolizumab model has an IIV of 38% CV on clearance and 21% CV on volume, and the simulated spread of exposure in the [anti-PD-1 analysis](../writing/fixed-vs-weight-dosing-en.html) comes from these values together with body weight. The [mosunetuzumab reimplementation](../writing/mosunetuzumab-public-pk-en.html) checks that the covariance matrix of the random effects is positive definite before simulating. See also [population PK models](population-pk-nlme.html).
