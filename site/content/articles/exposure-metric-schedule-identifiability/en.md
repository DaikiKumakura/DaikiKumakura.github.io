## Abstract {#article-abstract}

Exposure–response analyses of dose-finding studies often relate toxicity to one summary of exposure, and the choice among the weekly area under the concentration–time curve (AUC) and the maximum (Cmax) and minimum (Cmin) concentrations is usually made within one dosing schedule, where the summaries move together with dose. I simulated one-compartment oral pharmacokinetics (elimination half-life about 24 h, AUC proportional to dose) and a binary toxicity driven by exactly one of the three summaries, computed at steady state over one dosing interval for the same four weekly doses given twice daily (BID), daily (QD) or weekly (QW). Studies of 48 to 384 patients were allocated in equal numbers to the arms of one schedule (QD), two schedules (BID with QD, or QD with QW) or three (BID, QD and QW), and one logistic model per metric was fitted and compared by the Akaike information criterion (AIC); 2,000 studies were simulated per setting. With QD alone or with BID and QD the log metrics were nearly collinear (correlations 0.955 to 0.994) and AIC selected the true metric in 14.6% to 75.7% of studies. Adding QW, whose mean Cmax was 3.4 times and mean Cmin 0.105 times those of QD at the same weekly dose, lowered the correlations to 0.483 to 0.772 (and −0.174 between Cmax and Cmin) and raised the probability to at least 97.3% at 192 patients. The consequence for the regimen chosen depended on whether the schedule that carries the risk had been randomized and on how ties between schedules with equal AUC were resolved: when Cmax was the driver and the AUC model was always used, the share of studies that chose a regimen whose true toxicity exceeded the cap plus 0.05 (30% for the main cap of 0.25) ranged from 0.0% to 100% over the designs, caps and tie rules tried. These results hold for one pharmacokinetic model, a logistic form on the log of one metric, exact exposure and no confounding.

## Introduction {#article-introduction}

The guidance of the U.S. Food and Drug Administration (FDA) on dosage optimization in oncology recommends comparing several dosages in randomized trials and considers population pharmacokinetic and exposure–response analyses together with safety and activity when a dosage is selected ([1](#ref-1)). An exposure–response analysis needs a definition of exposure, and the usual choices (AUC, Cmax and Cmin) answer different pharmacological questions. Conference abstracts have examined the choice by simulation. Kågedal et al. reported that the best-correlating metric depended on dose and on the concentration–effect relationship, with AUC best overall, and that an exposure–response relationship estimated in one dose group may not predict the response in another ([2](#ref-2)). Hu and Gheyas reported that when correlations among metrics exceeded 0.95, AIC could not reliably distinguish them, while the dose chosen was unaffected by the wrong choice ([3](#ref-3)). De Vos et al. reported that power to detect an exposure effect was highest for AUC, followed by trough and then Cmax, and that omitting a confounder could change it ([4](#ref-4)). I read these three references through their abstracts only.

Those studies compared metrics within one dosing schedule, where the metrics move together with dose. Different schedules at the same weekly dose have the same AUC and different Cmax and Cmin. This article asks: **if toxicity is driven by exactly one of AUC, Cmax and Cmin, how often does an exposure–response analysis distinguish it when the study uses one, two or three dosing schedules, and what does the choice of metric do to the regimen that is selected?** The answer is computed by simulation with a known driver.

## Methods {#article-methods}

### Question and context of use

The question of interest was which exposure metric drives toxicity, and the context of use was the choice of a regimen (weekly dose and schedule) for a later trial from a randomized dose-finding study. The simulation is a research tool for studying the operating characteristics of the analysis. It does not recommend a trial design, and randomizing patients to schedules with very different peak concentrations at high doses would often be unacceptable (see Limitations).

### Pharmacokinetics, regimens and metrics

Individuals had one-compartment kinetics with first-order absorption and elimination and bioavailability 1, so that AUC is proportional to dose. Typical clearance (CL) was 5 L/h, volume of distribution (V) 170 L (elimination half-life about 24 h) and absorption rate constant (ka) 1 per hour, each multiplied by exp(η) with independent normal η of standard deviation (SD) 0.30, 0.20 and 0.50. A bank of 20,000 individuals was drawn once (seed 20261124); studies sampled from the bank, and η were not correlated. The regimens combined four weekly doses (70, 140, 280 and 560 mg) with three schedules that differ only in the dosing interval: twice daily (BID, 14 equal doses a week), daily (QD, 7) and weekly (QW, 1), giving 12 regimens. At steady state the concentration within a dosing interval of τ hours is C(t) = Dose·ka / (V·(ka − ke)) · (e^(−ke·t) / (1 − e^(−ke·τ)) − e^(−ka·t) / (1 − e^(−ka·τ))), with ke = CL / V. The three metrics were the weekly AUC at steady state (weekly dose / CL), the maximum of C over one steady-state dosing interval (Cmax) and the minimum of C over one steady-state dosing interval (Cmin), the last two computed on a 0.25 h grid; Cmin falls at the end of the interval, just before the next dose. At the same weekly dose, the mean Cmax of QW was 3.4 times and its mean Cmin 0.105 times those of QD, and BID had 0.869 and 1.198 times (Cmax and Cmin of the regimens in the bank).

### Toxicity

For each true driver m (AUC, Cmax or Cmin), the probability of toxicity was expit(a + s·ln(m)), with slope s = 1.5 per natural-log unit (main analysis; doubling the metric multiplies the odds by 2.8) or 0.75 (sensitivity analysis), and the intercept a was set so that the toxicity rate of QD 280 mg per week in the bank equalled 0.20. The toxicity rate of each regimen was the mean over the bank (Table 1). Efficacy was not modelled.

**Table 1.** True toxicity rate of each regimen by true driver (slope 1.5; bank of 20,000 individuals).

| Regimen | Weekly dose (mg) | True driver AUC | True driver Cmax | True driver Cmin |
| --- | --- | --- | --- | --- |
| BID | 70 | 0.031 | 0.025 | 0.041 |
| QD | 70 | 0.031 | 0.031 | 0.032 |
| QW | 70 | 0.031 | 0.166 | 0.002 |
| BID | 140 | 0.083 | 0.068 | 0.107 |
| QD | 140 | 0.083 | 0.082 | 0.085 |
| QW | 140 | 0.083 | 0.356 | 0.005 |
| BID | 280 | 0.200 | 0.169 | 0.245 |
| QD | 280 | 0.200 | 0.200 | 0.200 |
| QW | 280 | 0.200 | 0.606 | 0.013 |
| BID | 560 | 0.404 | 0.358 | 0.465 |
| QD | 560 | 0.404 | 0.408 | 0.397 |
| QW | 560 | 0.404 | 0.811 | 0.032 |

AUC, area under the concentration–time curve; Cmax, maximum concentration; Cmin, minimum concentration; BID, twice daily; QD, once daily; QW, once weekly.

### Studies and analysis

A study allocated N patients (48, 96, 192 or 384) to the arms formed by the four weekly doses and the schedules of the design, in equal numbers by rotation through the arms; each patient was a random individual of the bank, with the true individual metrics (no exposure error), and toxicity was Bernoulli. The designs were QD only (one schedule, 4 arms), BID and QD (two schedules, 8 arms), QD and QW (two schedules, 8 arms) and BID, QD and QW (three schedules, 12 arms). Three logistic regressions of toxicity on ln(AUC), ln(Cmax) and ln(Cmin) were fitted, each with an intercept; they have the same number of parameters, so the Akaike information criterion (AIC) ranking is the deviance ranking. The metric with the lowest AIC was selected, and a study was called ambiguous if the best and second-best AIC differed by less than 2.

To measure the consequence for the decision, each fitted model predicted the toxicity of each of the 12 regimens as the mean fitted probability over 5,000 individuals of the bank (the first 5,000), including schedules that the design did not allocate. The regimen chosen was the one with the highest weekly dose whose predicted toxicity was at most 0.25 (the cap). When several regimens met this, a tie rule decided: choose the schedule with the fewest doses (QW before QD before BID), the one with the most doses, or one of the tied regimens at random (reported as the expected share). Three decision models were compared: always the AUC model, the model of the metric selected by AIC, and the model of the true metric (known only in a simulation). A decision was counted as an overdose if the true toxicity of the regimen chosen was above 0.30 (the cap plus 0.05). The true optimum by the same rule was QW 280 mg (fewest doses) or BID 280 mg (most doses) when AUC was the driver, QD 280 mg or BID 280 mg when Cmax was, and QW 560 mg when Cmin was. In a sensitivity analysis for the Cmax driver, the cap was 0.15 or 0.35 (overdose above the cap plus 0.05).

Each of 96 settings (2 slopes × 3 true drivers × 4 designs × 4 patient numbers) was simulated 2,000 times with base R 4.5.3 ([5](#ref-5)). Each study used the seed 20261124 plus its index, so the results do not depend on the number of cores. The Monte Carlo standard error of a probability is at most 0.011, and that of the difference between two independent probabilities is at most about 0.016. Four additional runs used separate seeds (study indices from 5,000,000 and, for the cap sensitivity analysis, from 7,000,000): the deviances of the three models in the one-schedule design (2,000 studies per setting), the regimens chosen by the AUC model, the spread of the log metrics, and the sensitivity of the overdose shares to the cap.

## Results {#article-results}

### One schedule, or two similar schedules, leave the metrics nearly collinear

In the one-schedule design, the correlations between the logarithms of the metrics across patients were 0.994 (AUC with Cmax), 0.987 (AUC with Cmin) and 0.963 (Cmax with Cmin), because most of the variation is the weekly dose (Table 2). With BID and QD they were 0.992, 0.985 and 0.955. With QD and QW or with three schedules they were 0.761 and 0.772 (AUC with Cmax), 0.483 (AUC with Cmin) and −0.174 and −0.162 (Cmax with Cmin). The log Cmin of QW was spread widely (SD 1.878, against 0.431 for QD and 0.355 for BID), with the lowest values near −22 (Cmin about 10⁻¹⁰ mg/L; `results/diagnostic-metric-spread.csv`).

**Table 2.** Mean correlation, across patients, of the log metrics by design (384 patients, AUC as the driver; the values at other patient numbers and for other drivers differ by at most 0.005).

| Design | Log AUC and log Cmax | Log AUC and log Cmin | Log Cmax and log Cmin |
| --- | --- | --- | --- |
| One schedule (QD) | 0.994 | 0.987 | 0.963 |
| Two schedules (BID, QD) | 0.992 | 0.985 | 0.955 |
| Two schedules (QD, QW) | 0.761 | 0.483 | −0.174 |
| Three schedules (BID, QD, QW) | 0.772 | 0.483 | −0.162 |

Abbreviations as in Table 1.

### With QW absent AIC could not reliably identify the driver

With a single schedule and a slope of 1.5, AIC selected the true metric in 14.6% (48 patients) to 40.2% (384) of studies when AUC was the driver, 53.9% to 66.9% when Cmax was, and 59.6% to 74.8% when Cmin was (Table 3, Figure 1). Pairing BID with QD gave 15.3% to 43.3%, 55.7% to 68.4% and 61.1% to 75.7%, close to the one-schedule values. The best and second-best AIC differed by less than 2 in 97.8%, 95.6%, 91.2% and 87.0% of the AUC-driver studies of the one-schedule design at 48, 96, 192 and 384 patients, in up to 98.4% of the studies at 48 patients (Cmax driver), and in 55.1% of the Cmin-driver studies at 384 patients (Table 4).

With QD and QW or with all three schedules, the true metric was selected in 74.9% to 94.6% of studies at 48 patients and in at least 97.3% at 192 (AUC driver: 98.1% and 97.3% with two and three schedules). The two- and three-schedule designs that contained QW differed by at most 0.021 in every cell, which is within about two standard errors of a difference, so I do not claim that they were equivalent; at 384 patients 0.3% or fewer of their studies were ambiguous.

**Table 3.** Probability that AIC selects the true metric (slope 1.5; 2,000 studies per cell).

| True driver | Design | 48 patients | 96 patients | 192 patients | 384 patients |
| --- | --- | --- | --- | --- | --- |
| AUC | One schedule (QD) | 0.146 | 0.205 | 0.286 | 0.402 |
| AUC | Two schedules (BID, QD) | 0.153 | 0.231 | 0.319 | 0.433 |
| AUC | Two schedules (QD, QW) | 0.756 | 0.907 | 0.981 | 0.999 |
| AUC | Three schedules (BID, QD, QW) | 0.749 | 0.887 | 0.973 | 0.998 |
| Cmax | One schedule (QD) | 0.539 | 0.603 | 0.630 | 0.669 |
| Cmax | Two schedules (BID, QD) | 0.557 | 0.574 | 0.638 | 0.684 |
| Cmax | Two schedules (QD, QW) | 0.926 | 0.977 | 0.998 | 1.000 |
| Cmax | Three schedules (BID, QD, QW) | 0.905 | 0.973 | 0.999 | 1.000 |
| Cmin | One schedule (QD) | 0.596 | 0.610 | 0.692 | 0.748 |
| Cmin | Two schedules (BID, QD) | 0.611 | 0.657 | 0.702 | 0.757 |
| Cmin | Two schedules (QD, QW) | 0.938 | 0.981 | 0.998 | 1.000 |
| Cmin | Three schedules (BID, QD, QW) | 0.946 | 0.979 | 1.000 | 1.000 |

AIC, Akaike information criterion; other abbreviations as in Table 1.

![Probability that AIC selects the true metric by patients per study and design: about 0.15 to 0.75 for designs without QW, and 0.75 to 1.00 for designs with QW](shared/exposure-metric-schedule-identifiability/figures/figure-1-metric-selection.png)

**Figure 1.** Probability that AIC selects the true exposure metric (vertical axis) by patients per study (horizontal axis, log scale) for studies with one schedule (QD), two schedules (BID and QD, or QD and QW) and three schedules (BID, QD and QW), by true driver (slope 1.5; 2,000 studies per point). The dashed line marks one third. AIC, Akaike information criterion; BID, twice daily; QD, once daily; QW, once weekly.

**Table 4.** Share of ambiguous studies (the best and second-best AIC differ by less than 2; slope 1.5).

| True driver | Design | 48 patients | 96 patients | 192 patients | 384 patients |
| --- | --- | --- | --- | --- | --- |
| AUC | One schedule (QD) | 0.978 | 0.956 | 0.912 | 0.870 |
| AUC | Two schedules (BID, QD) | 0.972 | 0.939 | 0.888 | 0.842 |
| AUC | Two schedules (QD, QW) | 0.404 | 0.152 | 0.035 | 0.003 |
| AUC | Three schedules (BID, QD, QW) | 0.386 | 0.171 | 0.035 | 0.002 |
| Cmax | One schedule (QD) | 0.984 | 0.941 | 0.857 | 0.730 |
| Cmax | Two schedules (BID, QD) | 0.962 | 0.926 | 0.842 | 0.683 |
| Cmax | Two schedules (QD, QW) | 0.109 | 0.032 | 0.002 | 0.000 |
| Cmax | Three schedules (BID, QD, QW) | 0.136 | 0.030 | 0.002 | 0.000 |
| Cmin | One schedule (QD) | 0.968 | 0.905 | 0.768 | 0.551 |
| Cmin | Two schedules (BID, QD) | 0.946 | 0.848 | 0.706 | 0.492 |
| Cmin | Two schedules (QD, QW) | 0.139 | 0.029 | 0.004 | 0.000 |
| Cmin | Three schedules (BID, QD, QW) | 0.105 | 0.029 | 0.002 | 0.001 |

AIC, Akaike information criterion; other abbreviations as in Table 1.

### With AUC as the driver the true metric was often selected less than one third of the time

In the one-schedule design with AUC as the driver, the true metric was selected in fewer than one third of the studies at 48 to 192 patients (14.6%, 20.5% and 28.6%), although the three metrics were nearly collinear. A diagnostic run showed that the true model had the lowest mean deviance of the three in all nine settings (Table 5), but that with AUC as the driver the true model's deviance was higher than the lower deviance of the two other models in the typical study (median difference 0.45, 0.44 and 0.25 at 96, 192 and 384 patients), whereas with Cmax or Cmin as the driver it was lower (median differences from −0.15 to −1.77). A likely reason is that log AUC lies between log Cmax and log Cmin in this design (correlations 0.994 and 0.987, against 0.963 between the two), so that with AUC as the driver both other models are close competitors and the lower of two near-equal deviances is usually lower than the one of the true model, while with Cmax or Cmin as the driver one competitor is far and the other is the middle metric. I did not test this explanation beyond the deviance diagnostic, and the one-third reference is the share expected if the three models were exchangeable, which they were not.

**Table 5.** Diagnostic run in the one-schedule design (slope 1.5; 2,000 studies per cell with separate seeds): mean deviance of each model, share of studies in which each model had the lowest deviance, and the median difference between the deviance of the true model and the lower deviance of the other two models.

| True driver | Patients | Mean deviance, AUC model | Cmax model | Cmin model | Lowest deviance, AUC model | Cmax model | Cmin model | True model minus the lower of the other two (median) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AUC | 96 | 72.25 | 72.46 | 72.62 | 0.204 | 0.394 | 0.403 | 0.45 |
| AUC | 192 | 146.65 | 147.07 | 147.42 | 0.285 | 0.376 | 0.340 | 0.44 |
| AUC | 384 | 295.74 | 296.60 | 297.25 | 0.417 | 0.309 | 0.274 | 0.25 |
| Cmax | 96 | 73.22 | 73.02 | 74.09 | 0.182 | 0.575 | 0.244 | −0.15 |
| Cmax | 192 | 148.79 | 148.36 | 150.63 | 0.214 | 0.624 | 0.163 | −0.44 |
| Cmax | 384 | 299.42 | 298.57 | 303.07 | 0.243 | 0.678 | 0.080 | −0.89 |
| Cmin | 96 | 70.82 | 71.58 | 70.42 | 0.166 | 0.198 | 0.637 | −0.40 |
| Cmin | 192 | 144.41 | 145.95 | 143.62 | 0.217 | 0.105 | 0.679 | −0.79 |
| Cmin | 384 | 290.39 | 293.57 | 288.66 | 0.195 | 0.042 | 0.764 | −1.77 |

Abbreviations as in Table 1.

### A weaker exposure–response signal needed more patients

With a slope of 0.75, the true metric was selected in 9.3% to 23.2% of the one-schedule studies when AUC was the driver, in 51.4% to 58.6% when Cmax was and in 54.1% to 65.4% when Cmin was (Table 6). With QD and QW or three schedules at 384 patients the probabilities were 92.3% and 93.6% (AUC driver), 98.0% and 97.9% (Cmax) and 100% and 99.8% (Cmin). In the designs with QW, the patient number at which the probability reached about the level that the slope of 1.5 gave at 96 patients was about four times as large for the AUC and Cmax drivers and about twice as large for the Cmin driver (for example, with three schedules, AUC driver: 88.7% at 96 patients with a slope of 1.5, 93.6% at 384 with 0.75; Cmin driver: 97.9% and 94.5% at 96, 98.8% at 192).

**Table 6.** Probability that AIC selects the true metric with a weaker signal (slope 0.75; 2,000 studies per cell).

| True driver | Design | 48 patients | 96 patients | 192 patients | 384 patients |
| --- | --- | --- | --- | --- | --- |
| AUC | One schedule (QD) | 0.093 | 0.121 | 0.161 | 0.232 |
| AUC | Two schedules (BID, QD) | 0.099 | 0.142 | 0.181 | 0.250 |
| AUC | Two schedules (QD, QW) | 0.492 | 0.652 | 0.813 | 0.923 |
| AUC | Three schedules (BID, QD, QW) | 0.495 | 0.644 | 0.802 | 0.936 |
| Cmax | One schedule (QD) | 0.514 | 0.538 | 0.534 | 0.586 |
| Cmax | Two schedules (BID, QD) | 0.524 | 0.533 | 0.570 | 0.593 |
| Cmax | Two schedules (QD, QW) | 0.678 | 0.840 | 0.942 | 0.980 |
| Cmax | Three schedules (BID, QD, QW) | 0.689 | 0.819 | 0.933 | 0.979 |
| Cmin | One schedule (QD) | 0.541 | 0.585 | 0.620 | 0.654 |
| Cmin | Two schedules (BID, QD) | 0.569 | 0.590 | 0.612 | 0.682 |
| Cmin | Two schedules (QD, QW) | 0.842 | 0.945 | 0.984 | 1.000 |
| Cmin | Three schedules (BID, QD, QW) | 0.856 | 0.945 | 0.988 | 0.998 |

AIC, Akaike information criterion; other abbreviations as in Table 1.

### The cost of a wrong metric depended on extrapolation and on the tie rule

When Cmax was the driver, the model that always used AUC cannot tell apart schedules at the same weekly dose, since they have the same AUC, so which schedule was chosen was decided by the tie rule (Table 7). With the rule that prefers the fewest doses, the regimen chosen had a true toxicity above 0.30 in every study of the one-schedule design at 96 and 384 patients, in 70.5% and 83.3% of the studies with QD and QW, and in 96.1% and 100% of those with three schedules; with the rule that prefers the most doses, in 4.2% or fewer; with ties resolved at random, in 32.1% to 36.1% of the studies of the one-schedule and three-schedule designs (about one third, the share of QW among three tied schedules) and in 23.6% and 27.8% of those with QD and QW. The one-schedule design never allocated QW, so the AUC model extrapolated to it (Table 8: QW 280 mg was chosen in 82.3% and 98.0% of the studies, with a true toxicity of 0.606). Even with the true metric known, the one-schedule design gave an overdose in 8.6% of the studies at 96 patients, against 3.4% and 3.9% in the designs with QW, which shows the cost of extrapolation to an unallocated schedule.

With QW allocated, the overdose share of the AUC model rose with the number of patients (70.5% to 83.3% with QD and QW) because the model's prediction converged on the mixture of the schedules: it chose QW 140 mg, whose true toxicity is 0.356, in 70.1% of the studies at 96 patients and 82.5% at 384, and the safe QW 70 mg in 29.3% and 17.5% (Table 8). The overdose shares also depended on the cap: with a cap of 0.15 they were 5.4% and 0.1% for QD with QW at 96 and 384 patients, with 0.25 70.5% and 83.3% and with 0.35 18.4% and 4.3%; for three schedules they were 29.7% and 12.6%, 96.1% and 100%, and 73.3% and 88.9% (Table 9).

Choosing the metric by AIC gave an overdose in 44.5% (96 patients) and 33.4% (384) of one-schedule studies with Cmax as the driver, against 8.6% and 0.4% when the true metric was known, and in 5.3% and 0.0% (QD and QW) and 6.6% and 0.0% (three schedules) with AIC against 3.4% and 0.0%, and 3.9% and 0.0%, with the true metric. With AUC as the driver, AUC was right (4.2% or fewer overdoses at 96 patients, 0.1% or fewer at 384), and AIC choice led to an overdose in 39.9% and 27.8% of one-schedule studies, against 3.4% and 0.1% with the true metric. With Cmin as the driver, the AUC model produced no overdose when ties were resolved toward the fewest doses (QW has a low Cmin and is safe for this driver), but 63.9% and 73.7% of the studies with QD and QW overdosed when ties were resolved toward the most doses, and 42.6% and 49.1% when they were resolved at random; AIC choice with the most-doses rule overdosed in 8.1% of the studies at 96 patients and 0.2% at 384 (QD with QW; 18.1% at 48 patients, `results/summary.csv`).

**Table 7.** Share of studies in which the regimen chosen had a true toxicity above 0.30 (slope 1.5; cap 0.25; 2,000 studies per cell), by true driver, design and number of patients, for the AUC model always, the metric chosen by AIC and the true metric, with ties between schedules resolved toward the fewest doses, at random or toward the most doses.

| True driver | Design | Patients | AUC always: fewest doses | random | most doses | AIC choice: fewest doses | random | most doses | True metric known: fewest doses |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cmax | One schedule (QD) | 96 | 1.000 | 0.361 | 0.042 | 0.445 | 0.344 | 0.294 | 0.086 |
| Cmax | One schedule (QD) | 384 | 1.000 | 0.333 | 0.000 | 0.334 | 0.163 | 0.078 | 0.004 |
| Cmax | Two schedules (QD, QW) | 96 | 0.705 | 0.236 | 0.000 | 0.053 | 0.039 | 0.033 | 0.034 |
| Cmax | Two schedules (QD, QW) | 384 | 0.833 | 0.278 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Cmax | Three schedules (BID, QD, QW) | 96 | 0.961 | 0.321 | 0.001 | 0.066 | 0.047 | 0.038 | 0.039 |
| Cmax | Three schedules (BID, QD, QW) | 384 | 1.000 | 0.333 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| AUC | One schedule (QD) | 96 | 0.034 | 0.034 | 0.034 | 0.399 | 0.399 | 0.399 | 0.034 |
| AUC | One schedule (QD) | 384 | 0.001 | 0.001 | 0.001 | 0.278 | 0.278 | 0.278 | 0.001 |
| AUC | Two schedules (QD, QW) | 96 | 0.042 | 0.042 | 0.042 | 0.121 | 0.121 | 0.121 | 0.042 |
| AUC | Two schedules (QD, QW) | 384 | 0.001 | 0.001 | 0.001 | 0.003 | 0.003 | 0.003 | 0.001 |
| AUC | Three schedules (BID, QD, QW) | 96 | 0.037 | 0.037 | 0.037 | 0.125 | 0.125 | 0.125 | 0.037 |
| AUC | Three schedules (BID, QD, QW) | 384 | 0.000 | 0.000 | 0.000 | 0.002 | 0.002 | 0.002 | 0.000 |
| Cmin | One schedule (QD) | 96 | 0.000 | 0.017 | 0.026 | 0.015 | 0.026 | 0.035 | 0.000 |
| Cmin | One schedule (QD) | 384 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Cmin | Two schedules (QD, QW) | 96 | 0.000 | 0.426 | 0.639 | 0.000 | 0.048 | 0.081 | 0.000 |
| Cmin | Two schedules (QD, QW) | 384 | 0.000 | 0.491 | 0.737 | 0.000 | 0.001 | 0.002 | 0.000 |
| Cmin | Three schedules (BID, QD, QW) | 96 | 0.000 | 0.146 | 0.219 | 0.000 | 0.024 | 0.043 | 0.000 |
| Cmin | Three schedules (BID, QD, QW) | 384 | 0.000 | 0.040 | 0.061 | 0.000 | 0.001 | 0.002 | 0.000 |

AIC, Akaike information criterion; other abbreviations as in Table 1.

**Table 8.** Regimens chosen by the AUC model when Cmax was the driver (slope 1.5; cap 0.25; ties toward the fewest doses; 2,000 studies per row, separate seed).

| Design | Patients | Regimens chosen by the AUC model (share of studies; ties toward the fewest doses) |
| --- | --- | --- |
| One schedule (QD) | 96 | QW 280 mg (82.3%); QW 140 mg (14.1%); QW 560 mg (3.6%) |
| One schedule (QD) | 384 | QW 280 mg (98.0%); QW 140 mg (2.1%) |
| Two schedules (QD, QW) | 96 | QW 140 mg (70.1%); QW 70 mg (29.3%); none acceptable (0.5%); QW 280 mg (0.2%) |
| Two schedules (QD, QW) | 384 | QW 140 mg (82.5%); QW 70 mg (17.5%) |
| Three schedules (BID, QD, QW) | 96 | QW 140 mg (89.9%); QW 280 mg (6.3%); QW 70 mg (3.8%) |
| Three schedules (BID, QD, QW) | 384 | QW 140 mg (99.7%); QW 280 mg (0.3%) |

Abbreviations as in Table 1.

**Table 9.** Share of studies in which the regimen chosen had a true toxicity above the cap plus 0.05, for the Cmax driver by cap, design and number of patients (slope 1.5; 2,000 studies per cell; the rows with the cap 0.25 are those of the main analysis in Table 7, and the other rows come from separate runs with separate seeds).

| Cap | Design | Patients | AUC always: fewest doses | random | most doses | AIC choice: fewest doses | random | True metric known: fewest doses |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.15 | One schedule (QD) | 96 | 0.971 | 0.324 | 0.001 | 0.405 | 0.300 | 0.002 |
| 0.15 | One schedule (QD) | 384 | 1.000 | 0.333 | 0.000 | 0.333 | 0.162 | 0.000 |
| 0.15 | Two schedules (QD, QW) | 96 | 0.054 | 0.023 | 0.000 | 0.003 | 0.001 | 0.000 |
| 0.15 | Two schedules (QD, QW) | 384 | 0.001 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.15 | Three schedules (BID, QD, QW) | 96 | 0.297 | 0.105 | 0.000 | 0.016 | 0.006 | 0.000 |
| 0.15 | Three schedules (BID, QD, QW) | 384 | 0.126 | 0.042 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.25 | One schedule (QD) | 96 | 1.000 | 0.361 | 0.042 | 0.445 | 0.344 | 0.086 |
| 0.25 | One schedule (QD) | 384 | 1.000 | 0.333 | 0.000 | 0.334 | 0.163 | 0.004 |
| 0.25 | Two schedules (QD, QW) | 96 | 0.705 | 0.236 | 0.000 | 0.053 | 0.039 | 0.034 |
| 0.25 | Two schedules (QD, QW) | 384 | 0.833 | 0.278 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.25 | Three schedules (BID, QD, QW) | 96 | 0.961 | 0.321 | 0.001 | 0.066 | 0.047 | 0.039 |
| 0.25 | Three schedules (BID, QD, QW) | 384 | 1.000 | 0.333 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.35 | One schedule (QD) | 96 | 1.000 | 0.428 | 0.000 | 0.567 | 0.375 | 0.257 |
| 0.35 | One schedule (QD) | 384 | 1.000 | 0.372 | 0.000 | 0.381 | 0.192 | 0.086 |
| 0.35 | Two schedules (QD, QW) | 96 | 0.184 | 0.062 | 0.000 | 0.169 | 0.084 | 0.168 |
| 0.35 | Two schedules (QD, QW) | 384 | 0.043 | 0.014 | 0.000 | 0.032 | 0.016 | 0.032 |
| 0.35 | Three schedules (BID, QD, QW) | 96 | 0.733 | 0.250 | 0.000 | 0.208 | 0.101 | 0.196 |
| 0.35 | Three schedules (BID, QD, QW) | 384 | 0.889 | 0.296 | 0.000 | 0.040 | 0.020 | 0.040 |

AIC, Akaike information criterion; other abbreviations as in Table 1.

![Share of studies choosing a regimen with true toxicity above 30 percent by decision model and design: high for the AUC model in the one-schedule design, near zero when the true metric is known](shared/exposure-metric-schedule-identifiability/figures/figure-2-overdose.png)

**Figure 2.** Share of studies in which the regimen chosen had a true toxicity above 30%, by patients per study (log scale), for decisions using the AUC model always, the metric chosen by AIC and the true metric, in the one-schedule (solid) and three-schedule (dashed) designs, by true driver (slope 1.5; ties resolved toward the fewest doses; 2,000 studies per point). AIC, Akaike information criterion.

## Discussion {#article-discussion}

The three conference abstracts were read as abstracts only, and the studies they report differ from this one in their models and endpoints, so the comparison below is one of direction. The results do not contradict them. Within one dosing schedule the metrics were correlated at 0.955 or more, and AIC could not tell them apart in most studies, which is of the same order as the correlation of 0.95 at which Hu and Gheyas reported that AIC could not select ([3](#ref-3)). Their finding that the wrong metric did not change the dose chosen appears here only for the tie rules that favour the most frequent dosing (4.2% or fewer overdoses at 96 and 384 patients when the AUC model was used and Cmax was the driver). The simulation adds that the metrics become distinguishable once the study contains a schedule that decouples Cmax and Cmin from AUC, and that the QD and BID pair, whose Cmax and Cmin differ from QD by factors of 0.869 and 1.198, did not do so. What distinguished the metrics was the extreme contrast of QW (Cmax 3.4 times and Cmin 0.105 times those of QD); I did not test intermediate schedules, and a pair with a smaller contrast would probably have less power. This is consistent with the observation of Kågedal et al. that a relationship from one dose group may not predict another ([2](#ref-2)).

The decision results combine two errors. One is extrapolation: a one-schedule design never allocates QW, so any model must extrapolate to it, and even the model of the true metric overdosed in 8.6% of the studies at 96 patients. The other is the metric: an AUC model assigns one toxicity to all schedules at one weekly dose, so the choice among schedules is decided by an assumption outside the analysis, here the tie rule. When ties were resolved toward the fewest doses, the AUC model selected QW and overdosed in most or all studies of the designs tried at the cap of 0.25; when resolved at random, in about a quarter to a third; when resolved toward the most doses, in 4.2% or fewer. The conventional use of AUC is therefore not wrong in itself; it is silent about schedule. The polarization between "all studies" and "4.2% or fewer" comes from this structure and from the cap and threshold chosen, as Table 9 shows, and it should not be read as a typical operating characteristic. The overdose share of the AUC model for QD with QW rose with the number of patients because its prediction converged on the mixture of the two schedules (Table 8), which makes QW 140 mg the dose that exceeds 0.30; at small numbers noise often selected the safe QW 70 mg.

Two schedules that include QW were about as informative as three, with differences within about two standard errors. In the designs with QW, the weaker signal (slope 0.75) needed about four times as many patients for the AUC and Cmax drivers and about twice as many for Cmin, and the designs without QW did not reach the probabilities of the designs with QW even at 384 patients.

With AUC as the driver, the true metric was selected in fewer than one third of the studies at 48 to 192 patients. The diagnostic run measured that the true model has the lowest mean deviance but is often beaten by one of the two near-equal competitors on either side. The mechanism proposed here, that the middle position of log AUC makes the lower of two competitors more often below the true model, is consistent with the diagnostic and was not tested further.

### Limitations

One pharmacokinetic structure and one parameter set were used, with η independent and a single bank of individuals, and linear pharmacokinetics (AUC proportional to dose) was assumed. A logistic form on the logarithm of one metric was both the true and the fitted form, the slopes of 1.5 and 0.75 are strong (a doubling of the metric multiplies the odds by 2.8 or 1.7), only a binary toxicity at a weekly horizon was simulated, efficacy was not modelled, and the decision rule (highest weekly dose with predicted toxicity of at most 0.25; overdose above 0.30) and the tie rules are assumptions; the sensitivity analysis varied the cap for the Cmax driver only. Exposure was known without error, so the loss of information from shrinkage of individual estimates or from assay error is not represented, and no confounder was simulated, so the findings do not address the confounding examined by De Vos et al. ([4](#ref-4)). Real toxicity may depend on the time course of exposure and on more than one metric.

The schedules were limited to BID, QD and QW, and QW is extreme: its mean Cmax is 3.4 times and its mean Cmin 0.105 times those of QD, and its log Cmin has a very wide spread (SD 1.878, minimum near −22), so that a model of log Cmin is dominated by a few individuals in QW arms. Randomizing patients to a weekly schedule of 560 mg, whose true toxicity is 0.811 if Cmax is the driver (Table 1), would be unacceptable in practice, and the simulation is not a design recommendation. The one-schedule design could not allocate QW at all, and extrapolation to it is likely the main reason for its overdoses, although I did not separate the two sources of error by a decomposition. Allocation was by rotation among arms, with every weekly dose in every design, and patients were random individuals of one bank; dropout was not simulated and metrics were computed at steady state on a 0.25 h grid, which is coarse for the peak of BID but changes Cmax by little. Cmin as a driver is less plausible than AUC or Cmax and its results should be read with caution. AIC selection among three one-predictor models ignores the uncertainty of selection, and I did not evaluate model averaging or a model with several metrics. The one-third reference for the AUC driver is not exact (see Results), and the explanation for it is a hypothesis.

## Conclusion {#article-conclusion}

In simulated dose-finding studies of 48 to 384 patients with a toxicity driven by one of AUC, Cmax and Cmin, an exposure–response analysis that used QD alone, or BID with QD, could not reliably distinguish the metrics: the log metrics were correlated at 0.955 to 0.994 and the best two AIC values were within 2 in up to 98.4% of studies. Adding the extreme schedule QW decoupled the metrics (correlations 0.483 to 0.772) and made the true metric the one selected in at least 97.3% of studies at 192 patients with a slope of 1.5, and with a weaker signal about two to four times as many patients were needed in the designs with QW. The cost of a wrong metric for the regimen chosen appeared to come from two sources, extrapolation to a schedule that was not allocated and the arbitrary tie between schedules of equal AUC (which I did not separate by a decomposition), and the overdose share ranged from 0.0% to 100% with the design, the cap and the tie rule. The numbers hold for the simulated pharmacokinetics, the logistic form, exact exposure, the extreme QW contrast and the decision rules assumed.

## Data and code availability {#reproduce}

No patient data were used. The companion contains the simulation (`simulate.R`), the diagnostic and sensitivity runs (`diagnose_extra.R`), the table script (`mk_tables.R`), the figure script (`figures.R`), the aggregate results (`results/summary.csv` and the diagnostic and sensitivity files), the true toxicity rates, the calibration and the mean metrics of each regimen, and the session information. The seed is 20261124 (`Rscript simulate.R 2000 8`, about 14 minutes, and `Rscript diagnose_extra.R 8`, about 13 minutes, on a desktop computer with 8 worker processes). Base R and, for the figures, ggplot2 (4.0.4) are required; the numbers in the tables can be checked against the files in `results/`. The numbers depend on the random-number stream of the R version used.

[Download the companion: code and aggregate results](shared/exposure-metric-schedule-identifiability/exposure-metric-schedule-identifiability-companion.zip)

## References {#article-references}

1. <span id="ref-1"></span>U.S. Food and Drug Administration. Optimizing the dosage of human prescription drugs and biological products for the treatment of oncologic diseases: guidance for industry [Internet]. 2024 Aug [cited 2026 Nov 17]. Docket FDA-2022-D-2827. Available from: [FDA guidance page](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/optimizing-dosage-human-prescription-drugs-and-biological-products-treatment-oncologic-diseases)
2. <span id="ref-2"></span>Kågedal M, Liu Q, Jin JY. Selection of exposure metrics AUC, Cmax or Cmin in exposure response analyses – a simulation study [Conference abstract]. PAGE 25 (2016): Abstr 5707 [Internet]. Population Approach Group in Europe [cited 2026 Nov 19]. Available from: [PAGE abstract 5707](https://www.page-meeting.org/Abstracts/selection-of-exposure-metrics-auc-cmax-or-cmin-in-exposure-response-analyses-a-simulation-study/)
3. <span id="ref-3"></span>Hu H, Gheyas F. Choice of exposure metric in exposure-response modeling [Conference abstract]. PAGE 32 (2024): Abstr 11091 [Internet]. Population Approach Group in Europe [cited 2026 Nov 19]. Available from: [PAGE abstract 11091](https://www.page-meeting.org/Abstracts/choice-of-exposure-metric-in-exposure-response-modeling/)
4. <span id="ref-4"></span>De Vos K, Neyens M, Goeyvaerts N, Duval V, Iwaki Y, Perez-Ruixo JJ, et al. Choosing the right exposure metric: power and confounding in exposure-response (E-R) models [Conference abstract]. PAGE 34 (2026): Abstr 11966 [Internet]. Population Approach Group in Europe [cited 2026 Nov 19]. Available from: [PAGE abstract 11966](https://www.page-meeting.org/Abstracts/choosing-the-right-exposure-metric-power-and-confounding-in-exposure-response-e-r-models/)
5. <span id="ref-5"></span>R Core Team. R: A language and environment for statistical computing [Software]. 2026. Version 4.5.3. [R Project](https://www.r-project.org/)
