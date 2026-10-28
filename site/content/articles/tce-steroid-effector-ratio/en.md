[日本語版](tce-steroid-effector-ratio.html)

Even when a steroid reduces T-cell engager (TCE) activity, the difference need not be constant across culture conditions. In an experiment with the PSMA-targeting CC-1, cytotoxicity with dexamethasone was low at small effector-to-target (E:T) ratios and approached the mean response with tocilizumab at larger ratios.

I compared two explanations with the same number of parameters: a uniform reduction in the response ceiling and an increase in the effector input required for a given response. The latter had lower error when predicting unused E:T conditions. The exact fold increase in required input, however, was not stably estimable from this figure.

## Two combination conditions were compared

Kauer and colleagues' Figure 1C reports 72-hour coculture of healthy-donor PBMCs with LNCaP cells. CC-1 was 1 µg/mL, with either dexamethasone (DEX) at 0.1 µg/mL or tocilizumab (TOCI) at 10 µg/mL. E:T ratios were 0.625, 1.25, 2.5, 5 and 10. The figure reports mean±SD from four donors ([Kauer et al., 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7264835/)).

**This panel has no CC-1-alone curve.** The reference is the TOCI combination, compared with the DEX combination. E:T follows the source terminology, but the effector preparation was PBMCs rather than purified T cells. These ratios cannot be directly converted into intratumoral T-cell counts.

I read the square and triangular mean markers. Ten points are aggregates for five conditions in two groups, not individual data from four people. Source lines and error bars were not added as observations ([original Figure 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC7264835/#F1)).

| E:T ratio | TOCI combination mean | DEX combination mean | Difference |
| --- | ---: | ---: | ---: |
| 0.625 | 100.0 | 11.7 | 88.3 |
| 1.25 | 96.1 | 37.9 | 58.3 |
| 2.5 | 99.0 | 59.2 | 39.8 |
| 5 | 104.9 | 90.3 | 14.6 |
| 10 | 98.1 | 95.1 | 2.9 |

The source response is tumor-cell lysis as percent of control; differences are percentage points (pp). Values are approximate image readings. Their printed decimal places do not represent original assay precision.

The question is which description better predicts this condition-dependent difference: a lower ceiling or a horizontal shift. The context of use is description of a nonclinical assay at fixed drug concentrations and culture duration. Clinical superiority of CRS prophylaxis or clinical dosing is not evaluated.

## Comparing hypotheses at equal complexity

The reference Hill curve is

\[
f(r)=E\frac{r^h}{K^h+r^h},
\]

where \(r\) is the E:T ratio, \(E\) is the ceiling, \(K\) the half-maximal ratio and \(h\) the slope.

The horizontal-shift model changes \(K\) to \(qK\) under DEX while sharing the ceiling. The ceiling-change model shares \(K\) and changes the DEX ceiling to \(E/q\). Both have four parameters, \(E,K,h,q\), with \(q\ge1\). The main analysis constrains \(E\le100\), retains observed means slightly above 100 and uses equally weighted least squares.

Both points at a given E:T ratio are removed together. The remaining eight points estimate the model, which predicts the excluded pair. This is repeated across five ratios. It is **validation across unused culture conditions**, not leave-one-donor-out validation.

## Horizontal shift predicted unused conditions better

![Two descriptions of the E:T dependence](shared/tce-steroid-effector-ratio/figures/et-model-comparison.png)

Figure 1. Observed mean markers read from the source and fits from this analysis. Five means per group; the source aggregates four donors. These are not reproduced source fit lines.

| Model | Fitting RMSE | Paired E:T-holdout RMSE | Held-out DEX-only RMSE |
| --- | ---: | ---: | ---: |
| Horizontal shift | 3.17 | 6.54 | 7.21 |
| Ceiling change | 20.27 | 27.95 | 27.99 |

Units are pp. Changing only the ceiling could not simultaneously represent the small DEX response at low E:T and its approach to the reference group at high E:T. Horizontal shift allows both curves to approach the same ceiling and therefore describes this pattern more closely.

![Both groups at an E:T ratio were withheld together](shared/tce-steroid-effector-ratio/figures/heldout-ratio.png)

Figure 2. Prediction minus observed mean for the excluded DEX condition. These are condition-specific errors, not an error distribution across independent donors.

Allowing the ceiling search to extend to 150 gives E:T-holdout RMSE of 7.34 pp for horizontal shift and 23.99 pp for ceiling change, retaining the ranking. The latter fit estimates a ceiling of 132.0%; this is adjustment of an extrapolated curve, not a biological maximum cytotoxicity of 132%.

## The shift factor is not resolved

The main horizontal-shift coefficient \(q\) is 37.5. However, the TOCI means are already nearly flat at the smallest measured E:T ratio. Its reference half-maximal ratio \(K\) lies below the measured range: the ascending reference response was not observed directly.

I independently perturbed each mean marker's vertical position within ±1.5 pixels and refitted 100 reading scenarios. Fitting RMSE ranged from 2.59 to 3.73 pp for horizontal shift and from 19.57 to 21.00 pp for ceiling change, preserving the shape difference. In contrast, \(q\) ranged from 21.7 to approximately 180,000. These are reading-scenario ranges, not confidence intervals for a donor population.

The result therefore cannot mean that adding 37.5 times as many PBMCs compensates for DEX. What is supported is the decreasing between-group mean difference at larger measured ratios and the utility of a horizontal-shift approximation within that range. The shift does not identify whether proliferation inhibition, altered cell state, slower action or another process caused the pattern.

## Culture conditions are separate from clinical prophylaxis

The original study also includes proliferation, time-course and mouse-tumor experiments, but the present model uses only the 72-hour aggregates in Figure 1C. No conversion from fixed DEX or TOCI concentration to patient exposure was performed. Individual responses and covariance across the four donors cannot be reconstructed, so no new significance test of the group difference is supplied.

Treating the DEX-associated difference as the same fractional loss at every E:T ratio misses the measured response shape. Horizontal shift predicted unused conditions better than a uniform ceiling reduction, but the reference group's measurement range prevented precise quantification of that shift.

## Reproduction

The [analysis code and tables](shared/tce-steroid-effector-ratio/tce-steroid-effector-ratio-analysis.zip) include marker coordinates, axis calibration, models and condition-holdout predictions. Run `python analysis/download_sources.py` to retrieve sources and `python analysis/run.py` to regenerate CSVs and figures. `python -m unittest discover -s tests -v` checks condition splits and numerical recalculation. Original article figures are not included in the companion ZIP.

## References

Kauer J, Hörner S, Osburg L, et al. Tocilizumab, but not dexamethasone, prevents CRS without affecting antitumor activity of bispecific antibodies. *Journal for ImmunoTherapy of Cancer*. 2020;8:e000621. [doi:10.1136/jitc-2020-000621](https://doi.org/10.1136/jitc-2020-000621).

## Cite this article

Kumakura D. Does the effect of dexamethasone on T-cell engager cytotoxicity depend on the effector-to-target ratio? Independent reanalysis of public aggregate assay data. [Japanese](tce-steroid-effector-ratio.html); [English](tce-steroid-effector-ratio-en.html).
