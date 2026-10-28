## Definition

A **covariate** is a patient characteristic that explains part of the variability of a parameter. For body weight, the usual form is **allometric scaling**:

parameter = typical value × (weight / reference weight)^exponent

Theoretical exponents are 0.75 for clearances and 1 for volumes, but fitted values for a given drug differ and are reported with uncertainty.

## Why the exponent matters for dosing

If clearance scales with weight^0.6, then a dose proportional to weight (mg/kg) gives an exposure that rises slightly with weight (AUC ∝ weight^0.4), while a fixed dose gives an exposure that falls with weight (AUC ∝ weight^−0.6). Near the reference weight the two are about the same; at the extremes they differ in opposite directions.

## On this site

The reimplemented pembrolizumab model has weight exponents of 0.595 on clearance and 0.489 on volume, and the nivolumab model 0.566 and 0.597. The [anti-PD-1 analysis](../writing/fixed-vs-weight-dosing-en.html) shows the consequence: with fixed doses the troughs fall in heavy patients, and with weight-based doses the first-interval troughs fall in light patients. The sensitivity analysis moves the exponent to the ends of its 95% interval. See also [fixed versus weight-based dosing](fixed-vs-weight-based-dosing.html) and [clearance](clearance-cl.html).
