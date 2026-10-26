When drugs against the same target are developed one after another, it is tempting to use the dose-comparison results of the earlier drug to select the dose of the later one. In a Bayesian trial, the earlier drug's data can be "borrowed" as a prior distribution. If the new drug behaves like the earlier one, the correct dose can be chosen with fewer patients. If it does not, the earlier conclusion pulls the choice toward the wrong dose.

This article takes two published dose comparisons as the "existing drug": the KRAS G12C inhibitor sotorasib (240 and 960 mg) and the B7-H3 antibody–drug conjugate ifinatamab deruxtecan (8 and 12 mg/kg). They were borrowed as robust mixture priors in a simulated two-dose comparison of a hypothetical new drug, and the relation between the strength of borrowing and the accuracy of dose selection was examined.

The results first.
- **What is gained:** If the new drug behaved like the existing drug, borrowing raised the proportion of correct dose selections by 6 to 10 percentage points. The improvement in expected regret was only about 1 point.
- **What is lost:** If the new drug favored the opposite dose from the existing drug, full borrowing lowered correct selection to the 30 to 40% range.
- **Conflict detection:** The mechanism by which a robust mixture prior detects conflict and reduces borrowing had almost no effect with 40 patients per arm.
- **Rule of thumb:** Limiting the borrowing weight to 0.25 to 0.5 kept the loss within 1 point.

## Borrowing evidence for a hypothetical new drug {#question-and-context-of-use}

**Question of Interest (QOI):** In a dose-selection trial of a new drug, when the dose comparison of an existing drug of the same class is borrowed as a prior, how much more accurate does dose selection become, and how much more often is it wrong when the new drug differs?

**Context of Use (COU):** Material for discussing how much information from an existing drug may be borrowed, and what data specific to the new drug are needed, when planning a dose-optimization trial of a new drug. The effect of the existing drug is not used as a prediction for the new drug. No dose is recommended for any specific new drug.

## Setup {#setup}

**Data of the existing drug (published arm-level summaries):**

| Existing drug | Low dose: responses / severe adverse events | High dose: responses / severe adverse events | Dose favored by the observations |
| --- | --- | --- | --- |
| sotorasib 240 / 960 mg | 26/105, 20/104 | 34/104, 37/104 | Low dose |
| ifinatamab deruxtecan 8 / 12 mg/kg | 12/46, 20/46 | 23/42, 21/42 | High dose |

Severe adverse events are Grade ≥3 treatment-related adverse events for sotorasib and Grade ≥3 adverse events for ifinatamab deruxtecan. The better dose is the one with the larger utility U = response rate − rate of severe adverse events (one response and one severe adverse event are weighted equally, as in the main analysis of the [sotorasib dose-comparison article](sotorasib-dose-comparison-en.html)).

**Trial of the new drug:** 40 patients per arm are randomized to a low and a high dose.
- The response rate and the adverse-event rate in each arm were given the following mixture prior:
  ω × Beta(posterior of the existing drug) + (1 − ω) × Beta(1, 1)
- ω is the borrowing weight, from 0 (no borrowing) to 1 (full borrowing).
- When the data disagree with the existing drug, the mixture prior automatically lowers the weight of the existing-drug component (a robust prior).
- The dose with the larger posterior mean utility is selected. Each condition was simulated with 5,000 trials.

**True values of the new drug (scenarios):**
- **S0:** Equivalent to the existing drug (drawn from the existing drug's posterior).
- **S1:** The high dose gives no additional responses.
- **S2:** The high dose gives 15 points more responses.
- **S3:** The high dose gives no additional adverse events.
- **S4:** The high dose gives 15 points more adverse events.

**Why 15 points:** It is of the same order as the low-to-high differences observed for the existing drugs.
- Sotorasib differences: response +7.9 points, severe adverse events +16.3 points.
- Ifinatamab deruxtecan differences: response +28.7 points, severe adverse events +6.5 points.

The assumption is that even drugs of the same class can easily differ in the size of the dose effect by this much. S1 and S3 are extreme cases where the difference disappears.

## Results: small gains, large losses {#results-small-gains-large-losses}

![Change in expected regret against the borrowing weight](shared/borrowing-prior-dose-selection/figures/01-regret-change.png)

The figure shows the change in expected regret (the difference in utility between the truly best dose and the selected dose) from the no-borrowing case.

- **New drug equivalent (S0):** Full borrowing improved it by about 1 point.
- **New drug favoring the opposite dose from the existing drug:** Full borrowing worsened it by 3.5 to 4.3 points. This applies to S2 and S3 for sotorasib and to S1 for ifinatamab deruxtecan.
- **Scenarios in the same direction as the existing drug:** Borrowing improved the result.

![Correct-selection rate against the borrowing weight](shared/borrowing-prior-dose-selection/figures/02-correct-selection.png)

| | No borrowing | Full borrowing |
| --- | ---: | ---: |
| Borrowing sotorasib, new drug equivalent | 73% | 83% |
| Borrowing sotorasib, no added harm at the high dose of the new drug (S3) | 71% | 28% |
| Borrowing ifinatamab deruxtecan, new drug equivalent | 87% | 93% |
| Borrowing ifinatamab deruxtecan, no added response at the high dose of the new drug (S1) | 72% | 42% |

**Conflict detection did not work:** With a robust mixture prior, the weight of the existing-drug component should fall when the data of the new drug differ from the existing drug. At ω = 0.5, however, the posterior weight of the existing-drug component was:
- Equivalent scenarios: 0.70 to 0.74.
- Opposite-direction scenarios: 0.58 to 0.67.

With 40 patients per arm, a difference of about 15 points cannot be distinguished. It cannot be said that using a mixture prior protects the analysis automatically when the drugs differ.

## How much can be borrowed {#how-much-can-be-borrowed}

Using a rule fixed in advance (improvement when equivalent, and no more than 1 point of deterioration in any scenario), the acceptable ω was determined.

| Condition | Borrowing sotorasib | Borrowing ifinatamab deruxtecan |
| --- | --- | --- |
| Main analysis (40 per arm) | up to 0.5 | up to 0.5 |
| 25 per arm | up to 0.5 | up to 0.5 |
| 60 per arm | up to 0.5 | up to 0.75 |
| Effective sample size of the existing drug reduced to 50 | up to 0.75 | up to 0.5 |
| Weight on harm doubled | up to 0.25 | up to 0.5 |

Full borrowing (ω = 1) was not acceptable under any condition. Only ω = 0.25 was acceptable under all conditions.

## What can and cannot be concluded {#what-can-and-cannot-be-concluded}

**What can be concluded:** Under the utility and deterioration tolerance defined here, a borrowing weight up to 0.5 was acceptable in the main condition with 40 patients per arm for the new drug, while 0.25 was acceptable across all sensitivity conditions. These hypothetical-scenario results are not general rules for borrowing weights or sample sizes. In addition, separate evidence is needed that the endpoint that decided the dose for the existing drug points the same way for the new drug (exposure–response, target saturation, nonclinical data). That endpoint is harm for sotorasib and response for ifinatamab deruxtecan. Borrowing does not replace that evidence.

**What cannot be concluded:**
- The scenarios of the new drug are hypothetical.
- It is assumed that the doses of the existing and the new drug correspond (the same dose ratio sits at the same position).
- The correlation between response and adverse events within an arm and time-dependent harm are not handled.
- The effect of the existing drug was not used as a prediction for the new drug.


## Checking the implementation {#checking-the-implementation}

- **Independent reimplementation:** The mixture-prior update and the simulation were rewritten in a different language (R) with a different random-number stream. For the two existing drugs × two scenarios (equivalent and the one with the largest deterioration) × three borrowing weights (0, 0.5, 1), the correct-selection rate and expected regret agreed within Monte Carlo error (|z| < 4).
- **Posterior weights:** A unit test confirmed that the posterior weights of the mixture prior match the beta-binomial formula.
- **Reproducibility:** Rerunning with the same seed reproduces the result files byte for byte.

## Sources and data {#sources-and-data}

1. Amgen Inc. Sotorasib. Background Information for the Oncologic Drugs Advisory Committee, 05 October 2023 (FDA public document). <https://www.fda.gov/media/172698/download> (Table 20, Table 29)
2. Rudin CM, et al. OA04.03: interim analysis of IDeate-Lung01. *J Thorac Oncol*. 2024;19:S15–S16. [doi:10.1016/j.jtho.2024.09.033](https://doi.org/10.1016/j.jtho.2024.09.033). The arm-level summaries at the same data cutoff were taken from the [published interim results announcement](https://www.merck.com/news/ifinatamab-deruxtecan-continues-to-demonstrate-promising-objective-response-rates-in-patients-with-extensive-stage-small-cell-lung-cancer-in-ideate-lung01-phase-2-trial/).
3. Schmidli H, et al. Robust meta-analytic-predictive priors in clinical trials with historical control information. *Biometrics*. 2014;70:1023–1032. [doi:10.1111/biom.12242](https://doi.org/10.1111/biom.12242) (the idea of the robust mixture prior)

To rerun: `python test_analysis.py && python analysis.py && python figures.py && Rscript validate.R` (Python 3.12, numpy, scipy, pandas, matplotlib; R 4.5.3, jsonlite).

The analysis plan, code, input arm-level summaries, results and validation results are included in the [distribution files](shared/borrowing-prior-dose-selection/borrowing-prior-dose-selection-companion.zip).
