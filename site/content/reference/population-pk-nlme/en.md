## Definition

A **population PK (PopPK) model** describes the drug's typical profile in a patient population together with the variability around it. It is estimated from the pooled data of many patients, which may be sparse for each patient, with a **nonlinear mixed-effects (NLME)** model: nonlinear because concentrations are nonlinear functions of the parameters, mixed because it has both fixed and random effects.

## Parts of the model

- **Fixed effects:** typical values of the parameters (for example CL and V) and the effects of covariates such as body weight ([covariates](allometric-scaling-covariates.html)).
- **Random effects:** the [between-subject variability](inter-individual-variability-iiv.html) of the parameters.
- **Residual error:** the remaining difference between observation and prediction.

## Software

Commonly used tools are NONMEM, Monolix and nlmixr2 (R). On this site, nlmixr2 and rxode2 were used in the [nimotuzumab](../writing/nimotuzumab-poppk-en.html) and [warfarin](../writing/warfarin-pkpd.html) analyses, and [published models were reimplemented](poppk-reimplementation.html) from their tables, as for [mosunetuzumab](../writing/mosunetuzumab-public-pk-en.html).
