## Definition

A parameter is **structurally identifiable** if, with continuous, noise-free observation of the chosen model outputs after known doses, only one value of it reproduces the output. If many values give exactly the same output, the parameter is not identifiable, however much data are collected.

This depends only on the model structure, the observed outputs and the doses. It says nothing about noise or sampling times.

## Example: V/F

After oral dosing with no intravenous data, the bioavailability F cannot be separated from the volume V and the clearance CL. Only combinations such as V/F and CL/F can be determined. Fitting V and F separately then gives arbitrary values, and the fit reports a model that looks well determined when it is not.

## Why it matters

Checking structural identifiability before fitting tells whether a flat likelihood or an unstable estimate comes from the model itself. If it does, collecting more of the same data does not help; the model or the measured outputs have to change.

## Software

The R package [pkident](../software/pkident.html) checks structural identifiability of PK/PD ODE models built on rxode2, and compares two independent structural methods. Practical identifiability, the case with real noisy data, is a separate question: see [practical identifiability](practical-identifiability.html).
