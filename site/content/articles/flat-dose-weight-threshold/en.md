Reference date: the facts in this article reflect public information as of 5 November 2026.

日本語版: [フラット用量に体重の閾値はあるか](https://daikikumakura.github.io/writing/flat-dose-weight-threshold.html)

## Abstract

We computed the body weight at which the exposure of flat dosing (the same dose for every patient regardless of weight) departs from a reference, using the weight exponent \(b\) of clearance (CL) reported by population pharmacokinetic (PK) models. A weight threshold was defined, not as a clinical boundary, but as the weight at which the exposure ratio to that of the reference-weight patient equals \(1\pm\delta\) (\(\delta\) is the tolerated relative difference; 0.1, 0.2 and 0.3 were computed). Nine antibodies whose exponent and reference weight could be confirmed in the text or tables of the primary source were analysed: pembrolizumab, nivolumab, atezolizumab, durvalumab, avelumab, tislelizumab, cemiplimab, dostarlimab and ipilimumab. The exponent \(b\) ranged from 0.324 to 0.694.

The weight band in which exposure stays within ±20% of the reference (ratio 0.8–1.2) was 40–62 kg (light side) to 96–141 kg (heavy side) for flat dosing, and 39–51 kg to 93–145 kg for mg/kg dosing. All ±20% limits lay inside the minimum and maximum weights of the source populations for the seven antibodies whose weight range could be obtained, but the range was not available for three antibodies, and the density of the data was not confirmed. The variance of log exposure (AUC or average concentration) due to weight alone is \(b^2\sigma^2\) for flat dosing and \((1-b)^2\sigma^2\) for mg/kg dosing, and the two are equal at \(b=0.5\). The point estimate of \(b\) was below 0.5 for four antibodies; the probability that \(b<0.5\) from the standard error alone was 1.00 for avelumab, 0.99 for durvalumab, 0.85 for dostarlimab and 0.66 for cemiplimab. The 95% interval of a threshold from the uncertainty of \(b\) alone was widest for avelumab (126–168 kg, heavy side of flat dosing) and narrowest for ipilimumab (107–114 kg). In a one-compartment approximation of the trough (pre-dose concentration), the heavy-side limit for all nine antibodies fell 2–13 kg (at the interval of the source regimen) below the limit based on the area under the concentration-time curve (AUC). The results are conditional on the power model, the reported exponents and the assumed weight distributions, and a difference in exposure does not mean a difference in efficacy.

## Introduction

Whether an antibody is dosed in proportion to body weight (mg/kg) or as a flat dose is commonly explained by the weight exponent of CL in population PK models. The population PK analysis of tislelizumab states that exposure is similar for flat and mg/kg dosing when the exponent is below or near 0.5, and that of dostarlimab states that flat dosing gives smaller AUC variability when the exponent is below 0.5 ([1](#ref-1), [2](#ref-2)). The question "above what weight does flat dosing become unfavourable?" needs a definition of a threshold in addition to the exponent.

This site already has an article ([3](#ref-3)) and a reference page ([4](#ref-4)) that applied published pembrolizumab and nivolumab models to an adult weight distribution. There, the lower limit was the 5th percentile of the trough of the weight-based reference regimen, and the weight bands in which more than 10% of patients fell below it were examined. This note reuses the same published models and adds four things.

1. A closed-form definition and calculation of weight thresholds from the exponent \(b\).
2. A comparison of nine antibodies under one definition.
3. Threshold uncertainty from the standard error of the exponent.
4. The derivation and numerical check of the \(b=0.5\) boundary at which the variance of flat and mg/kg dosing is equal.

The aim is to examine the relation between the exponent and the thresholds under these definitions. A threshold is a definition of a difference in exposure, not a boundary of efficacy or safety. No dose is recommended.

## Assumptions and definitions

### Symbols

Let \(\mathrm{BW}\) (kg) be body weight, \(\mathrm{BW}_\mathrm{ref}\) (kg) the reference weight, and \(x=\mathrm{BW}/\mathrm{BW}_\mathrm{ref}\) (dimensionless) the relative weight. The power model of CL is

\[ \mathrm{CL}=\mathrm{CL}_\mathrm{ref}\,x^{b} \tag{1} \]

where \(\mathrm{CL}_\mathrm{ref}\) (L/day) is the CL of a reference-weight patient and \(b\) (dimensionless) is the weight exponent of CL. For the volume of distribution \(V\) (L) we use \(V=V_\mathrm{ref}\,x^{c}\) (\(V_\mathrm{ref}\) is \(V\) of a reference-weight patient and \(c\) is a dimensionless weight exponent). For linear PK, the steady-state AUC (area under the concentration-time curve over one interval) and the average concentration \(C_\mathrm{avg}\) are proportional to the dose divided by CL. Defining the exposure ratio \(R\) (dimensionless) as exposure relative to that of a reference-weight patient on the mg/kg dose, the exposure ratios of flat and mg/kg dosing are

\[ R_\mathrm{flat}(x)=s\,x^{-b},\qquad R_\mathrm{mg/kg}(x)=x^{1-b} \tag{2} \]

where \(s=D/(d\,\mathrm{BW}_\mathrm{ref})\) (dimensionless) is the flat dose \(D\) (mg) divided by the product of the mg/kg dose \(d\) (mg/kg) and the reference weight. \(s=1\) means that the flat dose equals the mg/kg dose of a reference-weight patient. The main results use \(s=1\). In that case \(R_\mathrm{flat}\) is relative to the exposure that the reference-weight patient receives on the same flat dose, and the results describe the spread of exposure around the reference-weight patient, not the distance from an exposure defined by the mg/kg dose. In actual approved regimens \(s\) can differ from 1, and those results are shown separately (Table 6).

![Two-panel figure of relative clearance against relative weight, and of the exposure ratio of flat and mg/kg dosing with the 0.8 to 1.2 band and the two ends of the flat-dose band.](shared/flat-dose-weight-threshold/figures/fig1_power_model_schematic.png)

Figure 1. Schematic of the power model. (a) Relative CL (clearance) for different \(b\). (b) Exposure ratio of flat dosing (solid) and mg/kg dosing (dashed) at \(b=0.6\) (illustrative). The grey band is the exposure ratio 0.8–1.2; dotted lines mark the two ends of the flat-dose band.

### Definition of a weight threshold

A threshold is the relative weight at which the exposure ratio equals \(r=1\pm\delta\). Here \(r\) (dimensionless) is the target exposure ratio and \(\delta\) (dimensionless) is the tolerated relative difference in exposure; 0.1, 0.2 and 0.3 were computed. Solving equation (2) for \(x\) gives

\[ x_\mathrm{flat}(r)=(s/r)^{1/b},\qquad x_\mathrm{mg/kg}(r)=r^{1/(1-b)} \tag{3} \]

The weight band in which exposure stays within \(1\pm\delta\) lies between the two weights corresponding to \(r=1+\delta\) and \(r=1-\delta\), for both regimens. The band was defined as a linear width \(1\pm\delta\) of the exposure ratio. A band that is symmetric on the log scale, \(\exp(\pm\delta)\), moves the limits somewhat (shown in the Results). For \(s=1\) the ratio of the upper to the lower limit of the band is \(((1+\delta)/(1-\delta))^{1/b}\) for flat dosing and \(((1+\delta)/(1-\delta))^{1/(1-b)}\) for mg/kg dosing. The flat-dose band is wider when \(1/b>1/(1-b)\), that is, when \(b<0.5\).

The weight at which the two regimens give equal exposure follows from equation (2): \(R_\mathrm{flat}/R_\mathrm{mg/kg}=s/x\), which equals 1 at \(x=s\) (the reference weight for \(s=1\)), independent of \(b\).

### Crossover of variance

If body weight is log-normal, \(\ln\mathrm{BW}\sim N(\mu,\sigma^2)\) (\(\mu\) is the mean and \(\sigma\) the standard deviation of \(\ln\mathrm{BW}\), both dimensionless), the variance of log exposure due to weight alone is

\[ \mathrm{Var}[\ln R_\mathrm{flat}]=b^{2}\sigma^{2},\qquad \mathrm{Var}[\ln R_\mathrm{mg/kg}]=(1-b)^{2}\sigma^{2} \tag{4} \]

The condition \(b^2=(1-b)^2\) holds at \(b=0.5\); for \(b<0.5\) the variance of flat dosing is smaller. This relation applies to the variance of log exposure defined as dose divided by CL (AUC and average concentration), not to the trough. The coefficient of variation (CV) of exposure is \(\sqrt{\exp(\mathrm{Var})-1}\).

### Uncertainty of the exponent and conditions of interpretation

With \(\mathrm{SE}(b)\) the standard error of \(b\), the delta-method standard error of the log threshold is given by equation (5) for flat dosing and equation (6) for mg/kg dosing.

\[ \mathrm{SE}(\ln x_\mathrm{flat})=\frac{|\ln(s/r)|}{b^{2}}\,\mathrm{SE}(b) \tag{5} \]

\[ \mathrm{SE}(\ln x_\mathrm{mg/kg})=\frac{|\ln r|}{(1-b)^{2}}\,\mathrm{SE}(b) \tag{6} \]

The \(b\) of each model is an effect conditional on the other covariates in that model (sex, albumin, tumour burden and others), not the marginal effect of weight.

### Trough (approximation)

The trough \(C_\mathrm{trough}\) depends on CL, \(V\) and the dosing interval \(\tau\) (days). At steady state for repeated intravenous (IV) bolus doses in a one-compartment model,

\[ C_\mathrm{trough}=\frac{D}{V}\,\frac{e^{-k\tau}}{1-e^{-k\tau}},\qquad k=\frac{\mathrm{CL}}{V} \tag{7} \]

This is an approximation: real antibodies need two or more compartments and are given by infusion. Here \(V\) was taken as the sum of the volumes of the central and peripheral compartments, \(V_\mathrm{c}\) and \(V_\mathrm{p}\) (both L), that is, \(V_\mathrm{ss}=V_\mathrm{c}x^{c_\mathrm{c}}+V_\mathrm{p}x^{c_\mathrm{p}}\) (\(c_\mathrm{c}\) and \(c_\mathrm{p}\) are the weight exponents of \(V_\mathrm{c}\) and \(V_\mathrm{p}\)). A sensitivity analysis with models of two or more compartments is shown in the Results.

## Methods

### Input data

Only antibodies for which the CL weight exponent, the reference weight and the power form could be confirmed in the text or tables of the primary source were used: pembrolizumab ([5](#ref-5), [Table 3 of Ahamadi et al.](https://doi.org/10.1002/psp4.12139)), nivolumab ([6](#ref-6), [Table 1 of Bajaj et al.](https://doi.org/10.1002/psp4.12143)), atezolizumab (the U.S. Food and Drug Administration (FDA) clinical pharmacology review ([7](#ref-7), [Table 8 of the review](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/761041Orig1s000ClinPharmR.pdf))), durvalumab ([8](#ref-8), [Table 2 of Baverel et al.](https://doi.org/10.1002/cpt.982)), avelumab ([9](#ref-9), [Table 2 of Wilkins et al.](https://doi.org/10.1002/psp4.12406)), tislelizumab ([1](#ref-1), [Table 3 of Budha et al.](https://doi.org/10.1002/psp4.12880) and [Equations 5 and 6 of the source](https://doi.org/10.1002/psp4.12880)), cemiplimab ([10](#ref-10), [Table 3 of Yang et al.](https://doi.org/10.1007/s10928-021-09739-y)), dostarlimab ([2](#ref-2), [Table 3 of Melhem et al.](https://doi.org/10.1111/bcp.15339)) and ipilimumab ([11](#ref-11), [Table 2 of Sanghavi et al.](https://doi.org/10.1002/psp4.12477)). For ipilimumab, the exponent 0.642 (95% interval 0.423–0.819) of an older time-invariant model ([12](#ref-12), [Table 2 of Feng et al.](https://doi.org/10.1111/bcp.12323)) was also used in the sensitivity analysis. For pembrolizumab, a footnote formula of the source gives a different exponent, 0.578 ([5](#ref-5)); the table value 0.595 was used for the main analysis and 0.578 for the sensitivity analysis.

Table 1 lists the exponents used. The standard error was derived by multiplying the reported relative standard error (RSE) by the estimate; when only an interval was reported, the interval width was divided by \(2\times1.96\), which is a symmetric normal approximation. The RSE of atezolizumab is 5%, rounded to an integer in the review. The reference weight is the value written in the source's formula, table footnote or reference patient of the covariate-effect analysis. For avelumab the formula ([Equation 3 of Wilkins et al.](https://doi.org/10.1002/psp4.12406)) is centred on the median, and the overall median of 71 kg in [Table 1 of Wilkins et al.](https://doi.org/10.1002/psp4.12406) was used (the centring constant is not stated). For tislelizumab, Equations 5 and 6 of the source are in the main text and are powers of weight with a reference of 65 kg. For dostarlimab the equation itself is not in the main text, and the power form was inferred from the reference patient weight (70 kg) and the description as "allometry". This is marked "Partial" in Figure 2. The weight effect of cemiplimab is shared by CL and the intercompartmental clearance, and \(V_\mathrm{c}\) and \(V_\mathrm{p}\) contain both weight and body mass index (BMI) (the equation is \(V\propto \mathrm{WGT}^{0.970}\,\mathrm{BMI}^{-0.560}\)).

Table 1. CL weight exponents used and weight ranges of the source populations. SE: standard error. CI: 95% interval (bootstrap or as reported in the source). BWref: reference weight. "Not reported" means that no interval was reported and only an RSE is available. The weight ranges are the minimum and maximum reported by the source; the 5th and 95th percentiles were NOT AVAILABLE (not in the main text of any source).

| Drug | b | SE (derived) | 95% CI (reported) | BWref (kg) | Source weight min–max (kg) |
| --- | --- | --- | --- | --- | --- |
| pembrolizumab | 0.595 | 0.047 | 0.506–0.686 | 76.8 | NOT AVAILABLE |
| nivolumab | 0.566 | 0.046 | 0.479–0.658 | 80 | NOT AVAILABLE |
| atezolizumab | 0.666 | 0.033 | not reported | 77 | NOT AVAILABLE |
| durvalumab | 0.389 | 0.045 | 0.299–0.477 | 69.8 | 34.0–149.1 |
| avelumab | 0.324 | 0.033 | 0.260–0.388 | 71 | 30.4–204 |
| tislelizumab | 0.565 | 0.034 | 0.491–0.631 | 65 | 31.9–130 |
| cemiplimab | 0.477 | 0.058 | not reported | 76.2 | 30.9–172 |
| dostarlimab | 0.470 | 0.029 | 0.414–0.527 | 70 | 34.0–182.0 |
| ipilimumab | 0.694 | 0.032 | 0.630–0.750 | 80 | 36.8–181 |

Source: `inputs/parameter_table.csv`, `inputs/source_weight_ranges.csv` and the tables of the sources (above). For nivolumab only the mean 79.1 kg (SD 19.3) is reported.

The antibodies that could not be confirmed were camrelizumab, adebrelimab, panitumumab, cetuximab, trastuzumab, bevacizumab and rituximab. The abstract of the camrelizumab population PK analysis states that body weight affected the intercompartmental clearance and not the linear clearance ([13](#ref-13)). The abstract of the panitumumab population PK analysis states that weight affected CL, the maximum non-linear elimination rate and the central volume, but the exponent could not be confirmed ([14](#ref-14), [15](#ref-15)). The trastuzumab population PK table gives a weight effect on linear CL of 0.967 (RSE 7.19%), but the covariate equation and reference weight are not in the main text, and the changes quoted in the text (27% lower at 46 kg and 43% higher at 98 kg relative to 66 kg) correspond to power exponents of 0.87 and 0.90. The reported value 0.967 as a power would predict about 29% lower and 46% higher; the numbers are close but do not agree, and the form could not be confirmed ([16](#ref-16)). For bevacizumab only a paediatric analysis was found ([17](#ref-17)), and the rituximab analysis found used body surface area as the covariate ([18](#ref-18)). No primary source that could be checked was found for adebrelimab and cetuximab. The status and reason for each are recorded in `inputs/not_verified.csv`. Figure 2 shows which antibodies were used and which could not be.

![Provenance matrix. The nine antibodies used have the exponent, uncertainty, reference weight, equation and volume exponent available, with the equation only partial for dostarlimab; the seven not used lack some or all of them.](shared/flat-dose-weight-threshold/figures/fig2_data_provenance_matrix.png)

Figure 2. Data provenance. CL: clearance. V: volume of distribution. Yes: confirmed. Partial: the equation is not explicit in the main text. RSE: only a relative standard error, no interval. CI: interval available. No: not confirmed or not used.

### Calculation

All thresholds were computed in closed form from equation (3). Uncertainty was obtained in three ways: the delta method (equations (5) and (6)); the 2.5th–97.5th percentiles of 200,000 random draws of \(b\sim N(b,\mathrm{SE}^2)\); and the values obtained by substituting the two ends of the reported interval into equation (3) (seven antibodies have intervals). The random seed was 20261105.

The weight distribution was set by four assumed log-normal scenarios (S1: median 75 kg and CV 20%; S2: 70 kg and 25%; S3: 80 kg and 30%; S4: 65 kg and 25%). They are assumptions, not measurements of a specific population. For each scenario, the proportion of patients whose exposure ratio falls outside 0.8–1.2 was computed exactly with the normal cumulative distribution function and checked with 400,000 random draws. To separate the effects of the location shift and the spread, we also computed the proportions with the median set to the reference weight and only the CV varied (20, 25 and 30%), and with CV 25% and only the median varied (65, 70, 75 and 80 kg). The variance check used S1 (\(\sigma=0.198\)). The total SD, adding a log-scale standard deviation (SD) of 0.30 (assumed) for the between-patient variability of CL to the weight-only variance, was also compared.

The closed forms were checked against the solution of the differential equation of one-compartment repeated bolus dosing (LSODA, relative tolerance \(10^{-11}\)). The trough and AUC were compared for nine antibodies, five relative weights and two dosing methods. This check verifies the implementation and does not test whether the one-compartment bolus approximation is adequate for real antibodies. The trough approximation used the reported typical CL, \(V_\mathrm{c}\), \(V_\mathrm{p}\) and weight exponents, at the common intervals of 21 and 14 days and at the interval of the regimen studied in each source (21 days (Q3W, every 3 weeks) for pembrolizumab, atezolizumab, tislelizumab, cemiplimab, dostarlimab and ipilimumab; 14 days (Q2W, every 2 weeks) for nivolumab, durvalumab and avelumab). For \(V\) of cemiplimab, the net exponent 0.41 was used, obtained by adding \(-0.560\) for BMI to the weight exponent, on the assumption that BMI is proportional to weight at fixed height; the result with the weight exponent 0.970 alone was treated as a sensitivity analysis. The heavy-side limits in two-compartment (three for tislelizumab) bolus models were computed with a matrix exponential using the reported intercompartmental clearance, held constant with weight and also varied as \(x^{b}\).

### Verification

Fifteen tests were run (closed forms against the differential equation, the multi-compartment matrix solution against the differential equation, the flat-to-mg/kg ratio \(1/x\), equal variance at \(b=0.5\), monotonicity, delta method against simulation, exact proportions against simulation, seed reproducibility, completeness of the input table and others). The whole analysis and the figures were run twice, and the hashes of the result files were identical.

## Results

### Range of exponents

The nine exponents ranged from 0.324 (avelumab) to 0.694 (ipilimumab); four were below 0.5 and five were 0.5 or above.

### Threshold weights

Figure 3 shows the exposure curves from equation (2) for each antibody. Table 2 gives the flat-dose weight bands for \(\delta=0.1,0.2,0.3\) and the mg/kg weight band for \(\delta=0.2\). For \(s=1\), flat and mg/kg exposure are equal at the reference weight.

![Nine small panels showing the exposure ratio of flat and mg/kg dosing for each antibody between 40 and 160 kg, with a grey band at 0.8 to 1.2.](shared/flat-dose-weight-threshold/figures/fig3_relative_exposure_by_drug.png)

Figure 3. Relative exposure by antibody. Solid: flat dose; dashed: mg/kg dose; grey band: exposure ratio 0.8–1.2; dotted line: reference weight. Logarithmic vertical axis. b: weight exponent of CL; BWref: reference weight.

Table 2. Weight band (kg, \(s=1\)) in which exposure stays within \(\pm\delta\) of the reference.

| Drug | Flat, ±10% | Flat, ±20% | Flat, ±30% | mg/kg, ±20% |
| --- | --- | --- | --- | --- |
| pembrolizumab | 65–92 | 57–112 | 49–140 | 44–120 |
| nivolumab | 68–96 | 58–119 | 50–150 | 48–122 |
| atezolizumab | 67–90 | 59–108 | 52–132 | 39–133 |
| durvalumab | 55–92 | 44–124 | 36–175 | 48–94 |
| avelumab | 53–98 | 40–141 | 32–213 | 51–93 |
| tislelizumab | 55–78 | 47–96 | 41–122 | 39–99 |
| cemiplimab | 62–95 | 52–122 | 44–161 | 50–108 |
| dostarlimab | 57–88 | 47–113 | 40–150 | 46–99 |
| ipilimumab | 70–93 | 62–110 | 55–134 | 39–145 |

Source: `analysis.py`, `results/thresholds.csv`.

At ±20%, the light-side limit of flat dosing was 40–62 kg and the heavy-side limit 96–141 kg; for mg/kg dosing the light-side limit was 39–51 kg and the heavy-side limit 93–145 kg. The relative weight on the heavy side, \(0.8^{-1/b}\), is larger for smaller \(b\): 1.99 for avelumab (\(b=0.324\)), 1.48 for tislelizumab (0.565) and 1.38 for ipilimumab (0.694). The limit in kg is this value multiplied by the reference weight, and because the reference weights differ (65–80 kg) the order can differ from that of \(b\) (tislelizumab 96 kg, ipilimumab 110 kg). The flat-dose band was wider than the mg/kg band for durvalumab, avelumab, cemiplimab and dostarlimab, the same four antibodies with \(b<0.5\).

With a band symmetric on the log scale, \(\exp(\pm0.2)\), the flat-dose limits were 38–132 kg for avelumab (40–141 kg with the linear definition) and 55–107 kg for pembrolizumab (57–112 kg) (`results/thresholds_log_symmetric.csv`). In the sensitivity analysis with other exponents, the ±20% flat-dose band was 56–113 kg with the pembrolizumab footnote exponent 0.578 (main analysis 57–112 kg) and 60–113 kg with the older ipilimumab model exponent 0.642 (main analysis 62–110 kg); the differences from the main analysis were within 3 kg.

The limit weights were compared with the weight range of the source populations (Table 1). All 24 limits at ±20% (seven antibodies with a known range, two regimens, light and heavy sides) lay inside the minimum and maximum of the source. At ±30%, five limits fell outside the range (the heavy-side flat-dose limit of durvalumab, 175 kg, against a maximum of 149.1 kg; the heavy-side limit of avelumab, 213 kg, against 204 kg; the light-side mg/kg limit of tislelizumab, 29 kg, against a minimum of 31.9 kg; and the light-side mg/kg limit of ipilimumab, 25 kg, and heavy-side limit, 189 kg, against a range of 36.8–181 kg). These are extrapolations. The weight range could not be obtained for pembrolizumab, nivolumab and atezolizumab (NOT AVAILABLE), so 12 limits could not be assessed. Even inside the range, the distribution of patients (the 5th and 95th percentiles are NOT AVAILABLE) was not confirmed, and patients at the extreme weights are probably few.

### Uncertainty

Table 3 gives the ±20% thresholds with the 95% interval from simulation of the standard error of \(b\) alone. Figure 4 shows these intervals.

Table 3. ±20% limit weights (kg) with 95% interval from the uncertainty of \(b\) only (simulation).

| Drug | Flat, light side | Flat, heavy side | mg/kg, heavy side |
| --- | --- | --- | --- |
| pembrolizumab | 57 (53–59) | 112 (106–120) | 120 (111–138) |
| nivolumab | 58 (55–61) | 119 (112–128) | 122 (113–136) |
| atezolizumab | 59 (57–60) | 108 (104–112) | 133 (122–152) |
| durvalumab | 44 (38–48) | 124 (111–147) | 94 (91–99) |
| avelumab | 40 (35–44) | 141 (126–168) | 93 (91–96) |
| tislelizumab | 47 (45–49) | 96 (93–102) | 99 (94–107) |
| cemiplimab | 52 (46–56) | 122 (111–141) | 108 (101–119) |
| dostarlimab | 47 (45–50) | 113 (107–120) | 99 (96–103) |
| ipilimumab | 62 (60–63) | 110 (107–114) | 145 (131–169) |

Source: `results/thresholds_uncertainty.csv`.

![Limit weights on the light and heavy sides with 95% intervals for each antibody, in two panels for flat and mg/kg dosing.](shared/flat-dose-weight-threshold/figures/fig4_threshold_weights_forest.png)

Figure 4. ±20% limit weights (kg). Triangles: light-side limit; squares: heavy-side limit (simulation median); horizontal lines: 95% interval from the uncertainty of \(b\) alone; black diamonds: reference weight. Antibodies are ordered by \(b\) (ascending from bottom to top); b in the labels is the weight exponent of CL.

The delta-method and simulation intervals were close, but the simulation intervals were asymmetric towards the upper side. The relative difference in interval width between the two methods was at most 11%. For the seven antibodies with reported intervals, substituting the ends of the interval into equation (3) also gave values close to the simulation interval (106–119 kg for the heavy-side limit of pembrolizumab flat dosing). For the heavy-side limit of flat dosing the widest interval was for avelumab (126–168 kg) and the narrowest for ipilimumab (107–114 kg); the narrowest light-side interval was also ipilimumab (60–63 kg).

### Crossover of variance at \(b=0.5\)

For a log SD of weight \(\sigma=0.198\) (S1, median 75 kg, CV 20%), the SD of log exposure due to weight alone from equation (4) differed from the value of 400,000 random draws by at most 0.0003 (log units). Table 4 gives \(b\), the probability that \(b<0.5\), the CV of exposure and the regimen with the smaller variance at the point estimate. Figure 5 shows the ratio of SDs against \(b\) and the position of each antibody.

Table 4. Variability of AUC (or average concentration) due to weight alone (\(\sigma=0.198\)). \(P(b<0.5)\) is a normal approximation based on the reported standard error alone and does not include uncertainty from model structure or between-study differences. "Lower variance (point estimate)" is the judgement from the point estimate of \(b\).

| Drug | b | P(b<0.5) | CV flat (%) | CV mg/kg (%) | Lower variance (point estimate) |
| --- | --- | --- | --- | --- | --- |
| pembrolizumab | 0.595 | 0.022 | 11.8 | 8.0 | mg/kg |
| nivolumab | 0.566 | 0.074 | 11.2 | 8.6 | mg/kg |
| atezolizumab | 0.666 | 0.000 | 13.2 | 6.6 | mg/kg |
| durvalumab | 0.389 | 0.993 | 7.7 | 12.1 | flat |
| avelumab | 0.324 | 1.000 | 6.4 | 13.4 | flat |
| tislelizumab | 0.565 | 0.027 | 11.2 | 8.6 | mg/kg |
| cemiplimab | 0.477 | 0.655 | 9.5 | 10.4 | flat |
| dostarlimab | 0.470 | 0.852 | 9.3 | 10.5 | flat |
| ipilimumab | 0.694 | 0.000 | 13.8 | 6.1 | mg/kg |

Source: `results/variance_crossover.csv`.

![Top: ratio of the SD of log exposure to the SD of log weight against b; the flat and mg/kg lines cross at b = 0.5. Bottom: b and its 95% interval for each antibody.](shared/flat-dose-weight-threshold/figures/fig5_variance_crossover.png)

Figure 5. \(b\) and the variance crossover. Top: ratio of the SD of log exposure to the SD of log weight (\(|b|\) for flat dosing, \(|1-b|\) for mg/kg dosing). Bottom: \(b\) for each antibody (points) and estimate ± 1.96 SE (horizontal lines). The dotted line is \(b=0.5\).

For cemiplimab and dostarlimab, the point estimate is close to 0.5 and the probability that \(b<0.5\) is only 0.66 and 0.85. \(P(b<0.5)\) is based on the reported standard error alone and excludes differences in model structure. Indeed, the differences in the exponent between models of the same antibody were 0.017 between the table and footnote of pembrolizumab, 0.052 between the two ipilimumab models and 0.011 for the time-invariant durvalumab model, which is 0.2–1.7 times the standard error of the main estimate. When a log-scale SD of 0.30 (assumed) for the between-patient variability of CL was added, the total SD differed by at most 0.024 between flat and mg/kg dosing (ipilimumab 0.330 and 0.306). When the between-patient variability of CL not due to weight is large, the difference between the regimens becomes small.

### Sensitivity to the weight distribution

The proportions are those of patients whose exposure ratio falls outside 0.8–1.2. In S1, the proportion was 0.2% (avelumab) to 18.4% (ipilimumab) for flat dosing and 0.1% (ipilimumab) to 16.5% (avelumab) for mg/kg dosing. Figure 6 shows the results for the four scenarios (S1–S4). Across scenarios the proportion ranged from 0.2% to 42.7% for flat dosing and from 0.1% to 36.7% for mg/kg dosing. The regimen with the smaller proportion agreed with the \(b<0.5\) rule for all nine antibodies in S1 and S3, and for eight (all but cemiplimab) in S2 and S4.

![For each antibody, the proportion with exposure ratio outside 0.8 to 1.2 under four weight-distribution scenarios, in two panels for flat and mg/kg dosing.](shared/flat-dose-weight-threshold/figures/fig6_weight_distribution_sensitivity.png)

Figure 6. Proportion outside the exposure ratio 0.8–1.2 under the weight-distribution scenarios. S1–S4 are scenarios 1–4, assumed log-normal distributions (median and coefficient of variation, CV), not measured populations. The variability is that due to weight alone and excludes the between-patient variability of CL. b: weight exponent of CL.

The effects of the location shift and the spread can be separated (`results/distribution_shift_spread.csv`). With the median set to the reference weight, raising the CV from 20% to 30% increased the proportions from 0.2–14.5% to 3.7–32.2% for flat dosing and from 0.1–13.4% to 2.8–31.0% for mg/kg dosing. With CV 25%, moving only the median from 65 kg to 80 kg decreased the flat-dose proportion for pembrolizumab (reference weight 76.8 kg) from 29.9% to 16.7% and increased it for tislelizumab (reference weight 65 kg) from 14.9% to 23.9%. The proportions were affected by the spread and by the offset between the median and the reference weight about as much as by \(b\).

### Difference from the trough

Table 5 gives, for a one-compartment approximation, the heavy-side weight at which the flat-dose trough is 20% lower than the reference, next to the AUC limit. The interval is that of the regimen studied in each source.

Table 5. Heavy-side limit weight of flat dosing (exposure ratio 0.8, kg). \(c_\mathrm{eff}\): effective weight exponent of \(V\) (base-2 logarithm of \(V_\mathrm{ss}(2\,\mathrm{BW}_\mathrm{ref})/V_\mathrm{ss}(\mathrm{BW}_\mathrm{ref})\)). \(t_{1/2}\): half-life in the approximation. Shift: the AUC limit minus the trough limit. Shift (2-comp): the same difference in a two-compartment (three for tislelizumab) bolus model, with the intercompartmental clearance held constant with weight / varied as \(x^{b}\). The \(c_\mathrm{eff}\) of cemiplimab is the net value including BMI.

| Drug | b | c_eff | t1/2 (day) | Interval (day) | AUC limit | Trough limit | Shift | Shift (2-comp) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pembrolizumab | 0.595 | 0.49 | 23.8 | 21 | 112 | 109 | 2.4 | 4.7 / 2.2 |
| nivolumab | 0.566 | 0.37 | 19.7 | 14 | 119 | 114 | 4.3 | 3.9 / 2.2 |
| atezolizumab | 0.666 | 0.27 | 24.2 | 21 | 108 | 101 | 6.3 | 6.6 / 4.3 |
| durvalumab | 0.389 | 0.22 | 20.8 | 14 | 124 | 117 | 7.3 | 6.2 / 1.5 |
| avelumab | 0.324 | 0.29 | 4.1 | 14 | 141 | 128 | 13.1 | 13.6 / 14.3 |
| tislelizumab | 0.565 | 0.20 | 29.1 | 21 | 96 | 91 | 5.9 | 6.4 / 5.3 |
| cemiplimab | 0.477 | 0.41 | 11.9 | 21 | 122 | 116 | 5.3 | 6.4 / 5.0 |
| dostarlimab | 0.470 | 0.42 | 19.7 | 21 | 113 | 110 | 2.3 | 4.5 / 2.2 |
| ipilimumab | 0.694 | 0.36 | 14.6 | 21 | 110 | 102 | 8.0 | 7.7 / 6.3 |

Source: `results/trough_approximation.csv`, `results/trough_two_compartment.csv`.

For all nine antibodies \(b>c_\mathrm{eff}\), so the elimination rate constant \(k=\mathrm{CL}/V\) increases with weight and the trough falls faster than the AUC. The heavy-side trough limit appeared at a weight 2.3–13.1 kg below the AUC limit (at the interval of the source regimen). With a common interval of 21 days for all antibodies the difference was 2.3–19.5 kg, the largest being for avelumab (\(k\tau=3.6\)); the source regimen of avelumab uses a 14-day interval. At the AUC-based limit weight, the trough was 0.75–0.79 times the reference. In the models with two or more compartments, the heavy-side trough limit moved by about \(-5\) to \(+6\) kg from the one-compartment value, and the difference from the AUC limit was 1.5–14.3 kg. The sign and size depend on the model structure.

The weight exponent of \(V\) of cemiplimab is not only the 0.970 reported for \(V_\mathrm{ss}\) but also includes the BMI exponent \(-0.560\) ([10](#ref-10)). If BMI is proportional to weight at fixed height, the net exponent is 0.41, and the heavy-side trough limit was 116 kg (21 days), about 5 kg below the AUC limit of 122 kg. Using only the weight exponent 0.970 for \(V\) gives a limit of 225 kg (21 days) and 164 kg (14 days), but this value depends strongly on the \(V\) exponent (178 kg at 0.82; not reached within 8 times the reference weight at 1.12) and also moves widely within the standard error of \(b\) (`results/cemiplimab_trough_sensitivity.csv`). This note therefore does not adopt that value as a result, and regards it as a strongly uncertain value of around 180 kg or more.

The check against the differential equation verifies the implementation; the relative differences for the trough and AUC were at most \(3.9\times10^{-11}\) (nine antibodies, five relative weights, two dosing methods, 90 comparisons in all). The multi-compartment matrix solution also differed from the differential equation by at most \(1\times10^{-11}\).

### Matching the dose to a reference weight

In the sensitivity analysis that changes the ratio \(s\) that matches the flat dose to the mg/kg dose at the reference weight (`results/dose_matching_sensitivity.csv`), the ±20% band of pembrolizumab flat dosing was 82–163 kg for \(s=1.25\) and 39–77 kg for \(s=0.8\). Table 6 gives \(s\) for the doses given in the sources or in the existing article, calculated including the difference in dosing interval.

Table 6. \(s\) and the flat-dose exposure band for the doses given in the sources or the existing article. \(s=(D/\tau_\mathrm{flat})/(d\,\mathrm{BW}_\mathrm{ref}/\tau_\mathrm{mg/kg})\) (\(\tau\) is the dosing interval). The value in parentheses for durvalumab is the per-dose ratio that ignores the difference in interval.

| Drug | Flat dose | mg/kg comparator | s | Flat ±20% band (kg) | Flat +10% heavy limit (kg) |
| --- | --- | --- | --- | --- | --- |
| pembrolizumab | 200 mg Q3W | 2 mg/kg Q3W | 1.30 | 88–174 | 143 |
| nivolumab | 240 mg Q2W | 3 mg/kg Q2W | 1.00 | 58–119 | 96 |
| atezolizumab | 1200 mg Q3W | 15 mg/kg Q3W | 1.04 | 62–114 | 96 |
| durvalumab | 1500 mg Q4W | 10 mg/kg Q2W | 1.07 (2.15) | 53–149 | 110 |
| avelumab | 800 mg Q2W | 10 mg/kg Q2W | 1.13 | 58–204 | 142 |
| tislelizumab | 200 mg Q3W | 3 mg/kg Q3W | 1.03 | 49–101 | 82 |

Source: `results/label_dose_matching.csv`. The doses of pembrolizumab and nivolumab follow the pairing in the existing article ([3](#ref-3)); the others are the doses in the sources.

The existing article reported weight bands in which more than 10% of patients fell below the lower limit at about 150 kg and above for pembrolizumab and about 100–120 kg and above for nivolumab ([3](#ref-3)). Under the exposure-ratio definition here, the heavy-side limit at ±10% was 143 kg for pembrolizumab with its 200 mg matched to 100 kg (\(s=1.30\)) and 92 kg for \(s=1\), and 96 kg for nivolumab at \(s=1\). The order in which pembrolizumab tolerates heavier weights than nivolumab appears only at \(s=1.30\) and is reversed at \(s=1\). The agreement in order with the existing article therefore arises from the dose matching \(s\), not from \(b\). The definitions (an exposure-ratio band versus the proportion below a floor set at the 5th percentile of the reference-regimen trough) and the populations (source populations versus general adults) also differ, so the two sets of numbers are not directly comparable.

## Discussion

The exponent \(b\) determines two quantities: the width of the weight band and which regimen has the smaller variance. The ratio of the upper to the lower weight at which exposure stays within ±20% of the reference is \((1.5)^{1/b}\) for flat dosing, which falls from about 3.5 to about 1.8 as \(b\) rises from 0.324 to 0.694. This ratio does not depend on the reference weight. The position of the band in kg does depend on it, and a limit is proportional to the reference weight (1 kg of reference weight is 1.3–1.5% of a limit). The reference weights are population medians of 65–80 kg, and the population and the definition of the covariates differ between sources. The centring constant of avelumab is not stated. Comparing the weights in Table 2 across antibodies therefore includes the differences in reference weight as well as in exponent.

The results for \(s=1\) answer the question of the spread of exposure around the reference-weight patient. In the regimens shown, \(s\) is 1.00–1.30 (1.07 for durvalumab with the interval taken into account), and the band moves to heavier weights (Table 6). Which weight's mg/kg dose the flat dose actually corresponds to moves the limits widely even for the same \(b\).

The crossover at \(b=0.5\) follows from the squares in equation (4) and was confirmed numerically. However, of the four antibodies whose point estimate was below 0.5, the probability was at least 0.99 only for avelumab and durvalumab; it is 0.85 for dostarlimab and 0.66 for cemiplimab. For tislelizumab, nivolumab and pembrolizumab the probability of being above 0.5 is 0.93–0.98, but their point estimates, 0.565–0.595, are close to 0.5. This probability is based on the reported standard error alone and excludes the differences in exponent between models (0.2–1.7 times the standard error). The dichotomy "flat dosing if \(b<0.5\)" cannot be settled for antibodies near the boundary. The relation is limited to the variance of AUC and average concentration, and the trough needs a separate calculation.

For panitumumab the exponent could not be confirmed, but a published analysis is informative. Liao et al. reported that the interpatient variability of the simulated AUC was 29% for 6 mg/kg and 34% for a flat 480 mg ([15](#ref-15)). The direction agrees with \(b>0.5\). However, panitumumab has non-linear PK, which is outside the power model used here, and its exponent was not confirmed. The range of exponents in this note, 0.32–0.69, is that of antibodies against PD-1, PD-L1 and CTLA-4, not of antibodies in general (0.967 is reported for trastuzumab).

For the trough, the effect of weight also depended on the \(V\) exponent. For all nine antibodies the heavy-side trough limit moved to a weight lighter than the AUC limit, by 2.3–13.1 kg at the interval of the source regimen and 2.3–19.5 kg at a common 21 days. This difference depends on the one-compartment bolus approximation, the interval, the \(V\) exponent and the treatment of the intercompartmental clearance, and in the two-compartment models its sign and size changed. For cemiplimab, using the weight exponent without BMI for \(V\) moved the limit to around 180 kg or more. How weight enters \(V\) determines the trough threshold.

On consistency with the existing article ([3](#ref-3)), the exponents and reference weights of pembrolizumab and nivolumab could be confirmed in the primary sources and were the same values (0.595 and 76.8 kg; 0.566 and 80 kg). The numbers move widely with the definition and the dose matching \(s\) and are not directly comparable.

## Limitations

The results are conditional on the power model (equation (1)), the reported exponents and the assumed weight distributions. Each exponent was estimated in the trial population of its source as a conditional value together with covariates correlated with weight, such as sex, albumin and tumour burden. The weight effect may include the effects of other covariates. The correlation between weight and other determinants of CL is not included in the calculation of the total SD with a log-scale SD of 0.30 (assumed), which assumes independence. The reported standard errors hold only if the model is correct. In the tislelizumab data 76.7% of patients were Asian ([1](#ref-1)), a population that differs from the other sources.

The weight effect is a power of total body weight, and lean body mass, obesity (at high BMI a power of total weight overestimates CL), cachexia, forms other than the power and non-linearity at the extremes of weight are not included. The limit weights are extrapolations at or beyond the ends of the source weight ranges (five ±30% limits lay outside), and the weight range could not be obtained for pembrolizumab, nivolumab and atezolizumab. The 5th and 95th percentiles could not be obtained from any source.

The standard errors are symmetric normal approximations derived from the reported RSE or intervals. In the durvalumab bootstrap 694 of 1,000 runs succeeded ([8](#ref-8)), and no intervals were reported for atezolizumab and cemiplimab. The atezolizumab value is the FDA reviewer's re-fit of the applicant's model ([7](#ref-7)), its RSE is rounded to an integer, and it is not a value from a journal article. The reference weight of avelumab is a median of 71 kg whose centring constant is not stated. For dostarlimab the equation is not in the main text. The reference weight is not an estimated parameter, and its uncertainty is not included. The CL models of nivolumab, avelumab, cemiplimab, dostarlimab, ipilimumab and durvalumab are time-varying, and the exponent refers to the CL at the baseline time. If the time-varying factor is independent of weight the steady-state ratios are preserved, but that factor is related to disease course and cachexia and may correlate with weight. The non-linear (Michaelis–Menten) elimination of durvalumab is not weight-adjusted in the table, which matters for light patients and for comparisons at low doses. The power-law ratio applies to the linear or baseline component.

The weight distributions are four log-normal scenarios and make no claim about a specific population. Real weight distributions have a heavier right tail than the log-normal. The between-patient variability of CL not due to weight and correlations between covariates were not included. The trough calculation is a one-compartment bolus approximation with a sensitivity analysis in two- and three-compartment models that tested only the treatment of the intercompartmental clearance. The maximum concentration was not analysed.

A difference in exposure is not a difference in efficacy or safety. Whether the exposure-response relationship is flat is outside this note. A threshold is a definition of an exposure ratio, not a clinical cut-off and not a dose recommendation. The antibodies that could not be confirmed (Figure 2) are not included, and the nine are not a representative sample of drugs.

The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

There is no single weight threshold for flat dosing. When a threshold is defined as the weight band in which the exposure ratio stays within ±20% of the reference, the light-side limit of flat dosing was 40–62 kg and the heavy-side limit 96–141 kg across nine antibodies. This range is determined by the exponent \(b\) (0.324–0.694), the reference weight (65–80 kg) and the matching \(s\) of the flat and mg/kg doses, and the standard error of \(b\) alone gave the heavy-side limit an interval up to about 40 kg wide (avelumab, 126–168 kg). The extreme weights may involve extrapolation beyond the few patients in the source populations. The variance of AUC (or average concentration) due to weight alone is equal for the two regimens at \(b=0.5\); the point estimate was below it for four antibodies, but the probability was at least 0.99 only for avelumab and durvalumab. When defined by trough, the heavy-side limit moved to a weight 2–13 kg below the AUC limit for the nine antibodies at the interval of the source regimen. These are calculations of exposure under the power model, the reported exponents and the assumed weight distributions; they do not show a difference in efficacy and are not a dose recommendation.

## Data and code availability

The inputs are the exponents and typical values transcribed from published tables (`inputs/parameter_table.csv`, with the source DOI, table location and basis of the reference weight on each row), the weight ranges of the source populations (`inputs/source_weight_ranges.csv`) and the record of antibodies that could not be confirmed (`inputs/not_verified.csv`). The calculation code (`powermodel.py`, `odecheck.py`, `analysis.py`, `figures.py`), the tests (`test_analysis.py`, 15 tests), the reproducibility check (`check_reproducibility.py`), `requirements.txt`, the result CSV/JSON files and the figures are in the companion ZIP. The random seed is 20261105; the runs used Python 3.12, NumPy 2.2, SciPy 1.14, pandas 2.2, matplotlib 3.9 and pytest 9. The commands, in order, are `python -X utf8 analysis.py`, `python -X utf8 figures.py`, `python -X utf8 -m pytest test_analysis.py -q` and `python -X utf8 check_reproducibility.py`; the whole takes about two minutes. That the hashes of the result files are identical across two runs is checked by `check_reproducibility.py`.

The input table contains only numerical values and table locations transcribed from the sources, and no source tables, figures or text are reproduced. The sources are published under their own licences: CC BY for cemiplimab ([10](#ref-10)) and trastuzumab ([16](#ref-16)); CC BY-NC for tislelizumab ([1](#ref-1)), dostarlimab ([2](#ref-2)), nivolumab ([6](#ref-6)), durvalumab ([8](#ref-8)) and the panitumumab analysis of Liao et al. ([15](#ref-15)); CC BY-NC-ND for pembrolizumab ([5](#ref-5)), avelumab ([9](#ref-9)), ipilimumab ([11](#ref-11), [12](#ref-12)), bevacizumab ([17](#ref-17)) and rituximab ([18](#ref-18)). Camrelizumab ([13](#ref-13)) and the panitumumab analysis of Ma et al. ([14](#ref-14)) are under publisher terms, and the FDA review ([7](#ref-7)) is a U.S. government document. These licences apply to the sources and not to the input table compiled for this note. All figures are original calculations. The code is released under the MIT License and the result CSV/JSON files and figures under CC BY 4.0, as stated in `LICENSE`.

[Download the code, results and figures](shared/flat-dose-weight-threshold/flat-dose-weight-threshold-companion.zip)

The full re-run materials are in the [companion archive](shared/flat-dose-weight-threshold/flat-dose-weight-threshold-companion.zip).


## References

<span id="ref-1"></span>1. Budha N, Wu CY, Tang Z, Yu T, Liu L, Xu F, et al. Model-based population pharmacokinetic analysis of tislelizumab in patients with advanced tumors. CPT Pharmacometrics Syst Pharmacol. 2023;12(1):95–109. [https://doi.org/10.1002/psp4.12880](https://doi.org/10.1002/psp4.12880)
<span id="ref-2"></span>2. Melhem M, Hanze E, Lu S, Alskär O, Visser S, Gandhi Y. Population pharmacokinetics and exposure-response of anti-programmed cell death protein-1 monoclonal antibody dostarlimab in advanced solid tumours. Br J Clin Pharmacol. 2022;88(9):4142–4154. [https://doi.org/10.1111/bcp.15339](https://doi.org/10.1111/bcp.15339)
<span id="ref-3"></span>3. Kumakura D. Do fixed doses of anti-PD-1 antibodies keep exposure in range at extreme body weights? [Internet]. DaikiKumakura.github.io; 2026 Oct 20 [cited 2026 Nov 5]. Available from: [https://daikikumakura.github.io/writing/fixed-vs-weight-dosing-en.html](https://daikikumakura.github.io/writing/fixed-vs-weight-dosing-en.html)
<span id="ref-4"></span>4. Kumakura D. Fixed (flat) dosing versus weight-based dosing [Internet]. DaikiKumakura.github.io; updated 2026 Oct 28 [cited 2026 Nov 5]. Available from: [https://daikikumakura.github.io/glossary/fixed-vs-weight-based-dosing.html](https://daikikumakura.github.io/glossary/fixed-vs-weight-based-dosing.html)
<span id="ref-5"></span>5. Ahamadi M, Freshwater T, Prohn M, Li CH, de Alwis DP, de Greef R, et al. Model-based characterization of the pharmacokinetics of pembrolizumab: a humanized anti-PD-1 monoclonal antibody in advanced solid tumors. CPT Pharmacometrics Syst Pharmacol. 2017;6(1):49–57. [https://doi.org/10.1002/psp4.12139](https://doi.org/10.1002/psp4.12139)
<span id="ref-6"></span>6. Bajaj G, Wang X, Agrawal S, Gupta M, Roy A, Feng Y. Model-based population pharmacokinetic analysis of nivolumab in patients with solid tumors. CPT Pharmacometrics Syst Pharmacol. 2017;6(1):58–66. [https://doi.org/10.1002/psp4.12143](https://doi.org/10.1002/psp4.12143)
<span id="ref-7"></span>7. U.S. Food and Drug Administration, Center for Drug Evaluation and Research. Clinical pharmacology and biopharmaceutics review(s), application number 761041Orig1s000 (atezolizumab), Reference ID 3992046 [Internet]. FDA; [date unknown; URL path 2016] [cited 2026 Nov 5]. Available from: [https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/761041Orig1s000ClinPharmR.pdf](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/761041Orig1s000ClinPharmR.pdf)
<span id="ref-8"></span>8. Baverel PG, Dubois VFS, Jin CY, Zheng Y, Song X, Jin X, et al. Population pharmacokinetics of durvalumab in cancer patients and association with longitudinal biomarkers of disease status. Clin Pharmacol Ther. 2018;103(4):631–642. [https://doi.org/10.1002/cpt.982](https://doi.org/10.1002/cpt.982)
<span id="ref-9"></span>9. Wilkins JJ, Brockhaus B, Dai H, Vugmeyster Y, White JT, Brar S, et al. Time-varying clearance and impact of disease state on the pharmacokinetics of avelumab in Merkel cell carcinoma and urothelial carcinoma. CPT Pharmacometrics Syst Pharmacol. 2019;8(6):415–427. [https://doi.org/10.1002/psp4.12406](https://doi.org/10.1002/psp4.12406)
<span id="ref-10"></span>10. Yang F, Paccaly AJ, Rippley RK, Davis JD, DiCioccio AT. Population pharmacokinetic characteristics of cemiplimab in patients with advanced malignancies. J Pharmacokinet Pharmacodyn. 2021;48(4):479–494. [https://doi.org/10.1007/s10928-021-09739-y](https://doi.org/10.1007/s10928-021-09739-y)
<span id="ref-11"></span>11. Sanghavi K, Zhang J, Zhao X, Feng Y, Statkevich P, Sheng J, et al. Population pharmacokinetics of ipilimumab in combination with nivolumab in patients with advanced solid tumors. CPT Pharmacometrics Syst Pharmacol. 2020;9(1):29–39. [https://doi.org/10.1002/psp4.12477](https://doi.org/10.1002/psp4.12477)
<span id="ref-12"></span>12. Feng Y, Masson E, Dai D, Parker SM, Berman D, Roy A. Model-based clinical pharmacology profiling of ipilimumab in patients with advanced melanoma. Br J Clin Pharmacol. 2014;78(1):106–117. [https://doi.org/10.1111/bcp.12323](https://doi.org/10.1111/bcp.12323)
<span id="ref-13"></span>13. Wang CY, Sheng CC, Ma GL, Xu D, Liu XQ, Wang YY, et al. Population pharmacokinetics of the anti-PD-1 antibody camrelizumab in patients with multiple tumor types and model-informed dosing strategy. Acta Pharmacol Sin. 2021;42(8):1368–1375. [https://doi.org/10.1038/s41401-020-00550-y](https://doi.org/10.1038/s41401-020-00550-y). Abstract and a truncated publisher page were read.
<span id="ref-14"></span>14. Ma P, Yang BB, Wang YM, Peterson M, Narayanan A, Sutjandra L, et al. Population pharmacokinetic analysis of panitumumab in patients with advanced solid tumors. J Clin Pharmacol. 2009;49(10):1142–1156. [https://doi.org/10.1177/0091270009344989](https://doi.org/10.1177/0091270009344989). Abstract only was read.
<span id="ref-15"></span>15. Liao MZ, Berkhout M, Prenen H, Dutta S, Upreti VV. Dose regimen rationale for panitumumab in cancer patients: to be based on body weight or not. Clin Pharmacol. 2020;12:109–114. [https://doi.org/10.2147/CPAA.S262949](https://doi.org/10.2147/CPAA.S262949)
<span id="ref-16"></span>16. Quartino AL, Li H, Kirschbrown WP, Mangat R, Wada DR, Garg A, et al. Population pharmacokinetic and covariate analyses of intravenous trastuzumab (Herceptin), a HER2-targeted monoclonal antibody, in patients with a variety of solid tumors. Cancer Chemother Pharmacol. 2019;83(2):329–340. [https://doi.org/10.1007/s00280-018-3728-z](https://doi.org/10.1007/s00280-018-3728-z)
<span id="ref-17"></span>17. Han K, Peyret T, Quartino A, Gosselin NH, Gururangan S, Casanova M, et al. Bevacizumab dosing strategy in paediatric cancer patients based on population pharmacokinetic analysis with external validation. Br J Clin Pharmacol. 2016;81(1):148–160. [https://doi.org/10.1111/bcp.12778](https://doi.org/10.1111/bcp.12778)
<span id="ref-18"></span>18. Gibiansky E, Gibiansky L, Chavanne C, Frey N, Jamois C. Population pharmacokinetic and exposure-response analyses of intravenous and subcutaneous rituximab in patients with chronic lymphocytic leukemia. CPT Pharmacometrics Syst Pharmacol. 2021;10(8):914–927. [https://doi.org/10.1002/psp4.12665](https://doi.org/10.1002/psp4.12665)
