A variant looks relevant to a disease, and a sequence model predicts an effect. Which cells should be used to test it?

That is often still unresolved. A gene name is not enough: the cell type and state change the response worth measuring. The same ambiguity carries into virtual perturbation if the input cells are poorly specified.

The [GEMS preprint](https://doi.org/10.64898/2026.10.14.759213), released on October 16, 2026, addresses this preceding question by associating GWAS candidate variants with potentially relevant cells and tissues. It has not yet been peer reviewed.

I find it more interesting as evidence for choosing an experimental system than as a tool that identifies a drug target outright. But the fraction of variants assigned a cell context can make that evidence look stronger than it is.

## Reading sequence predictions through disease association {#_1}

GEMS uses Borzoi to predict ATAC-seq and RNA-seq signals from sequence. It compares reference and alternate sequences and uses z-standardized absolute log2 fold changes as features. A disease-specific Random Forest distinguishes candidate variants with fine-mapping posterior inclusion probability (PIP) above 0.1 from nearby controls with PIP below 0.01. Because the input discards the effect sign, a contribution to this classifier does not reveal whether expression rises or falls. PIP also depends on fine-mapping assumptions; a value above 0.1 does not establish causality.

The traits are asthma, LDL cholesterol, multiple sclerosis (MS) and type 2 diabetes (T2D). After quality control there are 111 ATAC tracks and 160 RNA tracks. ATAC-only, RNA-only and multimodal models are trained separately. The RNA tracks include bulk tissues, a resolution difference hidden by the shorthand “cell-type prediction.”

SHAP is then used to examine feature contributions. The authors compare 100 repeated models with label-permuted null models and retain associations with variant-wise multiple-testing-adjusted FDR below 0.05. These are statistical assignments of the predicted cell/tissue features used to distinguish candidate variants. They are not measurements of the effect of manipulating a gene in those cells.

The paper also reports enrichment in experimentally identified cis-regulatory elements not used for training. Enrichment remains after variants overlapping training ATAC peaks are excluded, supporting more than a lookup of existing peaks. Regional enrichment still differs from establishing the causal cell context of an individual variant.

## The denominator behind “78%” {#78}

The abstract reports that, in single-modality analyses, the median fractions of candidate variants assigned at least one cell/tissue context across four traits are 58.7% for ATAC and 65.9% for RNA. This is an expansion of annotation coverage.

These percentages cannot be multiplied or subtracted to obtain agreement for the same variants. They are medians across traits, and their overlap is unknown. Moreover, Table 2 below concerns a **separately trained multimodal model**.

I transcribed the four rows of [the original Table 2](https://doi.org/10.64898/2026.10.14.759213) and used two denominators:

| Trait | All candidate variants N | Significant associations in both modalities B | Largest pair K | K / B | K / N |
| --- | ---: | ---: | ---: | ---: | ---: |
| Asthma | 547 | 167 | 100 | 59.9% | 18.3% |
| LDL | 985 | 191 | 149 | 78.0% | 15.1% |
| MS | 273 | 80 | 50 | 62.5% | 18.3% |
| T2D | 497 | 10 | 3 | 30.0% | 0.6% |

B counts variants with at least one significant ATAC association and at least one significant RNA association. Following Table 2, RNA mononuclear-cell features are excluded. This does not require the two modalities to identify biologically identical cells. K is the largest shared-variant count among RNA-tissue/ATAC-cell-type pairs. It does not mean that each variant is assigned exclusively to one cell type.

For LDL, the leading pair is liver RNA and hepatocyte ATAC. Its 149 / 191 = 78.0% indicates strong concentration among variants assigned contexts in both modalities. Relative to all 985 candidates, however, it is 149 / 985 = 15.1%.

$$
\frac{K}{N}=\frac{B}{N}\times\frac{K}{B}
$$

For LDL, 19.4% × 78.0% = 15.1%. Concentration within the selected subset and coverage of the entire candidate set are different quantities. The 15.1% is not accuracy: it is the fraction of the reported candidate set covered by the leading pair with significant associations in both modalities.

![Recalculation of GEMS Table 2 with a common denominator; dark color is the leading pair, light blue the remaining variants assigned in both modalities, and gray the variants without assignments in both](shared/gems-cell-context-selection/figures/denominators.png)

This original figure uses public aggregates; it is not a retrained-model comparison. Gray includes both variants assigned in only one modality and variants assigned in neither. It does not mean that the variants have no effect. Other cells outside the dark segment may also be worth investigating. The plot cannot estimate the success rate of a hepatocyte experiment.

## T2D's 2% is not simply a failure rate {#t2d2}

For T2D, 10 / 497 = 2.0% of variants are assigned in both modalities. The leading pair contains only three variants. Pancreas RNA with delta+gamma-cell ATAC is not the sole leader: colon and colon mucosa RNA each pair with the same ATAC cell type for three variants. Their overlap is unknown, so 3 + 3 + 3 is invalid.

It would also be wrong to read 2.0% as an agreement or disagreement rate after seeing the single-modality pancreatic-islet ATAC assignment of 26.0% and pancreas RNA assignment of 51.5%. These use different models and conditions. For the multimodal T2D model, the paper reports only 21 / 497 variants with a significant ATAC association, compared with 63.4% for RNA.

The authors suggest limited pancreatic-islet training data as one explanation. The islet ATAC tracks represent about 15,000 nuclei; rare endocrine types such as delta+gamma represent about 710. This explanation was not itself tested by an intervention that increased cell numbers. Missing assignments cannot be separated into biological irrelevance versus insufficient measurement or model sensitivity.

I would hesitate to make agreement on a biologically identical experimental system a universal requirement across traits. Poorly represented cells would become easier to exclude from research. Conversely, a pancreas assignment from RNA alone does not establish a particular islet cell type.

## A cell assignment is not functional validation {#_2}

GEMS assignments combine the variant's own PIP, the ATAC/RNA distinction and the resolution of tissues and cell types. Reporting only the top cell name hides alternative contexts, unassigned variants and modality disagreements.

This recalculation does not demonstrate that a particular cell-selection rule improves experiments. The fraction assigned in both modalities is not the success rate of functional experiments in selected cells. Assignment does not establish that the variant's action, or the result of a drug intervention, has been verified there.

## Scope and sources {#_3}

The analysis recalculates denominators and set partitions for four rows of Table 2 in preprint v1. It describes a candidate set, so no sampling-based confidence interval is attached. Linkage disequilibrium among variants also makes an independent-trial interval inappropriate.

The [Figshare DOI](https://doi.org/10.6084/m9.figshare.34511559) given in the paper did not resolve when checked on 2026-10-20; the public API also returned 404. Variant-level ranks, candidate counts and PIP-weighted coverage were therefore not reanalyzed. This records the state on that date, not the subsequent availability of the resource.

[Recalculation code, numerical inputs and reproduction instructions](shared/gems-cell-context-selection/gems-cell-context-selection.zip) are provided. Original figures and PDFs are not redistributed.

Source: Xie et al. [GEMS (GWAS Effect Mechanisms via Sequence-to-Function): Unveiling cell type-specific mechanisms for GWAS variants](https://doi.org/10.64898/2026.10.14.759213). bioRxiv v1, released 2026-10-16. See Table 2, the multimodal Results analysis and the variant–cell-type association Methods.
