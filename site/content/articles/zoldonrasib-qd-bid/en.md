Zoldonrasib (RMC-9805) is an oral RAS(ON) inhibitor targeting KRAS G12D. Phase 1 evaluates 150–1200 mg once daily (QD) and 300–600 mg twice daily (BID), with 1200 mg QD selected as a candidate phase 2 dose. AACR 2026 provides an updated clinical report ([1](#ref-1)).

How much would peak and predose concentrations change if 1200 mg were split into two 600 mg doses? The available inputs are mean QD PK curves and a statement of comparable AUC for QD and BID at equal daily dose. The materials used here do not contain measured BID concentration–time profiles.

I digitized five mean QD curves, fitted a small model and predicted BID. The principal comparison gives a peak ratio near 0.50 and a predose-concentration ratio near 3.4. The latter depends strongly on model structure and dosing interval. Neither is a clinically validated BID result.

## Question and intended use

The question is how peak, predose concentration and 24-hour AUC change after equal-daily-dose fractionation from QD to 12-hourly BID. The main comparison is 1200 QD versus 600 BID, with 900 QD versus 450 BID and 600 QD versus 300 BID as additional comparisons; doses are mg.

This public aggregate-data analysis examines conditions and measurements for a comparative PK study. It does not determine clinical dosing, efficacy, safety superiority or equivalence. Ctrough here is concentration immediately before the next dose. With absorption lag, concentration can fall further after administration before rising, so it differs from the strict minimum over 24 hours.

## Available curves and missing information

PK inputs come from page 8 of the public AACR 2025 presentation. Updated clinical results in 2026 are not mixed in as PK observations from another time ([2](#ref-2); [original presentation](https://www.revmed.com/wp-content/uploads/2025/04/AACR-2025-Zoldon-Corporate-Rev.pdf)).

Table 1. Information available and its use in this analysis.

| Material | Content | Use |
| --- | --- | --- |
| Cycle 1 Day 15 mean QD curves | 150, 300, 600, 900 and 1200 mg; whole-blood nM; SD error bars | Fit 5 doses × 9 times |
| QD AUC distributions | Boxes and individual points for 600, 900 and 1200 mg | Convert interquartile widths into a conditional variability scale |
| QD–BID AUC comparison | Footnote states comparable exposure at equal daily dose | Qualitative consistency only |
| Mean BID profiles | Not supplied in these materials | No external validation of BID shape |
| PK-group counts and individual series | Not specified in the figure | No estimation of mean sampling error or patient-level NLME |

Images were extracted and calibrated against axis marks. Times are 0.5, 1, 1.5, 2, 2.5, 4, 6, 8 and 24 hours. Overlapping markers were enlarged and read manually, with uncertain points flagged. Predose zero-hour points overlap the axis and were excluded; the 24-hour value substitutes under steady-state assumptions. Overlays against the source were checked. Digitization and rounded figures do not provide original-data precision.

Whole-blood nM is retained throughout without conversion to plasma, unbound or tumor concentration. No individual PK records were obtained.

## Model and estimation

The two-compartment model uses first-order absorption with a lag. Amount states are Ag, Ac and Ap:

\[
\dot A_g=-k_a A_g,
\]
\[
\dot A_c=k_a A_g-\frac{CL_*+Q_*}{V_*}A_c+\frac{Q_*}{V_{p*}}A_p,
\qquad
\dot A_p=\frac{Q_*}{V_*}A_c-\frac{Q_*}{V_{p*}}A_p,
\]
\[
C(t)=A_c(t)/V_*.
\]

At tlag after each administration, D f(D) enters Ag. D is mg and f(600)=1. The dose-specific f is an empirical input scale. Between-group background and clearance differences may also affect amplitudes, so f does not identify true bioavailability differences.

Amounts in mg are linked to output in nM without using molecular weight. Thus CL* and Q* have units mg/(nM·h), and V* and Vp* have units mg/nM. They contain a conversion scale and are not physiological apparent clearances in L/h or volumes in L. They parameterize rates and concentration predictions.

Table 2. Estimated shared coefficients and conversion-scale units.

| Shared coefficient | Estimate | Unit |
| --- | ---: | --- |
| CL* | 0.11254 | mg/(nM·h) |
| V* | 0.18942 | mg/nM |
| Q* | 0.02485 | mg/(nM·h) |
| Vp* | 0.13203 | mg/nM |
| ka | 0.7680 | /h |
| tlag | 0.3137 | h |

QD doses are superposed for 15 days, and the following objective is minimized over 45 points:

\[
\sum_{D,t}\{\log C_{\mathrm{model}}(D,t)-\log\bar C_{\mathrm{obs}}(D,t)\}^2
\]

Fitting logarithms does not change the arithmetic-mean origin of the inputs. The curve is not identified as population median or typical-patient PK. SD error bars are not used as independent precision weights for the means.

Table 3. Dose-specific empirical input scales.

| Dose D (mg) | Estimated input scale f(D) |
| --- | ---: |
| 150 | 0.433 |
| 300 | 1.050 |
| 600 | 1.000 |
| 900 | 1.136 |
| 1200 | 1.042 |

The 450 mg scale is interpolated linearly between 300 and 600 mg on log D and log f. Transport to BID assumes unchanged absorption shape and input scale for the same per-administration dose.

## Mean QD description remains weak near the trough

![Mean QD points and model fit; outlined points were read manually from overlaps](shared/zoldonrasib-qd-bid/figures/01-qd-fit.png)

Figure 1. Fits to aggregate mean curves, not patient prediction intervals.

Log-residual RMSE is 0.201. The two-compartment fit is better than first-order one-compartment absorption, with a reference pseudo-AIC difference of 43.3. Because this calculation assumes independent errors for correlated aggregate time points, it is not rigorous model-selection evidence.

Fast- and slow-phase half-lives are approximately 0.90 and 4.76 hours. ka is close to the fast distribution rate, making absorption and distribution difficult to separate. Coefficients should not be interpreted as identified drug-specific mechanisms. The flat prepeak shape at 150 mg is also inadequately represented.

At 1200 mg, model AUC24 is approximately 11,107 nM·h versus 13,148 from trapezoidal integration of public mean points, approximately 16% lower. Its proximity to the box-plot median, approximately 10,846 nM·h, does not establish reproduction of the mean curve. Integrals of mean points, median individual AUC and model integrals are distinct statistics. The discrepancy is not assigned to outliers or intentional median fitting.

I additionally excluded all 900 mg observations and interpolated its input scale from remaining doses.

Table 4. Held-out 900 mg dose-group check.

| Metric at 900 mg | From public mean points | Prediction with group omitted | Relative discrepancy |
| --- | ---: | ---: | ---: |
| AUC24 (nM·h) | 10,182 | 8,182 | −19.6% |
| Maximum of mean curve (nM) | 2,180 | 1,871 | −14.2% |
| 24 h concentration (nM) | 17.77 | 12.89 | −27.5% |

This checks an unused QD dose group, not BID prediction. The late concentration discrepancy and absence of intermediate observations between 8 and 24 hours remain weaknesses for 450 mg interpolation and interval changes.

## Fractionation changes peaks and predose concentrations

![Baseline-model QD and predicted BID concentration profiles](shared/zoldonrasib-qd-bid/figures/02-qd-vs-bid.png)

Figure 2. Model curves before adding conditional individual variability. They are not identified typical-patient profiles, and BID curves are predictions rather than observations.

Table 5. BID/QD exposure ratios at equal daily dose with conditional residual-sensitivity ranges.

| Regimen change (mg) | Cmax ratio | Ctrough ratio | AUC24 ratio |
| --- | ---: | ---: | ---: |
| 1200 QD → 600 BID | 0.496 (0.407–0.596) | 3.417 (1.730–4.650) | 0.960 (0.794–1.155) |
| 900 QD → 450 BID | 0.464 (0.392–0.537) | 3.198 (1.674–4.331) | 0.898 (0.763–1.047) |
| 600 QD → 300 BID | 0.542 (0.449–0.647) | 3.737 (1.926–5.002) | 1.050 (0.871–1.259) |

Point estimates are baseline-model ratios; parentheses are 2.5th–97.5th percentiles from 1,000 residual-resampling runs. They are not clinical 95% confidence intervals. Counts behind the means and temporal correlations are unknown, so resampling describes sensitivity under assumed residual errors. It does not resample patients or fully encompass digitization and structural uncertainty.

![Ratios and conditional residual-resampling sensitivity ranges](shared/zoldonrasib-qd-bid/figures/03-ratios.png)

Figure 3. Lines indicate conditional sensitivity ranges, not probabilities that peaks decrease in actual patients.

For 1200 QD versus 600 BID, baseline peak concentration roughly halves and predose concentration rises approximately 3.4-fold. AUC ratio 0.96 is largely determined by f(600)/f(1200), a consequence of input scales and linear mass balance rather than clinical equivalence. It is compatible with the presentation’s footnote, but measurements, sample sizes and comparison intervals are unavailable for quantitative validation. Applying boundaries such as 0.8 and 1.25 to these ranges does not establish clinical equivalence or superiority.

## Conditional individuals and structural sensitivity

Log interquartile widths from three dose-group AUC boxes are averaged to assume log SD=0.457 for CL* alone. The same random draws are assigned to 4,096 paired QD/BID individuals:

\[
CL_{*,i}=CL_*\exp(\eta_i),\qquad\eta_i\sim N(0,\sigma^2).
\]

This is neither individual-data NLME estimation nor a reconstruction of the actual population. Adding variation around a mean-curve model need not preserve its original mean. Absolute concentration percentiles are therefore not presented as clinical population forecasts; conditional within-person ratios are the focus.

For 1200 QD versus 600 BID, the Ctrough-ratio 5th–95th percentile range is approximately 2.38–4.29, arising from CL*-only variability rather than coefficient uncertainty. Near-constant AUC ratios around 0.96 follow from shared input scales and linearity. Allowing ka variability in 1,024 paired draws gives a median Ctrough ratio near 3.5.

Table 6. Structural, digitization and dosing-interval sensitivity for 1200 QD versus 600 BID.

| Setting | Cmax ratio | Ctrough ratio | AUC24 ratio |
| --- | ---: | ---: | ---: |
| Main analysis | 0.496 | 3.417 | 0.960 |
| Omit overlapping-marker points | 0.424 | 2.857 | 0.821 |
| Set all dose input scales to 1 | 0.517 | 3.559 | 1.000 |
| First-order absorption, 1-compartment | 0.516 | 7.340 | 0.960 |
| BID at 8/16-hour intervals | 0.514 | 2.030 | 0.960 |

The 8/16-hour result uses the smaller of two predose concentrations, not the global minimum. The one-compartment fit is poorer, so its roughly sevenfold trough ratio should not receive equal weight. Peak reduction has the same direction in tested scenarios, but BID absorption remains unmeasured and even that direction is not empirically guaranteed.

## Measured BID profiles remain unvalidated

Describing mean 1200 mg QD does not validate 600 mg BID. Predictions transport assumptions about input, food, formulation and time-dependent PK. The 450 mg BID prediction also interpolates an unmeasured per-dose input scale.

Tolerability, efficacy, target occupancy and effect thresholds are not evaluated, and monotherapy curves are not transported to combination exposure. Without checking BID predictions against measured profiles, clinical advantages of fractionation cannot be established.

## Data and code availability

The [companion archive](shared/zoldonrasib-qd-bid/zoldonrasib-qd-bid-companion.zip) supplies digitized CSV files, model, resampling, conditional-individual and plotting code. Original PDFs and figure images are not redistributed. The public PDF is needed only to repeat digitization; included CSV files suffice to rerun analysis and figures.

Closed-form calculations are compared with an independent differential-equation solver, with additional checks of AUC mass balance, interpolation and synthetic-data recovery. These are implementation tests rather than clinical validation of BID prediction. Inputs and model assumptions were checked on 23 October 2026. The trial is registered as [NCT06040541](https://clinicaltrials.gov/study/NCT06040541) ([3](#ref-3)); this analysis does not use its individual participant records.

## References {#references}

<span id="ref-1"></span>
1. Riess J, Haura EB, Yaeger R, Johnson M, Luo J, Parikh AR, et al. Abstract CT021: preliminary safety and clinical activity of zoldonrasib (RMC-9805), an oral, RAS(ON) G12D-selective, tri-complex inhibitor in patients with previously treated KRAS G12D non-small cell lung cancer (NSCLC). Cancer Research. 2026;86(8 Supplement):CT021. [doi:10.1158/1538-7445.AM2026-CT021](https://doi.org/10.1158/1538-7445.AM2026-CT021).

<span id="ref-2"></span>
2. Arbour KC, Tanvetyanon T, Yaeger R, Parikh AR, Oberstein P, Papadopoulos KP, et al. Preliminary safety and antitumor activity of zoldonrasib (RMC-9805), an oral, RAS(ON) G12D-selective, tri-complex inhibitor in patients with KRAS G12D non-small cell lung cancer (NSCLC) from a phase 1 study in advanced solid tumors. AACR Annual Meeting 2025 presentation. Page 8; data cutoff 2 December 2024. [Presentation](https://www.revmed.com/wp-content/uploads/2025/04/AACR-2025-Zoldon-Corporate-Rev.pdf).

<span id="ref-3"></span>
3. ClinicalTrials.gov. Study of RMC-9805 in participants with KRAS G12D-mutant solid tumors. NCT06040541. [Trial record](https://clinicaltrials.gov/study/NCT06040541).
