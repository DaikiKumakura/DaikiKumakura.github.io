## Abstract {#article-abstract}

In 43 publicly available pretreatment/on-treatment RNA pairs, a fixed cytolytic-expression summary usually increased. However, its change added only uncertain information about recorded best response beyond baseline expression. A within-participant pharmacodynamic change therefore needs separate evaluation before it can be used as a predictive biomarker.


## Introduction {#question-and-information-time}

The question of interest was whether a small, fixed immune-expression summary changes within participants and whether that change adds conditional information about recorded best overall response. The context of use is prioritizing pharmacodynamic monitoring hypotheses. This is not a clinical biomarker assay, treatment-selection rule, survival surrogate, or prospective prediction study.

The source study scheduled a pretreatment biopsy 1–7 days before dosing and an on-treatment biopsy during days 23–29. Individual exact biopsy dates are absent from the downloaded GEO metadata. Response denotes best overall RECIST 1.1 response ([1](#ref-1)).

That distinction determines the analysis. On-treatment expression cannot be used to describe what was knowable before treatment. Nor can the study schedule substitute for every participant's actual biopsy and event dates. Without those dates, a survival landmark analysis and immortal-time correction cannot be qualified from these files.

## Methods {#audit-the-pairs-before-scoring-them}

Official GSE91061 SOFT metadata, FPKM and raw-count files were downloaded and hashed. Sample titles contain participant and visit identifiers; visit labels were checked against the metadata characteristics. Expression columns matched metadata samples exactly. Response labels agreed within participants ([2](#ref-2)).

**Table 1. Pairing and data audit**

| Data audit | Count |
| --- | ---: |
| RNA samples / participants | 109 / 65 |
| Pretreatment / on-treatment samples | 51 / 58 |
| Participants with exactly one sample at each visit | 43 |
| Participants excluded as unpaired | 22 |
| Duplicate participant–visit rows | 2, belonging to one unpaired participant |
| Paired PRCR / SD / PD / unknown response | 9 / 15 / 18 / 1 |
| Response-known paired analysis | 42 participants, 9 responders |
| Genes in each expression matrix | 22,187 |

The duplicate on-treatment samples were not chosen between by response or expression. Their participant lacked an eligible pretreatment pair and did not enter the paired analysis. Unknown response remained in the change description and was excluded only from response-associated models. These rules preserve the observed sampling structure rather than manufacture a complete cohort.

### Fixed scores and assay differences {#fixed-scores-with-assay-differences-made-explicit}

The primary cytolytic-inspired score was the mean of log2(FPKM+1) for **GZMA and PRF1**. The gene choice follows the biological summary proposed by Rooney et al., but the published CYT measure used TPM. The present transformation, normalization, and pseudocount make this an adaptation rather than a reproduction of that assay ([3](#ref-3)).

A secondary, descriptive IFN-related score averaged log2(FPKM+1) over IFNG, STAT1, IDO1, CXCL9, CXCL10 and HLA-DRA. The literature motivates the panel; its NanoString-based scoring and clinical cutoffs are not imported into these RNA-seq measurements ([4](#ref-4)).

No genes or threshold were selected using this cohort's response labels. Change was defined as on-treatment minus pretreatment score. As a normalization sensitivity, the primary score was also computed from log2(CPM+1), using each raw-count library total. CPM does not perform gene-length normalization and does not establish equivalence to FPKM or TPM.

### Response-association evaluation {#response-association-methods}

Two ridge logistic models were fixed: baseline primary score alone, and baseline plus its change. PRCR was compared with SD/PD; stable disease was not reclassified as response. There were only nine responders, so no extra clinical interactions, nonlinear terms, or outcome-selected cutoffs were added.

Three patient-stratified folds were repeated 20 times. Centering, scaling and coefficients were estimated in the training fold only. Both visits from a participant stayed together. The slope penalty was fixed at one; it was not selected to maximize the result. Repeated held-out probabilities were averaged per participant.

## Results {#article-results}

### Paired changes {#paired-changes}

![Within-participant expression changes; thick lines connect visit medians](shared/on-treatment-immune-change/figures/paired-expression.png)

**Figure 1.** Within-participant scores. Thick lines connect visit-specific medians; their difference is not the median paired change.

**Table 2. Within-participant score changes**

| Score | Pairs | Median change | Participant-bootstrap 95% interval | Positive changes |
| --- | ---: | ---: | ---: | ---: |
| Cytolytic-inspired, FPKM | 43 | +0.346 | +0.154 to +1.108 | 33 / 43 |
| IFN-related, FPKM | 43 | +0.454 | +0.242 to +0.803 | 34 / 43 |
| Cytolytic-inspired, CPM sensitivity | 43 | +0.419 | +0.184 to +1.138 | 34 / 43 |

Figure 1 and Table 2 summarize the paired changes. Intervals resampled participants 2,000 times and summarized the median paired difference. The thick figure lines connect the median at each visit; their vertical difference is not the median of individual changes. The two summaries should not be conflated.

The FPKM and CPM primary-change ranks were strongly correlated, Spearman rho **0.996**. This supports stability of the rank pattern to this normalization change. It does not validate absolute score units, tissue comparability, or an immune-cell-count interpretation.

Bulk RNA changes can reflect changing cell composition, tumor content, sampling, or expression within cells. With no untreated longitudinal control, an observed change is not a randomized estimate of nivolumab's causal effect on the score. The paired design removes a fixed participant level; it does not remove every time-varying explanation.

### Conditional response information {#does-change-add-information-about-recorded-response}

![Observed change by response group in the selected paired cohort](shared/on-treatment-immune-change/figures/change-by-response.png)

**Figure 2.** Observed changes by recorded best-response group in the selected paired cohort. These are descriptive associations.

![Held-out diagnostics of conditional response association](shared/on-treatment-immune-change/figures/association-validation.png)

**Figure 3.** Held-out diagnostics of conditional response association. Predictions are aggregated from repeated patient-level cross-validation, with both visits kept together.

**Table 3. Held-out response-association measures**

| Held-out measure | Baseline | Baseline + change |
| --- | ---: | ---: |
| AUC | 0.599 | 0.673 |
| Brier score, lower is better | 0.1650 | 0.1635 |
| Log loss, lower is better | 0.5198 | 0.5042 |

Figures 2–3 and Table 3 summarize the conditional response analysis. The AUC difference was **+0.074**, with a stratified conditional bootstrap interval of **−0.084 to +0.269**. The Brier difference was **−0.0015** (−0.0251 to +0.0232); log-loss difference was **−0.0157** (−0.0946 to +0.0610). Each interval included no improvement. They condition on fitted held-out predictions, preserve the observed responder count, and omit uncertainty from refitting.

The extended model's held-out calibration slope was **0.648**, with intercept **−0.417** from an unpenalized calibration regression. With nine responders, these estimates are imprecise diagnostics; they do not qualify individual probabilities. The CPM sensitivity gave AUC 0.677 and Brier 0.1630 for the extended model, preserving the modest point improvement but not establishing clinical utility.

These are **conditional association diagnostics in participants with available pairs**, not pretreatment prediction. Best-response timing and individual biopsy dates cannot be ordered from these files. Patient-level cross-validation limits fitting leakage; it cannot repair selection into a second biopsy or qualify the information time of a clinical endpoint.

### Observable selection effects {#what-observable-selection-revealsand-misses}

**Table 4. Observable selection into paired sampling**

| Pretreatment samples | Participants | Known responses | PRCR | Median baseline primary score |
| --- | ---: | ---: | ---: | ---: |
| Also have an eligible on-treatment pair | 43 | 42 | 9 | 2.692 |
| No eligible on-treatment pair | 8 | 7 | 1 | 2.298 |

The small comparison in Table 4 records observable differences. It neither explains why an on-treatment biopsy is missing nor demonstrates that missingness is random. Other participants had only on-treatment specimens and could not enter this baseline comparison. Prior treatment, exact lesion composition and individual collection timing are not adjusted here.

## Discussion {#what-follows-for-a-monitoring-study}

The data support a within-participant immune-expression shift among observed pairs. They provide weaker evidence that the primary change adds useful response information. Collection timing, biopsy failure, lesion identity and response ascertainment limit interpretation at a fixed information time.

This analysis provides no PK measurements or exposure-linked response, and cannot justify dose adjustment. It also does not establish a novel immune biology discovery; it is a bounded reanalysis of an existing longitudinal cohort. The pairing audit, fixed low-dimensional scores and normalization sensitivity are documented in the companion.

## Conclusion {#article-conclusion}

Immune-expression scores increased within the observed pairs, but the incremental response information from change remained uncertain. The selected paired cohort and unresolved individual timing prevent interpreting these associations as pretreatment prediction or a validated monitoring rule.

## Data and code availability {#reproduce}

The companion includes acquisition and analysis code, aggregate results, figures, and an executed notebook. Participant metadata, expression matrices, scores and prediction rows remain outside the archive. See [README](shared/on-treatment-immune-change/README.md). Source manifests retain official URLs and SHA-256 hashes.


[Download code, aggregate results and executed notebook](shared/on-treatment-immune-change/on-treatment-immune-change-companion.zip)

## References {#references}

1. <span id="ref-1"></span>Riaz N, Havel JJ, Makarov V, Desrichard A, Urba WJ, Sims JS, et al. Tumor and microenvironment evolution during immunotherapy with nivolumab. Cell. 2017;171(4):934–949.e16. [doi:10.1016/j.cell.2017.09.028](https://doi.org/10.1016/j.cell.2017.09.028).
2. <span id="ref-2"></span>National Center for Biotechnology Information. Gene Expression Omnibus: GSE91061 [Dataset]. [Official series record](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE91061). Official sample metadata and processed expression files; acquisition URLs and SHA-256 hashes are retained in the companion.
3. <span id="ref-3"></span>Rooney MS, Shukla SA, Wu CJ, Getz G, Hacohen N. Molecular and genetic properties of tumors associated with local immune cytolytic activity. Cell. 2015;160(1–2):48–61. [doi:10.1016/j.cell.2014.12.033](https://doi.org/10.1016/j.cell.2014.12.033).
4. <span id="ref-4"></span>Ayers M, Lunceford J, Nebozhyn M, Murphy E, Loboda A, Kaufman DR, et al. IFN-γ–related mRNA profile predicts clinical response to PD-1 blockade. J Clin Invest. 2017;127(8):2930–2940. [doi:10.1172/JCI91190](https://doi.org/10.1172/JCI91190). The gene panel motivated the secondary summary; the original assay and cutoff were not reused.
