Reference date: the facts in this article reflect public information as of 5 November 2026.

Setidegrasib (ASP3082) degrades KRAS G12D together with its protein. In mouse xenografts, KRAS G12D degradation continued after the plasma concentration fell below the in vitro DC50 (the concentration giving half of the maximal degradation), and once-weekly dosing shrank tumors ([1](#ref-1)). In the human phase 1 trial, 10–800 mg was given intravenously (IV) once weekly, and 600 mg was selected as the phase 2 dose ([2](#ref-2)). For a degrader whose effect lasts until the target is resynthesized, the dosing interval cannot be set by plasma half-life alone. From the published numbers of the original paper, this article computes which of the elements that set this interval public data can determine and which they cannot. No public human data were used to calibrate the model or to choose a structure.

## Abstract

Mouse plasma and tumor concentrations ([Figure 4a of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4)) were described by a two-compartment plasma model and saturable tumor elimination. KRAS G12D degradation ([Figure 4b of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4)) fitted equally well when driven by the tumor concentration or by the plasma concentration (log-scale root mean square error, RMSE, 0.518 and 0.527; difference in Akaike information criterion, AIC, 1.3). The two structures differ in the assumed target turnover: the KRAS half-life was about 8.8 h with the tumor driver and about 130 h with the plasma driver. For both, the RMSE was about 1.4 times the replicate log standard deviation (SD, 0.378) of the 10 and 30 mg/kg groups, and the lack of fit was significant (F test, p = 0.0009 and 0.0007).

For tumor growth ([Figure 4c of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4)), the model was estimated from the vehicle and the 10 and 30 mg/kg groups only, and the 0.3, 1 and 3 mg/kg groups were predicted. The tumor-driven structure predicted the day-21 mean volumes at 0.94, 1.12 and 1.52 times the observations (additive kill, AIC −344.6), and the plasma-driven structure at 0.56, 0.51 and 0.72 times (growth modulation, AIC −318.7). A baseline that set the kill rate by dose alone without PK/PD, with the onset aligned to the first dose, gave a similar 0.92, 1.08 and 1.43 times (AIC −331.8). In six other xenograft models, both structures overpredicted the effect (median predicted/observed 0.51 over 14 groups; no observation fell inside the prediction band). Both structures predicted the observed direction, BIW better than QW, in all six models, but BIW carries twice the total dose of QW, so the direction does not discriminate between structures. The size of the difference (natural-log difference 0.14–0.62 observed) was 0.04–0.09 under the tumor-driven structure and 0.10–0.22 under the plasma-driven structure, small in both.

At the same 30 mg/kg per week, the ranking of QW (once weekly), BIW (twice weekly) and Q2W (once every two weeks) depended on the choice of structure. Under the tumor-driven structure the trough degradation stayed within 0.915–0.940 and QW and Q2W differed by 0.003–0.004. Under the plasma-driven structure QW and Q2W differed by 0.19–0.46 and the order was fixed as BIW, QW, Q2W. Human extrapolation remained a conditional scenario with an assumed allometric exponent and target turnover. The published abstract of the human phase 1 trial contains no exposure or degradation values, so the only quantities that could be set against predictions were the dose range and the selected dose.

## Introduction

Setidegrasib brings KRAS G12D and the E3 ligase VHL (von Hippel-Lindau protein) together so that the proteasome pathway degrades KRAS G12D ([1](#ref-1)). A KRAS G12D inhibitor, MRTX1133, has been reported ([3](#ref-3)). For a drug that blocks function, inhibition is generally expected to return when binding to the target is lost. With a degrader, the effect may last until the target is resynthesized. The times relevant to the dosing interval therefore divide into five: elimination from plasma, uptake into and retention in the tumor, degradation and resynthesis of the target, recovery of signaling, and tumor growth.

Yoshinari et al. reported mouse plasma, tumor and pancreas concentrations, the amount of KRAS G12D in tumors, and once-weekly and twice-weekly dosing in several tumor models ([1](#ref-1), [Figures 4 and 5 of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4)). The paper states that, when plasma protein binding is taken into account, the unbound concentration in the tumor appears not to reach an effective level, which makes the PK/PD (pharmacokinetic/pharmacodynamic) relationship hard to explain ([1](#ref-1)). The aim here is to integrate these numbers into one model and to answer three questions by computation.

1. Which structure explains the gap between falling plasma concentration and recovering degradation?
2. How far does a model calibrated on single doses predict untrained doses, dosing intervals and tumor models?
3. What does the ranking of QW (once weekly), BIW (twice weekly) and Q2W (once every two weeks) depend on?

This is not a study that determines the clinically optimal dose. It examines the predictive performance and identifiability of a model on public data. Only mouse data were used for calibration.

## Methods

### Data used and scope

The data used are listed in Table 1. Numbers were taken only from the tables of Supplementary Data 3 ([Source Data](https://static-content.springer.com/esm/art%3A10.1038%2Fs42004-025-01662-4/MediaObjects/42004_2025_1662_MOESM5_ESM.xlsx)) of the original paper, and none were read off figures ([1](#ref-1)).

Table 1. Data used. PK: pharmacokinetics; IV: intravenous; QW: once weekly; BIW: twice weekly; PDX: patient-derived xenograft.

| Use | Original figure | Content |
| --- | --- | --- |
| PK | [Figure 4a](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4) | PK-59 xenograft mice, single IV dose of 10 or 30 mg/kg; plasma, tumor and pancreas at 2, 6, 24, 48, 72 and 144 h (3 animals per time point) |
| Degradation | [Figure 4b](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4) | Tumor KRAS G12D normalized to β-actin, relative to the vehicle mean at each time (3 animals per time point) |
| Tumor growth | [Figure 4c](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4) | Vehicle and 0.3, 1, 3, 10, 30 mg/kg dosed on days 1, 8 and 14; tumor volume on days 0–21 (5 animals per group) |
| Other tumor models | [Figure 5a](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig5) and [Supplementary Figure 7a](https://static-content.springer.com/esm/art%3A10.1038%2Fs42004-025-01662-4/MediaObjects/42004_2025_1662_MOESM1_ESM.pdf) | AsPC-1, GP2d, HPAC, KP-4, GP5d, PK-1 xenografts; 30 mg/kg QW (days 1, 8) or BIW (days 1, 5, 8, 12; PK-1 days 1, 4, 8, 11); up to day 14 (5 animals per group) |
| Other tumor models | [Figure 5b](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig5) | Patient-derived xenograft (PDX) LXFA1125; 10 or 30 mg/kg BIW (days 1, 5, 8, 12, 15, 19); up to day 22 (8 animals per group) |

Six cell-line-derived xenograft (CDX) models and one PDX were used. [Figure 4a of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4) publishes individual values for each animal rather than means. The three animals of the 10 mg/kg plasma group at 144 h were below the limit of quantification (recorded as 0) and were excluded from the PK fit.

For human data, only the abstract of the phase 1 paper ([2](#ref-2)) and the trial registrations ([4](#ref-4), [5](#ref-5)) were checked. The full text of the NEJM paper was not read. The quantitative values in the abstract are the dose range (10–800 mg, once weekly, intravenous), the phase 2 dose (600 mg), and a partial response of 36% among 45 patients with non-small-cell lung cancer (NSCLC) at 600 mg, and contain no plasma concentration, degradation or signaling values ([2](#ref-2)). No report of a quantitative systems pharmacology model or dose prediction for setidegrasib by the developer was found in a standard web search on 5 November 2026; this was not an exhaustive search of literature databases. As for development status, the phase 1 trial is recruiting ([4](#ref-4)) and a phase 3 trial against docetaxel in NSCLC is recruiting ([5](#ref-5)).

### Model structure

The structure is shown in Figure 1.

![Figure 1: model structure](shared/setidegrasib-translational-pkpd/figures/fig1_model_structure.png)

Figure 1. Structure of the model in this article: intravenous bolus into plasma (A1, A2), tumor concentration (Ct), ratio of KRAS G12D (r) and tumor volume (V). The structural alternatives compared (the driver of degradation being the tumor or plasma concentration, and the effect being additive kill or growth modulation) are shown at the bottom.

Plasma was a two-compartment intravenous bolus, and the tumor took up drug from the plasma concentration and eliminated it in a saturable way. Amounts per body weight were used, and 1 mg/kg was converted to 1,000 ng/g body weight (concentration units ng/mL and ng/g). \(A_1\) and \(A_2\) are the amounts in the central and peripheral compartments (ng/g body weight), \(V_1\) is the central volume of distribution (L/kg), \(k_{10}\) is elimination and \(k_{12}\) and \(k_{21}\) are inter-compartment rate constants (1/h), \(k_{in}\) is the rate constant of uptake from plasma into the tumor (1/h), \(V_m\) is the maximal elimination rate in the tumor (ng/g/h) and \(K_m\) is its half-saturation concentration (ng/g).

\[\frac{dA_1}{dt}=-(k_{10}+k_{12})A_1+k_{21}A_2,\qquad \frac{dA_2}{dt}=k_{12}A_1-k_{21}A_2,\qquad C_p=\frac{A_1}{V_1}\]

\[\frac{dC_t}{dt}=k_{in}C_p-\frac{V_m C_t}{K_m+C_t}\]

The amount of KRAS G12D was expressed as the ratio \(r=R/R_0\) to its steady state without drug, and the degradation fraction as \(D=1-r\). \(k_{deg}\) is the rate constant of resynthesis and natural turnover (1/h), \(k_{max}\) is the maximal drug-induced degradation rate (1/h) and \(DC_{50}\) is the driving concentration giving half of it. For the driving concentration \(C_{drv}\) of degradation, two structures were used: the tumor concentration \(C_t\) and the plasma concentration \(C_p\).

\[\frac{dr}{dt}=k_{deg}(1-r)-\frac{k_{max}C_{drv}}{DC_{50}+C_{drv}}\,r\]

The Hill coefficient was fixed at 1. When it was freed, kmax and DC50 diverged individually under the tumor-driven structure (Hill coefficient 0.88, AIC −39.5), so it was not identifiable. Tumor volume followed Gompertz growth (growth rate \(k_g\), 1/h; carrying capacity \(K\), mm³) with two forms of effect: additive kill (coefficient \(s_1\), 1/h) and modulation of the growth rate (the growth term multiplied by \(1-cD\), with a dimensionless coefficient \(c\); regression is possible for \(c>1\)).

\[\frac{dV}{dt}=k_g V\ln\frac{K}{V}-s_1 D V\quad\text{or}\quad \frac{dV}{dt}=k_g V\ln\frac{K}{V}\,(1-cD)\]

The unbound plasma fraction (0.00784 in mice ([1](#ref-1))) was not used in the fit. Unbound drug concentrations in tumors were not measured, so the driving concentration is treated as an apparent driving concentration and is not equated with an intracellular unbound concentration.

### Order of estimation

The order in which data were used was fixed. (i) The seven PK parameters were estimated from plasma and tumor concentrations ([Figure 4a of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4), 69 observations). (ii) With PK fixed, kdeg, kmax and DC50 were estimated from KRAS degradation ([Figure 4b of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4), 36 observations). (iii) Growth parameters were estimated from the vehicle group of each tumor model. (iv) One effect parameter was estimated from the vehicle and 10 and 30 mg/kg groups of [Figure 4c of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4) (90 observations). (v) The 0.3, 1 and 3 mg/kg groups and the other tumor models were predicted. The objective was the sum of squared log-scale residuals, with equal weight per data point. AIC was \(n\ln(\mathrm{RSS}/n)+2k\) (\(n\) observations, \(k\) estimated parameters, RSS the residual sum of squares) and RMSE was \(\sqrt{\mathrm{RSS}/n}\), both from log residuals. Because each stage fixes the estimates of the previous one, upstream uncertainty does not propagate downstream.

Uncertainty was expressed by drawing 60 sets of PK and PD parameters from a Laplace approximation (a normal approximation on the log scale, truncated at ±2 on the log scale from the mean) and re-estimating the effect parameter in each set on tumor data resampled by animal with replacement. These are conditional parameter scenarios; they do not reproduce the variability of a patient population and do not include the tumor growth rate, between-animal variability or observation error. Because the KRAS turnover rate kdeg is weakly identified, it was evaluated by profile likelihood (kdeg fixed, the other parameters re-estimated, the range with a deviance increase of 3.84 or less taken as an approximate 95% interval).

For prediction in other tumor models, the PK and PD parameters of PK-59 were fixed and the growth of each tumor model was approximated by exponential growth of its vehicle group (because the Gompertz carrying capacity is not determined in the short observation periods). Comparison used the ratio to day-0 volume, which removes differences in initial volume between groups.

## Results

### Falling plasma and intratumoral retention

Plasma fell quickly, with means of 14.9 ng/mL at 24 h in the 10 mg/kg group and 56.3 ng/mL in the 30 mg/kg group. The in vitro DC50 (38 nM, a value given in the [legend of Figure 4a of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4)) corresponds to about 42 ng/mL with a molecular weight of about 1,117 g/mol of the neutral molecule, derived in this article from the [M+H]⁺ composition C60H66FN12O7S (m/z 1117.4877) given in the supplementary information. Tumor concentrations fell far more slowly than plasma: 223 ng/g at 24 h and 120 ng/g at 144 h in the 10 mg/kg group, and 1,117 ng/g and 781 ng/g in the 30 mg/kg group. KRAS G12D fell at 24 h to a mean of 18% of the vehicle group at 10 mg/kg (individual values 13, 20, 21%) and 7% at 30 mg/kg (6, 6, 9%), and returned at 144 h to 65% (56, 68, 71%) and 37% (45, 46, 20%), respectively.

The PK model fitted the 69 plasma and tumor observations from two doses with a log-scale RMSE of 0.396 (Figure 2). The parameters were \(V_1\) 1.11 L/kg, \(k_{10}\) 0.585 /h, \(k_{12}\) 0.0301 /h, \(k_{21}\) 0.0273 /h, \(k_{in}\) 0.0249 /h, \(V_m\) 4.73 ng/g/h and \(K_m\) 286 ng/g, and the terminal half-life of the two-compartment model was about 27 h. The log standard errors of \(V_m\) and \(K_m\) were 0.68 and 1.12, so the degree of saturation is determined only roughly. The low-concentration limit of the saturable version (\(V_m/K_m\) = 0.0165 /h) corresponds to a tumor elimination half-life of about 42 h. A version with linear tumor elimination had an elimination rate constant of 0.00836 /h (half-life about 83 h), RMSE 0.423 and AIC −106.8, which was 7.2 worse than the saturable version (AIC −114.0).

![Figure 2: mouse PK](shared/setidegrasib-translational-pkpd/figures/fig2_pk_fit.png)

Figure 2. Plasma, tumor and pancreas concentrations in PK-59 xenograft mice (individual values of the Source Data of [Figure 4a of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4), replotted; 10 mg/kg in blue and 30 mg/kg in orange) and the fit of the model in this article (lines). The pancreas was not modelled. Plasma at 10 mg/kg and 144 h was below quantification and is not plotted.

### Which structure explains the recovery of degradation

The tumor-driven structure gave kdeg 0.0784 /h (KRAS half-life 8.8 h), kmax 3.24 /h and DC50 4,741 ng/g, with RMSE 0.518 and AIC −41.4. The plasma-driven structure gave kdeg 0.00532 /h (half-life 130 h), kmax 0.272 /h and DC50 185 ng/mL, with RMSE 0.527 and AIC −40.1 (Figure 3). The difference is only 1.3 in AIC. The replicate log SD within each dose and time (within-group variability) was 0.212 in the vehicle group and 0.378 in the 10 and 30 mg/kg groups. The RMSE of both structures is about 1.4 times the SD of the 10 and 30 mg/kg groups (1.37 and 1.39), so a lack of fit remains that replicate variability does not explain (F test, 9 and 24 degrees of freedom, F = 4.84 and 5.11, p = 0.0009 and 0.0007). Neither follows the non-monotonic changes at 24, 48 and 72 h.

The tumor-driven DC50 (4,741 ng/g) is higher than the observed tumor concentrations (up to 1,690 ng/g), so under this structure only the low-concentration-limit ratio kmax/DC50 (6.8×10⁻⁴ /(ng/g)/h) is determined. With interpolation, the profile interval of kdeg was 0.044–0.160 /h (half-life 4.3–15.6 h) for the tumor driver and 0.043 /h or lower (half-life 16.0 h or longer) for the plasma driver, whose lower end remained open even at the lower limit of the search range (0.002 /h). The two intervals meet at about 0.044 /h. The KRAS turnover rate cannot be determined without deciding what drives degradation.

![Figure 3: KRAS degradation](shared/setidegrasib-translational-pkpd/figures/fig3_kras_degradation.png)

Figure 3. Left: individual values of the Figure 4b Source Data of the original paper (% of the vehicle mean) and the fits of the tumor-driven (solid) and plasma-driven (dashed) structures. Middle: fitted plasma and tumor concentrations; the grey line is the conversion of the in vitro DC50 of 38 nM (about 42 ng/mL). Right: increase in deviance when the KRAS half-life (\(\ln 2/k_{deg}\)) is fixed and the other parameters are re-estimated; the dashed line is the approximate 95% threshold (3.84).

### Prediction at untrained doses

Gompertz growth fitted the vehicle group better than exponential growth (PK-59, AIC −135.6 versus −101.1). The effect parameter was estimated from the vehicle and 10 and 30 mg/kg groups, and the 0.3, 1 and 3 mg/kg groups were predicted (Table 2). Twelve combinations were fitted: 2 drivers, 2 growth forms (Gompertz and exponential) and 3 effect forms (additive kill, growth modulation, Emax). In all four Emax (maximal-effect) fits, D50 reached the upper search bound of 5.0, and they were worse than additive kill. Table 2 shows four combinations and the baseline without PK/PD. The baseline set the kill rate by dose alone (two parameters, the maximal kill rate smax and the half-effect dose d50) and applied it at a constant rate from 24 h after the start of the study (the first dose on day 1).

Table 2. Prediction performance for tumor volume (Gompertz growth).

| Structure | Effect | Training AIC (n = 90) | Predicted/observed, 0.3 mg/kg | 1 mg/kg | 3 mg/kg |
| --- | --- | --- | --- | --- | --- |
| Tumor-driven | Additive kill | −344.6 | 0.94 | 1.12 | 1.52 |
| Tumor-driven | Growth modulation | −300.9 | 0.99 | 1.32 | 2.13 |
| Plasma-driven | Growth modulation | −318.7 | 0.56 | 0.51 | 0.72 |
| Plasma-driven | Additive kill | −273.9 | 0.40 | 0.35 | 0.56 |
| No PK/PD (constant kill rate) | Not applicable | −331.8 | 0.92 | 1.08 | 1.43 |

Note: predicted/observed is the ratio of mean volumes on day 21. AIC: Akaike information criterion. No PK/PD: the kill rate set by dose alone and applied at a constant rate from 24 h after the start of the study. Observed means were 1,818 mm³ at 0.3 mg/kg, 1,194 mm³ at 1 mg/kg and 496 mm³ at 3 mg/kg.

In the training fit, tumor-driven additive kill was best (AIC −344.6), 12.8 better than the baseline without PK/PD (−331.8). At untrained doses, tumor-driven additive kill came within about 12% of the observation at 0.3 and 1 mg/kg and underestimated the effect at 3 mg/kg (1.52 times; the predicted volume was too large). The plasma-driven structure gave 0.35–0.72 times and overestimated the effect in all three groups. Among growth-modulation fits, however, the plasma-driven structure is better both in training AIC (−318.7 versus −300.9) and at 3 mg/kg (0.72 versus 2.13 times). The untrained-dose predictions of the baseline (0.92, 1.08 and 1.43 times) are comparable to tumor-driven additive kill (0.94, 1.12 and 1.52 times), so the untrained-dose predictions did not show an advantage of linking effect to PK/PD. The baseline model cannot represent differences between dosing intervals. Figure 4 shows predictions and observations.

![Figure 4: tumor growth](shared/setidegrasib-translational-pkpd/figures/fig4_tumor_growth.png)

Figure 4. Tumor volume in the PK-59 model (points are means of 5 animals per group), with the fit of the tumor-driven structure (solid: vehicle, 10 and 30 mg/kg) and predictions (dashed: 0.3, 1 and 3 mg/kg). Left: growth modulation; right: additive kill. Dotted lines mark dosing days.

### Other tumor models and the QW–BIW comparison

PK and PD parameters were fixed, and 30 mg/kg QW and BIW (10 and 30 mg/kg BIW for the PDX) were predicted in six other xenograft models and the PDX. Over the 14 groups, the median of the predicted volume ratio (relative to day 0) was 0.51 times the observation (growth modulation, tumor-driven; range 0.29–1.16). The prediction was smaller than observed (effect overestimated) in 13 groups, and no group had its observation inside the band made from the 60 parameter sets (Figure 5). The band expresses parameter uncertainty only and is not a prediction interval. With additive kill, the effect was overestimated in all 14 groups, with a median of 0.34 times.

![Figure 5: external prediction](shared/setidegrasib-translational-pkpd/figures/fig4b_external_prediction.png)

Figure 5. Predictions (lines) and observations (points) in other tumor models. The vertical axis is the mean ratio to each animal's day-0 volume (log scale) and the band is the 5th–95th percentile range over 60 sets of PK and PD parameters. Drawn for the tumor-driven structure with growth modulation and exponential growth.

In all six observed xenografts, the end-point volume ratio was smaller for BIW than for QW (natural-log difference 0.14–0.62). The tumor-driven and plasma-driven structures both predicted this direction in all six models (Table 3). Because BIW carries twice the total dose of QW, any model in which the effect rises monotonically with dose predicts this direction regardless of structure. Agreement in direction does not discriminate between structures. The size of the difference was smaller than observed under both structures (the plasma-driven prediction is larger than the tumor-driven one).

Table 3. Difference in the natural log of the end-point (day 14) volume ratio between 30 mg/kg QW and BIW, ln(QW/BIW).

| Tumor model | Observed | Tumor-driven | Plasma-driven | Tumor-driven, QW-recalibrated | Plasma-driven, QW-recalibrated |
| --- | --- | --- | --- | --- | --- |
| AsPC-1 | 0.62 | 0.04 | 0.10 | 0.03 | 0.08 |
| GP2d | 0.36 | 0.06 | 0.16 | 0.04 | 0.12 |
| HPAC | 0.44 | 0.09 | 0.22 | 0.04 | 0.11 |
| KP-4 | 0.14 | 0.08 | 0.21 | 0.03 | 0.08 |
| GP5d | 0.21 | 0.07 | 0.18 | 0.04 | 0.12 |
| PK-1 | 0.47 | 0.08 | 0.19 | 0.04 | 0.11 |

Note: growth modulation, exponential growth. Positive means BIW is smaller. "QW-recalibrated" is the value when the potency c was re-estimated from the QW group of each tumor model alone and BIW was predicted; it removes the error from carrying potency over from PK-59 to other tumor models.

Even with potency re-estimated from the QW group alone, the difference was 0.03–0.04 (tumor-driven) and 0.08–0.12 (plasma-driven), short of the observed 0.14–0.62. The observed differences therefore contain a part that is not explained by the PK and PD transferred from PK-59 or by the structure of the effect. Under the tumor-driven structure, degradation is saturated at 0.92–0.96, so re-estimating potency from the QW group alone is not expected to produce a difference. Moving every dosing day one day earlier (a sensitivity on the dosing clock) did not change the best combination (tumor-driven additive kill) or the 6/6 direction (its AIC changed from −344.6 to −323.8; for Gompertz growth modulation, the AIC order of the tumor-driven and plasma-driven structures swapped).

### What the ranking of dosing intervals depends on

QW 30, BIW 15 and Q2W 60 mg/kg, which equalize the weekly dose at 30 mg/kg, were simulated for 56 days and the minimum of the degradation D over days 28–56 (the trough) was compared (Figure 6). Under the tumor-driven structure, the point estimates were 0.924, 0.926 and 0.920, within 0.006 of each other. Across the 60 draws, the medians of the trough for QW 30, BIW 15 and Q2W 60 were 0.902, 0.906 and 0.885, and only the 5th percentile of Q2W 60 widened, to 0.762. For 30 mg/kg per dose at QW, BIW and Q2W, the troughs were 0.924, 0.959 and 0.656, so Q2W fell lowest among intervals with the same dose per administration.

![Figure 6: by dosing interval](shared/setidegrasib-translational-pkpd/figures/fig5_regimens.png)

Figure 6. 56-day simulation (point estimates; horizontal axis in days) of QW 30, BIW 15 and Q2W 60 mg/kg, which equalize the weekly dose at 30 mg/kg. Top: tumor-driven; bottom: plasma-driven. From the left: plasma concentration, tumor concentration and KRAS degradation D.

To examine the effect of the unidentifiable kdeg, the ranking was compared over the whole profile range of kdeg (Figure 7). Under the tumor-driven structure, inside the approximate 95% interval (deviance of 3.84 or less), the troughs of the three regimens stayed within 0.915–0.940 and QW and Q2W differed by 0.003–0.004. Under the plasma-driven structure they spread out as BIW 0.73–0.85, QW 0.49–0.75 and Q2W 0.05–0.56, QW and Q2W differed by 0.19–0.46 (point estimate 0.30), and the order was fixed as BIW, QW, Q2W. The choice of structure determined the ranking, and the uncertainty of kdeg mattered less.

Within the tumor-driven structure, across the 60 parameter sets, the difference between the Q2W and QW troughs depended strongly on the tumor elimination parameters \(V_m\) (Spearman ρ = −0.97) and \(K_m\) (−0.93). These two are determined by the late phase of the tumor concentration in [Figure 4a of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4) (log SE 0.68 and 1.12). For the three equal-intensity regimens of 30 mg/kg per week, the simulated tumor concentration peaked at 4,047–4,821 ng/g (point estimates) and 7,278 ng/g (maximum over 60 sets), 2.4–4.3 times the largest training observation (1,690 ng/g), and this extrapolation was not validated (12,697 ng/g, about 7.5 times, for BIW 30 mg/kg, i.e. 60 mg/kg per week). In 23 of the 60 sets, kmax or DC50 lies at the edge of the truncation range on the log scale.

![Figure 7: sensitivity](shared/setidegrasib-translational-pkpd/figures/fig7_uncertainty_sensitivity.png)

Figure 7. Left and middle: trough degradation of the three regimens as the KRAS half-life (\(\ln 2/k_{deg}\)) is varied (points are the search grid). Right: Spearman correlation between parameters and the difference between the Q2W 60 and QW 30 troughs across the 60 draws under the tumor-driven structure.

Drawing the fraction of time with degradation of 0.9 or more during days 42–84 on a surface of dose per administration (5–90 mg/kg) and interval (3.5–21 days) (Figure 8), the tumor-driven structure reached 0.9 or more at 10 mg/kg or more for a 3.5-day interval, 20 mg/kg or more for 7 days, 45 mg/kg or more for 14 days and 90 mg/kg for 21 days (0.86 at 60 mg/kg for 21 days). The plasma-driven structure reached at most 0.96 (90 mg/kg, 3.5-day interval) and 0.43 or less for intervals of 7 days or longer.

![Figure 8: response surface](shared/setidegrasib-translational-pkpd/figures/fig6_response_surface.png)

Figure 8. Fraction of time with degradation of 0.9 or more during days 42–84, by dose per administration and dosing interval (point estimates). Left: tumor-driven; right: plasma-driven.

### Human extrapolation scenarios

Public human data were not used for calibration. With body-surface-area dose conversion (factors 3 for mouse and 37 for human ([6](#ref-6))), the mouse doses of 10 and 30 mg/kg correspond to about 57 mg and 170 mg for a 70 kg human. The 600 mg selected as the phase 2 dose is about 3.5 times the converted amount for the 30 mg/kg group (about 170 mg). This conversion follows the logic of a starting dose for toxicity and is not a prediction of exposure.

For the extrapolation of exposure, the assumptions were: clearance-type rate constants scaled by BW^(b−1) (BW is body weight, 70 kg for humans and 0.025 kg for the mouse; b = 0.67, 0.75, 0.85 and 1.0), volume of distribution per kg and the tumor saturation constant unchanged, and PD parameters unchanged. These are assumptions, not estimates. The extrapolation used the tumor-driven structure only. With b = 0.75, the trough degradation at 600 mg once weekly was 0.857, and 0.787–0.880 when b was varied over 0.67–0.85 and kdeg over both ends of the tumor-driven profile interval. With b = 1.0 (no scaling) it fell to 0.37–0.46. At 100 mg it was 0.40–0.54 (b = 0.67–0.75), a strong dose dependence (Figure 9).

![Figure 9: human scenarios](shared/setidegrasib-translational-pkpd/figures/fig8_human_scenarios.png)

Figure 9. Conditional scenarios for human extrapolation (not observations). Predicted trough degradation in weeks 4–6 with once-weekly intravenous dosing. The grey band is the tested dose range (10–800 mg) and the dashed line is 600 mg. Left: kdeg at the point estimate; right: at the lower end of the profile interval. A body weight of 70 kg is assumed.

The published abstract ([2](#ref-2)) contains no plasma concentration, degradation or signaling values, so a figure setting predictions against observations could not be made. The extrapolation predicts a dose dependence of degradation inside the tested dose range, but where the effect saturates depended strongly on the assumed scaling exponent.

## Discussion

That degradation continued after plasma fell below the in vitro DC50 could be explained with similar accuracy by retention of drug in the tumor alone (elimination half-life about 42 h) or by slow resynthesis of KRAS alone (half-life 130 h). The 36 observations of [Figure 4b of the original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12375097/#Fig4) hold too little information to separate the two. In addition, both structures leave a residual that replicate variability does not explain (RMSE about 1.4 times the SD of the 10 and 30 mg/kg groups, p < 0.001) and do not explain the behavior at 24, 48 and 72 h. At this quality of fit, the difference between structures cannot be concluded.

The untrained predictions gave limited information on this question. The volumes at untrained doses in the same PK-59 model were predicted closer by the tumor-driven structure than by the plasma-driven structure with additive kill (the tumor-driven structure was also off by 1.52 times at 3 mg/kg). With growth modulation the plasma-driven structure had the better training AIC and the better 3 mg/kg prediction, and the baseline without PK/PD predicted comparably. In other tumor models, both structures overestimated the effect and underestimated the size of the QW–BIW difference. This failure cannot be separated into the use of the PK-59 PK in other tumor models, differing potency between tumors, and an erroneous structure. Because re-estimating potency from the QW group alone did not close the gap, carrying potency over cannot be the whole explanation, but there is also no basis to conclude that the structure is wrong. Elements not examined include target-mediated elimination, delay of the effect (an effect compartment), indirect response of downstream signaling (such as phosphorylated ERK, pERK) and differences in drug distribution with tumor size.

That the ranking of dosing intervals depends on structure has practical implications. The difference between the QW trough and the Q2W trough is 0.003–0.004 under the tumor-driven structure and 0.19–0.46 under the plasma-driven structure, so which structure is right changes the basis for extending the interval. The observed BIW–QW difference (0.14–0.62) exceeds the predictions of both structures in five of six models, and the plasma-driven prediction looks closer only because it is larger (in KP-4 the plasma-driven prediction of 0.21 exceeds the observed 0.14). A structure cannot be chosen from this difference. Deciding requires time courses of intratumoral KRAS after repeated dosing and intratumoral concentrations at several dosing intervals.

## Limitations

PK and KRAS amounts come from one xenograft model (PK-59), two doses, and destructive measurements of 3 animals per time point, not time series within an individual. Figures 4a and 4b of the original paper use different animals. The terminal PK phase reached the limit of quantification in the 10 mg/kg plasma group, and only three points remain even including 2.2 ng/mL at 144 h in the 30 mg/kg group. The tumor-driven DC50 lies outside the observed range, and the Hill coefficient could not be identified. In the tumor-volume predictions, repeated measurements of the same animal were treated as independent points and the estimates were fixed stage by stage. The parameter bands do not include structural uncertainty, differences of potency between tumor models or between-animal variability. For the external tumor models, the PK of PK-59 was assumed and PK in each model was not measured. The external predictions concern data not used for training, but they come from the same paper and the same research group, and are not verification by independent researchers. The human scaling exponent and the target turnover assumption cannot be verified.

The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

The mouse data for setidegrasib explained the continuation of degradation after plasma fell equally well by intratumoral drug retention or by slow target resynthesis (AIC difference 1.3). For untrained doses in the same tumor model, tumor-driven additive kill gave the best training fit, but the baseline without PK/PD predicted comparably, and in other tumor models both structures overestimated the effect and underestimated the QW–BIW difference. The ranking of QW, BIW and Q2W depended on the choice of structure and was not determined by public data. Human public data were not used for calibration, and the abstract holds no exposure values, so the comparison of predictions with observations was limited to confirming the dose range. Separating drug retention from target turnover, which an optimization of the dosing interval requires, needs additional data such as time courses of intratumoral KRAS after repeated dosing.

## Data and code availability

Inputs are taken from Supplementary Data 3 (Source Data) of the original paper. Because the original paper is published under CC BY-NC-ND, the extracted numerical tables and the intermediate tables that contain individual values or summaries of the observed values beyond those printed in the article are not included in the package; the retrieval procedure and the extraction code (`extract_inputs.py`) are provided. Figures 2, 3, 4 and 5 replot individual or summarized values of this Source Data. The SHA-256 of the workbook is 941c00c6…cbb1. The model (`model.py`), estimation, validation and simulation (`analysis.py`, `stages_extra.py`, `stages_sens.py`, `stages_checks.py`), figure generation (`figures.py`), tests (`test_analysis.py`, 10 tests), result CSV/JSON files and figures are in the companion ZIP. The random seed is 20261105, and the analysis runs with Python 3.12, NumPy, SciPy, pandas and matplotlib. A full rerun takes roughly 11–15 minutes.

[Download the analysis code, results and figures](shared/setidegrasib-translational-pkpd/setidegrasib-translational-pkpd-companion.zip)

The full re-run materials are in the [companion archive](shared/setidegrasib-translational-pkpd/setidegrasib-translational-pkpd-companion.zip).


## References

<span id="ref-1"></span>1. Yoshinari T, Nagashima T, Ishioka H, Inamura K, Nishizono Y, Tasaki M, et al. Discovery of KRAS(G12D) selective degrader ASP3082. Commun Chem. 2025;8(1):254. [https://doi.org/10.1038/s42004-025-01662-4](https://doi.org/10.1038/s42004-025-01662-4)
<span id="ref-2"></span>2. Park W, Kasi A, Spira AI, Paz-Ares Rodríguez L, Herzberg BO, Pelster MS, et al. Setidegrasib in advanced non-small-cell lung cancer and pancreatic cancer. N Engl J Med. 2026;394(14):1409–1420. [https://doi.org/10.1056/NEJMoa2600752](https://doi.org/10.1056/NEJMoa2600752). Abstract only was read.
<span id="ref-3"></span>3. Hallin J, Bowcut V, Calinisan A, Briere DM, Hargis L, Engstrom LD, et al. Anti-tumor efficacy of a potent and selective non-covalent KRASG12D inhibitor. Nat Med. 2022;28(10):2171–2182. [https://doi.org/10.1038/s41591-022-02007-7](https://doi.org/10.1038/s41591-022-02007-7)
<span id="ref-4"></span>4. Astellas Pharma Inc. A Phase 1 Study of ASP3082 in Participants With Locally Advanced or Metastatic Solid Tumor Malignancies With KRAS G12D Mutation (NCT05382559) [Internet]. ClinicalTrials.gov; record updated 2026 Oct 14 [cited 2026 Nov 5]. Available from: [https://clinicaltrials.gov/study/NCT05382559](https://clinicaltrials.gov/study/NCT05382559)
<span id="ref-5"></span>5. Astellas Pharma Global Development Inc. A Randomized, Open-label, Phase 3 Study of Setidegrasib (ASP3082) versus Docetaxel (jRCT2031260120) [Internet]. Japan Registry of Clinical Trials; registered 2026 May 14, updated 2026 Oct 7 [cited 2026 Nov 5]. Available from: [https://jrct.mhlw.go.jp/en-latest-detail/jRCT2031260120](https://jrct.mhlw.go.jp/en-latest-detail/jRCT2031260120)
<span id="ref-6"></span>6. Nair AB, Jacob S. A simple practice guide for dose conversion between animals and human. J Basic Clin Pharm. 2016;7(2):27–31. [https://doi.org/10.4103/0976-0105.177703](https://doi.org/10.4103/0976-0105.177703)
