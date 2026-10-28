## Definition

The **Emax model** is E = E0 + Emax × C / (EC50 + C), where C is the concentration, E0 the baseline effect, **Emax** the maximum effect and **EC50** the concentration that gives half of Emax. For an inhibitory effect the form is E = E0 × (1 − Imax × C / (IC50 + C)).

## The Hill exponent

The **sigmoid Emax (Hill) model** adds an exponent γ: E = E0 + Emax × C^γ / (EC50^γ + C^γ). A larger γ makes the curve steeper around EC50; γ = 1 gives the simple Emax model.

## Use

These functions give the shape of the concentration–effect relationship in [indirect response models](indirect-response-model.html) and in direct-effect models. EC50 and γ often cannot be estimated well from sparse data; see [practical identifiability](practical-identifiability.html).

## On this site

In the [warfarin PK/PD analysis](../writing/warfarin-pkpd.html) the maximum inhibition is fixed to one and the Hill exponent is a typical-value parameter without between-subject variability. The [RAS inhibitor analysis](../writing/ras-inhibitor-target-coverage.html) links drug concentration to a target-coverage response.
