## Abstract {#abstract}

Most perturbation-prediction models target changes in RNA, but many drug targets and surface molecules recognized by immune cells are proteins. I recomputed public CRISPR knockout data from melanoma cells in which RNA and surface proteins were measured in the same cells (Perturb-CITE-seq) and asked how well changes in RNA reflect changes in protein. For the knocked-out gene itself, in 5 of 16 gene-by-condition pairs in which the protein fell by 0.5 or more, the mRNA fell by less than 0.1. PD-L1 (CD274) met this in all three conditions (this counting was chosen after seeing the results). For the indirect effects of knocking out other genes (13,251 pairs), the Pearson correlation between RNA and protein changes was 0.26, and 0.42 after correcting for measurement noise (0.40–0.52 across sensitivity analyses). I did not compute confidence intervals. In these data, inferring protein changes from RNA changes alone is limited. The results are restricted to 19 surface proteins, one cell system and knockout perturbations, and do not generalize to other cell types or perturbations.

## Introduction {#_1}

Perturbation-prediction models such as Virtual Cell models are mostly trained on RNA expression and predict how RNA changes after a perturbation. Yet many drug targets and many molecules that immune cells recognize on the cell surface are proteins.

It is well known that mRNA and protein levels correlate only partly across cells and tissues. Schwanhäusser et al. measured mRNA and protein levels and half-lives in cultured mouse cells and reported that mRNA level explains only part of the differences in protein level between genes ([1](#ref-1)). Liu et al. reviewed the relationship between mRNA and protein levels across multiple studies ([2](#ref-2)). These concern comparisons of levels across genes or cells; how well perturbation-induced changes agree within the same cells is a separate question.

The data are the melanoma-cell Perturb-CITE-seq data published by Frangieh et al. ([3](#ref-3)). In Perturb-CITE-seq, genes are knocked out one at a time with CRISPR (disrupting gene function), and RNA and surface proteins are measured together in each single cell. The original study used protein measurements in addition to RNA to investigate mechanisms of immune evasion by cancer cells ([3](#ref-3)).

The question of interest (QOI) is how well the change in the mRNA of a gene after CRISPR knockout predicts the change in the surface protein that gene encodes. I separated two targets.

- (a) Direct target: the protein of the knocked-out gene itself.
- (b) Indirect effects: changes in measured proteins when other genes are knocked out.

The context of use (COU) is to provide a yardstick for judging perturbation predictions trained and evaluated on RNA alone when they are used for protein-level decisions (target expression, surface antigens, immune evasion). The performance of any specific model is not evaluated.

## Methods {#article-methods}

### Data {#_2}

Frangieh et al. performed a CRISPR knockout screen in human melanoma cells and cultured the cells in three conditions ([3](#ref-3)).

- Control (no treatment).
- Stimulation with IFNγ (interferon-γ, an immune signaling molecule).
- Co-culture with T cells that attack cancer cells.

I used the scPerturb release as input ([4](#ref-4), [5](#ref-5)). The data are licensed CC BY 4.0 and can be downloaded without registration.

- 218,331 cells.
- 20 surface proteins, measured by counting DNA tags attached to antibodies (antibody-derived tags, ADT). The measurement derives from CITE-seq ([6](#ref-6)).
- Four isotype controls (antibodies without a target), which serve as a background guide.
- Of the 20 proteins, 19 whose corresponding gene's RNA was measured were used.

Among the knocked-out genes, 236 retained pairs with 30 or more cells (`results/all-pairs.csv`).

### Values and definition of change {#_3}

- **RNA:** Each cell's counts were scaled to a total of 10,000 (CP10k) and transformed with log1p (add 1, then take the natural logarithm).
- **Protein:** ADT counts were normalized per cell by the centered log-ratio (CLR). CLR is log1p(count) minus the mean of that cell's 19 proteins.
- **Change:** For each knockout and condition, cell means were taken, and the difference from the mean of control cells in the same condition was defined as the change. Pairs with fewer than 30 cells were excluded. RNA changes are differences in log1p and protein changes are differences in CLR; both are in natural-logarithm units and dimensionless. A value of −1 corresponds to a decrease of roughly 60%.

### Noise correction and decision rule {#noise-correction}

Measurement noise makes the correlation between RNA and protein changes look weaker than it is. I corrected the correlation as follows.

1. Knockout cells and control cells were each randomly split into two halves (the seed was fixed at 20261020). The two halves share no cells.
2. Agreement between the changes computed from each half (reliability) was calculated separately for RNA and protein. Reliability from half of the cells was converted to a value for all cells with the Spearman–Brown formula, which gives the reliability of a measurement doubled in length from the half-sample value.
3. The correlation was divided by the square root of the product of the two reliabilities (correction for attenuation). This estimates the correlation that would be obtained without noise, and assumes the noise is independent.
4. A "pair with a large protein change" was defined as one whose change was at least three times the noise standard deviation estimated from the difference between the halves.

The decision rule fixed in advance was: a corrected correlation below 0.5 is described as "RNA changes do not represent protein changes well", 0.5 to 0.8 as "partly represent", and 0.8 or more as "represent well".

### Analysis plan and post hoc changes {#plan-changes}

- The analysis plan was fixed before computation (2026-10-20).
- The first computation did not split control cells. This inflates reliability, so the split was added. The corrected correlation changed from 0.422 to 0.423.
- Metrics and sensitivity analyses added after seeing the results are marked "post hoc". These are the threshold for a "clear protein decrease" in direct targets (a decrease of 0.5 or more in CLR), the counting restricted to those pairs, the two sensitivity analyses addressing the properties of CLR, the median of per-protein correlations, the centered correlation, and the correlation among pairs with large protein changes.
- CLR was computed over the 19 proteins that have a corresponding RNA. The plan said 20; CD279 (PDCD1) has no corresponding RNA and was excluded.
- The sensitivity analysis "guide RNA count of one or fewer" was planned as restriction to cells with a multiplicity of infection (MOI) of 1. In the implementation it is restricted to cells with one or fewer guides, and control cells include cells with no detected guide.

### Implementation checks {#_5}

- **Independent recomputation:** I read the file directly with h5py and rewrote the library-size calculation, CLR and group means in separate code. Direct-target values agreed within a maximum difference of 4.9×10⁻⁶, and the indirect-effect correlation (0.26475) and number of pairs (13,251) also agreed (`results/validation.json`).
- **Unit tests:** Four points were checked on synthetic data (`test_analysis.py`).
  - The difference from the control in the same condition.
  - The Spearman–Brown formula.
  - Recovery of the true correlation by the attenuation correction.
  - Each CLR row summing to 0.
- **Reproducibility:** Rerunning with the same seed gave byte-identical result files. Inputs are pinned by SHA-256.

## Results {#article-results}

### The knocked-out gene's own RNA and protein {#1rna}

![Change in mRNA of the knocked-out gene itself and change in its protein](shared/rna-protein-perturbation/figures/01-direct-targets.png)

**Figure 1. Change in the mRNA of the knocked-out gene and change in its protein.** 10 genes × 3 conditions = 30 points (x axis: mRNA change, difference in log1p; y axis: protein change, difference in CLR; both in natural-logarithm units). The dotted line marks an mRNA change of −0.1.

Table 1 shows the values for each knocked-out gene (mean of the three conditions).

**Table 1. Changes in mRNA and protein of the knocked-out gene itself (mean of three conditions)**

| Knocked-out gene | mRNA change (mean of 3 conditions) | Protein change (mean of 3 conditions) |
| --- | ---: | ---: |
| CD274 (PD-L1) | −0.03 | −1.02 |
| CD58 | −0.10 | −0.87 |
| CD47 | −0.26 | −1.09 |
| CD44 | −0.26 | −0.75 |
| CD59 | −0.22 | −0.52 |
| IFNGR1 (CD119) | −0.19 | −0.50 |
| HLA-A | −0.33 | −0.09 |
| HLA-E | −0.56 | −0.12 |

Notes: mRNA is the difference in log1p and protein is the difference in CLR. CXCR4 and KDR, whose changes were barely measurable, are omitted. The table shows means over three conditions; the counts below were determined per condition. PD-L1 is the protein encoded by the CD274 gene, IFNGR1 is interferon-γ receptor 1, and HLA is human leukocyte antigen. B2M is β2-microglobulin, a component of HLA class I molecules. Source: `results/direct-targets.csv`.

The counting and results are as follows.

- **Planned metric:** Of 30 pairs, the mRNA decreased by less than 0.1 in 11/30 (37%). This includes pairs in which the protein also did not change (CXCR4, KDR). I therefore added the following counting after seeing the results (post hoc).
- **Scope:** From 10 genes × 3 conditions = 30 pairs, the six pairs for CXCR4 and KDR were removed, leaving 24 pairs.
- **Pairs with a clear protein decrease:** There were 16/24 pairs (a CLR decrease of 0.5 or more; this threshold was also chosen post hoc).
- **Pairs in which the mRNA hardly decreased:** Among these 16 pairs, 5 (31%) had an mRNA decrease below 0.1. These were CD274 in all three conditions and CD58 in two conditions (decreases of 0.07 with IFNγ and 0.099 in control; the latter is just at the boundary).

The reason the mRNA fell so little was not tested in this analysis. Possible explanations are as follows.

- **Incomplete nonsense-mediated mRNA decay (NMD):** CRISPR knockout introduces small deletions or insertions in DNA so that the protein cannot be made. If the machinery that degrades defective mRNA (NMD) does not work well enough, the mRNA level changes little.
- **Measurement:** A measurement that counts the 3' end side of mRNA cannot see differences in the edited position.
- **Mixed cells:** Unedited cells are mixed in.
- **Misassignment:** Guide RNAs (short RNAs that specify the CRISPR target) are misassigned to cells.
- **Condition-dependent induction:** The influence of induction by conditions such as IFNγ.

Under any of these explanations, looking at RNA alone makes these knockouts appear not to have worked.

HLA-A and HLA-E are the opposite examples: the mRNA fell but the protein hardly changed.

- **HLA-E:** The mean protein signal did not exceed the mean of the isotype controls (`results/protein-background.csv`), so the protein is probably not measured above background.
- **HLA-A:** This would be explained if the antibody recognizes not only HLA-A but also other HLA class I molecules (HLA-B, HLA-C). I did not check the antibody clone used by Frangieh et al.

For CXCR4 and KDR, neither RNA nor protein changed much. The KDR protein was also at background level, and its expression in these cells appears to be low to begin with.

### Indirect effects of knocking out other genes {#2rna}

![Indirect effects: change in mRNA and change in protein](shared/rna-protein-perturbation/figures/02-indirect-effects.png)

**Figure 2. Indirect effects: change in mRNA and change in protein.** For pairs of a knocked-out gene and the protein of another gene (13,251 pairs), the mRNA change (x axis) and the protein change (y axis) are plotted. Color indicates the density of pairs. Red diamonds show the HLA-A and HLA-E proteins when B2M was knocked out. Eighteen pairs outside the x-axis range (−0.4 to 0.4) are not shown. Units are the same as in Figure 1.

The correlation here is the Pearson correlation computed over 13,251 pooled pairs: knockout × 19 proteins × 3 conditions, restricted to pairs with 30 or more cells and excluding the 30 direct-target pairs (236 knocked-out genes). Because pairs that share the same knockout or the same control are included, the pairs are not independent of one another. Table 2 gives the results.

**Table 2. Main analysis of indirect effects**

| Metric (main analysis, 13,251 pairs) | Value |
| --- | ---: |
| Correlation between RNA and protein changes | 0.26 |
| Split-half reliability (RNA/protein, converted to all cells) | 0.62/0.64 |
| Correlation corrected for attenuation | 0.42 |
| Pairs with a large protein change (at least 3 × noise) | 576 pairs |
| Of these, proportion with the same direction of mRNA change (50% by chance) | 67% |
| Correlation among pairs with a large protein change | 0.49 |

Notes: The pairs with agreeing direction numbered 387/576. Source: `results/indirect-summary.csv`.

The corrected correlation of 0.42 falls on the "does not represent well" side of the rule fixed in advance. Only one post hoc sensitivity analysis (0.52) exceeded 0.5. The slope from regressing the protein change on the RNA change was 0.39.

The effect of how the data were aggregated was as follows.

- After subtracting the mean for each protein × condition (centering), the correlation was 0.27, unchanged. Average differences between proteins do not create the correlation.
- When the correlation was computed separately for each protein × condition, the median was 0.15. For a single protein, most knockouts produce small changes, and the correlation is lower still.

The corrected correlations by condition were 0.49 in control, 0.34 with IFNγ and 0.49 in co-culture. In control, the RNA reliability was low at 0.25. The changes themselves were small, and the corrected value is uncertain.

Table 3 shows the sensitivity analyses.

**Table 3. Corrected correlation in the sensitivity analyses**

| Setting | Corrected correlation |
| --- | ---: |
| Main analysis (CLR, all cells) | 0.42 |
| Cells with 1 or fewer guide RNAs (control includes cells with no detected guide) | 0.40 |
| Protein normalized by total ADT | 0.44 |
| Protein normalized by total RNA counts (post hoc) | 0.48 |
| Restricted to the 14 proteins above background (post hoc) | 0.52 |

Notes: "Above background" means the protein's mean exceeds the mean of the isotype controls. Source: `results/indirect-summary.csv`.

The two post hoc sensitivity analyses were added because of a property of CLR. CLR is referenced to the mean of 19 proteins, so when one protein falls strongly, other proteins appear to rise. Indeed, when B2M was knocked out, HLA-A fell while many of the 17 proteins other than HLA-A and HLA-E rose in CLR (condition-wise medians 0.04–0.09, maximum 0.34). Even with normalizations that avoid this apparent change, the corrected correlation was 0.48–0.52. The corrected correlations range from 0.40 to 0.52, and their squares range from 0.16 to 0.27. This is the part of the noise-free variance of change that a linear relationship can explain.

When B2M was knocked out, the HLA-A protein (as measured by its antibody) fell by 0.85–1.45 in CLR, whereas the HLA-A mRNA change was −0.05 to −0.01. B2M is a component of HLA class I molecules, so one interpretation is that, after B2M knockout, HLA-A RNA is still produced but the protein is no longer detected at the surface. This interpretation was not tested in this analysis, and no source is cited for it. A prediction based on RNA alone does not see this effect. Excluding the B2M pairs left the uncorrected correlation at 0.27, essentially unchanged (`results/b2m.csv`, `results/all-pairs.csv`).

## Discussion {#article-discussion}

### What an RNA-only evaluation misses {#virtual-cell}

As a matter of fact, in these data the corrected correlation was 0.4–0.5, and a linear relationship explained only about 20% (0.16–0.27) of the corrected variance. Even among pairs with large protein changes, about one third (189/576 pairs) had an mRNA that did not move in the same direction.

What this shows is that inferring surface protein changes from RNA changes alone is limited in these data. Using an RNA-only prediction as is for protein-determined decisions, such as immune evasion or expression of the target of an antibody drug, is not supported, at least in these data. However, this article does not evaluate any specific model; the statement means only that the same limitation would remain even if a model reproduced the RNA changes correctly.

That the mRNA of the target gene does not fall does not mean the knockout failed to work: in 5 of the 16 pairs in which the protein fell clearly, the mRNA did not fall. Using the change in the target's mRNA as the "size of the effect" in an evaluation metric can therefore overlook effects.

The protein side also has measurement limits. Only about 20 surface proteins are measured by antibodies, and they are affected by antibody specificity and background. The position of this analysis is not to decide whether RNA or protein is "correct", but to show where the two disagree when both are measured.

## Limitations {#_4}

- **Generalization:** It is unknown whether the findings apply to intracellular proteins, modifications such as phosphorylation, other cell types, or perturbations other than knockout (inhibitors, CRISPRa).
- **Selection of targets:** The 19 proteins are biased toward immune-related surface molecules.
- **Antibody specificity:** Antibodies may recognize other molecules (for example HLA-A).
- **Normalization:** Values change with the protein normalization method (the range is shown in the sensitivity analyses).
- **Timing:** RNA and protein were measured at the same time point, so the time lag (RNA changes first and protein later) cannot be assessed.
- **Uncertainty:** Confidence intervals for the direction agreement rate and the correlations were not computed. Pairs share knockouts and controls and are not independent, so a naive interval is unsuitable. Reliability was estimated from a single random split.
- **Thresholds:** The 0.5 for a clear protein decrease, the 0.1 for an mRNA that did not fall, and the factor of 3 for a large change are arbitrary criteria. The count of 5/16 depends on them, and the CD58 decrease in control (0.099) lies just inside the threshold.
- **Knockout efficiency:** Whether cells were edited and whether guide RNAs were assigned correctly were not verified in this analysis.

## Conclusion {#article-conclusion}

In these data (melanoma cells, CRISPR knockout, 19 surface proteins), changes in RNA reflected changes in protein only partly. For the knocked-out gene itself, in 5 of the 16 pairs with a clear protein decrease, the mRNA fell by less than 0.1. For indirect effects, the corrected correlation was 0.42 (0.40–0.52 in sensitivity analyses), below the 0.5 fixed in advance in the main analysis. The results are limited to one cell system and one measurement platform, and no uncertainty intervals are attached.

## Data and code availability {#availability}

The analysis plan, the code for acquisition, aggregation, testing, figures and independent recomputation, the SHA-256 of the inputs, the result tables and the validation results are included in the [companion material](shared/rna-protein-perturbation/rna-protein-perturbation-companion.zip). The input h5ad files (about 1.5 GB) are not included and are downloaded from scPerturb on Zenodo (CC BY 4.0) ([5](#ref-5)). The rerun is performed in this order.

`python acquire.py && python test_analysis.py && python analysis.py && python figures.py && python validate.py`

The environment is Python 3.12 with anndata, h5py, numpy, scipy, pandas, matplotlib and requests. The random seed was fixed at 20261020. The figures were produced in this analysis and no figures from the original paper were reproduced.

## References {#article-references}

1. <span id="ref-1"></span>Schwanhäusser B, Busse D, Li N, Dittmar G, Schuchhardt J, Wolf J, et al. Global quantification of mammalian gene expression control. Nature. 2011;473(7347):337–342. [doi:10.1038/nature10098](https://doi.org/10.1038/nature10098).
2. <span id="ref-2"></span>Liu Y, Beyer A, Aebersold R. On the dependency of cellular protein levels on mRNA abundance. Cell. 2016;165(3):535–550. [doi:10.1016/j.cell.2016.03.014](https://doi.org/10.1016/j.cell.2016.03.014).
3. <span id="ref-3"></span>Frangieh CJ, Melms JC, Thakore PI, Geiger-Schuller KR, Ho P, Luoma AM, et al. Multimodal pooled Perturb-CITE-seq screens in patient models define mechanisms of cancer immune evasion. Nat Genet. 2021;53(3):332–341. [doi:10.1038/s41588-021-00779-1](https://doi.org/10.1038/s41588-021-00779-1).
4. <span id="ref-4"></span>Peidli S, Green TD, Shen C, Gross T, Min J, Garda S, et al. scPerturb: harmonized single-cell perturbation data. Nat Methods. 2024;21(3):531–540. [doi:10.1038/s41592-023-02144-y](https://doi.org/10.1038/s41592-023-02144-y).
5. <span id="ref-5"></span>Peidli S, Green TD, Shen C, Gross T, Min J, Taylor-King JP, et al. scPerturb single-cell perturbation data: RNA and protein h5ad files [Dataset]. Zenodo; 2022. Version 1.0. [doi:10.5281/zenodo.7041849](https://doi.org/10.5281/zenodo.7041849). Licence: CC BY 4.0.
6. <span id="ref-6"></span>Stoeckius M, Hafemeister C, Stephenson W, Houck-Loomis B, Chattopadhyay PK, Swerdlow H, et al. Simultaneous epitope and transcriptome measurement in single cells. Nat Methods. 2017;14(9):865–868. [doi:10.1038/nmeth.4380](https://doi.org/10.1038/nmeth.4380).
