5-FU and olaparib have different mechanisms of action. Yet numerical profiles of cultured-cell morphology can make their responses look similar. Image-profile similarity is used in drug discovery as a clue to a drug's activity or mechanism of action ([1](#ref-1)). What does this proximity represent for a model learning drug similarity from images?

A Cell Painting study published on October 21, 2026 provides a concrete example. Two drugs that were close in cells spread on a flat surface separated when cells were grown as small three-dimensional aggregates. The two drugs also differed in DNA damage-response, DNA-synthesis and gene-expression measurements ([2](#ref-2)).

I re-examined published figure values and processed image features, summarized drug similarities, fixed concentrations and restricted comparisons to shared features. The question examined is not whether 3D is intrinsically correct but whether the experimental definition of drug response changes the list of similar drugs. If it does, I also ask how much of the change the public data allow to be attributed to culture format.

## Measuring cell morphology {#_1}

Cell Painting labels nuclei, mitochondria, cytoskeleton and other components with fluorescent dyes, then extracts shape, intensity and texture features ([3](#ref-3)). A drug response becomes a multivariate fingerprint. Cell-based screening in drug discovery has mostly used 2D culture. 3D culture is expected to be closer to the tissue microenvironment, but imaging and analysis pose specific challenges ([4](#ref-4), [5](#ref-5)). This study examined the colorectal cancer cell lines HCT116 and HT29 and 52 drugs ([2](#ref-2)).

Overlapping cells and depth-dependent attenuation complicate 3D imaging. The authors cleared small spheroids, detected cells in each of 12 optical sections spaced 5 µm apart, standardized each section against controls imaged at the same depth and aggregated features into well-level profiles. They also compared this approach with images projected into a single plane ([2](#ref-2)).

Here, single-cell includes identifying cells within sections. The same cell appears in several sections; the original paper estimates that each cell is detected three to four times, giving roughly 400 cells per HCT116 spheroid ([2](#ref-2)). Detected objects are therefore not independent cells. Similarly, the 630 drug pairs below do not constitute 630 independent experiments.

The 2D and 3D data differ in more than culture format. As described in the original paper, the 3D data came from a single experiment on six 384-well plates, whereas the 2D data came from a separate four-plate run. Imaging magnification was 20× in 2D and 30× in 3D. The 2D profiles received illumination correction and outlier-based quality control; illumination correction was not applied to the 3D spheroids ([2](#ref-2)). The 2D-versus-3D differences discussed below therefore include differences in experiment date, optics and preprocessing, in addition to culture format.

## Olaparib moves away from 5-FU {#5-fu}

I first reaggregated Source Data for [Figure 5d of the original paper](https://doi.org/10.1038/s41467-026-78596-5). The 36 HCT116 drugs retained in both 2D and 3D generate 630 pairs. These drugs passed selection using grit, a metric combining response strength and reproducibility; this is not a comparison of all 52 drugs.

The authors used cosine similarity, which increases as two feature vectors point in similar directions. Each drug had several concentrations. The table uses the maximum similarity across pairs of concentrations that passed the response criterion, rather than a fixed-concentration comparison. The Methods section of the original paper describes a consensus profile for each compound, but the released code computes similarity for each compound-concentration combination and takes the maximum ([6](#ref-6)). If the number of qualifying combinations differs between formats, a maximum is not a like-for-like comparison condition. This is why a fixed-concentration comparison follows.

**Table 1.** Drug similarity and rank using the authors' concentration aggregation.

| Relationship between 5-FU and olaparib | 2D | 3D |
| --- | ---: | ---: |
| Similarity using the authors' concentration aggregation | 0.886 | 0.377 |
| Olaparib rank among the other 35 shared drugs | 1 | 20 |

![Drug similarity changes with culture format](shared/cellpainting-2d-3d/figures/drug-neighborhoods.png)

**Figure 1.** Redrawn values from [Figure 5d of the original paper](https://doi.org/10.1038/s41467-026-78596-5). Each point is a drug pair; points below the dashed line have lower similarity in 3D. The red point represents 5-FU and olaparib. Pairs sharing a drug are not independent. Concentrations producing the maximum may differ between formats.

The original paper presented these two drugs as an example of a large 3D difference in similarity, so they were selected exploratorily. Across the same 630 pairs, the median difference (3D minus 2D) was −0.04 (interquartile range −0.16 to +0.08); similarity was lower in 3D for 370 pairs and higher for 260. The −0.51 difference for 5-FU and olaparib is the seventh largest in absolute value. Culture format moves similarity in both directions, and for most pairs the movement is small. Large differences are chosen from the edge of this distribution, and the edge contains both real change and measurement fluctuation. Recalculating at fixed concentrations uses the same data under a different aggregation and cannot remove this selection.

According to the original paper, neither drug exceeded the grit threshold of 1.96 in spheroid-wide projections (MIP) at the highest dose (5-FU 1.05, olaparib 0.98), and the separation was detected only in profiles aggregated from single cells. The paper also states that both drugs had previously been reported to show no measurable cytotoxicity in either format in a metabolic-activity assay ([2](#ref-2)). The separation therefore depends on the analysis method as well. Conversely, a morphological response was measurable at exposures at which cytotoxicity was not.

In this example, a search for drugs similar to 5-FU returns different results depending on culture format. This is, however, an existence proof from one pair, not an average change across drugs. If image-profile proximity is used for model training or candidate retrieval, the proximity labels may be conditional on culture format and readout. Which pairs move, and by how much, cannot be learned from this one pair.

## Fixing concentrations and image features {#_2}

To reduce flexibility in concentration selection, I fixed 5-FU at 10 µM and olaparib at 3 µM, the concentrations used for the imaging and molecular comparisons. Drug exposure lasted 48 h. The following calculations are additional analyses for this article.

The inputs were public HCT116 well-level features used for [Figures 5b and 4b of the original paper](https://doi.org/10.1038/s41467-026-78596-5). Each drug and format contributed four wells; the median of each feature defined its drug profile. The four wells are split two and two across two plates. The original design has two biological and two technical replicates ([2](#ref-2)); I did not verify how plates map onto these. I did not resegment raw images or repeat standardization against controls.

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

It is also necessary to separate a biological separation from larger measurement noise in 3D. Cosine similarity is lower for the same biological relationship when the profiles are noisier. The original paper itself notes that lower 3D grit scores could reflect technical difficulty of volumetric imaging, weaker responses, or both ([2](#ref-2)). Inspecting correlations among well profiles to detect batch effects and other technical artifacts is a recommended practice ([7](#ref-7)). From the same inputs, I therefore computed the cosine between profiles aggregated separately from the two plates for the same drug (416 shared features). For 5-FU it was 0.93 in 2D and 0.61 in 3D; for olaparib, 0.80 in 2D and 0.64 in 3D. Replicate agreement is lower in 3D. Taking the square root of the product of the two replicate agreements as a guide to the similarity attainable between the two profiles ([8](#ref-8)) gives 0.86 in 2D and 0.62 in 3D. The ratio of observed similarity to this guide is 0.94 in 2D and 0.57 in 3D. The 3D value remains lower on this ad hoc scale. However, treating two-plate cosine agreements as reliabilities requires assumptions including independent mean-zero errors and replication of the same latent profile. Applying correlation attenuation correction to these cosines was not validated. These values therefore establish neither noise-free similarities nor a test excluding noise alone.

The two drugs are not always dissimilar in 3D. In the 4 × 4 concentration grid (416 shared features, median, cosine), similarity was lower in 3D in 12 of 16 cells, and all four reversed cells were in the 0.3 µM 5-FU row. The original paper states that the separation is consistent across doses ([2](#ref-2)). My grid inherits the published processed features and well filtering, and differs from the supplementary-figure values by up to 0.14. At 0.3 µM 5-FU, the 2D similarity is low (0.07 to 0.30); comparisons at concentrations with little response are comparisons between profiles close to noise. Concentration changes the ratio of response magnitude to measurement noise. Reducing a response to a drug-name label while dropping concentration and time loses that information.

## DNA damage response and DNA synthesis give different orderings {#dnadna}

Do biological measurements support the morphological difference? 5-FU, a pyrimidine antimetabolite, affects DNA and RNA synthesis ([9](#ref-9)), whereas olaparib traps PARP1 and PARP2 on DNA ([10](#ref-10)). Both relate to DNA replication, but at different points. In 3D culture, the authors measured γH2AX foci, a DNA damage-response-related readout, and incorporation of 5-ethynyl-2'-deoxyuridine (EdU) into newly synthesized DNA, a DNA-synthesis readout. Reaggregating well-level Source Data for [Figure 6b of the original paper](https://doi.org/10.1038/s41467-026-78596-5) gave these medians.

**Table 3.** DNA damage-response and DNA-synthesis measurements in 3D culture.

| Median measurement | DMSO control | 5-FU 10 µM | Olaparib 3 µM |
| --- | ---: | ---: | ---: |
| γH2AX foci per nucleus | 0.87 | 1.89 | 4.84 |
| EdU-positive fraction | 34.8% | 7.7% | 16.3% |

Olaparib produced more γH2AX foci, whereas 5-FU produced a lower EdU-positive fraction. Relative to control, the EdU-positive fraction fell from 34.8% to 7.7% with 5-FU (27.1 percentage points) and to 16.3% with olaparib (18.5 percentage points); as ratios to control these are about 0.22 and 0.47. These readouts do not follow a single ordering in which greater damage means stronger suppression of DNA synthesis. For the 5-FU versus olaparib comparison, the original paper reports uncorrected two-sided Mann–Whitney p = 2.7 × 10⁻⁴ for γH2AX foci and p = 5.9 × 10⁻⁴ for the EdU-positive fraction ([2](#ref-2)). However, the 13 spheroids per condition were technical replicates in separate wells within one experiment, not 13 patients or 13 independent experiments. These p-values reflect differences relative to well-to-well variation within one experiment, not reproducibility across repeated experiments. The EdU-positive fraction is read as the fraction of cells in S phase, but the possibility that 5-FU, which acts on nucleotide metabolism, alters incorporation itself cannot be separated by this measurement alone.

In RNA sequencing, CDKN1A, which encodes the cell-cycle-arrest-associated protein p21, had log2 fold changes of +3.49 (FDR 8.3 × 10⁻⁷) for 5-FU and +1.35 (FDR 0.025) for olaparib relative to control. E2F-target and G2M-checkpoint gene sets were depleted by both drugs, more strongly by 5-FU. These are outputs of the authors' differential-expression analysis, not a reanalysis of raw counts here. A smaller FDR-adjusted p-value in one comparison does not by itself establish a significant difference between drugs. The RNA experiment had two biological and two technical replicates, n = 4 per drug and n = 3 for control after one low-read-count sample was excluded. Technical replicates were treated as separate samples in the authors' analysis ([2](#ref-2)).

As far as the text and figures show, these molecular measurements were made in 3D spheroids only; no 2D monolayer measurement of the same readouts is reported ([2](#ref-2)). The data therefore show that a molecular difference accompanies the image separation in 3D, but not whether the molecular responses to the two drugs were similar in 2D. The original paper observes that 5-FU drives the p53/p21 program more strongly while γH2AX does not follow the same order, and it proposes that the 3D format changes how each drug's mix of DNA damage, replication stress and nucleolar stress is converted into a p53/p21 response ([2](#ref-2)). This is the authors' proposal, not something tested by a direct comparison with 2D.

In 3D, the two drugs closest to 5-FU were abbreviated AMG23 and Nutli in the authors' table, with similarities of 0.771 and 0.741 (`results/neighbors.csv`). The original paper identifies them as the MDM2 inhibitors AMG-232 and Nutlin-3 and states that 5-FU groups with p53 activators, which fits a p53/p21-related interpretation. However, Nutli was already second in 2D (0.825), and AMG23 was eighth (0.746); proximity to p53 activators was already present in 2D. The neighborhood of 5-FU did not change completely in 3D; the change centers on its relationship with olaparib. According to the original paper, in TP53-mutant HT29 the MDM2 inhibitors elicited no phenotype, while 5-FU remained similar to other antimetabolites. The authors themselves add caveats to this interpretation: the link to p53 relies mainly on the MDM2 inhibitors, and HCT116 and HT29 differ in more than TP53. The molecular and image data can narrow the mechanism to examine next but cannot settle a causal p53 effect ([2](#ref-2)).

## Discussion and conclusion {#_3}

The answer to the opening question is as follows. In these public data, image profiles of 5-FU and olaparib that were close in 2D were not close in 3D. The decrease remained after concentrations and features were fixed, from 0.808 to 0.354 with 416 shared features. Omitting one plate leaves the 2D and 3D ranges non-overlapping. Reading the difference as an effect of culture format alone, however, leaves several other explanations open.

- Differences other than format: experiment date, magnification (20× and 30×), depth-dependent correction and the use of illumination correction all differ between 2D and 3D ([2](#ref-2)).
- Measurement noise: replicate agreement is lower in 3D than in 2D. The 3D value stays lower after an ad hoc scale adjustment, which does not fully estimate the noise contribution.
- Selection: this pair was chosen from the edge of 630 pairs, whose median difference is only −0.04.
- Scope: one cell line, one experiment, four wells per condition, with no independent repeat.

This analysis also did not test whether 3D predicts clinical drug efficacy more accurately.

The result changes how the original study is read. The claim that the drugs were nearly indistinguishable in 2D and separated in 3D is supported by one readout, image-profile similarity. The molecular measurements in 3D (γH2AX, EdU, CDKN1A) demonstrate biological differences between the drugs without assigning a fraction of the image-cosine difference to biology. They do not show that the 2D similarity held at the molecular level. Without the same molecular measurements in 2D, it cannot be determined whether the 2D images failed to capture a molecular difference or whether the molecular responses were in fact similar in 2D. The format-dependence claim turns on this distinction.

Matched optics and preprocessing, replicate correspondence and molecular measurements in both formats were unavailable, so the contribution of culture format itself could not be identified.

For models that learn drug similarity from images, the distribution of the 630 differences is informative. The effect of culture format is small for most drug pairs and large for some. This one pair therefore supports neither the statement that similarities learned in 2D cannot be used in 3D nor its opposite. The open question is whether the pairs that move most can be identified in advance. In model evaluation, reporting similarity labels separately by culture format, as a distribution of per-pair changes rather than a single-example comparison, carries more information than this example does. Even for the same drug, the neighborhood can depend on the environment, the measurement time and the readout.

## Data and code availability {#_4}

The [analysis code, extracted data, figures and calculated results](shared/cellpainting-2d-3d/cellpainting-2d-3d.zip) are provided. Run `analysis.py` and then `plot.py` in Python to regenerate the article's tables and figures. The authors' repository commit is fixed, and extraction sources and SHA-256 hashes are recorded.

Drug ranks reaggregate the authors' similarity table. Fixed-concentration and shared-feature comparisons are additional calculations from processed well-level features released as figure inputs. The authors' supplementary figures use different processed inputs, so this is not claimed as complete reproduction of all concentration-dependent values. The distribution of the 630 differences and the plate-wise replicate agreement are additional descriptive statistics computed from the included `inputs/` and are not part of `analysis.py`. The [additional descriptive script](shared/cellpainting-2d-3d/extra-descriptive-checks.py) recomputes them from the same inputs. Raw images and raw RNA counts were not reanalyzed; no trained AI model was evaluated and no new drug experiment was performed.

## References

1. <span id="ref-1"></span> Chandrasekaran SN, Ceulemans H, Boyd JD, Carpenter AE. Image-based profiling for drug discovery: due for a machine-learning upgrade? Nat Rev Drug Discov. 2021;20(2):145–159. [doi:10.1038/s41573-020-00117-w](https://doi.org/10.1038/s41573-020-00117-w).
2. <span id="ref-2"></span> Ringers C, Holmberg D, Larsson A, Jung B, Jarvius M, Luchniak A, et al. High-content morphological profiling by Cell Painting in 3D spheroids. Nat Commun. 2026;17:10790. [doi:10.1038/s41467-026-78596-5](https://doi.org/10.1038/s41467-026-78596-5).
3. <span id="ref-3"></span> Bray MA, Singh S, Han H, Davis CT, Borgeson B, Hartland C, et al. Cell Painting, a high-content image-based assay for morphological profiling using multiplexed fluorescent dyes. Nat Protoc. 2016;11(9):1757–1774. [doi:10.1038/nprot.2016.105](https://doi.org/10.1038/nprot.2016.105).
4. <span id="ref-4"></span> Langhans SA. Three-dimensional in vitro cell culture models in drug discovery and drug repositioning. Front Pharmacol. 2018;9:6. [doi:10.3389/fphar.2018.00006](https://doi.org/10.3389/fphar.2018.00006).
5. <span id="ref-5"></span> Booij TH, Price LS, Danen EHJ. 3D cell-based assays for drug screens: challenges in imaging, image analysis, and high-content analysis. SLAS Discov. 2019;24(6):615–627. [doi:10.1177/2472555219830087](https://doi.org/10.1177/2472555219830087).
6. <span id="ref-6"></span> Pharmbio. [colopaint3D: analysis code and Source Data](https://github.com/pharmbio/colopaint3D/tree/5f209bcfbccdef2b5c0c97060b9d82aef085f2cb) [software and data]. Commit 5f209bcfbccdef2b5c0c97060b9d82aef085f2cb [cited 2026 Oct 23]. Image archive: [BioImage Archive S-BIAD2254](https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD2254). RNA-seq: [GSE343958](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE343958).
7. <span id="ref-7"></span> Caicedo JC, Cooper S, Heigwer F, Warchal S, Qiu P, Molnar C, et al. Data-analysis strategies for image-based cell profiling. Nat Methods. 2017;14(9):849–863. [doi:10.1038/nmeth.4397](https://doi.org/10.1038/nmeth.4397).
8. <span id="ref-8"></span> Spearman C. The proof and measurement of association between two things. Am J Psychol. 1904;15(1):72–101. [doi:10.2307/1412159](https://doi.org/10.2307/1412159).
9. <span id="ref-9"></span> Longley DB, Harkin DP, Johnston PG. 5-fluorouracil: mechanisms of action and clinical strategies. Nat Rev Cancer. 2003;3(5):330–338. [doi:10.1038/nrc1074](https://doi.org/10.1038/nrc1074).
10. <span id="ref-10"></span> Murai J, Huang SY, Das BB, Renaud A, Zhang Y, Doroshow JH, et al. Trapping of PARP1 and PARP2 by clinical PARP inhibitors. Cancer Res. 2012;72(21):5588–5599. [doi:10.1158/0008-5472.CAN-12-2753](https://doi.org/10.1158/0008-5472.CAN-12-2753).
