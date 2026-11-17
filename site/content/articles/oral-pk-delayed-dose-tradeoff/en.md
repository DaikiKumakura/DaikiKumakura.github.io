The US prescribing information for daraxonrasib specifies 300 mg once daily and omitting a dose if it is more than four hours late ([1](#ref-1)). What can published pharmacokinetic (PK) summaries tell us about that cutoff? Models of irregular dosing can show low and high concentrations moving in different directions ([2](#ref-2)). I calculated the minimum concentration after one departure from the schedule and the maximum concentration the following day.

## Setting the profile from the label half-life and time to peak

I used a one-compartment model with first-order absorption and elimination, starting from steady state with a 24-hour dosing interval. I set $k=\log(2)/9.2$ from the reported terminal half-life of 9.2 hours. I then used bisection to choose the absorption rate $k_a$ whose steady-state time to maximum concentration matched the reported median of 2.2 hours ([1](#ref-1)). The label does not identify the reported time to peak as a steady-state value. The model assumes that elimination determines the terminal phase. The contribution of one dose is $k_a(e^{-kt}-e^{-k_at})/(k_a-k)$, where $t$ is time since dosing and the concentration unit is one dose divided by apparent volume. I removed the contribution of the scheduled dose at hour zero and added the contribution of the delayed dose where applicable. Dosing at and after hour 24 stayed on schedule.

To check the shape of the profile, I divided the model's maximum concentration by its steady-state area under the concentration–time curve (AUC) over 24 hours. The ratio was 0.076 h⁻¹. Dividing the label's geometric-mean peak of 365 ng/mL by its geometric-mean AUC of 3,760 ng·h/mL gives 0.097 h⁻¹ ([1](#ref-1)). The label does not specify the integration interval in that passage, and the two summaries do not give the variability of individual ratios. If the two integration intervals coincide, the model ratio is about 21% lower than the ratio of the published summaries. Scaling concentrations by a common factor cannot close the gap. The table reports ratios within the model.

**Table 1.** Comparison at the 9.2-hour half-life. Extrema were calculated on a 0.01-hour grid.

| Scenario at hour 0 | Minimum through hour 24 / usual trough | Maximum during hours 24–48 / usual peak |
| --- | ---: | ---: |
| On time | 1.000 | 1.000 |
| Taken 4 h late | 0.740 | 1.051 |
| Taken 8 h late (counterfactual) | 0.547 | 1.121 |
| Omitted | 0.164 | 0.855 |

## PK summaries cannot establish the four-hour cutoff

In Table 1, a four-hour delay gives a minimum in the first 24 hours of 74% of the usual trough and a next-day maximum of 105% of the usual peak. Varying the half-life to 6.5 and 11.9 hours (one reported standard deviation of 2.7 hours below and above the mean) and recalibrating the absorption rate to retain a 2.2-hour time to peak yields a four-hour-delay minimum ratio of 0.653 to 0.792. Across the three scenarios the next-day peak ratio is 1.042 to 1.051. These are half-life sensitivity results. They do not estimate a population interval.

Taking the dose eight hours late is a counterfactual outside the label instructions, included to show how much the next-day peak would rise in the model. Omitting one dose avoids that rise and yields a lower first-window minimum. The calculation does not estimate how either change affects efficacy or toxicity. The reported PK summaries are insufficient to derive the four-hour cutoff in the label.

## Data and code availability

The inputs are public prescribing-information summaries. [The reproducibility ZIP](shared/oral-pk-delayed-dose-tradeoff/companion.zip) contains the Python code and output.

## References

1. <a id="ref-1"></a> US Food and Drug Administration. Rasonque (daraxonrasib) prescribing information. 2026. Sections 2.2 and 12.3. [Drugs@FDA](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/220910Orig1s000lbl.pdf).
2. <a id="ref-2"></a> Clark ED, Lawley SD. Should patients skip late doses of medication? A pharmacokinetic perspective. J Pharmacokinet Pharmacodyn. 2022;49(4):429–444. [doi:10.1007/s10928-022-09812-0](https://doi.org/10.1007/s10928-022-09812-0).
