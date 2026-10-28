[日本語](tce-pet-lesion-retention.html)

Visible tumor uptake soon after administration does not establish how that signal will change later. I used a public table from a human PET study of the CEA×CD3 T-cell engager AMG 211 to test whether two early measurements predict next-day lesion signal.

Extending the 3–6-hour log slope to 24 hours performed substantially worse than carrying forward the 6-hour value. A retention factor estimated from other patients did not improve log error over that baseline either. The complete-case benchmark contains 16 lesions from four patients, not 16 independent patients.

## From 37 tabulated lesions to 16 complete cases

The source study measured the distribution of 89Zr-labeled AMG 211 by PET. The broader study enrolled nine patients, whereas public Supplementary Table S3 contains SUVmax measurements for 37 quantifiable lesions in six patients. Neither is the size of the present prediction cohort ([Moek et al., 2019](https://pubmed.ncbi.nlm.nih.gov/30745297/); [Supplementary Table S3](https://aacr.figshare.com/articles/journal_contribution/22470416)).

| Source patient ID | Tabulated lesions | Complete three-time-point lesions | Reason for exclusion |
| --- | ---: | ---: | --- |
| 1 | 13 | 0 | No 3-hour imaging (ND) |
| 2 | 4 | 4 | None |
| 3 | 4 | 4 | None |
| 5 | 7 | 7 | None |
| 7 | 8 | 0 | 6-hour scan technically not evaluable (NE) |
| 8 | 1 | 1 | None |
| Total | 37 | 16 | Four complete-case patients |

ND and NE were not replaced by zero. Lesions from one patient were never split between training and evaluation as though they came from different people. The analysis table was extracted directly from the public DOCX XML, not digitized from curves.

The question is whether the same lesion's SUVmax at the source's nominal 3, 6, and 24 hours can be predicted without using its 24-hour result. The context of use is a research benchmark for considering imaging-time-point reduction. SUVmax is a lesion radioactivity signal, not a concentration of active TCE.

![Figure 1. Three SUVmax measurements for each complete lesion](shared/tce-pet-lesion-retention/figures/lesion-trajectories.svg)

Calculations use the table's nominal 3, 6, and 24 hours. Individual exact scan-start timestamps are not given in that table and were not reconstructed. The supplemental methods describe tracer-alone and added-unlabeled-AMG-211 administration conditions. A patient-specific dose-adjustment model was not estimated here ([Supplementary methods](https://aacr.figshare.com/articles/journal_contribution/22470416)).

## Extending the early slope

Let \(S_t\) denote lesion SUVmax. Three methods were compared.

**Carry forward the 6-hour value**

\[
\widehat S_{24}=S_6.
\]

**Continue the 3–6-hour log slope**

\[
k_{3\to6}=\frac{\log(S_6/S_3)}{6-3},\qquad
\widehat S_{24}=S_6\exp\{k_{3\to6}(24-6)\}
=S_6\left(\frac{S_6}{S_3}\right)^6.
\]

This assumes that the signal maintains one constant log-change rate. It estimates neither drug elimination nor the radionuclide's physical half-life.

**Estimate a retention factor from other patients**

\[
\log r_{-p}=\frac1{P-1}\sum_{q\ne p}\frac1{n_q}
\sum_{j=1}^{n_q}\log\frac{S_{24,qj}}{S_{6,qj}},\qquad
\widehat S_{24,pj}=S_{6,pj}r_{-p}.
\]

Patient \(p\) is withheld in full, and the remaining three patients calibrate the factor. Averaging within patient before averaging across patients prevents one person with many lesions from dominating calibration. None of the test patient's 24-hour lesion measurements enters its factor.

## The early log slope did not persist

![Figure 2. Predicted versus observed 24-hour SUVmax for three methods](shared/tce-pet-lesion-retention/figures/prediction-scatter.svg)

The three panels share a vertical scale for comparison. Extreme predictions are retained rather than clipped. Dashed lines indicate equality.

The primary metric is the square root of the equal-patient mean of within-patient mean squared log errors. An equal-patient mean absolute SUV error is also shown.

| Method | Equal-patient log RMSE | Equal-patient SUV MAE |
| --- | ---: | ---: |
| Carry 6 hours | 0.653 | 1.577 |
| Continue early log slope | 3.604 | 7,770.357 |
| Other-patient retention factor | 0.689 | 1.413 |

See `outputs/tables/overall-scores.csv`. The retention factor modestly reduced MAE but did not improve log RMSE. Because the chosen metric changes the comparison, this is not an overall improvement in prediction.

Patient 3, lesion 4 illustrates the large errors. Its tabulated sequence was 2.4→11.3→3.3. Continuing the early rise predicted approximately 123,107 at 24 hours. The value 11.3 was not presumed to be a typographical error and corrected, nor was the prediction capped at an arbitrary upper limit. The example exposes failure of the constant-log-rate extrapolation assumption.

![Figure 3. Prediction errors with whole patients withheld](shared/tce-pet-lesion-retention/figures/patient-error.svg)

## The failure is not confined to one lesion

A post-hoc influence calculation excluded the largest early rise, patient 3 lesion 4. The primary analysis retains all 16 lesions. With the remaining 15, log RMSE was 0.586 for carrying 6 hours, 2.515 for slope continuation, and 0.646 for the other-patient retention factor. Removing that extreme lesion did not make slope continuation outperform the baseline (`outputs/tables/influence-exclusion.csv`).

In 500 scenarios independently perturbing each SUV by ±0.05 to assess the one-decimal printed inputs, log RMSE ranged respectively from 0.629 to 0.676, 3.538 to 3.663, and 0.662 to 0.716. These are input-rounding sensitivities, not confidence intervals for a population beyond the four patients (`outputs/tables/rounding-sensitivity.csv`).

Complete-case selection is another limitation. Performance in the 21 excluded lesions is unknown, and other drugs, targets, and administration conditions were not validated. These three time points cannot separate lesion measurement error, SUVmax noise, perfusion, binding, or internalization contributions.

The four-patient benchmark did not support continuing the 3–6-hour slope to 24 hours. Early uptake and next-day retention cannot be treated as the same constant-rate process here. Even simple predictions from 6 hours retained error, so these data do not support replacing the 24-hour scan.

## Reproducibility

[Code, extracted tables, and outputs](shared/tce-pet-lesion-retention/tce-pet-lesion-retention-analysis.zip). Run `analysis/download_sources.py` to fetch the public supplement and `analysis/run.py` to reproduce extraction, prediction, figures, and tables. `python -m unittest discover -s tests` checks whole-patient exclusion and calibration. The original DOCX is not redistributed; its URL, license, and SHA-256 are recorded.

## References

Moek KL, Waaijer SJH, Kok IC, et al. 89Zr-labeled Bispecific T-cell Engager AMG 211 PET Shows AMG 211 Accumulation in CD3-rich Tissues and Clear, Heterogeneous Tumor Uptake. *Clinical Cancer Research*. 2019;25(12):3517–3527. [doi:10.1158/1078-0432.CCR-18-2918](https://doi.org/10.1158/1078-0432.CCR-18-2918).

Moek KL, et al. Supplementary Data_clean. Supplementary methods and Table S3. [Publisher-linked public supplement](https://aacr.figshare.com/articles/journal_contribution/22470416). CC BY 4.0.

## Cite this article

Kumakura D. Can early PET predict next-day lesion retention of a T-cell engager? 2026. Independent reanalysis of published lesion-level SUVmax data.
