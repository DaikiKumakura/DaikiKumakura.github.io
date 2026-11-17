## Abstract {#article-abstract}

A dose-proportionality study asks whether exposure scales with dose, and the power model, in which the area under the concentration–time curve (AUC) is proportional to dose raised to a power β, is a common way to answer it. I simulated parallel-group single-dose studies of an intravenous drug whose elimination follows Michaelis–Menten kinetics, with saturation at the highest dose (80 mg) set to none, mild, moderate or strong, between-subject variability in clearance and volume, and 6 to 48 subjects per dose. AUC was estimated by noncompartmental analysis (NCA) from 4 samples to 24 h or 11 samples to 48 h, and was also taken as the true value (oracle). Proportionality was declared when the 90% confidence interval (CI) of β lay inside a window set by the dose ratio (0.893 to 1.107 for 10 to 80 mg). With no saturation and 24 subjects per dose, proportionality was declared in 67.7% of 2,000 studies with 4 samples (95.6% at 48 per dose, 17.3% at 12). Moderate saturation (true β 1.166) was almost never declared proportional over 10 to 80 mg (at most 0.2%), but over 20 to 40 mg the true β of 1.154 lay inside the window and proportionality was declared in 29.2% of studies at 24 per dose and 50.8% at 48. Strong saturation (true β 1.421) had a CI excluding 1 in at least 99.9% of studies over 10 to 80 mg and was never declared proportional, but the 4-sample design overestimated β (mean 1.558 at 24 per dose against 1.420 for the true AUC and 1.458 for 11 samples). A diagnostic run traced this to the extrapolated tail of the AUC beyond a last sample at 24 h, when the concentration at 80 mg was still about twice Km: 9 samples to 24 h gave the same bias as 4, and only the 48 h window reduced it. Mild saturation (true β 1.049) is inside the window and is not a failure of detection. These results hold for one set of assumed pharmacokinetic parameters, one dose-escalation design and one NCA method.

## Introduction {#article-introduction}

Dose proportionality is checked in early studies by comparing exposure across dose levels. The power model fits log AUC to log dose, and the slope β equals 1 for proportionality. Smith et al. proposed to compare the CI of the ratio of dose-normalized geometric mean exposures between the highest and lowest dose with an acceptance interval fixed in advance, and noted that for a power model the acceptance region for β depends only on the dose ratio ([1](#ref-1)). Hummel et al. reviewed approaches in phase I dose-escalation studies, found the power model to be the preferred approach in about one-third of the articles they reviewed from 2002 to 2006, and showed by power calculations that a bioequivalence-type acceptance interval of 0.8 to 1.25 lacks power to conclude proportionality across a complete dose range in typical phase I studies; they proposed 0.5 to 2 for exploratory assessments ([2](#ref-2)). I read both references through their abstracts only.

Two features of real studies are less often quantified together. Elimination can saturate, in which case exposure rises more than in proportion to dose. And the exposure of each subject in a dose-escalation study is frequently estimated from a few samples, so that the AUC includes an extrapolated tail. This article asks: **when elimination saturates, how often does a power-model study with 6 to 48 subjects per dose declare dose proportionality, and does the sampling design change the answer?** The answer is computed by simulation, so that the true β is known for every setting.

## Methods {#article-methods}

### Pharmacokinetic model and population

Each subject received one intravenous bolus of 10, 20, 40 or 80 mg (wide range, ratio 8) or 20 or 40 mg (narrow range, ratio 2) in a parallel-group design with 6, 12, 24 or 48 subjects per dose. The concentration followed one-compartment kinetics with Michaelis–Menten elimination, dC/dt = −Vmax·C / (Km + C), where C is the concentration, Vmax is the maximal elimination rate in concentration units per hour and Km is the Michaelis constant. The initial concentration C₀ was dose divided by volume. The typical volume was 50 L and the typical linear clearance (Vmax·V / Km, the clearance at low concentration) was 5 L/h. Between subjects, log clearance had a standard deviation (SD) of 0.30 and log volume 0.20, independently; Km was the same for everyone. The concentration and the AUC from 0 to infinity were computed in closed form (the concentration through the Lambert W function ([3](#ref-3)); AUC = C₀(C₀/2 + Km)/Vmax), and I checked the closed forms against a numerical Runge–Kutta solution (largest relative difference 1.1 × 10⁻⁶ in four cases).

Saturation was set by the ratio of the initial concentration of 80 mg at the typical volume (1.6 mg/L) to Km: none (Km very large, linear), mild (ratio 0.25), moderate (ratio 1) and strong (ratio 4). The true β of each setting was the slope of the log geometric mean AUC against log dose across the doses of the design, computed from 200,000 simulated subjects per dose (Table 1). These are assumed values, not parameters of any drug.

**Table 1.** True power-model slope β and acceptance window by saturation and dose range.

| Saturation (C₀ of 80 mg / Km) | True β, 10–80 mg | True β, 20–40 mg |
| --- | --- | --- |
| None | 1.000 | 1.000 |
| Mild (0.25) | 1.049 | 1.042 |
| Moderate (1) | 1.166 | 1.154 |
| Strong (4) | 1.421 | 1.418 |
| Acceptance window for β | 0.893 to 1.107 | 0.678 to 1.322 |

The window is 1 + ln(0.8)/ln(r) to 1 + ln(1.25)/ln(r) for dose ratio r. Under the power model the ratio of dose-normalized geometric mean AUC between the highest and lowest dose is r^(β − 1), so this window corresponds to a ratio between 0.8 and 1.25, and the acceptance region for β depends only on the dose ratio, as Smith et al. noted ([1](#ref-1)). I derived the window formula here and applied it to the CI of β from all doses, not to a CI of the ratio between the two extreme doses. A true β inside the window is within the accepted departure from proportionality, and I call it proportional by this criterion; it does not mean β = 1: across 10 to 80 mg, the true β of 1.049 (ratio 8^0.049 = 1.11) is inside and 1.166 (ratio 1.41) is outside.

### Sampling and AUC estimation

In the main comparison, samples were drawn at 0.5, 2, 8 and 24 h (4 samples) or at 0.25, 0.5, 1, 2, 4, 6, 8, 12, 24, 36 and 48 h (11 samples) after the dose. These two designs differ in the number of samples, in the number of terminal points (2 or 3) and in the last sampling time (24 or 48 h); the diagnostic run below separates the three. Each observed concentration was the true concentration multiplied by a lognormal error with SD 0.10 on the log scale. The AUC was computed by noncompartmental analysis (NCA): the concentration at time 0 was back-extrapolated from the first two samples (log-linear, or the first sample if the second was not lower), AUC from 0 to the last sample used the linear-up/log-down trapezoidal rule, and the part beyond the last sample was the last concentration divided by the terminal rate constant, estimated by log-linear regression on the last 2 (4 samples) or 3 (11 samples) samples. If the estimated terminal rate was not positive, the AUC was not extrapolated (at most 0.31% of subjects in any setting). The third estimate, called the oracle below, was the true AUC from 0 to infinity of each simulated subject, which isolates the error due to sampling the concentration–time curve.

### Power-model analysis and outcomes

For each simulated study I fitted log AUC = a + β·log dose by least squares to all subjects (one AUC per subject) and computed the two-sided 90% CI of β from the t distribution. Proportionality was declared if the CI lay entirely inside the window. I also recorded whether the CI excluded 1. When the model is exactly proportional, the second probability is the type I error rate and should be about 0.10; I treat it as a check of the simulation and not as a decision rule. Each setting (4 saturation levels × 2 dose ranges × 4 sample sizes × 3 AUC estimates) was simulated 2,000 times (seed 20261119; R 4.5.3 ([4](#ref-4))). The Monte Carlo SE of a probability is at most 0.011. The three AUC estimates were computed in the same simulated subjects within each study.

### Diagnostic run

To examine the AUC bias under saturation, I simulated 5,000 subjects at each dose of the wide range for no, moderate and strong saturation (seed 20261121) with four sampling designs: the 4-sample design with 2 terminal points; the same 4 samples with 3 terminal points; 9 samples to 24 h (the first nine times of the 11-sample design) with 3 terminal points; and the 11-sample design to 48 h with 3 terminal points. For each I saved the ratio of the estimated to the true AUC; the ratio of the observed part (0 to last sample) to the true AUC over the same interval, using the closed form; the ratio of the extrapolated tail to the true tail beyond the last sample; the ratio of the estimated terminal rate constant to the true local elimination rate at the last sample time, Vmax/(Km + C); the true last concentration divided by Km; and the share of the estimated AUC that was extrapolated, including the share of subjects with more than 20% extrapolated. The 20% threshold is a descriptive cut-off chosen here.

## Results {#article-results}

![Probability of declaring proportionality and of a CI excluding 1, by sample size, saturation and dose range](shared/dose-proportionality-sparse-sampling/figures/figure-1-power-model.png)

**Figure 1.** Power-model studies with the 4-sample AUC (AUC, area under the concentration–time curve; CI, confidence interval). Panel A: probability that the 90% CI of β lay inside the acceptance window. Panel B: probability that the 90% CI excluded 1. Colours give the true saturation (C₀ of 80 mg divided by Km), line types the dose range. Each point is 2,000 simulated studies; subjects per dose are shown on a log scale.

### Declaring proportionality needs many subjects even without saturation

With linear elimination, the probability of declaring proportionality over 10 to 80 mg with the 4-sample AUC was 0.006 at 6 subjects per dose, 0.173 at 12, 0.677 at 24 and 0.956 at 48 (Figure 1A, Table 2). The mean width of the 90% CI of β fell from 0.274 to 0.095 over the same sizes, against a window width of 0.214. Over 20 to 40 mg the window is wider (0.644) but the CI is wider still (mean width 0.427 at 24 per dose), and the probabilities were 0.018, 0.121, 0.612 and 0.942. The probability that the CI excluded 1 was 0.094 to 0.108 at every size, close to the nominal 0.10, as expected when the model is exactly proportional.

**Table 2.** Probability of declaring proportionality (90% CI of β inside the window) with 4-sample AUC, over 2,000 studies per cell.

| Saturation | Dose range | 6 per dose | 12 per dose | 24 per dose | 48 per dose |
| --- | --- | --- | --- | --- | --- |
| None | 10–80 mg | 0.006 | 0.173 | 0.677 | 0.956 |
| None | 20–40 mg | 0.018 | 0.121 | 0.612 | 0.942 |
| Mild | 10–80 mg | 0.005 | 0.106 | 0.367 | 0.621 |
| Mild | 20–40 mg | 0.011 | 0.112 | 0.566 | 0.894 |
| Moderate | 10–80 mg | 0.000 | 0.002 | 0.001 | 0.000 |
| Moderate | 20–40 mg | 0.005 | 0.068 | 0.292 | 0.508 |
| Strong | 10–80 mg | 0.000 | 0.000 | 0.000 | 0.000 |
| Strong | 20–40 mg | 0.000 | 0.001 | 0.000 | 0.000 |

### A proportional verdict applies to the dose range studied

Mild saturation (true β 1.049 over 10 to 80 mg) is inside the window, so a proportional verdict is correct by the criterion, and it was reached in only 0.367 of studies at 24 per dose and 0.621 at 48 (Table 2). The CI excluded 1 in 0.338 and 0.515 of those studies (Figure 1B), which is a departure that the data can detect and the criterion still accepts. Moderate saturation (true β 1.166) was rejected over 10 to 80 mg: the CI excluded 1 in 0.632, 0.892, 0.996 and 1.000 of studies at 6, 12, 24 and 48 per dose, and proportionality was declared in at most 0.002. Over 20 to 40 mg the true β of 1.154 is inside the window (0.678 to 1.322), and the CI excluded 1 in only 0.215 of studies at 12 per dose and 0.326 at 24, while proportionality was declared in 0.292 at 24 and 0.508 at 48 per dose. The same elimination kinetics thus gave different verdicts over the two dose ranges, as the criterion defines them (dose-normalized AUC 1.41 times higher at the top dose over 10 to 80 mg, 1.11 times over 20 to 40 mg). Strong saturation (true β 1.42) was detected at every size over 10 to 80 mg (CI excluding 1 in at least 0.999 of studies) and in 0.470 to 0.999 of studies over 20 to 40 mg, and was never declared proportional (at most 0.001).

### The 4-sample design overestimates the slope under strong saturation

With no or mild saturation, the mean estimated β from the 4-sample AUC was within 0.002 of the result from the true AUC (Table 3, 24 per dose, 10 to 80 mg). With moderate saturation it was 0.015 higher (1.179 against 1.164), a small bias on which the verdict did not depend. Under strong saturation it was 1.558, against 1.420 from the true AUC and 1.458 from the 11-sample AUC, a bias of 0.14 against 0.04, with an SD across studies of 0.062 against 0.042 and 0.049. The CI width was 0.191 against 0.139 and 0.154. The bias did not change the verdict (the CI excluded 1 in at least 99.9% of studies with every method) but it put the point estimate 0.14 above the true β, about a third of the distance (0.42) between the proportional value and the true β.

**Table 3.** Mean estimated β, SD across studies and mean CI width at 24 subjects per dose, 10–80 mg (2,000 studies per cell).

| Saturation (true β) | AUC | Mean β | SD of β | Mean CI width |
| --- | --- | --- | --- | --- |
| None (1.000) | True | 0.999 | 0.039 | 0.131 |
| None (1.000) | 11 samples | 0.999 | 0.040 | 0.132 |
| None (1.000) | 4 samples | 0.999 | 0.041 | 0.135 |
| Moderate (1.166) | True | 1.164 | 0.040 | 0.133 |
| Moderate (1.166) | 11 samples | 1.163 | 0.040 | 0.135 |
| Moderate (1.166) | 4 samples | 1.179 | 0.044 | 0.144 |
| Strong (1.421) | True | 1.420 | 0.042 | 0.139 |
| Strong (1.421) | 11 samples | 1.458 | 0.049 | 0.154 |
| Strong (1.421) | 4 samples | 1.558 | 0.062 | 0.191 |

![Estimated AUC divided by true AUC at each dose for four sampling designs](shared/dose-proportionality-sparse-sampling/figures/figure-2-auc-bias.png)

**Figure 2.** Median ratio of the NCA AUC to the true AUC at each dose (5,000 subjects per dose) for four sampling designs, by saturation. The designs are 4 samples to 24 h with 2 or 3 terminal points, 9 samples to 24 h and 11 samples to 48 h.

The diagnostic run located the bias (Figure 2, Table 4). Under strong saturation the median ratio of the 4-sample AUC to the true AUC was 1.009 at 10 mg, 1.022 at 20 mg, 1.089 at 40 mg and 1.249 at 80 mg, against 1.001, 1.002, 1.008 and 1.060 for 11 samples. The observed part of the AUC was not the source: at 80 mg its ratio to the true value was 0.993 with 4 samples and 0.998 with 11. The extrapolated tail was: its median ratio to the true tail was 1.780 at 80 mg with 4 samples, and the extrapolated share of the estimated AUC was 0.514. The sample at 24 h was still in the saturating range, with a true median concentration of 2.1 times Km. The estimated terminal rate constant was 0.828 times the true local rate at that time, consistent with a rate constant averaged over concentrations that were still saturating and lower than the rate that applies as the concentration falls.

Using 9 samples to 24 h gave the same bias as 4 samples (ratio 1.241 against 1.249), and using 3 terminal points rather than 2 did not reduce it (1.282). Extending the last sample to 48 h reduced the AUC ratio to 1.060, with a true last concentration of 0.79 times Km, and the extrapolated share to 0.148, although the tail ratio itself stayed high (1.645). The AUC bias therefore followed the sampling window, through the share of the AUC that is extrapolated, and not the number of samples. The 4-sample and 9-sample designs also differ in their sampling times, so the comparison isolates the number of samples only approximately. Without saturation the ratio was 1.003 to 1.006 at every dose for all four designs (extrapolated share about 0.09 for the 24 h designs and 0.008 for 48 h).

**Table 4.** Diagnostic run at 80 mg under strong saturation (C₀ / Km = 4; 5,000 subjects, medians).

| Sampling design | AUC ratio | Observed-part ratio | Tail ratio | Rate constant / true local rate | Last concentration / Km | Extrapolated share | Subjects with > 20% extrapolated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 samples to 24 h, 2 terminal points | 1.249 | 0.993 | 1.780 | 0.828 | 2.143 | 0.514 | 0.964 |
| 4 samples to 24 h, 3 terminal points | 1.282 | 0.990 | 1.868 | 0.788 | 2.143 | 0.529 | 0.980 |
| 9 samples to 24 h, 3 terminal points | 1.241 | 1.000 | 1.761 | 0.834 | 2.143 | 0.505 | 0.965 |
| 11 samples to 48 h, 3 terminal points | 1.060 | 0.998 | 1.645 | 0.754 | 0.786 | 0.148 | 0.374 |

AUC ratio, estimated AUC divided by true AUC from 0 to infinity; observed-part ratio, estimated over true AUC from 0 to the last sample; tail ratio, estimated over true AUC beyond the last sample; extrapolated share, tail divided by estimated AUC.

## Discussion {#article-discussion}

Three things limited the power-model verdict in these simulations. The first is the criterion itself. A window of 0.8 to 1.25 on the dose-normalized ratio between extreme doses is hard to satisfy: with linear elimination and 12 subjects per dose, proportionality was declared in only 17.3% of studies over a dose ratio of 8, and about 24 subjects per dose were needed to reach two thirds (Table 2). This agrees in direction with the power calculations of Hummel et al., who concluded that the criterion lacks power in typical phase I studies ([2](#ref-2)). I did not reproduce their calculations or their proposed window, and my designs differ from theirs.

The second is the dose range. The CI of β depends on the spread of log dose, and so does the window; with a ratio of 2 the CI is about three times wider (0.427 against 0.135 at 24 per dose), but the window is three times wider too. As a result, a clearly non-proportional drug across 10 to 80 mg (moderate saturation, 1.41 times higher dose-normalized AUC at the top dose) was accepted as proportional by the criterion over 20 to 40 mg, where the same kinetics give a ratio of 1.11. This is a consequence of the criterion, not an error of the model. A proportional verdict is a statement about the dose range that was studied.

The third is the estimation of AUC itself, and here the diagnostic run gave a measured answer. Under strong saturation the observed part of the AUC was unbiased and the extrapolated tail was overestimated by a factor of 1.78 at 80 mg, where the last sample at 24 h still lay in the saturating range (about twice Km). By a simple calculation, a first-order extrapolation at the true local rate would overestimate the tail by (Km + C)/(Km + C/2), which is 1.5 at C = 2.1 Km, because the true rate rises as the concentration falls; the estimated rate constant, 0.83 of the local rate, would add about 1.2. The product, about 1.8, is consistent with the observed 1.78, but the run did not separate the two parts. The comparison of 4 and 9 samples to 24 h and of 24 h and 48 h windows shows that the window, and not the count, mattered; the main comparison of 4 and 11 samples (Table 3) mixed the two. With the 4-sample design, 96% of subjects at 80 mg had more than 20% of the AUC extrapolated, so the extrapolated share, which a study report would show, flags the problem before β is fitted. Its effect on β was a steeper apparent increase of AUC with dose, in the direction of the saturation itself (1.558 against 1.420). A bias of this kind could also push a drug that lies near the edge of the window out of it; I did not simulate that case.

### Limitations

One set of pharmacokinetic parameters (volume 50 L, linear clearance 5 L/h, between-subject SD 0.30 and 0.20, error SD 0.10) and a one-compartment, intravenous bolus model with parallel dose groups were used. Oral absorption, a crossover design in which each subject receives several doses, mixed-effects estimation of β and population pharmacokinetic modelling were not studied, and the loss of power or the bias in those designs may differ. Km was the same for every subject and was set relative to the 80 mg dose, so over 20 to 40 mg the highest dose had half the saturation (C₀/Km) of the setting named in Table 1. Saturation was set at four levels and the true β differs by dose range, so the probabilities in Table 2 apply to those settings. The NCA used a fixed rule (last 2 or 3 samples for the terminal rate); other rules, such as selecting the terminal phase by the adjusted R², might behave differently, and a regression through 2 points cannot be judged by R² at all. I did not apply an extrapolation limit to exclude AUC values, and I did not check whether the variance of log AUC was equal across doses. The sampling times were fixed and the same for every subject. Concentrations below a quantification limit were not simulated. The window of 0.8 to 1.25 on the ratio of the extreme doses was used for every setting; the wider window of 0.5 to 2 proposed for exploratory work ([2](#ref-2)) was not evaluated. I did not compare the power model with an analysis based on dose-normalized AUC or with a Michaelis–Menten fit to the concentrations. The accounts of the two references are from their abstracts only.

## Conclusion {#article-conclusion}

In simulated parallel-group studies of an intravenous drug with saturable elimination, a power-model assessment over 10 to 80 mg declared proportionality in 67.7% of studies with 24 subjects per dose when elimination was linear, and almost never when saturation was moderate or strong (true β 1.166 and 1.421; at most 0.2% of studies). Over 20 to 40 mg, the wider window accepted moderate saturation (true β 1.154) in 29.2% of studies at 24 per dose and 50.8% at 48, so a proportional verdict applies to the dose range studied. Estimating AUC from 4 samples to 24 h overestimated β under strong saturation (1.558 against 1.420 for the true AUC; 1.458 with 11 samples to 48 h). The diagnostic run located the overestimate in the extrapolated tail, which was 51% of the AUC at 80 mg where the last sample, at 24 h, was still above Km; 9 samples to 24 h gave the same bias, so the window and not the number of samples explained it. The numbers hold for the assumed pharmacokinetic parameters, the intravenous parallel design and the fixed NCA rule.

## Data and code availability {#reproduce}

No subject-level data were used. The companion contains the simulation (`simulate.R`), the diagnostic run (`diagnose_mechanism.R`), the check of the closed forms (`check_closed_form.R`), the figure script (`figures.R`), the aggregate results (`results/summary.csv` and `results/diagnostic-mechanism.csv`) and the session information. The seeds are 20261119 (`Rscript simulate.R 2000`, about 12 minutes on a desktop computer) and 20261121 (`Rscript diagnose_mechanism.R`). Base R and ggplot2 (4.0.4) are required; the numbers in the tables can be checked against `results/summary.csv` and `results/diagnostic-mechanism.csv`.

[Download the companion: code and aggregate results](shared/dose-proportionality-sparse-sampling/dose-proportionality-sparse-sampling-companion.zip)

## References {#article-references}

1. <span id="ref-1"></span>Smith BP, Vandenhende FR, DeSante KA, Farid NA, Welch PA, Callaghan JT, et al. Confidence interval criteria for assessment of dose proportionality. Pharm Res. 2000;17(10):1278–1283. [doi:10.1023/A:1026451721686](https://doi.org/10.1023/A:1026451721686)
2. <span id="ref-2"></span>Hummel J, McKendrick S, Brindley C, French R. Exploratory assessment of dose proportionality: review of current approaches and proposal for a practical criterion. Pharm Stat. 2009;8(1):38–49. [doi:10.1002/pst.326](https://doi.org/10.1002/pst.326)
3. <span id="ref-3"></span>Schnell S, Mendoza C. Closed form solution for time-dependent enzyme kinetics. J Theor Biol. 1997;187(2):207–212. [doi:10.1006/jtbi.1997.0425](https://doi.org/10.1006/jtbi.1997.0425)
4. <span id="ref-4"></span>R Core Team. R: A language and environment for statistical computing [Software]. 2026. Version 4.5.3. [R Project](https://www.r-project.org/)
