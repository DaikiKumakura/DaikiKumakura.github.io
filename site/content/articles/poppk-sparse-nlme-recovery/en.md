## Abstract {#article-abstract}

Population pharmacokinetic analyses of sparse data estimate typical values, between-subject variability and residual error from a few samples per subject. I simulated a one-compartment oral model (typical clearance CL 5 L/h, volume of distribution V 50 L, absorption rate constant ka 1 per hour; between-subject standard deviations (SDs) 0.30, 0.20 and 0.50 on the log scale; residual SD 0.15 on the log concentration), with 20, 40 or 80 subjects and 2, 3, 4 or 6 samples per subject drawn from four time windows, and fitted it by the nlme package of R (the estimation method of Lindstrom and Bates) with random effects on CL, V and ka, or on CL and V only. Each of 24 cells was simulated 400 times (seed 20261123). nlme returned a fit without error in 96.3% to 99.8% of studies with 2 samples per subject and in at least 99.5% with 3 or more, but a fit without any convergence warning was obtained in only 42.2% to 46.3% of the full-model studies with 2 samples, 53.0% to 55.7% with 3, and 82.3% to 93.0% with 4 or 6. The median error of the typical values depended on the number of samples per subject and not on the number of subjects: with the full model at 40 subjects, typical CL was overestimated by 6.4% with 2 samples and 1.6% with 6, V underestimated by 11.3% and 2.0%, and ka by 29.4% and 6.9%. The SD of the random effect on V was estimated at zero in 41.0% of studies with 2 samples at 40 subjects (5.5% with 4), and that share fell to 23.0% when the optimiser started from the true values. Giving every subject an absorption-phase sample did not remove the bias. Omitting the random effect on ka, which the data-generating model contained, left the typical values no worse but raised the residual SD by 23.5% to 31.0% and the SD of the random effect on V by 18.8% to 29.0% at 40 subjects. These results hold for one set of assumed parameters, one sampling scheme and the nlme implementation.

## Introduction {#article-introduction}

Nonlinear mixed-effects pharmacokinetic models are fitted with approximations of the likelihood, one of which is the linearization of Lindstrom and Bates. Lindstrom and Bates proposed estimators for nonlinear mixed-effects models that combine least-squares estimation for nonlinear fixed-effects models with maximum-likelihood or restricted maximum-likelihood estimation for linear mixed-effects models ([1](#ref-1)). I read that reference through its abstract only. The nlme package of R is a widely available implementation ([2](#ref-2)).

When each subject contributes only two to four samples, individual parameters cannot be estimated one subject at a time, and the population method has to borrow strength across subjects. The question is how much a fixed number of subjects can compensate for few samples per subject. **For a one-compartment oral model analysed by nlme, how do convergence, the bias of typical values and the recovery of between-subject variability depend on the number of subjects (20 to 80) and on the number of samples per subject (2 to 6), and what happens when the random effect on the absorption rate constant is left out?** The answer is computed by simulation, so that every estimate can be compared with a known true value.

## Methods {#article-methods}

### Simulated studies

Each subject received a single oral dose of 100 mg. The concentration was C(t) = Dose·ka / (V·(ka − ke)) · (e^(−ke·t) − e^(−ka·t)), with ke = CL / V, where CL is clearance, V the volume of distribution, ka the absorption rate constant and ke the elimination rate constant. Individual parameters were the typical values (CL = 5 L/h, V = 50 L, ka = 1 per hour) multiplied by exp(η), where η is a random effect drawn from independent normal distributions with SD 0.30 for CL, 0.20 for V and 0.50 for ka (the between-subject SDs). The observed log concentration was the true log concentration plus a normal error of SD 0.15 (the residual SD). Each subject had 2, 3 or 4 samples, each taken at a random time within a different one of four windows (0.25–2 h, 2–6 h, 6–12 h and 12–24 h) chosen at random for that subject, or 6 samples, with one in each window and a second sample in each of the first two windows. Because the windows were chosen at random for the 2- to 4-sample schemes, half of the subjects with 2 samples and a quarter of those with 3 had no sample in the first window, which covers the absorption phase. This random-window scheme is the sampling design of this article; I did not simulate a design optimized in advance.

### Analysis

I fitted the log concentration by nlme with the model above on the log scale, with fixed effects on log CL, log V and log ka and independent random effects either on all three (full model) or on log CL and log V only (ka without a random effect), starting from CL = 3, V = 30 and ka = 0.5. The full model has the structure of the data-generating model; the reduced model omits a random effect that the data-generating model contained. nlme was run with the option that returns the fit after the iteration limit instead of stopping. A study was called returned if nlme gave a fit without an error, and clean if, in addition, it gave no warning other than one structural warning. The structural warning, that there are fewer observations than random effects in every subject, appears with 2 samples and 3 random effects; it was recorded separately and did not make a study unclean. The other warnings that I saw were that the iteration limit was reached, that step halving failed and that a precision matrix was singular, and any such warning made a study unclean. I summarize the relative error, (estimate / true value) − 1, as the median and the 5th to 95th percentile over returned studies, together with the share of studies in which a random-effect SD was estimated at less than 0.1% of its true value (called an estimate at zero; 1% and 10% were also computed) and the share in which the estimate was within 20% of the true value, both over returned studies. The typical values are the exponentiated fixed effects, which are medians of the individual parameters and not their means, and the relative errors are medians over studies. There were 3 subject numbers × 4 sample numbers × 2 models = 24 cells, each with 400 studies, in separate random datasets with R 4.5.3 ([3](#ref-3)) and nlme 3.1-168; each study used its own seed derived from seed 20261123, so the results do not depend on the number of cores. The Monte Carlo standard error of a share is at most 0.025.

Two checks were added at 40 subjects with the full model, each with 400 studies. In the first, every subject had the same sampling windows (windows 1 and 3 for 2 samples, windows 1, 2 and 4 for 3 samples), so that every subject had a sample in the absorption window. In the second, the starting values of the optimiser were the true values, or CL = 3, V = 30 and ka = 2.

## Results {#article-results}

### Fits returned often but converged cleanly less often

With 2 samples per subject, nlme returned a fit in 96.3% (20 subjects), 97.5% (40) and 99.8% (80) of the full-model studies, and in at least 99.5% with 3 or more samples (Table 1). The share of clean fits was much lower: 45.5%, 46.3% and 42.2% with 2 samples, 53.0% to 55.7% with 3, 82.3% to 84.5% with 4 and 92.2% to 93.0% with 6. The reduced model returned a fit in 97.0% (20 subjects) to 100% of studies with 2 samples and in all studies with 3 or more, and its clean share was 48.0% to 68.5% with 2 samples and 93.5% to 99.8% with 3 or more. In the full model with 40 subjects, the typical values from clean fits only were close to those from all returned fits (2 samples: CL 5.9%, V −10.6%, ka −29.3% against 6.4%, −11.3% and −29.4%), so the bias below does not come from fits that nlme flagged.

**Table 1.** Share of studies in which nlme returned a fit / returned a fit without a convergence warning (400 studies per cell).

| Model | Subjects | 2 samples | 3 samples | 4 samples | 6 samples |
| --- | --- | --- | --- | --- | --- |
| Random effect on ka | 20 | 0.963 / 0.455 | 0.995 / 0.530 | 1.000 / 0.825 | 1.000 / 0.930 |
| Random effect on ka | 40 | 0.975 / 0.463 | 1.000 / 0.557 | 1.000 / 0.845 | 1.000 / 0.922 |
| Random effect on ka | 80 | 0.998 / 0.422 | 0.998 / 0.545 | 1.000 / 0.823 | 1.000 / 0.922 |
| No random effect on ka | 20 | 0.970 / 0.480 | 1.000 / 0.935 | 1.000 / 0.980 | 1.000 / 0.983 |
| No random effect on ka | 40 | 1.000 / 0.610 | 1.000 / 0.983 | 1.000 / 0.990 | 1.000 / 0.990 |
| No random effect on ka | 80 | 0.998 / 0.685 | 1.000 / 0.963 | 1.000 / 0.993 | 1.000 / 0.998 |

### Typical values were biased, and more samples per subject reduced the bias but more subjects did not

For the full model, the median relative error of the typical values depended on the number of samples per subject and hardly on the number of subjects (Figure 1, Table 2). At 40 subjects, typical CL was overestimated by 6.4% with 2 samples and by 1.6% with 6; V was underestimated by 11.3% and 2.0%; and ka by 29.4% and 6.9%. At 20 and 80 subjects the medians with 2 samples were 6.4% and 6.2% for CL, −10.2% and −11.8% for V, and −26.8% and −30.6% for ka (see `results/summary.csv`). More subjects narrowed the 5th to 95th percentile (typical ka with 2 samples: −85.3% to 23.9% at 20 subjects, −62.6% to 3.8% at 40 and −54.9% to −7.5% at 80) but did not move the median toward zero; at 80 subjects the interval excluded zero.

![Relative error of typical CL, V and ka by number of samples per subject and number of subjects](shared/poppk-sparse-nlme-recovery/figures/figure-1-typical-values.png)

**Figure 1.** Relative error of the typical values (median, with the 5th to 95th percentile as a band) by samples per subject, for 20, 40 and 80 subjects (full model, 400 studies per point). CL, clearance; V, volume of distribution; ka, absorption rate constant.

**Table 2.** Median relative error (%) of the typical values, with the 5th to 95th percentile, at 40 subjects, full model.

| Parameter | 2 samples | 3 samples | 4 samples | 6 samples |
| --- | --- | --- | --- | --- |
| CL | 6.4 (−2.9 to 16.6) | 3.7 (−5.5 to 11.8) | 2.1 (−6.1 to 10.7) | 1.6 (−6.2 to 9.7) |
| V | −11.3 (−37.6 to 3.1) | −5.9 (−16.2 to 3.1) | −3.5 (−10.2 to 4.1) | −2.0 (−7.9 to 5.0) |
| ka | −29.4 (−62.6 to 3.8) | −20.1 (−38.4 to 1.9) | −11.7 (−25.0 to 3.9) | −6.9 (−18.8 to 6.1) |

### Neither an absorption-phase sample for every subject nor the starting values explained the bias

Because a random choice of windows leaves half of the subjects with 2 samples without an absorption-phase sample, I asked whether that explains the bias in ka (Table 3). When every subject had one sample in the absorption window and one in the elimination window (windows 1 and 3), the errors were larger and not smaller (ka −76.0%, V −69.0%, CL 14.9%), and nlme returned a fit in 92.2% of studies. With 3 samples in windows 1, 2 and 4, the errors were close to those of random windows (ka −19.5% against −20.1%, V −7.3% against −5.9%, CL 1.7% against 3.7%). Starting the optimiser from the true values did not remove the bias (typical ka −30.3% with 2 samples and −17.9% with 3), and starting from ka = 2 changed it little (−25.4% and −16.7%). The starting values did change the estimate of the random-effect SD on V: the share estimated at zero with 2 samples was 41.0% from the default start, 23.0% from the true values and 18.7% from ka = 2, and with 3 samples 19.2%, 3.0% and 2.0%.

**Table 3.** Design and starting-value checks at 40 subjects, full model (400 studies per row): share of returned and of clean fits, median relative error (%) of the typical values, and share (%) of studies with the SD of the random effect on V estimated at zero. Rows with different starting values or windows are separate random datasets.

| Design | Starting values | Returned | Clean | Typical CL | Typical V | Typical ka | Share of SD(V) at zero |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 samples, random windows | default | 0.975 | 0.463 | 6.4 | −11.3 | −29.4 | 41.0 |
| 2 samples, random windows | true values | 0.968 | 0.470 | 6.6 | −11.5 | −30.3 | 23.0 |
| 2 samples, random windows | ka = 2 | 0.975 | 0.495 | 5.8 | −9.4 | −25.4 | 18.7 |
| 2 samples, windows 1 and 3 for all | default | 0.922 | 0.442 | 14.9 | −69.0 | −76.0 | 47.7 |
| 3 samples, random windows | default | 1.000 | 0.557 | 3.7 | −5.9 | −20.1 | 19.2 |
| 3 samples, random windows | true values | 0.998 | 0.557 | 3.2 | −5.5 | −17.9 | 3.0 |
| 3 samples, random windows | ka = 2 | 0.998 | 0.565 | 3.9 | −5.0 | −16.7 | 2.0 |
| 3 samples, windows 1, 2 and 4 for all | default | 0.995 | 0.495 | 1.7 | −7.3 | −19.5 | 35.7 |

### Between-subject variability needed more samples than the typical values

The SD of the random effect on V was the hardest to recover (Figure 2, Table 4). At 40 subjects it was estimated at zero in 41.0% of studies with 2 samples, 19.2% with 3, 5.5% with 4 and 1.8% with 6 samples (49.0%, 20.8%, 5.8% and 1.8% with a threshold of 1% of the true value, and 50.0%, 21.5%, 5.8% and 1.8% with 10%), and the share of studies within 20% of the true SD was 21.5%, 47.8%, 65.8% and 72.2%. The median error of −83.0% with 2 samples reflects that large share of estimates at zero. The SD of the random effect on CL was estimated with a median error of −11.3% to −4.9% and within 20% of the true value in 65.6% to 88.5% of studies. The SD of the random effect on ka was estimated at zero in 5.1% of studies with 2 samples and within 20% in 45.1% to 80.5%. The residual SD was estimated with a median error of 9.6% with 2 samples and 0.3% with 6, at zero in 3.1% of studies with 2 samples, and within 20% in 45.9% and 99.8%. At 80 subjects with 6 samples, the shares within 20% of the true SD were 97.8% (CL), 89.2% (V) and 92.2% (ka).

![Share of studies in which the estimated random-effect SD was within 20% of the true value](shared/poppk-sparse-nlme-recovery/figures/figure-2-random-effects.png)

**Figure 2.** Share of studies in which the estimated SD of the random effect on CL, V or ka was within 20% of its true value, by samples per subject and number of subjects (full model, returned studies, 400 studies per point).

**Table 4.** Variability parameters at 40 subjects, full model: median relative error (%); share of studies estimated at zero (%); share within 20% of the true value (%).

| Parameter | 2 samples | 3 samples | 4 samples | 6 samples |
| --- | --- | --- | --- | --- |
| SD of the random effect on CL (true 0.30) | −11.3; 0.0; 65.6 | −8.6; 0.0; 79.2 | −6.8; 0.0; 85.2 | −4.9; 0.0; 88.5 |
| SD of the random effect on V (true 0.20) | −83.0; 41.0; 21.5 | −14.7; 19.2; 47.8 | −8.8; 5.5; 65.8 | −5.1; 1.8; 72.2 |
| SD of the random effect on ka (true 0.50) | −18.0; 5.1; 45.1 | −10.3; 0.5; 58.2 | −10.4; 0.0; 67.0 | −7.2; 0.0; 80.5 |
| Residual SD (true 0.15) | 9.6; 3.1; 45.9 | 6.6; 0.0; 77.8 | 2.8; 0.0; 90.8 | 0.3; 0.0; 99.8 |

### Omitting the random effect on ka moved variability into the residual and into V

In the reduced model, the typical values were no worse than those of the full model and their errors were smaller (at 40 subjects and 2 samples: CL 4.1%, V −3.8%, ka −14.3%, Table 5). The residual SD, however, was overestimated by 23.5% to 31.0% for all sample numbers, against 0.3% to 9.6% in the full model. The SD of the random effect on V was overestimated by 18.8% to 29.0%, against errors of −5.1% to −83.0% (underestimates) in the full model; the SD of the random effect on CL was little affected (−12.0% to −5.4%, against −11.3% to −4.9%). Restricted to clean fits, the residual SD was overestimated by 22.3% to 30.8% and the SD of the random effect on V by 18.8% to 31.4%. The variability that the reduced model could not attribute to ka appeared in the residual error and in V, which is consistent with the shift I expected; I did not test the mechanism.

**Table 5.** Median relative error (%) at 40 subjects: full model and the model without a random effect on ka (returned studies).

| Parameter | Model | 2 samples | 3 samples | 4 samples | 6 samples |
| --- | --- | --- | --- | --- | --- |
| Typical CL | Full | 6.4 | 3.7 | 2.1 | 1.6 |
| Typical CL | No random effect on ka | 4.1 | 2.1 | 0.9 | 0.6 |
| Typical V | Full | −11.3 | −5.9 | −3.5 | −2.0 |
| Typical V | No random effect on ka | −3.8 | −1.6 | 0.0 | 0.8 |
| Typical ka | Full | −29.4 | −20.1 | −11.7 | −6.9 |
| Typical ka | No random effect on ka | −14.3 | −10.9 | −6.0 | −4.6 |
| Residual SD | Full | 9.6 | 6.6 | 2.8 | 0.3 |
| Residual SD | No random effect on ka | 23.5 | 29.3 | 31.0 | 28.4 |
| SD of the random effect on CL | Full | −11.3 | −8.6 | −6.8 | −4.9 |
| SD of the random effect on CL | No random effect on ka | −12.0 | −7.0 | −9.0 | −5.4 |
| SD of the random effect on V | Full | −83.0 | −14.7 | −8.8 | −5.1 |
| SD of the random effect on V | No random effect on ka | 29.0 | 25.0 | 18.8 | 27.5 |

## Discussion {#article-discussion}

The typical values and the variability parameters responded to different design choices. The typical values had a bias that depended on the number of samples per subject and that did not shrink with more subjects: at 20, 40 and 80 subjects the median error was about the same (the typical ka was slightly worse at 80 subjects), and more subjects only narrowed the interval. This pattern is consistent with a bias that belongs to the estimator when the information per subject is small, and not with sampling error that more subjects would average out. Two explanations were not supported by these runs. The bias did not come from fits that nlme flagged, since clean fits gave nearly the same medians, and it was not due to the absence of an absorption-phase sample or to the starting values, since a fixed absorption sample for every subject did not help (with 2 samples it made the estimates worse, probably because every subject then had the same two time points and V and ka were weakly separated) and starting from the true values left the bias in place. I did not identify the cause. The linearization around the random effects, the flatness of the likelihood in V and ka for few samples, and the dependence of ka on the profile shape remain possible explanations, and I did not test them.

The estimated SD of the random effect on V was the weakest estimate. With 2 samples per subject, an estimate at zero was more common than a good estimate. The share depended on the starting values (41.0% against 23.0% from the true values), so part of the estimates at zero reflect where the optimiser ended and not only the information in the data. An SD estimated at zero should not be read as an absence of variability in the population, since the simulated SD was 0.20.

The convergence result changes how the first numbers should be read. A fit that nlme returns after reaching the iteration limit is not a converged fit, and with 2 samples only 42.2% to 46.3% of the full-model studies were clean, so the returned fits include many that the software itself flagged. The medians of the clean fits resembled those of all returned fits, but the clean fits are a selected subset (only 185 of 400 studies for the full model at 40 subjects with 2 samples).

When the random effect on ka was dropped, the typical values were not worse (their errors were smaller), but the residual SD and the SD of the random effect on V were overestimated by about 19% to 31%. A reader who sees only the typical values would not detect the misspecification, and a reader who compares the residual SD with an assay error would see an unexplained error that is partly the omitted variability. The reduced model also gave clean fits much more often (for example 98.3% against 55.7% with 3 samples at 40 subjects), which is a reason that analysts drop random effects when a fit does not converge; the simulated results show a cost of doing so when the omitted variability exists.

### Limitations

One set of parameters (typical values, SDs, residual SD, dose), one structural model (one compartment, first-order oral absorption, no lag time) and one sampling scheme (random windows) were used. In the random-window scheme the number of samples per subject changed together with the share of subjects who had an absorption-phase sample (50% with 2 samples, 75% with 3, 100% with 4 or 6), so the effect of the number of samples is not separated from that of window coverage, except through the fixed-window checks, which used different random datasets and, with 2 samples, a returned subset of 92.2%. The window scheme is not representative of every sparse design, and the 6-sample scheme is not rich sampling; a design optimized in advance was not tested. The residual error was a normal error on the log concentration, which is not a proportional-plus-additive error model. Random effects were independent in both the data and the analysis; correlations were not simulated, and the only misspecification examined was the omitted random effect on ka. I used nlme (the Lindstrom–Bates approach) and did not compare it with other estimation methods (first-order conditional estimation with interaction in NONMEM, stochastic approximation expectation maximization, or a Bayesian analysis), so the biases here apply to this implementation. The statement that the linearization is a possible source of the bias is a hypothesis that this article does not test. The starting values were fixed at three settings, and the convergence check was limited to nlme's own warnings; I did not examine standard errors or shrinkage. The bias is reported as the median relative error over studies and not as a mean error or a root mean square error, and the SDs estimated at zero distort the medians and the shares within 20%. The 0.1% threshold and the 20% band are descriptive cut-offs chosen here, and the Monte Carlo error of a median or percentile was not computed. The account of the reference is from its abstract only.

## Conclusion {#article-conclusion}

For a one-compartment oral model with random effects on CL, V and ka, nlme returned a fit in at least 96.3% of studies, but gave a fit without a convergence warning in 42.2% to 46.3% of the full-model studies with 2 samples per subject and 82.3% or more with 4 or 6. The bias of the typical values depended on the number of samples per subject and not on the number of subjects (typical ka −29.4% with 2 samples and −6.9% with 6 at 40 subjects), and neither an absorption sample for every subject nor starting values at the truth removed it. The SD of the random effect on V was estimated at zero in 41.0% of studies with 2 samples at 40 subjects, and that share depended on the starting values. Omitting the random effect on ka did not worsen the typical values but overestimated the residual SD by 23.5% to 31.0% and the SD of the random effect on V by 18.8% to 29.0%. The numbers hold for the assumed parameters, the random-window sampling scheme and the nlme implementation.

## Data and code availability {#reproduce}

No subject-level data were used. The companion contains the simulation (`simulate.R`), the figure script (`figures.R`), the aggregate results (`results/summary.csv`), the results of every simulated study (`results/raw.csv`) and the session information. The seed is 20261123 (`Rscript simulate.R 400`, about 46 minutes on a desktop computer with 11 worker processes). R, the nlme package (3.1-168) and, for the figures, ggplot2 (4.0.4) are required; the numbers in the tables can be checked against `results/summary.csv`.

[Download the companion: code and aggregate results](shared/poppk-sparse-nlme-recovery/poppk-sparse-nlme-recovery-companion.zip)

## References {#article-references}

1. <span id="ref-1"></span>Lindstrom MJ, Bates DM. Nonlinear mixed effects models for repeated measures data. Biometrics. 1990;46(3):673–687. [doi:10.2307/2532087](https://doi.org/10.2307/2532087)
2. <span id="ref-2"></span>Pinheiro J, Bates D, R Core Team. nlme: linear and nonlinear mixed effects models [Software]. 2025. Version 3.1-168. [CRAN](https://CRAN.R-project.org/package=nlme)
3. <span id="ref-3"></span>R Core Team. R: A language and environment for statistical computing [Software]. 2026. Version 4.5.3. [R Project](https://www.r-project.org/)
