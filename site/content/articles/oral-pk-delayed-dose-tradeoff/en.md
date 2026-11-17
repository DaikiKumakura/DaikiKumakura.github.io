If a dose scheduled every 12 hours is taken nine hours late, just three hours remain before the next scheduled dose. Catching up on the late dose still leaves a choice of timing, and that choice changes the next concentration peak. Clark and Lawley studied irregular dosing with pharmacokinetic models ([1](#ref-1)). Here, I calculate the low and high concentrations in separate windows.

## Keeping or shifting the next scheduled time

The model starts at steady state. It has one compartment, an absorption rate constant of 1 per hour, and an elimination half-life of eight hours. The dose divided by apparent volume is one concentration unit. The contribution $t$ hours after a dose is $k_a(e^{-kt}-e^{-k_at})/(k_a-k)$, and zero before dosing. I set $k=log(2)/8$ and summed the previous regular doses as geometric series, then added or subtracted deviations from the schedule. I calculated extrema on a 0.001-hour grid in two windows measured from the scheduled dose at hour zero.

**Table 1. Concentration extrema on a 0.001-hour grid**

| Change to the schedule at hours 0, 12 and 24 | Minimum from hour 0 to just before hour 12 | Maximum from hour 12 through hour 24 |
| --- | ---: | ---: |
| No change | 0.599 | 1.278 |
| Skip the dose at hour 0 | 0.212 | 0.962 |
| Move the dose to hour 9 and keep hours 12 and 24 | 0.275 | 1.653 |
| Move the dose to hour 9 and continue every 12 hours | 0.275 | 1.184 |

The final two rows of Table 1 have the same profile up to hour 12. Keeping the next dose at hour 12 raises the second window's maximum to 1.653, about 1.29 times the planned peak. Moving it to hour 21 lowers that maximum to 1.184 and shifts the dosing schedule. Two schedules can pass through the same minimum and still differ in their next peak and dosing times.

The model assumes linear absorption and elimination and specifies no efficacy or toxicity threshold. A 24-hour calculation cannot establish long-term exposure or how to handle a late dose of an actual drug.

## Data and code availability

The calculation uses hypothetical inputs. [Download the Python code and output](shared/oral-pk-delayed-dose-tradeoff/companion.zip).

## References

1. <a id="ref-1"></a> [Clark ED, Lawley SD. Should patients skip late doses of medication? A pharmacokinetic perspective. J Pharmacokinet Pharmacodyn. 2022;49(4):429–444.](https://doi.org/10.1007/s10928-022-09812-0)
