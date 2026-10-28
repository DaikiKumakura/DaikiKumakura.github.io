5-FU and olaparib have different mechanisms of action. Yet numerical profiles of cultured-cell morphology can make their responses look similar. What does this proximity represent for a model learning drug similarity from images?

A Cell Painting study published on October 21, 2026 provides a concrete example. Two drugs that were close in cells spread on a flat surface separated when cells were grown as small three-dimensional aggregates. The two drugs also differed in DNA damage-response, DNA-synthesis and gene-expression measurements ([1](#ref-1)).

I re-examined published figure values and processed image features, summarized drug similarities, fixed concentrations and restricted comparisons to shared features. The question examined is not whether 3D is intrinsically correct but whether the experimental definition of drug response changes the list of similar drugs.

## Measuring cell morphology {#_1}

Cell Painting labels nuclei, mitochondria, cytoskeleton and other components with fluorescent dyes, then extracts shape, intensity and texture features. A drug response becomes a multivariate fingerprint. This study examined the colorectal cancer cell lines HCT116 and HT29 and 52 drugs.

Overlapping cells and depth-dependent attenuation complicate 3D imaging. The authors cleared small spheroids, detected cells in individual optical sections, standardized each section against controls and aggregated features into well-level profiles. They also compared this approach with images projected into a single plane ([1](#ref-1)).

Here, single-cell includes identifying cells within sections. The same cell can appear in several sections, so detected objects are not necessarily independent cells. Similarly, the 630 drug pairs below do not constitute 630 independent experiments.

## Olaparib moves away from 5-FU {#5-fu}

I first reaggregated Source Data for [Figure 5d of the original paper](https://doi.org/10.1038/s41467-026-78596-5). The 36 HCT116 drugs retained in both 2D and 3D generate 630 pairs. These drugs passed selection using grit, a metric combining response strength and reproducibility; this is not a comparison of all 52 drugs.

The authors used cosine similarity, which increases as two feature vectors point in similar directions. Each drug had several concentrations. The table uses the maximum similarity across pairs of concentrations that passed the response criterion, rather than a fixed-concentration comparison. I checked this definition in the [authors' analysis code](https://github.com/pharmbio/colopaint3D/blob/5f209bcfbccdef2b5c0c97060b9d82aef085f2cb/analysis/3_Figure4/3_PairwiseCorrelations.ipynb) ([2](#ref-2)).

**Table 1.** Drug similarity and rank using the authors' concentration aggregation.

| Relationship between 5-FU and olaparib | 2D | 3D |
| --- | ---: | ---: |
| Similarity using the authors' concentration aggregation | 0.886 | 0.377 |
| Olaparib rank among the other 35 shared drugs | 1 | 20 |

![Drug similarity changes with culture format](shared/cellpainting-2d-3d/figures/drug-neighborhoods.png)

**Figure 1.** Redrawn values from [Figure 5d of the original paper](https://doi.org/10.1038/s41467-026-78596-5). Each point is a drug pair; points below the dashed line have lower similarity in 3D. The red point represents 5-FU and olaparib. Pairs sharing a drug are not independent. Concentrations producing the maximum may differ between formats.

The original paper selected these two drugs as an exploratory example of a large change. They do not represent the average change across all drugs.

Even within the same cell line, a search for drugs similar to 5-FU returns different results. For foundation-model training or candidate retrieval, these neighborhood relations can themselves be learning targets. Culture conditions therefore cannot simply be treated as nuisance variation to remove later.

## Fixing concentrations and image features {#_2}

To reduce flexibility in concentration selection, I fixed 5-FU at 10 µM and olaparib at 3 µM, the concentrations used for the imaging and molecular comparisons. Drug exposure lasted 48 h. The following calculations are additional analyses for this article.

The inputs were public HCT116 well-level features used for [Figures 5b and 4b of the original paper](https://doi.org/10.1038/s41467-026-78596-5). Each drug and format contributed four wells; the median of each feature defined its drug profile. I did not resegment raw images or repeat standardization against controls.

The feature sets differ between 2D and 3D. I selected seven fixed feature-name prefixes covering shape, intensity, texture and related measurements, and harmonized the illumination-correction token `illum`. This yielded 849 features in 2D and 594 in 3D, including 416 shared features. Similarity between the two drugs was calculated within each format. A 2D vector was not compared directly with a 3D vector.

**Table 2.** Feature selection and aggregation at fixed concentrations.

| Fixed-concentration calculation | 2D | 3D |
| --- | ---: | ---: |
| Features selected in each format, median, cosine | 0.708 | 0.375 |
| Shared 416 features, median, cosine | 0.808 | 0.354 |
| Shared 416 features, mean, cosine | 0.821 | 0.237 |
| Shared 416 features, median, Pearson correlation | 0.807 | 0.359 |

At these concentrations, similarity remained lower in 3D across feature sets and aggregation methods. With shared features and one imaging plate omitted at a time, values ranged from 0.707 to 0.809 in 2D and from 0.157 to 0.369 in 3D. This small sensitivity check involved only two plates per format. These ranges are neither confidence intervals nor estimates of variation across independent experiments.

![Fixed-concentration comparison and concentration dependence](shared/cellpainting-2d-3d/figures/fixed-dose-sensitivity.png)

**Figure 2.** Left: fixed-concentration comparison using 416 shared features. Circles use all wells; crosses omit one plate at a time. Right: similarity differences, 3D minus 2D, for shared concentration combinations. The outlined cell marks the fixed concentrations discussed in the text. Not every combination has lower similarity in 3D. The published preprocessing and response filter are retained, requiring particular caution at low concentrations.

These drugs are not always dissimilar in 3D. At some low concentrations, including 0.3 µM 5-FU, the direction reverses. Concentration changes the ratio of response magnitude to measurement noise. Reducing a response to a drug-name label while dropping concentration and time loses that information.

## DNA damage response and DNA synthesis give different orderings {#dnadna}

Do biological measurements support the morphological difference? In 3D culture, the authors measured γH2AX foci, a DNA damage-response-related readout, and incorporation of 5-ethynyl-2'-deoxyuridine (EdU) into newly synthesized DNA, a DNA-synthesis readout. Reaggregating well-level Source Data for [Figure 6b of the original paper](https://doi.org/10.1038/s41467-026-78596-5) gave these medians.

**Table 3.** DNA damage-response and DNA-synthesis measurements in 3D culture.

| Median measurement | DMSO control | 5-FU 10 µM | Olaparib 3 µM |
| --- | ---: | ---: | ---: |
| γH2AX foci per nucleus | 0.87 | 1.89 | 4.84 |
| EdU-positive fraction | 34.8% | 7.7% | 16.3% |

Olaparib produced more γH2AX foci, whereas 5-FU produced a lower EdU-positive fraction. These readouts do not follow a single ordering in which greater damage means stronger suppression of DNA synthesis. The 13 spheroids per condition were technical replicates in separate wells within one experiment, not 13 patients or 13 independent experiments.

In RNA sequencing, CDKN1A, which encodes the cell-cycle-arrest-associated protein p21, had log2 fold changes of +3.49 for 5-FU and +1.35 for olaparib relative to control. These are outputs of the authors' differential-expression analysis, not a reanalysis of raw counts here. A smaller FDR-adjusted p-value in one comparison does not by itself establish a significant difference between drugs. The RNA experiment had two biological and two technical replicates. One control sample was excluded for low read count, and technical replicates were treated as separate samples in the authors' analysis ([1](#ref-1)).

In 3D, the two drugs closest to 5-FU were abbreviated AMG23 and Nutli in the authors' table, with similarities of 0.771 and 0.741 (`results/neighbors.csv`). Reading these as the MDM2 inhibitors AMG 232 and nutlin fits a p53/p21-related interpretation. However, Nutli was already second in 2D (0.825), and HCT116 and HT29 differ in more than TP53. Their contrast alone cannot identify a causal p53 effect. Together, morphology, DNA synthesis, damage-response and RNA measurements can narrow mechanistic hypotheses rather than settle them.

## Discussion and conclusion {#_3}

In this comparison, proximity of image responses in 2D did not guarantee proximity in 3D. The changing relationship between 5-FU and olaparib is one specific example.

Magnification, light attenuation, cell detection and feature selection also differed. Persistence of the difference with shared features does not isolate a culture-format effect. Nor did this analysis test whether 3D more accurately predicts clinical drug efficacy.

An image-based relation of similar drugs cannot therefore be detached from experimental conditions and treated as an intrinsic drug property. Even for the same drugs, the neighborhood depends on environment, measurement time and readout.

## Data and code availability {#_4}

The [analysis code, extracted data, figures and calculated results](shared/cellpainting-2d-3d/cellpainting-2d-3d.zip) are provided. Run `analysis.py` and then `plot.py` in Python to regenerate the article's tables and figures. The authors' repository commit is fixed, and extraction sources and SHA-256 hashes are recorded.

Drug ranks reaggregate the authors' similarity table. Fixed-concentration and shared-feature comparisons are additional calculations from processed well-level features released as figure inputs. The authors' supplementary figures use different processed inputs, so this is not claimed as complete reproduction of all concentration-dependent values. Raw images and raw RNA counts were not reanalyzed; no trained AI model was evaluated and no new drug experiment was performed.

## References

1. <span id="ref-1"></span> Ringers C, Holmberg D, Larsson A, Jung B, Jarvius M, Luchniak A, et al. High-content morphological profiling by Cell Painting in 3D spheroids. Nat Commun. 2026;17:10790. [doi:10.1038/s41467-026-78596-5](https://doi.org/10.1038/s41467-026-78596-5).
2. <span id="ref-2"></span> Pharmbio. [colopaint3D: analysis code and Source Data](https://github.com/pharmbio/colopaint3D/tree/5f209bcfbccdef2b5c0c97060b9d82aef085f2cb) [software and data]. Commit 5f209bcfbccdef2b5c0c97060b9d82aef085f2cb [cited 2026 Oct 23]. Image archive: [BioImage Archive S-BIAD2254](https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD2254). RNA-seq: [GSE343958](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE343958).
