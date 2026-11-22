## Abstract {#article-abstract}

Phenobarbital doses for neonates are usually written in mg/kg. In a model-based comparison, I asked whether a weight-based maintenance dose brings more infants into a serum target range than a flat dose or a weight-band dose of the same average size. The data were the routine clinical data of 59 preterm infants (155 serum concentrations) distributed with the R package nlmixr2data, from a 1985 population pharmacokinetic study. The dose column is documented as µg/kg but is not consistent with that unit: the first concentration after the loading dose fell with body weight with a log–log slope of −0.94 (95% confidence interval, CI, −1.13 to −0.74; 35 infants), as expected if the column is a total dose in mg, and that reading gives a volume close to the original report's. Among five pre-specified models, the one with clearance (CL) and volume (V) proportional to weight had the lowest Akaike information criterion (AIC); the model without weight did not converge. Its estimates (CL 0.0047 L/h/kg, V 1.00 L/kg) were close to the original abstract. I simulated the loading dose of 20 mg/kg and the daily maintenance dose of 4 mg/kg of an Australasian neonatal formulary against an assumed target of 15 to 40 mg/L. The mg/kg rule put a median of 85.3% of virtual infants in range 24 h after the loading dose and 99.9% or more after a week, the weight-band rule 81.4% and 99.4%, and a flat dose at the median weight 63.1% and 77.5% (medians over 272 bootstrap fits; parameter uncertainty only). The ranking held at 168 h and for most other targets, variability levels and models, but not at 24 h when the lower target limit was raised to 20 mg/L, where the mg/kg rule fell below the others because its 24 h concentrations lie just above 15 mg/L. The advantage of the mg/kg rule is largely a consequence of the proportional-to-weight model that generates and evaluates the virtual infants, so it is not an independent test of the rules; it also depends on the assumed target and on between-infant variability, which the data estimated with little precision. The results rest on one 1985 cohort and do not recommend a dose.

## Introduction {#article-introduction}

A population pharmacokinetic study of routine clinical data from 59 preterm infants given phenobarbital reported a mean clearance of 0.0047 L/h/kg, a mean volume of distribution of 0.96 L/kg and a half-life of 141 h, with no effect of gestational age, sex, asphyxia or treatment duration on clearance and a 13% larger volume when the 5-minute Apgar score was below 5 ([1](#ref-1)). Those figures are taken from the abstract; I did not read the full report. Current neonatal formularies give the dose per kilogram of body weight. The Australasian Neonatal Medicines Formulary recommends a 20 mg/kg intravenous loading dose, a maintenance dose of 4 mg/kg once daily (3 to 5 mg/kg) starting 24 hours after the loading dose, and a serum target of 15 to 40 mg/L ([2](#ref-2)). A children's hospital clinical pathway gives the same loading dose and a target of 15 to 40 mcg/mL, which is the same unit ([3](#ref-3)). The two documents are not necessarily independent, and I did not find a primary trial that fixes this range, so I treat it as an assumed target and test other ranges.

The question is a decision question about a dosing rule: **for infants like those of this cohort, does a maintenance dose in mg/kg bring a larger share of infants into the target range than a flat dose or a weight-band dose of the same average size, and how much of that difference is uncertain?** A per-kilogram dose is used because phenobarbital clearance and volume change with body weight, and a population model of neonates after congenital heart surgery also uses weight as a covariate on both parameters, with postnatal age as a further covariate on clearance ([4](#ref-4)). What the data of this cohort add is a check of that weight scaling and a measure of how much between-infant variability remains after it. They do not contain infants given the rules compared here, a limit that I come back to below.

## Methods {#article-methods}

### Question of interest and context of use

The question of interest is the one above. The context of use is a research comparison of three dosing rules by simulation from a pharmacokinetic model fitted to routine data. It is not a dosing recommendation: the data are an old observational cohort without clinical outcomes, and the target range is assumed. The model carries the whole comparison, because no infant in the data was given the three rules, so I report what the model implies and where it is uncertain.

### Data and audit

The data are the dataset pheno_sd of the nlmixr2data package, version 2.0.10 ([5](#ref-5)), which lists the sources as the textbook of Pinheiro and Bates, the work of Davidian and Giltinan and the original report ([1](#ref-1), [6](#ref-6)). The file has 744 rows with an infant identifier (ID), time in hours since the first dose (TIME), the recorded dose (AMT), body weight in kg (WT), the 5-minute Apgar score (APGR), the serum concentration in mg/L (DV) and event flags (EVID, 1 for a dose and 0 for an observation). I took the rows with EVID = 1 as doses (589 rows) and those with EVID = 0 as observations (155 rows). I checked that body weight and Apgar score were constant within an infant, that no values were missing, that every infant's first record was a dose at time 0, that no observation preceded the first dose, and that times were increasing and not duplicated. The dataset documentation gives the unit of AMT as µg/kg. For the first concentration observed after the loading dose and before the second dose I regressed log(DV / AMT) on log(WT). If AMT is a total dose, the slope should be −1, and if it is a dose per kilogram, 0. I also summarized the dose per kilogram actually given, its variation within infants, and its relation to weight. The dose was treated as an intravenous bolus given at the recorded time; the duration of the infusion is not recorded. The data file is not redistributed with the companion (see Data and code availability).

### Pharmacokinetic models and selection

The model was a one-compartment model with intravenous bolus doses summed over each infant's recorded dose history, CL and V on the log scale, independent random effects on CL and V, and an additive normal error on the log concentration. Five models were specified before the comparison. M0 had no covariates. M1 had CL ∝ WT^0.75 and V ∝ WT with fixed exponents. M2 had estimated exponents for CL and V. M3 was M1 with an effect of an Apgar score below 5 on CL. M4 had CL ∝ WT and V ∝ WT (proportional to weight). The weights were scaled to the cohort median of 1.3 kg. I fitted them with nlme (the Lindstrom–Bates method ([7](#ref-7)), nlme 3.1-168 ([8](#ref-8)) in R 4.5.3 ([9](#ref-9))). nlme was run so that it stops with an error when it does not converge, and a fit was called converged only when it returned without an error. nlme also warns when the number of observations per infant is smaller than the number of random effects in every infant; that did not apply here, because the infants had 1 to 6 observations and two random effects, and I counted the other warnings (iteration limit, step halving, singular precision matrix). The rule fixed in advance was to choose the lowest AIC and to prefer a simpler model within 2 AIC units. As a check, I computed out-of-fold population predictions (fixed effects only) by 5-fold cross-validation over infants, repeated 5 times (seed 20261125), so that an infant's observations were never used for both fitting and evaluation. After seeing the abstract of the original report, I also fitted a post hoc model M5 with an Apgar score below 5 on V. I also fitted two post hoc models with weight exponents away from proportionality, to see whether the dose-rule comparison depends on the proportional-to-weight assumption: M6 with CL ∝ WT^0.5 and V ∝ WT, and M7 with CL ∝ WT and V ∝ WT^0.8.

### Uncertainty

Parameter uncertainty was assessed by a subject-level bootstrap of the chosen model: 300 resamples of the 59 infants with replacement, each infant keeping its whole dose and observation history, and the fixed effects and random-effect standard deviations (SDs) were saved from each fit that succeeded. Between-infant variability is the random-effect variability inside a fit, and parameter uncertainty is the spread across bootstrap fits; the two are reported separately. The intervals from the bootstrap are conditional on the fits that succeeded.

### Dosing rules and target

Each virtual infant received a loading dose at time 0 and a daily maintenance dose starting at 24 h, as in the formulary ([2](#ref-2)). The mg/kg rule was 20 mg/kg and then 4 mg/kg. The flat rule gave every infant the dose of the cohort median weight (1.3 kg): 26 mg and then 5.2 mg. The weight-band rule used four bands (< 1.0, 1.0 to < 1.5, 1.5 to < 2.5 and ≥ 2.5 kg) with the mg/kg dose at the median weight of the cohort infants in the band. A second flat rule used the cohort mean weight (1.525 kg) as a sensitivity. Virtual infants were drawn with replacement from the weights and Apgar scores of the 59 infants (4,000 per fit, the same infants and random effects for all rules within a fit), and the serum concentration was computed 24 h after the loading dose, just before the first maintenance dose, and 168 h after it, just before the seventh. The outcome was the share of infants with a concentration of 15 to 40 mg/L, with the shares below and above reported as well. Sensitivity analyses used the target ranges of 20 to 40, 10 to 40 and 15 to 30 mg/L, larger assumed between-infant SDs (0.30 and 0.20, 0.40 and 0.30, 0.50 and 0.40 for CL and V; these are assumed values and not estimates from the data) and the other converged models. All seeds are derived from 20261125.

### Further checks

I refitted the chosen model to the observations taken within 72 h of the first dose only, to see whether CL could be estimated before dose adjustments accumulated. I also checked how well the chosen model predicts the observed concentrations: for each observation I simulated the concentration of a new infant with the same weight, Apgar score and dose history (4,000 draws, including the random effects and the residual error) and counted the observations inside the 5th to 95th percentile of the draws. This is an in-sample check on the same observations that were used for fitting; it uses the point estimate of the chosen model, simulates each observation independently (ignoring the correlation of observations within an infant), and does not include parameter uncertainty. I also counted the observed concentrations within 15 to 40 mg/L.

## Results {#article-results}

### Data audit

The dataset had 59 infants, 589 dose records and 155 observations, with 1 to 6 observations per infant (median 3) (Table 1). The values for body weight (0.6 to 3.6 kg, mean 1.525 kg) and the number of infants agree with the cohort described in the abstract of the original report (59 infants, birth weights 600 to 3,620 g, mean 1,520 g) ([1](#ref-1)). That agreement suggests that WT is the birth weight, but the documentation does not say, and weight changes within the first week; I treated WT as constant. Ten infants had an Apgar score below 5.

**Table 1.** Audit of pheno_sd.

| Item | Value |
| --- | --- |
| Rows / infants | 744 / 59 |
| Dose records / observations | 589 / 155 |
| Observations per infant, median (range) | 3 (1–6) |
| Dose records per infant, median (range) | 12 (1–15) |
| Body weight, kg, median (range) | 1.3 (0.6–3.6) |
| 5-minute Apgar score, median (range) | 7 (1–10); 10 infants below 5 |
| First dose (loading), recorded AMT, median (range) | 22.8 (9.5–70) |
| Loading dose per kg (AMT / WT), median (25th–75th percentile; range) | 19.7 (10.0–20.0; 9.5–29.5) |
| Later dose per kg per dose, median (25th–75th percentile; range) | 2.5 (2.47–2.63; 1.9–27.3), given at a median interval of 12 h |
| Infants with later doses / with later doses not all identical | 56 / 26 |
| Slope of log(later AMT) on log(WT) (95% CI) | 0.99 (0.91–1.07) |
| Serum concentration (DV), mg/L, median (range) | 24.6 (6.7–67.9) |
| Observation time since the first dose, h, median (maximum) | 63.5 (389.8) |
| Unit check: slope of log(DV / AMT) on log(WT) (35 infants) | −0.94 (95% CI −1.13 to −0.74) |

The dose column is not consistent with the documented unit of µg/kg and behaved as a total dose (Figure 1A): the slope of −0.94 has a 95% CI that excludes 0 and includes −1. With a total dose in mg, the median concentration per unit dose times weight gave 0.975, a volume of about 1.0 L/kg, which is close to the 0.96 L/kg of the original report ([1](#ref-1)); with µg/kg, the volume implied by the first concentration would be about a thousandth of a litre per kilogram. I therefore treated AMT as the total dose in mg and report the discrepancy with the documentation. I did not check the original source for the unit.

The infants were already dosed close to a per-kilogram scheme. The later doses were 2.5 mg/kg per dose at a median interval of 12 h (25th to 75th percentile 2.47 to 2.63 mg/kg), the loading dose was 19.7 mg/kg (a quarter of the infants had 10 mg/kg or less), and the dose rose in proportion to weight (slope 0.99). The per-kilogram dose therefore varied little between infants, and in 26 of the 56 infants with later doses the later doses were not all identical, so dose adjustments occurred, but the data do not show why.

![Unit check of the dose column and out-of-fold predictions of the chosen model](shared/neonatal-phenobarbital-weight-dosing/figures/figure-1-unit-and-fit.png)

**Figure 1.** (A) The first serum concentration after the loading dose divided by the recorded dose (AMT), by body weight (WT; 35 infants, log axes). The solid line is the fitted slope; the dashed and dotted lines show a slope of −1 (AMT is a total dose) and 0 (AMT is a dose per kg). (B) Out-of-fold population predictions of the chosen model (M4) against observed concentrations over 5 repeats of 5-fold cross-validation over infants (log axes; the grey lines show equality and ±30%). M4, model with CL and V proportional to weight.

### Model comparison and parameter estimates

The model without covariates (M0) did not converge within 200 iterations from either starting point, so it was not compared. None of the full-data fits of M1 to M4 gave a warning. Among the models that converged, M4 had the lowest AIC (−94.2), M2 was 2.3 units higher, M3 2.8 and M1 5.4 higher (Table 2). By the rule fixed in advance M4 was chosen. The estimated exponents of M2 were 1.15 for CL and 0.92 for V, close to proportionality. The Apgar score below 5 on CL (M3) raised CL by 37% (estimate 0.315 on the log scale) without improving the AIC. Cross-validation did not separate the models: the root mean squared error (RMSE) of the log concentration was 0.203 (M1), 0.219 (M2), 0.202 (M3) and 0.210 (M4), with the range over the 5 repeats overlapping (for example 0.197 to 0.216 for M4). Not every cross-validation fit converged (M1 18, M2 23, M3 21 and M4 23 of 25), and the models differ in how many folds were available.

Three post hoc models were fitted for sensitivity. The model with an Apgar score below 5 on V (M5) had an AIC 2.1 units lower than M4 and a 15.8% larger V in these infants (estimate 0.147 on the log scale), close to the 13% in the abstract of the original report ([1](#ref-1)). This closeness is exploratory and not an independent replication: M5 was specified after I had seen that abstract, it rests on 10 infants with an Apgar score below 5, and a 2.1-unit AIC difference is small. The model with CL ∝ WT^0.5 (M6) did not converge, and the model with V ∝ WT^0.8 (M7) converged with an AIC 3.6 units higher than M4.

**Table 2.** Pre-specified models and post hoc models, fitted to the 155 concentrations of 59 infants.

| Model | Structure | Estimated parameters | Converged | AIC | ΔAIC | Cross-validation RMSE (log) | Cross-validation fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M0 | No covariates | 5 | No (200 iterations) | n/a | n/a | n/a | n/a |
| M1 | CL ∝ WT^0.75, V ∝ WT | 5 | Yes | −88.8 | 5.4 | 0.203 | 18/25 |
| M2 | Estimated exponents (CL 1.15, V 0.92) | 7 | Yes | −91.9 | 2.3 | 0.219 | 23/25 |
| M3 | M1 + Apgar < 5 on CL | 6 | Yes | −91.4 | 2.8 | 0.202 | 21/25 |
| M4 | CL ∝ WT, V ∝ WT (chosen) | 5 | Yes | −94.2 | 0 | 0.210 | 23/25 |
| M5 (post hoc) | M4 + Apgar < 5 on V | 6 | Yes | −96.3 | −2.1 | not done | not done |
| M6 (post hoc) | CL ∝ WT^0.5, V ∝ WT | 5 | No (200 iterations) | n/a | n/a | not done | not done |
| M7 (post hoc) | CL ∝ WT, V ∝ WT^0.8 | 5 | Yes | −90.6 | 3.6 | not done | not done |

AIC, Akaike information criterion; RMSE, root mean squared error of the log concentration (population predictions, 5 repeats of 5-fold cross-validation over infants); ΔAIC relative to M4; CL, clearance; V, volume of distribution; WT, body weight. The number of estimated parameters is the number of degrees of freedom of the log-likelihood.

For the chosen model the clearance was 0.0047 L/h/kg and the volume 1.00 L/kg for a 1.3 kg infant, with a half-life of 148 h; the SDs of the random effects were 0.184 on CL and 0.182 on V (coefficients of variation of about 19% and 18%) and the residual SD 0.118 on the log scale (Table 3). These values are close to those in the abstract of the original report ([1](#ref-1)). Of the 300 bootstrap fits, 272 succeeded and 28 failed: 27 reached the limit of 200 iterations without converging and 1 stopped with a numerical error. Three of the 272 successful fits gave a warning, and in 19 the SD of the random effect on CL was estimated at practically zero (below 0.001). The bootstrap 5th to 95th percentile of that SD was 0.0002 to 0.269 and for the SD on V 0.139 to 0.218; between-infant variability, especially of CL, was therefore not identified precisely. The intervals in Table 3 are parameter uncertainty only and are conditional on the 272 successful fits.

**Table 3.** Estimates of the chosen model (M4) and the values in the abstract of the original report ([1](#ref-1)).

| Quantity | This analysis, estimate (bootstrap 5th–95th percentile) | Original report (abstract) |
| --- | --- | --- |
| CL, L/h/kg | 0.0047 (0.0044–0.0051) | 0.0047 (CV 19%) |
| V, L/kg | 1.00 (0.96–1.05) | 0.96 (CV 16%) |
| Half-life, h | 148 (134–160) | 141 |
| SD of random effect on CL | 0.184 (0.0002–0.269) | n/a |
| SD of random effect on V | 0.182 (0.139–0.218) | n/a |
| Residual SD (log scale) | 0.118 (0.100–0.134) | n/a |

CL, clearance; V, volume of distribution; CV, coefficient of variation; SD, standard deviation. The estimates are for the chosen model with weights scaled to 1.3 kg and divided by 1.3. The intervals are conditional on the 272 successful bootstrap fits and reflect parameter uncertainty only.

I tried to refit the chosen model to the 84 observations of 58 infants taken within 72 h of the first dose, but that fit did not converge, so CL could not be estimated from the early observations alone. The predictive check gave 134 of 155 observations (86.5%) inside the 90% predictive interval of a new infant with the same dose history (89.1% of the observations within 48 h and 84.6% after 48 h), slightly less than the nominal 90%. The observed concentrations were within 15 to 40 mg/L in 134 of 155 (86.5%), below 15 mg/L in 15 (9.7%) and above 40 mg/L in 6 (3.9%); the equal count of 134 for the predictive interval and for the target range is a coincidence, and the two checks measure different things; these infants received doses that were close to 2.5 mg/kg every 12 h and are not a test of the rules compared below.

### Comparison of dosing rules

Across the bootstrap fits the mg/kg rule put a median of 85.3% of infants in the range of 15 to 40 mg/L 24 h after the loading dose (5th to 95th percentile of the fits 76.0% to 94.6%) and a median of 100.0% (99.6% to 100.0%) 168 h after it (Table 4, Figure 2A). The weight-band rule gave 81.4% (73.6% to 89.1%) and 99.4% (98.0% to 99.9%), the flat rule at the median weight 63.1% (59.0% to 67.0%) and 77.5% (75.4% to 79.0%). The medians over bootstrap fits differ slightly from the point-estimate values in Table 5 (for example 85.3% against 84.7% for the mg/kg rule at 24 h). The mg/kg rule exceeded the flat rule by 22.2 percentage points at 24 h (5th to 95th percentile of the paired differences 16.7 to 27.6) and by 22.5 (21.0 to 24.1) at 168 h in every bootstrap fit. The weight-band rule was lower than the mg/kg rule by 3.8 percentage points at 24 h (−5.9 to −1.8) and by 0.6 (−1.6 to −0.1) at 168 h. At 24 h the shortfall of the mg/kg rule was entirely below the range (14.7%): the geometric mean concentration was 17.7 mg/L, close to the lower limit. The geometric coefficient of variation of the concentration was 0.16 with the mg/kg rule and 0.45 with the flat rule. The flat rule set at the cohort mean weight had 73.0% and 72.7%; it moved infants from below to above the range, with 15.8% above 40 mg/L at 168 h, and did not remove the difference.

**Table 4.** Share of virtual infants (%) with a serum phenobarbital concentration below, within and above 15–40 mg/L (median over 272 successful bootstrap fits, with the 5th to 95th percentile for the share within; parameter uncertainty only).

| Rule | Time | Below | Within | Above |
| --- | --- | --- | --- | --- |
| mg/kg | 24 h | 14.7 | 85.3 (76.0–94.6) | 0.0 |
| Weight band | 24 h | 18.6 | 81.4 (73.6–89.1) | 0.0 |
| Flat, 1.3 kg dose | 24 h | 35.8 | 63.1 (59.0–67.0) | 1.1 |
| Flat, 1.525 kg dose | 24 h | 23.7 | 73.0 (70.0–75.8) | 3.3 |
| mg/kg | 168 h | 0.0 | 100.0 (99.6–100.0) | 0.0 |
| Weight band | 168 h | 0.1 | 99.4 (98.0–99.9) | 0.5 |
| Flat, 1.3 kg dose | 168 h | 14.9 | 77.5 (75.4–79.0) | 7.5 |
| Flat, 1.525 kg dose | 168 h | 11.4 | 72.7 (69.4–75.4) | 15.8 |

The flat rule had a low share within range at the extremes of weight (Figure 2B). At 168 h it had 47.2% within range among infants under 1.0 kg (52.8% above 40 mg/L), 98.9% at 1.0 to under 1.5 kg, 92.1% at 1.5 to under 2.5 kg and 3.0% at 2.5 kg or more (97.0% below 15 mg/L); the mg/kg and weight-band rules had at least 96.9% within range in every band at that time. These by-band results come from the point estimate of the chosen model and resample the infants of each band (8, 29, 14 and 8 infants in the four bands).

![Share of virtual infants within 15 to 40 mg/L by dosing rule, overall and by weight band](shared/neonatal-phenobarbital-weight-dosing/figures/figure-2-attainment.png)

**Figure 2.** (A) Share of virtual infants within 15 to 40 mg/L for the mg/kg, weight-band and flat rules at 24 h and 168 h after the loading dose; points are the median and bars the 5th to 95th percentile over 272 successful bootstrap fits (parameter uncertainty only). (B) The same share by weight band for the point estimate of the chosen model.

### Sensitivity of the comparison

The ranking of mg/kg, weight-band and flat rules held at 168 h in every scenario of Table 5, and at 24 h in every scenario but one. At 24 h with a target of 20 to 40 mg/L the ranking reversed: the mg/kg rule had 22.8% within range (77.2% below), the weight-band rule 30.2% and the flat rule 33.0%, because the geometric mean concentration of the mg/kg rule at 24 h was 17.7 mg/L, below the new lower limit. At 168 h with that target the mg/kg rule had 95.9%, the band rule 90.8% and the flat rule 62.5%. With larger assumed variability the shares of every rule fell: at 168 h the mg/kg rule had 98.7%, 92.5% and 83.4% for the assumed SD pairs of 0.30 and 0.20, 0.40 and 0.30, and 0.50 and 0.40, and the flat rule 73.6%, 69.2% and 64.3%. The advantage of the mg/kg rule over the flat rule at 168 h did not shrink steadily: it was 22.6 percentage points for the estimated variability (point estimates), 25.1 for the first assumed pair, 23.4 for the second and 19.1 for the third. Across the models M1 to M5 and M7 the mg/kg rule had 82.0% to 85.7% within range at 24 h and 99.5% to 100.0% at 168 h, and the flat rule 62.6% to 64.8% and 76.2% to 82.6%; with V ∝ WT^0.8 (M7) the advantage of the mg/kg rule over the flat rule was 18.0 points at 24 h and 20.0 at 168 h.

These sensitivity analyses are weak evidence of robustness. Every model in Table 5 makes both CL and V depend strongly on weight, and the rules are evaluated in virtual infants generated by the same model, so a dose in mg/kg gives similar concentrations at all weights in these models by construction. The analyses show that the result does not hinge on one set of exponents, the variability or the target (except the lower limit at 24 h), not that the dependence on weight is correct.

**Table 5.** Share (%) of virtual infants within the target range by sensitivity scenario (point estimates; between-infant variability only; the first three columns are at 24 h and the last three at 168 h).

| Scenario | mg/kg 24 h | Band 24 h | Flat 24 h | mg/kg 168 h | Band 168 h | Flat 168 h |
| --- | --- | --- | --- | --- | --- | --- |
| Primary (M4, 15–40 mg/L) | 84.7 | 80.9 | 62.6 | 100.0 | 99.3 | 77.4 |
| Target 20–40 mg/L | 22.8 | 30.2 | 33.0 | 95.9 | 90.8 | 62.5 |
| Target 10–40 mg/L | 100.0 | 99.9 | 84.7 | 100.0 | 99.3 | 87.2 |
| Target 15–30 mg/L | 84.6 | 80.3 | 57.4 | 91.4 | 81.5 | 57.2 |
| Assumed SDs 0.30 and 0.20 | 82.7 | 79.5 | 61.2 | 98.7 | 96.5 | 73.6 |
| Assumed SDs 0.40 and 0.30 | 73.1 | 72.0 | 57.6 | 92.5 | 89.9 | 69.2 |
| Assumed SDs 0.50 and 0.40 | 66.5 | 65.4 | 53.7 | 83.4 | 80.9 | 64.3 |
| Model M1 | 84.9 | 81.4 | 63.2 | 99.8 | 99.4 | 80.8 |
| Model M2 | 84.8 | 81.5 | 63.4 | 100.0 | 99.1 | 76.2 |
| Model M3 | 85.7 | 82.3 | 64.3 | 99.5 | 99.4 | 82.6 |
| Model M5 (post hoc) | 84.8 | 81.6 | 64.8 | 100.0 | 99.4 | 78.3 |
| Model M7 (post hoc, V ∝ WT^0.8) | 82.0 | 80.2 | 64.0 | 99.9 | 99.3 | 79.9 |

## Discussion {#article-discussion}

The comparison of dosing rules is close to a restatement of the weight scaling that the data support, and its main result is circular in part. With CL and V both proportional to weight (the model with the lowest AIC, estimated exponents of 1.15 and 0.92 in the more flexible model, and a first concentration that fell with weight as a total dose should), a dose in mg/kg gives the same concentration in infants of every weight, apart from between-infant variability. The same model then generates and evaluates the virtual infants, so the advantage of the mg/kg rule is the proportional-to-weight assumption restated, and it is not an independent test of the rules. What the simulation adds is the size of the loss when that scaling is true: a flat dose lost about 22 percentage points of the share within 15 to 40 mg/L, and nearly all of it for infants of 2.5 kg or more, while a four-band dose lost 0.6 to 3.8 points. Under this model, a weight-band dose approximates the mg/kg dose closely, and its small loss comes from using the band's median weight for infants whose weight differs from it. The percentage points also depend on the dose chosen as the flat reference: a flat dose set at the mean weight moved infants from below to above the range.

The data do not contain what would test this assumption. The infants were dosed at close to 2.5 mg/kg every 12 h, with a per-kilogram dose that varied little between infants and a total dose that rose in proportion to weight (slope 0.99). Weight and dose were therefore almost collinear, the weight dependence of CL and V is informed by how concentrations at a nearly constant dose per kilogram vary with weight, and the behaviour of a flat or band dose is an extrapolation by the model to dose–weight combinations that were not given. The exponent models did not discriminate well (AIC differences of 2.3 to 3.6 units, overlapping cross-validation), and one model with a lower V exponent (M7) reduced the advantage of the mg/kg rule from about 22 to 20 points at 168 h and to 18 at 24 h (the model with the lower CL exponent, M6, did not converge, so only the V side of the weight assumption could be tested). Part of the dosing was adjusted for reasons that the data do not show (26 of 56 infants had later doses that were not all identical); if doses were adjusted according to concentrations, the estimates of CL and V could be biased in a direction and by an amount that I cannot tell, and the refit to the early observations that I attempted did not converge.

The share within range of the mg/kg rule depended on the assumed between-infant variability, which the data estimated with little precision. The random-effect SDs were about 0.18, in agreement with the coefficients of variation of the original abstract, but the bootstrap interval of the SD on CL included practically zero, and the predictive check had 86.5% of the observations inside the 90% interval, slightly less than nominal. Under the estimated variability the mg/kg rule reached 99.9% or more at one week; with SDs of 0.50 and 0.40 it reached 83.4%. The ranking of the rules was stable at 168 h, but the size of the advantage was not monotone in the variability (22.6, 25.1, 23.4 and 19.1 points), and the ranking reversed at 24 h when the lower limit of the target was 20 mg/L: the 24 h concentration of a 20 mg/kg loading dose sits just above 15 mg/L, so the 24 h shares are sensitive to where the range begins. The 100% at one week also ignores the increase of clearance with postnatal age that a cohort of neonates after cardiac surgery reported ([4](#ref-4)), and is optimistic for that reason.

Model selection did not decide the matter. The AIC favoured the proportional model by 2.3 to 5.4 units over the others, cross-validation did not distinguish the models, and the Apgar effect was inconclusive: the effect on CL that I specified in advance did not improve the AIC, while the post hoc effect on V of the same direction as the original abstract's had an AIC 2.1 units lower with a size near the reported 13%, which I read as exploratory because it rests on 10 infants and on a model chosen after reading that abstract. It did not change the rule comparison (Table 5).

### Limitations

- **Cohort and data.** One 1985 single-centre observational cohort of 59 preterm infants given routine care. The assay methods, the care of neonates (for example therapeutic hypothermia and the way doses are given) and co-medication differ from today's, and the data have no co-medication, asphyxia or hypothermia covariates, and no postnatal age or gestational age. Maturation of clearance, which a study in neonates after cardiac surgery reports ([4](#ref-4)), could not be modelled, so the 168 h results may be too favourable for infants whose clearance rises during the first week.
- **Dose and weight.** The unit of the dose column differs from its documentation, and the reading as a total dose rests on the check in Figure 1A and on the volume, not on the original source. It is not known whether WT is the birth weight or the weight at dosing. Doses were close to a per-kilogram scheme and may have been adjusted according to concentrations (26 of 56 infants had non-identical later doses), which can bias the estimates in a direction and by an amount I do not know, and the dose–weight collinearity limits what the data say about weight dependence; the early-observation refit did not converge. Infusion durations are not recorded: doses were treated as bolus doses, whereas a slow infusion over 15 to 30 minutes is likely, with a small effect on the 24 h and 168 h concentrations.
- **Model.** Random effects were independent and normal on the log scale, without a correlation of CL and V; with 1 to 6 observations per infant, two random effects are weakly identified (19 bootstrap fits had an SD of practically zero), and the SDs were estimated imprecisely. The model without covariates, the model with CL ∝ WT^0.5 and 28 of 300 bootstrap fits did not converge, and the cross-validation comparison used different numbers of folds for the models. The results of the 19 bootstrap fits at the boundary were kept. The post hoc models were specified after seeing the original abstract (M5) or to test the weight assumption (M6 and M7).
- **Simulation.** The 24 h and 168 h concentrations are model predictions in virtual infants given the three rules; the infants were resampled from the weights and Apgar scores of the 59 infants, and the by-band results rest on 8 to 29 infants per band. The bootstrap intervals are parameter uncertainty only and are conditional on the 272 successful fits. The median over bootstrap fits (85.3%) and the point estimate (84.7%) differ slightly for the mg/kg rule at 24 h.
- **Target.** The target range of 15 to 40 mg/L is that of two clinical documents that are not necessarily independent. A concentration within range is not seizure control, safety was not evaluated, and the shares at 24 h depend strongly on where the lower limit of the range lies.
- **References.** The accounts of the original report and of the other references are from their abstracts or web pages only, and I did not verify the formulary and the pathway against a primary trial.

## Conclusion {#article-conclusion}

In a one-compartment model fitted to the 155 concentrations of 59 preterm infants, with clearance and volume proportional to weight, a phenobarbital maintenance dose in mg/kg put a median of 85.3% of virtual infants in the range of 15 to 40 mg/L at 24 h and 99.9% or more at one week, a four-band dose 81.4% and 99.4%, and a flat dose at the median weight 63.1% and 77.5%; the flat dose lost about 22 percentage points and had a low share within range at weights of 2.5 kg and above. This advantage follows from the weight proportionality of the model that generated the infants, was not monotone in the assumed variability, and reversed at 24 h when the lower target limit was set at 20 mg/L. Parameter uncertainty spread the share of the mg/kg rule at 24 h over 18.6 percentage points (5th to 95th percentile width, 76.0% to 94.6%). The conclusion is limited to this model and cohort; it does not say which dose to give to an infant, and it does not address efficacy, safety, age-related changes in clearance or doses adjusted to concentrations.

## Data and code availability {#reproduce}

The data are not redistributed with this article. The companion contains the scripts (`common.R`, `rules_lib.R`, `01_audit.R`, `02_fit.R`, `02b_apgar_v.R`, `03_bootstrap.R`, `04_rules.R`, `05_extra.R`, `figures.R`), the aggregate results (`results/*.csv`, without the observation-level cross-validation predictions) and the session information, together with a `README.md` that gives the steps for obtaining the data: download `nlmixr2data_2.0.10.tar.gz` from CRAN (SHA-256 8555db27117eac430a97ea984c0d7eed2277aedaddc7e39eb3d943527ccb6650), extract `data/pheno_sd.rda` into the folder `_download/nlmixr2data/data/` beside the scripts, and read it with `load()`; the package is not installed. The package is listed on CRAN under the GPL (version 3 or later), but I did not check the rights to the original data and therefore did not include them. The seed is 20261125 (about 5 minutes for `02_fit.R` and for `03_bootstrap.R` with 8 worker processes; the other scripts take seconds to a few minutes). R 4.5.3, nlme 3.1-168 and, for the figures, ggplot2 4.0.4 are required; the numbers in the tables can be checked against `results/*.csv`.

[Download the companion: code and aggregate results](shared/neonatal-phenobarbital-weight-dosing/neonatal-phenobarbital-weight-dosing-companion.zip)

## References {#article-references}

1. <span id="ref-1"></span>Grasela TH Jr, Donn SM. Neonatal population pharmacokinetics of phenobarbital derived from routine clinical data. Dev Pharmacol Ther. 1985;8(6):374–383. [doi:10.1159/000457062](https://doi.org/10.1159/000457062)
2. <span id="ref-2"></span>ANMF consensus group. Phenobarbital (Phenobarbitone), newborn use only [Internet]. Australasian Neonatal Medicines Formulary; 2021 [cited 2026 Nov 19]. Available from: [ANMF phenobarbital monograph (PDF)](https://www.seslhd.health.nsw.gov.au/sites/default/files/groups/Royal_Hospital_for_Women/Neonatal/Neomed/neomed21phenobarbital.pdf)
3. <span id="ref-3"></span>Children's Hospital of Philadelphia. Neonatal seizure/status epilepticus clinical pathway – N/IICU – anti-seizure medications (ASM) [Internet]. Children's Hospital of Philadelphia; ©2026 [cited 2026 Nov 19]. Publication date not stated. Available from: [CHOP clinical pathway](https://www.chop.edu/clinical-pathway/neonatal-seizure-status-epilepticus-anti-seizure-medications-asm)
4. <span id="ref-4"></span>Thibault C, Massey SL, Naim MY, Abend NS, Zuppa AF. Population pharmacokinetics of IV phenobarbital in neonates after congenital heart surgery. Pediatr Crit Care Med. 2020;21(8):e557–e565. [doi:10.1097/PCC.0000000000002341](https://doi.org/10.1097/PCC.0000000000002341)
5. <span id="ref-5"></span>Fidler M, Schoemaker R, Baron K, Wendling T, Grasella T, Weil C, et al. nlmixr2data: datasets for nlmixr2 [Dataset]. CRAN; 2026. Version 2.0.10 (published 2026 Jul 10) [cited 2026 Nov 19]. Author names as listed in the package DESCRIPTION. Available from: [CRAN](https://cran.r-project.org/package=nlmixr2data)
6. <span id="ref-6"></span>Pinheiro JC, Bates DM. Mixed-effects models in S and S-PLUS [Book]. New York: Springer-Verlag; 2000. [doi:10.1007/b98882](https://doi.org/10.1007/b98882)
7. <span id="ref-7"></span>Lindstrom MJ, Bates DM. Nonlinear mixed effects models for repeated measures data. Biometrics. 1990;46(3):673–687. [doi:10.2307/2532087](https://doi.org/10.2307/2532087)
8. <span id="ref-8"></span>Pinheiro J, Bates D, R Core Team. nlme: linear and nonlinear mixed effects models [Software]. 2025. Version 3.1-168. [CRAN](https://CRAN.R-project.org/package=nlme)
9. <span id="ref-9"></span>R Core Team. R: A language and environment for statistical computing [Software]. Vienna: R Foundation for Statistical Computing; 2026. Version 4.5.3. [R Project](https://www.r-project.org/)
