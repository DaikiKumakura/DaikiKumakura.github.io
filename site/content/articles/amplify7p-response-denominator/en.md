[日本語](amplify7p-response-denominator.html)

Does a report of immune responses in 99% of patients mean that 99% responded to the KRAS mutation present in their own tumor? Public AMPLIFY-7P materials distinguish responses to any vaccine peptide from responses to a patient's tumor-matched mutation.

The first count was 89/90; the second was 78 among the 89 responders. With the same denominator of 90, these become 98.9% and 86.7%. This is not a correction of an erroneous reported number. It is a recalculation that keeps different questions separate.

## Aligning the population and response definition

Camupepimut (ELI-002 7P) contains seven mutant-KRAS peptides. The randomized phase 2 report published on October 23, 2026 compared 96 participants assigned to vaccine with 48 assigned to observation. The primary DFS endpoint was not met. Among 90 immune-evaluable vaccine-arm participants, 89 had a recorded response to at least one vaccine peptide ([George et al., 2026](https://doi.org/10.1038/s41591-026-04734-7)).

The question of interest is how the reported response proportions change when their antigen target and denominator are aligned. The context of use is interpretation of public immunology data and audit of biomarker definitions. This is neither a re-evaluation of clinical efficacy nor a patient-selection model.

Figure 5 Source Data provides participant-level maximum fold changes across vaccine antigens in panel 5b and for the tumor-matched mutation in panel 5i. However, the first panel contains numeric positive summaries for 89 participants and the second for 78. A worksheet with 91 rows does not imply that 90 complete numeric response measurements are present.

| Quantity | Count | Interpretation |
| --- | ---: | --- |
| Randomized to vaccine | 96 | Allocation population |
| Immune evaluable | 90 | Main denominator for immune-response reporting |
| Positive maximum summaries in Figure 5b | 89 | Any-vaccine-antigen responders |
| Positive maximum summaries in Figure 5i | 78 | Tumor-matched responders |
| Participants linked across both positive panels | 78 | Selected population with two positive summaries |

Every ID in the 78-participant panel was present in the 89-participant panel, with no duplicate IDs within either. The 12 absent tumor-matched numeric summaries were not assigned fold changes of zero or one. The calculations are implemented in `analysis/run.py`; the grain and row audit is saved in `outputs/data-quality-audit.json`.

## Conditioning on 89 responders or 90 evaluable participants

Let \(A\) denote a recorded response to any vaccine antigen and \(T\) a recorded response to the tumor-matched peptide. In the published counts, tumor-matched responders form a subset of any-antigen responders. With \(E\) denoting immune evaluability:

\[
\widehat P(A\mid E)=89/90,\qquad
\widehat P(T\mid A,E)=78/89,\qquad
\widehat P(T\mid E)=78/90.
\]

These are proportions of reported response categories, not probabilities of a latent biological response.

| Definition | Count | Recalculated rate | Wilson 95% interval |
| --- | ---: | ---: | ---: |
| Any vaccine peptide / evaluable | 89/90 | 98.9% | 94.0–99.8% |
| Tumor-matched peptide / any responder | 78/89 | 87.6% | 79.2–93.0% |
| Tumor-matched peptide / evaluable | 78/90 | 86.7% | 78.1–92.2% |

On the common denominator of 90, the difference is 12.2 percentage points (`outputs/tables/response-denominators.csv`). This is not a comparison between treatment arms. It is the change produced by narrowing the response definition within one vaccine arm. No independent two-sample test was performed.

![Response definitions and denominators](shared/amplify7p-response-denominator/figures/response-denominators.svg)

The Wilson intervals condition on each denominator. They do not include missingness, assay error or selection of observation times. The three estimates are dependent; overlap between their intervals is not a test of their difference.

## Maximum response magnitudes also differ

The 78 participants with numeric positive summaries in both panels were linked by ID. Within this selected set, the median maximum response across vaccine antigens was 52.58-fold; the median tumor-matched maximum was 11.445-fold. The median within-participant ratio of tumor-matched maximum to overall maximum was 0.374, with an interquartile range of 0.133–0.787 (`outputs/tables/paired-positive-summary.csv`).

![Paired positive summaries in 78 participants](shared/amplify7p-response-denominator/figures/paired-positive-folds.svg)

These are descriptive statistics after selection of 78 participants. They do not describe the tumor-matched response distribution in all 90 evaluable participants. A maximum selected across multiple antigens and measurement opportunities is also expected to exceed a maximum restricted to one antigen. The comparison therefore includes the effect of that selection operation.

Measurements used ex vivo Fluorospot or intracellular cytokine staining (ICS). The original response definition combines a baseline-relative increase with an absolute assay threshold. The script does not discover new responders using fold change of at least two alone; it reconciles counts of already reported positive summaries.

The maxima are not synchronized measurements at a common sampling time. Their ratio cannot establish recognition of actual tumor cells, T-cell trafficking into tumors or cytotoxic potency.

## Including the six unascertained participants

The allocation population of 96 differs from the immune-evaluable population of 90 by six participants. Rather than impute their responses, the analysis calculates the arithmetic range obtained if none or all six satisfy a recorded response category:

\[
k/96\le p_{\mathrm{all}}\le(k+6)/96.
\]

The published categories in the 90 evaluated participants remain fixed. This is neither a model of why observations are unavailable nor an estimate of the true response rate among unascertained participants.

| Definition | Arithmetic range among all 96 |
| --- | ---: |
| Any vaccine antigen | 92.7–99.0% |
| Tumor-matched antigen | 81.3–87.5% |

![Ascertainment bounds for six participants](shared/amplify7p-response-denominator/figures/ascertainment-bounds.svg)

These bounds are not confidence intervals. They show why a proportion conditional on evaluability differs from a proportion in the allocation population. They do not contradict the reported 98.9% among evaluable participants (`outputs/tables/ascertainment-bounds.csv`).

## Immune responses and treatment effects

Survival groups defined using maximum post-vaccination immune responses are not randomized baseline groups. Follow-up to response assessment, disease status and sampling opportunities may matter. These counts cannot establish that increasing the immune response would improve DFS.

The 2025 immunogenicity presentation reports 540/630 positive antigen-level responses, whereas the 2026 article reports 543/623 after restricting the denominator to 89 immune responders. Both the reporting occasion and the population differ; these are not pooled as one fixed dataset. Seven antigens measured in each participant are also not treated as 630 independent participants ([2025 presentation](https://elicio.com/wp-content/uploads/2025/09/Immunogenicity-Data-9-4-25.pdf), [2026 article](https://doi.org/10.1038/s41591-026-04734-7)).

In this audit, 99% refers to a response to any vaccine antigen among evaluable participants. Counting tumor-matched responses with the same denominator gives 86.7%. Neither measure is clinical benefit itself. The public summaries establish that the antigen target, evaluation population and selection of maxima change what a number from the same trial describes.

## Analysis materials

[Reproduction code and aggregate tables](shared/amplify7p-response-denominator/amplify7p-response-denominator-analysis.zip). The code acquires the public workbook with hash verification and regenerates the aggregate calculations and new figures. The original workbook, original figures and participant-level derivative tables are not redistributed. Numerical results are saved in `outputs/results.json`.

## References

George B, Singh H, Devoe CE, et al. Lymph node-targeted, mKRAS-specific amphiphile vaccine in pancreatic cancer: the randomized phase 2 AMPLIFY-7P trial. *Nature Medicine*. Published October 23, 2026. [doi:10.1038/s41591-026-04734-7](https://doi.org/10.1038/s41591-026-04734-7). Figure 5 Source Data, CC BY-NC-ND 4.0. This article reports independent calculations and newly drawn figures; original figures and participant records are not redistributed.

Elicio Therapeutics. AMPLIFY-7P Phase 2 immunogenicity data. September 2025. [Public presentation](https://elicio.com/wp-content/uploads/2025/09/Immunogenicity-Data-9-4-25.pdf).

## Cite this article

Kumakura D. What does a 99% immune-response rate count in a KRAS vaccine trial? Independent reanalysis of published AMPLIFY-7P response summaries. 2026.
