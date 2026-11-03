Reference date: the facts in this article are as of 3 November 2026.

The EMBER preprint, posted on 31 October 2026, presents a foundation model that learns context-dependent gene representations and reports improved cross-context perturbation-response prediction and genetic-interaction ranking relative to the baselines evaluated ([1](#ref-1)). Which baselines, on which metrics and by how much cannot be told from the abstract's "relative to evaluated baselines"; the main text and supplementary tables must be read. I read the full text of the preprint (the PDF), and from the means and standard deviations in Supplementary Tables S5 and S6, this note places the size of the gains against the baselines and against the variability across splits. No model was re-run. The preprint has not been peer reviewed. This note does not judge the usefulness of the model; it organizes the size of the reported numbers.

## Scope and sources

I read the main text, methods and Supplementary Tables S1–S7 of the preprint ([1](#ref-1)). Quoted numbers are from the text and supplementary tables. From the means and standard deviations in Supplementary Tables S5 (perturbation-response prediction, PDF pages 46–57) and S6 (genetic-interaction prediction, page 58), I transcribed into the companion archive (`inputs/`), only for the columns used, the rows for EMBER, its static-embedding ablation, STRING (GNN) (the interaction database STRING embedded by a graph neural network), the trivial baselines, and the "best external baseline" that I selected from all models in the table. The preprint is released under CC BY-NC-ND 4.0, and the transcription is limited to selected rows with the source stated. The text extracted from the PDF has breakage at page breaks, and I corrected the names of some rows. To check these corrections, a test confirms that EMBER's mean AUPRC matches the values in the text (0.425, 0.486 and 0.494). Drug-response prediction (Supplementary Table S7) and the narrowing of trigenic candidates are not covered here.

Terms: AUPRC is the area under the precision-recall curve and AUROC the area under the receiver operating characteristic curve. qGI is the quantitative genetic-interaction value, and EMBER-GI is EMBER's probe for genetic-interaction prediction. Context Mean is a trivial predictor of the mean response per cell line; Train Mean predicts from the training frequency of the readout gene alone, and its AUPRC is near the chance level (about 0.33 at a positive-to-negative ratio of 1 to 2).

## Discussion by issue

### Evaluation design and what the numbers mean

Perturbation-response prediction is a binary task: for a pair of a perturbed gene and a readout gene, predict whether the readout gene is differentially expressed. Negatives were readout genes from other perturbations with adjusted p above 0.1, two for each positive. Because the ratio of positives to negatives is 1 to 2, the AUPRC of a chance prediction is about 0.33, and Train Mean is near that level. The random embedding in the supplementary table (Random, Noise Floor) has an AUPRC of 0.354–0.377 for an unseen cell line with seen perturbations, so it is not the chance level (about 0.33 in the other two settings) (Supplementary Table S5). Results are reported as the mean and standard deviation over 10 random splits. The preprint itself states that these splits overlap, that the variation reflects split variability, and that it is not independent biological replication ([1](#ref-1)). It also states that the comparisons assess recovery of differentially expressed genes under the specified splits, not overall transcriptomic prediction accuracy. The control cells of a held-out cell line were used in pretraining and embedding extraction ([1](#ref-1)). Significance is shown by a paired t-test across splits against the best external baseline. Because the splits overlap, this note does not recompute p values; it gives the difference divided by the standard deviation across splits (d) as a descriptive measure. d is the size of the difference relative to split variability and does not express sampling uncertainty.

### Perturbation-response prediction: the gain is larger when crossing cell lines

In all three settings, EMBER's AUPRC exceeded the best external baseline that I selected (Table 1, Figure 1). The gain was large when crossing cell lines and small for unseen perturbations within the same cell line. For unseen perturbations in a seen cell line, EMBER's mean AUPRC was 0.494 and the best external baseline's was 0.482, a difference of 0.011 (0.006–0.017 by cell line); the best external baseline was mostly STRING (GNN). For an unseen cell line with seen perturbations it was 0.486 versus 0.443, a difference of 0.043 (0.030–0.058). For an unseen cell line and unseen perturbations it was 0.425 versus 0.386, a difference of 0.039 (0.028–0.055); the best external baseline in the last setting is a combination of the STRING (GNN) and scGPT embeddings.

Table 1. Perturbation-response prediction (Supplementary Table S5, test AUPRC, mean of four cell lines). Best external is the mean over cell lines of the highest-AUPRC external model I selected from the supplementary table for each cell line. d: the difference divided by the root mean square of the two models' standard deviations across splits (range over cell lines). Share: the proportion of EMBER's improvement over the anchor that is already captured by the best external baseline (mean). The anchor is Train Mean or, in the one setting that has it, Context Mean.

| Regime | EMBER | Best external | Difference (range) | d (range) | Share, anchor Train Mean | Share, anchor Context Mean |
| --- | ---: | ---: | --- | --- | ---: | ---: |
| Seen cell line, unseen perturbations | 0.494 | 0.482 | 0.011 (0.006 to 0.017) | 0.4 to 1.8 | 93% | not in table |
| Unseen cell line, seen perturbations | 0.486 | 0.443 | 0.043 (0.030 to 0.058) | 3.1 to 11.4 | 72% | 37% |
| Unseen cell line and perturbations | 0.425 | 0.386 | 0.039 (0.028 to 0.055) | 1.7 to 5.7 | 58% | not in table |

![Figure 1. Test AUPRC for perturbation-response prediction (mean ± standard deviation over 10 splits). For each setting and cell line: the random embedding (noise floor), STRING (GNN), the best external baseline selected from the supplementary table, and EMBER. From Supplementary Table S5.](shared/ember-effect-sizes-baselines/figures/01-perturbation-auprc.png)

The size of the difference can be seen on another scale. For unseen perturbations within a seen cell line, the best external baseline (mostly STRING (GNN)) already accounts for 93% of EMBER's improvement over Train Mean. When crossing cell lines, this share falls to 58–72%, and EMBER's added gain is relatively larger. The setting with an unseen cell line and seen perturbations has a row for the trivial predictor Context Mean. Its AUPRC was 0.397–0.432, comparable to many external models, and its difference from EMBER was 0.034–0.087 by cell line. With this anchor, the share captured by the best external baseline is 37%. The share moves greatly with the choice of anchor. The difference from EMBER's static-embedding ablation (without context) was, by cell line, 0.023–0.045 when crossing cell lines and −0.002 to 0.023 for unseen perturbations within a cell line, so the effect of context is not constant within a cell line and was slightly negative for K562.

### Genetic-interaction prediction: better ranking, nearly the same correlation of values

On the HAP1 genetic-interaction map (222 query genes and 17,724 library genes), evaluated on unseen library genes, EMBER-GI's AUPRC for detecting significant interactions was 0.181, against a chance level of 0.089 and 0.156 for STRING (GNN) (difference 0.025, d = 3.1) (Table 2, Figure 2). The AUROC was 0.602 versus 0.566. For the signed interaction value (qGI), the Pearson correlation was 0.072 for EMBER-GI and 0.071 for STRING (GNN), a difference of 0.001 (d = 0.1). The Spearman rank correlation was 0.050 versus 0.039 (d = 3.7). Ranking by AUPRC and AUROC improves, but the Pearson correlation does not differ, and the correlation values themselves are low for both. The AUROCs for negative and positive interactions separately were 0.545 and 0.568, computed against balanced, matched negatives, so 0.5 is the chance level ([1](#ref-1)). According to the methods, ranking is evaluated on residual predictions from which gene-wise mean effects have been removed. The preprint does not say whether Pearson and Spearman were computed on the same residual predictions, so whether the ranking metrics and the correlation metrics can be compared on the same footing could not be confirmed.

Table 2. Genetic-interaction prediction on the HAP1 map (Supplementary Table S6, mean ± standard deviation over 10 splits). STRING (GNN) is the best external baseline for AUPRC and Pearson; for AUROC the best is Geneformer-V2 104M (0.581, 0.021 below EMBER-GI) and for Spearman it is TranscriptFormer (0.044, 0.006 below).

| Metric | EMBER-GI | STRING (GNN) | Difference | d |
| --- | --- | --- | ---: | ---: |
| AUPRC, any interaction (chance 0.089) | 0.181 ± 0.008 | 0.156 ± 0.008 | 0.025 | 3.1 |
| AUROC, any interaction | 0.602 ± 0.010 | 0.566 ± 0.008 | 0.036 | 4.0 |
| Pearson r, signed qGI | 0.072 ± 0.007 | 0.071 ± 0.008 | 0.001 | 0.1 |
| Spearman rho, signed qGI | 0.050 ± 0.003 | 0.039 ± 0.003 | 0.011 | 3.7 |

![Figure 2. Genetic-interaction prediction metrics for EMBER-GI and STRING (GNN) (bars: mean; error bars: standard deviation over 10 splits). From Supplementary Table S6.](shared/ember-effect-sizes-baselines/figures/02-genetic-interaction-metrics.png)

### A hypothesis: dependence on SCFD1

From EMBER-GI's predicted interactions with MTOR, the preprint nominates SCFD1 as a candidate dependency during mTOR inhibition. Among the predicted MTOR interaction partners after excluding known synthetic-lethal pairs, SCFD1 ranked 14th. In a retrospective check of two published CRISPR screens, SCFD1-targeted cells were more depleted under Torin1 than under vehicle. In human HAP1 cells the log2 fold change was −3.69 versus −2.21 (p = 0.062), not significant; in mouse EPP2 cells it was −1.89 versus −1.47 (p = 0.0046). On a different measure, among all predictions the SCFD1–MTOR pair was in the top 0.81% for EMBER, 1.90% for STRING (GNN) and 12.2% for the static embedding (a different scale from the rank of 14th) ([1](#ref-1)). This is a recheck of published screens, not a new experiment, and one of the two was not significant. The p values are nominal, and a single gene was examined. The preprint itself positions the result as supporting the prioritization of experiments.

## Overall assessment

The preprint's claim (improvement over the baselines evaluated) is supported, as far as the supplementary tables allow it to be checked. The size of the improvement, however, differs greatly by setting. When crossing cell lines it is 0.03–0.06 in AUPRC, several times the standard deviation across splits. For unseen perturbations within a cell line, the improvement is small (0.006–0.017), and the best external baseline accounts for more than 90% of the improvement over Train Mean. In genetic interactions, the AUPRC for ranking is about twice chance, and the Pearson correlation is as low as that of the comparator. How these differences bear on prioritizing experiments cannot be told from this analysis.

## Limitations

- The analysis is arithmetic on the supplementary tables' means and standard deviations, not a re-run of models. Because the splits overlap, d is a descriptive measure, not an inferential statistic.
- The "best external baseline" is the one with the highest test AUPRC among all models in the supplementary table, selected by me for each cell line. Selecting a maximum among many tends to make the differences smaller and the shares larger. The selected model differs by cell line, and there may be cell lines where it does not coincide with the "best external baseline" in the paper's text.
- The numbers were transcribed from text extracted from the PDF, and I corrected the names of some rows. EMBER's means were confirmed to match the text, but transcription errors in other rows were not checked for every row.
- AUPRC depends on the positive-to-negative ratio (1 to 2). Values cannot be compared with other studies. The control cells of held-out cell lines were used in pretraining, so the evaluation is not fully free of information about the target cell line.
- Drug-response prediction, the narrowing of trigenic candidates and the preprint's biological interpretation are not covered.
- The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

According to the supplementary tables, EMBER showed higher AUPRC than the external baselines: 0.03–0.06 higher when crossing cell lines and only 0.006–0.017 higher for unseen perturbations within a cell line. For genetic interactions, the AUPRC for ranking was 0.025 higher than STRING (GNN), while the Pearson correlation of the signed values was at the same level (0.072 versus 0.071). The abstract's "relative to evaluated baselines" should be read at this size, setting by setting and metric by metric.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`), the selected rows transcribed from Supplementary Tables S5 and S6 (`inputs/`; the preprint is under CC BY-NC-ND 4.0 and its source is reference 1) and result tables are in the companion archive. Run with Python 3.12, NumPy 2.2, pandas 2.2 and Matplotlib 3.9: `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The calculation is arithmetic on the reported means and standard deviations and uses no random numbers.

The full re-run materials are in the [companion archive](shared/ember-effect-sizes-baselines/ember-effect-sizes-baselines-companion.zip).


## References

<span id="ref-1"></span>1. Ho N, Xing EP, Ma J. EMBER: contextualized gene representations enable compositional prediction across cellular perturbations [Preprint, version 1]. bioRxiv. 2026 Oct 31 [cited 2026 Nov 3]. [doi:10.64898/2026.10.28.762655](https://doi.org/10.64898/2026.10.28.762655). Not peer reviewed. Full text and supplementary tables read.
