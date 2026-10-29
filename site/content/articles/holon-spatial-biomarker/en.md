Give a pathology image to an AI model and receive a map of gene expression. Being able to examine a cancer's molecular state without another assay would be useful.

But a plausible-looking map is a long way from evidence that can guide a treatment choice. Reading the Holon-S1 technical report, I was less interested in the ranking of models than in its treatment of EREG in breast cancer. The report connects treatment response with the spatial arrangement of predicted expression, rather than expression level alone.

Molecular information recoverable from images could narrow regions for additional measurement or hypotheses for validation. The report does not establish replacement of RNA analysis generally.

## What was measured and what was inferred {#_1}

Holon-S1 is a research model that estimates spatial gene expression from routine hematoxylin and eosin (H&E) pathology images. The developer's technical report evaluates multiple tissues and spatial-transcriptomics assays, selecting genes with supported predictions for each tissue. It does not claim equal accuracy for every gene ([1](#ref-1)).

A region in a spatial map is not necessarily one cell. The example cases use 56×56 µm regions ([1](#ref-1)); these are not measurements of individual cells' expression.

“RNA-seq” also covers different measurements. Bulk RNA-seq, single-cell RNA-seq and spatial transcriptomics provide different information. The question here is whether an image-derived spatial expression map can serve as a biomarker. The report does not establish replacement of RNA analysis generally, including mutation and splicing analysis.

There is more than one reason an image may correspond to expression. A change in cell composition can change both appearance and expression. Tissue architecture may also be associated with particular cell states. Accurate predictions do not necessarily mean that gene-specific regulatory mechanisms were read from the image.

## EREG expression and its spatial arrangement {#ereg}

The [breast-cancer analysis](https://sophont.med/blog/holon/#spatial-organization-for-biomarker-discovery) concerns triple-negative breast cancer (TNBC) and pathological complete response (pCR) after neoadjuvant chemotherapy. IMPRESS is the discovery cohort and TransNEO the independent evaluation cohort. From spatial statistics of predicted expression, the authors selected gEREG, which represents local variation in EREG, and reported an association with treatment response ([1](#ref-1)).

The shift from “Is EREG high?” to “How do predicted EREG values change across locations?” interested me. The same collection of expression values can yield different statistics when grouped together or interspersed.

I checked this with a small synthetic grid. Each position in a 16×16 grid holds either 0 or 1, with equal numbers of each. One arrangement puts all the ones in the left half; another is a checkerboard. The values, mean and variance are identical. Only their arrangement changes.

To illustrate local variation, I averaged the absolute difference between horizontally or vertically adjacent positions:

$$
G=\frac{1}{|E|}\sum_{(i,j)\in E}|x_i-x_j|.
$$

Here E is the set of adjacent grid edges. This is not a reimplementation of Holon-S1's gEREG. It is an educational statistic whose dependence on spatial arrangement can be calculated with all conditions specified.

![Synthetic grids with the same mean expression but different adjacent differences](shared/holon-spatial-biomarker/figures/spatial-layout.svg)

**Figure 1.** All data are synthetic. The split and checkerboard both have mean 0.5 and variance 0.25, but their mean adjacent differences G are 0.0333 and 1, respectively. No patient data or Holon-S1 predictions were used.

I also randomly permuted the same values 1,000 times with a fixed seed. Mean G was 0.5019, close to the expectation 128/255 (approximately 0.5020) obtained from the probability that an edge joins unequal values. The [results and reproduction code](shared/holon-spatial-biomarker/companion.zip) are available. Random placement is not proposed as a correct tissue model; it provides a comparison that destroys arrangement while preserving the total.

## A high spatial statistic has alternative explanations {#_2}

The example also shows why the checkerboard's high G does not establish strong intercellular interaction. High and low values were simply placed alternately.

In real specimens, tumor–stroma mixing, cell density, section quality and fine-scale prediction errors may all enter the statistic. Conversely, smoothing predictions can erase both real boundaries and errors. A spatial statistic therefore includes the tissue mask, adjacency definition, resolution and smoothing conditions as parts of its measurement procedure.

Whether image-derived arrangement adds predictive information can be tested against models using mean expression, tumor–stroma proportion and cell composition. Interpreting that gain specifically as EREG spatial expression additionally requires agreement with measured RNA in corresponding regions. An image-derived surrogate can be predictive without being an accurate molecular measurement. These distinguish the meaning of a spatial statistic; they are not additional validation results established here.

## External prediction and association estimates are different evaluations {#_3}

The report distinguishes applying a model trained in the discovery cohort to TransNEO from refitting regressions within each cohort to estimate odds ratios ([1](#ref-1)). Treating the latter as external validation of a fixed predictor changes the meaning of the evaluation. Reported odds ratios are per discovery-cohort standard deviation, not intervention effects of increasing EREG by a fixed amount or equal-fold increases in response probability. Its stromal tumor-infiltrating lymphocyte comparator (sTIL) is also automatically estimated from images, rather than being a pathologist's sTIL assessment ([1](#ref-1)). The analysis procedures are described in the [technical report](https://sophont.med/blog/holon/).

Selecting features after testing many genes and spatial statistics can introduce optimism into discovery-cohort performance. Evaluation of the complete selection process differs from independent evaluation of a fixed candidate. The report describes five-fold evaluation in IMPRESS and application of IMPRESS-trained models to TransNEO, but this description does not establish whether gene–metric selection was repeated within every training fold. Discovery cross-validation should not be assumed independent of the entire feature-selection process. Having an external evaluation is valuable, but its precision still depends on patient and response counts.

Average precision (AP), which summarizes a precision–recall curve, also depends on the pCR prevalence in the evaluation population. Values from populations with different positive fractions are not directly comparable. A patient-level validation and patient-level uncertainty are appropriate; many tiles from one patient are not many independent patients.

Patient-level predictions and outcomes were not jointly available from the public materials, so I did not independently recompute AP or odds ratios. Nor did I digitize plotted numbers to present an apparently precise replication. Access to model weights was not confirmed. The synthetic grid calculation above does not validate the model's predictive performance.

## An association with pCR does not determine treatment selection {#_4}

An association with pCR among treated patients does not establish that patients with a given marker benefit more from this drug than from an alternative treatment. Association with response and explanation of between-treatment differences are separate questions. Demonstrating treatment-benefit prediction involves treated and comparison groups and evaluation of a treatment-by-marker interaction ([2](#ref-2)). Predicting pCR here does not establish which patients benefit from switching treatments.

Image-predicted EREG arrangement is also not the same observation as measured RNA or protein in that region. Combining the report's associations with the grid calculation does not estimate the benefit of changing an individual's treatment. What the calculation established is that arrangement alone changes a spatial statistic while the distribution of values remains fixed. For the opening question, the report presents image-derived spatial expression maps as biomarker candidates but does not show replacement of RNA-seq.

## Discussion and scope

Three questions matter for gEREG: whether it helps predict pCR from pathology, whether it accurately measures EREG's actual arrangement, and whether altering that arrangement with treatment improves outcomes. Independent-cohort prediction addresses the first. Corresponding molecular measurements address the second, and comparative intervention evidence addresses the third. Satisfying the first does not automatically satisfy the others.

The report compares gEREG with image-estimated sTIL, not all alternatives including pathologist assessments, mean EREG and tissue composition. Association after sTIL adjustment does not isolate a mechanism independent of every known microenvironment factor. The synthetic grid does not validate the predictor, but makes one relevant distinction explicit: arrangements can differ even when total expression does not.

## Data and code availability {#_5}

The [reproduction ZIP](shared/holon-spatial-biomarker/companion.zip) uses only the Python standard library: a 16×16 grid, 128 instances of each value, nonperiodic boundaries, horizontal/vertical adjacency, and seed 20261026. It generates figures, CSV and summary JSON without estimating biological parameters or patient effect sizes.

The technical report was checked on 26 October 2026. It is a developer report on a research model; this article is not independent clinical validation. The announcement date, 20 October ([3](#ref-3)), is not assumed to be the technical report's first publication date.

## References {#article-references}

1. <span id="ref-1"></span>Muhammad H, Warner B, Scotti PS, Abraham TM. Holon-S1 Technical Report [Technical report]. Sophont Technical Report; 2026. Month and day of publication not stated. [doi:10.5281/zenodo.23569193](https://doi.org/10.5281/zenodo.23569193). Available from: [https://sophont.med/blog/holon/](https://sophont.med/blog/holon/) [cited 2026 Oct 26].
2. <span id="ref-2"></span>Ballman KV. Biomarker: Predictive or Prognostic? J Clin Oncol. 2015;33(33):3968–3971. [doi:10.1200/JCO.2015.63.3651](https://doi.org/10.1200/JCO.2015.63.3651). Abstract consulted.
3. <span id="ref-3"></span>Sophont. Sophont launches Holon-S1 to reveal tumor biology from routine pathology slides [Press release]. PR Newswire; 2026 Oct 20 [cited 2026 Oct 26]. Available from: [https://www.prnewswire.com/news-releases/sophont-launches-holon-s1-to-reveal-tumor-biology-from-routine-pathology-slides-302914452.html](https://www.prnewswire.com/news-releases/sophont-launches-holon-s1-to-reveal-tumor-biology-from-routine-pathology-slides-302914452.html).
