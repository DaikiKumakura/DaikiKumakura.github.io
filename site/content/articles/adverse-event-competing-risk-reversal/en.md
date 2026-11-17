Censoring patients who die before their first adverse event can reverse the ranking of two groups at six months. The SAVVY study compared methods for estimating adverse event risks in trials with varying follow-up, including estimators that account for competing events ([1](#ref-1)). Constant hazards make it possible to see exactly how a ranking reversal arises.

## Death before the first adverse event

Let $a$ be the cause-specific hazard of a first adverse event and $d$ the cause-specific hazard of death before that event. Assume both hazards are constant among patients who have experienced neither event. Administrative censoring occurs at six months, with no other loss to follow-up. If deaths are censored, the limit of one minus the Kaplan–Meier estimate ($1-KM$) is $1-e^{-6a}$. Cumulative incidence with death as a competing event integrates the event-free probability $e^{-(a+d)s}$ times $a$, giving $a(1-e^{-6(a+d)})/(a+d)$.

**Table 1. First adverse event estimands at six months**

| Group | Adverse event hazard per month | Death hazard per month | $1-KM$ with deaths censored | Cumulative incidence |
| --- | ---: | ---: | ---: | ---: |
| A | 0.10 | 0.30 | 45.1% | 22.7% |
| B | 0.08 | 0.02 | 38.1% | 36.1% |

In Table 1, group A has a higher adverse event hazard among patients who have experienced neither an adverse event nor death. More patients in A die first, which reduces the time during which a first adverse event can occur. Its cumulative incidence is therefore lower. Any assessment of safety that includes the burden of death also needs to show the mortality results.

The hazards are hypothetical. This example estimates neither the safety of an actual drug nor the effect of an intervention that removes death. Recurring events and interruptions to follow-up are outside the calculation.

## Data and code availability

The calculation uses hypothetical inputs. [Download the Python code and output](shared/adverse-event-competing-risk-reversal/companion.zip).

## References

1. <a id="ref-1"></a> [Stegherr R, Schmoor C, Beyersmann J, Rufibach K, Jehl V, Brückner A, et al. Survival analysis for AdVerse events with VarYing follow-up times (SAVVY)-estimation of adverse event risks. Trials. 2021;22:420.](https://doi.org/10.1186/s13063-021-05354-x)
