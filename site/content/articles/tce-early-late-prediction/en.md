If a 48-hour T-cell engager (TCE) assay could substitute for a 72-hour result, candidate assessment could finish a day earlier. But does a small response at 48 hours indicate limited activity or a response still developing?

I digitized observed means at 24, 48 and 72 hours from public 5T4×CD3 experiments. Small models fitted only to 24 and 48 hours predict the 72-hour observations. A lag model reduces pooled error across two cell lines, but the line-specific results differ: carrying the 48-hour value forward works better for MDA-MB-468.

## Can the 72-hour measurement be omitted?

The question is how accurately 24- and 48-hour measurements predict the 72-hour activity readout, and whether the public data support omitting late measurements in candidate assessment.

The endpoint is in-vitro cytotoxicity, not clinical effects, dosing intervals or responses to TCEs targeting other antigens. This is retrospective figure-based evaluation: 72-hour values were visible when images were retrieved. It is not prospectively blinded validation, but those values are excluded from parameter estimation and lag selection.

## Eighteen series with early observations

Yuan and colleagues analyze T-cell activation and tumor-cell effects of a 5T4×CD3 antibody using quantitative systems pharmacology (QSP). Their study includes 14 cell lines, but [the original Figure 3](https://doi.org/10.1208/s12248-026-01259-2) provides observed 24-, 48- and 72-hour values for only MDA-MB-231 and MDA-MB-468 ([1](#ref-1)).

Nine concentrations have all three times in each line: 0.0000176, 0.0000878, 0.000439, 0.0022, 0.011, 0.0549, 0.274, 1.37 and 6.86 nM. All use an effector-to-target (E:T) ratio of 4:1 and DuoBody-CD3×5T4 with CD3-binding KD of 683 nM.

**Table 1.** Inputs and exclusions.

| Information in the public figure | Treatment |
| --- | --- |
| Gray observed means for 2 lines × 9 concentrations × 3 times | 54 digitized points |
| 24 and 48 hours in each line | 18 points per line used for fitting |
| 72 hours in each line | 9 points per line used for prediction evaluation |
| MDA-MB-468, another 10 concentrations | Excluded because observations exist only at 72 hours |
| Blue QSP model curves | Not treated as observations |

Combining gray symbols and blue curves would introduce circularity: an original model fitted through 72 hours would supply early values used to predict that same endpoint. Only observed symbols were read here.

The assay is Alamar Blue. Its cytotoxicity percentages are not identical to directly counted fractions of dead cells. Original orange ranges are 25th–75th percentiles, not standard errors of the mean (SEM). They are omitted for conditions with one or two culture IDs, so missing ranges are not evidence of low variability ([1](#ref-1)).

Donor and culture-ID correspondence across times was not recovered. This evaluation compares aggregate means sharing line, concentration and E:T labels; it does not forecast the trajectory of the same donor.

## Carry-forward and linear-extrapolation references

Write the observed 72-hour value as \(y_{72}\) and its prediction as \(\widehat y_{72}\). The first reference carries the 48-hour value forward:

\[
\widehat y_{72}^{\mathrm{carry}}=y_{48}
\]

The second extends the change from 24 to 48 hours through the next 24 hours, clipping predictions to 0–100%:

\[
\widehat y_{72}^{\mathrm{linear}}
=\operatorname{clip}(2y_{48}-y_{24},0,100)
\]

Observed values themselves are retained without clipping. Some low-concentration MDA-MB-231 signals are higher at 24 than 48 hours; they were not edited to enforce smooth increases.

## Linking concentration and time with two coefficients

The small concentration-dependent model is

\[
\widehat E(C,t)=100\left[
1-\exp\left\{-k_{\max}
\frac{C}{EC_{50}+C}\max(t-\tau,0)\right\}
\right]
\]

Concentration \(C\) is in nM, time \(t\) and lag \(\tau\) in hours, and \(k_{\max}\) in inverse hours. With an assumed 100% ceiling and initially \(\tau=0\), I fit \(k_{\max}\) and \(EC_{50}\) separately for each line. The nine concentrations at two early times receive equal weight in least-squares fitting.

Here \(EC_{50}\) is the concentration halving the model's rate term, not the EC50 of the 72-hour concentration-response curve or binding KD. Nor is \(k_{\max}\) an individual T cell's killing rate.

I then fix lag at every integer hour from 0 through 47, refitting the two coefficients each time. The selected lag minimizes error at 24 and 48 hours, not error at 72 hours.

**Table 2.** Parameters fitted to early data.

| Line | Model | \(k_{\max}\), h⁻¹ | \(EC_{50}\), nM | Selected lag, h |
| --- | --- | ---: | ---: | ---: |
| MDA-MB-231 | No lag | 0.0150 | 0.376 | Fixed at 0 |
| MDA-MB-231 | Lag selected using early data | 0.0384 | 0.457 | 21 |
| MDA-MB-468 | No lag | 0.0387 | 0.141 | Fixed at 0 |
| MDA-MB-468 | Lag selected using early data | 0.0781 | 0.190 | 14 |

These 21- and 14-hour estimates come from an empirical equation and aggregate data. They do not show that T-cell activation actually waited that long. The 100% ceiling, zero response at zero concentration and monotonically increasing time course are assumptions and do not match every observation.

![Early-data fits and 72-hour observations](shared/tce-early-late-prediction/figures/01-early-late-curves.png)

**Figure 1.** Examples at low, intermediate and high concentrations. Gray symbols are observed means used in fitting; open symbols are excluded 72-hour means. Curves beyond 48 hours extrapolate in time. Vertical ranges denote ±2 image pixels, not the original variability intervals. Source: [original Figure 3](https://doi.org/10.1208/s12248-026-01259-2) ([1](#ref-1)); curves and figure are from this analysis.

## Line differences matter more than pooled error

Errors are expressed in percentage points (pp). Root mean squared error (RMSE) is the square root of the average squared difference between predictions and observations.

**Table 3.** Prediction errors at 72 hours.

| Method | MDA-MB-231 RMSE, pp | MDA-MB-468 RMSE, pp | RMSE across 18 conditions, pp | Errors within 10 pp |
| --- | ---: | ---: | ---: | ---: |
| Carry 48 hours forward | 18.1 | 5.2 | 13.3 | 14/18 |
| Linear extrapolation | 10.2 | 14.4 | 12.5 | 13/18 |
| No-lag model | 16.4 | 5.1 | 12.1 | 14/18 |
| Lag selected using early data | 7.2 | 9.1 | 8.2 | 16/18 |

Ten pp is an illustrative counting tolerance, not a validated assay acceptance criterion. Distributed tables also count errors within 5 and 20 pp.

The nine equally weighted concentrations include low-response conditions. The count 16/18 is not a candidate-selection success rate and does not establish adequate prediction where concentration-response curves change steeply.

MDA-MB-231 responses increase between 48 and 72 hours at some concentrations, so carry-forward underpredicts. At 1.37 nM, the observed mean rises from approximately 53% to 87%; the lag model predicts approximately 77%.

For MDA-MB-468 at 0.0549 nM, observed means are approximately 47% and 44%, whereas the lag model predicts approximately 64%. The small observed decline is not interpreted as recovery or resistance; reading error and culture composition may contribute. It illustrates that improved early fit need not improve later prediction.

![Prediction errors at 72 hours compared with simple references](shared/tce-early-late-prediction/figures/02-prediction-errors.png)

**Figure 2.** Left: no-lag predictions versus observed 72-hour means. Right: pooled RMSE across all 18 conditions for four methods. This aggregate reconstruction is neither a significance test between models nor validation in independent donors.

Despite the lag model's lower pooled error, carry-forward is better for MDA-MB-468. Selecting the best method separately for each line after inspecting 72-hour results would not provide an unbiased estimate of prediction performance and is not reported as such.

## The lag is not uniquely determined by early data

For MDA-MB-231, early-data error changes little across part of the lag range. I examine fits within 2 pp of the minimum training RMSE. This score tolerance is neither a confidence interval nor a set of biologically validated parameters.

At 0.274 nM, 72-hour predictions within that range span approximately 43–100%. The minimum-error fit predicts approximately 52%, versus an observed mean near 59%. A close best-fit prediction does not imply that early data uniquely determine it.

![Early errors and later predictions across fixed lag values](shared/tce-early-late-prediction/figures/03-lag-identifiability.png)

**Figure 3.** At each fixed lag, coefficients are refitted using only 24 and 48 hours. The dotted minimum-RMSE-plus-2-pp line denotes the sensitivity tolerance. The search originally ended at 36 hours and was extended to 47 after early scores remained flat at the boundary. No-lag and minimum-error estimates and principal scores are unchanged.

For \(24\leq\tau<48\), every 24-hour prediction is zero. At 48 hours, time enters through the product

\[
a=k_{\max}(48-\tau)
\]

Changing the rate to preserve \(a\) can leave the 48-hour concentration response similar while changing the 72-hour prediction. This property of the equation is not evidence of a genuinely long biological delay.

Some source observations are already positive at 24 hours. Extreme lags miss those points; remaining within an average-RMSE tolerance does not resolve time-specific residuals or biological plausibility. Low-concentration positive signals near background also exceed what this zero-start model describes. A small average score is not proof that rate and lag are identified.

## Digitization sensitivity does not justify omitting measurements

The source image is 685×370 pixels, with a particularly small right panel. Two pixels correspond to approximately 3.5 pp in MDA-MB-231 and 5.2 pp in MDA-MB-468.

I calculate 128 fixed-seed reading scenarios within ±2 pixels, keeping the selected lag fixed and refitting coefficients. This separates reading sensitivity from the lag uncertainty examined above.

Lag-model RMSE spans approximately 5.1–9.6 pp for MDA-MB-231 and 7.0–12.7 pp for MDA-MB-468. Carry-forward for MDA-MB-468 spans approximately 2.9–8.9 pp, overlapping the model range. These are reading-assumption scenarios, not biological confidence intervals or upper bounds on all error. They create neither cellular/donor replicates nor virtual patients.

Donor correspondence across times and prediction on separate experimental days remain unverified. These 18 series do not justify broadly eliminating 72-hour measurements.

## Evidence does not support omitting the late measurement

The lag model has lower pooled error, but carrying 48 hours forward predicts MDA-MB-468 more accurately. Similar early fits can produce divergent later predictions, so average scores do not establish stable extrapolation.

Low-response conditions contribute to the 18-series score, and donors and experimental days were not independently validated. Digitization sensitivity does not certify that any particular concentration can forgo a 72-hour measurement.

## Data and code availability

The [analysis archive](shared/tce-early-late-prediction/tce-early-late-prediction-analysis.zip) includes 54 digitized coordinates, exclusions, processed data, models, tables and execution code, with official image sources, license information and SHA-256 hashes.

Main values correspond to `outputs/tables/predictions.csv`, `method-summary.csv` and `parameters.csv` generated by `analysis/run.py`. Sensitivity results are in `lag-profile.csv` and `reading-score-summary.csv`. These are not original individual-donor measurements or refits of the original QSP model.

## References

1. <span id="ref-1"></span>Yuan X, Thalhauser C, Afzal N, Kemper K, An G, Li T. An In Vitro Quantitative Systems Pharmacology Platform for Characterizing CD3-Bispecific Antibody-Mediated T-Cell Activation and Tumor Cell Cytotoxicity. AAPS J. 2026;28(5):123. [Paper and supplementary materials](https://link.springer.com/article/10.1208/s12248-026-01259-2) / [doi:10.1208/s12248-026-01259-2](https://doi.org/10.1208/s12248-026-01259-2). CC BY 4.0. Observed means in the original Figure 3 were digitized for the early-time fitting, 72-hour comparison and figures/tables of this article. Blue original-model curves were not treated as observations.
