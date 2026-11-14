**QOI: To what extent does elimination half-life explain the approved dosing frequency (once daily or not) of oral small-molecule drugs?**

**COU: When a regimen is being considered for a new oral drug, to judge whether a half-life value can serve as a rule of thumb for "once daily or more often". It describes approved drugs and is not used to decide a regimen or to make a causal claim.**

QOI (question of interest) is the question this article answers, and COU (context of use) is what the answer is used for. Here "explain" means the strength of the descriptive association between half-life and the approved dosing frequency, checked by out-of-sample prediction; no cause is claimed. The data are the 93 single-ingredient drugs with a half-life value among the 104 oral small-molecule drugs approved by the US Food and Drug Administration (FDA) in 2020–2024; the half-life and dosing frequency of each drug come from the supplementary data of the paper by Brown ([1](#ref-1), [2](#ref-2)).

**Answer: half-life is only a weak cue for whether a drug is dosed once daily.** A longer half-life went with less dosing at two or three times a day (odds ratio 0.78 per doubling of half-life, 95% interval 0.58–0.98; the upper end is close to 1). In out-of-sample evaluation, in which each drug is predicted after being left out, no difference from always predicting the base rate (29 of 93 drugs, 31%) could be shown: Brier score 0.216 against 0.219. This does not mean there is no information, but small differences cannot be distinguished. The share dosed twice or three times daily was 42% (10 of 24 drugs) with a half-life under 6 h and 24% (8 of 34 drugs) at 24 h or more, in the direction expected from pharmacokinetics. Yet 14 drugs with a half-life under 6 h were dosed once daily and 8 drugs with a half-life of 24 h or more were dosed more than once daily, so both groups contain a number of drugs that go the other way.

Abbreviations: QD, once daily; BID, twice daily; TID, three times daily; FIC, first-in-class (a new mechanism of action); orphan, orphan drug designation; $t_{1/2}$, elimination half-life in hours; M0, M1 and M2, the models described below.

## Introduction

Brown tabulated dose, dosing frequency, human pharmacokinetics and drug-drug interactions for 104 oral small-molecule drugs approved by the FDA in 2020–2024 ([1](#ref-1)). The approved frequency was QD for 67%, BID for 28% and TID for 4%, with one weekly drug (tovorafenib, under 1%) (text of section 1 and Figure 1 of the original article). BID or TID was used for 50% of FIC drugs against 19% of other drugs, and for 41% of orphan drugs against 20% of other drugs (Abstract and section 1 text of the original article). The median half-life was 14.8 h for 104 drugs ([original Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl3)), and the definition of the half-life value differs by source: terminal-phase, mean, effective, or population pharmacokinetic estimate ([1](#ref-1)).

Half-life is the time for a concentration to fall by half, so a drug with a shorter half-life loses concentration faster. The expectation that this makes shorter dosing intervals more likely is a hypothesis to be tested. This article counts how well that expectation fits the actual approved frequencies, using half-life as the only input. Why a given drug ended up with its regimen is not in the data and is not addressed.

## Methods

### Data and classification

The input is the supplementary data file of Brown's paper, `jm5c02863_si_002.xlsx`, which has two sheets (`Sheet1` and `Dose_and_Class`) ([2](#ref-2)). The publisher's file is not redistributed (how to obtain it and its SHA256 are recorded in the companion archive). The 104 rows of `Dose_and_Class` were treated as one approved entry each, and a combination product counts as one entry.

Dosing frequency was normalised from the `Dose_and_Class` label to QD (including "QD (or less)" and cyclic regimens such as 21 days on and 7 days off), BID, TID and once weekly. The outcome was 1 for BID or TID (more than once daily) and 0 for QD or once weekly. One drug labelled "QD or BID" (maralixibat) was excluded from the primary analysis, and both codings were tried in a sensitivity analysis. FIC and orphan flags were taken from `Dose_and_Class` and checked against `Sheet1`.

For the primary analysis the half-life of the parent drug was used. The cells are text and mix ranges ("32 to 57"), days ("6-9 days"), mean ± SD and patient-group values. Ranges were converted to the geometric mean of the bounds, days were multiplied by 24, and all 94 distinct strings were confirmed to be readable before any analysis. Combination entries (10) were left out of the primary analysis because their components have different half-lives and the frequency is set for the combination as a whole. The primary set is the 93 single-ingredient entries with a half-life value and an unambiguous frequency label (hereafter, 93 drugs).

### Half-life bins

Half-life was divided into six bins (under 3, 3–6, 6–12, 12–24, 24–48 and 48 h or more), and the share dosed BID or TID with a Wilson 95% interval was computed for each bin ([3](#ref-3)).

### Prediction models and evaluation

The outcome is binary (more than once daily or not), and logistic regression was used. M0 is the base rate (the share in the training data), M1 uses only the base-2 logarithm of half-life, and M2 adds four terms to M1: FIC, orphan, oncology indication and presence of an active metabolite. No further model search was done. A weak L2 penalty (inverse strength C = 100) was used for all models.

Evaluation used leave-one-out (LOO; each entry is a separate drug, so no ingredient is split between training and evaluation) and leave-one-disease-group-out (LOGO; six groups: oncology, neuroscience, metabolic/renal/cardiovascular, infection, immunology/gastroenterology and other). The metrics were the Brier score (the mean squared difference between predicted probability and outcome; lower is better) ([4](#ref-4)), log loss (the mean negative log-likelihood of the predicted probabilities, in nats; lower is better) ([5](#ref-5)), AUC (area under the receiver operating characteristic curve, a measure of how well predictions rank the drugs), and the calibration intercept and slope ([6](#ref-6)), all computed on pooled out-of-sample predictions. Intervals are percentile intervals from 2,000 bootstrap resamples of the entries ([7](#ref-7)) with the out-of-sample predictions held fixed (an approximation: the model is not refitted within each resample). This approximation leaves out the variation due to the training data, so the intervals are biased toward being too narrow. The random seed was 20261114.

Only the interval of the half-life coefficient (slope) was obtained by refitting the model in each resample. Rules that predict "more than once daily" when the half-life is below 6, 8 or 12 h were also evaluated. For these rules, besides accuracy, the positive predictive value (PPV, the share of drugs predicted "more than once daily" that really were) and the positive likelihood ratio (LR+, sensitivity divided by 1 − specificity) were computed.

### Reference curve

The fraction of the peak concentration of one dose that remains at the end of the dosing interval was written as $2^{-\tau/t_{1/2}}$ ($\tau$ is the dosing interval in hours), assuming one compartment, instantaneous absorption and first-order elimination. In a linear model, accumulation on repeated dosing raises the absolute concentrations but does not change the steady-state trough-to-peak ratio $2^{-\tau/t_{1/2}}$. The calculation ignores slow absorption, non-linear drugs, delay of drug effect and active metabolites. It is a reference determined by half-life and was not fitted to the data.

### Label check

Before the analysis, after the rows of the supplementary data had been listed, 10 entries were chosen to spread across approval years and to include atypical frequency or half-life entries, and the dosing frequency and half-life in the workbook were compared with the current US prescribing information on DailyMed: selpercatinib, finerenone, avacopan, maralixibat, futibatinib, olutasidenib, ganaxolone, daprodustat, ritlecitinib and tovorafenib ([8](#ref-8)). Eight of the 10 (selpercatinib, finerenone, avacopan, futibatinib, olutasidenib, ganaxolone, daprodustat and ritlecitinib) are among the 22 drugs of Figure 5 below. The sample is not representative.

### Record of the analysis plan

The classification definitions, the handling of ambiguous labels, the half-life bin edges, the thresholds and the 10 drugs to check were written in the README of the companion materials after the rows of the supplementary data (including the half-life values) had been listed once and before any model was fitted. They are therefore not blind to the data. The record has no timestamp, hash or commit, so the timing cannot be checked from outside. Analyses added after the first results were seen are the sensitivity analysis excluding drugs later withdrawn after approval, the PPV and LR+ of the threshold rules, and the check of the artefact in the LOO base rate.

## Results

### Data check

Table 1 compares values recounted from the workbook with those Brown reported in the text (`analysis/01_build_dataset.py`). The frequency shares and the shares by FIC and orphan status matched (exactly, if maralixibat is counted as QD; see the note to the table). The counts per approval year differed by one in 2022 and 2023 (13 and 24 in the workbook, 12 and 25 in the text). The cause was not traced.

Table 1. Values recounted from the workbook and values in Brown's text. The parentheses in the right column give where the value is stated in the original article.

| Item | Recounted from the workbook | Reported in the original article (location) |
|---|---|---|
| Entries | 104 | 104 (Abstract) |
| Entries per approval year (2020, 2021, 2022, 2023, 2024) | 22, 24, 13, 24, 21 | 22, 24, 12, 25, 21 (text introducing original Table 1) |
| Once daily (QD, including "QD or less") | 69 (66.3%) | 67% (section 1 text) |
| Twice daily (BID) | 29 (27.9%) | 28% (section 1 text) |
| Three times daily (TID) | 4 (3.8%) | 4% (section 1 text) |
| Less often than once daily | 1 (1.0%, tovorafenib weekly) | <1% (section 1 text) |
| Labelled "QD or BID" | 1 (maralixibat) | not stated |
| BID or TID among FIC / non-FIC entries | 21/42 (50.0%) / 12/61 (19.7%) | 50% / 19% (Abstract; section 1 text) |
| BID or TID among orphan / non-orphan entries | 24/58 (41.4%) / 9/45 (20.0%) | 41% / 20% (Abstract; section 1 text) |
| Half-life, median (quartiles) | 15.0 h (5.7–32.0 h), n = 93 single-ingredient entries | 14.8 h (6–30.8 h), n = 104 (original Table 3) |

Note: QD, BID, TID and FIC are defined at the start of the article. The denominator of the frequency shares is 104. The FIC and orphan shares use the 103 entries without maralixibat. If maralixibat (`Sheet1`: QD, not FIC, orphan) is counted as QD, QD is 70/104 (67.3%), BID or TID among non-FIC entries is 12/62 (19.4%) and among orphan entries 24/59 (40.7%), matching Brown's 67%, 19% and 41%. With combinations included at the shortest component half-life, the median of 102 entries was 13.0 h; at the longest component, 14.0 h. The frequency labels in `Sheet1` and `Dose_and_Class` agree for the 103 entries other than maralixibat; the FIC flag differs between two columns for 6 entries (`Dose_and_Class` was used). The orphan flag did not differ. The locations in the original article are the text before [original Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl1), the text of section 1, and [original Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl3) ([1](#ref-1)).

Figure 1 shows the data flow. From 104 entries, 10 combinations and maralixibat were removed, leaving 93 entries in the primary set, of which 29 were BID or TID and 64 QD or weekly.

![Flow from 104 approved entries, with 10 combination entries and maralixibat removed, to the primary set of 93 entries (29 BID or TID, 64 QD or weekly).](shared/oral-drug-halflife-dosing-frequency/figures/fig1_data_audit_flow.png)

Figure 1. Data flow. Grey boxes are entries left out of the primary analysis; the blue box is the primary set.

### Half-life and dosing frequency

Figure 2 and Table 2 give the share dosed BID or TID by half-life bin. The share went up and down by bin and was not monotone. The under-3 h bin was low at 20% (2 of 10 drugs), the 3–6 h bin was highest (8 of 14 drugs, 57%) and the 48 h or more bin was lowest (2 of 15, 13%). The 24–48 h bin was 32% (6 of 19), higher than the 12–24 h bin (18%). The Spearman rank correlation between half-life and the outcome was −0.20 (n = 93, p = 0.051), a borderline exploratory reference value.

![Share dosed BID or TID by half-life bin with Wilson 95% intervals, overlaid with the logistic fit, the base rate and the reference curve for the fraction of peak concentration left at 24 h.](shared/oral-drug-halflife-dosing-frequency/figures/fig2_halflife_vs_multi_daily.png)

Figure 2. Share dosed BID or TID by half-life bin (blue points with Wilson 95% intervals; counts above the points), logistic regression on log half-life (orange) and base rate (dotted). The red dashed line is the reference curve $2^{-24/t_{1/2}}$ for the QD interval (24 h) (right axis) under a one-compartment assumption; it was not fitted to the data. BID or TID means dosed twice or three times daily.

Table 2. Share dosed BID or TID by half-life bin (`analysis/02_models.py`).

| Half-life bin (h) | Entries | BID or TID | Share | Wilson 95% interval |
|---|---|---|---|---|
| <3 | 10 | 2 | 20.0% | 5.7–51.0% |
| 3–6 | 14 | 8 | 57.1% | 32.6–78.6% |
| 6–12 | 18 | 8 | 44.4% | 24.6–66.3% |
| 12–24 | 17 | 3 | 17.6% | 6.2–41.0% |
| 24–48 | 19 | 6 | 31.6% | 15.4–54.0% |
| >=48 | 15 | 2 | 13.3% | 3.7–37.9% |

Note: 93 single-ingredient entries. ">=48" means 48 h or more. BID and TID are defined at the start of the article.

In the full-data logistic regression (M1), the slope was −0.244 on the log-odds scale per doubling of half-life (odds ratio 0.78), with a bootstrap 95% interval, refitted in each resample, of −0.540 to −0.020 (odds ratio 0.58–0.98). The upper end of the interval is close to 0. The fitted probability was 0.47 at a half-life of 2 h, 0.37 at 6 h, 0.27 at 24 h and 0.18 at 96 h. The observed share moves from 20% in the under-3 h bin to 57% in the 3–6 h bin, which does not fit a monotone logistic curve. The sign of the slope did not change across the sensitivity analyses (−0.220 to −0.294).

### Out-of-sample prediction

Figure 3 and Table 3 give the out-of-sample performance. The Brier score of M1 (half-life only) was 0.216 (95% interval 0.179–0.253) under LOO, against 0.219 (0.182–0.256) for the base-rate model M0, a difference of −0.003 (−0.019 to 0.014). The difference in log loss was −0.009 (−0.047 to 0.031), and leaving out whole disease groups (LOGO) also gave no difference (difference in Brier score 0.000). The AUC of M1 was 0.575 (0.456–0.698), an interval that contains 0.5. The LOO base-rate model M0 includes an artefact: leaving one drug out shifts the training base rate in the opposite direction, so its Brier score is 0.0047 larger than the in-sample base-rate Brier score (0.2146). This is about the size of the difference between M1 and M0 (−0.003).

For M2 (half-life plus four terms) the Brier score was 0.202 (0.158–0.247), a difference from M1 of −0.015 (−0.049 to 0.020), and the AUC was 0.693 (0.578–0.799). The interval of the difference contains 0, so with these numbers it cannot be said that the four added terms (FIC, orphan, oncology indication, active metabolite) improve out-of-sample prediction. In M2 the point estimates for FIC and orphan are positive (odds ratios 3.6 and 4.5), in the same direction as the difference in shares Brown reported, but no interval was computed for them and these numbers are not interpreted. These two terms overlap with disease area. When the oncology group is held out in LOGO, the oncology indicator is constant in the training data and its coefficient cannot be estimated (the penalty shrinks it to zero).

![Out-of-sample Brier score (left) and log loss (right) for the models M0 base rate, M1 half-life only and M2 half-life plus four terms, with bootstrap 95% intervals.](shared/oral-drug-halflife-dosing-frequency/figures/fig3_model_comparison.png)

Figure 3. Out-of-sample Brier score (left) and log loss (right, in nats); lower is better. Circles are LOO (leave-one-out) and squares LOGO (leave-one-disease-group-out). M0 is the base rate, M1 uses half-life only, and M2 adds FIC, orphan, oncology indication and presence of an active metabolite to half-life. Intervals are percentile 95% intervals from resampling the entries, with the out-of-sample predictions held fixed.

Table 3. Out-of-sample performance (n = 93, 29 entries BID or TID, `analysis/02_models.py`).

| Evaluation | Model | Brier score (95% interval) | Log loss, nats (95% interval) | AUC (95% interval) |
|---|---|---|---|---|
| Leave-one-out | M0 base rate | 0.219 (0.182–0.256) | 0.632 (0.553–0.710) | not defined |
| Leave-one-out | M1 log2 half-life | 0.216 (0.179–0.253) | 0.623 (0.541–0.705) | 0.575 (0.456–0.698) |
| Leave-one-out | M2 M1 + FIC, orphan, oncology, active metabolite | 0.202 (0.158–0.247) | 0.584 (0.483–0.694) | 0.693 (0.578–0.799) |
| Leave-one-disease-group-out | M0 base rate | 0.218 (0.182–0.255) | 0.628 (0.553–0.706) | not defined |
| Leave-one-disease-group-out | M1 log2 half-life | 0.218 (0.180–0.256) | 0.627 (0.544–0.711) | 0.578 (0.460–0.701) |
| Leave-one-disease-group-out | M2 M1 + FIC, orphan, oncology, active metabolite | 0.197 (0.154–0.243) | 0.576 (0.469–0.691) | 0.709 (0.595–0.812) |

Note: M0 is a constant prediction (the share in the training data), so no AUC is computed for it. Lower is better for Brier score and log loss; higher is better for AUC. AUC is the area under the ROC curve.

The out-of-sample calibration slope was 0.44 for M1 and 0.63 for M2, both below 1: observed shares differed less than the predicted probabilities did (Figure 4). When the signal in half-life is weak, the LOO calibration slope tends to come out small, so the value itself may be biased. Each of the four groups has about 23 entries, and the intervals are wide.

![Mean predicted probability and observed share dosed BID or TID by quartile of out-of-sample prediction, with Wilson 95% intervals, for M1 and M2.](shared/oral-drug-halflife-dosing-frequency/figures/fig4_calibration.png)

Figure 4. LOO calibration. Points are quartile groups of predicted probability (about 23 entries each), and vertical lines are Wilson 95% intervals. The diagonal is perfect calibration. M1 is the half-life-only model and M2 adds four terms.

### Simple threshold rules

Table 4 gives the performance of rules that predict "more than once daily" when the half-life is below a threshold. At no threshold could accuracy be distinguished from the 68.8% (64/93) of the rule that predicts QD for every drug (the interval for the 6 h rule, 54.4–73.5%, contains 68.8%). Accuracy is a poor metric when "more than once daily" is 31% of the sample. With the 6 h threshold, specificity was 78.1% but sensitivity was 34.5%, missing 19 of the 29 drugs dosed more than once daily. The PPV was 41.7% (24.5–61.2%), somewhat above the base rate of 31.2%, and LR+ was 1.58. There is a weak signal above the base rate, but the interval is wide.

Table 4. Performance of threshold rules (n = 93, `analysis/02_models.py`).

| Rule: predict BID or TID if half-life is below | Sensitivity (Wilson 95% interval) | Specificity (Wilson 95% interval) | Accuracy (Wilson 95% interval) | PPV (Wilson 95% interval) | LR+ |
|---|---|---|---|---|---|
| 6 h | 34.5% (19.9–52.7%) | 78.1% (66.6–86.5%) | 64.5% (54.4–73.5%) | 41.7% (24.5–61.2%) | 1.58 |
| 8 h | 48.3% (31.4–65.6%) | 75.0% (63.2–84.0%) | 66.7% (56.6–75.4%) | 46.7% (30.2–63.9%) | 1.93 |
| 12 h | 62.1% (44.0–77.3%) | 62.5% (50.3–73.3%) | 62.4% (52.2–71.5%) | 42.9% (29.1–57.8%) | 1.66 |

Note: The positive class is BID or TID. PPV, positive predictive value (the share of drugs predicted "more than once daily" that really were); LR+, positive likelihood ratio (sensitivity divided by 1 − specificity). The accuracy of the rule that predicts QD for every drug is 68.8% (64/93), and the base rate of "more than once daily" is 31.2% (29/93).

### Half-life and dosing interval

Table 5 gives, for each regimen, the half-life, the dosing interval divided by the half-life, and the fraction of the peak remaining at the end of the dosing interval (the reference curve). The median half-life was 18.0 h for QD, 9.4 h for BID and 3.5 h for TID, decreasing in that order, but the interquartile ranges overlap widely. The median of the dosing interval divided by half-life was close for QD (1.33) and BID (1.28) and larger only for TID (2.36; 4 drugs). The interquartile ranges, however, overlap widely: 0.67–3.21 for QD and 0.48–2.45 for BID. The median fraction of the peak remaining at the end of the interval was 0.40 for QD, 0.41 for BID and 0.20 for TID. That QD and BID are close is nearly an arithmetical consequence of the median half-life being about twice as long when the interval is twice as long, and it is an exploratory observation found after the fact. The calculation assumes one compartment, instantaneous absorption and first-order elimination.

Table 5. Half-life and the ratio of dosing interval to half-life by regimen (`analysis/02_models.py`, n = 93).

| Regimen | Entries | Half-life, median (quartiles), h | Dosing interval divided by half-life, median (quartiles) | Median fraction of peak left at the end of its own dosing interval (reference calculation) |
|---|---|---|---|---|
| QD | 63 | 18.0 (7.5–36.1) | 1.33 (0.67–3.21) | 0.40 |
| BID | 25 | 9.4 (4.9–25.0) | 1.28 (0.48–2.45) | 0.41 |
| TID | 4 | 3.5 (2.5–11.5) | 2.36 (1.56–4.04) | 0.20 |
| Once weekly | 1 | 56.0 | 3.00 | 0.12 |

Note: The dosing interval was taken as 24 h for QD, 12 h for BID, 8 h for TID and 168 h for weekly dosing. The right column is the median over drugs of $2^{-\tau/t_{1/2}}$ ($\tau$ is the dosing interval); it is a reference calculation assuming one compartment and instantaneous absorption, not a measured concentration.

### Drugs for which half-life alone points the other way

Figure 5 shows the 14 drugs with a half-life under 6 h dosed QD, and the 8 drugs with a half-life of 24 h or more dosed BID or TID. The former are opicapone, ritlecitinib, trofinetide, vamorolone, daprodustat, odevixibat, finerenone, futibatinib, abrocitinib, asciminib, resmetirom, sotorasib, gepirone and momelotinib, with half-lives of 0.91–5.7 h. The latter are iptacopan, pacritinib, voclosporin, selpercatinib, ganaxolone, repotrectinib, olutasidenib and avacopan, with half-lives of 25–97.6 h. The reason these regimens were chosen is not stated in the workbook or in the label passages read. Of the 22 drugs in Figure 5, only 8 had their labels read (ritlecitinib, finerenone, futibatinib, daprodustat, selpercatinib, ganaxolone, olutasidenib and avacopan in Table 6). Candidate factors (persistence of drug effect through covalent binding or target occupancy, a difference between terminal-phase and effective half-life, modified-release formulations) have no column in the workbook and were not checked. Two of the drugs, daprodustat and gepirone, are marked in the workbook as withdrawn after approval.

![Half-lives of the 14 drugs with a half-life under 6 h dosed QD or weekly (left) and the 8 drugs with a half-life of 24 h or more dosed BID or TID (right).](shared/oral-drug-halflife-dosing-frequency/figures/fig5_case_map.png)

Figure 5. Drugs for which half-life alone does not match the dosing frequency. Left: 14 drugs with a half-life under 6 h dosed once daily or weekly (of the 24 drugs with a half-life under 6 h). Right: 8 drugs with a half-life of 24 h or more dosed BID or TID (of the 34 drugs with a half-life of 24 h or more). The half-life axes are logarithmic, in hours.

### Comparison with the labels

Table 6 compares the workbook with the current labels for the 10 entries chosen in advance (`analysis/04_label_audit_compare.py`). The 10 entries are not a representative sample, and no overall error rate can be estimated from them. The dosing frequency agreed for all 10 (for maralixibat the label differs by indication, which fits the "QD or BID" in the `Dose_and_Class` sheet). The half-life agreed for 8; for ritlecitinib the workbook has 1.25 h, below the lower end of the label range of 1.3–2.3 h, and for maralixibat the workbook has no value while the label gives 1.6 h.

Table 6. Comparison of 10 entries between the workbook and the current labels (DailyMed).

| Entry (approval year) | Frequency in the workbook | Frequency in the current label | Half-life in the workbook | Half-life in the current label | Half-life check |
|---|---|---|---|---|---|
| selpercatinib (2020) | BID | BID (twice daily; other frequencies in paediatric and dose-reduction tables) | 32 | 32 h | agree |
| finerenone (2021) | QD | QD | 2–3 h | 2–3 h | agree |
| avacopan (2021) | BID | BID | 97.6 | 97.6 h | agree |
| maralixibat (2021) | QD or BID (Sheet1: QD) | QD for Alagille syndrome, BID for PFIC | no value | 1.6 h | workbook has no value |
| futibatinib (2022) | QD | QD | 2.9 | 2.9 h | agree |
| olutasidenib (2022) | BID | BID | 67 | about 67 h | agree |
| ganaxolone (2022) | TID | TID | 34 | 34 h | agree |
| daprodustat (2023) | QD | QD | 1–4 h | 1–4 h | agree |
| ritlecitinib (2023) | QD | QD | 1.25 | 1.3–2.3 h | below the label range |
| tovorafenib (2024) | weekly | weekly | 56 | about 56 h | agree |

Note: PFIC, progressive familial intrahepatic cholestasis. Half-lives are in hours. The labels are versions dated March 2025 to November 2026 (the version date shown by DailyMed, `inputs/label_audit.csv`).

### Sensitivity analyses

Changing how half-life was taken, how combinations were handled, the coding of maralixibat, whether the weekly drug was kept or whether drugs withdrawn after approval were kept left the slope negative, between −0.220 and −0.294, and the LOO Brier score of M1 (0.216–0.221) was only 0.002–0.007 lower than the base rate in each setting (0.218–0.225) (`sensitivity.csv` in the companion archive). The AUC of M1 was 0.56–0.61. Excluding the 6 drugs the workbook marks as withdrawn after approval (4 of them in the primary set), leaving 89 drugs, the slope was −0.258 and the Brier difference 0.004.

## Discussion

The direction of the relation between half-life and dosing frequency is the one expected from pharmacokinetics (a longer half-life goes with less frequent dosing), and the interval of the slope excludes 0 (odds ratio 0.58–0.98), but its upper end is close to 0, a borderline result. Its size is small, and the out-of-sample difference from the base rate fell within its interval. The shares by half-life bin also have wide intervals and are not monotone. With these numbers, half-life is a weak cue for once-daily dosing, and it cannot be said that "the half-life tells you whether a drug is dosed once daily". The analysis is exploratory, and no correction was made for multiplicity across bins, thresholds and sensitivity analyses.

The medians of the dosing interval divided by half-life were nearly equal for QD (1.33) and BID (1.28): at the level of medians, BID drugs have a shorter interval in line with their shorter half-life (Table 5). But the interquartile ranges of this ratio overlap widely (0.67–3.21 for QD, 0.48–2.45 for BID), the interquartile ranges of half-life also overlap widely, and both frequencies were approved for drugs with the same half-life. Factors other than half-life may act on the frequency, but the workbook has no column for them (speed of absorption, duration of drug effect, adverse events related to concentration peaks, formulation, target population). This article did not test their contribution.

The four terms added in M2 had point estimates that favoured out-of-sample prediction, but the interval contains 0, and this is not a test of the effect of the added terms. FIC and orphan overlap with disease area. The relation Brown reported between FIC or orphan status and frequency was reproduced in the recount (Table 1).

## Limitations

- **A description of approved drugs only.** Drugs tested at other frequencies in development and settled on the present one at approval, and drugs that were never approved, are not included. Drugs withdrawn after approval are included: 4 of the 6 marked as withdrawn in the workbook are in the primary set (daprodustat, gepirone, infigratinib and umbralisib). Approved regimens may be those in which half-life and frequency fit, so no claim can be made that half-life determined the frequency.
- **The half-life definitions are heterogeneous.** The workbook values mix terminal-phase, mean, effective, population estimates and patient-group values ([1](#ref-1)). Ranges were converted to the geometric mean, and using the lower or the upper bound did not change the direction of the slope. Differences between single-dose and repeated-dose values, food conditions and special populations were not adjusted for.
- **The regimen was reduced to one main indication and dose.** For drugs whose frequency changes with indication or age (selpercatinib, maralixibat and others), the single label in the workbook was used. Weekly, cyclic and short-course drugs follow the frequency label. The workbook has no column for modified-release formulations, so the possibility that short half-life QD drugs rest on extended-release formulations cannot be excluded.
- **The sample is small, and dependence between drugs is not modelled.** Of 93 drugs, 29 are BID or TID, and each half-life bin or disease group has 10–20 drugs. Drugs of the same class, the same developer or the same approval period tend to have similar regimen designs; no clustering was modelled, and because the intervals assume independence they may be too narrow. The intervals are an approximation from a bootstrap with the out-of-sample predictions held fixed, biased toward being too narrow. The LOGO groups "other" and "infection" have 6 drugs each, so a lack of difference there cannot be confirmed and the result is undetermined.
- **The exclusions may weaken the slope.** The excluded combinations lean toward more frequent dosing (4 of 9 entries), so the exclusion may have pulled the slope toward 0 (included in the sensitivity analyses).
- **The effect of the four M2 terms was not identified.** FIC, orphan and disease area overlap, so no causal claim can be made. No intervals were computed for the M2 coefficients.
- **No correction for multiplicity.** The bins, the three thresholds, the nine sensitivity settings and the Spearman correlation are exploratory, with no correction of p values or intervals. The Spearman p = 0.051 and the upper end of the slope interval at −0.020 are borderline.
- **The reference curve depends on assumptions.** It assumes one compartment, first-order elimination, instantaneous absorption and linear pharmacokinetics. Many of the half-life values come from drugs for which these assumptions do not hold (multiphasic elimination, target-mediated elimination, active metabolites).
- **Inconsistencies in the workbook were not corrected.** The per-year counts that differ from the text by one, the FIC column that disagrees for 6 entries, and the missing half-life of maralixibat were reported as found. The `Dose_and_Class` column was used for FIC.
- **The label check covers only 10 entries.** The other 94 entries were not compared with labels. The 10 entries are not a representative sample; the half-life agreed for 8, differed for 1 and was missing for 1, which cannot be applied as an overall error rate.
- **The image of original Table 1 was not read.** Row values come from the workbook only. [Original Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl1) is an image, and about the first 70% of the original text (100,000 of 145,798 characters) was read.

## Conclusion

On the QOI: among the 93 single-ingredient oral small-molecule drugs approved by the FDA in 2020–2024, half-life is only a weak cue for dosing more than once daily. A longer half-life goes with less dosing at two or more times a day (odds ratio 0.78, 95% interval 0.58–0.98), but out-of-sample evaluation could not show a difference from the base rate (31%) (difference in Brier score −0.003, 95% interval −0.019 to 0.014). This result does not exclude small differences, and drugs that go the other way are present at a half-life under 6 h and at 24 h or more.

On the COU: using half-life alone as a rule of thumb for "once daily or more often" is not supported by the description of these 93 drugs. The result is a description of approved drugs. It is not a conclusion about the choice of regimen or a causal statement that half-life determines frequency.

## Data and code availability

The materials for re-running (the scripts in `analysis/`, the source records and the label comparison table in `inputs/`, the summary tables, figures and logs in `outputs/`, and the list of table hashes `MANIFEST_SHA256.txt`) are in the [companion archive](shared/oral-drug-halflife-dosing-frequency/oral-drug-halflife-dosing-frequency-companion.zip). Brown's supplementary data file `jm5c02863_si_002.xlsx` (SHA256 `796452e02efe3edd647375d15d5b1911682ef44d2709499f8846387fdf950213`) is the publisher's copyrighted material and is not in the archive. It is obtained from the Supporting Information of the paper and placed in `inputs/raw/`; `analysis/01_build_dataset.py` stops if the SHA256 differs. Tables with per-drug values (the cleaned data, the primary set, the out-of-sample predictions and the case tables) are regenerated from the workbook by `01_build_dataset.py` and `02_models.py`.

The environment was Python 3.12.4 ([9](#ref-9)), NumPy 2.2.6 ([10](#ref-10)), SciPy 1.14.0 ([11](#ref-11)), pandas 2.2.2 ([12](#ref-12)), Matplotlib 3.9.1 ([13](#ref-13)), openpyxl 3.1.5 ([14](#ref-14)) and scikit-learn 1.8.0 ([15](#ref-15)), with random seed 20261114. The scripts run in the order `python -X utf8 analysis/01_build_dataset.py`, `02_models.py`, `03_figures.py`, `04_label_audit_compare.py` and `05_manifest.py`, and `python -X utf8 analysis/05_manifest.py --check` compares the output tables with the hashes in the list. `analysis/00_label_audit_fetch.py`, used to read the labels, needs network access and is not part of the re-run.

## References

<span id="ref-1"></span>1. Brown DG. What do oral drugs really look like? Dose regimen, pharmacokinetics, and safety of recently approved small-molecule oral drugs. J Med Chem. 2025 Nov 18;68(22):23751–23780. PMID: 41252611. [doi:10.1021/acs.jmedchem.5c02863](https://doi.org/10.1021/acs.jmedchem.5c02863). Full text: [PMC12670434](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/) (text read up to about 100,000 of 145,798 characters; [original Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl1) is an image and was not read; [original Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl3) values were read from the text).

<span id="ref-2"></span>2. Brown DG. Supporting Information: data files (jm5c02863_si_002.xlsx) for "What do oral drugs really look like?" [Dataset]. ACS Publications; 2025. [doi:10.1021/acs.jmedchem.5c02863](https://doi.org/10.1021/acs.jmedchem.5c02863). SHA256 796452e02efe3edd647375d15d5b1911682ef44d2709499f8846387fdf950213; saved by hand from the publisher site on 2026 Nov 14.

<span id="ref-3"></span>3. Wilson EB. Probable inference, the law of succession, and statistical inference. J Am Stat Assoc. 1927;22(158):209–212. [doi:10.1080/01621459.1927.10502953](https://doi.org/10.1080/01621459.1927.10502953)

<span id="ref-4"></span>4. Brier GW. Verification of forecasts expressed in terms of probability. Mon Weather Rev. 1950;78(1):1–3. DOI: 10.1175/1520-0493(1950)078&lt;0001:VOFEIT&gt;2.0.CO;2. Link: [doi.org](https://doi.org/10.1175/1520-0493(1950)078%3C0001:VOFEIT%3E2.0.CO;2)

<span id="ref-5"></span>5. Gneiting T, Raftery AE. Strictly proper scoring rules, prediction, and estimation. J Am Stat Assoc. 2007;102(477):359–378. [doi:10.1198/016214506000001437](https://doi.org/10.1198/016214506000001437)

<span id="ref-6"></span>6. Van Calster B, McLernon DJ, van Smeden M, Wynants L, Steyerberg EW; Topic Group "Evaluating diagnostic tests and prediction models" of the STRATOS initiative. Calibration: the Achilles heel of predictive analytics. BMC Med. 2019;17:230. [doi:10.1186/s12916-019-1466-7](https://doi.org/10.1186/s12916-019-1466-7)

<span id="ref-7"></span>7. Efron B. Bootstrap methods: another look at the jackknife. Ann Stat. 1979;7(1):1–26. [doi:10.1214/aos/1176344552](https://doi.org/10.1214/aos/1176344552)

<span id="ref-8"></span>8. National Library of Medicine. DailyMed: current prescribing information, read on 2026 Nov 14 [Internet]. Bethesda (MD): NLM. Labels (DailyMed set IDs): selpercatinib [7fa848ba-a59c-4144-9f52-64d090f4d828](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7fa848ba-a59c-4144-9f52-64d090f4d828); finerenone [fc726765-5d5a-4d6e-b037-b847bda9fb7c](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fc726765-5d5a-4d6e-b037-b847bda9fb7c); avacopan [c93cbc0b-29a3-46a5-9c85-41815ea5cf4a](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c93cbc0b-29a3-46a5-9c85-41815ea5cf4a); maralixibat [64000394-1ef6-4e76-8ba8-11f25ba1b167](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=64000394-1ef6-4e76-8ba8-11f25ba1b167); futibatinib [0b1332a1-0581-4707-9bf6-1eccfa39bef4](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0b1332a1-0581-4707-9bf6-1eccfa39bef4); olutasidenib [4a0c7c8b-b95f-455d-9600-b7351e4397fe](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a0c7c8b-b95f-455d-9600-b7351e4397fe); ganaxolone [d91612c4-b03a-4be4-a1ee-6a13e3b83d4e](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d91612c4-b03a-4be4-a1ee-6a13e3b83d4e); daprodustat [d82aa06e-5a33-4844-99b7-4701313455a4](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d82aa06e-5a33-4844-99b7-4701313455a4); ritlecitinib [1882f799-61b0-4813-965a-4910c4ae419c](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1882f799-61b0-4813-965a-4910c4ae419c) (two set IDs exist for this product; the first was read); tovorafenib [ea3a9631-3a66-6a7c-e053-2995a90ae2ad](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ea3a9631-3a66-6a7c-e053-2995a90ae2ad).

<span id="ref-9"></span>9. Python Software Foundation. Python [Software]. Version 3.12.4. Available from: [https://www.python.org/](https://www.python.org/)

<span id="ref-10"></span>10. Harris CR, Millman KJ, van der Walt SJ, Gommers R, Virtanen P, Cournapeau D, et al. Array programming with NumPy [Software, version 2.2.6]. Nature. 2020;585(7825):357–362. [doi:10.1038/s41586-020-2649-2](https://doi.org/10.1038/s41586-020-2649-2)

<span id="ref-11"></span>11. Virtanen P, Gommers R, Oliphant TE, Haberland M, Reddy T, Cournapeau D, et al. SciPy 1.0: fundamental algorithms for scientific computing in Python [Software, version 1.14.0]. Nat Methods. 2020;17(3):261–272. [doi:10.1038/s41592-019-0686-2](https://doi.org/10.1038/s41592-019-0686-2)

<span id="ref-12"></span>12. McKinney W. Data structures for statistical computing in Python [Software: pandas, version 2.2.2]. In: Proceedings of the 9th Python in Science Conference. 2010. p. 56–61. [doi:10.25080/Majora-92bf1922-00a](https://doi.org/10.25080/Majora-92bf1922-00a)

<span id="ref-13"></span>13. Hunter JD. Matplotlib: a 2D graphics environment [Software, version 3.9.1]. Comput Sci Eng. 2007;9(3):90–95. [doi:10.1109/MCSE.2007.55](https://doi.org/10.1109/MCSE.2007.55)

<span id="ref-14"></span>14. Gazoni E, Clark C. openpyxl [Software]. Version 3.1.5. Available from: [https://openpyxl.readthedocs.io/](https://openpyxl.readthedocs.io/)

<span id="ref-15"></span>15. Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B, Grisel O, et al. Scikit-learn: machine learning in Python [Software, version 1.8.0]. J Mach Learn Res. 2011;12:2825–2830. Available from: [https://jmlr.org/papers/v12/pedregosa11a.html](https://jmlr.org/papers/v12/pedregosa11a.html)
