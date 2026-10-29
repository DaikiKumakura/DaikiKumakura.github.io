[日本語版](mrna-tce-repeat-pk.html)

When a T-cell engager (TCE) is encoded by mRNA, the injected material is not the antibody protein itself. The subsequent protein concentration reflects both production and disappearance. Reproducing the first concentration profile does not establish that superimposing an unchanged response will predict repeated dosing.

I examined this distinction using public data on MTS105, an mRNA-encoded TCE targeting glypican-3 (GPC3). A small model described the first rise and fall, but its individual-animal fourth-occasion predictions did not outperform simply replaying the first measured profile in concentration-scale root mean squared error (RMSE). Between-occasion differences remained that were less apparent in the mean curve.

## Comparing the first and fourth occasions in the same ten animals

Huang and colleagues described MTS105, a lipid-nanoparticle mRNA formulation encoding a GPC3×CD3 TCE. The present analysis uses serum TCE protein concentrations from the Source Data corresponding to [the original Figure 6B](https://www.nature.com/articles/s41467-025-66087-y#Fig6) ([1](#ref-1)).

The workbook contains 210 observations at 21 times in ten cynomolgus monkeys. These are individual-animal values, not digitized figure means. The concentration unit is ng/mL. The Methods specifies 45 µg/kg; the required dosing inputs are Days 1, 8, 15 and 22.

**Table 1.** Analysis intervals and observation counts.

| Interval | Observations used | Records | Role |
| --- | --- | ---: | --- |
| First dose | Nine times from Day 1 through Day 8 | 90 | Parameter estimation |
| Later occasions | Twelve times from Day 8.5 onward | 120 | Prediction without refitting |
| Fourth occasion | Nine times from Day 22 through Day 29 | 90 | Main prediction assessment |

The integer-day samples on Days 8, 15, 22 and 29 are treated as predose. Protein newly produced after that day's injection does not enter its predose observation. The workbook's decimal times, including 1.01 and 1.042 days, are preserved rather than replaced by nominal 0.25-hour and one-hour times.

Figure 6 describes four injections through Day 22, whereas the Methods describes five, including Day 29. This reporting difference is retained. The final analyzed observation is the Day 29 predose sample, so both descriptions require only doses on Days 1, 8, 15 and 22 for the present forecast ([original Figure 6 and Methods](https://www.nature.com/articles/s41467-025-66087-y#Fig6)).

The question is whether the first profile predicts later concentrations in the same animal. The context of use is assessment of between-occasion prediction in this nonclinical dataset. It is not validation of a dose or interval for new animals or humans.

## Two states describe production and disappearance

The single-dose concentration is

\[
C_i(t)=A_i\frac{e^{-k_s t}-e^{-k_f t}}{k_f-k_s},\qquad k_f>k_s>0.
\]

This is the solution for a decaying production source feeding a protein compartment with first-order disappearance. The animal-specific magnitude \(A_i\) has units ng/mL/day, and both rate constants have units day\(^{-1}\). The rates are shared across the ten animals; only the magnitudes are animal specific. This is not a nonlinear mixed-effects (NLME) model estimating a random-effects distribution or its variance.

The source administered a 30-minute intravenous infusion. Here, time zero is infusion start and the production source is approximated as an instantaneous input. The earliest sampling includes a time during infusion, so the model does not resolve the immediate infusion profile or effects of infusion rate.

Protein concentrations alone do not assign the two rates to mRNA disappearance and protein elimination: exchanging those biological assignments produces the same convolution. Accordingly, \(k_s\) and \(k_f\) are ordered empirical rates. Repeated-dose forecasts sum identical single-dose responses at the known dosing times.

Comparators are a single exponential decline and empirical replay of each animal's first measured profile every seven days. Replay uses linear interpolation between observations and sets the response beyond seven days to zero. Its zero first-occasion error is inevitable reuse of the input measurements, not evidence of predictive ability.

There are 91 recorded zeros among 210 observations: 36 on the first occasion and 47 on the fourth. The workbook does not identify which, if any, are genuine zeros or values encoded as zero below a quantification limit. All first-occasion observations are retained for the main fit, minimizing

\[
\sum_{i,t\in\mathrm{first}}
\left[\operatorname{asinh}\{C_i^{\rm pred}(t)/s\}
-\operatorname{asinh}\{C_i^{\rm obs}(t)/s\}\right]^2.
\]

The main scale \(s\) is 1 ng/mL. The transformation accepts zero values; it does not identify the assay-error distribution. Sensitivity analyses change \(s\) and omit reported zeros during estimation.

## Better first-dose fit does not establish repeat-dose prediction

![First-occasion estimation and fourth-occasion prediction](shared/mrna-tce-repeat-pk/figures/occasion-prediction.png)

**Figure 1.** Observed means of ten animals, models estimated only from the first occasion, and first-profile replay shown as a gray dashed line. Fourth-occasion measurements never enter parameter estimation. This figure was newly generated by the present analysis.

**Table 2.** Concentration-scale RMSE for fitting and prediction.

| Method | First-occasion RMSE | Later-occasion RMSE | Fourth-occasion RMSE |
| --- | ---: | ---: | ---: |
| Single exponential | 9.48 | 20.16 | 18.22 |
| Two-state production/disappearance | 5.95 | 17.94 | 16.58 |
| Replay of first profile | 0.00 | 17.37 | 15.63 |

RMSE is in ng/mL, weighting each animal-time observation equally. The two-state model represents the initial rise and improves on a single exponential. However, fourth-occasion concentration RMSE is larger than for replay. Ranking reverses on the transformed scale: fourth-occasion asinh RMSE is 1.384 for the two-state model and 1.476 for replay. Ranking therefore depends on whether large concentration errors or differences including the low-concentration region receive more weight.

Resampling animal identities 10,000 times while holding predictions fixed gives a percentile 95% interval of 6.19–24.05 ng/mL for the two-state fourth-occasion RMSE and 8.55–21.68 ng/mL for replay. The two intervals overlap substantially and do not constitute a test of the difference between models. These intervals are conditional on which of the ten animals are represented. They exclude parameter-refitting, quantification-limit and model-structure uncertainty.

The fitted rates are 1.962 and 1.965 day\(^{-1}\), with their separation approaching the lower search boundary. Near equality, the expression approaches \(A_i t e^{-kt}\). This is evidence that one empirical time scale approximately describes the initial profile, not that two distinct biological rates were measured.

## Individual changes are larger than the average suggests

![Paired first- and fourth-occasion observations](shared/mrna-tce-repeat-pk/figures/paired-animal-prediction.png)

**Figure 2.** Observations on the first and fourth occasions in the same animal and the two-state forecast based on its first occasion. Each panel is one animal, ten in total. No correction is fitted to later occasions.

I compared seven-day trapezoidal integrals of the recorded concentrations. The fourth-to-first ratio has a median of 0.613, a minimum of zero and a maximum of 9.805. The arithmetic mean of the individual ratios is 2.034, substantially different from the median. Two animals have zero recorded values at every fourth-occasion sampling time, whereas others have marked increases.

![Paired exposure ratios calculated from the reported values](shared/mrna-tce-repeat-pk/figures/paired-exposure.png)

**Figure 3.** Ratios of trapezoidal integrals retaining reported zeros. These values do not establish that true exposure or protein production disappeared.

A model that repeats the same production and disappearance process every week has difficulty representing this pattern. The present analysis cannot attribute the differences specifically to immunogenicity, changing translation efficiency or assay limitations.

**Table 3.** Fourth-occasion prediction error under alternative first-occasion fits.

| Handling during first-occasion estimation | Fourth-occasion RMSE (ng/mL) |
| --- | ---: |
| All records retained; \(s=0.5\) | 16.87 |
| All records retained; \(s=1\) | 16.58 |
| All records retained; \(s=2\) | 16.31 |
| Reported zeros omitted; \(s=1\) | 16.15 |

Every forecast is scored against all 90 fourth-occasion records. Large individual prediction errors persist under these choices. This sensitivity analysis is not a substitute for a censored likelihood with a known quantification limit.

## Group accumulation differs from individual reproducibility

The source reports sex-stratified Day-22/Day-1 AUC and Cmax ratios mostly within 0.5–2.0 and no significant accumulation. Here the distribution instead divides individual trapezoidal integrals of recorded values. A ratio of means, a mean of individual ratios and their median need not agree. This distribution therefore does not by itself refute the original group summary ([1](#ref-1)).

Conversely, little group-level accumulation does not guarantee accurate next-occasion predictions for the same individual. The finding here is individual prediction error. The comparison is also restricted to serum protein concentrations; fitting it does not establish stable liver production, functional TCE abundance or tumor activity across occasions.

Both the two-state model and empirical replay are deterministic predictions from the same first-occasion information. Their errors do not identify a biological mechanism that changes between occasions. First-occasion measurement error, transformation and interpolation, unknown quantification limits and model approximation also contribute.

## What the data support

Describing the first rise and fall with a small model and predicting repeat-dose exposure in the same animal proved to be different tasks. The two-state model improved the former but did not outperform replay of the first profile in concentration-scale RMSE in the latter (the ranking reverses on the transformed scale).

This is occasion extrapolation in the same ten animals, not external validation in an independent animal cohort. Sparse trapezoidal integrals do not recover unobserved peaks, and zero encoding limits exposure interpretation. The data do not justify converting these differences into a human virtual-patient distribution or a human dosing interval. Assuming that the response after the first dose simply recurs on repeat dosing left large individual errors in fourth-occasion prediction, even in this public MTS105 dataset.

## Data and code availability

The [companion files](shared/mrna-tce-repeat-pk/mrna-tce-repeat-pk-analysis.zip) contain analysis code and CSV tables. The original workbook is not bundled: it is downloaded from the official URL and verified by SHA-256. Run `python analysis/run.py` to regenerate extraction, estimation, prediction and figures, and `python -m unittest discover -s tests -v` to check event timing and scores.

## References

1. <span id="ref-1"></span>Huang Y, Liu S, Zhang X, Zhang B, Shi F, Zhang J, et al. Organ-specific delivery of an mRNA-encoded bispecific T cell engager targeting glypican-3 in hepatocellular carcinoma. Nat Commun. 2025;16(1):11111. [doi:10.1038/s41467-025-66087-y](https://doi.org/10.1038/s41467-025-66087-y).


<span id="reproduction"></span>
<span id="cite-this-article"></span>
