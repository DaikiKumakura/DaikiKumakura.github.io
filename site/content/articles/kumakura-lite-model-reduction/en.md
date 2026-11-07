Reference date: the facts in this article are based on public information as of 7 November 2026.

日本語版: [Kumakura-Lite: 機能分業型の微生物増殖モデルを2状態へ縮約する条件と実測データでの予測力](https://daikikumakura.github.io/writing/kumakura-lite-model-reduction.html)

## Abstract

This article asks under which conditions the three-state functional-specialization model of microbial growth (cell density \(N\), substrate \(R\), metabolite \(M\); [1](#ref-1), [2](#ref-2)) reduces to two states, and what reduced or reformulated models offer when predicting culture medium concentrations that were not used for calibration. In batch culture, \(dR/dt\) and \(dM/dt\) are both proportional to \(N\); with the clock \(d\tau = N\,dt\), \((R, M)\) becomes a closed two-state system independent of \(N\), and \(N\) is recovered by a linear quadrature (derivation). When metabolite degradation is absent and the metabolite yields of the growth and non-growth functions are equal (Lite-S), \(M = M_0 + \nu(R_0 - R)\) holds exactly, and the difference from the three-state solution fell to the integrator tolerance (relative error of \(N\), \(3.9\times10^{-11}\)). For the quasi-steady-state approximation for fast metabolite relaxation (Lite-Q), the time-scale ratio \(\varepsilon\) does not depend on \(N\). With initial values placed on the quasi-steady curve, the slopes of the error against \(\varepsilon\) on log axes were 0.90 at zero order and 1.55 with the first-order correction; starting from \(M(0)=0\), an initial boundary layer remained and the first-order correction gave no improvement. The error of the weak-feedback approximation (Lite-W) increased with \(\zeta=\max M/(R+h)\), with a proportionality coefficient of 0.01 to 0.20 over the conditions examined. With the parameters of the numerical example in the doctoral thesis ([2](#ref-2)) and the start \(M(0)=0\), every reduction fell outside its validity conditions, with 44–66% error in \(N\). Lite-M, a resource-response law that is a product of saturating uptake and functional allocation, was compared with existing growth laws on dilution-series data of 16 strains. In interpolation to unused concentrations, the error of Lite-M was smaller than that of Monod (error ratio 0.70, 95% interval 0.60–0.81), Monod with density limit and the Hill type, whereas in extrapolation to higher or lower concentrations no advantage could be confirmed, and the reduced models Lite-S, Lite-Q and Lite-W did not exceed Monod.

## Introduction

The functional-specialization model of Kumakura et al. divides a microbial population into a growth function (MG) and a metabolite-detoxification function (DB) through the allocation fraction \(p = R/(R+M+h)\), and includes feedback in which the metabolite lowers the carrying capacity ([1](#ref-1), [2](#ref-2)). The original analyses addressed equilibria and local stability, classification of growth phases, parameter sweeps and application to one measured data set. State reduction, time-scale separation, identifiability and predictive comparison with other growth laws were not treated (as far as the original paper, its supplementary appendices and the thesis text could confirm). The first author of the original paper and the author of the thesis is also the author of this article; the assumptions of the original were not taken to be correct but were checked with equations and numbers.

This article asks two questions. (1) Under which conditions can the three-state ordinary differential equations be reduced to two or one state, and how can the error be evaluated? (2) Do the low-dimensional models obtained by reduction or reformulation offer anything, relative to existing growth laws, when predicting growth curves at medium concentrations not used for calibration? The mathematics of the reductions was verified by symbolic computation and numerical integration; the predictive comparison used a public dilution-series data set.

The reductions build on the classical treatment of the quasi-steady-state assumption in enzyme kinetics ([3](#ref-3)) and on geometric singular perturbation theory ([4](#ref-4)). A growth rate expressed as a saturating function of substrate goes back to Monod ([5](#ref-5)), and a form that includes population density in the saturation constant to Contois ([6](#ref-6)). A limited literature search found no study with the same form of argument (quasi-steady-state reduction of a batch substrate–metabolite model) or with a growth rate of the form \(R^2/(R+h)\). Not finding such work is not a proof that none exists.

## Assumptions and definitions

### The original model

The equations agree between [Equations (1-1) to (1-4) of the original](https://doi.org/10.1016/j.jtbi.2023.111597) ([1](#ref-1), p. 2) and the [doctoral thesis](https://eprints.lib.hokudai.ac.jp/repo/huscap/all/95430/Daiki_Kumakura.pdf) ([2](#ref-2), p. 9), and the symbols follow them.

\[
\frac{dN}{dt}=\mu a_1 R N p\Bigl(1-\frac{N}{K(M)}\Bigr)-dN,\quad
\frac{dR}{dt}=\lambda-a_1RNp-b_1RN(1-p),
\]
\[
\frac{dM}{dt}=a_2RNp+b_2RN(1-p)-cMN(1-p),\quad
p=\frac{R}{R+M+h},\quad K(M)=K_0+(K-K_0)e^{-fM}.
\]

\(\mu\) is the conversion coefficient to growth (1 in the thesis); \(a_1, b_1\) are the substrate-uptake coefficients of MG and DB; \(a_2, b_2\) are the metabolite-production coefficients; \(c\) is the metabolite-degradation coefficient; \(d\) is the death rate; \(h\) is a constant that avoids division by zero in \(p\); \(K_0, K\) are the minimum and optimal carrying capacities; and \(f\) is the coefficient of the metabolite-induced decline of the carrying capacity. Batch culture (\(\lambda=0\)) is treated.

[Table 1 of the original](https://doi.org/10.1016/j.jtbi.2023.111597) ([1](#ref-1), p. 3) and [of the thesis](https://eprints.lib.hokudai.ac.jp/repo/huscap/all/95430/Daiki_Kumakura.pdf) ([2](#ref-2), p. 13) list units that are internally inconsistent (for example \(\mu\) in cell/mL, \(K\) in cell, \(\lambda\) in mL/min). In the numerical examples \(N_0=0.1\), \(K=3\) and the peak is about 1, and the application to measured data used OD600. \(N\) is therefore treated as an effective quantity proportional to OD and do not convert to cell numbers. The time unit is minutes.

The 2023 original paper ([1](#ref-1)) (PDF) and its supplementary appendices S1 to S3 were read, which confirmed that Equations (1-1) to (1-4) (p. 2), Table 1 (p. 3) and the numerical example of [Figure 3](https://doi.org/10.1016/j.jtbi.2023.111597) (p. 5) agree with the doctoral thesis ([2](#ref-2)). The original treats \(\lambda=0\) as batch culture and \(\lambda>0\) as a chemostat-like condition with substrate influx, and in Appendix S3 non-dimensionalizes the model under \(h=0\) and \(K(M)=K\), which removes three parameters. The \(N\) clock of this article separates the structure without reducing the number of parameters, and is a different procedure from that non-dimensionalization. The units in Table 1 are inconsistent in the same way in the original and the thesis, and were treated as described above. Equation (2-1) of the original (p. 3) contains in its equilibrium the expression \((b_2+\sqrt{b_2^2+4a_2c})/(2c)\), which Appendix S3 writes in the non-dimensional form \(x=(\gamma+\sqrt{\gamma^2+4\beta\eta})/(2\eta)\) (\(\beta=a_2/a_1\), \(\gamma=b_2/a_1\), \(\eta=c/a_1\)). It has the same form as the slope for which the quasi-steady curve becomes \(M^*(R)=R\,(b_2+\sqrt{b_2^2+4a_2c})/(2c)\) when \(h=0\) (which follows from \(\mathcal{D}=R^2(b_2^2+4a_2c)\)).

### Symbols and dimensionless quantities

The reaction fluxes are \(U_G=a_1RNp\) and \(U_D=b_1RN(1-p)\). The metabolite yields are defined as \(\nu_G=a_2/a_1\) and \(\nu_D=b_2/b_1\), assuming \(a_1, b_1>0\). When \(\nu_G=\nu_D\) the common value is written \(\nu\).

The following reduced models are defined. Lite-S is the exact reduction for \(c=0\) and \(\nu_G=\nu_D\); Lite-Q is the asymptotic reduction in which \(M\) is replaced by the quasi-steady curve \(M^*(R)\); Lite-W is the weak-feedback approximation with \(p\to R/(R+h)\) and \(K(M)\to K\); Lite-M is a mechanistic model proposed here, with saturating uptake, and is not a reduction.

Figure 1 shows the relations among the models. Solid arrows denote exact reductions, dashed arrows asymptotic approximations, and the dotted arrow a mechanistic reformulation.

![Figure 1: relations among the models](shared/kumakura-lite-model-reduction/figures/fig1_model_relations.png)

**Figure 1.** Relations from the original three-state model to Lite-S, Lite-Q, Lite-W and Lite-M. Lite-S is exact, Lite-Q and Lite-W are asymptotic approximations, and Lite-M is a resource-response law proposed here, not a reduction. The upper right box is the triangular structure in the \(N\) clock. The logistic equation is the exact limit \(h\to0\), \(d=0\), \(K\to\infty\). Conceptual diagram, not a numerical result.

## Methods

### Settings of the numerical experiments

All numerical experiments that verify the theory used reference parameters (not values determined from measurements). The reference set is \(\mu=0.5\), \(a_1=b_1=0.02\), \(a_2=b_2=0.01\), \(c=0\), \(h=1\), \(d=0\), \(K=10\), \(K_0=2\), \(f=0.1\), \(N_0=0.01\), \(R_0=10\), \(M_0=0\), with time in nominal units (only the numerical example of the thesis is in minutes, and only the fits to the dilution-series data are in hours). The ordinary differential equations were integrated with LSODA (rtol \(10^{-11}\), atol \(10^{-14}\)) and output at 4001 points, ending when \(R\) fell to \(10^{-4}R_0\).

The Lite-S check (experiment 1) used \(b_1=0.01\), \(a_2=0.01\), \(b_2=0.005\) (\(\nu=0.5\)), and the \(c>0\) balance was checked with \(c=0.05\). Yield mismatch was produced by changing \(b_2\) so that \(\nu_D/\nu_G\) was 1, 0.9, 0.75, 0.5, 0.25 and 0. The Lite-Q check (experiment 2) used \(a_1=0.02\), \(b_1=0.01\), \(a_2=0.01\), \(b_2=0.005\), \(c=0.05\) as the base, scaled \((a_2,b_2,c)\) by \(s\) at 15 points from 0.1 to 1000, with \(N(0)=0.01\) and \(M_0\) either 0 or \(M^*(R_0)\). The time-scale ratio \(\varepsilon\) is the maximum over \(R\) scanned on \([0.01R_0,R_0]\). The dependence on \(N(0)\) was examined at \(s=30\) and \(M_0=0\) with \(N(0)\) from \(10^{-4}\) to 1. The Lite-W check (experiment 3) used \(a_1=0.02\), \(b_1=0.005\), \(c=0\), \(h=1\) on a grid of 45 points: \(\nu\) at 9 values from \(10^{-3}\) to 3 and \(f\) at 0, \(10^{-3}\), \(10^{-2}\), 0.1 and 1. The Grönwall bound was checked with \(a_1=0.02\), \(b_1=0.005\), \(a_2=0.01\), \(b_2=0.0025\), \(c=f=d=0\) and \(\tau\le20\). The logistic limit used \(\mu=0.5\), \(a_1=b_1=0.02\), \(a_2=b_2=c=0\), \(R_0=10\), \(N_0=0.01\), with \(h/R_0\), \(K/C\) and \(d\) varied as in the table. Computation times are medians of 7 runs at rtol \(10^{-8}\) and atol \(10^{-11}\).

The identifiability analysis was done around the parameters of Figure 3 of the thesis (\(h\) fixed; the seven parameters \(a_1\), \(b_1\), \(a_2\), \(b_2\), \(c\), \(K\), \(f\) estimated). The observation had 61 time points and a noise standard deviation of 2% of each observed maximum. The profile likelihood re-estimated the other parameters on a grid of 15 points of \(\log_{10}c\) (at most 80 function evaluations per point), and may contain points that did not converge.

### Comparison on dilution-series data

The dilution-series data published by Sun et al. ([7](#ref-7), [8](#ref-8)) for 16 strains were used. For each strain, the optical density at 600 nm (OD600) was measured in four wells every 10 minutes for 48 hours at 20 relative initial concentrations of a rich medium (2.88 to 200). The `Time` column of the files steps in units of 600 without a stated unit; it was interpreted as seconds, that is, 10-minute intervals (an assumption based on the authors' preprint, [9](#ref-9)). The data are not blank-corrected (the initial OD has strain medians of 0.101 to 0.105 and individual wells from 0.097 to 0.266), so the observable \(x(t)\) was taken as OD minus the mean of the first three points of each curve, averaged over the four wells and thinned to 97 points at 30-minute spacing. The subtraction uses the initial reading of the held-out curve itself, but the models predict \(N(t)-N(0)\), so no later values of a held-out curve are used.

The model output \(N(t)-N(0)\) was fitted to \(x(t)\). Absolute resource amounts are not measured, so the initial resource \(R_0\) was set equal to the relative concentration, and \(R\) is in relative-concentration units. The mechanistic models (Monod, Hill-type generalised Monod, Monod with density limit, Lite-W, Lite-M, Lite-S, Lite-Q) were fitted jointly with one parameter set shared over all training concentrations, and unused concentrations were predicted without refitting. The numbers of parameters are 4 for Monod, 5 for Hill, 5 for Monod with density limit, 6 for Lite-W, 7 for Lite-M, 10 for Lite-S and 11 for Lite-Q. Monod has \(N_0\), the maximum growth rate, the half-saturation constant \(K_m\) and a yield. The Hill type is \(\mu R^n/(K_m^n+R^n)\), and Monod with density limit multiplies the Monod growth rate by \((1-N/K)\). Lite-M contains Monod in the limit \(h\to0\), \(K\to\infty\). Lite-S is the exact reduction \(M=\nu(R_0-R)\), and Lite-Q the quasi-steady reduction \(M^*(R)\), expressed with two parameters \(a_2/c\) and \(b_2/c\) because the scale of the degradation coefficients does not affect \(M^*\). To examine where the effect of Lite-M comes from, two ablations were added. Lite-M (\(\alpha=1\), 6 parameters) fixes the substrate use of the non-growth function equal to the uptake and keeps the allocation \(R/(R+h)\). Lite-M (\(\alpha=0\), 6 parameters) lets only the growing fraction consume substrate (consumption is also limited by the allocation). A further form, Monod with density limit and a free consumption factor, was also fitted, but it is a reparameterisation in which only the ratio to the Monod yield matters and gave results identical to Monod with density limit, so it is not interpreted (its rows remain in the result files).

For optimisation, 60 random points within log-parameter bounds were screened with fixed-step fourth-order Runge–Kutta, and the best three were refined by least squares (at most 150 evaluations) with adaptive LSODA (rtol \(10^{-7}\), atol \(10^{-10}\)). To Hill, Monod with density limit, Lite-M and the ablations, a start was added that reproduces the Monod fit of the same split (\(n=1\) for Hill; \(K\) at the upper bound for the density-limited forms; \(h\) at the lower bound and \(\alpha=1\) for Lite-M), so that models nested in Monod cannot have a worse training fit than Monod. LSODA was also used for the held-out predictions. At the final parameters of the fits on all concentrations (split "all"), the difference between LSODA at rtol \(10^{-7}\) and at \(10^{-10}\) was at most \(6.4\times10^{-6}\) OD. Global optimality is not guaranteed.

The phenomenological models (Logistic, Gompertz ([10](#ref-10)), Richards, Baranyi ([11](#ref-11))) are own reparameterisations of the standard forms for \(N(t)-N(0)\) (definitions in `realdata.py` of the companion material). They were fitted separately for each concentration, and the parameters at unused concentrations were given by regression on the training concentrations (\(K\) linear in concentration, \(\log r\) linear in \(\log\) concentration, other parameters at the median). Curves with a maximum below 0.02 OD were treated as no growth. They use the same information as the mechanistic models through the regression, but count parameters differently (median over splits in Table 3).

There were five splits: interpolation (6 interior concentrations of the 20 held out), a second interpolation split (6 concentrations shifted by one, run only for Monod, Hill, Monod with density limit, Lite-M and its two ablations), high-concentration extrapolation (train on the lower 14, predict the upper 6), low-concentration extrapolation (train on the upper 10, predict the 7 concentrations where growth starts to be detectable) and fitting on all concentrations. The positions of the held-out concentrations are the same for all strains, and the range of the low-concentration split was chosen from a first look at the data to cover where growth becomes detectable. Training and held-out data come from the same strain and the same plate series at different concentrations; they are not new strains or independent experiments. The metric was the RMSE (root-mean-square error, OD units) against the four-well mean, and the geometric mean of the ratio of RMSE to that of Monod with a 95% interval was obtained by cluster bootstrap over strains (4000 resamples, fixed seed). Held-out predictions that were non-finite or had an RMSE above 1 OD were counted as failures and entered the ratio with RMSE replaced by 1.

The comparison was not reduced beforehand to one primary hypothesis: intervals for 12 models and three splits (plus the second interpolation split) are shown without correction for multiplicity. Lite-M was defined at the start of the analysis as a form that keeps the mechanism of the original, but the check of integration accuracy (with fixed-step fourth-order Runge–Kutta the fits exploited numerical error) and the addition of nested starts were made after the interpolation results on the same data had been seen. In the first run, with fixed-step Runge–Kutta, the Lite-M ratio to Monod in interpolation was 0.86 (0.75–0.99, 12/16 strains) and that of Monod with density limit 1.17. The second run, with adaptive integration, gave 0.70 and 0.85, and the final run with nested starts gave 0.70 and 0.84. The results of the earlier runs are kept in `results/rk4_superseded` and `results/lsoda_run1_superseded` of the companion material.

## Results

### With N as the clock, the three states become triangular

The right-hand sides of \(dR/dt\) and \(dM/dt\) have a factor of \(N\) to the first power (confirmed by symbolic computation; the list of checks is in the companion material).

\[
\frac{dR}{dt}=N\,F_R(R,M),\qquad F_R=-\frac{R\,[a_1R+b_1(M+h)]}{R+M+h},\qquad
\frac{dM}{dt}=N\,G(R,M)=\frac{N\,Q(R,M)}{R+M+h}\tag{1}
\]

where \(Q=a_2R^2+b_2R(M+h)-cM(M+h)\) (Equation (1)). With the clock \(d\tau=N\,dt\), \((R,M)\) becomes an autonomous two-state system \(dR/d\tau=F_R,\ dM/d\tau=G\) independent of \(N\). \(N\) obeys \(dN/d\tau=\mu a_1Rp\,(1-N/K(M))-d\), which is linear in \(N\). Time is recovered by \(t=\int d\tau/N\). The triangular structure holds for \(\lambda=0\); for \(\lambda>0\), \(\lambda/N\) enters \(dR/d\tau\) and \(R\) is no longer independent of \(N\).

It follows that the ratio of the time scales of \(M\) relaxation and \(R\) depletion does not depend on \(N\), which is used in the quasi-steady-state argument below.

### The metabolite balance gives Lite-S exactly

When \(\nu_G=\nu_D=\nu\), \(d(M+\nu R)/dt=-cMN(1-p)\) holds (confirmed symbolically). For \(c=0\), \(M+\nu R\) is conserved and \(M\) can be eliminated as \(M=M_0+\nu(R_0-R)\). The equation for \((R,M)\) then becomes a one-dimensional equation in \(R\), so \(R(\tau)\) can be written as a quadrature, and \(N\) follows from a linear equation.

For \(c>0\), \(M+\nu R\) decreases monotonically and the following bound holds.

\[
M\le M_0+\nu(R_0-R)\tag{2}
\]

 When \(\nu_G\neq\nu_D\), \(d(M+\nu_DR)/dt=(\nu_G-\nu_D)U_G-cMN(1-p)\), and for \(c=0\) the integral term in \(M=M_0+\nu_D(R_0-R)+(\nu_G-\nu_D)\int_0^t U_G\,dt'\) remains. Adding this integral as a state gives an exact rewriting of the three-state model, but the number of states is not reduced.

With the reference parameters for \(\nu=0.5\) and \(c=0\) (`kl_models.py` in the companion material; verification values, not measured), the three-state model was compared with Lite-S (Figure 2). The maximum relative errors of \(N\), \(R\) and \(M\) were \(3.9\times10^{-11}\), \(2.5\times10^{-11}\) and \(2.5\times10^{-11}\), and the drift of the conserved quantity \(M+\nu R\) was \(8.0\times10^{-15}\). When the tolerance was lowered from \(10^{-4}\) to \(10^{-12}\), the difference decreased at the same rate as the error of the three-state model itself (table in the companion material, `results/exp1_tolerance_convergence.csv`). When the yields differ (\(\nu_D/\nu_G\) varied from 0.9 to 0), the relative error of Lite-S was 0.3% to 3.1% for \(N\) and 3.4% to 46% for \(M\). The reconstruction of \(M\) with the integral term added agreed to the trapezoidal-rule error (at most \(4\times10^{-7}\)).

![Figure 2: trajectories of Lite-S and the three-state model](shared/kumakura-lite-model-reduction/figures/fig2_lite_s_exact.png)

**Figure 2.** Comparison of the original three-state model and Lite-S (\(c=0\), \(\nu_G=\nu_D=0.5\), reference parameters). From the left: trajectories of \(N\) and \(M\), trajectory of \(R\), and the error over time. The thin dashed and dotted lines are Lite-S and overlap the solid original solution. The right panel shows the relative errors of \(N\) and \(M\) and the drift of the conserved quantity (log axis). Own simulation, not measured data.

The condition for Lite-S (\(c=0\)) excludes metabolite degradation, so it is not a reduction for general microorganisms with strong detoxification. The role of this model is limited to showing that an exact low-dimensional model can be constructed from the original.

### For fast M relaxation (Lite-Q), the error depends on how the initial value is placed

\(Q=0\) in Equation (1) is the quadratic \(cM^2+(ch-b_2R)M-(a_2R^2+b_2Rh)=0\) in \(M\), whose non-negative root for \(c>0\) is unique:

\[
M^*(R)=\frac{b_2R-ch+\sqrt{\mathcal{D}(R)}}{2c},\qquad \mathcal{D}=(ch-b_2R)^2+4c(a_2R^2+b_2Rh).
\]

\(Q\) is concave in \(M\) and \(Q(R,0)\ge0\), so for fixed \(R\) the curve \(M^*\) is globally attracting (derivation). The local relaxation rate is \(\gamma_M=-\partial(dM/dt)/\partial M|_{M^*}=N\sqrt{\mathcal{D}}/(R+M^*+h)\), confirmed both symbolically and by a numerical Jacobian. \(\gamma_M\) is proportional to \(N\), but so is the change of \(R\); the ratio of the relaxation rate in the \(\tau\) clock, \(\gamma_\tau=\sqrt{\mathcal{D}}/(R+M^*+h)\), to the depletion rate of \(R\), \(|F_R|/R\),

\[
\varepsilon=\max_R\frac{|F_R(R,M^*)|}{R\,\gamma_\tau(R)},
\]

contains no \(N\). From this ratio one cannot say that the quasi-steady-state approximation fails because \(N\) is small.

Scaling \((a_2,b_2,c)\) by the same factor \(s\) leaves \(M^*\) unchanged and multiplies only \(\gamma_\tau\) by \(s\) (because \(M^*\) is homogeneous in the three coefficients). Using this property, \(\varepsilon\) was swept from \(5.6\) to \(5.6\times10^{-4}\) (Figure 3). With the initial value on the quasi-steady curve (\(M_0=M^*(R_0)\)), in the region \(\varepsilon<0.2\) the maximum relative error of \(N\) decreased as \(\varepsilon^{0.90}\) for zero-order Lite-Q and as \(\varepsilon^{1.55}\) for the first-order correction \(M\approx M^*-M^{*\prime}(R)\,F_R/\gamma_\tau\) (slopes on the log axes). For the error of the peak density the slopes were \(0.99\) and \(2.04\). The effectiveness of the first-order correction was confirmed only when starting on the quasi-steady curve. The slopes do not reach the expected orders (1 and 2) and may be pre-asymptotic.

Starting from \(M_0=0\), an initial boundary layer remains. The error of \(N\) decreased only as \(\varepsilon^{0.51}\), and the first-order correction did not reduce it (at \(\varepsilon=5.6\times10^{-4}\), 1.7% for zero order and 1.7% for first order). The first-order correction compensates for the slope of the quasi-steady curve and does not act on the boundary layer.

The origin of this error was examined by varying the initial \(N(0)\) from \(10^{-4}\) to 1 (\(s=30\), \(M_0=0\)). The error of \(N\) in the phase plane with \(R\) on the horizontal axis was almost constant at 0.50–0.55%. This follows from the triangular structure, since the trajectory of \((R,M)\) in the \(\tau\) clock does not depend on \(N(0)\) (the numbers confirm it). The error of \(N(t)\) in the time domain, in contrast, increased as \(N(0)\) became smaller: 0.9% at \(N(0)=1\) and 41% at \(10^{-4}\). The shift of the time at which \(N\) reaches half of its maximum was 0.47, 2.9, 9.7, 19.3 and 29.7 (nominal time units) for \(N(0)=1\), \(10^{-1}\), \(10^{-2}\), \(10^{-3}\) and \(10^{-4}\); it grew by a factor of 1.5 to 6 for each tenfold decrease of \(N(0)\) and was not proportional to \(1/N(0)\). The qualitative interpretation that a lag in the \(\tau\) clock is stretched in the time domain while \(N\) is small is consistent with this result, but was not confirmed quantitatively.

![Figure 3: quasi-steady curve of Lite-Q and its error](shared/kumakura-lite-model-reduction/figures/fig3_lite_q.png)

**Figure 3.** Left: trajectories for \(s=1, 10, 100\) and the quasi-steady curve \(M^*(R)\). Middle: time-scale ratio \(\varepsilon\) and the maximum relative error of \(N\) (Q0 is zero order, Q1 the first-order correction; solid lines for \(M_0=M^*(R_0)\), dashed for \(M_0=0\)). Dotted lines show slopes 1 and 2 as guides. Right: phase-plane and time-domain errors when \(N(0)\) is varied (\(s=30\), \(M_0=0\)). Own simulation.

### The weak-feedback error increases with M/(R+h) (Lite-W)

The change in allocation is exactly \(R/(R+h)-R/(R+M+h)=RM/[(R+h)(R+M+h)]\), and the carrying capacity satisfies \(|K(M)-K|\le|K-K_0|fM\) (from \(1-e^{-x}\le x\)). Dropping the influence of \(M\) gives

\[
\frac{dN}{dt}=\mu a_1\frac{R^2}{R+h}N\Bigl(1-\frac NK\Bigr)-dN,\qquad
\frac{dR}{dt}=-\frac{RN(a_1R+b_1h)}{R+h}
\]

(Lite-W). The error in the \(R\) equation can be evaluated in the \(\tau\) clock. If \(M\le M_{\max}\), then \(|F_R(R,M)-F_R(R,0)|=|a_1-b_1|R^2M/[(R+h)(R+M+h)]\le|a_1-b_1|M_{\max}=:\delta\) (since \(R^2/(R+h)^2\le1\)), and with \(L\) the Lipschitz constant of \(F_R(\cdot,0)\) (bounded by \(\max(a_1,b_1)\)), Grönwall's inequality gives \(|R_{\mathrm{orig}}-R_W|\le(\delta/L)(e^{L\tau}-1)\) (proven). In the numerical example (\(\tau=20\)) the observed error was 0.146 against a bound of 1.84: valid, but about 13 times loose. The bound covers only \(R(\tau)\).

The size of the error was evaluated numerically. On a grid (45 points, \(a_1\ne b_1\), \(h=1\), \(R_0=10\)) with \(\nu=a_2/a_1=b_2/b_1\) from \(10^{-3}\) to 3 and \(f\) from 0 to 1, plotting against \(\zeta=\max M/(R+h)\), the relative error of \(N\) for \(f=0\) and \(\zeta<0.3\) was close to \(0.047\,\zeta\), with a slope of 0.99 (Figure 4). On this grid, for \(c=0\), \(\zeta\) equals \(\nu R_0/h\), so only the axis of \(\nu\) is moved. Varying also \(h\) (0.3 to 10), \(b_1/a_1\) (0.1 to 0.5) and \(R_0\) (10 and 30) in 96 points (\(f=0\); 42 of them with \(\zeta<0.3\)), the ratio of the error to \(\zeta\) spread from 0.010 to 0.20 (median 0.069). That the error increases with \(\zeta\) is certain, but the coefficient 0.047 is not a general constant. Where \(\zeta\) exceeded 1 (\(f=0\), the grid of 45 points) the error reached 6.1% to 64%. A larger \(f\) increased the error (at \(\zeta=0.2\), 0.94% for \(f=0\) and 3.1% for \(f=1\)).

The growth rate \(g(R)=\mu a_1R^2/(R+h)\) increases monotonically, since \(g'(R)=\mu a_1R(R+2h)/(R+h)^2>0\). For \(R\ll h\), \(g\approx(\mu a_1/h)R^2\); for \(R\gg h\), \(g\approx\mu a_1R\). The quadratic dependence at low concentration arises because the allocation \(p\) becomes small in proportion to \(R\) and the uptake is also proportional to \(R\). No study dealing with this form itself was found in a limited search. However, \(pR=R^2/(R+M+h)\) has an algebraic form close to a Monod type whose half-saturation constant depends on a state variable (the Contois type has a constant proportional to biomass ([6](#ref-6)); here it is \(M+h\)), so the novelty should be read as limited.

![Figure 4: phase map of the weak-feedback error](shared/kumakura-lite-model-reduction/figures/fig4_weak_feedback_map.png)

**Figure 4.** Maximum relative error of \(N\) for Lite-W. Left: grid of \(\nu\) and \(f\) (colour is the common logarithm of the error). Right: error against \(\zeta=\max M/(R+h)\) (\(f=0\) and \(f=1\)). Own simulation (\(a_1=0.02\), \(b_1=0.005\), \(h=1\)).

### What was confirmed for reduction to one state is only the logistic limit

In the limit \(h\to0\) (\(p\to1\)), \(d=0\), \(K\to\infty\), without metabolite, \(dN/dt=\mu a_1RN\) and \(dR/dt=-a_1RN\), so \(N+\mu R=C\) (constant) is conserved. Substituting \(R=(C-N)/\mu\) gives the logistic equation \(dN/dt=a_1N(C-N)\) (confirmed symbolically, for \(R>0\)). This relation has the same structure as the known derivation of the logistic equation from mass balance and a constant yield (the source was not checked), and is not claimed as a new result. Extending the balance to general conditions, the rate of change of \(N+\mu R\) is \(-\mu U_D-\mu U_GN/K(M)-dN\), so the factors that break the simple yield approximation decompose into three terms: the substrate flux to DB, density limitation and death (confirmed symbolically).

The range of validity was examined numerically (\(a_1=b_1\), \(\mu=0.5\), \(R_0=10\)). With \(h=10^{-6}R_0\) and \(d=0\), as \(K/C\) was varied from 1 to \(10^8\) the maximum relative error against the logistic solution fell from 38% (\(K/C=1\)) to 0.52% (\(K/C=100\)) and \(10^{-5}\) (\(K/C=10^8\)). Even at \(K/C=10^4\), the error was 4.6% for \(h=10^{-2}R_0\) and 24% for \(h=0.1R_0\), so a small \(h\) was also required. With \(d=0.005\) (within \(T=450\), \(dT\approx2.3\)), small relative to the growth-rate scale \(a_1C=0.10\), the error was still above 85%. No error bound was derived. What was confirmed for reduction to one state is only this limit; it is not claimed that one state is impossible under other conditions (for Lite-S, \(R\) can be written as a quadrature and \(N\) obeys a linear equation, a nearly one-dimensional structure).

### The parameters of the thesis example fall outside the validity conditions of the reductions

The reduced models were applied to the conditions of [Figure 3 of the thesis](https://eprints.lib.hokudai.ac.jp/repo/huscap/all/95430/Daiki_Kumakura.pdf) (\(\mu=1\), \(a_1=0.00025\), \(b_1=0.0015\), \(a_2=b_2=0.001\), \(c=d=0.01\), \(h=10^{-5}\), \(K=3\), \(K_0=1.5\), \(f=0.01\), \(N_0=0.1\), \(R_0=100\), \(M_0=0\), \(\lambda=0\); [2](#ref-2)) (Table 1). In these conditions \(\nu_G=4\) and \(\nu_D=0.67\), so the yields differ; \(c\ne0\); and the feedback is not negligible (\(\zeta_{\max}=0.42\), \(f M_{\max}=0.28\)). \(N\) of the three-state model reached its maximum of 1.24 at 357 min.

**Table 1.** Reduced models applied to the parameter set of the thesis figure (relative sup error against the original model, \(T=4000\) min).

| Model | Start | err N | err R |
| --- | --- | --- | --- |
| Lite-S (\(\nu=a_2/a_1\)) | M0 = 0 | 0.442 | 0.182 |
| Lite-Q, zero order | M0 = 0 | 0.513 | 0.050 |
| Lite-Q, first order | M0 = 0 | 0.561 | 0.059 |
| Lite-W | M0 = 0 | 0.661 | 0.080 |
| Lite-Q, zero order | M0 = M*(R0) | 0.069 | 0.015 |
| Lite-Q, first order | M0 = M*(R0) | 0.070 | 0.008 |

From \(M_0=0\) every reduction gave 44–66% error in \(N\) (the maximum absolute error up to \(T=4000\) min divided by the maximum of \(N\) of the three-state model). Lite-Q fell to 7% when started from \(M_0=M^*(R_0)\), but the three-state reference solution of that row is also different (the maximum of \(N\) is 0.83, not 1.24), so it is not a comparison on the same trajectory. The time-scale ratio is small (\(\varepsilon=0.13\)), but the error from \(M_0=0\) is probably a lag caused by the initial boundary layer. The small density \(N_0=0.1\) may have contributed, which was not confirmed in this example. In this example \(R\) falls only from 100 to 49, and the Lite-S row also depends on the choice \(\nu=a_2/a_1\). The numerical example of the original does not lie in the region where the reductions can be used. Whether a reduction can be used depends on the initial condition as well as on the parameters.

### The resource-response law Lite-M is a product of functional allocation and saturating uptake

Lite-M replaces the linear substrate uptake with a saturating form \(u(R)=v_{\max}R/(K_m+R)\) and keeps the allocation \(p(R)=R/(R+h)\).

\[
\frac{dN}{dt}=N\Bigl[Yu(R)p(R)\Bigl(1-\frac NK\Bigr)-d\Bigr],\qquad
\frac{dR}{dt}=-Nu(R)\bigl[p(R)+\alpha(1-p(R))\bigr].
\]

\(Y\) is the effective biomass yield and \(\alpha\) the relative substrate use of the non-growth function. The growth rate without density limitation is \(g(R)=Yv_{\max}R^2/[(K_m+R)(h+R)]\), which approaches \(Yv_{\max}R^2/(K_mh)\) as \(R\to0\) and \(Yv_{\max}\) as \(R\to\infty\) (confirmed symbolically). It increases monotonically, since \(g'(R)=Yv_{\max}R[2K_mh+(K_m+h)R]/[(K_m+R)^2(h+R)^2]>0\). The local exponent \(d\ln g/d\ln R\) tends to 2 at low concentration and to 0 at high concentration (Figure 5), distinct from the change from 1 to 0 of the Monod law. It reduces to the Monod law as \(h\to0\). This is a mechanistic reformulation that keeps the idea of functional allocation, not an exact reduction of the original. It is a product of two saturations (a Monod-type uptake and the allocation \(R/(R+h)\)), close to the product of a Monod and a Hill type, and is not claimed as a new growth law.

![Figure 5: resource dependence of the growth rate](shared/kumakura-lite-model-reduction/figures/fig5_growth_laws.png)

**Figure 5.** Left: growth rate against resource concentration (log–log; \(h=1\), \(K_m=2\), coefficients normalised to 1). Right: local exponent \(d\ln g/d\ln R\); dotted lines at 0, 1 and 2. Comparison of own functions, not measured data.

### In a single culture curve the metabolite parameters have very low precision under local approximation

The identifiability of the three-state model was evaluated locally around the parameters of the thesis figure (\(h\) fixed, seven parameters estimated). The observation noise was assumed to have a standard deviation of 2% of the maximum of each observed variable (an assumption). The common logarithm of the condition number of the Fisher information matrix was 8.7 when only \(N\) was observed in a single curve, 6.9 for \(N\) and \(R\), and 4.5 for \(N\) and \(M\) (Table 2). With \(N\) alone, the linearised relative standard deviations were 24 for \(a_2\) and 80 for \(b_2\), far above 1, that is, practically undetermined within the local approximation (these numbers are only a guide from linearisation). Fitting three initial substrate levels jointly lowered the common logarithm of the condition number to 5.6, and adding observations of \(N\) and \(M\) brought the relative standard deviation of \(a_2\) to 0.9%. The real-data analysis of the original used three series (cell density, substrate and metabolite; [1](#ref-1)), a situation different from \(N\) alone.

**Table 2.** Local practical identifiability of the original model (7 free parameters; noise SD = 2% of each observed maximum; relative SD is a fraction of the parameter value).

| Design | Observed | log10 condition number | Relative SD of a2 | Relative SD of c | Relative SD of b2 |
| --- | --- | --- | --- | --- | --- |
| single R0 | N | 8.65 | 24.1 | 21.7 | 80.2 |
| single R0 | N+R | 6.94 | 0.704 | 1.85 | 9.36 |
| single R0 | N+M | 4.53 | 0.048 | 0.092 | 0.465 |
| three R0 | N | 5.58 | 0.243 | 0.381 | 1.85 |
| three R0 | N+R | 5.61 | 0.211 | 0.317 | 1.62 |
| three R0 | N+M | 4.22 | 0.009 | 0.034 | 0.144 |

In the profile likelihood of \(c\) (one noise realisation; a grid of 15 points of \(\log_{10}c\); re-estimation of the other parameters with at most 80 function evaluations per point), when only \(N\) was observed at a single initial substrate level, the range with \(\Delta\chi^2\le3.84\) extended from the lower end of the grid (\(\log_{10}c=-3.5\)) to \(-1.14\), so \(c\) was undetermined over more than two decades around the true value of \(-2\). With \(N\) alone but three simultaneous initial levels it was \([-2.21,-2.0]\), and adding observations of \(M\) (single initial level) left only the single grid point of the true value. For \(N\) and \(M\), \(\chi^2\) was not monotone, and the re-estimation may include points that did not converge. This analysis rests on a local approximation and one noise realisation and is not a determination of structural identifiability. Implications for the Lite models on real data are inferences from this result.

### Reducing the number of states did not translate directly into shorter computation

For \(c=0\), with the same parameters and tolerance (rtol \(10^{-8}\)), the median computation time with LSODA was 3.1 ms for the three-state original model, 3.8 ms for Lite-S and 2.7 ms for Lite-W. For \(c=0.05\) it was 4.9 ms for the original, 3.6 ms for Lite-Q and 5.7 ms for the first-order Lite-Q. The numbers of function evaluations were 319, 307 and 371, and 423, 291 and 259, respectively, with small differences. With Radau, the original took 100 ms against 97 ms for Lite-S; no difference due to stiffness was seen. For models of this size, Python overhead dominates, and reducing the number of states did not mean faster computation.

### Interpolation gave Lite-M a smaller error than the Monod family, but extrapolation showed no advantage

Table 3 shows the results, Figure 7 the RMSE ratio to Monod, Figure 8 the relation of parameters, error and computation time, and Figure 6 example predictions.

**Table 3.** Held-out RMSE ratio to the Monod model (geometric mean over 16 strains, 95% cluster-bootstrap interval; number of strains with a smaller RMSE than Monod) and cost.

| Model | Parameters | Interpolation 1 | Interpolation 2 | High extrapolation | Low extrapolation | Fit time (s) |
| --- | --- | --- | --- | --- | --- | --- |
| Hill-Monod | 5 | 0.92 (0.87–0.97); 11/16 | 0.94 (0.89–0.99); 13/16 | 0.79 (0.55–1.08); 6/16 | 0.87 (0.71–0.99); 11/16 | 39 |
| Monod + K | 5 | 0.84 (0.75–0.93); 13/16 | 0.91 (0.84–1.00); 9/16 | 1.05 (0.98–1.18); 11/16 | 1.23 (1.06–1.47); 5/16 | 26 |
| Lite-W | 6 | 1.88 (1.68–2.08); 0/16 | not run | 1.74 (1.12–2.46); 2/16 | 1.40 (1.06–1.87); 5/16 | 20 |
| Lite-M | 7 | 0.70 (0.60–0.81); 16/16 | 0.77 (0.63–0.92); 13/16 | 1.06 (0.74–1.37); 5/16 | 1.02 (0.80–1.27); 9/16 | 100 |
| Lite-M (alpha = 1) | 6 | 0.71 (0.61–0.81); 16/16 | 0.78 (0.67–0.91); 13/16 | 1.04 (0.72–1.40); 5/16 | 1.00 (0.79–1.22); 9/16 | 29 |
| Lite-M (alpha = 0) | 6 | 0.81 (0.72–0.88); 15/16 | 0.89 (0.81–0.98); 11/16 | 0.92 (0.71–1.16); 13/16 | 1.15 (0.95–1.41); 7/16 | 20 |
| Lite-S | 10 | 0.91 (0.81–1.02); 10/16 | not run | 1.85 (1.22–2.74); 4/16 | 1.39 (1.01–1.93); 6/16 | 230 |
| Lite-Q | 11 | 1.51 (1.29–1.73); 1/16 | not run | 2.94 (1.75–4.70); 3/16 | 1.47 (1.05–2.07); 6/16 | 303 |
| Logistic+reg | 42 | 1.73 (1.12–3.29); 2/16 | not run | 1.16 (0.80–1.62); 5/16 | 1.92 (1.34–2.83); 4/16 | 1 |
| Gompertz+reg | 42 | 2.05 (1.36–3.89); 0/16 | not run | 1.23 (0.85–1.74); 4/16 | 1.95 (1.37–2.83); 4/16 | 1 |
| Richards+reg | 56 | 1.25 (1.14–1.41); 1/16 | not run | 1.20 (0.84–1.63); 5/16 | 1.90 (1.29–2.84); 4/16 | 1 |
| Baranyi+reg | 56 | 1.34 (1.18–1.54); 3/16 | not run | 1.47 (0.94–2.22); 4/16 | 1.86 (1.26–2.82); 6/16 | 1 |

Note: Hill-Monod is the Hill-type generalised Monod; Monod + K is Monod with density limit; Lite-M (alpha = 1) and Lite-M (alpha = 0) are ablations of Lite-M; +reg denotes the phenomenological models fitted per concentration with regression for unused concentrations; Interpolation 1 and 2 are the first and second interpolation splits; High and Low extrapolation are the extrapolations to higher and lower concentrations. Parameters are the numbers of free parameters (median over splits for the per-concentration models). Interpolation 2 was run for some models only. Fit time is the median per strain and split and includes the Monod fit used for the nested start in Hill-Monod, Monod + K, Lite-M and the ablations. Ratios below 1 mean a smaller error than Monod.

In the first interpolation split, the RMSE of Lite-M was 0.70 times that of Monod (95% interval 0.60–0.81) and smaller in all 16 strains. The median was 0.008 OD (Monod 0.014, Monod with density limit 0.010, Hill 0.012). The direct ratio to Monod with density limit was 0.83 (0.74–0.92, 14/16 strains) and to the Hill type 0.76 (0.65–0.88, 14/16 strains); the intervals did not include 1. In the second split, with the held-out concentrations shifted by one, Lite-M gave 0.77 times Monod (0.63–0.92, 13/16), 0.84 times Monod with density limit (0.74–0.94, 13/16) and 0.81 times the Hill type (0.67–0.97, 10/16). Lite-S was comparable to Monod (0.91, 0.81–1.02), while Lite-W (1.88) and Lite-Q (1.51) were worse. The phenomenological models fitted per concentration with regression were worse than Monod (1.25 to 2.05). This holds for this regression scheme (\(K\) linear in concentration, other parameters at the median), and the parameter counts of 42 and 56 in the table exceed the roughly five regression coefficients used for prediction.

In the ablations, the 6-parameter Lite-M with \(\alpha\) fixed at 1 gave the same accuracy as Lite-M (ratio to Monod 0.71 in the first split; Lite-M divided by the \(\alpha=1\) form 0.99, 0.98–1.01). The \(\alpha=0\) form (consumption also limited by the allocation) was less accurate (ratio to Monod 0.81, 0.72–0.88, 15/16 strains; Lite-M divided by the \(\alpha=0\) form 0.87, 0.79–0.95; in the second split 0.89 to Monod and 0.87 for Lite-M divided by it). The \(\alpha=0\) form still had a smaller error than Monod with density limit (0.95, 0.91–0.99). The interpolation gain is consistent with a form that contains the allocation factor and in which the non-growth function keeps consuming substrate at low concentrations where growth is suppressed. On the other hand, accuracy was the same with \(\alpha\) free or fixed at 1, so \(\alpha\) itself is not determined by these data. In the fits on all concentrations, \(K_m\) of Lite-M was at its lower bound (0.1) in 7 strains and \(\alpha\) at a bound in 6 strains, so the values of \(K_m\) of the saturating uptake and of \(\alpha\) are not determined by these data. The training RMSE agreed within 1% with that of Monod with density limit in only one strain (105), so Lite-M collapses to Monod with density limit in few strains.

In high-concentration extrapolation, Lite-M gave 1.06 times Monod (0.74–1.37), with no difference that could be confirmed. The Hill type gave 0.79 (0.55–1.08) and Monod with density limit 1.05 (0.98–1.18). Lite-Q (2.94), Lite-S (1.85) and Lite-W (1.74) were worse. In one strain (2443) Monod had an RMSE of 18 OD, which was replaced by 1 as a failure and used as the baseline. Without that strain, Lite-M gave 1.22 times Monod (1.03–1.44), the Hill type 0.91 (0.68–1.12) and Monod with density limit 1.05 (0.97–1.20). In high-concentration extrapolation no advantage of Lite-M was confirmed, and it was worse than Monod once the failed baseline was excluded. The medians were 0.049 OD for Monod and Monod with density limit, 0.050 for the Hill type and 0.063 for Lite-M.

In low-concentration extrapolation, the median of Monod was 0.007 OD and that of the Hill type 0.006 OD, the smallest. Lite-M gave 1.02 times Monod (0.80–1.27), no difference that could be confirmed, and was worse than the Hill type (1.18, 1.04–1.36, better in 3/16 strains). Monod with density limit was worse (1.23, 1.06–1.47). The root-mean-square deviation of single wells from the four-well mean was 0.009 OD (median over strains), which corresponds to a standard deviation of about 0.010 OD per well and about 0.005 OD for the four-well mean (assuming normal noise). The RMSE in the low-concentration split (0.006 to 0.008 OD) is close to this level, which pulls ratios between models toward 1.

The median training RMSE (all concentrations) was 0.0097 OD for Lite-M, 0.0098 for Lite-M with \(\alpha=1\), 0.0121 for Monod with density limit, 0.0156 for the Hill type and 0.0166 for Monod, larger than for Richards (0.0056) and Baranyi (0.0060), which use 56 to 80 parameters per strain fitted per concentration. Goodness of fit did not match goodness of prediction. Among models nested in Monod, the training RMSE of Hill, Lite-M and Lite-M with \(\alpha=1\) never exceeded that of Monod by more than 0.1% in 64 fits, whereas Monod with density limit exceeded it in 5 fits and Lite-M with \(\alpha=0\) in 2 fits (by about 0.2% at most, because \(K\) was bounded at 100 OD). Prediction failures (non-finite or above 1 OD) were one strain for Monod and one for Monod with density limit in high-concentration extrapolation, and one for Gompertz in interpolation. The median computation times were about 10 s for Monod against about 40 s for the Hill type, about 100 s for Lite-M, about 29 s for Lite-M with \(\alpha=1\), about 230 s for Lite-S and about 300 s for Lite-Q.

![Figure 6: example predictions in the interpolation split. Four-well mean observations and model predictions at six held-out concentrations; no model reproduces the decline after the peak](shared/kumakura-lite-model-reduction/figures/fig6_example_fits.png)

**Figure 6.** Predictions at held-out concentrations in the first interpolation split (strain 1299, the strain at the median of the Lite-M/Monod RMSE ratio among the 16 strains, chosen by a rule fixed before the results were seen). Black dots are the mean of four wells; lines are model predictions. The vertical axis is the increase in OD600 from the initial value. After the peak the measured OD declines, which only Lite-S, with its death term, can reproduce. Result of analysis of public data.

![Figure 7: RMSE ratio to Monod. In interpolation Lite-M is smallest; in extrapolation the intervals include 1](shared/kumakura-lite-model-reduction/figures/fig7_prediction_ratio.png)

**Figure 7.** RMSE ratio to Monod at held-out concentrations (geometric mean over 16 strains, 95% cluster-bootstrap interval over strains). The dashed line marks a ratio of 1. From the left: first interpolation split, high-concentration extrapolation, low-concentration extrapolation. Result of analysis of public data.

![Figure 8: relation of the number of parameters, validation error and computation time](shared/kumakura-lite-model-reduction/figures/fig8_complexity.png)

**Figure 8.** Left: number of parameters of the mechanistic models and median held-out RMSE (circles: interpolation; squares: high-concentration extrapolation; triangles: low-concentration extrapolation). Right: median fitting time per strain and split. Result of analysis of public data.

## Discussion

The answer to the reduction question is conditional. For batch culture the triangular structure in the \(N\) clock holds without further conditions, and \(R\) and \(M\) can be studied separately from \(N\). The number of states can actually be reduced only when metabolite degradation is absent and the yields of the growth and non-growth functions are equal (Lite-S, exact), when \(M\) relaxes fast and the initial value is near the quasi-steady curve (Lite-Q, asymptotic), or when \(M/(R+h)\) and \(fM\) are small (Lite-W, asymptotic). The parameters of the numerical example in the original and the thesis have unequal yields (\(\nu_G=4\), \(\nu_D=0.67\)), \(c\neq0\) and \(\zeta_{\max}=0.42\), and for the start \(M_0=0\) fall under none of these conditions. Starting from \(M_0=M^*(R_0)\), the error of Lite-Q falls to 7% (against a different reference trajectory). The reductions are not approximations that replace the original model, but tools to be used region by region of parameter space and initial condition.

Regarding the error of Lite-Q, the explanation that the quasi-steady-state approximation fails because \(N\) is small does not agree with the \(N\)-independence of the time-scale ratio. That the phase-plane error does not depend on \(N(0)\) is a consequence of the triangular structure. The increase of the time-domain error with smaller \(N(0)\) is consistent with the lag in the \(\tau\) clock caused by the initial boundary layer appearing in the time domain, but it was not proportional to \(1/N(0)\) and no quantitative explanation is given. The first-order correction reduced the error below the zero-order one when starting on the quasi-steady curve, but with the realistic start \(M(0)=0\) the boundary layer dominated and it was ineffective. A correction that includes the boundary layer was not derived here.

The work is placed relative to earlier studies. The derivation of the logistic equation from the mass balance of resource consumption is probably known (the source was not checked). The growth rate \(R^2/(R+h)\) has an algebraic form close to a Monod type whose half-saturation constant depends on a state variable (the Contois type has a constant proportional to biomass ([6](#ref-6)); here it is \(M+h\)), so its novelty should be read as limited. That the coefficient in the equilibrium of Equation (2-1) of the original coincides with the slope of the quasi-steady curve at \(h=0\) is a rereading, in terms of the quasi-steady curve, of a structure already in the original. The triangular structure is a change of time that follows from the proportionality of the substrate and metabolite equations to \(N\); it is simple, but useful because it yields the \(N\)-independence of the time-scale ratio. The contribution here is the triangular structure for batch culture, the range of validity of the reductions separated into the three conditions of yield, degradation and feedback, and their numerical verification.

On prediction, Lite-M had a smaller RMSE than Monod (0.70 and 0.77), Monod with density limit (0.83 and 0.84) and the Hill type (0.76 and 0.81) in interpolation to unused concentrations, in both splits. Since Lite-M contains Monod in the limit \(h\to0\), a better fit is natural, but the difference remained at held-out concentrations. The ablations show that accuracy was the same with \(\alpha\) free or fixed at 1 and that the form in which consumption is also limited by the allocation (\(\alpha=0\)) improved less. The interpolation gain is consistent with the combination of the allocation factor and a substrate consumption by the non-growth function that continues at low concentrations where growth is suppressed. The effect of the allocation factor and the effect of the coupling of consumption are not fully separated; the allocation factor gives a quadratic rise at low concentration, so the interpolation gain shows only that this combination suits the shape of the concentration response in this series. The mechanism of functional allocation is not demonstrated. Neither resource nor metabolite was measured in this series, \(R_0\) was set to the relative concentration, and OD is the only observable, so little information distinguishes mechanisms. \(K_m\) and \(\alpha\) of Lite-M sat at their bounds in many strains, so the saturating-uptake part is not supported by these data. In extrapolation no advantage was confirmed; at the high-concentration side it was worse once the failed baseline was excluded, and at the low-concentration side the Hill type was better.

The reduced models (Lite-S, Lite-Q, Lite-W) did not exceed Monod in prediction. Lite-S was comparable in interpolation, and Lite-Q and Lite-W were worse. However, Lite-S, Lite-Q and Lite-W use linear uptake without saturation (and Lite-W has no allocation factor), and the three-state original model itself was not fitted to the real data, so one can say neither that reduction made prediction worse nor that reduction leaves prediction unchanged. Reducing the number of states did not shorten the computation time. Together with the identifiability result of Table 2, observations of OD alone do not determine the metabolite coefficients, so the benefit of fitting reductions that contain the metabolite to real data is presumably small. The assessment may change for data in which \(R\) or \(M\) is measured, which was not tested. Sun et al. report that symbolic regression favours Monod-type growth laws and that identifying the true generative model is not well posed ([7](#ref-7)). That Monod and the Hill type remained strong baselines in the extrapolations here does not contradict that report.

## Limitations

The strength of the mathematical results differs by item. The triangular structure in the \(N\) clock, the exactness of Lite-S, the uniqueness of \(M^*\) and its global attraction (for fixed \(R\)) and the error bound for \(R\) in Lite-W rest on derivation or proof and were checked symbolically. The slopes of the Lite-Q error (observed 0.90 and 1.55), the proportionality coefficient of the Lite-W error, the explanation of the time-domain error by the boundary layer and the range of validity of the logistic approximation are numerical observations and are not shown as theorems. The slopes do not reach the expected orders 1 and 2 and may be pre-asymptotic. The error bound covers only \(R(\tau)\) and is about 13 times loose (observed error 0.146 against a bound of 1.84).

The parameters of the numerical experiments are verification values, not values determined from measurements. Even for the thesis example, \(N\) was treated as a quantity proportional to OD. The identifiability analysis rests on a local approximation around one point and on a single noise realisation, and is not a determination of structural identifiability.

The real-data comparison is limited to one public data set (16 strains). Held-out concentrations are different concentrations of the same strain and the same plate series as the training data, with neighbouring concentrations about 1.25-fold apart; they are not predictions for new strains, new media compositions or independent experiments. Two interpolation splits were used and no others were tried; the two splits use the same 16 strains and share 8 of the 14 training concentrations, so they are not independent evidence. The range of the low-concentration split was chosen from a first look at where growth becomes detectable. Making \(R_0\) proportional to the relative concentration of the rich medium and reading the time unit as 10-minute intervals are assumptions, and the non-linearity of OD against biomass, blank handling and the decline of OD in the late phase (Figure 6) are not in the models. The death rate of Lite-M and the Monod family was fixed at 0. Sums of squares and RMSE are dominated by curves with high OD. Optimisation does not guarantee a global optimum; models nested in Monod received the Monod solution as an extra start, but optimisation is not equally difficult for the other models. The design and the optimisation conditions were changed after the interpolation results on the same data had been seen (Methods), so the final results are not a validation with a specification fixed beforehand. There is no correction for multiplicity. The bootstrap over strains rests on 16 clusters. The three-state original model was not fitted to the real data as a control. Prediction of the growth curve of an unknown medium from its composition was not tested; another data set with 13,608 curves suited for this ([12](#ref-12)) was obtained but not analysed.

Before publication, the article was inspected by AI review agents from three viewpoints (numbers, methods and rules) and their findings were addressed. It has not been checked by a human third party.

## Conclusion

In batch culture the three-state functional-specialization model becomes a closed two-state system \((R,M)\) in the \(N\) clock. It reduces exactly when degradation is absent and the yields are equal (Lite-S), and approximately when the metabolite relaxes fast and the initial value is on the quasi-steady curve, or when the feedback is weak (Lite-Q, Lite-W). The parameters of the numerical example of the original lie outside these conditions for the start \(M_0=0\), where the reduction error was 44% to 66%. What was confirmed for reduction to one state is only the logistic limit.

For predicting dilution concentrations not used for calibration, Lite-M, the product of functional allocation and saturating uptake, gave a smaller error than Monod, Monod with density limit and the Hill type in interpolation (ratio to Monod 0.70 and 0.77; smaller in all 16 strains in the first split). The gain is consistent with the allocation factor combined with substrate consumption that is not limited by it, and did not depend on the value of \(\alpha\), but no advantage was confirmed in extrapolation. The reduced models did not exceed Monod, and reducing the number of states did not shorten computation. What is supported is the interpolation gain of Lite-M and the range of validity of the reductions; the mechanism of functional specialization and prediction for unknown media are not demonstrated.

## Data and code availability

The analysis code, symbolic computation, tests, figure generation and result CSV files are in the companion material (the licence is stated in the accompanying `LICENSE`). The real data (the 16 CSV files of Sun et al.) are not redistributed; the script `fetch_data.py` downloads them from the official repository ([8](#ref-8)) and checks SHA-256 hashes. The result CSV files contain RMSE values and fitted parameters derived from those data, and the results of earlier runs are kept in `results/rk4_superseded` and `results/lsoda_run1_superseded`. The record of the literature search is in `inputs/literature_search.md`. The random seed is 20261106; the environment was Python 3.12, NumPy 2.2, SciPy 1.14 and SymPy 1.14. The 27 symbolic checks and 14 pytest tests pass, and hashes of the deterministic result files can be checked with `check_reproducibility.py`. Timing results depend on the machine.

The full re-run materials are in the [companion archive](shared/kumakura-lite-model-reduction/kumakura-lite-model-reduction-companion.zip).


## References

<span id="ref-1"></span>1. Kumakura D, Yamaguchi R, Hara A, Nakaoka S. Disentangling the growth curve of microbial culture. J Theor Biol. 2023;573:111597. [https://doi.org/10.1016/j.jtbi.2023.111597](https://doi.org/10.1016/j.jtbi.2023.111597)

<span id="ref-2"></span>2. Kumakura D. Functional specialization and phenotypic plasticity: a mathematical modeling approach to microbial growth dynamics [Doctoral thesis]. Hokkaido University; 2025 Mar 25. Dissertation no. 16276. [https://doi.org/10.14943/doctoral.k16276](https://doi.org/10.14943/doctoral.k16276). Full text: [https://hdl.handle.net/2115/95430](https://hdl.handle.net/2115/95430)

<span id="ref-3"></span>3. Segel LA, Slemrod M. The quasi-steady-state assumption: a case study in perturbation. SIAM Rev. 1989;31(3):446–477. [https://doi.org/10.1137/1031091](https://doi.org/10.1137/1031091)

<span id="ref-4"></span>4. Fenichel N. Geometric singular perturbation theory for ordinary differential equations. J Differ Equ. 1979;31(1):53–98. [https://doi.org/10.1016/0022-0396(79)90152-9](https://doi.org/10.1016/0022-0396(79)90152-9)

<span id="ref-5"></span>5. Monod J. The growth of bacterial cultures. Annu Rev Microbiol. 1949;3:371–394. [https://doi.org/10.1146/annurev.mi.03.100149.002103](https://doi.org/10.1146/annurev.mi.03.100149.002103)

<span id="ref-6"></span>6. Contois DE. Kinetics of bacterial growth: relationship between population density and specific growth rate of continuous cultures. J Gen Microbiol. 1959;21(1):40–50. [https://doi.org/10.1099/00221287-21-1-40](https://doi.org/10.1099/00221287-21-1-40)

<span id="ref-7"></span>7. Sun TA, Kičiatovas D, Aapalampi I, Kuosmanen T, Hiltunen T, Mustonen V. Discovering data-driven microbial growth models with symbolic regression. Methods Ecol Evol. 2026;17(7):2135–2148. [https://doi.org/10.1111/2041-210x.70335](https://doi.org/10.1111/2041-210x.70335)

<span id="ref-8"></span>8. Sun TA et al. SR-Monod: symbolic regression and Monod dynamics to study bacterial growth [Software and data]. GitHub; [cited 2026 Nov 6]. GPL-3.0 as stated in the repository; files used are listed with SHA-256 hashes in the companion material. Available from: [https://github.com/anthony-sun/SR-Monod](https://github.com/anthony-sun/SR-Monod)

<span id="ref-9"></span>9. Sun TA, Kičiatovas D, Aapalampi I, Kuosmanen T, Hiltunen T, Mustonen V. Discovering data-driven microbial growth models with symbolic regression [Preprint]. bioRxiv; 2025 Jun 4. [https://doi.org/10.1101/2025.06.02.657040](https://doi.org/10.1101/2025.06.02.657040)

<span id="ref-10"></span>10. Zwietering MH, Jongenburger I, Rombouts FM, van 't Riet K. Modeling of the bacterial growth curve. Appl Environ Microbiol. 1990;56(6):1875–1881. [https://doi.org/10.1128/aem.56.6.1875-1881.1990](https://doi.org/10.1128/aem.56.6.1875-1881.1990)

<span id="ref-11"></span>11. Baranyi J, Roberts TA. A dynamic approach to predicting bacterial growth in food. Int J Food Microbiol. 1994;23(3–4):277–294. [https://doi.org/10.1016/0168-1605(94)90157-0](https://doi.org/10.1016/0168-1605(94)90157-0)

<span id="ref-12"></span>12. Aida H, Ying BW. Population dynamics of *Escherichia coli* growing under chemically defined media. Sci Data. 2025;12(1):984. [https://doi.org/10.1038/s41597-025-05356-3](https://doi.org/10.1038/s41597-025-05356-3)
