## Definition

A parameter is **practically identifiable** when the available data (their number, sampling times, doses and assay error) determine it with a finite, acceptably narrow confidence interval. A structurally identifiable parameter can still fail this test, for example when sampling is too sparse or too late.

## How it shows up

- **Expected precision:** for a given design, the expected standard error of each parameter can be calculated before the study from the Fisher information.
- **Likelihood profile:** after fitting, the likelihood is profiled over one parameter. A bounded profile means the data determine it; a flat profile means the data cannot tell values apart.

## What to do when it fails

First check whether the model is structurally identifiable. If it is, the cause is the design: add a sampling time, a measurement, a dose level or follow-up time, or fix a parameter to an external value. The [nimotuzumab analysis](../writing/nimotuzumab-poppk-en.html) asks, for example, how complex a population PK model needs to be for an exposure comparison with measured PK data.

## Software

[pkident](../software/pkident.html) calculates expected standard errors for a sampling design, suggests which added measurement would help, and classifies likelihood profiles of nlmixr2 fits as bounded or flat. Decisions are local to the assumed parameter values, and population designs are not covered. See also [structural identifiability](structural-identifiability.html).
