## Purpose

This sample demonstrates the publishing system. It calculates the analytical solution of logistic growth rather than fitting observed data.

## Model

\\[\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)\\]

N is population size, r is the growth rate, and K is carrying capacity.

## Code

The code below comes from the same source file as the Japanese version. The build does not execute R.

{{code:r:model.R}}

## Interpretation

Under these conditions, the population approaches carrying capacity 100 from an initial value of 5. The model does not represent changes in the environment over time.
