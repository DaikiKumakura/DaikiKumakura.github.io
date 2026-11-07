## Introduction

Evaluations of Perturb-seq models increasingly include retrieval: given a cell state, name which perturbation was applied from a list of candidates. The reported numbers differ between papers and competitions. ExPert reports top-10 recall and "fold over chance" ([1](#ref-1)); the Virtual Cell Challenge primer describes a perturbation discrimination score (PDisc and its normalization) ([2](#ref-2)); PerturBench uses a rank metric where 0 is perfect and 0.5 is random ([3](#ref-3)); RNA fingerprinting can decline to answer (abstain) ([4](#ref-4)).

Can these numbers be converted into one another, and which comparisons survive? This article puts one discriminability scale on the problem, namely how much higher the true candidate scores than the other candidates, and checks it against the figure source data released with ExPert ([5](#ref-5)). The model is a simple lens, not a claim about how any method works. The analysis plan was not fixed before computing, and no confidence intervals were computed for the fitted parameters. The mixture fits, the held-out-k interpolation check and the screen-level effective discriminability were added while looking at results, so they are exploratory.

## Abstract

For a retrieval task with N candidates, an M-alternative forced-choice signal-detection model (the true candidate's score is Normal with mean d′, the other candidates' scores Normal with mean 0, all variances 1) gives top-k recall, mean reciprocal rank (MRR) and rank-fraction discrimination scores as functions of d′ and N. At N = 1,157 and d′ = 2, the normalized discrimination score (1 − 2·PDisc) is 0.84, top-10 recall 0.35 and fold over chance 40. Fitting ExPert's released recall@k (k = 1, 5, 10, 20, 50, 100), a model with one d′ for all queries does not fit: fitted on k = 1, 10, 100, the RMSE on held-out k = 5, 20, 50 is 0.082 (contexts seen in training, ID) and 0.084 (contexts withheld from training, OOD), where RMSE is the root-mean-square error. If d′ varies across queries, both a two-parameter continuous distribution and a three-parameter two-component mixture interpolate the held-out k within 0.01 (a weak test, because a smooth curve is fitted at three points), and for ExPert reproduce MRR, which was not used in fitting, within 0.01 (OOD observed 0.376, mixture 0.376). Heterogeneity across queries is one of several explanations of why the single-d′ model fails. The d′ required for 50% top-10 recall is 1.66 at 200 candidates and 3.30 at 19,895; a roughly 100-fold larger pool costs 1.64 units of d′. Fold over chance depends strongly on N, so values at different N are not comparable without N. Reading a reported value also requires checking fold weighting, query composition and abstention.

## Methods

### Discriminability model

There are $N$ candidates, one of which is the true perturbation. The true candidate's score is $S \sim \mathcal{N}(d', 1)$ and the other $N-1$ scores are independent $\mathcal{N}(0,1)$. The true candidate's rank is 1 plus the number of other candidates above $S$ (ties are ignored). Given $S = s$, let $q(s) = 1 - \Phi(s)$ be the probability that a distractor exceeds $s$. Then

$$
\mathrm{top}\text{-}k = \mathbb{E}_S\!\left[\Pr\big(\mathrm{Bin}(N-1,\,q(S)) \le k-1\big)\right],\quad
\mathrm{MRR} = \mathbb{E}_S\!\left[\frac{1-(1-q(S))^{N}}{N\,q(S)}\right],\quad
\mathrm{AUROC} = \Phi\!\left(d'/\sqrt{2}\right)
$$

where $\Phi$ is the standard normal cumulative distribution function, $\mathrm{Bin}$ is the binomial distribution, and AUROC is the probability that the true candidate outscores one other candidate. The rank-fraction discrimination score (PDisc) is taken as the expected fraction of other candidates that are closer than the true one, $\mathrm{PDisc} = 1 - \Phi(d'/\sqrt{2})$, with normalized value $1 - 2\,\mathrm{PDisc}$. This has a similar form to the definition in the Virtual Cell Challenge primer (rank by Manhattan distance, divide by the total, multiply by 2, subtract from 1) ([2](#ref-2)). It is a hypothetical rank-fraction scale, not a conversion of that score: the actual scoring differs in distance, candidate set and averaging. Fold over chance is top-k divided by $k/N$ ($k$ is the number of top-ranked candidates counted). Ties are ignored in the model; the original counts ties as half ([1](#ref-1)), which can raise recall and MRR slightly for coarse scores. Using d′ for M-alternative forced choice follows the classical d′ tables of Hacker and Ratcliff from psychophysics, which concern percent correct, that is, top-1 ([6](#ref-6)). The extension to top-k and MRR is made here. This article does not quote their table values; it computes the formulas above by numerical integration (a grid of 4,001 points).

When d′ differs between queries, these quantities are averaged over the distribution of d′. Here $\pi$ is the proportion of strong queries. Three families were compared:

- a single d′ (1 parameter)
- d′ drawn from a normal distribution $\mathcal{N}(\mu, \tau^2)$ (2 parameters; integrated with 41-point Gauss–Hermite quadrature)
- a two-component mixture of strong queries $d'_1$ and weak queries $d'_2$ with proportion $\pi$ (3 parameters)

### Data and fitting

The input is `fig2a_radar_ext.csv` from the figure source data of ExPert (Zenodo, CC BY 4.0) ([5](#ref-5)). For ExPert and baseline methods it holds recall@k (k = 1, 5, 10, 20, 50, 100), MRR and AUROC for pseudobulk queries (the pooled profile of all cells of one perturbation in one dataset) against 1,157 candidates, in held-out cells of contexts seen in training (ID) and in contexts withheld from training (OOD). In the original methods, metrics are computed per dataset-by-fold combination and averaged with one vote per perturbation ([1](#ref-1)). The MRR definition is given in the original ([1](#ref-1)). I did not find a definition of AUROC in the text of the original that I read. The model's AUROC is true-versus-one-distractor, and I could not confirm that the released value uses the same definition. Agreement in AUROC is therefore only a consistency check, valid if the definitions match.

Fitting minimized the sum of squared errors of recall at k = 1, 10, 100 (Nelder–Mead), then predicted held-out recall at k = 5, 20, 50, MRR and AUROC and compared them with the released values. The same procedure was run for ExPert in both regimes plus the nearest-centroid baseline, XGBoost and linear regression (8 conditions in total). No confidence intervals for the fitted parameters or the RMSE were computed. The numerical integration was checked against Monte Carlo simulation (seed 20261107): recall and MRR for 20,000 queries agreed with the quadrature within 0.004 at d′ = 1, 2 and 3.

### Re-aggregation of released values

Fold over chance for ExPert's zero-shot retrieval (19,895-gene candidate set) was re-aggregated from the released data of original Figure 3 for 12 cross-validation splits (one model each) ([5](#ref-5)), in two ways: unweighted and weighted by effect size. Abstention was re-aggregated from the released source data of original Figure S4 ([5](#ref-5)). Nothing was retrained. The effective d′ of a screen is the single-d′ value, at N = 19,895, that gives that screen's unweighted top-10 recall. Real query populations are mixtures, so this is a convenient value (the single d′ giving the same top-10 recall), not an estimated parameter.

## Results

### One d′ determines each metric

Figure 1 shows each metric against d′ at N = 1,157. Table 1 gives representative values.

![Metrics as functions of d-prime for 1,157 candidates: normalized discrimination score, top-100, top-10, MRR and top-1.](shared/retrieval-metrics-common-scale/figures/fig1_metrics_vs_dprime.png)

Figure 1. Metrics against d′ for 1,157 candidates. The normalized discrimination score (1 − 2·PDisc) rises first at small d′, and top-1 rises last. Computed from the equal-variance Gaussian model, not from data.

Table 1. Metric values for given d′ (N = 1,157; `analysis/07_afc_model.py`). PDisc is the expected fraction of other candidates scoring above the true one; PDiscNorm is its normalization.

| d′ | PDisc | PDiscNorm (1 − 2·PDisc) | Top-1 | Top-10 | Fold over chance (top-10) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0.5 | 0.362 | 0.276 | 0.004 | 0.030 | 3.4 |
| 1.0 | 0.240 | 0.520 | 0.015 | 0.083 | 9.6 |
| 2.0 | 0.079 | 0.843 | 0.112 | 0.347 | 40.1 |
| 3.0 | 0.017 | 0.966 | 0.396 | 0.725 | 83.9 |
| 4.0 | 0.002 | 0.995 | 0.752 | 0.944 | 109.3 |

As an illustration, a normalized discrimination score of 0.86 (an arbitrary example value) corresponds to d′ = 2.09, where top-1 is 0.129 and top-10 is 0.379 at N = 1,157 (`analysis/11_effective_dprime.py`). Rank-fraction metrics approach their ceiling once d′ exceeds 2, before top-1 or MRR does. Methods that sit close together on a high discrimination score can differ widely in top-k.

### Fit to ExPert's released values

Figure 2 and Table 2 show the fits to k = 1, 10, 100.

![Observed top-k recall of ExPert in seen and held-out contexts with fitted curves from one d-prime, a normal distribution of d-prime and a two-component mixture.](shared/retrieval-metrics-common-scale/figures/fig2_expert_fits.png)

Figure 2. ExPert's released recall@k (N = 1,157) with three fitted families. Filled circles were used in fitting; open circles were held out. The normal and mixture curves nearly overlap.

Table 2. Held-out recall, and predicted MRR and AUROC not used in fitting (`analysis/09_afc_validation.py`).

| Regime | Family | Parameters | RMSE, held-out k | MRR (observed 0.634 / 0.376) | AUROC (observed 0.958 / 0.845) |
| --- | --- | ---: | ---: | ---: | ---: |
| ID | One d′ | 1 | 0.082 | 0.614 | 0.990 |
| ID | Normal d′ | 2 | 0.002 | 0.626 | 0.953 |
| ID | Mixture | 3 | 0.004 | 0.636 | 0.961 |
| OOD | One d′ | 1 | 0.084 | 0.271 | 0.948 |
| OOD | Normal d′ | 2 | 0.006 | 0.372 | 0.830 |
| OOD | Mixture | 3 | 0.004 | 0.376 | 0.867 |

In the MRR and AUROC headers the observed values are given as ID / OOD. Held-out k are 5, 20 and 50.

The facts are these. A single d′ misses held-out recall by about 0.08. In OOD its MRR of 0.271 falls well below the observed 0.376, and its AUROC of 0.948 exceeds the observed 0.845. Models with query-dependent d′ reproduce held-out recall within 0.006, but with 3 fitted points this is largely interpolation of a smooth curve, so it is weak evidence for either family; the 2-parameter fit is not exactly determined by the 3 points and so carries more weight than the 3-parameter one. MRR is close to the observation for the continuous distribution (0.372) and the mixture (0.376). Neither query-dependent family matches AUROC within about 0.025 (OOD 0.830 for the continuous distribution and 0.867 for the mixture against 0.845), so AUROC does not separate them; the one clear signal is the single-d′ value in ID (0.990 against 0.958). The mixture fit gave a strong component $d'_1$ = 4.07, a weak component $d'_2$ = 1.55 and a strong share of 0.72 in ID, and 3.57, 0.88 and 0.51 in OOD. The continuous fit gave mean 3.65 and standard deviation 1.65 in ID, and mean 2.27 and standard deviation 1.91 in OOD.

Across all 8 conditions, the held-out-k RMSE of the single d′ was about 0.028 or more in 7 conditions, at most 0.011 for the continuous distribution and at most about 0.004 for the mixture. The exception was XGBoost OOD, where recall is near chance and all three families gave 0.003.

As interpretation, what the released curves reject is the equal-variance, independent-candidate model with one d′. Query heterogeneity is one explanation. Others also give a shallow recall curve: correlated or hub-like distractors, unequal variances, heavy-tailed or bounded scores, and queries whose true candidate cannot be retrieved. The released values cannot separate them. Averaging over splits, datasets and perturbations (one vote per perturbation) can itself create a mixture, and per-split or per-screen data, such as Table 5, are the direct evidence on heterogeneity. The continuous distribution and the mixture are nearly indistinguishable on the curves, so the two-component form is not supported. The normal fit for OOD puts about 12% of its mass at negative d′, which is not interpretable as discriminability. The 3-parameter mixture is exactly determined by the 3 fitted points, so the real tests are the held-out k, MRR and AUROC, of which MRR is the most informative.

### What the candidate count demands of discriminability

Figure 3 and Table 3 show how the d′ needed for a target recall grows with N.

![Required d-prime against candidate set size for top-10 recall of 50% and 90% and top-1 recall of 50%.](shared/retrieval-metrics-common-scale/figures/fig3_required_dprime.png)

Figure 3. d′ required for a target recall (single-d′ model). The horizontal axis is logarithmic.

Table 3. Required d′ under the equal-variance Gaussian model (`analysis/08_required_dprime.py`). Slow growth is a property of Gaussian tails; heavier tails or correlated distractors give a stronger dependence on N.

| N | Top-10 = 50% | Top-10 = 90% | Top-1 = 50% |
| ---: | ---: | ---: | ---: |
| 100 | 1.30 | 2.60 | 2.50 |
| 200 | 1.66 | 2.96 | 2.74 |
| 1,157 | 2.40 | 3.69 | 3.28 |
| 8,347 | 3.05 | 4.34 | 3.80 |
| 19,895 | 3.30 | 4.59 | 4.01 |
| 100,000 | 3.73 | 5.02 | 4.38 |

The d′ needed for 50% top-10 recall is 1.66 at N = 200 and 3.30 at N = 19,895; a 99.5-fold larger pool adds 1.64 units of d′. At fixed d′, fold over chance grows with N. For top-10 recall at d′ = 2.25 it is 51 at N = 1,157 and 293 at N = 19,895 (Figure 4; `outputs/tables/fold_at_fixed_dprime.csv`).

![Fold over chance of top-10 recall against candidate set size for three values of d-prime on logarithmic axes.](shared/retrieval-metrics-common-scale/figures/fig4_fold_vs_N.png)

Figure 4. Fold over chance of top-10 recall at fixed d′. Both axes are logarithmic.

Extending the mixture fit of ExPert OOD (script 07, fitted to all six k) to other N gives top-10 recall of 0.607 at N = 200, 0.484 at 1,157, 0.364 at 8,347 and 0.312 at 19,895, with fold over chance of 12, 56, 304 and 620. The single-d′ fit gives 0.148 at N = 19,895, more than twofold lower. Because the two fits disagree so much, and because changing N also changes the training split in practice, the extrapolation is not used as a prediction and is shown only as a conversion example.

### Points to check when reading a reported value

I examined how the same "fold over chance" moves with definition in ExPert's released values (`analysis/01_zero_shot_definitions.py`, median over 12 fold models).

Table 4. Fold over chance for zero-shot retrieval (N = 19,895) by definition, median over 12 splits. The original reports the effect-weighted values as "overall" (genes withheld from training, context seen) and as OOD (context also withheld) ([1](#ref-1)).

| Query set | Unweighted fold | Effect-weighted fold |
| --- | ---: | ---: |
| All queries pooled | 17.5 | 26.9 |
| Gene withheld, context seen | 17.0 | 26.2 |
| Gene and context withheld (OOD) | 9.0 | 13.5 |

The effect-weighted 26.2-fold and 13.5-fold agree with the values reported in the original ([1](#ref-1)). Weighting by knockdown effect size has a rationale, since perturbations with no effect cannot be retrieved. Weighted and unweighted values answer different questions rather than one correcting the other. Unweighted folds are smaller, with a median split-wise ratio of 1.52 (range 1.47–1.58). By screen, unweighted top-10 recall ranges from 0.0009 to 0.315 (Table 5). The four essential-gene screens (K562 essential, HepG2, RPE1, Jurkat) hold 0.44% of queries and 26.4% of all hits (a hit is a query whose true perturbation was ranked in the top 10). Excluding these four, the unweighted fold at the screen-by-model level falls from 8.4 to 6.2.

Table 5. Unweighted top-10 recall by screen and the single d′ giving the same value (N = 19,895; selected screens. All 22 screens are in `outputs/tables/effective_dprime_screens.csv`). The effective d′ is not comparable across screens with different mixtures of effect sizes.

| Screen | Queries | Top-10 recall | Fold | Effective d′ |
| --- | ---: | ---: | ---: | ---: |
| K562 essential (Replogle 2022) | 876 | 0.3151 | 627 | 2.82 |
| Zhuang 2026 | 4,956 | 0.0420 | 83 | 1.57 |
| X-Atlas HCT116 | 110,520 | 0.0045 | 8.9 | 0.68 |
| Marson 2025 D3 Stim48hr | 41,904 | 0.0009 | 1.9 | 0.18 |

This spread shows that discriminability differs widely between queries even within the released values. It points the same way as the mixture fits of Table 2 but is not a direct confirmation. A screen's value is itself a mixture within the screen. A pooled fold depends on which screens contribute how many queries.

Another point is abstention. The per-dataset RNA fingerprinting ensemble can decline to answer ([4](#ref-4)). In the source data of original Figure S4 ([5](#ref-5)) it abstains on 20.3% of 1,579,672 cells in ID and 53.9% of 210,280 cells in OOD across 22 datasets. In the source data of original Figure S4C, OOD top-10 recall is 0.086 over all cells and 0.136 over the cells it answered, and ExPert on the same cells moves from 0.226 to 0.255. These panels use different aggregations from the abstention shares above and are not mutually consistent as a simple product; I did not reconcile them. The original reports that ExPert's lead holds on the answered cells ([1](#ref-1)). A top-k for a method that abstains mixes the abstention rate with the accuracy on answered cells. A comparison needs both the share answered (coverage) and the accuracy among those answered.

## Discussion

Part of the reason numbers differ between metrics is a difference of scale. The scale is a conversion lens, not evidence about ExPert's score distributions. The normalized discrimination score, the rank fraction, top-k and MRR are monotone functions of one d′, so they convert into one another once N is fixed (Table 1). Three things do not convert:

- folds at different N (Figure 4)
- pooled values over different query compositions (Tables 4 and 5), which are different questions rather than errors
- top-k for methods that abstain

ExPert's released curves were interpolated, and MRR reproduced, within about 0.01 when discriminability is allowed to vary across queries. Either a mixture of strong and weak queries or a continuous distribution explains the curve shape, and the released values alone cannot separate them. The original's claim, a recall more than twice the best existing method in withheld contexts ([1](#ref-1)), is not weakened by this model. What was examined here is how to read reported numbers.

For evaluation design, under the Gaussian model the required d′ grows only slowly with N (Table 3). When tasks with different N are compared, a top-k curve reported with N is therefore a steadier basis than fold over chance. Recall also depends on how the candidate list is defined (for example, duplicates at gene or perturbation level). Narrowing to 100 candidates lowers the d′ needed for 50% top-10 recall to 1.30. Converting the Virtual Cell Challenge discrimination score to d′ requires real values, because its distance and candidate set differ ([2](#ref-2)). PerturBench's rank metric ([3](#ref-3)) likewise converts only as far as it is a rank fraction. These individual values were not converted here.

## Limitations

- **Model assumptions:** a simple equal-variance Gaussian model. Score-distribution tails and correlations between candidates are not modeled. If candidates resemble one another (gene families, for example), the assumption of independent other candidates breaks. Ties are ignored in the model.
- **Fitting:** fits are to released summary curves (averaged over folds and perturbations), not to per-query data. Averaging can itself create mixtures. The 3-parameter fit is exactly determined by its 3 fitted points. No uncertainty was computed for the parameters, the RMSE, the effective d′ or the medians in Table 4 (only the range of the split-wise ratio is given).
- **AUROC definition:** the definition of the released AUROC was not in the text of the original that I read. Agreement with the model's AUROC is only a consistency check valid if the definitions match.
- **Extrapolation:** the extrapolation to N = 19,895 differs more than twofold between the single d′ and the mixture (0.148 versus 0.312). It is not used as a prediction.
- **Unread sources:** I read the first half of the RNA fingerprinting paper ([4](#ref-4)) and the first half of PerturBench ([3](#ref-3)). I did not read the second halves. Forward-prediction literature such as Systema is not cited because its full text was not read.
- **Data:** ExPert's released data are figure summaries, not a recomputation from raw data. ExPert is a preprint and has not been peer reviewed. The authors' competing interests are as stated in the paper (one author is affiliated with NVIDIA, and another is a consultant to several companies).
- **Exploratory analysis:** the mixture fits, the held-out-k check and the screen-level effective d′ were added after seeing results.
- **Use of AI and review:** the article was written with an AI (Claude) and reviewed three times by AI reviewers commissioned by the same author; this is not confirmation by a human third party.

## Conclusion

Retrieval metrics for identifying the true perturbation among candidates convert among top-k, MRR and rank-fraction discrimination scores once the query discriminability d′ and the candidate count N are fixed. A model with one d′ for all queries does not fit ExPert's released recall@k, while a model with query-dependent d′ reproduced held-out k and MRR. Whether the dependence is two-component or continuous cannot be decided from the released values. Fold over chance depends on N, weighting and query composition, and the top-k of a method that abstains mixes coverage with accuracy. Unless these are reported alongside, folds and top-k values cannot be compared directly across papers. This conclusion depends on the equal-variance Gaussian assumption, the released summary values and an unconfirmed AUROC definition.

## Data and code availability

The re-run materials (scripts 01, 06, 07, 08, 09, 10 and 11 in `analysis/`, tables, figures and logs in `outputs/`, and `data/fig2a_radar_ext.csv`) are in the [companion archive](shared/retrieval-metrics-common-scale/retrieval-metrics-common-scale-companion.zip). `fig2a_radar_ext.csv` is part of the figure source data of ExPert ([5](#ref-5), CC BY 4.0), and attribution is given in the README. Scripts 07 to 11 run on the bundled data alone (Windows 11, Python 3.12.4, numpy 2.2.6, pandas 2.2.2, scipy 1.14.0, matplotlib 3.9.1). Scripts 01 and 06 need the data of original Figure 3 and Figure S4 in the Zenodo record ([5](#ref-5)) (retrieval steps are in the README), which are not bundled; their output tables and logs are. Re-run: `python analysis/07_afc_model.py && python analysis/08_required_dprime.py && python analysis/09_afc_validation.py && python analysis/10_figures.py && python analysis/11_effective_dprime.py`. The random seed is 20261107.

## References

<span id="ref-1"></span>1. Schwartz L, Schlamowitz JL, Kuznets-Speck B, Johnson CW, Das D, Grody EI, et al. ExPert infers causal perturbations from cell states across biological and clinical contexts [Preprint]. bioRxiv; 2026. Version 1, posted 2026 Nov 3. Not peer reviewed. [doi:10.64898/2026.11.02.762549](https://doi.org/10.64898/2026.11.02.762549).

<span id="ref-2"></span>2. Fleetwood C, Adduri A. Arc Virtual Cell Challenge: a primer [Internet]. Hugging Face Blog; 2025 Jul 18 [cited 2026 Nov 7]. Available from: https://huggingface.co/blog/virtual-cell-challenge

<span id="ref-3"></span>3. Wu Y, Wershof E, Schmon SM, Nassar M, Osiński B, Eksi R, et al. PerturBench: benchmarking machine learning models for cellular perturbation analysis [Preprint]. arXiv; 2024. Version 4, 2025 Oct 24. [arXiv:2408.10609](https://arxiv.org/abs/2408.10609).

<span id="ref-4"></span>4. Grabski IN, Lee J, Blair J, Dalgarno C, Mascio I, Bradu A, et al. Mapping transcriptional responses to cellular perturbation dictionaries with RNA fingerprinting [Preprint]. bioRxiv; 2025. Version 1, posted 2025 Sep 20. [doi:10.1101/2025.09.19.676866](https://doi.org/10.1101/2025.09.19.676866).

<span id="ref-5"></span>5. Schwartz L, Schlamowitz JL, Kuznets-Speck B, Johnson CW, Das D, Grody EI, et al. ExPert - figure data [Dataset]. Zenodo; 2026. Version v0.1.0 (2026 Oct 28). [doi:10.5281/zenodo.23740198](https://doi.org/10.5281/zenodo.23740198). CC BY 4.0.

<span id="ref-6"></span>6. Hacker MJ, Ratcliff R. A revised table of d′ for M-alternative forced choice. Percept Psychophys. 1979;26:168–170. [doi:10.3758/BF03208311](https://doi.org/10.3758/BF03208311).
