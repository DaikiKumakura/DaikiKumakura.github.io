## Abstract {#article-abstract}

Tumour growth inhibition models fitted to xenograft studies are used to rank compounds by potency and to project the response to untested doses. Some of them describe the vehicle tumours with exponential growth, although vehicle tumours may slow down as they grow. I simulated xenograft studies with 5 arms (vehicle and four constant drug concentrations, 8 animals per arm), vehicle tumours that grow in a Gompertz way, and a drug that adds a concentration-dependent kill rate to the log growth rate (maximal kill rate 0.20 per day, half-maximal concentration 3), and fitted two models by least squares to the log tumour volume: an exponential-growth model and the correct Gompertz model. Three Gompertz rates (0.02, 0.05 and 0.10 per day, with the same vehicle volume at day 21) and three study durations (14, 21 and 28 days) were simulated 2,000 times each. The half-maximal concentration was recovered by both models (median 2.99 to 3.01 in all 18 cells). The exponential model underestimated the maximal kill rate in every cell (for example 0.153, 0.135 and 0.121 per day at 14, 21 and 28 days with a Gompertz rate of 0.05, against 0.20), and the bias grew with the study duration and with the Gompertz rate. A closed-form approximation, which treats the exponential fit as a straight line through the origin fitted to the saturating log difference between treated and vehicle tumours, reproduced the nine median estimates within 0.001. In this design, the exponential model predicted too small a treated-to-vehicle volume ratio at day 28 for a concentration inside the tested range (5): the median predicted ratio was 0.46 of the true ratio after 14 days and 0.78 after 28 days (Gompertz rate 0.05); at the last observation day it was 0.93 and 0.78. The Akaike information criterion (AIC) preferred the Gompertz model in about 96% or more of the studies in 8 of 9 cells (at least 98.8% in 7), and in 46.0% of the studies in the nearly exponential case (rate 0.02) at 14 days. The results hold for a constant drug concentration, a kill-rate effect added to the log growth rate without delay, and one set of assumed parameters.

## Introduction {#article-introduction}

Pharmacokinetic–pharmacodynamic models of tumour growth in xenograft mice link a dosing regimen to tumour volume. In the model of Simeoni et al., vehicle tumours grow exponentially and then linearly, the growth rate of treated tumours is reduced in proportion to drug concentration and to the number of proliferating cells, and the model parameters were proposed for ranking compounds by potency and for predicting the response to other doses and schedules ([1](#ref-1)). I read that reference through its abstract only. The model simulated here is simpler: the kill rate depends on drug concentration alone and is subtracted from the log growth rate, and there is no linear growth phase, no dependence on the number of proliferating cells and no cell-death delay.

The question is how much the form of the vehicle growth matters for these uses. When the vehicle tumours grow in a saturating way and the model assumes exponential growth, the shape of the curve in the vehicle arm is misfitted, and the drug parameters are fitted jointly with it. Gompertz growth is one saturating form, chosen here as an example. The practical consequence depends on the parameter and on the use. **If the vehicle tumours follow a Gompertz curve and the analysis assumes exponential growth, which of the potency (the concentration for half-maximal kill), the maximal kill rate and the projected volume ratio for an untested concentration are biased, how does the bias depend on the study duration, and can a model comparison reveal it?** The answer is obtained by simulation with known parameters.

## Methods {#article-methods}

### Simulated studies

Let x be the natural log of the tumour volume (mm³). In an untreated tumour, dx/dt = β (x∞ − x), a Gompertz curve with rate β per day and plateau x∞. Treatment adds a constant kill rate k(C) = kmax·C / (EC50 + C), so dx/dt = β (x∞ − x) − k(C), and the solution is x(t) = x_ss + (x₀ − x_ss) exp(−β t) with x_ss = x∞ − k(C)/β. The kill rate k and the concentration C are constant over the study; the arms were C = 0 (vehicle), 1, 3, 10 and 30 in arbitrary units. The true parameters were kmax = 0.20 per day (the maximal kill rate) and EC50 = 3 (the concentration at which the kill rate is half of kmax, in the same arbitrary units as C). The initial volume was 150 mm³ in the median animal, with a between-animal standard deviation (SD) of 0.10 in x₀. Each animal had measurements on days 0, 3, 7, 10, 14, 18, 21, 25 and 28, truncated at the study duration (14, 21 or 28 days; 200, 280 or 360 observations per study), with a normal error of SD 0.15 on the log scale. There were 8 animals per arm. The Gompertz rate β was set to 0.05, 0.02 or 0.10 per day, and the plateau x∞ was chosen so that the vehicle volume at day 21 was 1,470 mm³ in all three settings (Table 1). These are assumed values, not parameters of a compound or a tumour model.

**Table 1.** Gompertz settings (vehicle tumours) and the true treated-to-vehicle volume ratio at day 28 for concentration 5.

| Gompertz rate β (per day) | Plateau volume (mm³) | Vehicle volume at day 14 / 21 / 28 (mm³) | True volume ratio at day 28, concentration 5 |
| --- | --- | --- | --- |
| 0.02 | 116,509 | 762 / 1,470 / 2,603 | 0.069 |
| 0.05 | 5,022 | 878 / 1,470 / 2,113 | 0.152 |
| 0.10 | 2,021 | 1,064 / 1,470 / 1,726 | 0.309 |

### Fitted models and outcomes

Both models were fitted by least squares to the log volume of all observations pooled across animals (the BFGS quasi-Newton method of R's optim with three starting points, parameters on the log scale where they must be positive; for the Gompertz model one of the three starting points was close to the true values). The exponential model is x(t) = x₀ + (kg − k(C)) t with parameters x₀, kg (the exponential growth rate, per day), kmax and EC50. The Gompertz model has the true form, with parameters x₀, x∞, β, kmax and EC50. The fits ignore the correlation of repeated measurements in the same animal. For each study I saved the estimates of kmax and EC50, the predicted log ratio of treated to vehicle volume at concentration 5 (a concentration inside the tested range and not one of the four treated arms) at day 28 and at the last observation day, and the residual sum of squares (SS). The AIC was computed from the SS as n·ln(SS/n) + 2p, where n is the number of observations and p = 4 for the exponential and 5 for the Gompertz model ([2](#ref-2)), and the share of studies in which it was lower for the Gompertz model was recorded. Each combination of Gompertz rate and duration was simulated 2,000 times (seed 20261122) with R 4.5.3 ([3](#ref-3)). No study gave a non-finite prediction, an EC50 above 10⁴ or a kmax above 10³; convergence codes of the optimiser were not recorded. I report medians and the 5th to 95th percentiles of the estimates across the 2,000 studies.

## Results {#article-results}

![Estimated maximal kill rate by study duration and fitted model for three Gompertz rates](shared/tgi-growth-model-misspecification/figures/figure-1-kmax.png)

**Figure 1.** Estimated maximal kill rate (median and 5th to 95th percentile of 2,000 studies per point) by study duration, for the exponential and the Gompertz model. Panels give the Gompertz rate of the vehicle tumours; the grey line is the true value, 0.20 per day.

### The half-maximal concentration was recovered by both models

The median estimate of EC50 was between 2.99 and 3.01 for both models in all 18 combinations (Table 2), with the same spread: for the Gompertz rate of 0.05 at 14 days, the 5th to 95th percentile was 2.47 to 3.71 for the exponential and 2.47 to 3.74 for the Gompertz model. The spread narrowed with the duration (2.74 to 3.28 at 28 days). In this design the log difference between a treated arm and the vehicle arm is exactly −k(C)·g(t), with g(t) = (1 − e^(−βt))/β, a function of time that is the same for every treated arm, because the kill is added to the log growth rate, the concentration is constant and there is no delay. The exponential model fits −k(C)·t instead, so its misfit scales the kill rate of every arm in the same way and leaves the shape across concentrations, and thus EC50, unchanged. This separability is specific to the design, and a delay in the effect or an effect that depends on the number of proliferating cells would break it.

**Table 2.** Median (5th to 95th percentile) of the estimated maximal kill rate (true 0.20 per day) and half-maximal concentration (true 3), 2,000 studies per cell.

| Gompertz rate (per day) | Duration (days) | kmax, exponential | kmax, Gompertz | EC50, exponential | EC50, Gompertz |
| --- | --- | --- | --- | --- | --- |
| 0.02 | 14 | 0.179 (0.169–0.188) | 0.200 (0.175–0.233) | 3.005 (2.507–3.680) | 3.004 (2.506–3.684) |
| 0.02 | 21 | 0.170 (0.164–0.175) | 0.200 (0.181–0.220) | 2.996 (2.647–3.387) | 2.995 (2.646–3.390) |
| 0.02 | 28 | 0.162 (0.158–0.165) | 0.200 (0.186–0.215) | 3.001 (2.752–3.277) | 3.000 (2.749–3.282) |
| 0.05 | 14 | 0.153 (0.145–0.160) | 0.201 (0.176–0.229) | 3.001 (2.471–3.714) | 3.002 (2.465–3.744) |
| 0.05 | 21 | 0.135 (0.131–0.140) | 0.200 (0.182–0.218) | 3.000 (2.658–3.407) | 3.004 (2.647–3.423) |
| 0.05 | 28 | 0.121 (0.119–0.124) | 0.200 (0.187–0.214) | 2.993 (2.738–3.278) | 2.992 (2.728–3.296) |
| 0.10 | 14 | 0.120 (0.113–0.127) | 0.200 (0.178–0.223) | 2.994 (2.396–3.806) | 2.995 (2.386–3.802) |
| 0.10 | 21 | 0.098 (0.094–0.102) | 0.200 (0.186–0.216) | 3.009 (2.604–3.518) | 3.009 (2.597–3.529) |
| 0.10 | 28 | 0.082 (0.080–0.085) | 0.200 (0.188–0.212) | 2.998 (2.686–3.380) | 3.004 (2.680–3.375) |

### The maximal kill rate was underestimated, more so for longer studies

The exponential model underestimated kmax in every cell (Table 2, Figure 1). With a Gompertz rate of 0.05 the median estimate was 0.153, 0.135 and 0.121 per day at 14, 21 and 28 days, against the true 0.20, and with a rate of 0.10 it fell to 0.082 per day at 28 days. The 5th to 95th percentile of the exponential estimate was narrow and did not include the true value in any cell (for example 0.119 to 0.124 at 28 days and a rate of 0.05), while the Gompertz estimate was centred on 0.20 with a wider interval (0.187 to 0.214). The bias is smallest for the nearly exponential vehicle growth (rate 0.02: 0.179 at 14 days) and increases with the Gompertz rate and the study length.

The pattern follows from the design. The log difference between a treated and the vehicle arm, −k(C)·g(t), saturates in time, whereas the exponential model fits a straight line through the origin, −k′(C)·t. Least squares over the observation days then gives approximately kmax′ = kmax·Σ g(t)·t / Σ t², where the sums run over the days of the study. This expression gave 0.152, 0.135 and 0.121 per day for a rate of 0.05 at 14, 21 and 28 days, and matched all nine simulated medians within 0.001 (`check_kmax_approximation.R`). It is an approximation because x₀ and kg are also fitted and the vehicle arm contributes to them.

### Predictions for an intermediate concentration were too optimistic

I asked what the models predict for a concentration of 5, which is inside the tested range but is not one of the four treated arms, at day 28 and at the last observation day (Table 3, Figure 2). For a 14- or 21-day study, day 28 is an extrapolation in time. The exponential model predicted too small a treated-to-vehicle volume ratio, that is, too much inhibition. With a Gompertz rate of 0.05 the median predicted ratio was 0.459 of the true ratio (true 0.152; log ratio −2.66 against −1.88) after 14 days, 0.619 after 21 days and 0.784 after 28 days. With rates of 0.02 and 0.10 the values after 14 days were 0.641 and 0.400. The Gompertz model's median prediction was within 0.007 of the true ratio in every cell, with a wider spread after 14 days (0.735 to 1.302 of the true ratio for a rate of 0.05). The prediction at the last observation day, which does not extrapolate in time and so reflects the lack of fit to the curvature, was also too optimistic, and increasingly so with the duration (0.930, 0.863 and 0.784 of the true ratio at 14, 21 and 28 days for a rate of 0.05).

![Predicted divided by true volume ratio for concentration 5 by study duration, exponential model](shared/tgi-growth-model-misspecification/figures/figure-2-prediction.png)

**Figure 2.** Median of the predicted divided by the true treated-to-vehicle volume ratio for concentration 5 from the exponential model, at the last observation day and at day 28, by study duration. A value below 1 means that the predicted inhibition was larger than the true inhibition. Panels give the Gompertz rate.

**Table 3.** Exponential model: predicted divided by true treated-to-vehicle volume ratio for concentration 5 (median, with the 5th to 95th percentile at day 28), and the share of studies in which AIC preferred the Gompertz model.

| Gompertz rate (per day) | Duration (days) | At the last observation day | At day 28 | At day 28, 5th–95th percentile | Share of studies in which AIC preferred Gompertz |
| --- | --- | --- | --- | --- | --- |
| 0.02 | 14 | 0.965 | 0.641 | 0.508–0.812 | 0.460 |
| 0.02 | 21 | 0.921 | 0.750 | 0.654–0.866 | 0.960 |
| 0.02 | 28 | 0.865 | 0.865 | 0.785–0.951 | 1.000 |
| 0.05 | 14 | 0.930 | 0.459 | 0.375–0.570 | 0.988 |
| 0.05 | 21 | 0.863 | 0.619 | 0.549–0.692 | 1.000 |
| 0.05 | 28 | 0.784 | 0.784 | 0.729–0.846 | 1.000 |
| 0.10 | 14 | 0.901 | 0.400 | 0.333–0.479 | 1.000 |
| 0.10 | 21 | 0.833 | 0.587 | 0.532–0.651 | 1.000 |
| 0.10 | 28 | 0.769 | 0.769 | 0.720–0.821 | 1.000 |

### A model comparison revealed the misspecification in most settings

AIC preferred the Gompertz model in 98.8% to 100% of the studies in 7 of the 9 cells (Table 3). The two exceptions were in the nearly exponential vehicle growth (rate 0.02): 0.960 at 21 days and 0.460 at 14 days. In the 14-day cell the exponential model's bias in kmax was smallest (0.179 against 0.20) and so was its error at the last observation day (0.965 of the true ratio), but the extrapolation to day 28 was still 0.641 of the true ratio. With 8 animals per arm and a log measurement error of 0.15, the data therefore carried enough information to prefer the correct growth model in most cells before the exponential model's estimates were used. I did not evaluate how often AIC prefers the Gompertz model when the vehicle tumours are exactly exponential.

## Discussion {#article-discussion}

The potency parameter was not affected in this design. Because the log difference between treated and vehicle arms is k(C) times a function of time that is common to all treated arms, the misfit of the exponential model acts on the kill-rate scale and not on the shape across concentrations, and both models estimated EC50 at 3. The efficacy scale was affected. The exponential model has one growth rate for every arm and no saturation, so the saturation of the log difference is absorbed in the maximal kill rate, and the estimate came out lower than the true value in all nine cells, by an amount that the closed-form approximation reproduced. The bias grows with the Gompertz rate and the duration because g(t) departs further from a straight line. This saturation comes from the return of the log volume toward its plateau, a property of Gompertz growth, and would not arise in the linear growth phase of the model of Simeoni et al. ([1](#ref-1)).

The projected volume ratio was affected in the opposite direction. A lower kmax does not mean a more cautious projection: the exponential model lets the treated-to-vehicle ratio keep falling as exp(−k′ t), whereas the true log ratio flattens toward −k/β as both vehicle and treated tumours approach their plateaus (−2.5 for concentration 5 at a Gompertz rate of 0.05, against −1.88 at day 28). In this design the exponential model therefore predicted too much inhibition for a concentration that was not one of the treated arms, and, for a 14-day study, by a factor of 0.46 on the volume ratio at day 28 (Gompertz rate 0.05). The prediction at the last observation day also overstated the inhibition, so the misfit is not only a matter of extrapolating in time. The sign and size of the bias depend on the drug-effect mechanism and on the concentration profile: with a delayed effect or a kill proportional to the growth contribution, they could differ, and I did not simulate those cases. A use that depends on the absolute volume ratio, such as choosing a concentration that reaches a target ratio, could be biased in the same direction as the predictions here.

The model comparison caught the misspecification in most settings. That reflects the sample size (8 animals per arm, up to 360 observations) and the amount of vehicle curvature I chose, and the 0.46 share at 14 days with a Gompertz rate of 0.02 shows that it fails when the tumours are close to exponential in the window. In that cell the bias in kmax was smallest, but the extrapolation to day 28 was still 0.64 of the true ratio. The AIC counted every observation as independent although the simulated animals shared a random initial volume, so for real data, with additional between-animal variation, its detection rate could be lower than here. Fewer animals, higher measurement error or longer windows with less curvature would also change it.

### Limitations

The simulated drug effect was a kill rate that depends on a constant concentration, with no pharmacokinetics, no delay between exposure and cell death, and no dependence of the effect on the number of proliferating cells; the model of Simeoni et al. includes these ([1](#ref-1)), and the conclusions may not carry over to it. The invariance of EC50 and the sign and size of the prediction bias depend on that mechanism. The true model was Gompertz with a constant kill, and the Gompertz fit therefore had the true form (with a starting point close to the truth), so its unbiasedness shows that the estimator works when the form is right, not that Gompertz growth describes tumours. Exponential growth followed by linear growth, logistic growth and other vehicle curves were not simulated. The settings (kmax 0.20, EC50 3, the arms 1 to 30, 8 animals, error SD 0.15, three Gompertz rates) are single values. The vehicle volume at the plateau for a Gompertz rate of 0.02 (116,509 mm³) is not realistic for a mouse tumour and serves only to make the growth nearly exponential in the window, and at a rate of 0.10 the vehicle tumours are close to their plateau by day 28. The measurement error was normal with a constant SD on the log scale; volume-dependent error, outliers and early removal of animals were not simulated. Between-animal variation was limited to the initial volume, so variation in individual growth rates was not simulated, and the fits pooled all observations and ignored the correlation of repeated measurements. I did not evaluate the coverage of any interval, the false-positive rate of AIC when the vehicle growth is exactly exponential, or predictions at concentrations other than 5. The account of the reference is from its abstract only.

## Conclusion {#article-conclusion}

When the vehicle tumours grew in a Gompertz way and the model assumed exponential growth, the half-maximal concentration was recovered (median 2.99 to 3.01 against 3). The maximal kill rate was underestimated in all nine cells (for example 0.121 against 0.20 per day after 28 days at a Gompertz rate of 0.05, and 0.082 at a rate of 0.10), as a closed-form approximation based on the saturating treated-to-vehicle log difference also showed, and the treated-to-vehicle volume ratio for a concentration inside the tested range was predicted too small in this design, by a factor of 0.46 after 14 days and 0.78 after 28 days for the day-28 projection at a rate of 0.05. AIC favoured the correct model in about 96% or more of the studies in 8 of 9 cells, and in 46.0% of the studies for the nearly exponential vehicle at 14 days. These results hold for a constant-concentration kill-rate effect added to the log growth rate, one set of assumed parameters and 8 animals per arm.

## Data and code availability {#reproduce}

No animal data were used. The companion contains the simulation (`simulate.R`), the check of the closed-form approximation (`check_kmax_approximation.R`), the figure script (`figures.R`), the aggregate results (`results/summary.csv`) and the session information. The seed is 20261122 (`Rscript simulate.R 2000`, about 11 minutes on a desktop computer). Base R and ggplot2 (4.0.4) are required; the numbers in the tables can be checked against `results/summary.csv`.

[Download the companion: code and aggregate results](shared/tgi-growth-model-misspecification/tgi-growth-model-misspecification-companion.zip)

## References {#article-references}

1. <span id="ref-1"></span>Simeoni M, Magni P, Cammia C, De Nicolao G, Croci V, Pesenti E, et al. Predictive pharmacokinetic-pharmacodynamic modeling of tumor growth kinetics in xenograft models after administration of anticancer agents. Cancer Res. 2004;64(3):1094–1101. [doi:10.1158/0008-5472.CAN-03-2524](https://doi.org/10.1158/0008-5472.CAN-03-2524)
2. <span id="ref-2"></span>Akaike H. A new look at the statistical model identification. IEEE Trans Automat Contr. 1974;19(6):716–723. [doi:10.1109/TAC.1974.1100705](https://doi.org/10.1109/TAC.1974.1100705)
3. <span id="ref-3"></span>R Core Team. R: A language and environment for statistical computing [Software]. 2026. Version 4.5.3. [R Project](https://www.r-project.org/)
