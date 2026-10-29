Does greater target-antigen abundance make a cell line respond to lower T-cell engager (TCE) concentrations? Explaining measured response curves and predicting a cell line before measuring its response use different information.

I digitized observed means from public 5T4×CD3 figures and evaluated small concentration–effect models while leaving out entire cell lines. Letting antigen abundance alter the half-maximal effective concentration (EC50) modestly reduced mean error, but some high-concentration responses remained poorly predicted. Effector-to-target (E:T) ratios were evaluated separately within one cell line.

## Question and intended use

The question is whether antigen abundance or E:T ratio improves prediction for cell lines or conditions whose response data were withheld. The intended use is to decide, for planning an in vitro experiment, whether antigen measurements alone suffice or line-specific response measurements remain necessary.

The input comes from Yuan et al.'s quantitative systems pharmacology (QSP) analysis ([1](#ref-1)); Kemper et al. reported the experimental work ([2](#ref-2)). Kemper reports an inverse association between 5T4 expression and IC50, complete killing in some low-expression lines, and partial killing in SW780 despite higher expression. Sensitivity to Fas or IFNγ signaling is a proposed explanation, not an established cause. This article asks how well a small antigen-dependent model predicts an entirely excluded line rather than merely explaining known curves.

The target is 5T4×CD3 cytotoxicity after 72 hours. Unseen cell lines and unseen E:T conditions are separate tasks. This does not extrapolate to DLL3, human doses, cytokine release syndrome (CRS) or clinical regimens.

## Observed symbols differ from fitted curves

Yuan and colleagues report a quantitative systems pharmacology (QSP) model linking antibody binding, T-cell activation and differentiation, and tumor cytotoxicity ([1](#ref-1)). This analysis uses [original Supplementary Figure S10 and main Figure 6](https://doi.org/10.1208/s12248-026-01259-2). The source assessment uses the open-access main text and the Kemper experimental report. Supplementary figures supply the digitization inputs, but supplementary prose was checked only through the main text; its 14-line, 72-hour description and the stated 9,447–61,686 molecules/cell range agree with those inputs.

Only DuoBody-CD3x5T4 with the paper's CD3-binding dissociation constant (KD) of 683 nM is included, not the 16 nM high-affinity variant. The 72-hour endpoint derives from Alamar Blue viability measurements, not directly observed single-cell death probabilities ([1](#ref-1)). Antigen abundance was estimated by binding DuoBody-CD3x5T4 to cells, detecting it with fluorescent secondary antibody and calibrating against IgG beads. It is an antibody-binding estimate rather than a directly counted absolute receptor number; its measurement error was unavailable.

The QSP analysis pooled 677 culture IDs and 1,525 observations across conditions and T-cell donors ([1](#ref-1)). Kemper's study used 3–10 donors per line ([2](#ref-2)). Errors against displayed means can therefore reflect donor composition as well as model inadequacy, which these aggregate inputs cannot separate.

**Table 1.** Digitized information and intended evaluation.

| Source | Extracted information | Use |
| --- | --- | --- |
| Supplementary Table S1 | 14 lines: 5T4 molecules/cell | Predictor for held-out lines |
| Supplementary Figure S10 | E:T=4:1, 72 hours: 166 observed-mean symbols | Leave-one-line-out evaluation |
| Figure 6 | MDA-MB-468, E:T=1, 2, 4 and 8:1: 43 observed symbols | Separate leave-one-ratio-out evaluation |

Symbols are observed means; solid curves are the authors' fitted model. **Fitted curves were not digitized as observations.** Numerical source tables were unavailable, so symbol centers and calibrated axes were converted to concentrations and cytotoxicity. A published WebPlotDigitizer reliability study concerns other graph types and software conditions ([3](#ref-3)); its reported precision is not borrowed for these manually recorded coordinates. I instead examine ±2-pixel sensitivity below. Two overlapping low-concentration blue-circle candidates in S10 were excluded because centers were indeterminate; positions and reasons are distributed.

The 166 and 43 points are neither patients nor biological replicates. Nearby symbols remain displayed means, not independent donors. S10 and Figure 6 both include 4:1 conditions and are not combined to inflate sample size.

## Three Hill models

For concentration \(C\), effect \(E\), and antigen abundance \(A\),

\[
E(C,A)=E_{\max}(A)\frac{C^h}{EC_{50}(A)^h+C^h}
\]

The Hill equation is a widely used pharmacological shape ([4](#ref-4)). Baseline is fixed at 0%, maximum at 0–100%, and slope h at 0.2–8 (`src/models.py`). This empirical approximation of background-corrected cytotoxicity does not identify activation or synapse-formation parameters. It assumes monotonic increase and zero background, excluding low-concentration background variation and high-concentration hook effects. A close fit does not identify an optimal unobserved concentration or mechanism.

EC50 means half the curve's own maximum, not necessarily a concentration killing 50% of cells. This matters when maximum effect is low. Hill slope \(h\) is shared across lines or E:T conditions in each predictive model.

**Table 2.** Model structures.

| Model | Variation between lines | Parameters |
| --- | --- | --- |
| shared | None | 3 |
| potency | Antigen-dependent EC50 | 4 |
| both | Antigen-dependent EC50 and maximum | 5 |

For example,

\[
\log EC_{50}(A)=a+b\log(A/25000)
\]

The both model additionally uses \(\operatorname{logit}(E_{\max}/100)=d+e\log(A/25000)\). The reference 25,000 sets scale, not an efficacy cutoff. Coefficient signs are not constrained to force greater antigen to improve response.

Coefficients are fitted to 13 of 14 lines and the remaining line predicted from concentration and antigen abundance, repeating 14 times. Grouping by line avoids allowing observations from the same line into both training and evaluation, a concern for hierarchical data ([5](#ref-5)). Held-out efficacy, line-specific fitted coefficients and response-derived line categories are excluded from predictors. The original four Max_kill classes were constructed by visual inspection of response profiles and subsequently supported in covariate fitting ([1](#ref-1)). They can describe known data but are not available predictors before measuring a new line's response.

Each line receives equal total squared-error weight. Evaluation averages line-specific root-mean-square error (RMSE) across 14 lines, avoiding dominance by lines with more concentrations. Mean absolute error (MAE) is reported alongside RMSE. RMSE weights large misses more heavily; MAE describes average absolute deviation. Their suitability depends on the error distribution and question ([6](#ref-6), [7](#ref-7)). There is no independent validation population for model tuning: this is grouped evaluation within one study.

## Antigen abundance leaves substantial errors

**Table 3.** Predictive errors in held-out lines.

| Model | Mean held-out RMSE | Mean MAE |
| --- | ---: | ---: |
| shared | 19.33 | 14.78 |
| potency | 18.02 | 13.69 |
| both | 18.28 | 13.91 |

Units are cytotoxicity percentage points (pp); MAE is mean absolute error. Results come from `analysis/run.py` and `outputs/tables/model-comparison.csv`. Potency reduces mean RMSE by 1.32 pp versus shared, calculated before rounding, improving nine of 14 lines. Adding antigen dependence to maximum effect does not outperform potency.

Changes vary substantially by line. RMSE decreases for DU 145 (23.18→15.24 pp), BxPC-3 (26.66→20.86), PC-3 (23.09→17.84), SK-GT-4 (19.02→12.72), and MDA-MB-468 (21.24→17.44), but increases for SCC-9 (34.56→40.15) and PANC-1 (21.32→27.19). Five lines worsen. SW780 changes little (28.91→28.58). The average gain is a balance of improvements and deteriorations, not a uniform effect (`cell-line-errors.csv`).

![Predictions and observed means in four held-out lines](shared/tce-antigen-effector-prediction/figures/01-held-out-curves.png)

**Figure 1.** Each panel's line is excluded from training. Examples illustrate a close prediction, overprediction, low maximum, and low-concentration response. Figure 2 and CSV include all 14 lines.

SCC-9 observed means remain around 35% at high concentrations, whereas predictions approach higher effects. SW780 is also overpredicted. DU 145's low-concentration response is inadequately represented. These failures are compatible with Yuan and Kemper's descriptions of partial killing despite medium-to-high antigen abundance ([1](#ref-1), [2](#ref-2)). Conversely, PANC-1 has relatively low abundance, 16,500 molecules/cell, but its own descriptive fit has EC50 about 0.016 nM. That fit is an explanation of known observations, not an unseen-line input. Antigen-based extrapolation can miss both weak and strong responders.

This does not establish irrelevant antigen abundance: the tested simple mapping to EC50 and maximum fails to predict all curves adequately. T-cell donor composition, intrinsic sensitivity and assay or culture conditions remain unresolved.

![All line errors and antigen-versus-descriptive-maximum relationships](shared/tce-antigen-effector-prediction/figures/02-line-errors-antigen.png)

**Figure 2.** Left: held-out RMSE for all 14 lines. Right: descriptive maximum effects fitted to each line's own observations, not unseen-line predictions. PC-3 and SCC-9 have similar antigen abundance but different fitted maxima. Right-panel estimates are not reused as predictive inputs on the left.

## Digitization and line-selection sensitivity

I shifted centers horizontally and vertically within ±2 pixels and refitted all 14 folds for 32 scenarios. These are center-location sensitivities, not complete measurement-error estimates or confidence intervals.

**Table 4.** Range of average RMSE across 32 center-location scenarios.

| Model | Mean RMSE range |
| --- | ---: |
| shared | 19.22–19.43 |
| potency | 17.92–18.10 |
| both | 18.19–18.37 |

The conclusion changes little within these shifts. They do not recover unreadable missing points, antigen-quantification error or donor variation. Resampling line-level RMSE differences 10,000 times using a bootstrap ([8](#ref-8)) gives a central 95% range of −3.39 to 0.79 pp for potency minus shared. This describes stability among the fixed 14 lines, not a significance test accounting for shared-training dependence between folds. There is no universally unbiased estimator of K-fold cross-validation variance valid for all distributions ([9](#ref-9)); this does not make the present naive resampling interval a corrected test. Lines are not a random future-tumor sample, so the range does not establish superiority.

## E:T ratios evaluated separately within one line

E:T is the initial T-cell-to-tumor-cell ratio. Yuan describes similar 72-hour responses at four ratios, with the strongest right shift at 1:1 ([1](#ref-1)). For MDA-MB-468 in Figure 6 only, I replace the EC50 predictor with \(\log((E:T)/4)\), fit three ratios, and predict the fourth.

**Table 5.** Held-out E:T prediction errors.

| Held-out E:T | Shared RMSE | E:T-dependent EC50 RMSE |
| --- | ---: | ---: |
| 1:1 | 14.29 | 7.68 |
| 2:1 | 6.07 | 7.13 |
| 4:1 | 11.19 | 13.39 |
| 8:1 | 11.56 | 7.45 |
| Mean over 4 ratios | 10.77 | 8.91 |

Units are pp. Ratios 1:1 and 8:1 extrapolate outside the remaining range; 2:1 and 4:1 interpolate. All change conditions within one line, not lines, donors or laboratories.

The E:T coefficient is negative in every fold, −0.71 to −0.34 (`fold-parameters.json`, an additional summary not included in the companion). Gains occur at the extrapolated 1:1 and 8:1 settings; both interpolated settings worsen. Adding an E:T term fitted to the remaining three ratios did not improve those two internal conditions. Four folds do not establish stability of this contrast.

![Leave-one-E:T-out predictions in MDA-MB-468](shared/tce-antigen-effector-prediction/figures/03-held-out-et.png)

**Figure 3.** Each panel's ratio observations are withheld. The ratio model improves average error but worsens 4:1. A 72-hour endpoint does not identify early killing rates or E:T effects in other lines. Yuan's faster early killing at higher E:T and later convergence are simulation findings ([1](#ref-1)), not additional early observations analyzed here.

## Discussion

In the tested small model, antigen abundance provided more information about EC50 than maximum response. Its potency coefficient was negative in all 14 line-holdout fits, −2.01 to −1.35. A separate descriptive Spearman correlation between antigen abundance and each line's own fitted EC50 was −0.45 (14 lines; unadjusted two-sided p=0.11). This additional calculation, absent from the companion, agrees in direction with Kemper's reported IC50 association ([2](#ref-2)) but does not reproduce that analysis or establish a precise association in 14 selected lines.

Descriptive maximum effect had almost no rank association with antigen abundance (Spearman 0.02, `outputs/results.json`). The both model's maximum-effect coefficient ranged from −0.30 to 0.48 across folds. SCC-9 had 36,102 molecules/cell but a descriptive fitted maximum near 36%. These observations are consistent with the failure of the tested simple antigen mapping to capture some response ceilings. They do not identify the reason: intrinsic signaling sensitivity, donor composition and antigen measurement error remain untested explanations.

Absolute errors also lack a measured noise reference. The input contains means, not replicate-level variation. Yuan reports line and donor effects on Max_kill and over 100% interindividual variability in some parameters ([1](#ref-1)). The part of the 18.02-pp mean RMSE that a better predictor could eliminate cannot be separated from donor and assay variation here. Relative performance among the tested models is more directly observable than an attainable-error floor.

The original QSP uses line-specific covariates for EC50_act and Max_kill, including response-derived Max_kill classes ([1](#ref-1)). Our result is compatible with the inability of this particular antigen-only mapping to replace response-ceiling information, but the original all-data fit is not an unseen-line evaluation and cannot be ranked against these predictions.

Within-line E:T holdouts have shared-model errors of 6.07–14.29 pp; holding out MDA-MB-468 entirely gives 21.24 pp. These tasks differ in concentrations, training information and fold construction. The observed difference does not quantify the relative magnitudes of cell-line and E:T effects.

For another antigen system, Van De Vyver et al. describe a cibisatamab model that captures partial killing in lower-CEA-expression lines ([10](#ref-10)); only its abstract was consulted. Different targets, molecules, structures and validation designs prevent ranking errors across papers or generalizing the present 5T4 result to all TCEs.

## Conclusion

Adding antigen abundance modestly reduced mean held-out error, 19.33→18.02 pp, but five lines worsened and the descriptive resampling range included zero. Within the tested mapping, antigen abundance informed potency more consistently than maximum response and did not substitute for an unmeasured line's response curve. This is not proof that all antigen-based models must fail. E:T evidence remains confined to one line.

The original QSP's all-data fit and these held-out predictions use different information ([1](#ref-1)); their juxtaposition cannot establish superiority of either model.

## Data and code availability

[Download digitized observations, analysis code and all-line results](shared/tce-antigen-effector-prediction/tce-antigen-effector-prediction-analysis.zip).

```bash
python analysis/download_sources.py
python analysis/digitize.py
python analysis/run.py
python -m unittest discover -s tests
```

The seed is 2026102606. Materials include source URLs, coordinates, axis calibration and exclusions. Main numerical results are in `outputs/tables/*.csv` and `outputs/results.json`. Fold-coefficient ranges and the descriptive EC50–antigen Spearman correlation are additional summaries that are not outputs of the distributed companion code; they can be reproduced after running `run.py` with the separate script [extra-fold-checks.py](shared/tce-antigen-effector-prediction/extra-fold-checks.py), which reads `outputs/fold-parameters.json` and `descriptive-curve-fits.csv`. A separate rerun of the packaged analysis matched `model-comparison.csv`. Numbers are manually digitized public figures, not original individual records. Yuan materials are used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), with digitization, fitting and independently drawn figures identified as modifications.

## References

1. <span id="ref-1"></span>Yuan X, Thalhauser C, Afzal N, Kemper K, An G, Li T. An In Vitro Quantitative Systems Pharmacology Platform for Characterizing CD3-Bispecific Antibody-Mediated T-Cell Activation and Tumor Cell Cytotoxicity. AAPS J. 2026;28(5):123. [doi:10.1208/s12248-026-01259-2](https://doi.org/10.1208/s12248-026-01259-2).
2. <span id="ref-2"></span>Kemper K, Gielen E, Boross P, Houtkamp M, Plantinga TS, de Poot SA, et al. Mechanistic and pharmacodynamic studies of DuoBody-CD3x5T4 in preclinical tumor models. Life Sci Alliance. 2022;5(11):e202201481. [doi:10.26508/lsa.202201481](https://doi.org/10.26508/lsa.202201481).
3. <span id="ref-3"></span>Drevon D, Fursa SR, Malcolm AL. Intercoder reliability and validity of WebPlotDigitizer in extracting graphed data. Behav Modif. 2017;41(2):323-39. [doi:10.1177/0145445516673998](https://doi.org/10.1177/0145445516673998).
4. <span id="ref-4"></span>Goutelle S, Maurin M, Rougier F, Barbaut X, Bourguignon L, Ducher M, et al. The Hill equation: a review of its capabilities in pharmacological modelling. Fundam Clin Pharmacol. 2008;22(6):633-48. [doi:10.1111/j.1472-8206.2008.00633.x](https://doi.org/10.1111/j.1472-8206.2008.00633.x).
5. <span id="ref-5"></span>Roberts DR, Bahn V, Ciuti S, Boyce MS, Elith J, Guillera-Arroita G, et al. Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure. Ecography. 2017;40(8):913-29. [doi:10.1111/ecog.02881](https://doi.org/10.1111/ecog.02881).
6. <span id="ref-6"></span>Willmott CJ, Matsuura K. Advantages of the mean absolute error (MAE) over the root mean square error (RMSE) in assessing average model performance. Clim Res. 2005;30:79-82. [doi:10.3354/cr030079](https://doi.org/10.3354/cr030079).
7. <span id="ref-7"></span>Chai T, Draxler RR. Root mean square error (RMSE) or mean absolute error (MAE)? Arguments against avoiding RMSE in the literature. Geosci Model Dev. 2014;7(3):1247-50. [doi:10.5194/gmd-7-1247-2014](https://doi.org/10.5194/gmd-7-1247-2014).
8. <span id="ref-8"></span>Efron B. Bootstrap methods: another look at the jackknife. Ann Stat. 1979;7(1):1-26. [doi:10.1214/aos/1176344552](https://doi.org/10.1214/aos/1176344552).
9. <span id="ref-9"></span>Bengio Y, Grandvalet Y. No unbiased estimator of the variance of K-fold cross-validation. J Mach Learn Res. 2004;5:1089-105. [https://www.jmlr.org/papers/v5/grandvalet04a.html](https://www.jmlr.org/papers/v5/grandvalet04a.html).
10. <span id="ref-10"></span>Van De Vyver AJ, Weinzierl T, Eigenmann MJ, Frances N, Herter S, Buser RB, et al. Predicting tumor killing and T-cell activation by T-cell bispecific antibodies as a function of target expression: combining in vitro experiments with systems modeling. Mol Cancer Ther. 2021;20(2):357-66. [doi:10.1158/1535-7163.MCT-20-0269](https://doi.org/10.1158/1535-7163.MCT-20-0269).
