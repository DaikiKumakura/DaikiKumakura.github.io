Arc Institute's Virtual Cell Challenge 2026 (VCC) is a competition to predict how cells respond to genetic perturbations. The deadline for the final evaluation, on three cell lines the models have never seen, was November 5, 2026, and results were expected in mid-to-late November ([1](#ref-1)). The facts in this article are as of October 30, 2026. By the time it is published, the deadline and the announcement may both have passed; the final results are not reflected.

The challenge is described on the organizer's page ([1](#ref-1)). One participant published code and a retrospective on GitHub ([2](#ref-2)). In that record, the validation score was 0.164, the top ten were near 0.32 and the leader was at 0.47. The retrospective reports the following ([2](#ref-2)).

- On 168 training targets, alignment between predicted and real effects (mean cosine similarity) was 0.084.
- Two halves of the same real cells agreed at 0.65.
- On the same targets, the discrimination score was 0.86.

The retrospective's point is that knockdowns (suppression of gene expression) could be told apart, but the direction of their effects could not be stated ([2](#ref-2)). Can this combination of high discrimination and low alignment arise as a property of the metrics? This article counts how discrimination and alignment relate in public data.

What is checked is whether numbers in the same region can arise in public data. It is neither a reproduction of the VCC scoring nor a reproduction of the participant's numbers (0.084, 0.86). The closeness of that region says nothing about the quality of the participant's predictions. The analysis plan was not fixed before computing: the curve over the number of cells used for the replicate prediction and the comparison of exclusion rules were added after seeing results (post hoc; exploratory analysis).

## Abstract

On 102 perturbations from a public dataset by Norman et al., I computed discrimination (PDS, the rank of the correct perturbation) and alignment (cosine similarity between predicted and real effects) for predictions built from real cells of the same perturbation. A prediction made from the average of just one real cell had alignment 0.11 and discrimination 0.83. With two cells it was 0.16 and 0.89. This is a region near the participant's report (alignment 0.084, discrimination 0.86). Conversely, a prediction returning the average effect of the other perturbations had alignment 0.50 and discrimination 0.49. A content-poor prediction that moved only the target gene itself had discrimination 0.98 without gene exclusion and 0.50 under cell-eval2's default rule (`vcc2026`). High discrimination does not imply high alignment, and high alignment does not imply that perturbations can be told apart. Discrimination also depends on the evaluation rule.

## Methods

### Metric definitions

- **Effect:** the mean expression of perturbed cells minus the mean expression of control cells, per gene.
- **Discrimination (PDS):** for each perturbation, the rank of the correct reference among all perturbations' real effects when ordered by closeness to the predicted effect. A value of 1 means closest and 0.5 means no discrimination. Distance is cosine distance, and rank is converted as 1 − (rank ÷ (number of perturbations − 1)). Ties receive the mid-rank.
- **Alignment:** cosine similarity between the predicted and real effects. A value of 1 is the same direction, and 0 is unrelated.
- **Target-gene exclusion:** cell-eval2 is a reimplementation of Arc Institute's cell-eval ([3](#ref-3)). The bundled AUTHORS file indicates that the maintainer is affiliated with Arc Institute. I have not confirmed agreement with the official VCC scoring. In cell-eval2's `vcc2026` preset, all target genes of the panel are removed from the evaluated genes (panel), so that target-gene changes alone cannot give discrimination. The older rule (row) removes only the perturbation's own target ([3](#ref-3)). I also computed the case without exclusion.

### Data

I used the public dataset of Norman et al. ([4](#ref-4)) as harmonized in scPerturb ([5](#ref-5), [6](#ref-6)) (CC BY 4.0). It is a K562 gene-activation (CRISPR activation, CRISPRa) experiment. Of the single perturbations with at least 60 cells, 102 whose target gene is present in the expression matrix were used (3 of 105 single perturbations with at least 60 cells were excluded because their target gene is absent; `prepare.log`). Expression per cell was scaled to a total of 10,000 and log1p-transformed. Genes detected in at least 5% of all cells, plus the target genes, gave 9,601 genes. This gene selection used all cells before the split into two halves.

### Construction of real effects and predictions

- Cells of each perturbation were randomly split into two halves (seed 20261030). One half (mean 276 cells) is treated as the “real” effect; predictions are built from the other half. Pseudobulk here means a single profile obtained by averaging cells.
- The predictions are:
  - the average of k cells of the same perturbation (k = 1–60, and the entire half);
  - the average effect of the other perturbations (excluding the perturbation itself);
  - a vector moving only the target gene itself;
  - a content-free vector moving every target gene regardless of perturbation (−1, the reverse direction, because the experiment is activation).
- Discrimination and alignment were computed under three exclusion rules (none, row, panel). Under panel, 9,499 genes are evaluated. The 95% intervals come from 2,000 bootstrap resamplings of perturbations. They reflect sampling variation of perturbations only. Because discrimination ranks depend on comparisons among perturbations, the intervals may be narrower than the true uncertainty.

The data are 102 CRISPRa perturbations, whereas the VCC evaluates CRISPR interference (CRISPRi, suppression) knockdowns in three cell lines, and normalization differs. What is tested here is the behavior of the metrics, not a VCC score.

### Implementation checks

- The same author reimplemented in R the discrimination (three exclusion rules) and alignment and recomputed them on a public subset (102 perturbations × 1,502 genes). The definitions are the same, so this is not third-party confirmation. Across nine combinations (three predictions × three rules), the maximum difference in discrimination and alignment was 5.0 × 10⁻⁷, below 1 × 10⁻⁴ (`results/validation.json`). The re-implementation covers only three predictions: replicate, average of the others and target only. The cell-count curve, content-free prediction, bootstrap and cross-perturbation cosines were not recomputed in R.
- Six unit tests passed (a perfect prediction gives 1; all-tied ranks give 0.5; target-gene exclusion gives 0.5 for the target-only prediction; mid-rank handling of ties; and others) (`test_analysis.py`).
- Re-running with the same seed reproduces the result files. Inputs are pinned by SHA-256.

## Results

### Discrimination becomes high while alignment is still low

Table 1 shows alignment and discrimination for predictions made by averaging k real cells of the same perturbation. It corresponds to the blue line in Figure 1.

Table 1. Number of cells used for the prediction, alignment and discrimination (panel rule, 102 perturbations, 95% bootstrap intervals).

| Cells per prediction | Alignment (95% interval) | Discrimination (95% interval) | Cosine with wrong candidates (mean) |
| ---: | ---: | ---: | ---: |
| 1 | 0.11 (0.09–0.13) | 0.83 (0.77–0.88) | 0.03 |
| 2 | 0.16 (0.14–0.18) | 0.89 (0.84–0.93) | 0.05 |
| 3 | 0.19 (0.16–0.22) | 0.91 (0.87–0.94) | 0.06 |
| 5 | 0.24 (0.22–0.27) | 0.93 (0.90–0.96) | 0.08 |
| 10 | 0.33 (0.29–0.36) | 0.96 (0.93–0.98) | 0.11 |
| 60 | 0.59 (0.55–0.63) | 0.97 (0.95–0.99) | 0.21 |
| about 276 (the entire half) | 0.74 (0.70–0.77) | 0.98 (0.96–0.99) | 0.25 |

Source: `results/replicate-curve.csv`; the row for about 276 is from `results/predictions-summary.csv`. “Cosine with wrong candidates” is the mean cosine between a prediction and the real effects of the other perturbations.

![Scatter plot of discrimination against alignment. Predictions using more cells move to the right while discrimination levels off near 0.98.](shared/vcc2026-discrimination-alignment/figures/01-pds-vs-alignment.png)

Figure 1. Discrimination (vertical) against alignment (horizontal). The blue line is predictions averaging k real cells; the orange point is the average of the other perturbations; red squares are the target-gene-only prediction (filled: no exclusion; open: panel rule); the green star is the participant's report (different data; not comparable). The dotted line is discrimination 0.5. 102 perturbations from Norman 2019 (CRISPRa, K562). The sample size for each point on the blue line is n = 102 perturbations; intervals are in Table 1. The points are built from the same cell split and are not independent.

Discrimination approaches its upper limit faster than alignment. As Table 1 shows, while alignment moves from 0.11 to 0.74, discrimination moves only from 0.83 to 0.98. A prediction with alignment 0.16 and one with alignment 0.74 look like a difference of only 0.89 versus 0.98 in discrimination.

The following explanation seems likely. In a space of about 9,500 genes, cosines between unrelated directions cluster near 0 (the theoretical standard deviation is 1/√9,499 ≈ 0.0103; `results/summary.json`). A one-cell prediction is noisy, with a cosine of only 0.11 to the correct effect. But its cosine to wrong candidates is smaller still, 0.03 on average. The rank depends only on whether the cosine to the correct effect exceeds that to the wrong ones, not on how large the margin is.

The participant's report (alignment 0.084, discrimination 0.86, agreement between real halves 0.65) lies in a region near the one-cell prediction in this dataset (alignment 0.11, discrimination 0.83). The data and definitions differ, however. This closeness shows only that low alignment and high discrimination can coexist as a property of the metrics; it does not show that the predictions were noisy.

### A prediction can have high alignment and chance-level discrimination

A prediction returning the average effect of the other perturbations (excluding the perturbation itself) had alignment 0.50 (0.44–0.56) and discrimination 0.49 (0.44–0.55) (panel rule; `results/predictions-summary.csv`).

Real effects of different perturbations share a common component. The cosine between real effects of different perturbations has a median of 0.31 (5th–95th percentile range −0.29 to 0.64; `results/summary.json`). The average effect captures this shared component, so alignment is high. But it returns the same prediction for every perturbation and therefore cannot tell them apart. Predicting only a shared response, such as a stress response, can produce high alignment.

### Discrimination depends on the evaluation rule

Table 2 shows discrimination for three predictions under the three exclusion rules. It corresponds to Figure 2.

Table 2. Discrimination by exclusion rule (95% bootstrap intervals, 102 perturbations).

| Prediction | No exclusion | row (only the perturbation's own target excluded) | panel (all targets excluded; cell-eval2 default) |
| --- | ---: | ---: | ---: |
| Moves only the target gene itself | 0.98 (0.96–0.99) | 0.50 (0.50–0.50) | 0.50 (0.50–0.50) |
| Content-free prediction moving the other target genes uniformly | 0.50 (0.44–0.55) | 0.67 (0.63–0.72) | 0.50 (0.50–0.50) |
| Average effect of the other perturbations | 0.49 (0.43–0.54) | 0.50 (0.44–0.55) | 0.49 (0.44–0.55) |

Source: `results/predictions-summary.csv`. An interval of zero width arises because the prediction gives a constant rank across all perturbations.

![Bar chart of discrimination for three predictions under three exclusion rules.](shared/vcc2026-discrimination-alignment/figures/02-exclusion-scope.png)

Figure 2. Discrimination under different exclusion rules: no exclusion (red), row (orange) and panel (blue). Error bars are 95% bootstrap intervals; the dotted line is discrimination 0.5. The horizontal axis shows the type of prediction and the vertical axis shows PDS. n = 102 perturbations.

Without target-gene exclusion, the target-only prediction is almost perfectly discriminating (0.98), because only the perturbation's own target gene changes strongly. Alignment measured on non-target genes is 0. Under cell-eval2's default rule (panel), discrimination is 0.50.

For the content-free prediction, an explanation inside the cell-eval2 source states that, under the older row rule, a content-free submission that merely moved the other target genes obtained discrimination of 0.76–0.80 on the VCC's three validation cell contexts, against baselines of 0.51–0.53. That measurement was made with cell-eval2 0.14.0 and is not reproduced here. I confirmed this statement from the explanatory text in the bundled `cell_eval2/metrics/discrimination.py` ([3](#ref-3)). It is the library's own description, and agreement with the official VCC scoring is unconfirmed. In this dataset, the same form of prediction scored 0.67 under row and 0.50 under panel. Under panel, this loophole is closed.

## Discussion

When reading final scores, discrimination alone makes differences in prediction quality hard to see. In this dataset, predictions with alignment in the 0.1 range reached discrimination of 0.8–0.9. That differences among top entries might appear in metrics other than discrimination is an unverified inference from how quickly discrimination approaches its limit here. The final VCC ranking is said to rest on an aggregate of six metrics ([1](#ref-1)). This article treats only discrimination.

Placing a metric close to alignment, the reproducibility ceiling of the real data and a shared-response baseline next to discrimination makes its value easier to interpret.

- **A metric close to alignment:** how well the direction of the predicted effect matches the real one.
- **Reproducibility ceiling of the real data:** the agreement between two halves of the same cells. It was 0.65 in the participant's report ([2](#ref-2)) and 0.74 here. Definitions and data differ, so comparison needs care.
- **Shared-response baseline:** the “average of the other perturbations” reaches alignment 0.50. An alignment that does not exceed this may contain no perturbation-specific information. This prediction, however, was built from the real averages of other perturbations in the same dataset. I did not check whether it can be built under the same conditions from the VCC training data.

Availability of in-context data also matters. In the participant's report, using data on other knockdowns measured in the same cell type raised alignment from 0.115 to 0.42. Holding out an entire cell type left it at 0.115 to 0.118 ([2](#ref-2)). In the final evaluation, perturbation responses measured in the cell lines are not given to participants ([1](#ref-1)).

## Limitations

- **Data differences:** The data here are 102 CRISPRa perturbations in one cell line, using pseudobulk averages. The VCC uses three new CRISPRi cell lines with different normalization. How fast discrimination approaches its limit depends on how well separated the perturbation set is. The relationships found here cannot simply be carried over to VCC data.
- **Participant's numbers:** The participant's numbers are the participant's own report and were not reproduced here. I make no judgment about the participant or about the merits of any particular submission.
- **Official score:** The final VCC score combines six metrics ([1](#ref-1)). This article treats discrimination only. Agreement between cell-eval2 and the official VCC scoring has not been confirmed.
- **Other definitions of discrimination:** L1 or L2 distances and cell-level discrimination were not tested.
- **Intervals:** The 95% intervals reflect only sampling variation from resampling perturbations. They do not include uncertainty from data acquisition or differences among cell lines. The intervals for discrimination and alignment differ slightly across exclusion rules because of the order in which random numbers are consumed (the alignment point estimate is the same under all rules). Table 1 shows the panel-rule rows for both discrimination and alignment.
- **Control mean:** Because the control mean is subtracted from both predictions and real effects, shared noise may raise cosines slightly. This effect was not evaluated.
- **Plan:** The analysis plan was not fixed before computing. The cell-count curve and the comparison of exclusion rules are post hoc and exploratory.

## Conclusion

The combination of discrimination 0.86 and alignment 0.08 can arise as a property of the metrics. In public data, a prediction from just one real cell gave numbers in the same region. Discrimination approaches its upper limit before alignment does, so differences in alignment are hard to see in discrimination, and this relation also depends on the target-gene exclusion rule. The results are for 102 CRISPRa perturbations and do not indicate the quality of the participant's predictions or any VCC score.

## Data and code availability

The re-run materials (`acquire.py`, `prepare.py`, `analysis.py`, `figures.py`, `validate.R`, `test_analysis.py`, `results/`, `figures/`, `validation-data/`, `input-provenance.json`) are included in the distribution package. The input h5ad file (about 700 MB) is not bundled; it is retrieved with `acquire.py` and checked by SHA-256. Re-run: `python acquire.py && python prepare.py && python test_analysis.py && python analysis.py && python figures.py && Rscript validate.R` (Python 3.12, anndata, numpy, pandas, matplotlib, requests; R 4.5.3, jsonlite). Random numbers are fixed with seed 20261030. `validate.R` runs using only the bundled `validation-data/`.

The participant's numbers are quoted from commit 2fc9097 of the repository in reference 2 (`RETRO.md`). The cell-eval2 0.20.0 wheel was used read-only and was not executed (its SHA-256 is recorded in `input-provenance.json`).

The full re-run materials are in the [companion archive](shared/vcc2026-discrimination-alignment/vcc2026-discrimination-alignment-companion.zip).


## References

<span id="ref-1"></span>1. Arc Institute. The 2026 Virtual Cell Challenge: predicting perturbation responses in cell contexts a model has never seen [Internet]. Arc Institute; 2026 Aug 20 [cited 2026 Oct 31]. Available from: https://arcinstitute.org/news/virtual-cell-challenge-2026

<span id="ref-2"></span>2. Pinho R. VCC 2026: public perturbation prediction pipeline [Software]. GitHub; 2026. Commit 2fc9097 (2026 Oct 29); RETRO.md and README.md. Available from: https://github.com/rpinho/virtual-cell-challenge/blob/2fc9097716b94bc4c02de3aa4c5d9bbe06b94749/RETRO.md

<span id="ref-3"></span>3. cell-eval2 contributors (maintainer: Dobin A). cell-eval2 [Software]. PyPI; 2026. Version 0.20.0 (released 2026 Oct 23) [cited 2026 Oct 31]. Wheel contents examined: AUTHORS, cell_eval2/metrics/discrimination.py. Available from: https://pypi.org/project/cell-eval2/

<span id="ref-4"></span>4. Norman TM, Horlbeck MA, Replogle JM, Ge AY, Xu A, Jost M, et al. Exploring genetic interaction manifolds constructed from rich single-cell phenotypes. Science. 2019;365(6455):786–793. [doi:10.1126/science.aax4438](https://doi.org/10.1126/science.aax4438).

<span id="ref-5"></span>5. Peidli S, Green TD, Shen C, Gross T, Min J, Garda S, et al. scPerturb: harmonized single-cell perturbation data. Nat Methods. 2024;21(3):531–540. [doi:10.1038/s41592-023-02144-y](https://doi.org/10.1038/s41592-023-02144-y).

<span id="ref-6"></span>6. Peidli S, Green TD, Shen C, Gross T, Min J, Taylor-King JP, et al. scPerturb single-cell perturbation data: RNA and protein h5ad files [Dataset]. Zenodo; 2022. Version 1.0. [doi:10.5281/zenodo.7041849](https://doi.org/10.5281/zenodo.7041849). CC BY 4.0.
