## Abstract {#article-abstract}

A population pharmacokinetic fit to a real dataset is usually done once, with all samples. I asked how far the estimates move when the same subjects are sampled sparsely. The data were the Theoph dataset of R (12 subjects, oral theophylline, 10 post-dose samples per subject). A one-compartment oral model with random effects on clearance (CL), volume of distribution (V) and absorption rate constant (ka) was fitted with nlme, a package of R for nonlinear mixed-effects models. This dense fit (CL 0.0400 L/h/kg, V 0.451 L/kg, ka 1.27 per hour) is the reference and not a true value. Each subject was thinned to 2, 3, 4 or 6 samples drawn from four time windows and refitted 500 times per scheme (seed 20261126). nlme returned a fit in 85.4% of the 2-sample resamples, 96.8% of the 3-sample resamples and at least 99.6% of the 4- and 6-sample resamples, but 70% to 84% of the returned fits carried a convergence warning. Among fits in the reference mode (ka above the elimination rate constant ke), the median typical CL and V were within 4.1% of the reference at every sample number; typical ka was the least stable (5th to 95th percentile −48.0% to 81.9% with 2 samples, −14.7% to 13.4% with 6). The standard deviation (SD) of the random effect on V (reference 0.116) was estimated at less than 1% of the reference in 63.0% to 81.1% of fits. Two disjoint subsets of the same size agreed within 20% for CL in 85.3% to 100% of pairs and for ka in 29.5% to 58.1%. A second parameter set with ka and ke exchanged reproduced the dense data (approximate log-likelihood difference 0.28); adding a start that reaches it moved 15.8% to 64.4% of the fits to that mode, against at most 3.0% from one start. The thinned samples are subsets of the reference data, and 12 subjects are few.

## Introduction {#article-introduction}

A companion simulation study examines what nlme recovers from sparse sampling when the truth is known ([1](#ref-1)). It cannot say how a real dataset behaves, because real data do not follow the model exactly. The Theoph dataset is a convenient real case. It is distributed with R; the documentation reports a study of theophylline in 12 subjects by Upton, with serum concentrations at 11 time points over 25 hours after an oral dose, and lists the dataset among those analysed in a standard text on mixed-effects models ([2](#ref-2), [3](#ref-3)). I use it as a test bed for one question.

**Question of interest:** how far do the nlme estimates of a one-compartment oral model move from the estimates obtained with all samples when each subject contributes only 2, 3, 4 or 6 of them? **Context of use:** judging whether a sparse sampling scheme in an early study would have given the same typical values, between-subject variability and residual error as a dense scheme in this dataset. A typical value was taken as the same when it lay within 20% of the reference; the 20% band is a descriptive choice made here, not a regulatory limit. The result is not a clinical dose recommendation, and theophylline is not the drug of a particular development program.

## Methods {#article-methods}

### Data and dense reference

The Theoph dataset has 132 rows: 12 subjects, body weight (kg), dose (mg/kg), time (h) and serum concentration (mg/L), with 11 samples per subject ([2](#ref-2)). The sample at time 0 was dropped because its log cannot be taken (the concentration is zero in 9 of 12 subjects), leaving 10 samples per subject (120 observations; 0.25 to 24.7 h; 0.85 to 11.4 mg/L). The model was a one-compartment model with first-order absorption, C(t) = Dose·ka / (V·(ka − ke)) · (e^(−ke·t) − e^(−ka·t)) with ke = CL / V, where the dose is in mg/kg so that CL is in L/h/kg and V in L/kg, fitted to the log concentration with a normal residual error by nlme, which uses the Lindstrom–Bates approach ([4](#ref-4)); I used nlme 3.1-168 ([5](#ref-5)) in R 4.5.3 ([6](#ref-6)). Independent random effects were on log CL, log V and log ka. The reference was the fit to all 120 observations from the start CL = 0.04, V = 0.5 and ka = 0.5 (Table 1). It is an estimate from 12 subjects and not the truth. Approximate 95% intervals (Wald-type, from the intervals function of nlme) for its variance parameters were computed, and the reference was also refitted without the random effect on V.

### Thinning

The 10 post-dose samples of each subject fall into four windows defined on the actual sampling times: window 1, up to 1.2 h (3 samples per subject, about 0.25, 0.5 and 1 h); window 2, above 1.2 and up to 4 h (2 samples, about 2 and 3.5 h); window 3, above 4 and up to 8 h (2 samples, about 5 and 7 h); and window 4, above 8 h (3 samples, about 9, 12 and 24 h). Every subject has 3, 2, 2 and 3 samples in the four windows. A subject with 2, 3 or 4 samples had a random choice of that many different windows and one random sample from each; with 6 samples, one random sample from each window and a second, different sample from each of windows 1 and 2. Every resample used the same 12 subjects, and each scheme was run 500 times (seed 20261126; each resample used its own seed). The thinned data have 24, 36, 48 and 72 observations against 120. This window scheme is structured; it does not represent the variety of real sparse designs.

### Fits and summaries

Each resample was fitted from the reference start. In a second analysis it was also fitted from a second start (CL 0.3, V 0.2 and ka 1), the start from which the dense data reach a second fit (Table 1), and the fit with the higher log-likelihood returned by nlme was kept. nlme was run so that it returns its last fit when the iteration limit is reached, as in the companion study ([1](#ref-1)). A fit was called returned if there was no error and clean if, in addition, there was no warning other than the structural warning that a subject has fewer observations than random effects, as in the companion study. A fit with ka smaller than ke was counted as being in the other mode (below). For the fits in the reference mode, the deviation from the reference was (estimate / reference) − 1, summarized as the median and the 5th to 95th percentile over fits and as the share within 20% of the reference. I call it a deviation and not a bias, because the reference is itself an estimate. For the SDs I also computed the share estimated at less than 1% of the reference, which I call a boundary estimate, and the share with the residual SD below 1% of the reference, which I call a degenerate fit. The Monte Carlo standard error of a share is at most 0.022 for independent resamples; the resamples are not independent, so this is a lower bound.

### Non-overlapping comparison

For sizes 2, 3, 4 and 5 (two subsets of 5 exhaust the 10 samples, so 6 is not possible), two disjoint random subsets of that size were drawn from each subject's 10 samples, without regard to the windows, and each was fitted from the reference start; 200 pairs per size (seed 20261127). Two fits agreed if the absolute log ratio of their estimates was at most log 1.2, and a fit was within 20% of the reference if the absolute deviation was at most 0.2; the shares are of the pairs in which both fits were returned and had ka greater than ke (156, 194, 196 and 198 of 200 pairs).

### Identifiability

For ka ≠ ke, exchanging ka and ke and multiplying V by ke/ka gives the same individual concentration curve, because the expression Dose·ka / (V·(ka − ke)) · (e^(−ke·t) − e^(−ka·t)) is unchanged by that exchange, and CL = V·ke is unchanged. The model therefore has two parameter sets for the same individual curve, one with ka greater than ke and one with ka smaller than ke (the flip-flop mode). The exchange does not preserve independent random effects on log CL, log V and log ka, so the likelihood of the two sets is not identical, and a constraint or outside information has to choose between them. Whether a second set is pharmacologically plausible is a separate question that I do not address.

## Results {#article-results}

### The dense data also reach a second mode in which ka and ke are exchanged

The reference fit had ka 1.27 per hour and ke 0.0888 per hour (Table 1). Starting the same dense data from CL 0.3, V 0.2 and ka 1 led to a fit with ka 0.0895 per hour and ke 1.27 per hour, a volume of 0.032 L/kg, which is the volume of the reference times ke/ka (0.451 × 0.0888/1.265 = 0.032), and the same clearance (0.0405 against 0.0400 L/h/kg). The second mode therefore exists as a fit of the dense data, which rests on the symmetry above and on the convergence of the second start, and not on the closeness of the likelihood. The variance parameters differ because of the independent random-effect structure (the SD on V was 0.672 and that on ka 0.072 in the second fit). Its log-likelihood, which nlme computes by the linearization method and is only an approximation to the marginal likelihood, was 2.00 against 2.29; I read the difference of 0.28 as an approximate, structure-dependent value and not as a measure of how well the two modes are separated. I use the first mode, ka greater than ke, as the reference because it is the usual reading for oral theophylline, an assumption that these data alone do not decide.

**Table 1.** Fits of the dense data (12 subjects, 120 observations) from two starting points.

| Fit | CL (L/h/kg) | V (L/kg) | ka (1/h) | ke (1/h) | SD of random effect on CL | on V | on ka | Residual SD | Log-likelihood |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reference (start CL 0.04, V 0.5, ka 0.5) | 0.0400 | 0.451 | 1.265 | 0.0888 | 0.247 | 0.116 | 0.660 | 0.172 | 2.29 |
| Start CL 0.3, V 0.2, ka 1 | 0.0405 | 0.032 | 0.0895 | 1.266 | 0.208 | 0.672 | 0.072 | 0.178 | 2.00 |

CL, clearance; V, volume of distribution; ka, absorption rate constant; ke, elimination rate constant; SD, standard deviation.

The Wald-type approximate 95% intervals of the reference SDs were 0.156 to 0.393 for CL, 0.059 to 0.229 for V, 0.402 to 1.085 for ka and 0.147 to 0.200 for the residual error. The refit without the random effect on V had a log-likelihood of −0.99 against 2.29 (a difference of 3.28), but it stopped at the iteration limit without convergence, so I do not interpret the difference.

### Returned fits and convergence warnings

From the reference start, nlme returned a fit in 85.4% of the 2-sample resamples, 96.8% of the 3-sample and 99.6% of the 4- and 6-sample resamples (Table 2). Fits without a convergence warning were 25.8%, 21.8%, 15.6% and 29.4% of all resamples; among the returned fits, 69.8%, 77.5%, 84.3% and 70.5% carried a convergence warning (Table 3). The structural warning appeared in all fits with 2 samples. I asked whether boundary estimates account for the warnings. At least one SD was below 1% of the reference in 96.0%, 81.6%, 82.7% and 89.8% of the returned fits. Among the fits with a convergence warning and the clean fits it was 96.3% and 95.3% with 2 samples (Fisher's exact test p = 0.60), 80.8% and 84.4% with 3 (p = 0.48), 85.2% and 69.2% with 4 (p = 0.0016) and 87.2% and 95.9% with 6 (p = 0.0031), so the direction was not consistent: boundary estimates were more frequent among the warned fits with 4 samples (for the SD on V alone, 83.6% against 50.0%) and less frequent with 6. Because boundary estimates occur in most fits, they neither explain nor exclude the warnings. A degenerate residual SD occurred in 28.8% of the 2-sample fits and in at most 0.2% of the others.

**Table 2.** Share (%) of resamples in which nlme returned a fit, returned a fit without a convergence warning (clean; of all 500 resamples), and share (%) of returned fits with ka smaller than ke, by scheme (500 resamples each), and the number of fits in the reference mode.

| Fit | Returned | Clean | ka < ke among returned | Fits in the reference mode |
| --- | --- | --- | --- | --- |
| 2 samples, one start | 85.4 | 25.8 | 3.0 | 414 |
| 3 samples, one start | 96.8 | 21.8 | 0.2 | 483 |
| 4 samples, one start | 99.6 | 15.6 | 0.0 | 498 |
| 6 samples, one start | 99.6 | 29.4 | 0.0 | 498 |
| 2 samples, better of two starts | 99.4 | 30.4 | 29.4 | 351 |
| 3 samples, better of two starts | 100.0 | 23.8 | 15.8 | 421 |
| 4 samples, better of two starts | 100.0 | 26.0 | 18.2 | 409 |
| 6 samples, better of two starts | 100.0 | 66.0 | 64.4 | 178 |

CL, clearance; ka, absorption rate constant; ke, elimination rate constant.

**Table 3.** Warnings and boundary estimates among all returned fits from the reference start (share, %); the shares in Table 6 refer to the fits in the reference mode only.

| Share (%) of returned fits | 2 samples | 3 samples | 4 samples | 6 samples |
| --- | --- | --- | --- | --- |
| Structural warning (fewer observations than random effects) | 100.0 | 0.0 | 0.0 | 0.0 |
| Convergence warning (any warning other than the structural one) | 69.8 | 77.5 | 84.3 | 70.5 |
| SD of random effect on V below 1% of the reference | 63.0 | 71.5 | 78.3 | 81.1 |
| SD of random effect on CL below 1% of the reference | 43.8 | 29.5 | 8.2 | 15.7 |
| SD of random effect on ka below 1% of the reference | 14.5 | 3.3 | 0.4 | 0.2 |
| Residual SD below 1% of the reference | 28.8 | 0.2 | 0.0 | 0.0 |
| Any of the four SDs below 1% of the reference | 96.0 | 81.6 | 82.7 | 89.8 |
| Any SD below 1%, among clean fits | 95.3 | 84.4 | 69.2 | 95.9 |
| Any SD below 1%, among fits with a convergence warning | 96.3 | 80.8 | 85.2 | 87.2 |

SD, standard deviation; CL, clearance; V, volume of distribution; ka, absorption rate constant.

### Reaching the second mode depended on the starting values

From the reference start, 3.0% of the returned 2-sample fits and 0.2% of the 3-sample fits had ka smaller than ke, and none of the 4- and 6-sample fits. When the second start was added and the fit with the higher log-likelihood kept, the share with ka smaller than ke was 29.4%, 15.8%, 18.2% and 64.4% (Table 4, Figure 1). Excluding the fits with a degenerate residual SD changed this to 32.5%, 15.8%, 18.2% and 64.4%, so degeneracy of the residual SD does not explain it. In those fits the median CL was 1.9% to 3.1% above the reference, and the median V and ka were 91.9% to 93.9% below it, as the exchange predicts. Where the better-of-two fit was in the other mode, its log-likelihood exceeded that of the single-start fit by a median of 2.3 (2 samples) to 5.1 (4 samples) units. With 6 samples, the median log-likelihood of the single-start fit was −3.8 and that of the chosen fit 0.7 in the 322 resamples in which the chosen fit had ka smaller than ke. I did not establish why the share rises to 64.4% with 6 samples; because nlme's log-likelihood is a linearized approximation and the two modes place the between-subject variability on different parameters, I do not read it as a statement about which mode is correct, and the choice by log-likelihood is partly a choice of random-effect structure.

**Table 4.** Share (%) of fits with ka smaller than ke under different choices of fit and exclusions.

| Share (%) of fits with ka < ke | 2 samples | 3 samples | 4 samples | 6 samples |
| --- | --- | --- | --- | --- |
| One start, all returned fits | 3.0 | 0.2 | 0.0 | 0.0 |
| Better of two starts, all returned fits | 29.4 | 15.8 | 18.2 | 64.4 |
| Better of two starts, excluding fits with residual SD below 1% of the reference | 32.5 (n = 397) | 15.8 (n = 500) | 18.2 (n = 500) | 64.4 (n = 500) |
| Better of two starts, excluding fits with any SD below 1% of the reference | 0.0 (n = 16) | 2.5 (n = 81) | 10.7 (n = 75) | 94.1 (n = 17) |

ka, absorption rate constant; ke, elimination rate constant; SD, standard deviation.

![Bar chart of the share of returned fits with ka smaller than ke, from one start and from the better of two starts, by samples per subject](shared/theoph-sparse-thinning-real-data/figures/figure-1-flip-flop.png)

**Figure 1.** Share of returned fits in which ka (absorption rate constant) was smaller than ke (elimination rate constant), from the reference start alone and with the better of two starts, by samples per subject (500 resamples per scheme).

### Typical CL and V stayed close to the reference and ka did not

Among fits in the reference mode, the median deviation of typical CL was +4.1%, +2.2%, −0.1% and +2.3%, and that of V was −1.5%, −0.2%, +1.6% and −2.0% with 2, 3, 4 and 6 samples (Table 5, Figure 2). The 5th to 95th percentile of CL was −10.2% to 18.9% with 2 samples and −1.6% to 7.6% with 6, and CL and V were within 20% of the reference in all of the 3-, 4- and 6-sample fits (93.7% and 94.4% with 2 samples). Typical ka was less stable: the median deviation was −7.9%, −1.0%, +11.8% and −3.6%, the 5th to 95th percentile was −48.0% to 81.9% with 2 samples, −32.8% to 49.0% with 3, −17.4% to 44.9% with 4 and −14.7% to 13.4% with 6, and the share within 20% of the reference was 46.6%, 56.7%, 64.1% and 99.0%. Restricted to the clean fits (78 to 147 per scheme), the medians were similar for CL and V (Table 5) and less favourable for ka at 2 and 3 samples (−13.2% and −10.9%).

![Line and band chart of the deviation of typical CL, V and ka from the dense reference by samples per subject](shared/theoph-sparse-thinning-real-data/figures/figure-2-typical-values.png)

**Figure 2.** Deviation of the typical values of CL (clearance), V (volume of distribution) and ka (absorption rate constant) from the dense reference (median and 5th to 95th percentile, as a percentage of the reference) by samples per subject, for fits in the reference mode (reference start, 500 resamples per scheme).

**Table 5.** Deviation (%) from the dense reference of the typical values: median (5th to 95th percentile); share (%) within 20% of the reference. Fits in the reference mode, all returned fits and clean fits only.

| Parameter and fits | 2 samples | 3 samples | 4 samples | 6 samples |
| --- | --- | --- | --- | --- |
| CL, all fits in the reference mode | 4.1 (−10.2 to 18.9); 93.7 | 2.2 (−4.8 to 10.8); 100.0 | −0.1 (−5.0 to 6.6); 100.0 | 2.3 (−1.6 to 7.6); 100.0 |
| CL, clean fits only | 4.3 (−8.7 to 13.4); 98.4 | 4.7 (−2.7 to 11.0); 100.0 | 0.8 (−4.4 to 7.8); 100.0 | 3.2 (−0.9 to 7.7); 100.0 |
| V, all fits in the reference mode | −1.5 (−17.7 to 15.0); 94.4 | −0.2 (−8.6 to 7.8); 100.0 | 1.6 (−4.5 to 6.6); 100.0 | −2.0 (−5.8 to 1.8); 100.0 |
| V, clean fits only | −2.1 (−16.7 to 10.5); 96.9 | −1.5 (−9.2 to 5.1); 100.0 | 1.2 (−6.3 to 5.8); 100.0 | −2.5 (−6.0 to 0.7); 100.0 |
| ka, all fits in the reference mode | −7.9 (−48.0 to 81.9); 46.6 | −1.0 (−32.8 to 49.0); 56.7 | 11.8 (−17.4 to 44.9); 64.1 | −3.6 (−14.7 to 13.4); 99.0 |
| ka, clean fits only | −13.2 (−50.6 to 52.2); 48.0 | −10.9 (−34.4 to 31.4); 63.3 | 7.1 (−22.0 to 41.3); 67.9 | −4.7 (−14.9 to 10.3); 99.3 |
| Number of fits (all / clean) | 414 / 127 | 483 / 109 | 498 / 78 | 498 / 147 |

CL, clearance; V, volume of distribution; ka, absorption rate constant.

### Variability parameters moved the most

The SD of the random effect on V (reference 0.116) was estimated at less than 1% of the reference in 62.8%, 71.6%, 78.3% and 81.1% of the reference-mode fits with 2, 3, 4 and 6 samples (63.0%, 71.5%, 78.3% and 81.1% of all returned fits, Table 3), and it was within 20% of the reference in at most 8.8% (Table 6). The SD of the random effect on CL (reference 0.247) was within 20% of the reference in 17.1%, 28.0%, 54.0% and 66.9% of the fits, and that on ka (reference 0.660) in 27.5%, 48.7%, 51.4% and 96.4%. The residual SD (reference 0.172) was 32.0%, 28.5% and 32.7% below the reference at the median with 2, 3 and 4 samples and 9.0% above it with 6. With 2 samples, 28.8% of the returned fits had a degenerate residual SD; among the same fits as in Table 6 without the degenerate ones, the median deviation of the residual SD was −7.4%, so the shortfall at 2 samples is largely the degenerate fits, while with 3 and 4 samples (almost no degenerate fits) it is a shrinkage of about 30%.

**Table 6.** Variability parameters relative to the dense reference: median deviation (%); share (%) estimated at less than 1% of the reference; share (%) within 20% of the reference. Fits in the reference mode, reference start.

| Parameter | 2 samples | 3 samples | 4 samples | 6 samples |
| --- | --- | --- | --- | --- |
| SD of the random effect on CL (reference 0.247) | −47.8; 44.4; 17.1 | 4.8; 29.6; 28.0 | 14.3; 8.2; 54.0 | −4.0; 15.7; 66.9 |
| SD of the random effect on V (reference 0.116) | −100.0; 62.8; 3.9 | −100.0; 71.6; 6.2 | −100.0; 78.3; 8.8 | −100.0; 81.1; 7.4 |
| SD of the random effect on ka (reference 0.660) | −24.0; 14.3; 27.5 | −4.1; 3.3; 48.7 | 15.3; 0.4; 51.4 | 1.3; 0.2; 96.4 |
| Residual SD (reference 0.172) | −32.0; 27.3; 31.2 | −28.5; 0.0; 29.0 | −32.7; 0.0; 16.3 | 9.0; 0.0; 78.3 |

SD, standard deviation; CL, clearance; V, volume of distribution; ka, absorption rate constant.

### Non-overlapping subsets

Two disjoint subsets of the same size fitted separately agreed with each other within 20% for CL in 85.3%, 98.5%, 99.5% and 100.0% of the pairs with 2, 3, 4 and 5 samples, for V in 75.6%, 96.4%, 98.5% and 99.5%, and for ka in 29.5%, 39.2%, 51.0% and 58.1% (Table 7). Each half was within 20% of the reference in 47.4%, 62.1%, 74.5% and 87.9% of the ka fits. With 4 samples drawn without regard to the windows, 74.5% of the ka fits were within 20% of the reference, against 64.1% for the window-based subsets that overlap the reference; with 5 samples (half of the data) it was 87.9% against 99.0% for 6 samples (60% of the data), so part of the high agreement at 6 samples may come from the overlap, and I did not separate the two. Random sampling without windows and window-based sampling also differ in design, which limits the comparison.

**Table 7.** Agreement of two disjoint subsets: share (%) of pairs within 20% of each other and share (%) of fits within 20% of the reference. Both fits returned and in the reference mode (200 pairs per size).

| Parameter and quantity | 2 samples | 3 samples | 4 samples | 5 samples |
| --- | --- | --- | --- | --- |
| CL, the two halves within 20% of each other | 85.3 | 98.5 | 99.5 | 100.0 |
| CL, each half within 20% of the reference | 94.9 | 99.5 | 99.7 | 100.0 |
| V, the two halves within 20% of each other | 75.6 | 96.4 | 98.5 | 99.5 |
| V, each half within 20% of the reference | 94.2 | 99.5 | 100.0 | 100.0 |
| ka, the two halves within 20% of each other | 29.5 | 39.2 | 51.0 | 58.1 |
| ka, each half within 20% of the reference | 47.4 | 62.1 | 74.5 | 87.9 |
| Pairs used (both fits returned, ka > ke) | 156 | 194 | 196 | 198 |

CL, clearance; V, volume of distribution; ka, absorption rate constant.

## Discussion {#article-discussion}

With 12 real subjects, thinning to 2 to 6 samples per subject moved the typical CL and V by a few percent, and with 3 or more samples both stayed within 20% of the dense reference in all fits; typical ka and the variance parameters were much less certain. This is the pattern of the simulated study of the same model ([1](#ref-1)), in which typical ka was the most biased and the SD of the random effect on V the hardest to recover, but I do not compare the numbers: the reference here is a dense estimate from 12 subjects with its own error, the sampling windows differ, and the model fits the real data only approximately. By the 20% criterion of the question of interest, a sparse scheme with at least 3 samples per subject gave the same typical CL and V as the dense scheme in this dataset, whereas typical ka was the same in 56.7% to 64.1% of the fits with 3 and 4 samples. Typical CL is the parameter of this model that is also unaffected by the exchange of ka and ke.

Three points limit what the thinned fits show. First, thinned samples are subsets of the reference data, and 6 of 10 samples are 60% of the data, so the deviations must shrink as the subset approaches the full set; the share of typical ka within 20% rose from 64.1% with 4 samples to 99.0% with 6, but disjoint subsets reached 87.9% with 5, so the part of the shrinkage that comes from the overlap is not separated. Second, the residual SD and the random-effect SDs trade off when each subject has few observations: with 3 and 4 samples the residual SD fell by about 30% while the SD of the random effect on CL deviated by up to 14.3% and the SD on V was estimated at the boundary; I did not test this explanation. Third, the SD of the random effect on V was small in the reference (0.116, Wald-type approximate 95% interval 0.059 to 0.229) and was estimated at the boundary in most thinned fits. An estimate at the boundary does not mean that V does not vary, and the dense data neither establish nor exclude that V varies: the approximate interval excludes zero but is wide, and the refit without the random effect on V did not converge.

Boundary estimates occurred in most fits; they neither explain nor exclude the convergence warnings, whose nature remains unexamined.

The identifiability result matters more than the percentages. The two parameter sets for the same individual curve exchange ka and ke, the dense data reached both, and the approximate log-likelihood difference of 0.28 reflects both the approximation and the different random-effect structure. The mode that a fit reached depended on its start: from the reference start almost all fits stayed in the mode with ka greater than ke, while adding a second start moved 15.8% to 64.4% of the fits to the other mode, with V and ka about 92% to 94% lower and CL unchanged. A fit that reports typical CL is therefore unaffected by this exchange, and one that reports V or ka is not unless the mode is checked or constrained. For oral theophylline the reading with ka greater than ke is the usual one, but the data do not decide it by themselves.

### Limitations

The reference is a fit to 12 subjects and not the true population value, and thinning the same 12 subjects 500 times gives resamples that are not independent of each other or of the reference, so the percentiles describe the variation due to the sample choice within these subjects and not sampling variation across new studies; the tails are coarse with 12 subjects. The thinned data are subsets of the reference data (24 to 72 of 120 observations). The windows are structured (3, 2, 2 and 3 samples per subject, the same for every subject) and do not represent the variety of real sparse designs, and the non-overlapping comparison used random samples without windows. The pre-dose sample was dropped, and the zero concentrations at that time were not used. The error model was a normal error on the log concentration with independent random effects, and I did not assume or examine correlations between random effects; covariates (weight, dose) were not modelled. One estimation method (nlme, the Lindstrom–Bates approach) was used, and other methods (first-order conditional estimation, stochastic approximation expectation maximization) might behave differently. One drug was used. The summaries include fits with convergence warnings; I report all returned fits and the clean fits separately for the typical values, and the variability summaries are for all returned fits in the reference mode. A boundary estimate of an SD is not an absence of variability. The log-likelihood is nlme's linearized approximation and does not compare the two modes strictly; the choice of the better of two fits partly selects a random-effect structure. The Theoph documentation attributes the data to a study of Upton as cited in Boeckmann, Sheiner and Beal; I read the documentation and not that source, and the accounts of the other references are from their abstracts or the documentation only.

## Conclusion {#article-conclusion}

Thinning the 12 subjects of the Theoph dataset to 2 to 6 samples per subject kept the typical CL and V of a one-compartment oral nlme fit within 20% of the dense fit (CL 0.0400 L/h/kg, V 0.451 L/kg) in all fits with 3 or more samples, left typical ka unstable, and moved the SD of the random effect on V to the boundary in most fits. The model also has a second parameter set with ka and ke exchanged that the dense data also reach (approximate log-likelihood difference 0.28), and which fit a resample reached depended on its starting values, so V and ka cannot be read from a single fit without checking the mode. These results are limited to one dataset of 12 subjects, to thinned subsets of that dataset and to the nlme implementation.

## Data and code availability {#reproduce}

The data are the Theoph dataset distributed with R; no data were downloaded. The companion contains the resampling script (`simulate.R`), the non-overlapping comparison (`disjoint_halves.R`), the checks of the reference fit (`reference_checks.R`), the summaries from the raw results (`extra_from_raw.R`), the figure script (`figures.R`), the reference fits (`results/reference.csv`, `results/reference-checks.csv`), the result of every resample (`results/raw.csv`, `results/disjoint-raw.csv`), the summaries (`results/summary.csv`, `results/extra-from-raw.csv`, `results/flip-choice-diagnostics.csv`, `results/warned-vs-clean.csv`, `results/disjoint-summary.csv`) and the session information. The seeds are 20261126 (`Rscript simulate.R 500 8`, about 31 minutes on a desktop computer with 8 worker processes) and 20261127 (`Rscript disjoint_halves.R 200 8`, about 12 minutes). R, the nlme package (3.1-168) and, for the figures, ggplot2 (4.0.4) are required; the numbers in the tables can be checked against the files in `results/`.

[Download the companion: code and aggregate results](shared/theoph-sparse-thinning-real-data/theoph-sparse-thinning-real-data-companion.zip)

## References {#article-references}

1. <span id="ref-1"></span>Kumakura D. [What does nlme recover from sparse sampling in a population pharmacokinetic analysis? Simulated studies with 20 to 80 subjects and 2 to 6 samples per subject](https://daikikumakura.github.io/writing/poppk-sparse-nlme-recovery.html) [Internet]. 2026 Dec 29.
2. <span id="ref-2"></span>R Core Team. Pharmacokinetics of theophylline (Theoph) [Dataset documentation]. R datasets package; R-patched documentation [cited 2026 Nov 20]. Available from: [https://stat.ethz.ch/R-manual/R-patched/library/datasets/html/Theoph.html](https://stat.ethz.ch/R-manual/R-patched/library/datasets/html/Theoph.html)
3. <span id="ref-3"></span>Pinheiro JC, Bates DM. Mixed-effects models in S and S-PLUS. New York: Springer; 2000. [doi:10.1007/978-1-4419-0318-1](https://doi.org/10.1007/978-1-4419-0318-1)
4. <span id="ref-4"></span>Lindstrom MJ, Bates DM. Nonlinear mixed effects models for repeated measures data. Biometrics. 1990;46(3):673–687. [doi:10.2307/2532087](https://doi.org/10.2307/2532087)
5. <span id="ref-5"></span>Pinheiro J, Bates D, R Core Team. nlme: linear and nonlinear mixed effects models [Software]. 2025. Version 3.1-168. [CRAN](https://CRAN.R-project.org/package=nlme)
6. <span id="ref-6"></span>R Core Team. R: A language and environment for statistical computing [Software]. 2026. Version 4.5.3. [R Project](https://www.r-project.org/)
