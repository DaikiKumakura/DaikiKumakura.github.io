## Abstract {#article-abstract}

Six hundred public scores for MAP, a predictor of transcriptional responses to unprofiled drugs, were reaggregated while distinguishing withheld information from available inputs. Mean scores exceeded the selected comparator for all 16 drugs, but only 12 had positive correlation differences in all five evaluations. One of 96 reported means differed beyond what simple rounding readily explains. This descriptive audit of a fixed test set does not validate generalization to unseen structural or mechanistic classes, or improvement in drug efficacy.

## Introduction {#article-introduction}

Which genes change when a new compound is added to cells? Predictions for compounds without RNA measurements could help narrow experimental candidates. But an unseen drug name does not necessarily mean an unseen structure or mechanism.

MAP, published in August 2026, incorporates drug and gene knowledge into representations for predicting transcriptional responses [original paper](https://www.nature.com/articles/s42256-026-01286-w) ([1](#ref-1)).

This article distinguishes information withheld from information still available. Here I recalculate public Source Data for 16 drugs, six methods and five evaluations. I did not train or run the models. Recalculated results are distinguished from untested applications. Sources were checked on 2026-10-12.

## Scope and sources {#article-scope}

### Pretraining and prediction-time inputs {#_1}

A model representing drugs only as identifiers cannot interpret a new identifier. Molecular structure provides a way to use similarities to training compounds. MAP's knowledge learning connects structures, protein sequences and descriptive text, then uses the resulting representation for response prediction.

Pretraining information is different from prediction-time input. The [official demo I inspected](https://github.com/MAGIC-AI4Med/MAP/blob/629ebdc1617eaf89825185a1512d772eccc3dc7e/MAP/demo.py) ([2](#ref-2)) passes control-cell inputs, a compound's SMILES and concentration to the predictor. I did not execute it, but the code establishes an interface different from looking up a known drug identifier.

Two possible routes to an unmeasured compound's response remain distinct: resemblance to responses of structurally similar known compounds, and relationships learned through knowledge that structure alone may not capture. Both may operate. Better performance after adding knowledge does not by itself establish discovery of a new mechanism.

### Information excluded during evaluation {#_2}

The paper evaluates both unseen drug–cell combinations and drugs whose transcriptional responses are excluded entirely from training. For the latter, it also states that test drugs, synonyms and related edges are removed from knowledge learning. The calculations below concern that setting [evaluation design](https://www.nature.com/articles/s42256-026-01286-w#Sec4) ([1](#ref-1)).

**Table 1　Withheld information and evaluation targets**

| Information held out | Information still available | Question addressed |
| --- | --- | --- |
| Drug–cell combination | The same drug's measured responses in other cells | Transfer across cell backgrounds |
| The drug's transcriptional responses | Structure, learned representation and other drugs' responses | Prediction for an unprofiled drug |
| Structural series | Distant structures and known targets/pathways | Prediction less dependent on close analogues |
| Mechanism-of-action group | Structure and drugs with other mechanisms | Prediction beyond known mechanism groups |

The last two rows of Table 1 are additional evaluations proposed here. MAP's drug holdout does not automatically hold out structural series or mechanisms. A different identifier can still have a close analogue in training.

That is not inherently leakage. Knowledge of analogues is legitimate when improving a chemical series. Extending results from analogues to new structures or mechanisms requires evaluation in that intended scope.

I also inspected the official knowledge-data loader, but did not reproduce the pairing of split knowledge graphs and checkpoints. A stated exclusion in a paper is different from verifying that exclusion in a particular executable artifact.

## Reaggregation methods and results {#article-results}

### Drug-level differences and variation across evaluations {#16}

I used the `Fig_3c` sheet in the [Source Data](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42256-026-01286-w/MediaObjects/42256_2026_1286_MOESM4_ESM.xlsx) ([3](#ref-3)). This evaluates unprofiled drugs in six Tahoe-100M cancer cell lines using pseudobulk scores. It does not evaluate individual cell fates or every cell type. For each drug, MAP, CRISP, ChemCPA, PRnet, trainMean and XPert have Pearson delta correlations for the top 50 differentially expressed genes. Differential expression is the drug–control change; delta correlation measures agreement between predicted and observed gene-wise changes. This expression delta differs from the between-method correlation difference calculated below.

For each of all 16 drugs, I selected the comparator with the highest published mean, held it fixed and subtracted its score from MAP's in each of five evaluations. Selection used the evaluation outcomes, so this is a descriptive comparison of published results, not a model-selection procedure available for an unknown candidate.

\[
d_{j,e}=r_{\mathrm{MAP},j,e}-r_{\mathrm{comparison},j,e}.
\]

Here \(j\) denotes drug and \(e\) evaluation. Plot points are mean \(d\) calculated from the five published rounded values.

![Correlation differences between MAP and the selected comparators for 16 drugs](shared/map-unprofiled-drugs/figures/01-drug-advantages.png)

**Figure 1.** Original recalculation showing all 16 drugs. Lines span the minimum and maximum of five differences, not confidence intervals. Comparators differ between drugs but are fixed across a drug's five evaluations; they are recorded in `results/drug-comparisons.csv`.

MAP exceeds the comparator in the published mean for all 16 drugs. Recomputing the means from the five rounded values preserves that conclusion. Figure 1 and Table 2 show that only 12 drugs, however, have a positive difference in every evaluation.

**Table 2　Drugs with correlation differences changing sign across evaluations**

| Drug | Comparator | Mean correlation difference | Minimum–maximum | Evaluations with positive difference |
| --- | --- | ---: | ---: | ---: |
| Bergenin | XPert | 0.0084 | −0.058–0.072 | 3/5 |
| Balsalazide | CRISP | 0.0176 | −0.012–0.050 | 3/5 |
| Nafamostat | XPert | 0.0516 | −0.072–0.134 | 4/5 |
| Ralimetinib dimesylate | XPert | 0.0620 | −0.032–0.120 | 4/5 |

This does not negate the mean advantage. Its magnitude varies by candidate, and small differences can change sign between evaluations. One overall mean does not imply a uniform improvement for every compound.

The five evaluations use the same fixed test set. Differences were paired by the evaluation indices in the table, but the scores alone do not verify what was randomized, or whether methods shared seeds or sampled cells. These are not five additional patients or independent experimental systems. They cannot estimate success across all unknown drugs or biological uncertainty. The differences are correlation units, not percentage improvements in drug efficacy.

### Agreement with published means {#_3}

I checked all 96 published means (16 drugs × six methods) against the corresponding five values. MAP's published mean for drospirenone is 0.941, whereas their mean is 0.9346. The 0.0064 difference is difficult to explain by rounding both values to three decimal places alone.

I did not replace the published value as an established error. The available scores do not determine whether another aggregation procedure or a reporting issue explains it. Both values remain in the distributed CSV. The comparator difference stays positive: 0.059 using published means and 0.0528 after recalculation.

Input and aggregation consistency matter when tiny score differences are used to choose candidates. This discrepancy does not change the mean advantage across all 16 drugs; more decimal places do not make a comparison more certain.

### Comparisons across knowledge-learning conditions {#_4}

I also read unprofiled-drug correlations in the [Fig_5a Source Data sheet](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42256-026-01286-w/MediaObjects/42256_2026_1286_MOESM4_ESM.xlsx) ([3](#ref-3)). PrimeKG is an existing biomedical knowledge graph; MAP-KG integrates drugs, genes and their relationships for this study. Published means are 0.321 with random initialization, 0.734 after adding MoleculeSTM, 0.747 with PrimeKG and 0.822 with MAP-KG.

![Knowledge-learning stages and unprofiled-drug correlations](shared/map-unprofiled-drugs/figures/02-knowledge-stages.png)

**Figure 2.** Original plot of four public conditions. Successive correlation differences are 0.413, 0.013 and 0.075. They are correlation units, not causal fractions attributable to knowledge.

The large first difference includes the introduction of molecule–text pretraining. Later differences also change learning content and amount. The 0.413 cannot be assigned to structure alone and the 0.075 to target mechanisms alone.

I read this as evidence that prediction changes when information and pretraining conditions change. Which relationship improves which drug remains a question for information-matched controls and per-drug evaluation. A prediction consistent with mechanisms differs from identifying a mechanism from predictions.

## Discussion {#_5}

Doubling every true change still gives Pearson correlation one when the changes are nonconstant. A correlation advantage does not establish correct ranking of drug-induced change magnitudes.

The top 50 genes selected from measured responses can diagnose recovery of changed genes, but are unknown when predicting an unprofiled drug [gene-selection procedure](https://www.nature.com/articles/s42256-026-01286-w#Sec44) ([1](#ref-1)).

These Source Data are score tables. I did not recompute errors on a common gene set, drug discrimination or performance by structural distance. The mean advantage for 16 drugs is supported; the structural distances over which it persists are unresolved by this table.

## Conclusion {#article-conclusion}

The public scores support a mean advantage across 16 drugs, while individual evaluation differences and aggregation consistency require separate checks. Drug holdout does not imply structural-series or mechanism holdout. Better prediction after adding knowledge alone does not establish mechanism discovery or improved drug efficacy.

## Data and code availability {#_6}

[Input CSV, recalculation code, figures and results](shared/map-unprofiled-drugs/map-unprofiled-drugs.zip) are available. `python analysis.py` uses only the standard library; figure regeneration uses matplotlib. The inputs are 600 public scores with source-sheet and cell locations retained.

This is descriptive score recalculation and static reading of official code. It does not execute the model, reproduce evaluation from cell-level data, add independent test drugs or estimate clinical effects.

Sources are the [MAP paper](https://www.nature.com/articles/s42256-026-01286-w) ([1](#ref-1)), [supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42256-026-01286-w/MediaObjects/42256_2026_1286_MOESM1_ESM.pdf) ([4](#ref-4)) and [official code](https://github.com/MAGIC-AI4Med/MAP) ([2](#ref-2)), checked at `629ebdc`. The package excludes the original paper, figures, Source Data workbook, official code and model weights.

## References {#article-references}

1. <span id="ref-1"></span>Feng J, Zhao Z, Zhang X, Liu M, Chen J, Quan X, et al. A knowledge-driven framework for predicting single-cell responses for unprofiled drugs. Nature Machine Intelligence. 2026;8(9):1478–1491. [doi:10.1038/s42256-026-01286-w](https://doi.org/10.1038/s42256-026-01286-w).
2. <span id="ref-2"></span>MAP developers. MAP: official implementation [Software; cited 2026 Oct 12]. Commit 629ebdc1617eaf89825185a1512d772eccc3dc7e. [Fixed repository](https://github.com/MAGIC-AI4Med/MAP/tree/629ebdc1617eaf89825185a1512d772eccc3dc7e).
3. <span id="ref-3"></span>Feng J, Zhao Z, Zhang X, Liu M, Chen J, Quan X, et al. Source Data for: A knowledge-driven framework for predicting single-cell responses for unprofiled drugs [Dataset]. 2026. Sheets Fig_3c and Fig_5a. [Workbook](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42256-026-01286-w/MediaObjects/42256_2026_1286_MOESM4_ESM.xlsx).
4. <span id="ref-4"></span>Feng J, Zhao Z, Zhang X, Liu M, Chen J, Quan X, et al. Supplementary Information for: A knowledge-driven framework for predicting single-cell responses for unprofiled drugs. 2026. [Supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42256-026-01286-w/MediaObjects/42256_2026_1286_MOESM1_ESM.pdf).
