## Definition

Reimplementing a published population PK (PopPK) model means rebuilding its structure, typical values, covariate effects and variability from the paper, its tables and its supplement (often NONMEM code) in software you control, for example R with rxode2 or Python. The original patient data are not needed.

## Why do it

A reimplemented model can answer questions the paper did not: how exposure changes with another dosing interval, how it varies across a weight distribution, or how sensitive a conclusion is to a parameter reported with uncertainty.

## How to check it

- Reproduce the typical values and the exposure summaries reported in the paper.
- Recompute key outputs with an independent implementation (a different solver or language) and compare.
- Record every inconsistency in the source, for example a table value that differs from its footnote, and test both versions as a sensitivity analysis.

## What it does not show

Agreement with published values shows that the model was rebuilt correctly. It does not validate the model for predicting a new patient population or a new regimen. The [mosunetuzumab reimplementation](../writing/mosunetuzumab-public-pk-en.html) separates these two points, and the [anti-PD-1 dosing analysis](../writing/fixed-vs-weight-dosing-en.html) reimplements two models and checks them against an independent calculation.
