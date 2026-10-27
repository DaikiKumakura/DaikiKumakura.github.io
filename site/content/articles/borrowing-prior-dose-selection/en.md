## Abstract {#article-abstract}

Public arm-level dose comparisons of sotorasib and ifinatamab deruxtecan were borrowed as robust mixture priors for simulated two-dose trials of a hypothetical new drug. When the new drug resembled the historical drug, correct selection improved by 6–10 percentage points, but expected regret improved by only about 1 point. With the opposite dose favored, full borrowing reduced correct selection to 28–42%. At 40 patients per arm, posterior mixture-weight adjustment did not prevent this error. Under the stated utility and loss tolerance, weights up to 0.5 were acceptable in the main condition and 0.25 across all sensitivity conditions. These are conditional simulation results, not general borrowing rules or recommended doses.

## Introduction {#question-and-context-of-use}

**Question of Interest (QOI):** In a dose-selection trial of a new drug, when the dose comparison of an existing drug of the same class is borrowed as a prior, how much more accurate does dose selection become, and how much more often is it wrong when the new drug differs?

**Context of Use (COU):** Material for discussing how much information from an existing drug may be borrowed, and what data specific to the new drug are needed, when planning a dose-optimization trial of a new drug. The effect of the existing drug is not used as a prediction for the new drug. No dose is recommended for any specific new drug.

Robust mixture priors combine a historical-information component with a weak-information component and allow their posterior weights to respond to disagreement ([1](#ref-1)). Here the informative component comes from one earlier drug’s arm-level posterior, rather than a meta-analysis of several studies.

## Methods {#setup}

### Public data and utility {#data-and-utility}

Sotorasib inputs came from the public sponsor briefing document. Ifinatamab deruxtecan inputs came from the company announcement at the cutoff corresponding to the IDeate-Lung01 interim report ([2](#ref-2), [3](#ref-3), [4](#ref-4)). Table 1 gives the inputs.

**Table 1. Historical arm-level data**

| Existing drug | Low dose: responses / severe adverse events | High dose: responses / severe adverse events | Dose favored by the observations |
| --- | --- | --- | --- |
| sotorasib 240 / 960 mg | 26/105, 20/104 | 34/104, 37/104 | Low dose |
| ifinatamab deruxtecan 8 / 12 mg/kg | 12/46, 20/46 | 23/42, 21/42 | High dose |

Severe adverse events are Grade ≥3 treatment-related adverse events for sotorasib and Grade ≥3 adverse events for ifinatamab deruxtecan. The better dose is the one with the larger utility U = response rate − rate of severe adverse events (one response and one severe adverse event are weighted equally, as in the main analysis of the sotorasib dose-comparison article ([5](#ref-5))).

### Hypothetical trial and prior {#trial-and-prior}

 40 patients per arm are randomized to a low and a high dose.
- The response rate and the adverse-event rate in each arm were given the following mixture prior:
  ω × Beta(a_H, b_H) + (1 − ω) × Beta(1, 1), with a_H=x_H+1 and b_H=n_H−x_H+1 for historical count x_H and total n_H in each arm and endpoint.
- ω is the borrowing weight, from 0 (no borrowing) to 1 (full borrowing).
- When the data disagree with the existing drug, the mixture prior can lower the posterior weight of the existing-drug component (a robust prior).
- The dose with the larger posterior mean utility is selected. Each condition was simulated with 5,000 trials.

### Truth scenarios {#truth-scenarios}
- **S0:** Equivalent to the existing drug (drawn from the existing drug's posterior).
- **S1:** The high dose gives no additional responses.
- **S2:** Add 0.15 to the high-dose response probability drawn from the historical posterior.
- **S3:** The high dose gives no additional adverse events.
- **S4:** Add 0.15 to the similarly drawn high-dose adverse-event probability.

S2 and S4 probabilities are clipped to 0–0.99.

**Why 15 points:** It is of the same order as the low-to-high differences observed for the existing drugs.
- Sotorasib differences: response +7.9 points, severe adverse events +16.3 points.
- Ifinatamab deruxtecan differences: response +28.7 points, severe adverse events +6.5 points.

A difference of this magnitude within a class is a scenario assumption; its frequency was not estimated from actual drugs. S1 and S3 are extreme cases where the difference disappears.

## Results {#results-small-gains-large-losses}

![Change in expected regret against the borrowing weight](shared/borrowing-prior-dose-selection/figures/01-regret-change.png)

**Figure 1.** Change in expected regret relative to no borrowing, with 5,000 simulated trials per scenario.

Figure 1 shows the change in expected regret (the difference in utility between the truly best dose and the selected dose) from the no-borrowing case. Figure 2 and Table 2 show correct-selection rates.

- **New drug equivalent (S0):** Full borrowing improved it by about 1 point.
- **New drug favoring the opposite dose from the existing drug:** Full borrowing worsened it by 3.5 to 4.3 points. This applies to S2 and S3 for sotorasib and to S1 for ifinatamab deruxtecan.
- **Scenarios in the same direction as the existing drug:** Borrowing improved the result.

![Correct-selection rate against the borrowing weight](shared/borrowing-prior-dose-selection/figures/02-correct-selection.png)

**Figure 2.** The fraction selecting the utility-maximizing dose under the simulated truth; these rates are not clinically validated selection performance.

**Table 2. Correct-selection rates**

| | No borrowing | Full borrowing |
| --- | ---: | ---: |
| Borrowing sotorasib, new drug equivalent | 73% | 83% |
| Borrowing sotorasib, no added harm at the high dose of the new drug (S3) | 71% | 28% |
| Borrowing ifinatamab deruxtecan, new drug equivalent | 87% | 93% |
| Borrowing ifinatamab deruxtecan, no added response at the high dose of the new drug (S1) | 72% | 42% |

### Posterior mixture weights and disagreement {#posterior-mixture-weight}

 With a robust mixture prior, the weight of the existing-drug component should fall when the data of the new drug differ from the existing drug. At ω = 0.5, however, the posterior weight of the existing-drug component was:
- Equivalent scenarios: 0.70 to 0.74.
- Opposite-direction scenarios: 0.58 to 0.67.

With 40 patients per arm in the tested conditions, weight adjustment was insufficient for disagreement of about 15 points. It cannot be said that using a mixture prior protects the analysis automatically when the drugs differ.

### Borrowing under a loss-tolerance criterion {#how-much-can-be-borrowed}

Table 3 applies a rule fixed in advance (improvement when equivalent, and no more than 1 point of deterioration in any scenario) to determine acceptable ω.

**Table 3. Maximum acceptable borrowing weight in each sensitivity condition**

| Condition | Borrowing sotorasib | Borrowing ifinatamab deruxtecan |
| --- | --- | --- |
| Main analysis (40 per arm) | up to 0.5 | up to 0.5 |
| 25 per arm | up to 0.5 | up to 0.5 |
| 60 per arm | up to 0.5 | up to 0.75 |
| Effective sample size of the existing drug reduced to 50 | up to 0.75 | up to 0.5 |
| Weight on harm doubled | up to 0.25 | up to 0.5 |

Full borrowing (ω = 1) was not acceptable under any condition. Only ω = 0.25 was acceptable under all conditions.

### Implementation checks {#checking-the-implementation}

- **Independent reimplementation:** The mixture-prior update and the simulation were rewritten in a different language (R) with a different random-number stream. For the two existing drugs × two scenarios (equivalent and the one with the largest deterioration) × three borrowing weights (0, 0.5, 1), the correct-selection rate and expected regret had differences standardized by Monte Carlo standard errors satisfying |z| < 4.
- **Posterior weights:** A unit test confirmed that the posterior weights of the mixture prior match the beta-binomial formula.
- **Reproducibility:** Rerunning with the same seed reproduces the result files byte for byte.


## Discussion {#what-can-and-cannot-be-concluded}

Under the utility and deterioration tolerance defined here, a borrowing weight up to 0.5 was acceptable in the main condition with 40 patients per arm for the new drug, while 0.25 was acceptable across all sensitivity conditions. These hypothetical-scenario results are not general rules for borrowing weights or sample sizes. In addition, separate evidence is needed that the endpoint that decided the dose for the existing drug points the same way for the new drug (exposure–response, target saturation, nonclinical data). That endpoint is harm for sotorasib and response for ifinatamab deruxtecan. Borrowing does not replace that evidence.

### Assumptions and limitations {#assumptions-and-limits}
- The scenarios of the new drug are hypothetical.
- It is assumed that the doses of the existing and the new drug correspond (the same dose ratio sits at the same position).
- The correlation between response and adverse events within an arm and time-dependent harm are not handled.
- The effect of the existing drug was not used as a prediction for the new drug.


## Conclusion {#article-conclusion}

Borrowing improved selection when the new drug resembled the historical drug but increased errors when dose effects pointed the other way. A robust mixture prior did not automatically protect the tested small trials. Acceptable weights depend on the assumed truths, utility and loss tolerance.

## Data and code availability {#availability}

To rerun: `python test_analysis.py && python analysis.py && python figures.py && Rscript validate.R` (Python 3.12, numpy, scipy, pandas, matplotlib; R 4.5.3, jsonlite).

The analysis plan, code, input arm-level summaries, results and validation results are included in the [distribution files](shared/borrowing-prior-dose-selection/borrowing-prior-dose-selection-companion.zip).

## References {#sources-and-data}

1. <span id="ref-1"></span>Schmidli H, Gsteiger S, Roychoudhury S, O'Hagan A, Spiegelhalter D, Neuenschwander B. Robust meta-analytic-predictive priors in clinical trials with historical control information. Biometrics. 2014;70(4):1023–1032. [doi:10.1111/biom.12242](https://doi.org/10.1111/biom.12242).
2. <span id="ref-2"></span>Amgen Inc. Sotorasib: Background Information for the Oncologic Drugs Advisory Committee, 05 October 2023 [Internet; sponsor briefing document]. 2023 Sep 5. [Tables 20 and 29](https://www.fda.gov/media/172698/download).
3. <span id="ref-3"></span>Rudin CM, Ahn MJ, Johnson M, Hann CL, Girard N, Nishio M, et al. OA04.03 Ifinatamab deruxtecan (I-DXd) in extensive-stage small cell lung cancer (ES-SCLC): interim analysis of IDeate-Lung01 [Conference abstract]. J Thorac Oncol. 2024;19(10):S15–S16. [doi:10.1016/j.jtho.2024.09.033](https://doi.org/10.1016/j.jtho.2024.09.033).
4. <span id="ref-4"></span>Merck & Co., Inc. Ifinatamab deruxtecan continues to demonstrate promising objective response rates in patients with extensive-stage small cell lung cancer in IDeate-Lung01 phase 2 trial [Internet; company announcement]. 2024 Sep 7 [cited 2026 Oct 28]. [Interim results](https://www.merck.com/news/ifinatamab-deruxtecan-continues-to-demonstrate-promising-objective-response-rates-in-patients-with-extensive-stage-small-cell-lung-cancer-in-ideate-lung01-phase-2-trial/). The arm-level counts used here correspond to the 2024 Apr 25 data cutoff.
5. <span id="ref-5"></span>Kumakura D. How far does a dose-comparison trial support dose selection? Arm-level data for sotorasib 960 mg and 240 mg [Internet; technical note]. 2026 Oct 14. [Earlier benefit–risk analysis](https://daikikumakura.github.io/writing/sotorasib-dose-comparison-en.html).
