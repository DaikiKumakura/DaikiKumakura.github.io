## Abstract {#article-abstract}

Public SCOT trial results were reconstructed to compare efficacy preservation and toxicity reduction after three versus six months of adjuvant treatment. The reported adjusted DFS HR met the trial’s noninferiority margin, while the three-year DFS difference was −0.4 percentage points (95% interval −2.6 to +1.8). Grade ≥2 neuropathy decreased by 33.4 points in participants with recorded safety grades; missing-grade bounds within the safety cohort retained the direction. Different analysis populations and unknown within-patient joint outcomes prevent estimating individual benefit–risk or a joint disease-free-without-neuropathy endpoint. Noninferiority does not establish identical efficacy.

## Introduction {#question-and-scope}

A shorter treatment schedule can reduce toxicity while leaving uncertainty about efficacy. These are separate dimensions of evidence. Combining them into one attractive number can hide different analysis populations, missing outcomes, and unmeasured patient preferences.

This article uses public SCOT trial results to reconstruct a duration comparison, quantify its uncertainty, and identify what the available data cannot estimate. It is an aggregate-data evidence analysis, not a patient-level reanalysis or a clinical treatment recommendation.

The question of interest is how a randomized treatment-duration comparison informs the balance between efficacy preservation and toxicity reduction. The context of use is study design and evidence appraisal. A wrong inference could overstate what a shorter regimen preserves, or promote a utility-weighted ranking whose assumptions are hidden.

SCOT was selected because its original efficacy and safety tables are openly retrievable. Individual participant data were not obtained; there is no claim of individual outcome modeling, NLME estimation, or exposure–response analysis here.

## Methods {#source-data-and-denominators}

SCOT randomized treatment duration, three versus six months, for high-risk stage II or stage III colorectal cancer. CAPOX or FOLFOX was selected before randomization. The 2018 report used an adjusted DFS hazard-ratio noninferiority margin of 1.13. Its published tables and text are the source inputs below ([1](#ref-1)).

**Table 1. Published inputs and denominators**

| Published input | Three months | Six months |
| --- | ---: | ---: |
| Randomized participants | 3,044 | 3,044 |
| DFS intention-to-treat population | 3,035 | 3,030 |
| Three-year DFS | 76.7% | 77.1% |
| Safety cohort | 434 | 434 |
| Sensory-neuropathy grade available | 420 | 409 |
| Grade ≥2 sensory neuropathy | 103 | 237 |
| Grade ≥3 sensory neuropathy | 18 | 67 |
| Missing neuropathy grade | 14 | 25 |

The acquisition script downloads the official open-access XML and records its SHA-256. Grade ≥3 counts and missingness are extracted directly from [Table 2 of the original report](https://pmc.ncbi.nlm.nih.gov/articles/PMC5883334/); grade ≥2 counts are reconciled against the original report. No survival events are invented from rounded survival percentages.

### Efficacy and toxicity quantities {#estimate-an-evidence-vector-before-a-utility}

The primary comparison retains three quantities:

1. Three-year DFS difference, three minus six months, using the published survival estimate and its published interval.
2. Adjusted DFS HR, three versus six months, compared with the trial margin.
3. Neuropathy risk reduction, six minus three months, recomputed from observed safety counts.

These quantities answer different questions. A hazard ratio does not become an absolute risk difference by subtraction. A Kaplan–Meier survival estimate is not a binomial proportion with the randomized count as its denominator. Toxicity proportions from a subset cannot be silently given the efficacy population's denominator.

For neuropathy, each arm's binomial Wilson interval was computed and combined using a component-based interval for the risk difference. For a positive difference d = p6 − p3, its lower limit is d minus the square root of (p6 − L6)² + (U3 − p3)²; the upper limit uses (U6 − p6)² + (p3 − L3)². These intervals describe sampling uncertainty among observed safety participants. They do not account for selecting the safety subset ([2](#ref-2)).

## Results {#reconstructed-results}

![Separate efficacy and toxicity evidence](shared/treatment-duration-benefit-risk/figures/benefit-risk-evidence.png)

**Figure 1.** Separate efficacy and toxicity estimates and intervals; the endpoints use different populations and time scales.

**Table 2. Separate efficacy and toxicity estimates**

| Quantity | Estimate | 95% interval | Interpretation |
| --- | ---: | ---: | --- |
| Three-year DFS difference, 3 − 6 months | −0.4 percentage points | −2.6 to +1.8 | Published survival estimate; both small loss and gain remain compatible |
| Grade ≥2 neuropathy reduction, 6 − 3 months | 33.4 percentage points | 26.9 to 39.5 | Recomputed in participants with available grades |
| Grade ≥3 neuropathy reduction, 6 − 3 months | 12.1 percentage points | 8.0 to 16.3 | Recomputed from the maximum-grade table |

Figure 1 and Table 2 show that the derived toxicity differences are large compared with the observed efficacy difference, but the comparison is not a patient-level trade-off. The efficacy and safety endpoints are measured on different populations and time scales.

![Trial margin and hazard-ratio uncertainty](shared/treatment-duration-benefit-risk/figures/noninferiority-margin.png)

**Figure 2.** The published adjusted DFS hazard ratio and confidence interval compared with the prespecified upper margin 1.13.

Figure 2 compares the trial margin with the reported DFS HR, which was 1.006 with an interval of 0.909–1.114, below the prespecified upper margin of 1.13. This is a margin-based inference. It does not establish identical efficacy or prove an arbitrarily stricter margin. Conversely, the absolute DFS interval is not the trial's primary adjusted HR test; the two must not be substituted for each other.

### Missing-grade bounds within the safety cohort {#a-missingness-analysis-that-does-not-pretend-to-recover-everyone}

Within the 434-per-arm safety cohort, assign every missing grade first in the direction least favorable to shorter treatment: all 14 missing three-month grades are ≥2 events and none of the 25 missing six-month grades are events. Reverse the assignments for the opposite bound.

Figure 3 shows the resulting grade ≥2 risk-reduction bounds are **27.6 to 36.6 percentage points**. These are identification bounds under arbitrary missing grades, not a confidence interval. They are computed independently of the complete-case sampling interval.

![Bounds for missing grades within the audited safety cohort](shared/treatment-duration-benefit-risk/figures/missingness-bounds.png)

**Figure 3.** Identification bounds for missing grades in the 434-per-arm safety cohort, not sampling confidence intervals or all-participant bounds.

The direction of the safety difference survives these assignments within this cohort. It does not follow that the same bound applies to all randomized participants. The majority of trial participants are outside the detailed safety cohort; giving their unmeasured grades an invented value would create a different sensitivity problem. Representativeness, adverse-event ascertainment, and the observation process remain relevant.

### Later follow-up {#check-the-later-follow-up}

The 2026 final report gives five-year OS of 82.4% in both arms, with overall OS HR 0.96 (main-text interval 0.86–1.07). Reported regimen-specific HRs differ: CAPOX 0.90 (0.78–1.03), FOLFOX 1.10 (0.93–1.34). The abstract prints a different lower overall limit, 0.8; this analysis records the discrepancy and uses the main text ([3](#ref-3)).

This later report adds context; its survival follow-up is not merged with the earlier toxicity counts to manufacture a new joint endpoint. Regimen choice was not randomized, so the subgroup contrast is not a randomized head-to-head CAPOX versus FOLFOX comparison. Failure to meet a subgroup noninferiority criterion also does not alone prove inferiority.

## Discussion {#why-disease-free-without-neuropathy-is-not-identified}

A potentially attractive endpoint is the probability of being disease-free at three years without important neuropathy. Marginal survival and marginal toxicity do not identify that probability: it depends on which people experienced both outcomes. Even if both margins came from the same population, their joint probability would require additional information or explicit bounds. Here, the denominator mismatch comes first.

Similarly, the covariance of the two treatment-effect estimates is unknown. A simulated probability of positive net benefit would depend on a fabricated joint distribution unless its assumptions were stated. This analysis therefore does not generate that probability or label one schedule “optimal.”

As a purely hypothetical preference calculation, suppose both marginal differences could be transported to one population and define benefit as DFS probability plus w times avoided grade ≥2 neuropathy. At the point estimates, −0.004 + w×0.3342 changes sign at **w=0.0120**. Replacing the point efficacy loss with the largest loss in the reported DFS interval moves that arithmetic threshold to **0.0778**. These numbers are not preference estimates, confidence limits for a utility, or recommendations. Their purpose is to make the required valuation and transport assumptions visible.

### Limits of aggregate benefit–risk {#implications-for-model-informed-development}

The published efficacy and toxicity margins do not identify their joint distribution within patients. They also do not specify how patients value an efficacy decrement against cumulative toxicity. A single benefit–risk number would therefore require assumptions beyond the observed margins.

The data support an aggregate duration comparison and within-cohort toxicity sensitivity analysis. They do not identify individual benefit–risk, a continuous duration–response curve, an untested duration, or a PK-guided dosing rule.

## Conclusion {#article-conclusion}

Shorter treatment reduced neuropathy in the observed safety cohort, and the primary efficacy analysis met its specified noninferiority margin. Their combination does not establish equal efficacy or individual net benefit. Population alignment, joint outcomes and patient preferences remain necessary for a joint benefit–risk interpretation.

## Data and code availability {#reproduce}

The companion contains acquisition and extraction code, aggregate inputs and results, figures, and an executed notebook. Downloaded source articles remain outside the archive. See [README](shared/treatment-duration-benefit-risk/README.md). Numerical results can be traced to `results/extracted-inputs.json` and `results/analysis.json`.


[Download code, aggregate results and executed notebook](shared/treatment-duration-benefit-risk/treatment-duration-benefit-risk-companion.zip)

## References {#references}

1. <span id="ref-1"></span>Iveson TJ, Kerr RS, Saunders MP, Cassidy J, Hollander NH, Tabernero J, et al. 3 versus 6 months of adjuvant oxaliplatin-fluoropyrimidine combination therapy for colorectal cancer (SCOT): an international, randomised, phase 3, non-inferiority trial. Lancet Oncol. 2018;19(4):562–578. [doi:10.1016/S1470-2045(18)30093-7](https://doi.org/10.1016/S1470-2045%2818%2930093-7). [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC5883334/). CC BY 4.0.
2. <span id="ref-2"></span>Newcombe RG. Interval estimation for the difference between independent proportions: comparison of eleven methods. Stat Med. 1998;17(8):873–890. [doi:10.1002/(SICI)1097-0258(19980430)17:8<873::AID-SIM779>3.0.CO;2-I](https://doi.org/10.1002/%28SICI%291097-0258%2819980430%2917%3A8%3C873%3A%3AAID-SIM779%3E3.0.CO%3B2-I).
3. <span id="ref-3"></span>Iveson T, Saunders MP, Kelly C, Kerr RS, Cassidy J, Hollander NH, et al. Three versus 6 months of adjuvant oxaliplatin-fluoropyrimidine chemotherapy for colorectal cancer: final results of SCOT—an international, randomized, phase III, noninferiority trial. J Clin Oncol. 2026;44(7):534–539. [doi:10.1200/JCO-25-00621](https://doi.org/10.1200/JCO-25-00621). [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12931879/). The differing overall-HR lower limits in the abstract and main text are retained in the source audit.
