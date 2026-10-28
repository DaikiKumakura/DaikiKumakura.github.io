A disease-associated variant and a sequence model predicting an effect still leave a practical question: which cells should be used to test it? A gene name alone does not identify the cellular state in which its response matters. That choice also precedes a virtual perturbation.

GEMS, released as a preprint on October 16, 2026, links candidate variants from genome-wide association studies (GWAS) to potentially relevant cells and tissues ([1](#ref-1)). I examine its contribution to choosing experimental systems rather than treating it as a device that identifies a therapeutic target at once. The fraction receiving a cell annotation can overstate the strength of that evidence.

## Reinterpreting sequence predictions through disease association

GEMS uses Borzoi predictions of ATAC-seq (chromatin accessibility) and RNA-seq (gene expression) signals. Features are z-standardized absolute log2 fold changes between reference and alternate sequences. A trait-specific random forest distinguishes fine-mapped candidates with posterior inclusion probability, PIP, above 0.1 from nearby controls below 0.01 ([1](#ref-1)). Because signs are discarded before classification, feature contributions do not identify expression increases or decreases. PIP itself depends on fine-mapping assumptions; exceeding 0.1 does not establish causality.

The traits are asthma, LDL cholesterol, multiple sclerosis (MS), and type 2 diabetes (T2D). After quality control there are 111 ATAC and 160 RNA tracks. Separate models use ATAC, RNA, or both ([1](#ref-1)). Some RNA tracks represent bulk tissues, so “cell-type prediction” encompasses different resolutions.

SHAP (Shapley-value-based feature attribution) quantifies feature contributions. One hundred repeated models are compared with label-permuted null models, retaining variant-specific associations with multiple-testing-adjusted false discovery rate (FDR) below 0.05 ([1](#ref-1)). This identifies the cell or tissue prediction features used by a model to distinguish candidates, not experimentally measured effects of cell-specific genetic interventions.

The paper also tests enrichment of ATAC variant–cell-type associations in independent experimental cis-regulatory regions ([1](#ref-1)). Enrichment persists after removing variants overlapping training-source ATAC peaks, supporting information beyond lookup of existing peaks. Regional enrichment nevertheless differs from identifying the causal cellular context of each variant.

## The denominator behind 78%

The abstract reports median candidate-annotation fractions across four traits of 58.7% for ATAC and 65.9% for RNA in single-modality analyses ([1](#ref-1)). Multiplying or subtracting these medians cannot establish agreement on the same variants. Variant overlap is unknown, and [original Table 2](https://doi.org/10.64898/2026.10.14.759213) ([1](#ref-1), Table 2), transcribed below, concerns a separately trained multimodal model.

**Table 1.** Candidate variants and denominators for the most frequent multimodal cell combination.

| Trait | All candidates N | Significant associations in both modalities B | Largest combination K | K / B | K / N |
| --- | ---: | ---: | ---: | ---: | ---: |
| Asthma | 547 | 167 | 100 | 59.9% | 18.3% |
| LDL | 985 | 191 | 149 | 78.0% | 15.1% |
| MS | 273 | 80 | 50 | 62.5% | 18.3% |
| T2D | 497 | 10 | 3 | 30.0% | 0.6% |

B counts variants with at least one significant association in each modality, excluding RNA mononuclear-cell features as specified in the original table. This alone does not mean both modalities indicate the same biological cells. K is the largest shared-variant count among RNA-tissue/ATAC-cell-type combinations. Variants are not necessarily assigned uniquely.

For LDL, the leading combination is liver RNA and hepatocyte ATAC: 149/191=78.0% among dual-associated variants, but 149/985=15.1% among all candidates.

$$
\frac{K}{N}=\frac{B}{N}\times\frac{K}{B}
$$

Here 19.4% × 78.0% = 15.1%. Concentration within the selected subset and coverage of all candidates answer different questions. The latter is neither accuracy nor a success probability: it describes the fraction of the reported candidate set captured by the most frequent combination.

![Denominator-standardized aggregation of original Table 2](shared/gems-cell-context-selection/figures/denominators.png)

**Figure 1.** Independent redrawing of public aggregates, not a retrained GEMS performance comparison. Dark color denotes the leading combination; light blue denotes other dual-associated variants; gray denotes variants lacking significant associations in both modalities. Gray includes single-modality and unannotated candidates, not demonstrated absence of biological effects. Other combinations can remain experimentally useful, and this figure cannot estimate hepatocyte-experiment success.

## The 2% for T2D is not automatically failure

Only 10/497=2.0% of T2D candidates have associations in both modalities. The largest combination contains three variants. Pancreas RNA with delta+gamma-cell ATAC is tied with colon and colonic-mucosa RNA paired with the same ATAC cell type, each involving three variants. Their overlap is unknown, so they cannot be added as 3+3+3.

The single-modality islet-ATAC annotation rate of 26.0% and pancreas-RNA rate of 51.5% cannot turn 2.0% into a disagreement rate: models and selection conditions differ. In the multimodal T2D model, only 21/497 variants have significant ATAC associations, whereas the reported RNA fraction is 63.4% ([1](#ref-1)).

The authors suggest limited islet-cell training data as one contributor: approximately 15,000 nuclei for islet ATAC tracks and approximately 710 for rare endocrine cells such as delta+gamma ([1](#ref-1)). They did not establish that explanation by experimentally increasing cell counts. Biological irrelevance and insufficient measurement/model sensitivity remain inseparable explanations of missing annotations.

Requiring matching ATAC and RNA contexts universally could exclude underrepresented cells. Conversely, a pancreas RNA association does not identify a specific islet cell type.

## Cell assignment does not establish experimental validity

Interpretation depends jointly on candidate PIP, modality, and tissue-versus-cell-type resolution. Reporting only the leading cell name conceals multiple candidates, unassigned variants, and modality differences. This aggregation does not validate a rule for selecting cells or estimate functional-experiment success. An assigned candidate context is not confirmation of a variant's action or a drug intervention in that context. The aggregates therefore cannot decide the next experimental cell for LDL (hepatocytes) or T2D (a specific islet cell type). GEMS associations are one clue for choosing an experimental system, and their validity must be tested in separate experiments.

## Data and code availability

The calculation re-expresses denominators and set partitions for four rows of [original Table 2, version 1](https://doi.org/10.64898/2026.10.14.759213). These describe a candidate collection, so no sampling-based confidence interval is added. Linkage disequilibrium (LD) also prevents treating variants as independent trials.

The paper's [Figshare DOI](https://doi.org/10.6084/m9.figshare.34511559) did not resolve and its public API returned 404 when checked on October 20, 2026. This records availability then, not subsequent status. I therefore did not reanalyze variant-level rankings, candidate multiplicity, or PIP-weighted coverage.

The [code, aggregate inputs, and reproduction instructions](shared/gems-cell-context-selection/gems-cell-context-selection.zip) are provided without original figures or PDF. Reading covers Table 2, the multimodal Results, and variant–cell-type association Methods.

## References

1. <span id="ref-1"></span>Xie X, Qian S, Chang D, Bhangale T, McCarthy MI, Eraslan G, et al. GEMS (GWAS Effect Mechanisms via Sequence-to-Function): Unveiling cell type-specific mechanisms for GWAS variants [Preprint]. bioRxiv; 2026. Version 1, posted 2026 Oct 16. [doi:10.64898/2026.10.14.759213](https://doi.org/10.64898/2026.10.14.759213). Not peer reviewed.

<span id="78"></span>
<span id="_1"></span>
<span id="_2"></span>
<span id="_3"></span>
<span id="t2d2"></span>
