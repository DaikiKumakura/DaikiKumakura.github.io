[日本語](zw209-repeated-challenge.html)

T-cell engagers with almost identical activity after the first two stimulations need not remain equivalent after the third. In a public ZW209 poster, three cytotoxicity curves initially overlap and then separate. This allows a small forecasting test: can the early observations predict the later divergence?

A constant-retention model calibrated on the first two observations substantially overpredicted third-stimulation activity for the CD28-null control and the AMG 757 analogue, by approximately 92 and 86 percentage points (pp). Its third-stimulation error for ZW209 was small. The biological separation is already reported in the original poster. The additional result here is a quantitative test of a fixed early-to-late extrapolation rule, not a newly discovered mechanism.

## What was restimulated

The October 23, 2026 development announcement for ZW209 supplies a current reason to examine this molecule. The data analyzed here, however, are preclinical observations from Figure 2B of an AACR 2025 poster, not clinical outcomes ([development announcement](https://ir.zymeworks.com/news-releases/news-release-details/zymeworks-enters-exclusive-global-license-and-collaboration/); [Lau et al., 2025, Figure 2](https://www.zymeworks.com/wp-content/uploads/2025/04/ZYME-AACR-2025-ZW209_final.pdf)).

The assay used T cells and DLL3-positive NCI-H82 tumor cells. After each stimulation, T cells were collected, counted and restimulated with fresh tumor cells and antibody. Consequently, this is not an observation of a declining drug concentration in vivo.

The plotted comparators are ZW209, ZW209 CD28null and the analogue labeled AMG 757† in the poster. The last comparator is not assumed to be identical to clinical or commercial drug material. Figure 2B contains five markers for ZW209 and three for each control. Donor counts, independent experiment counts and variance are not specified for this panel. Eleven plotted markers cannot be treated as eleven independent participants.

| Item | Definition for this analysis |
| --- | --- |
| Question of interest | How accurately do the first two cytotoxicity measurements predict the third? |
| Context of use | Assessment of extrapolation across restimulations within this assay |
| Common evaluation | Third-stimulation measurements for all three molecules |
| Additional observations | Fourth and fifth ZW209 measurements only; unreported controls are not imputed |
| Outside scope | Human doses, dose intervals or clinical efficacy |

## Recovering overlapping markers from vector objects

Markers overlap at the first two stimulations, making separate image readings difficult. The original PDF retains the differently colored markers as vector drawing objects. The script selects these objects by color and location within Figure 2B. Their bounding-box centers are transformed from PDF coordinates to cytotoxicity using the displayed 0% and 100% axis positions.

The extracted positions are saved with the resulting values in `data/processed/vector-observations.csv`. These are coordinates of a published graphical summary, not recovered individual donor records. Rendering or inspecting the source does not create new experimental observations.

| Molecule | First stimulation | Second | Third |
| --- | ---: | ---: | ---: |
| ZW209 | 98.2% | 97.8% | 97.5% |
| ZW209 CD28null | 97.7% | 97.1% | 4.5% |
| AMG 757 analogue | 97.7% | 97.0% | 10.1% |

The poster describes the third-stimulation controls as having no antitumor activity. The displayed markers are slightly above zero. The calculations retain their extracted values rather than replacing them with zero.

## Calibrating a retention rule on two stimulations

Let \(A_n\) denote cytotoxicity after stimulation \(n\). A constant fraction retained per stimulation gives

\[
A_n=A_1r^{n-1},\qquad
\widehat r=\frac{A_2}{A_1}.
\]

No numerical optimization is required for this two-point calibration. The third-stimulation forecast is \(\widehat A_3=A_2^2/A_1\). Observations from the third and subsequent stimulations are not used for calibration. Retention limits were not adjusted after seeing the held-out results.

The index \(n\) denotes stimulation number, not days. Measurement days are 4, 7, 11, 14 and 18, with unequal intervals. The fitted fraction therefore is not a daily decay rate or a half-life. Cytotoxicity is not the number of viable effector cells, and \(r\) is not T-cell survival probability.

The simple baseline carries forward the second value: \(\widehat A_n=A_2\). Comparing against this baseline tests whether extrapolating an early trend is more useful than assuming no further change. The balanced comparison is restricted to the third stimulation, available for all three molecules.

## Similar initial retention did not predict the separation

The fitted retention fractions were 0.9963 for ZW209, 0.9944 for CD28null and 0.9937 for the AMG 757 analogue. All three simply encode nearly constant early activity. Their observed third-stimulation activities were very different.

| Molecule | Retention-rule prediction | Source observation | Predicted minus observed |
| --- | ---: | ---: | ---: |
| ZW209 | 97.5% | 97.5% | −0.1 pp |
| ZW209 CD28null | 96.6% | 4.5% | +92.0 pp |
| AMG 757 analogue | 96.4% | 10.1% | +86.4 pp |

![Repeated-stimulation forecasts calibrated on two initial points](shared/zw209-repeated-challenge/figures/repeat-forecast.svg)

The close third-point prediction for ZW209 does not establish accurate prediction of every later stimulation. Only ZW209 has fourth- and fifth-stimulation observations in the plot. Those observations remain visible, but later unperformed or unreported control observations are not imputed as zero.

| Method | Third-stimulation RMSE | Mean absolute error |
| --- | ---: | ---: |
| Geometric retention | 72.9 pp | 59.5 pp |
| Carry second value | 73.3 pp | 59.9 pp |

These quantities are saved in `outputs/tables/common-round-scores.csv`. They average three molecular summaries, not patient-level prediction errors. The small difference between the two methods is less consequential than their shared failure to capture the controls' sudden loss of activity.

![Held-out third-stimulation errors](shared/zw209-repeated-challenge/figures/third-round-error.svg)

## Small coordinate changes do not remove the failure

Each of the first three vertical coordinates was independently perturbed within ±0.5 PDF point. Two thousand fixed-seed scenarios were calculated per molecule. This is a sensitivity analysis for graphical coordinate placement, not a confidence interval for donor variation or assay measurement error.

| Molecule | Range of third-stimulation prediction error |
| --- | ---: |
| ZW209 | −1.50 to +1.45 pp |
| ZW209 CD28null | +90.61 to +93.51 pp |
| AMG 757 analogue | +84.93 to +87.79 pp |

Large overprediction for both controls persisted. Conversely, the small ZW209 error should not be presented as precision to a tenth of a percentage point: its sign changes under these minor graphical perturbations.

## The mechanism is not identified by this forecast

The matched CD28-null comparison is informative about a contribution from CD28 function. It does not, on its own, quantitatively separate changes in cell abundance, cell state, recovery or reseeding. The caption describes collecting and counting T cells, but complete viable input counts and E:T ratios across restimulations cannot be reconstructed from this panel. Failure of a fixed retention rule does not establish a particular exhaustion mechanism.

Likewise, exact calibration on two measurements is not evidence of forecasting ability. High early cytotoxicity did not distinguish later activity in this experiment. This is a distinction between assay horizons used for molecular selection, not a clinical ranking of treatments. Initial concentration-response activity and activity after repeated challenges cannot be treated as interchangeable measurements.

## Reproduction material

[Code, extracted coordinates and result tables](shared/zw209-repeated-challenge/zw209-repeated-challenge-analysis.zip). Run `analysis/download_sources.py` to obtain the public source PDF, followed by `analysis/run.py` for extraction, forecasts, sensitivity analysis and new figures. The original PDF and original figures are not redistributed. The coordinate rules, all eleven marker locations and source SHA-256 are recorded.

## References

Lau D, Repenning P, Canals Hernaez D, et al. ZW209, a DLL3 targeted trispecific T cell engager with integrated CD28 co-stimulation, demonstrates safety and potent preclinical efficacy in models of small cell lung cancer. AACR Annual Meeting 2025. Abstract 7318, Figure 2. [Public poster](https://www.zymeworks.com/wp-content/uploads/2025/04/ZYME-AACR-2025-ZW209_final.pdf). New analyses and figures were generated from displayed marker coordinates; the source poster is not redistributed.

Zymeworks. Zymeworks Enters into an Exclusive Global License and Collaboration Agreement with Roche for ZW209, a Trispecific T cell Engager Targeting DLL3. October 23, 2026. [Development announcement](https://ir.zymeworks.com/news-releases/news-release-details/zymeworks-enters-exclusive-global-license-and-collaboration/).

## Cite this article

Kumakura D. Can initial ZW209 cytotoxicity predict activity after repeated stimulation? Independent analysis of public figure coordinates. 2026. [Japanese](zw209-repeated-challenge.html); [English](zw209-repeated-challenge-en.html).
