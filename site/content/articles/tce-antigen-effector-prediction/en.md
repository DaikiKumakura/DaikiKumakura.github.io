Does greater target-antigen abundance make a cell line respond to lower T-cell engager (TCE) concentrations? Explaining measured response curves and predicting a cell line before measuring its response use different information.

I digitized observed means from public 5T4×CD3 figures and evaluated small concentration–effect models while leaving out entire cell lines. Letting antigen abundance alter the half-maximal effective concentration (EC50) modestly reduced mean error, but some high-concentration responses remained poorly predicted. Effector-to-target (E:T) ratios were evaluated separately within one cell line.

## Question and intended use

The question is whether antigen abundance or E:T ratio improves prediction for cell lines or conditions whose response data were withheld. The intended use is to decide, for planning an in vitro experiment, whether antigen measurements alone suffice or line-specific response measurements remain necessary.

The target is 5T4×CD3 cytotoxicity after 72 hours. Unseen cell lines and unseen E:T conditions are separate tasks. This does not extrapolate to DLL3, human doses, cytokine release syndrome (CRS) or clinical regimens.

## Observed symbols differ from fitted curves

Yuan and colleagues report a quantitative systems pharmacology (QSP) model linking antibody binding, T-cell activation and differentiation, and tumor cytotoxicity ([1](#ref-1)). This analysis uses [original Supplementary Figure S10 and main Figure 6](https://doi.org/10.1208/s12248-026-01259-2). Kemper and colleagues describe the experimental background ([2](#ref-2)).

Only DuoBody-CD3x5T4 with the paper's CD3-binding dissociation constant (KD) of 683 nM is included, not the 16 nM high-affinity variant. The 72-hour endpoint derives from Alamar Blue viability measurements, not directly observed single-cell death probabilities ([1](#ref-1)).

**Table 1.** Digitized information and intended evaluation.

| Source | Extracted information | Use |
| --- | --- | --- |
| Supplementary Table S1 | 14 lines: 5T4 molecules/cell | Predictor for held-out lines |
| Supplementary Figure S10 | E:T=4:1, 72 hours: 166 observed-mean symbols | Leave-one-line-out evaluation |
| Figure 6 | MDA-MB-468, E:T=1, 2, 4 and 8:1: 43 observed symbols | Separate leave-one-ratio-out evaluation |

Symbols are observed means; solid curves are the authors' fitted model. **Fitted curves were not digitized as observations.** Numerical source tables were unavailable, so symbol centers and calibrated axes were converted to concentrations and cytotoxicity. Two overlapping low-concentration blue-circle candidates in S10 were excluded because centers were indeterminate; positions and reasons are distributed.

The 166 and 43 points are neither patients nor biological replicates. Nearby symbols remain displayed means, not independent donors. S10 and Figure 6 both include 4:1 conditions and are not combined to inflate sample size.

## Three Hill models

For concentration \(C\), effect \(E\), and antigen abundance \(A\),

\[
E(C,A)=E_{\max}(A)\frac{C^h}{EC_{50}(A)^h+C^h}
\]

Baseline is fixed at 0% and maximum at 0–100%. This empirical approximation of background-corrected cytotoxicity does not identify activation or synapse-formation parameters. It assumes monotonic increase and zero background, excluding low-concentration background variation and high-concentration hook effects. A close fit does not identify an optimal unobserved concentration or mechanism.

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

Coefficients are fitted to 13 of 14 lines and the remaining line predicted from concentration and antigen abundance, repeating 14 times. Held-out efficacy, line-specific fitted coefficients and response-derived line categories are excluded from predictors. Original line classes can describe all data but cannot serve as known predictors for an unseen line ([1](#ref-1)).

Each line receives equal total squared-error weight. Evaluation averages line-specific root-mean-square error (RMSE) across 14 lines, avoiding dominance by lines with more concentrations. There is no independent validation population for model tuning: this is grouped evaluation within one study.

## Antigen abundance leaves substantial errors

**Table 3.** Predictive errors in held-out lines.

| Model | Mean held-out RMSE | Mean MAE |
| --- | ---: | ---: |
| shared | 19.33 | 14.78 |
| potency | 18.02 | 13.69 |
| both | 18.28 | 13.91 |

Units are cytotoxicity percentage points (pp); MAE is mean absolute error. Results come from `analysis/run.py` and `outputs/tables/model-comparison.csv`. Potency reduces mean RMSE by 1.32 pp versus shared, calculated before rounding, improving nine of 14 lines. Adding antigen dependence to maximum effect does not outperform potency.

![Predictions and observed means in four held-out lines](shared/tce-antigen-effector-prediction/figures/01-held-out-curves.png)

**Figure 1.** Each panel's line is excluded from training. Examples illustrate a close prediction, overprediction, low maximum, and low-concentration response. Figure 2 and CSV include all 14 lines.

SCC-9 observed means remain around 35% at high concentrations, whereas predictions approach higher effects. SW780 is also overpredicted. DU 145's low-concentration response is inadequately represented. This does not establish irrelevant antigen abundance: the tested simple mapping to EC50 and maximum fails to predict all curves adequately. T-cell donor composition, intrinsic sensitivity and assay or culture conditions remain unresolved.

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

The conclusion changes little within these shifts. They do not recover unreadable missing points, antigen-quantification error or donor variation. Resampling line-level RMSE differences 10,000 times gives a central 95% range of −3.39 to 0.79 pp for potency minus shared. This describes stability among the fixed 14 lines, not a significance test accounting for shared-training dependence between folds. Lines are not a random future-tumor sample, so the range does not establish superiority.

## E:T ratios evaluated separately within one line

E:T is the initial T-cell-to-tumor-cell ratio. For MDA-MB-468 in Figure 6 only, I replace the EC50 predictor with \(\log((E:T)/4)\), fit three ratios, and predict the fourth.

**Table 5.** Held-out E:T prediction errors.

| Held-out E:T | Shared RMSE | E:T-dependent EC50 RMSE |
| --- | ---: | ---: |
| 1:1 | 14.29 | 7.68 |
| 2:1 | 6.07 | 7.13 |
| 4:1 | 11.19 | 13.39 |
| 8:1 | 11.56 | 7.45 |
| Mean over 4 ratios | 10.77 | 8.91 |

Units are pp. Ratios 1:1 and 8:1 extrapolate outside the remaining range; 2:1 and 4:1 interpolate. All change conditions within one line, not lines, donors or laboratories.

![Leave-one-E:T-out predictions in MDA-MB-468](shared/tce-antigen-effector-prediction/figures/03-held-out-et.png)

**Figure 3.** Each panel's ratio observations are withheld. The ratio model improves average error but worsens 4:1. A 72-hour endpoint does not identify early killing rates or E:T effects in other lines.

## Antigen abundance alone did not predict an unmeasured response curve

Antigen information modestly lowers mean error, but the central 95% resampling range of the line-level difference includes zero, and the models fail to capture the low high-concentration response in some lines. Within this analysis, antigen measurements cannot replace response curves. E:T evidence is limited to one line.

The original QSP describes line and donor differences using all data ([1](#ref-1)). Its fitted curves and these held-out predictions use different information. Placing them side by side cannot establish superiority of a more complex model.

## Data and code availability

[Download digitized observations, analysis code and all-line results](shared/tce-antigen-effector-prediction/tce-antigen-effector-prediction-analysis.zip).

```bash
python analysis/download_sources.py
python analysis/digitize.py
python analysis/run.py
python -m unittest discover -s tests
```

The seed is 2026102606. Materials include source URLs, coordinates, axis calibration and exclusions. Numbers are manually digitized public figures, not original individual records. Yuan materials are used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), with digitization, fitting and independently drawn figures identified as modifications.

## References

1. <span id="ref-1"></span>Yuan X, Thalhauser C, Afzal N, Kemper K, An G, Li T. An In Vitro Quantitative Systems Pharmacology Platform for Characterizing CD3-Bispecific Antibody-Mediated T-Cell Activation and Tumor Cell Cytotoxicity. AAPS J. 2026;28(5):123. [doi:10.1208/s12248-026-01259-2](https://doi.org/10.1208/s12248-026-01259-2).
2. <span id="ref-2"></span>Kemper K, Gielen E, Boross P, Houtkamp M, Plantinga TS, de Poot SA, et al. Mechanistic and pharmacodynamic studies of DuoBody-CD3x5T4 in preclinical tumor models. Life Sci Alliance. 2022;5(11):e202201481. [doi:10.26508/lsa.202201481](https://doi.org/10.26508/lsa.202201481).
