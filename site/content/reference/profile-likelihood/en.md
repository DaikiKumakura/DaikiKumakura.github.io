## Definition

The **profile likelihood** of a parameter is the maximum of the likelihood over all the other parameters, plotted against the value of the parameter. It shows how much worse the fit becomes as the parameter moves away from its estimate.

## Confidence intervals

A confidence interval can be read from the profile as the range where twice the drop of the log-likelihood stays below a threshold (3.84 for 95% with one parameter, from the chi-square distribution). Unlike a Wald interval it can be asymmetric.

## Bounded and flat profiles

- **Bounded:** the profile rises on both sides, so the data determine the parameter.
- **Flat or one-sided:** the profile stays near the maximum on one or both sides, so the data cannot tell values apart. This is a [practical identifiability](practical-identifiability.html) problem, or, if the model structure causes it, a [structural identifiability](structural-identifiability.html) one.

## On this site

The R package [pkident](../software/pkident.html) classifies the likelihood profiles of nlmixr2 fits as bounded or flat, to tell whether a flat profile is a property of the model or of the data. The [nimotuzumab analysis](../writing/nimotuzumab-poppk-en.html) asks how complex a model the data can support.
