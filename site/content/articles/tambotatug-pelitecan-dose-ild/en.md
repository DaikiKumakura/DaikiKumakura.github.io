Tambotatug pelitecan (YL201, Tam-Peli) is an antibody–drug conjugate (ADC) that targets B7-H3 and carries the topoisomerase I inhibitor payload YL0010014. In its phase 1/1b trial, 2.0 mg/kg and 2.4 mg/kg every 3 weeks were evaluated as recommended expansion doses ([1](#ref-1)). A higher dose might increase efficacy, but might also increase myelosuppression and interstitial lung disease (ILD).

**QOI (the question this article tries to answer): Is escalation to 2.4 mg/kg necessary?**

**COU (the use and scope of the analysis): To evaluate efficacy and adverse effects relative to 2.0 mg/kg.**

## Abstract

The public data do not show an efficacy gain from escalating to 2.4 mg/kg, and Grade ≥3 adverse events were higher at 2.4 mg/kg. The tumor-type-standardized difference in confirmed objective response rate (ORR) was 1.9 points (95% credible interval −10.9 to 13.4), which cannot rule out a gain or a loss of around 10 points. For Grade ≥3 treatment-related adverse events (TRAEs), the standardized difference was 17.0 points (3.8 to 29.3), higher at 2.4 mg/kg (background other than tumor type is not adjusted). ILD was 11/324 and 11/335 patients (ratio 0.97, 0.42–2.21); because follow-up and the allocation of patients with metastatic castration-resistant prostate cancer (mCRPC) are not published, whether the doses differ cannot be judged. In the pharmacokinetics (PK) of dose-escalation patients, the ADC AUC0–21d (area under the concentration–time curve to day 21) ratio was 1.53 (1.18–1.98), and the interval spans the dose ratio of 1.2. This is an exploratory comparison between non-randomized cohorts and not a causal effect of the escalation.

## Introduction

Three public sources were used: the phase 1/1b original article (Nature Medicine 2025) and its supplementary information ([1](#ref-1), [2](#ref-2)), and a pooled ILD analysis of 723 patients presented at ESMO 2026 (e-poster) ([3](#ref-3)). The dose groups were not randomized and differ in tumor-type composition, region and follow-up. This article sets out how far group-level tallies alone can answer the question. The mathematical models serve to relate exposure to observations and to show what can be judged.

The analysis plan was not fixed before computing. The tumor-type-standardized comparison, the sensitivity analysis of ILD follow-up and the sensitivity analysis of mCRPC allocation were added while looking at results, so they are exploratory.

## Methods

### Data

PK came from [supplementary Table 5](https://static-content.springer.com/esm/art%3A10.1038%2Fs41591-025-03600-2/MediaObjects/41591_2025_3600_MOESM1_ESM.pdf#page=19) of the original article (phase 1 dose escalation, cycle 1, geometric mean (GM) and geometric coefficient of variation (CV); 9 patients at 2.0 mg/kg and 16 at 2.4 mg/kg) ([2](#ref-2)). Efficacy and safety counts were transcribed from [supplementary Table 7](https://static-content.springer.com/esm/art%3A10.1038%2Fs41591-025-03600-2/MediaObjects/41591_2025_3600_MOESM1_ESM.pdf#page=21) (tallies by dose group for small cell lung cancer (SCLC), nasopharyngeal carcinoma (NPC) and all patients) and from [Table 2](https://doi.org/10.1038/s41591-025-03600-2) of the original article (TRAEs by dose group) ([1](#ref-1), [2](#ref-2)). The safety population is 96 patients at 2.0 mg/kg and 195 at 2.4 mg/kg, and the efficacy-evaluable population 87 and 184 (supplementary Table 7). The dose-expansion cohorts in supplementary Table 1 have 86 and 177 patients; the differences from supplementary Table 7 (10 and 18 patients) may be dose-escalation patients, but the tables do not say so. The "other" tumor stratum was derived as all patients minus SCLC and NPC (a derived value). For ILD, Tables 1–4 and the text of the ESMO 2026 e-poster (data cutoff March 16, 2026) were used ([3](#ref-3), [Tables 1–4](https://medically.roche.com/global/en/oncology/esmo-2026/medical-material/ESMO-2026-poster-siqing-tambotatug-pelitecan-yl201-analyses-of-interstitial-lung-disease-pdf.html)). Individual event and censoring times, and individual pairing of PK with ILD, are not published. The trials of the original article (the supplement uses INT-101-01 and CN-101-01 data) and the pooled analysis (INT-101-01, CN-101-01 and CN-201-01) probably contain overlapping patients. The number of overlapping patients was not checked, but the pooled analysis is not an independent validation set. The e-poster was funded by the sponsors (F. Hoffmann-La Roche and MediLink Therapeutics).

### Analysis of the PK summaries

The log of each geometric mean was taken as $\mathcal{N}(\ln \mathrm{GM}, s^2/n)$ with $s = \sqrt{\ln(1 + \mathrm{CV}^2)}$ computed from the published geometric coefficient of variation (a lognormal assumption; the variance was treated as known, without its own uncertainty). The ratio of the 2.4 mg/kg group to the 2.0 mg/kg group was obtained with a parametric bootstrap of 200,000 draws on the log scale (seed 20261107), with the 2.5th and 97.5th percentiles as the interval, and compared with the dose ratio of 1.2; the table gives the share of bootstrap draws above 1.2 (not a posterior probability). Dose proportionality was assessed by weighted regression of ln(GM) on ln(dose) over the four ADC dose levels from 1.6 to 2.8 mg/kg (a slope of 1 is proportional). This is an analysis of summary values only, not a fit of a population PK model.

The population PK model of the original article ([supplementary Table 4](https://static-content.springer.com/esm/art%3A10.1038%2Fs41591-025-03600-2/MediaObjects/41591_2025_3600_MOESM1_ESM.pdf#page=18)) contains saturable elimination of the ADC (Vmax 2.31 nmol/h, Km 5.1 nM) ([2](#ref-2)). Individual concentrations are not published and it was not refitted here.

### Tumor-type-standardized comparison

For each dose group and stratum (SCLC, NPC, other), the count was modeled as $Y \sim \mathrm{Binomial}(n, p)$ with a Beta(0.5, 0.5) prior on $p$, treating strata and groups independently (no borrowing). Posteriors were summarized with 200,000 draws. The crude difference is the difference between group totals; the standardized difference is the sum of stratum differences weighted by the share of each stratum in the pooled patients of both groups. As a sensitivity to the choice of weights, the stratum shares of the 2.0 mg/kg group and of the 2.4 mg/kg group were also used. As frequentist references, the Newcombe interval and Fisher's exact test for the crude difference and a stratified Mantel–Haenszel odds ratio (Robins–Breslow–Greenland variance) are reported. The strata are tumor types only, with no adjustment for other background.

### Analysis of ILD

For ILD, beta-binomial posteriors per dose group and their difference and ratio were obtained first. As a sensitivity analysis for the difference in follow-up, onset time was assumed lognormal (median 94.5 days; σ of 0.8, 1.0 or 1.3), and follow-up was set (i) fixed at each group's median, (ii) exponential with that median, or (iii) uniform from 0 to twice the median; $F_{\mathrm{eff}}$ is the mean probability that onset occurs within follow-up. The adjusted lifetime risk was taken as the observed risk divided by $F_{\mathrm{eff}}$, and the ratio of 2.4 mg/kg to 2.0 mg/kg was compared. σ = 1.0 is consistent with the poster's median onset time of 94.5 days (range 17–549 days, 22 patients). This sensitivity analysis ignores treatment discontinuation and risk windows and is not an estimate. For mCRPC, all 99 patients (no ILD) were assumed to be in either the 2.0 or the 2.4 mg/kg group, the number assumed to be at 2.4 mg/kg was varied from 0 to 99, and the ratio of ILD proportions among the other patients was computed.

## Results

### ADC exposure ratio and the dose ratio

Figure 1 shows cycle 1 exposure in dose-escalation patients. Table 1 gives ratios of geometric means of the 2.4 mg/kg group to the 2.0 mg/kg group.

![Geometric means with 95% intervals by dose of ADC Cmax and AUC0-21d and free payload AUC0-21d, with 2.0 and 2.4 mg/kg in different colors.](shared/tambotatug-pelitecan-dose-ild/figures/fig1_exposure.png)

Figure 1. Cycle 1 exposure (dose-escalation patients; geometric mean with 95% interval from the geometric CV; blue is 2.0 and orange 2.4 mg/kg). Cmax is the maximum concentration. Computed from supplementary Table 5 ([2](#ref-2)).

Table 1. Exposure ratio, 2.4 mg/kg group over 2.0 mg/kg group (`analysis/01_pk_exposure.py`). The dose ratio is 1.2. GM is the geometric mean; the last column is the share of bootstrap draws in which the ratio exceeds 1.2 (not a posterior probability).

| Analyte | Parameter | GM at 2.0 mg/kg (n = 9) | GM at 2.4 mg/kg (n = 16) | Ratio (95% interval) | Share of draws > 1.2 |
| --- | --- | ---: | ---: | --- | ---: |
| ADC | Cmax, µg/mL | 35.3 | 43.8 | 1.24 (1.02–1.51) | 0.63 |
| ADC | AUC0–21d, µg·h/mL | 1,516 | 2,314 | 1.53 (1.18–1.98) | 0.97 |
| Total antibody | Cmax, µg/mL | 36.5 | 44.3 | 1.21 (1.04–1.42) | 0.56 |
| Total antibody | AUC0–21d, µg·h/mL | 1,670 | 2,320 | 1.39 (1.13–1.71) | 0.92 |
| Free payload | Cmax, ng/mL | 0.917 | 1.061 | 1.16 (0.78–1.72) | 0.43 |
| Free payload | AUC0–21d, ng·h/mL | 96.8 | 124 | 1.28 (0.93–1.78) | 0.65 |

The ADC Cmax ratio of 1.24 nearly matches the dose ratio of 1.2. The AUC0–21d ratio of 1.53 has a point estimate above the dose ratio, but its interval of 1.18–1.98 includes 1.2 and its lower end is close to it. The "share above 1.2 of 0.97" comes from a bootstrap that treats the variance as known, so the true uncertainty is larger. The slopes over 1.6 to 2.8 mg/kg are 1.85 (0.89–2.80) for AUC and 0.95 (0.25–1.64) for Cmax; both intervals include 1. The supplement states that a nonlinear term was added to ADC elimination to define target saturation above 2 mg/kg ([2](#ref-2), [supplementary methods](https://static-content.springer.com/esm/art%3A10.1038%2Fs41591-025-03600-2/MediaObjects/41591_2025_3600_MOESM1_ESM.pdf#page=3)). An AUC ratio above the dose ratio is consistent with some saturable elimination remaining near 2.0 mg/kg, but with 9 and 16 patients and a geometric CV of about 30%, it cannot be distinguished from small-sample variation. Free payload has a large CV (35–53%), and whether exposure rises with the increase cannot be determined.

### Response: crude and tumor-type-standardized differences

In the crude comparison, the confirmed ORR looks higher at 2.0 mg/kg. Figure 2 and Table 2 show the comparison split by tumor type.

![Confirmed ORR difference by SCLC, NPC and other strata, with the crude difference and the standardized difference. After standardization the negative direction of the crude difference disappears.](shared/tambotatug-pelitecan-dose-ild/figures/fig2_orr_strata.png)

Figure 2. Confirmed ORR difference (2.4 − 2.0 mg/kg; posterior median and 95% credible interval). The parentheses in the stratum labels are n/N at 2.0 mg/kg versus n/N at 2.4 mg/kg.

Table 2. Proportions and differences by dose group for confirmed ORR and Grade ≥3 TRAE (2.4 − 2.0 mg/kg; `analysis/02_efficacy_safety.py`). SCLC, NPC and all patients are from supplementary Table 7 ([2](#ref-2)); "other" is derived by subtraction.

| Endpoint | Stratum | 2.0 mg/kg, n/N (%) | 2.4 mg/kg, n/N (%) | Difference, median (95% credible interval), points |
| --- | --- | --- | --- | --- |
| Confirmed ORR | SCLC | 21/31 (67.7) | 23/36 (63.9) | −3.7 (−25.6 to 18.7) |
| Confirmed ORR | NPC | 17/35 (48.6) | 16/34 (47.1) | −1.4 (−24.3 to 21.4) |
| Confirmed ORR | Other (derived) | 4/21 (19.0) | 30/114 (26.3) | 6.8 (−14.1 to 22.3) |
| Confirmed ORR | Crude (all) | 42/87 (48.3) | 69/184 (37.5) | −10.8 (−23.2 to 1.8) |
| Confirmed ORR | Standardized | | | 1.9 (−10.9 to 13.4) |
| Grade ≥3 TRAE | SCLC | 18/36 (50.0) | 27/38 (71.1) | 20.7 (−1.1 to 41.3) |
| Grade ≥3 TRAE | NPC | 18/37 (48.6) | 21/37 (56.8) | 8.0 (−14.3 to 29.8) |
| Grade ≥3 TRAE | Other (derived) | 8/23 (34.8) | 66/120 (55.0) | 19.9 (−2.0 to 39.2) |
| Grade ≥3 TRAE | Crude (all) | 44/96 (45.8) | 114/195 (58.5) | 12.6 (0.4 to 24.5) |
| Grade ≥3 TRAE | Standardized | | | 17.0 (3.8 to 29.3) |

The share of SCLC and NPC in the efficacy-evaluable population is 76% (66/87) in the 2.0 mg/kg group and 38% (70/184) in the 2.4 mg/kg group. Because the 2.0 mg/kg group is weighted toward these two tumor types with high ORR, the crude ORR looks higher at 2.0 mg/kg; this apparent difference is within what tumor-type composition can explain. By stratum, the differences are −3.7 points in SCLC, −1.4 in NPC and +6.8 in the other tumors; the signs differ and every interval includes 0. The standardized difference is 1.9 points (−10.9 to 13.4; posterior probability that it is positive, 0.62), and the stratified Mantel–Haenszel odds ratio was 1.04 (0.58–1.86). With the weights of the 2.0 mg/kg group's tumor mix the difference is −0.4 points, and with the 2.4 mg/kg group's mix it is +3.1 points, so the sign depends on the weights (`outputs/tables/std_weight_sensitivity.csv`). The confirmed ORR for all patients matched the values in [Extended Data Table 1](https://doi.org/10.1038/s41591-025-03600-2) of the original article (48.3% and 37.5%) ([1](#ref-1)). The supplement reports median follow-up of the response population as 6.5 and 7.4 months, and median progression-free survival (PFS) as 7.6 months (95% confidence interval 6.0–7.8) at 2.0 mg/kg and 5.6 months (4.9–7.2) at 2.4 mg/kg ([2](#ref-2), supplementary Table 7). The tumor-type composition differs for PFS and it was not analyzed here.

### Toxicity: Grade ≥3 TRAE and hematologic toxicity

Grade ≥3 TRAE has a higher point estimate at 2.4 mg/kg in all three strata, but every stratum interval includes 0 (Figure 3, Table 2).

![Grade 3 or higher treatment-related adverse event difference by SCLC, NPC and other strata, with the crude difference and the standardized difference. All point estimates are higher at 2.4 mg/kg, but the stratum intervals include 0.](shared/tambotatug-pelitecan-dose-ild/figures/fig3_g3_trae_strata.png)

Figure 3. Grade ≥3 TRAE difference (2.4 − 2.0 mg/kg; posterior median and 95% credible interval).

The standardized difference is 17.0 points (3.8 to 29.3; posterior probability of being positive, 0.99), and the stratified Mantel–Haenszel odds ratio was 1.97 (1.15–3.37). With the weights of the 2.0 mg/kg group's mix the difference is 15.5 points, and with the 2.4 mg/kg group's mix 17.7 points, so it changes little. The crude difference is 12.6 points (0.4 to 24.5; Fisher's exact test p = 0.046), and it becomes larger on standardization. The 2.0 mg/kg group is weighted toward SCLC and NPC, whose Grade ≥3 TRAE proportions in that group are higher than in "other" (34.8%), so the crude difference looks smaller than the within-stratum differences. At 2.4 mg/kg, however, NPC (56.8%) and "other" (55.0%) are close. Region (in the pooled analysis of the ESMO poster, 98.5% of the 2.4 mg/kg group is Asian) and treatment duration are not adjusted, and the difference may include their effects.

Table 3 gives the item-by-item comparison, centered on hematologic toxicity. It is a crude comparison, not standardized for tumor type.

Table 3. Number of patients with TRAEs by dose group and differences (crude comparison, 2.4 − 2.0 mg/kg; `analysis/02_efficacy_safety.py`; counts from Table 2 of the original article ([1](#ref-1))). SAE is serious adverse event.

| Endpoint | 2.0 mg/kg (n = 96) | 2.4 mg/kg (n = 195) | Difference, median (95% credible interval), points | Fisher exact p |
| --- | --- | --- | --- | ---: |
| Grade ≥3 leukopenia | 17 (17.7%) | 70 (35.9%) | 18.0 (7.5 to 27.8) | 0.002 |
| Grade ≥3 neutropenia | 21 (21.9%) | 72 (36.9%) | 14.9 (4.0 to 25.2) | 0.011 |
| Grade ≥3 anemia | 15 (15.6%) | 55 (28.2%) | 12.4 (2.4 to 21.6) | 0.020 |
| Grade ≥3 lymphopenia | 15 (15.6%) | 41 (21.0%) | 5.3 (−4.4 to 14.1) | 0.34 |
| Grade ≥3 thrombocytopenia | 9 (9.4%) | 31 (15.9%) | 6.4 (−1.8 to 13.8) | 0.15 |
| TRAE led to discontinuation | 5 (5.2%) | 11 (5.6%) | 0.3 (−5.9 to 5.5) | 1.00 |
| TRAE led to dose reduction | 13 (13.5%) | 38 (19.5%) | 5.9 (−3.4 to 14.3) | 0.25 |
| TRAE led to interruption | 38 (39.6%) | 70 (35.9%) | −3.7 (−15.6 to 7.9) | 0.61 |
| TRAE with death | 1 (1.0%) | 6 (3.1%) | 1.8 (−2.0 to 5.2) | 0.43 |
| Treatment-related SAE | 23 (24.0%) | 64 (32.8%) | 8.8 (−2.3 to 19.2) | 0.14 |

Of the five hematologic Grade ≥3 items, three (leukopenia, neutropenia and anemia) are more frequent at 2.4 mg/kg, whereas the intervals for lymphopenia and thrombocytopenia include 0. Leukopenia and neutropenia are related items and not independent findings. The proportions of TRAEs that led to discontinuation, dose reduction or interruption differ little. There are many items and no multiplicity correction was made, so the p values are exploratory. Supplementary Figure 7 shows logistic regressions of exposure and response in dose-escalation patients ([2](#ref-2), [supplementary Figure 7](https://static-content.springer.com/esm/art%3A10.1038%2Fs41591-025-03600-2/MediaObjects/41591_2025_3600_MOESM1_ESM.pdf#page=11)), but it is an image, its direction of effect was not read, and it was not used here.

### ILD: follow-up and tumor-type composition

In the ESMO 2026 pooled analysis, ILD/pneumonitis was 11/324 (3.4%) at 2.0 mg/kg and 11/335 (3.3%) at 2.4 mg/kg (Figure 4). By grade, 2.0 mg/kg had 3 Grade 1, 4 Grade 2 and 4 Grade 3 patients, and 2.4 mg/kg had 2, 4 and 5; there was no Grade 4 or 5 ([3](#ref-3), Table 2).

![Posterior density of ILD probability by dose group and the number of patients by grade.](shared/tambotatug-pelitecan-dose-ild/figures/fig4_ild.png)

Figure 4. ILD/pneumonitis at 2.0 and 2.4 mg/kg. Left, posterior density (Jeffreys prior); right, patients by grade.

The crude difference is −0.1 points (−2.9 to 2.7), the ratio 0.97 (0.42–2.21) and Fisher's exact test p = 1.00. The posterior probability that the ratio exceeds 1.5 is 0.15. The median time to onset is reported as 94.5 days (range 17–549 days) for all grades and 67 days (range 21–144 days) for Grade 3 ([3](#ref-3)). At the time of the phase 1 original article (312 patients), ILD was 4 patients (1.3%): 2/96 (2.1%) at 2.0 mg/kg and 2/195 (1.0%) at 2.4 mg/kg ([1](#ref-1), Table 2). The pooled analysis has 22 patients with ILD (3.0%), consistent with a larger population and longer follow-up.

Median follow-up is reported as 9.2 months at 2.0 mg/kg and 16.8 months at 2.4 mg/kg ([3](#ref-3)). With the same number of events, the longer-followed 2.4 mg/kg group had more opportunity to show events. Table 4 and the left panel of Figure 5 give the follow-up-adjusted lifetime risk ratio of 2.4 mg/kg to 2.0 mg/kg when the onset-time distribution and the follow-up model are changed.

Table 4. Sensitivity to follow-up (ILD, 2.4 mg/kg / 2.0 mg/kg; `analysis/03_ild.py`). All nine combinations. Onset time is lognormal (median 94.5 days). F_eff is the mean probability that onset is observed within follow-up.

| σ | Follow-up model | F_eff at 2.0 mg/kg | F_eff at 2.4 mg/kg | Adjusted risk ratio, median (95% credible interval) |
| ---: | --- | ---: | ---: | --- |
| 0.8 | Fixed at median | 0.913 | 0.983 | 0.90 (0.39–2.05) |
| 0.8 | Exponential | 0.751 | 0.848 | 0.86 (0.38–1.96) |
| 0.8 | Uniform | 0.773 | 0.873 | 0.86 (0.38–1.96) |
| 1.0 | Fixed at median | 0.861 | 0.954 | 0.87 (0.38–1.99) |
| 1.0 | Exponential | 0.732 | 0.832 | 0.85 (0.37–1.95) |
| 1.0 | Uniform | 0.745 | 0.852 | 0.85 (0.37–1.93) |
| 1.3 | Fixed at median | 0.798 | 0.903 | 0.86 (0.38–1.95) |
| 1.3 | Exponential | 0.705 | 0.804 | 0.85 (0.37–1.94) |
| 1.3 | Uniform | 0.707 | 0.815 | 0.84 (0.37–1.92) |

With σ = 1.0, 13.9% of onsets occur later than 9.2 months and 4.6% later than 16.8 months. Across the nine combinations the adjusted median ratio is 0.84 to 0.90, slightly below the observed ratio of 0.97 and small against the width of the interval (about 0.37–2.05). The longer-followed 2.4 mg/kg group has more opportunity to show events, and correcting for that moves the ratio downward. This is stated as a direction only. The onset-time distribution rests on events observed within follow-up, so its right tail may be missing, and the size of the correction may be too small or too large. The interval does not include the uncertainty of $F_{\mathrm{eff}}$, and follow-up was used, not treatment duration.

![Follow-up-adjusted lifetime risk ratio of ILD for 2.4 versus 2.0 mg/kg under nine assumptions, and the ratio when the number of mCRPC patients allocated to 2.4 mg/kg is varied.](shared/tambotatug-pelitecan-dose-ild/figures/fig5_ild_sensitivity.png)

Figure 5. Sensitivity analyses of ILD. Left, the follow-up model; right, the effect of the unpublished allocation of the mCRPC patients (99 patients, no ILD).

The pooled analysis includes 99 patients with mCRPC, with no ILD (the numbers per dose group are not reported). Assuming that all 99 are in either the 2.0 or the 2.4 mg/kg group: if all of them were allocated to 2.4 mg/kg, the ILD proportion among the other patients would be 3.4% (11/324) at 2.0 mg/kg and 4.7% (11/236) at 2.4 mg/kg, a ratio of 1.37. If all were allocated to 2.0 mg/kg, it would be 4.9% (11/225) versus 3.3%, a ratio of 0.67 (right panel of Figure 5; `outputs/tables/ild_mcrpc_allocation.csv`). This range of 0.67–1.37 has the extreme allocations as its end points. The follow-up adjustment (0.84–0.90) is a value under an assumed distribution, so the two are not on the same scale. The assumption ignores that mCRPC patients may also be among the 52 patients at 1.6 mg/kg or the 12 patients of unknown dose (723 − 324 − 335 − 52). In addition, the proportion of Asian patients is 72.8% in the 2.0 mg/kg group and 98.5% in the 2.4 mg/kg group, and prior thoracic radiotherapy is 6.2% versus 4.2%, suggesting that region and the participating cohorts differ between the groups ([3](#ref-3), Table 1). The ESMO poster states that the low ILD rates support continued development at 1.6 and 2.0 mg/kg ([3](#ref-3)).

### Benefit and harms side by side

Figure 6 places efficacy and the main harms side by side without combining them.

![Standardized confirmed ORR difference, standardized Grade 3 or higher TRAE difference, neutropenia, anemia, treatment-related death, discontinuation and the crude ILD difference with intervals, side by side.](shared/tambotatug-pelitecan-dose-ild/figures/fig6_benefit_harm.png)

Figure 6. Differences between 2.4 and 2.0 mg/kg (posterior median and 95% credible interval). Values from different data sets (phase 1/1b and the pooled analysis) are placed together; they are not joint probabilities within the same patients.

The ORR difference is near 0 (1.9 points; −10.9 to 13.4), the intervals for Grade ≥3 TRAE (17.0 points) and Grade ≥3 neutropenia (14.9 points) lie above 0, and ILD is near 0 (−0.1 points).

## Discussion

On the QOI, the public data show three things. First, an ORR gain from 2.4 mg/kg cannot be confirmed. The crude ORR looks lower at 2.4 mg/kg, but this is within what tumor-type composition can explain, and after standardization it is 1.9 points (−10.9 to 13.4). The interval is wide and cannot rule out a gain or a loss of around 10 points, but there is no evidence of a gain. Second, Grade ≥3 TRAE was higher at 2.4 mg/kg. The point estimates were in the same direction in all three strata, but every stratum interval includes 0, and region and treatment duration are not adjusted. Grade ≥3 leukopenia, neutropenia and anemia were also more frequent at 2.4 mg/kg (crude comparison, no correction). Third, ILD cannot be judged.

Exposure is about 1.5 times higher in ADC AUC at 2.4 mg/kg than at 2.0 mg/kg; the point estimate is above the dose ratio of 1.2, but the interval includes the dose ratio. Free payload AUC is 1.3 times with a wide interval. Toxicity may be related to exposure, but data pairing individual PK with toxicity are not published and were not estimated here.

On ILD, correcting for the difference in follow-up moves the ratio down to about 0.85. The correction, however, rests on assumptions about the onset-time distribution and the shape of follow-up. The uncertainty from the unknown allocation of mCRPC is wider, with the ratio moving over 0.67 to 1.37, but this range has extreme allocations as its end points. The interval of the crude ratio of 0.97 (0.42–2.21) includes both a doubling and a halving of ILD. With only 11 events in each group, equivalence of ILD between doses cannot be judged from the public data. Nearly equal observed proportions of ILD are not evidence that the true hazards are equal.

As a judgment on the value of escalation, the public data stay at "no efficacy gain confirmed, and an increase in myelosuppression observed." This supports 2.0 mg/kg as a candidate dose, but it does not show that 2.4 mg/kg fails to increase efficacy. Because the dose groups differ in tumor type, region and observation period, it is not a causal effect of dose.

## Limitations

- **Non-randomized cohorts:** the 2.0 mg/kg and 2.4 mg/kg groups differ in tumor type, region and follow-up. Standardization is by tumor type only, with no adjustment for other background (number of prior therapies, performance status (PS), region, tumor burden, treatment duration). The standardized difference also depends on the choice of weights (−0.4 to +3.1 points for ORR).
- **The "other" stratum:** it is a heterogeneous mix of many tumor types; the 2.0 mg/kg group has only 21 patients in it (23 for safety) yet it carries about half of the standardization weight. The "all patients" of supplementary Table 7 may include dose-escalation patients, and their share may differ between groups.
- **Derived values:** the counts of the "other" stratum are derived as all patients minus SCLC and NPC.
- **PK:** summary values of dose-escalation patients (9 and 16 per group), not individual data and not exposure in the expansion cohorts. Because the variance was treated as known, the intervals and the "share above 1.2" are optimistic. No population PK model was fitted, and exposure was not linked to efficacy or toxicity at the individual level.
- **ILD follow-up:** the follow-up sensitivity analysis rests on assumptions about the onset-time distribution (lognormal, from the median and range of the observed events; because only events within follow-up are observed, the right tail may be missing) and the shape of follow-up. The interval does not include the uncertainty of $F_{\mathrm{eff}}$. Individual event times, censoring times and treatment discontinuation are not published, and no time-dependent hazard model was fitted.
- **mCRPC allocation:** the numbers of the 99 patients per dose group are not published. The sensitivity analysis assumes that all 99 are in the two dose groups and does not handle the 12 patients of unknown dose.
- **Overlap:** the patients of the original article and of the pooled analysis overlap to some extent, so the pooled analysis is not an independent validation set (the number of overlapping patients was not checked). ILD rose from 4 patients at the phase 1 time point (312 patients) to 22 in the pooled analysis.
- **Sponsor:** the e-poster was funded by Roche and MediLink Therapeutics. The conclusion statements of the poster are the interpretation of its authors including the sponsor and are not evaluated here.
- **Unused sources:** supplementary Figure 7 (exposure–response) is an image and was not used. The primary source of the ILD figure from the phase 3 TAISHAN-302 (11/224, quoted in the e-poster) was not read. The ESMO 2026 poster comparing 1.6 and 2.0 mg/kg in non-small cell lung cancer (NSCLC) was not read.
- **PFS:** median PFS by dose group is described only and was not analyzed.
- **Multiplicity and exploration:** item-wise p values and credible intervals are exploratory values without correction. The analysis plan was not fixed in advance.

## Conclusion

On the QOI (is escalation to 2.4 mg/kg necessary), the public data support the following. An ORR gain from escalation to 2.4 mg/kg cannot be confirmed (the tumor-type-standardized difference is 1.9 points, −10.9 to 13.4; the interval cannot rule out a gain or a loss of around 10 points). The crude ORR looks lower at 2.4 mg/kg, which is explained by SCLC and NPC, with high ORR, being concentrated in the 2.0 mg/kg group. On the other hand, Grade ≥3 TRAE was higher at 2.4 mg/kg (standardized difference 17.0 points, 3.8 to 29.3; region and treatment duration not adjusted), with point estimates in the same direction in all three strata. ILD is 11/324 and 11/335; adjustment for the difference in follow-up changes the ratio only slightly to 0.84–0.90, but because the allocation of mCRPC patients is unknown the range is 0.67–1.37 and equivalence cannot be judged. This is a comparison between non-randomized cohorts and not a causal effect of escalation. The public data give no efficacy evidence that supports the necessity of escalation.

## Data and code availability

The re-run materials (scripts in `analysis/`, input CSVs and the provenance record in `inputs/`, tables, figures and logs in `outputs/`) are in the [companion archive](shared/tambotatug-pelitecan-dose-ild/tambotatug-pelitecan-dose-ild-companion.zip). The input CSVs hold counts and summary values transcribed from the tables of the original article and supplement ([1](#ref-1), [2](#ref-2)) and the e-poster ([3](#ref-3)); the original files are not bundled. The "other" stratum is a derived value (`inputs/PROVENANCE.md`). Re-run: `python analysis/01_pk_exposure.py && python analysis/02_efficacy_safety.py && python analysis/03_ild.py && python analysis/04_figures.py` (Windows 11, Python 3.12.4, numpy 2.2.6, pandas 2.2.2, scipy 1.14.0, matplotlib 3.9.1). The random seed is 20261107.

## References

<span id="ref-1"></span>1. Ma Y, Yang Y, Huang Y, Fang W, Xue J, Meng X, et al. A B7H3-targeting antibody–drug conjugate in advanced solid tumors: a phase 1/1b trial. Nat Med. 2025;31(6):1949–1957. [doi:10.1038/s41591-025-03600-2](https://doi.org/10.1038/s41591-025-03600-2).

<span id="ref-2"></span>2. Ma Y, Yang Y, Huang Y, Fang W, Xue J, Meng X, et al. Supplementary Information: Supplementary Methods, Results, Figures 1–7 and Tables 1–8 [Supplementary material]. In: A B7H3-targeting antibody–drug conjugate in advanced solid tumors: a phase 1/1b trial. Nat Med. 2025;31(6):1949–1957. File 41591_2025_3600_MOESM1_ESM.pdf. Available from: https://static-content.springer.com/esm/art%3A10.1038%2Fs41591-025-03600-2/MediaObjects/41591_2025_3600_MOESM1_ESM.pdf

<span id="ref-3"></span>3. Fu S, Rohatgi A, Liu S, Zugazagoitia J, Doger de Speville B, Gambardella V, et al. Tambotatug pelitecan (YL201): analyses of interstitial lung disease in patients with advanced solid tumors from phase 1/2 studies [Conference poster]. ESMO Congress 2026; 2026 Oct 23–27; Madrid. Roche Medically [Internet]; 2026 Oct 23 [cited 2026 Nov 7]. Available from: https://medically.roche.com/global/en/oncology/esmo-2026/medical-material/ESMO-2026-poster-siqing-tambotatug-pelitecan-yl201-analyses-of-interstitial-lung-disease-pdf.html
