When an AlphaGenome prediction correlates with an experiment, can its output be read as the percentage by which RNA will fall? I see two different questions here. A model can put larger effects higher while predicting a 10% decrease where the experiment measures 40%. That difference matters if a subsequent calculation uses the magnitude.

I reanalyzed published prediction CSVs from a CRISPR interference (CRISPRi) benchmark. Among 352 Gasperini pairs covered by all four models, AlphaGenome had a Pearson correlation of 0.46. Its uncalibrated root mean squared error (RMSE) was nevertheless 24.75 percentage points, larger than the 17.33 points from a baseline that returned the mean observed effect in the other genes. Association did not establish an immediately usable effect scale.

Calling the prediction useless would also miss something. An affine calibration learned from experimental measurements reduced RMSE to 15.40 points when evaluated on genes excluded from calibration training. The distinction between those results is the subject of this analysis.

## Define the population before comparing models

The starting point is a technical article by Murphy and Koo and its public code. The comparison, updated November 4, 2026, evaluates AlphaGenome, Borzoi, Enformer and NTv3 on two K562 CRISPRi datasets. It is an author technical blog comparison, which should be distinguished from a peer-reviewed comparative paper [(1)](#ref-1). This article is a statistical reanalysis of published predictions, not an independent rerun of genomic-model inference or cellular experiments [(2)](#ref-2).

The original experiments measured gene expression after enhancer repression [(3)](#ref-3) [(4)](#ref-4). The exported benchmark tables are selected: Fulco contains validated pairs with decreased expression; Gasperini contains significant, high-confidence pairs. Every observed effect used here was a positive decrease. These data cannot answer what fraction of a model's proposed experimental candidates will validate.

The unit is an enhancer–gene pair. I joined the four model tables one to one on gene_id and enh_loc, checking that observed effects and distances matched. Table 1 summarizes the common coverage.

Table 1. Pairs with matched predictions across models.

| Dataset | AlphaGenome published pairs | Common pairs | Common genes | Common enhancers |
| --- | ---: | ---: | ---: | ---: |
| Fulco | 63 | 62 | 20 | 51 |
| Gasperini | 438 | 352 | 256 | 340 |

Using common pairs reduces differences in evaluation-set composition. It does not standardize the readouts or implementations. Enformer uses cap analysis of gene expression (CAGE), a transcription-initiation readout; the other selected files use RNA-seq, with different aggregation schemes. Borzoi uses a four-model ensemble, AlphaGenome a community implementation with an all-fold distilled checkpoint, and NTv3 the revised 1 Mb model. The analysis does not mix in test-time augmentation (TTA) prediction files, which average predictions across transformed inputs [(1)](#ref-1) [(2)](#ref-2).

## Correlation does not establish the effect scale

Define the measured fractional decrease as

$$
y_i=1-\frac{RNA_{\mathrm{perturbed},i}}{RNA_{\mathrm{control},i}}.
$$

The exported y_delta column already represents this decrease. It must not be subtracted from one again. The prediction p is the difference between the original-sequence prediction and the mean enhancer-shuffled prediction, divided by the original prediction. It is not an absolute RNA count difference.

I measured error using

$$
\mathrm{RMSE}=\sqrt{\frac{1}{n}\sum_i(\hat y_i-y_i)^2}.
$$

RMSE gives each pair equal weight, so genes with more tested enhancers contribute more to the total. Errors below are multiplied by 100 and reported in percentage points. Predicting a 10% decrease instead of 30% is a 20-point difference, not a 20% relative error.

![Published AlphaGenome predictions and observed RNA decreases](shared/alphagenome-crispri-calibration/raw-calibration.png)

Figure 1. Scatterplots drawn from the common published pairs. The dashed line denotes equality; negative predictions are retained. Color denotes distance from enhancer to transcription start site (TSS). The source comparison's scatterplots appear in [Figure 2 of the technical article](https://genomicsxai.github.io/blogs/2026-007/#results). This figure is a new plot of the common pairs, not a reproduction of that figure.

Mean prediction minus mean observation was −12.63 points for Fulco and −12.58 for Gasperini. An offset alone does not explain everything: predicted and observed variation also fail to match perfectly in Gasperini.

Pearson correlation is unchanged by adding a constant or multiplying predictions by a positive constant. Evidence of association therefore does not establish the correct origin or scale. Comparing magnitude error with a mean-only predictor makes this distinction visible.

## Keep evaluation genes out of calibration training

Within each screen, I fitted an affine correction,

$$
\hat y_i=a+b p_i.
$$

Several enhancers can target the same gene. A random pair split could put measurements for that gene in both training and evaluation. Instead, I excluded all pairs belonging to one gene, estimated a and b by ordinary least squares on the other genes, predicted the excluded gene, and repeated this for every gene. All reported calibrated errors use these leave-one-gene-out predictions, without clipping to zero or one.

The mean baseline also excludes the evaluation gene. A distance-only baseline fits an affine function of log10 distance with the same splits. Calibration requires experimental labels: its improvement is supervised and is not an improvement in the original model's zero-shot performance. A held-out gene here is excluded from fitting the correction; it is not established to have been absent from AlphaGenome pretraining.

Table 2. Uncalibrated and calibrated errors. pp denotes percentage points.

| Dataset | Pearson r, raw AlphaGenome | Raw RMSE (pp) | Calibrated RMSE (pp) | Held-out mean RMSE (pp) | Distance-only RMSE (pp) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Fulco | 0.67 | 18.54 | 14.89 | 18.77 | 17.88 |
| Gasperini | 0.46 | 24.75 | 15.40 | 17.33 | 17.38 |

For Gasperini in Table 2, the mean predictor makes smaller errors than the uncalibrated output. Yet the calibrated output improves on the mean. The prediction contains information that a single overall mean does not recover.

To quantify uncertainty, I resampled genes 2,000 times and refitted the calibration in every resample. All methods used the same draws, allowing paired RMSE differences. The 95% intervals use the 2.5th and 97.5th percentiles of the resampled distribution. Calibrated AlphaGenome minus the mean baseline was −1.93 points for Gasperini, with a 95% interval from −2.83 to −1.09. Fulco's point estimate was −3.88 points, but its interval ranged from −9.40 to +1.51 and included zero. Its 62 pairs represent only 20 genes. The favorable point estimate does not establish an improvement there.

![Uncalibrated and gene-held-out calibrated errors](shared/alphagenome-crispri-calibration/heldout-calibration.png)

Figure 2. Uncalibrated and gene-held-out calibrated RMSE on common pairs. Vertical lines show 95% gene-cluster bootstrap intervals; dashed lines show the held-out mean baseline. Method differences should be judged using paired difference intervals, rather than overlap between individual bar intervals.

Calibration reduced error for the other models too. Calibrated Fulco RMSE was 14.56 points for Borzoi, 15.39 for Enformer and 17.65 for NTv3; Gasperini values were 16.33, 16.61 and 16.50. A comparison based only on raw correlation misses correctable scale differences. These are nevertheless comparisons of different implementations, outputs, ensembles and training conditions, not controlled experiments isolating architecture.

## Why this correction cannot be exported to candidate discovery

For interpretation, fitting the affine model to all pairs gives approximately a=0.138 and b=0.848 for Fulco, and a=0.254 and b=0.351 for Gasperini. These are descriptive full-data coefficients; evaluation above used a separately trained equation for every excluded gene.

The correction does not simply enlarge predictions. It adds a positive intercept and compresses their variation. In the descriptive Gasperini fit, an original prediction of zero becomes about a 25% decrease. Among pairs selected for confirmed positive effects, that can reduce average error. Its behavior in a candidate pool containing inactive enhancers has not been measured here.

For experimental design, this is consequential. Reading a prediction of 0.2 as a 20% decrease requires calibration data appropriate to the intended candidate population and evaluation before positive-effect selection. This analysis provides no candidate success rate. Estimating magnitudes among active pairs and discovering active pairs remain separate tasks.

## Sensitivity checks and limits

Some enhancers connect to several genes. Holding out entire connected components of the gene–enhancer graph prevents those enhancers from appearing in both calibration training and evaluation. Calibrated AlphaGenome RMSE was then 14.86 points for Fulco and 15.40 for Gasperini, close to the primary estimates. Using all published AlphaGenome pairs instead of the common subset gave 14.78 and 15.55 points. The direction of the conclusion persisted, but those different-coverage numbers are not used for direct comparisons with other models.

The predicted intervention also differs from the experiment. The benchmark shuffles a 2 kb DNA segment while preserving dinucleotide frequencies. CRISPRi induces repression with systems such as dCas9-KRAB; it does not replace the DNA in that way. The discrepancy includes this intervention mismatch and cannot all be attributed to genomic-model failure [(1)](#ref-1) [(2)](#ref-2).

Both screens use K562. Generalization to other cells or patients was not tested. Aggregated experimental effects were treated as observations; measurement noise was not separated from latent true effects. Gene-cluster intervals do not fully describe that measurement uncertainty. Resampling assumes independence between genes and does not fully account for shared enhancers or screen-wide dependence. Component-held-out sensitivity analysis does not correct these intervals. The calibration and comparisons were selected exploratorily, not preregistered.

In Gasperini, the association retains information useful for magnitude prediction, and supervised calibration improves on the mean baseline. But using the raw output as the effect magnitude produces larger errors than the correlation of 0.46 alone might suggest. Ranking experimental candidates and inserting a predicted decrease into a quantitative calculation require different validation.

## Data and code availability

The prediction CSVs were retrieved from a [pinned public repository commit](https://github.com/Al-Murphy/seq2func_crispri_eval/tree/b4917f5b1a5ccdac8800d00ed31f65cfcb483093). The retrieval manifest verifies inputs by SHA256. Seeds were 20261110 for Fulco and 20261111 for Gasperini, with 2,000 resamples each. The [analysis code](shared/alphagenome-crispri-calibration/analysis.py), [aggregate results](shared/alphagenome-crispri-calibration/results.json) and [reproduction instructions](shared/alphagenome-crispri-calibration/analysis-readme.md) are available.

[Download code, results and figures](shared/alphagenome-crispri-calibration/alphagenome-crispri-calibration.zip)

## References

<a id="ref-1"></a>
1. Murphy A, Koo PK. Benchmarking seq2func models on distal enhancer effects with CRISPRi screens. Genomics x AI. Published June 25, 2026; updated November 4, 2026. [Article](https://genomicsxai.github.io/blogs/2026-007/).

<a id="ref-2"></a>
2. Murphy A. seq2func_crispri_eval. GitHub repository. Snapshot b4917f5b1a5ccdac8800d00ed31f65cfcb483093. [Code and prediction tables](https://github.com/Al-Murphy/seq2func_crispri_eval/tree/b4917f5b1a5ccdac8800d00ed31f65cfcb483093).

<a id="ref-3"></a>
3. Fulco CP, Nasser J, Jones TR, Munson G, Bergman DT, Subramanian V, et al. Activity-by-contact model of enhancer–promoter regulation from thousands of CRISPR perturbations. Nature Genetics. 2019;51:1664–1669. [doi:10.1038/s41588-019-0538-0](https://doi.org/10.1038/s41588-019-0538-0).

<a id="ref-4"></a>
4. Gasperini M, Hill AJ, McFaline-Figueroa JL, Martin B, Kim S, Zhang MD, et al. A Genome-wide Framework for Mapping Gene Regulation via Cellular Genetic Screens. Cell. 2019;176(1–2):377–390.e19. [doi:10.1016/j.cell.2018.11.029](https://doi.org/10.1016/j.cell.2018.11.029).
