Accuracy rose from 17.5% to 24.4%. An AI model reading cell images appeared better able to handle changes in imaging conditions. But which drug images contributed the approximately 6.9-percentage-point gain?

BatchBench, a preprint released on October 21, 2026, benchmarks identification of administered compounds from Cell Painting images acquired at different sources. I examined its score table and cross-checked 95,215 public label and metadata rows. Reconstructing the gain from rounded subgroup scores showed that approximately 94.5% of the improvement with AdaBN came from images of eight positive-control compounds. This is not evidence of an error. It means that improved aggregate accuracy and improved discrimination of compounds of interest are different claims.

## Evaluation at unseen sources {#_1}

Cell Painting stains intracellular structures to characterize morphological drug responses. Images also contain differences in microscopes, staining, plates and experiment dates.

BatchBench makes this problem central. It selects the 2,000 most frequent compounds from JUMP Cell Painting and one field of view per well. Inputs are five-channel images; the task is to identify the administered compound among 2,000 classes ([1](#ref-1)).

Eight of nine public sources provide training data, with source 2 reserved for validation. Four additional sources provide private test data. This differs from randomly splitting images from the same source. Reaggregating public labels and source information confirmed 81,880 training images, 13,335 validation images, 2,000 training classes and 1,877 validation classes. No compound appeared only in validation.

The unseen unit is the source generating the data, not a new compound whose efficacy must be predicted. Identifying compound labels from images is also distinct from predicting targets, mechanisms or patient efficacy.

Use of test images is not universally prohibited. Test-time adaptation using unlabeled images is allowed. AdaBN recalculates batch-normalization statistics using images from a plate, adapting to its distribution without accessing labels. Using the four private sources for training, pretraining or model selection is prohibited. I also examined the [official baseline implementation](https://github.com/ml-jku/batchbench-baselines/tree/df18b76bbf6233a0a8bdb423801c5353e613078f) ([2](#ref-2)).

## Eight control compounds contribute 36% of test images {#836}

Results are divided into three image groups. POSCON contains eight positive-control compounds with many training images and strong morphological effects. TARGET comprises images from a reference collection spanning targets and mechanisms; REST contains the other images.

I calculated proportions from image counts in [Table 1 of the original paper](https://arxiv.org/html/2610.30104v1).

Table 1. Group composition of public images and private test images.

| Image group | Public images | Public proportion | Private test proportion |
| --- | ---: | ---: | ---: |
| POSCON | 48,574 | 51.0% | 36.2% |
| TARGET | 23,455 | 24.6% | 54.9% |
| REST | 23,186 | 24.4% | 8.9% |

Aggregate accuracy is an image-count-weighted average of subgroup accuracies, not an equally weighted average over compounds. Eight compounds can have substantial influence if they contribute many images.

The public subgroup compound counts sum to 8 + 293 + 1,926, exceeding 2,000. Label-level inspection found 227 compounds in both TARGET and REST. Image rows belong to separate groups, but a compound can appear across groups. Treating them as three disjoint compound sets would misrepresent the aggregation.

For this check I used the 200-pixel CSV and the 500-pixel NPZ and label arrays. Image identifiers, sources, batches, plates, groups and labels matched in row order, with no duplicate image identifiers. I did not acquire image pixels or private test data ([3](#ref-3)).

## Decomposing the AdaBN gain {#adabn}

[Table 2 of the original paper](https://arxiv.org/html/2610.30104v1) reports means and sample standard deviations over three random seeds. The calculations below use the means, in percentage accuracy.

Table 2. Mean accuracy reported in the original paper (%).

| Method | Overall | POSCON | TARGET | REST |
| --- | ---: | ---: | ---: | ---: |
| ResNet18 without adaptation | 17.5 | 46.5 | 1.2 | 0.2 |
| deepCORAL | 20.1 | 50.2 | 3.4 | 0.7 |
| AdaBN | 24.4 | 64.6 | 1.9 | 0.2 |
| TENT | 24.9 | 66.1 | 1.7 | 0.2 |
| ARM-BN | 26.0 | 66.5 | 3.5 | 0.4 |

Compared with no adaptation, AdaBN improves POSCON by 18.1 percentage points, TARGET by 0.7 points and REST by zero at the displayed precision. Multiplying these changes by private-test image proportions gives contributions of approximately 6.55, 0.38 and zero points. POSCON accounts for approximately 94.5% of the reconstructed gain.

![Subgroup performance and contributions to the AdaBN gain](shared/batchbench-score-audit/figures/subgroups-and-gain.png)

Figure 1. Left: mean accuracies from [Table 2 of the original paper](https://arxiv.org/html/2610.30104v1). Distributed code includes all seven methods in that table. Right: AdaBN minus no adaptation, weighted by private-test image proportions. This descriptive calculation uses rounded means and does not test significance of the improvement.

This decomposition requires no model retraining. Weighted subgroup scores reproduced reported totals within less than 0.043 percentage points for all seven methods, consistent with rounding.

It would also be unwarranted to call AdaBN useless. Reliable identification of positive controls can support checks of the measurement system. The issue is which improvement a number represents. The aggregate result alone does not establish improved performance for compounds represented by few images.

## Composition changes the ranking of methods {#_2}

I performed a further sensitivity calculation, fixing subgroup accuracies at published values while varying the positive-control image weight. The relative weights of TARGET and REST remained fixed at private-test proportions.

This is reweighting, not an experiment rerunning AI on a different data composition.

Excluding positive controls, accuracy weighted by TARGET and REST image counts is approximately 1.66% for AdaBN and 3.02% for deepCORAL. This reverses their order in the original aggregate score. Based on rounded values, their curves cross at a positive-control image proportion of approximately 8.6%.

![Sensitivity to aggregation weights and image composition by public source](shared/batchbench-score-audit/figures/mixture-and-sources.png)

Figure 2. Left: reweighting with subgroup accuracies fixed. The dashed line marks the private-test positive-control proportion. Right: public metadata aggregated by source; source 2 is validation. Sources differ in compound composition as well as imaging conditions.

The 8.6% value is not an operational threshold. A changed image composition can change adaptation statistics and thus subgroup accuracies themselves; this calculation holds them fixed. Seed-level predictions and their covariance were unavailable, so no confidence interval for the ranking difference is reported.

A measurement system dominated by positive-control images and one comparing weak responses from sparsely imaged compounds place different weights on performance. One aggregate accuracy cannot represent all these uses.

## Does removing batch effects leave only biology? {#_3}

Batch correction is more than subtracting technical differences. If technical conditions are associated with compound composition, making sources harder to distinguish may also attenuate biological differences of interest. Conversely, good performance that retains source information need not transfer to the next experiment.

BatchBench combines cross-source evaluation, subgroup performance and unlabeled adaptation in a useful framework. Its score table cannot, however, separate how much performance loss reflects technical differences, weak phenotypes or limited image counts. Positive controls differ in training-image count, phenotype strength and plate arrangement. This reaggregation does not isolate those causal effects either.

Aggregate accuracy depends on the POSCON, TARGET and REST mixture. Macro accuracy, giving each compound equal weight, cannot be calculated from this table. A cross-source score difference cannot be treated as a single performance difference independent of drug composition.

## Data and code availability {#_4}

The [analysis code, aggregate inputs, results and figures](shared/batchbench-score-audit/batchbench-score-audit.zip) are provided. `analysis.py` and `plot.py` regenerate reweighting calculations and figures. `fetch_data.py` and `extract.py` retrieve public metadata at a fixed revision and recheck row alignment, source splits and overlapping compound groups. I did not execute the original model code.

Scores are fixed to [Table 2 of preprint version 1](https://arxiv.org/html/2610.30104v1). When checked, the hosting Space's results JSON contained sample-format rows with example URLs that did not correspond to the paper's scores; I therefore did not cite it as a current measured leaderboard. The article reaggregates published results rather than reevaluating models on the private test set. Sources were checked on October 24, 2026.

## References

1. <span id="ref-1"></span> Topf S, Sanchez-Fernandez A, Klambauer G. [BatchBench: Benchmarking AI Robustness to Batch Effects and Domain Shift in Biomedical Images](https://arxiv.org/abs/2610.30104v1). [Preprint]. arXiv; 2026. Version 1, arXiv:2610.30104v1, posted 2026 Oct 21; not peer-reviewed. [cited 2026 Oct 24].
2. <span id="ref-2"></span> Machine Learning at JKU. [BatchBench baseline implementation](https://github.com/ml-jku/batchbench-baselines/tree/df18b76bbf6233a0a8bdb423801c5353e613078f) [software]. Commit df18b76bbf6233a0a8bdb423801c5353e613078f [cited 2026 Oct 24].
3. <span id="ref-3"></span> AI Lab JKU. [JUMP Cell Painting challenge datasets](https://huggingface.co/datasets/ai-lab-jku/jumpcp-challenge-datasets/tree/a5c2888d320f57e14d1c7d4dd4374397935ab9a4) [dataset]. Revision a5c2888d320f57e14d1c7d4dd4374397935ab9a4 [cited 2026 Oct 24].
