Accuracy rose from 17.5% to 24.4%. An AI model reading cell images appeared better able to handle changes in imaging conditions. But which drug images contributed the approximately 6.9-percentage-point gain?

BatchBench, a preprint released on October 21, 2026 ([1](#ref-1)), benchmarks identification of administered compounds from Cell Painting images acquired at different sources. I examined its score table and cross-checked 95,215 public label and metadata rows. Reconstructing the gain from rounded subgroup scores showed that approximately 94.5% of the improvement with AdaBN came from images of eight positive-control compounds. The original paper itself states that the aggregate is dominated by these images and reports subgroup scores alongside it ([1](#ref-1)). The calculation here quantifies that contribution; it does not point out an error. Improved aggregate accuracy and improved discrimination of compounds of interest are different claims.

## Evaluation at unseen sources {#_1}

Cell Painting stains intracellular structures to characterize morphological drug responses ([2](#ref-2)). Images also contain differences in microscopes, staining, plates and experiment dates. JUMP Cell Painting is a large public dataset imaged at 13 sources with different microscopes and workflows ([1](#ref-1), [3](#ref-3)), and batch effects across laboratories and equipment have been noted to limit the integration of image-based profiles ([4](#ref-4)).

BatchBench makes this problem central. It selects the 2,000 most frequent compounds from JUMP Cell Painting and one field of view per well. Inputs are five-channel images; the task is to identify the administered compound among 2,000 classes ([1](#ref-1)).

Eight of nine public sources provide training data, with source 2 reserved for validation. Four additional sources provide private test data, and test images also come from unseen batches and plates ([1](#ref-1)). This differs from randomly splitting images from the same source. Reaggregating public labels and source information confirmed 81,880 training images, 13,335 validation images, 2,000 training classes and 1,877 validation classes ([5](#ref-5)). No compound appeared only in validation.

The unseen unit is the source generating the data, not a new compound whose efficacy must be predicted. Identifying compound labels from images is also distinct from predicting targets, mechanisms or patient efficacy.

Use of test images is not universally prohibited. Test-time adaptation using unlabeled images is allowed. AdaBN recalculates batch-normalization statistics using images from a plate, adapting to its distribution without accessing labels ([1](#ref-1), [6](#ref-6)). Using the four private sources for training, pretraining or model selection is prohibited ([1](#ref-1)). I also examined the [official baseline implementation](https://github.com/ml-jku/batchbench-baselines/tree/df18b76bbf6233a0a8bdb423801c5353e613078f) ([7](#ref-7)).

## Scope and sources {#scope}

I read the full HTML text of BatchBench version 1 and used its text and Tables 1 and 2 for the calculations ([1](#ref-1)). Subgroup scores are limited to the three-decimal means and sample standard deviations over three random seeds printed in Table 2; I have neither seed-level predictions nor images. Public metadata were used to aggregate row counts, sources, groups and labels ([5](#ref-5)). Values displayed on the leaderboard side were not used. Literature other than BatchBench is cited as background within the extent of bibliographic records and abstracts, not as a re-examination of its detailed results.

## Eight control compounds contribute 36% of test images {#836}

Results are divided into three image groups. POSCON contains eight positive-control compounds present on every plate, usually at fixed positions, with many training images and strong morphological effects. TARGET comprises images of 293 compounds from a reference collection spanning targets and mechanisms; REST contains the other images, with about 12 images per compound in the public split ([1](#ref-1)).

I calculated proportions from image counts in [Table 1 of the original paper](https://arxiv.org/html/2610.30104v1).

Table 1. Group composition of public images and private test images.

| Image group | Public images | Public proportion | Private test proportion |
| --- | ---: | ---: | ---: |
| POSCON | 48,574 | 51.0% | 36.2% |
| TARGET | 23,455 | 24.6% | 54.9% |
| REST | 23,186 | 24.4% | 8.9% |

The private test set contains 46,150 images by the sum of the original Table 1 (POSCON 16,691, TARGET 25,352, REST 4,107). REST has 4,107 images for 1,864 compounds, an average of 2.2 images per compound. The paper explicitly designs the difference in group composition between the public and private sets (label shift), and notes that TTA methods can degrade when covariate shift and label shift coincide ([1](#ref-1)). Zhao et al. likewise reported that the effectiveness of TTA varies greatly with the type of distribution shift and that existing methods systematically struggle with some shifts ([8](#ref-8)).

Aggregate accuracy is an image-count-weighted average of subgroup accuracies, not an equally weighted average over compounds. A mean over images is pulled toward majority classes and is a different quantity from a mean over classes (macro average) ([9](#ref-9)). POSCON and TARGET together exceed 90% of test images, so the aggregate is dominated by these two groups, as the paper also states ([1](#ref-1)). Eight compounds can have substantial influence if they contribute many images.

The public subgroup compound counts sum to 8 + 293 + 1,926, exceeding 2,000. Label-level inspection found 227 compounds in both TARGET and REST. Image rows belong to separate groups, but a compound can appear across groups. Treating them as three disjoint compound sets would misrepresent the aggregation.

For this check I used the 200-pixel CSV and the 500-pixel NPZ and label arrays. Image identifiers, sources, batches, plates, groups and labels matched in row order, with no duplicate image identifiers. I did not acquire image pixels or private test data ([5](#ref-5)).

## Decomposing the AdaBN gain {#adabn}

[Table 2 of the original paper](https://arxiv.org/html/2610.30104v1) reports means and sample standard deviations over three random seeds. The calculations below use the means, in percentage accuracy. The compared methods are ResNet18 without adaptation, deepCORAL ([10](#ref-10)), AdaBN ([6](#ref-6)), TENT ([11](#ref-11)), ARM-BN ([12](#ref-12)) and others, all built on ResNet18 ([1](#ref-1)). The table below shows five methods; DANN and CS-ARM-BN are included only in the distributed code. Uniform random selection among 2,000 classes has expected accuracy 1/2,000, or 0.05% ([1](#ref-1)).

Table 2. Mean accuracy reported in the original paper (%).

| Method | Overall | POSCON | TARGET | REST |
| --- | ---: | ---: | ---: | ---: |
| ResNet18 without adaptation | 17.5 | 46.5 | 1.2 | 0.2 |
| deepCORAL | 20.1 | 50.2 | 3.4 | 0.7 |
| AdaBN | 24.4 | 64.6 | 1.9 | 0.2 |
| TENT | 24.9 | 66.1 | 1.7 | 0.2 |
| ARM-BN | 26.0 | 66.5 | 3.5 | 0.4 |

Compared with no adaptation, AdaBN improves POSCON by 18.1 percentage points, TARGET by 0.7 points and REST by zero at the displayed precision. Multiplying these changes by private-test image proportions gives contributions of approximately 6.55, 0.38 and zero points. POSCON accounts for approximately 94.5% of the reconstructed gain. This is an accounting allocation of the aggregate difference, not an explanation of why POSCON images improved.

![Subgroup performance and contributions to the AdaBN gain](shared/batchbench-score-audit/figures/subgroups-and-gain.png)

Figure 1. Left: mean accuracies from [Table 2 of the original paper](https://arxiv.org/html/2610.30104v1). Distributed code includes all seven methods in that table. Right: AdaBN minus no adaptation, weighted by private-test image proportions. This descriptive calculation uses rounded means and does not test significance of the improvement.

This decomposition requires no model retraining. Weighted subgroup scores reproduced reported totals within less than 0.043 percentage points for all seven methods, consistent with rounding.

I also examined seed-to-seed variation. Using only the sample standard deviations and the three runs, and treating seeds as unpaired between methods, I attached rough 95% intervals to subgroup differences with Welch's method ([13](#ref-13)). The POSCON difference of 18.1 points has an interval of 9.4–26.8 points, wide because the standard deviation without adaptation is 3.6 points. The TARGET difference of 0.7 points spans −0.4 to 1.8 points, including zero. REST differed by 0.0 points. The overall difference of 6.9 points has an interval of 3.5–10.4 points. These are illustrative calculations assuming independent normally distributed runs. There are only three runs, standard deviations are rounded, and between-method pairing and covariance are unknown. These intervals establish neither that improvement is confined to POSCON nor that TARGET has no improvement.

Applying the same decomposition to the other methods shows that the source of improvement differs by method. The proportion of the improvement over no adaptation that comes from POSCON is approximately 52% for deepCORAL, 85% for ARM-BN, 94.5% for AdaBN and 96% for TENT. deepCORAL's overall gain is small, 2.6 points, but approximately 47% of it comes from a 2.2-point TARGET gain (interval about 1.0–3.4 points). ARM-BN also improved TARGET by 2.3 points. For TENT and AdaBN, the intervals include zero. Methods with similar overall scores did not improve the same image groups.

It would also be unwarranted to call AdaBN useless. The eight POSCON compounds have strong phenotypes and many training images. That their identification improved under batch effects is evidence that the adaptation has some effect. The issue is which improvement a number represents. The aggregate result alone does not establish improved performance for weak responses or compounds represented by few images. Because POSCON compounds are present on every plate, usually at fixed positions ([1](#ref-1)), this table also cannot distinguish whether higher POSCON accuracy reflects reading of morphology or image features tied to plate or position.

## Composition changes the ranking of methods {#_2}

I performed a further sensitivity calculation, fixing subgroup accuracies at published values while varying the positive-control image weight. The relative weights of TARGET and REST remained fixed at private-test proportions.

This is reweighting, not an experiment rerunning AI on a different data composition.

Excluding positive controls, accuracy weighted by TARGET and REST image counts is approximately 1.66% for AdaBN and 3.02% for deepCORAL. This reverses their order in the original aggregate score. Based on rounded values, their curves cross at a positive-control image proportion of approximately 8.6%. The same rough method gives the 1.4-point difference between these two methods an interval of 0.2–2.5 points, but this depends on the stated assumptions and does not establish that the ranking reversal exceeds seed variation. For reference, applying the public composition (POSCON 51.0%) gives aggregate values of approximately 24.1% without adaptation and approximately 33.5% for AdaBN.

![Sensitivity to aggregation weights and image composition by public source](shared/batchbench-score-audit/figures/mixture-and-sources.png)

Figure 2. Left: reweighting with subgroup accuracies fixed. The dashed line marks the private-test positive-control proportion. Right: public metadata aggregated by source; source 2 is validation. Sources differ in compound composition as well as imaging conditions.

The 8.6% value is not an operational threshold. A changed image composition can change adaptation statistics and thus subgroup accuracies themselves; this calculation holds them fixed. Seed-level predictions and their covariance were unavailable, so within-method subgroup standard deviations were combined assuming perfect positive correlation. This maximizes the weighted-sum variance for fixed marginal variances; it does not guarantee conservative coverage of the entire interval, including unknown between-method covariance and Welch degrees of freedom.

Three points follow for reading the original results. First, the ranking by aggregate accuracy depends on the composition of image groups used for evaluation. A ranking difference described as superiority needs to state the composition under which it holds. Second, about 86% of the 1.1-point aggregate difference between ARM-BN and TENT comes from TARGET, where the difference is 1.8 points (interval 0.7–2.9 points); the POSCON difference of 0.4 points (interval −2.1 to 2.9 points) has an approximate interval including zero. Reading a small aggregate difference as comparable improvement overlooks that different image groups improved. Third, identification of compounds with few images and weak phenotypes (TARGET and REST), which the paper names as the main open problem, is above chance level (0.05%) for all methods, but REST reaches at most 0.7%. The rounded three-run mean REST accuracy of 0.2% corresponds to an average of roughly 6–10 correct images per run out of 4,107, not an observed count for each run. Uniform random selection has an expectation of about 2; this is neither a comparison with a class-frequency baseline nor a significance test. A measurement system dominated by positive-control images and one comparing weak responses from sparsely imaged compounds should prioritize different scores.

## Does removing batch effects leave only biology? {#_3}

Batch correction is more than subtracting technical differences. If technical conditions are associated with compound composition, making sources harder to distinguish may also attenuate biological differences of interest. Conversely, good performance that retains source information need not transfer to the next experiment.

BatchBench combines cross-source evaluation, subgroup performance and unlabeled adaptation in a useful framework. RxRx1, which likewise targets generalization to unseen experimental batches, uses genetic perturbations and provides a classification task for evaluating batch-correction methods ([14](#ref-14)). BatchBench differs in targeting compounds and in providing subgroup scores and a private test set. I have not compared the results of the two directly, and I checked RxRx1 only at the level of its abstract.

BatchBench's score table cannot, however, separate how much performance loss reflects technical differences, weak phenotypes or limited image counts. Positive controls differ in training-image count, phenotype strength and plate arrangement. This reaggregation does not isolate those causal effects either.

Aggregate accuracy depends on the POSCON, TARGET and REST mixture. Macro accuracy, giving each compound equal weight, cannot be calculated from this table. A cross-source score difference cannot be treated as a single performance difference independent of drug composition.

## Conclusion {#conclusion}

Of the improvement in aggregate accuracy with AdaBN, from 17.5% to 24.4%, approximately 94.5% is accounted for by images of the eight positive-control compounds, which make up 36.2% of private-test images. The TARGET gain (293 compounds) was 0.7 points, with an assumption-dependent approximate interval including zero, and REST did not change at the displayed precision. Most aggregate improvement comes from the strong-phenotype controls. The aggregate score alone does not establish comparable improvement for weak responses and compounds with few images. This conclusion depends on rounded three-seed means and descriptive calculations with subgroup accuracies held fixed. It is not a re-evaluation of models on the private test set, so actual performance under a changed composition of image groups is not estimated.

## Data and code availability {#_4}

The [analysis code, aggregate inputs, results and figures](shared/batchbench-score-audit/batchbench-score-audit.zip) are provided. `analysis.py` and `plot.py` regenerate reweighting calculations and figures. `fetch_data.py` and `extract.py` retrieve public metadata at a fixed revision and recheck row alignment, source splits and overlapping compound groups. I did not execute the original model code.

The rough seed-to-seed intervals and per-method contribution proportions were computed with the [supplementary calculation script](shared/batchbench-score-audit/extra-score-checks.py), using `numpy` and `scipy`. Its only inputs are the means and sample standard deviations of Table 2. Run `python extra-score-checks.py`; it is provided separately from the original ZIP.

Scores are fixed to [Table 2 of preprint version 1](https://arxiv.org/html/2610.30104v1). When checked, the hosting Space's results JSON contained sample-format rows with example URLs that did not correspond to the paper's scores; I therefore did not cite it as a current measured leaderboard. The article reaggregates published results rather than reevaluating models on the private test set. Sources were checked on October 24, 2026; the supplementary calculations and a re-read of the full paper were done on October 29, 2026.

## References

1. <span id="ref-1"></span> Topf S, Sanchez-Fernandez A, Klambauer G. [BatchBench: Benchmarking AI Robustness to Batch Effects and Domain Shift in Biomedical Images](https://arxiv.org/abs/2610.30104v1). [Preprint]. arXiv; 2026. Version 1, arXiv:2610.30104v1, posted 2026 Oct 21; not peer-reviewed. [cited 2026 Oct 24].
2. <span id="ref-2"></span> Bray MA, Singh S, Han H, Davis CT, Borgeson B, Hartland C, et al. [Cell Painting, a high-content image-based assay for morphological profiling using multiplexed fluorescent dyes](https://doi.org/10.1038/nprot.2016.105). Nat Protoc. 2016;11(9):1757–74.
3. <span id="ref-3"></span> Chandrasekaran SN, Ackerman J, Alix E, Ando DM, Arevalo J, Bennion M, et al. [JUMP Cell Painting dataset: morphological impact of 136,000 chemical and genetic perturbations](https://doi.org/10.1101/2023.03.23.534023) [Preprint]. bioRxiv; 2023. Posted 2023 Mar 24; [bibliographic record checked only].
4. <span id="ref-4"></span> Arevalo J, Su E, Ewald JD, van Dijk R, Carpenter AE, Singh S. [Evaluating batch correction methods for image-based cell profiling](https://doi.org/10.1038/s41467-024-50613-5). Nat Commun. 2024;15(1):6516.
5. <span id="ref-5"></span> AI Lab JKU. [JUMP Cell Painting challenge datasets](https://huggingface.co/datasets/ai-lab-jku/jumpcp-challenge-datasets/tree/a5c2888d320f57e14d1c7d4dd4374397935ab9a4) [dataset]. Revision a5c2888d320f57e14d1c7d4dd4374397935ab9a4 [cited 2026 Oct 24].
6. <span id="ref-6"></span> Li Y, Wang N, Shi J, Hou X, Liu J. [Adaptive batch normalization for practical domain adaptation](https://doi.org/10.1016/j.patcog.2018.03.005). Pattern Recognit. 2018;80:109–17.
7. <span id="ref-7"></span> Machine Learning at JKU. [BatchBench baseline implementation](https://github.com/ml-jku/batchbench-baselines/tree/df18b76bbf6233a0a8bdb423801c5353e613078f) [software]. Commit df18b76bbf6233a0a8bdb423801c5353e613078f [cited 2026 Oct 24].
8. <span id="ref-8"></span> Zhao H, Liu Y, Alahi A, Lin T. [On pitfalls of test-time adaptation](https://proceedings.mlr.press/v202/zhao23d.html). Proc Mach Learn Res. 2023;202:42058–80.
9. <span id="ref-9"></span> Sokolova M, Lapalme G. [A systematic analysis of performance measures for classification tasks](https://doi.org/10.1016/j.ipm.2009.03.002). Inf Process Manag. 2009;45(4):427–37.
10. <span id="ref-10"></span> Sun B, Saenko K. [Deep CORAL: correlation alignment for deep domain adaptation](https://doi.org/10.1007/978-3-319-49409-8_35). In: Hua G, Jégou H, editors. Computer Vision – ECCV 2016 Workshops. Lecture Notes in Computer Science, vol 9915. Cham: Springer; 2016. p. 443–50.
11. <span id="ref-11"></span> Wang D, Shelhamer E, Liu S, Olshausen B, Darrell T. [Tent: fully test-time adaptation by entropy minimization](https://arxiv.org/abs/2006.10726) [Preprint]. arXiv; 2020. arXiv:2006.10726. Published in: International Conference on Learning Representations; 2021. [abstract checked only].
12. <span id="ref-12"></span> Zhang M, Marklund H, Dhawan N, Gupta A, Levine S, Finn C. [Adaptive risk minimization: learning to adapt to domain shift](https://proceedings.neurips.cc/paper/2021/hash/c705112d1ec18b97acac7e2d63973424-Abstract.html). Adv Neural Inf Process Syst. 2021;34:23664–78.
13. <span id="ref-13"></span> Welch BL. [The generalization of "Student's" problem when several different population variances are involved](https://doi.org/10.1093/biomet/34.1-2.28). Biometrika. 1947;34(1–2):28–35.
14. <span id="ref-14"></span> Sypetkowski M, Rezanejad M, Saberian S, Kraus O, Urbanik J, Taylor J, et al. [RxRx1: a dataset for evaluating experimental batch correction methods](https://doi.org/10.1109/CVPRW59228.2023.00451). In: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW). 2023. p. 4285–94.
