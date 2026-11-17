A randomized two-dose study asks which dose to carry forward. A modestly higher response rate leaves two separate questions open. Is the increase worthwhile, and is toxicity acceptable? The FDA oncology dosage guidance recommends evaluating safety and antitumour activity at each dosage ([1](#ref-1)). ROSE is one design that uses a prespecified probability of correct selection to set the size of a randomized comparison ([2](#ref-2)). I used simulated trials to compare immediate selection with the option to defer a decision.

## Adding a third decision

The simulated trials allocated equal numbers to low and high doses. The high dose was correct if its true population response rate exceeded the low-dose rate by at least eight percentage points and its toxicity rate was at most 25%. The true low-dose toxicity rate was at most 25% in every setting. I approximated the population rates from 400,000 simulated individuals per dose. Response and toxicity were binary outcomes in one assessment window. The thresholds were assumptions for this comparison.

I applied three rules to the same trial samples. The arm-rate rule uses observed proportions by assigned dose. The exposure–response rule uses pooled logistic regressions on log exposure, omits severity and predicts both dose levels assuming exposure is proportional to dose. Both rules choose low whenever either threshold fails. The three-way rule selects high if the lower response-difference bound is at least eight points and the upper high-dose toxicity bound is at most 25%. It selects low if the upper low-dose toxicity bound is at most 25% and either the upper response-difference bound is below eight points or the lower high-dose toxicity bound is above 25%. It defers in the remaining trials. I used Wilson bounds for toxicity and a Newcombe-style combination of Wilson bounds for the response difference ([3](#ref-3)). Component bounds were nominally one-sided 90%. That level does not determine the trial-level error rate.

## Larger groups leave the confounding in place

I crossed three scenarios (clear benefit, plateau and excess toxicity) with the presence or absence of severity-driven clearance and 40 or 100 participants per arm, running 2,000 trials per setting. When more severe disease both reduces the chance of response and lowers exposure through faster clearance, the pooled exposure slope absorbs part of the severity effect. The dose ratio was 2:1. In the confounded scenario, an increase of one severity SD multiplied clearance by 1.49 and reduced the response log-odds by 0.6. Randomization assigns doses, while exposures still vary between individuals.

Table 1 shows four of the simulated settings.

**Table 1.** Incorrect selection and deferral in the two-dose comparisons.

| Scenario | Patients per arm | Arm-rate error | Exposure–response error | Three-way error | Three-way deferral |
| --- | ---: | ---: | ---: | ---: | ---: |
| Clear benefit without confounding | 40 | 18.70% | 12.75% | 1.15% | 75.45% |
| Plateau with confounding | 40 | 27.95% | 74.55% | 1.95% | 79.95% |
| Plateau with confounding | 100 | 25.00% | 87.55% | 1.90% | 65.65% |
| Excess toxicity with confounding | 40 | 13.95% | 11.05% | 0.10% | 73.25% |

With a confounded plateau and 40 per arm, correct selection was 46.6 points lower for exposure–response than for the arm-rate rule. The paired 95% Monte Carlo interval was −49.0 to −44.2 points. At 100 per arm the difference widened to −62.55 points. The interval describes finite simulation error around this comparison under the specified scenario.

The three-way rule made fewer incorrect selections, while deferring nearly eight in ten trials at the plateau with 40 per arm. If a wrong selection costs one and deferral costs $c$, its estimated expected loss is $0.0195+0.7995c$, against $0.2795$ for the arm-rate rule. In this scenario the three-way rule is preferable when $c$ is below approximately 0.325. Taking deferral to cost 0.5 reverses that ordering. Different costs for selecting the wrong high or low dose would change the boundary.

The simulation leaves out discontinuation, time-varying exposure and late toxicities. Within its assessment window and specified data-generating process, the comparison depends on the total cost of deferral, including further observation and delay.

## Data and code availability

The [companion ZIP](shared/dose-selection-with-deferral/companion.zip) contains the R code and full results.

## References

1. <a id="ref-1"></a> US Food and Drug Administration. Optimizing the Dosage of Human Prescription Drugs and Biological Products for the Treatment of Oncologic Diseases. Guidance for Industry. 2024. [FDA guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/optimizing-dosage-human-prescription-drugs-and-biological-products-treatment-oncologic-diseases).
2. <a id="ref-2"></a> Wang S, Yuan Y, Liu S. Randomized optimal selection design for dose optimization. Biometrics. 2025;81(4):ujaf124. [doi:10.1093/biomtc/ujaf124](https://doi.org/10.1093/biomtc/ujaf124).
3. <a id="ref-3"></a> Newcombe RG. Interval estimation for the difference between independent proportions: comparison of eleven methods. Stat Med. 1998;17:873–890. [PubMed](https://pubmed.ncbi.nlm.nih.gov/9595617/).
