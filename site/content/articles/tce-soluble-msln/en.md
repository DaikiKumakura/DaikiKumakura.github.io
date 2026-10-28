A mesothelin-targeting T-cell engager (TCE) encounters soluble MSLN as well as the cell-surface target. Even when target-cell properties remain fixed, changing the soluble-antigen concentration can change the response at the same TCE concentration.

This reanalysis fitted a model using public H226 experiments at 0 and 50 ng/mL soluble MSLN, then predicted the complete concentration–response curve at 500 ng/mL. Error was lower for both molecules than with a model ignoring soluble antigen. Nevertheless, EC50 at 500 ng/mL was overpredicted relative to a descriptive fit of that observed curve, with a larger discrepancy for one molecule.

[日本語版](tce-soluble-msln.html)

## Predicting a higher soluble-antigen condition

**QOI: Can responses at 0 and 50 ng/mL soluble MSLN predict the TCE concentration–response curve at 500 ng/mL?**

**COU: Examine how much concentration-setting predictions can miss when soluble antigen is ignored within the same nonclinical assay. This is not used to select a human dose or regimen from circulating antigen values.**

Snell and colleagues compared the MSLN-bivalent NM28-2746 with monovalent NM28-1872. Only H226 in their Figure 4a is analysed here. C86 cells in the same figure are excluded, and antigen-density-based cell selection is not evaluated. The rightward shift caused by soluble antigen is already established in the original study. The question here is prediction of a higher unused condition from two lower conditions ([Snell et al., 2023](https://doi.org/10.1080/2162402X.2023.2233401)).

| Item | Conditions used |
| --- | --- |
| Target cells | H226 |
| Molecules | NM28-2746 and NM28-1872 |
| Co-culture | Human PBMCs; E:T 30:1 |
| Measurement | LDH cytotoxicity at 40 hours |
| TCE concentrations | Untreated plus ten concentrations; fivefold dilutions from 50 nM |
| Soluble MSLN used for fitting | 0 and 50 ng/mL |
| Prediction target | All concentrations at 500 ng/mL |

## Reading observed markers rather than source fit lines

Sixty-six mean markers were digitized: two molecules, three conditions and 11 points. Each molecule contributes 22 training points and 11 prediction-evaluation points. Nominal concentrations follow the experimental dilution protocol; vertical pixel coordinates are converted using the zero and 100% axis marks. Smooth source fitted curves are not treated as observations ([original Figure 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC10339761/#f0004)).

The original Figure 4a shows means and SD from one representative experiment of at least two. The original within-condition replicate count is unspecified. The 66 points are aggregate plot markers, not 66 independent donors. Figure 4b summarizes EC50 across experiments and is not treated as the fit to the same individual experimental curve.

Untreated points enter estimation and error calculations. They are omitted only from logarithmic plots because zero cannot be displayed on that axis. Slightly negative marker readings are preserved rather than clipped to zero.

## A model in which soluble antigen changes only EC50

For TCE concentration \(C\) in nM and soluble MSLN \(S\) in ng/mL:

\[
E(C,S)=b+E_{\max}\frac{C^h}{EC_{50}(S)^h+C^h}
\]

\[
EC_{50}(S)=EC_{50}(0)\left(1+\frac{S}{K_{\mathrm{app}}}\right)
\]

Here \(b\) is baseline, \(E_{\max}\) is response amplitude above baseline and \(h\) is the Hill coefficient. EC50 reaches half this amplitude and is distinct from the concentration giving absolute 50% cytotoxicity. \(K_{\mathrm{app}}\), in ng/mL, is an empirical shift scale for this assay, not a KD measured in a binding experiment. The model assumes soluble antigen changes EC50 but not baseline, response amplitude or Hill coefficient.

The comparator holds EC50 common across soluble-antigen conditions. Both models are fitted by equally weighted least squares using only 0 and 50 ng/mL. The 500 ng/mL values enter neither coefficient estimation nor initialization selection. This is retrospective condition-exclusion evaluation with the source figure already visible, not prospectively blinded validation.

## How closely is the 500 ng/mL curve predicted?

![Curves fitted to two lower conditions and predictions at 500 ng/mL](shared/tce-soluble-msln/figures/soluble-antigen-forecast.svg)

Points are observed H226 means. Green includes the soluble-antigen EC50 shift; orange omits it. The lines in the right-hand 500 ng/mL panels are not refitted to those points.

| Molecule | Model | Training-condition RMSE | Prediction RMSE at 500 ng/mL |
| --- | --- | ---: | ---: |
| NM28-2746 | No antigen-dependent shift | 8.16 | 23.74 |
| NM28-2746 | EC50 shift | 3.01 | 4.77 |
| NM28-1872 | No antigen-dependent shift | 10.39 | 24.30 |
| NM28-1872 | EC50 shift | 2.31 | 5.96 |

RMSE is in cytotoxicity percentage points. Including the concentration shift predicted the unused condition more accurately than fitting an averaged baseline and response ceiling without soluble antigen.

| Molecule | EC50(0) | Hill coefficient | Kapp | Predicted EC50(500) |
| --- | ---: | ---: | ---: | ---: |
| NM28-2746 | 0.001033 nM | 0.980 | 11.54 ng/mL | 0.04581 nM |
| NM28-1872 | 0.07296 nM | 1.683 | 8.32 ng/mL | 4.458 nM |

These parameters were fitted at 0 and 50 ng/mL. Describing both molecules with the same form of Kapp equation does not establish a shared binding mechanism or clinical competition mechanism.

## Predicted EC50 still differs from the observed-curve fit

After prediction, independent Hill curves were fitted to each observed condition to obtain descriptive EC50 values for diagnosis. These fits were not fed back into the 500 ng/mL predictions.

![Predicted EC50 and separate descriptive condition fits](shared/tce-soluble-msln/figures/potency-extrapolation.svg)

| Molecule | Predicted EC50 at 500 ng/mL | Descriptive fit at that condition |
| --- | ---: | ---: |
| NM28-2746 | 45.81 pM | 35.46 pM |
| NM28-1872 | 4,458 pM | 2,583 pM |

Lower whole-curve RMSE does not mean the concentration at the middle of the response is reproduced exactly. In particular, a common Hill coefficient and a simple EC50 shift did not fully describe the NM28-1872 curve at 500 ng/mL. Whole-curve error and the location of the response range being considered for concentration setting are distinct quantities.

## Sensitivity to marker reading

Each marker's vertical coordinate was perturbed by a uniform ±1.5 pixels, and fitting and prediction were repeated 100 times. Axis calibration remained fixed.

| Molecule | Prediction RMSE range without shift | Prediction RMSE range with EC50 shift |
| --- | ---: | ---: |
| NM28-2746 | 22.73–24.44 | 3.81–5.76 |
| NM28-1872 | 23.25–25.40 | 5.30–6.91 |

The soluble-antigen model retained its lower error under this reading sensitivity. These ranges are not biological confidence intervals. They do not reproduce the original SD, between-experiment or between-donor variability, or uncertainty in axis calibration. They are not used as virtual-patient distributions.

In these data, ignoring soluble MSLN missed the high-antigen response despite keeping the target cells and culture conditions fixed. The simple extrapolation from 0 and 50 ng/mL also overestimated EC50 to a molecule-dependent extent. Including soluble antigen in a model and transporting its coefficient to another assay or to patients are different operations. The supported prediction here is limited to conditions within this H226 40-hour assay.

## Analysis material

The code contains the original-figure source and hash, observed-marker coordinates, nominal concentration series, estimation, prediction and reading sensitivity. Figures are newly drawn from public observations; original figures are not reproduced. Manuscript values are in `outputs/results.json`; condition-level predictions and every sensitivity calculation are in `outputs/tables/`.

[Analysis code and aggregate outputs](shared/tce-soluble-msln/tce-soluble-msln-analysis.zip)

## References

1. Snell D, Gunde T, Warmuth S, et al. An engineered T-cell engager with selectivity for high mesothelin-expressing cells and activity in the presence of soluble mesothelin. *OncoImmunology*. 2023;12:2233401. [doi:10.1080/2162402X.2023.2233401](https://doi.org/10.1080/2162402X.2023.2233401). Original source: CC BY-NC 4.0. Changes: experimental mean-marker digitization, model fitting, withheld-condition prediction, reading sensitivity and new figures.

## Cite this article

Kumakura D. Predicting a soluble-mesothelin condition withheld from T-cell engager model fitting. Personal research article. 2026. Retrospective reanalysis of public aggregate experimental data.
