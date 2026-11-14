**QOI: If the mean nutrient concentration is the same, does varying it periodically instead of holding it constant slow growth? Under what conditions?**

**COU: To judge whether the mean concentration alone is enough when comparing growth under a varying supply. The conclusions are theoretical conditions and are not used to predict any particular strain or drug.**

QOI (question of interest) is the question this article answers, and COU (context of use) is what the answer is used for.

**Answer: if the supply rate $g(u)$ needed to hold the growth rate at $u$ is convex, the long-run growth rate under a periodic supply cannot exceed that under a constant supply with the same mean.** $g$ being convex is the same as $\varphi=g^{-1}$, the steady-state growth rate as a function of supply, being concave (growth rises more slowly as supply increases). Conversely, if $g$ has a concave stretch ($\varphi$ is convex on the low-supply side, a threshold-like response), slowly alternating two supply levels that correspond to that stretch, for equal times, gives an example that beats the constant supply. The first statement follows from Jensen's inequality, and the second shows that the condition is also necessary.

The setting is a deterministic model with a bounded periodic supply $S(t)$ imposed from outside, no consumption of the nutrient by the cells, no density dependence and exponential growth of the biomass; $g$ is $C^1$, and $C^2$ where convexity is used. The numbers apply only to the transporter model $g(u)=(bu+u^2)/(M-u)$ (a form that assumes binding, unbinding and dilution by growth) with $b/M=0.5$, mean supply $\bar s=1$ and relative amplitude $\alpha=0.8$, and to an artificial non-convex example ($g(u)=cu/(1+u/k)+Bu^2/(M-u)$). The transporter model is always convex; with a square wave of period $10/M$ the long-run growth rate was 12.9% lower than under constant supply. In the non-convex example, switching two levels (0.005 and 0.08) with period $1000/M$ gave 8.7% higher growth. The size of the loss can be bounded on both sides using the variance of the growth rate, but the upper bound can be loose.

Symbols: $S(t)$ is the externally imposed nutrient supply (concentration), $a$ converts concentration into a rate, and $s=aS$ is the converted supply (1/time). Below, both $S$ and $s$ are called "supply", and the symbol is given where the distinction matters. $u$ is the specific growth rate (1/time), $M$ is the upper limit of $u$, $g(u)$ is the supply rate needed to hold the growth rate at $u$ (same dimension as $s$), $\varphi=g^{-1}$ is the steady-state growth rate as a function of supply, $X$ is the biomass (arbitrary units), $\bar S$ is the period average of $S$, and $\lambda$ is the long-run growth rate. In the numerical work time is measured in units of $1/M$. The relative amplitude $\alpha$ means that the supply moves between $\bar s(1\pm\alpha)$ (two levels for the square wave, maximum and minimum for the sinusoid).

## Introduction

Microbial growth rate is usually written as a saturating function of the nutrient concentration in the medium ([1](#ref-1)). In real cultures the concentration changes over time, so when growth differs between a constant and a varying supply with the same mean, the mean concentration alone cannot be used for comparison. The direction of the difference is set by the curvature of the response function: if the response is concave, variation lowers the mean response. This follows from Jensen's inequality ([2](#ref-2)) and has been presented in ecology as a general argument for predicting the effect of environmental variation ([3](#ref-3)).

In competition theory there is classical literature on competitive exclusion and on mechanisms that maintain species diversity in fluctuating environments ([4](#ref-4), [5](#ref-5)). The theory of continuous culture (the chemostat) is collected in a monograph ([6](#ref-6)). There is work deriving bacterial growth laws from intracellular reaction models ([7](#ref-7)), work discussing growth laws in a constraint-based framework ([8](#ref-8)), an experiment measuring *E. coli* growth under nutrient fluctuations with timescales from 30 s to 60 min ([9](#ref-9)), and theory of periodic forcing of the storage-type Droop model ([10](#ref-10)). References 1, 2, 4, 5, 7 and 10 were checked for bibliographic data only, and references 3, 6, 8 and 9 up to summaries; full texts were not checked and no systematic literature search was done. Among the sources checked, none was found that brings together, in one place, the long-run growth rate under a periodic input in a minimal model whose state is the growth rate itself, from existence, uniqueness and attractivity through the size of the loss. The individual elements are standard methods, however, and no new theoretical contribution is claimed.

The aim of this article is to check, by proof and by numerical computation using direct integration, the conditions under which the concavity or convexity argument holds in a model where the growth rate follows the supply with a delay.

## Problem formulation

The model has three quantities: biomass $X$, specific growth rate $u$, and an externally imposed supply $S(t)$.

$$\frac{dX}{dt}=uX,\qquad \frac{du}{dt}=(M-u)\bigl(aS(t)-g(u)\bigr),\qquad 0\le u<M \tag{1}$$

$M$ (1/time) is the upper limit of $u$, $a$ is a coefficient converting concentration $S$ into a rate (1/time), and $g(u)$ (1/time) is the supply rate needed to hold the growth rate at $u$. $S$ is a prescribed function of time, and the cells do not consume the nutrient. Feedback through consumption and density dependence are not treated, and $X$ keeps growing exponentially.

As a concrete example, consider a transporter that binds the substrate and is used for growth, with the $u$ equation $u'=aS(M-u)-bu-u^2$ ($b>0$ is the sum of the unbinding and catalytic rates). This corresponds to $g(u)=(bu+u^2)/(M-u)$ in Equation (1). Dropping the $u^2$ term gives the Monod form $u=Ms/(s+b)$ at steady state ($s=aS$), and the $u^2$ term can be read as dilution by growth. With the term included, $g$ is still convex and the steady-state growth rate $\varphi$ is concave and saturating in the supply. This form is given as the definition of the model here; its derivation from mass-action kinetics is not treated. The only properties of $g$ used in the proofs are those listed in the assumptions below.

Under a constant supply $S\equiv\bar S$, the root $u_c=g^{-1}(a\bar S)$ of $g(u)=a\bar S$ is a stable equilibrium and the long-run growth rate is $u_c$. For a supply $S(t)$ of period $\omega$, the long-run growth rate is defined as

$$\lambda=\lim_{t\to\infty}\frac{1}{t}\log\frac{X(t)}{X(0)}.$$

The comparison is between $\lambda$ and $u_c$ for supplies with the same period average $\bar S=\omega^{-1}\int_0^{\omega}S\,dt$. This is a comparison at equal mean concentration. Comparing at equal total nutrient supplied would need a mass balance and is a different problem, not treated here.

The numerical computations use the dimensionless form $M=1$. Measuring time in units of $1/M$ and dividing $u$, $g$ and $aS$ by $M$ turns Equation (1) into the same form with $M=1$.

## Assumptions and definitions

The assumptions are limited to three.

- A1: $S:[0,\infty)\to[0,\infty)$ is bounded, piecewise continuous and $\omega$-periodic; $a>0$.
- A2: $g:[0,M)\to[0,\infty)$ is $C^1$ with $g(0)=0$, $g'>0$, and $g(u)\to\infty$ as $u\uparrow M$. Where convexity or variance bounds are used, $g$ is $C^2$.
- A3: The initial values are $u(0)\in[0,M)$ and $X(0)>0$.

With $v=-\log(1-u/M)\in[0,\infty)$, so that $u=M(1-e^{-v})$, Equation (1) becomes the scalar equation

$$\frac{dv}{dt}=aS(t)-G(v),\qquad G(v)=g\bigl(M(1-e^{-v})\bigr) \tag{2}$$

$G$ satisfies $G(0)=0$, $G'(v)=Me^{-v}g'(u)>0$ and $G(v)\to\infty$. With $S_{\max}=\sup S$, let $V$ satisfy $G(V)=aS_{\max}$ ($V=0$ if $S_{\max}=0$). With $V_0=\max(v(0),V)$, write $m_0=\min_{[0,V_0]}G'$; $G'$ is continuous and positive, so $m_0>0$. When $V_0=V$, $m_0$ is written $m$. Let $\varphi(s)=g^{-1}(s)$ be the equilibrium growth rate for a supply $s=aS$.

## Derivation

### Existence, uniqueness and attractivity of the periodic solution

**Proposition 1.** Under A1 to A3, the solution of Equation (2) exists for all time and stays in $[0,V_0]$. There is exactly one $\omega$-periodic solution $v^*$ with values in $[0,V]$, and it is the only periodic solution with $v\ge0$. Every solution satisfies
$$|v(t)-v^*(t)|\le e^{-m_0t}\,|v(0)-v^*(0)|.$$

*Proof.* At $v=0$, $v'=aS\ge0$, so $v\ge0$ is preserved. If $v>V$ then $G(v)>aS_{\max}\ge aS$, so $v'<0$ and $[0,V_0]$ is preserved. The solution is bounded and therefore exists for all time, and it is unique because $G$ is $C^1$ and locally Lipschitz. The difference of two solutions satisfies $(v_1-v_2)'=-c(t)(v_1-v_2)$ with $c(t)=\int_0^1G'(\theta v_1+(1-\theta)v_2)\,d\theta\ge m_0$, so $|v_1-v_2|$ decays at least as fast as $e^{-m_0t}$. The period map $P(v_0)=v(\omega;v_0)$ maps $[0,V]$ into itself with Lipschitz constant at most $e^{-m\omega}<1$, so by Banach's fixed-point theorem it has a unique fixed point $v^*(0)$, which gives the periodic solution. Any other periodic solution $v_p$ would satisfy $|v_p-v^*|\to0$, and both are periodic, so they coincide. $\square$

### Growth rate and the period-average identity

Since $u=M(1-e^{-v})$ is $M$-Lipschitz in $v$, $|u(t)-u^*(t)|\le M|v(t)-v^*(t)|$ decays exponentially. For any initial values, the growth of $\log X$ is therefore $\int_0^tu\,ds$, which differs from $\int_0^tu^*\,ds$ only by a bounded amount.

**Proposition 2.** The long-run growth rate is $\lambda=\bar u^*:=\omega^{-1}\int_0^\omega u^*dt$, independent of the initial values, and along the periodic solution

$$a\bar S=\overline{g(u^*)} \tag{3}$$

holds (an overline denotes the period average).

*Proof.* The first part follows from the previous paragraph. Integrating Equation (2) for $v^*$ over one period gives $v^*(\omega)=v^*(0)$, so $0=\int_0^\omega(aS-G(v^*))\,dt=\omega a\bar S-\int_0^\omega g(u^*)\,dt$. $\square$

### A periodic supply is slower when $g$ is convex

**Theorem 3.** If $g$ is convex, then $\lambda\le u_c$ for every periodic supply. Equality holds if and only if $g$ is affine on the range $[u_{\min},u_{\max}]$ of $u^*$. If $g$ is strictly convex, the inequality is strict unless $S$ is constant.

*Proof.* From Equation (3) and Jensen's inequality, $g(\lambda)=g(\bar u^*)\le\overline{g(u^*)}=a\bar S=g(u_c)$. Since $g$ is increasing, $\lambda\le u_c$. Equality in Jensen's inequality holds exactly when the convex function is affine on the range. If $g$ is strictly convex, equality requires $u^*$ to be constant; then $v^*$ is constant too, and Equation (2) gives $aS(t)=G(v^*)$ almost everywhere, so $S$ is constant. $\square$

### A counterexample when $g$ is not convex

$\varphi=g^{-1}$ is convex where $g$ is concave, because $\varphi'=1/g'$ gives $\varphi''=-g''/g'^3$. Where $\varphi$ is convex, slowly alternating two supply levels gives a growth rate above the constant supply. The next proposition makes the error of this slow-switching limit explicit.

**Proposition 4.** Let $S$ be a square wave taking $s_2=aS_2$ and $s_1=aS_1$ ($0\le s_1<s_2$) for half a period $\omega/2$ each. With $V=G^{-1}(s_2)$ and $m=\min_{[0,V]}G'$,

$$\Bigl|\lambda-\tfrac12\bigl(\varphi(s_1)+\varphi(s_2)\bigr)\Bigr|\le\frac{2MV}{m\,\omega} \tag{4}$$

*Proof.* During a half period with constant $s_i$, $w=v-v_i$ with $v_i=G^{-1}(s_i)$ satisfies $w'=-(G(v)-G(v_i))$. Both $v^*$ and $v_i$ lie in $[0,V]$, so $|w(0)|\le V$, and as in Proposition 1, $|w(t)|\le Ve^{-mt}$. Over a half period, $\int|u^*-u_i|\,dt\le M\int|w|\,dt\le MV/m$, with $u_i=M(1-e^{-v_i})=\varphi(s_i)$. Adding the two half periods gives $|\int_0^\omega u^*dt-\tfrac{\omega}{2}(u_1+u_2)|\le2MV/m$, and dividing by $\omega$ gives Equation (4). $\square$

**Corollary 5.** Let $g\in C^2$. If $g''(u_0)<0$ for some $u_0\in(0,M)$, there is a periodic two-level supply with $\lambda>u_c$. Hence for $C^2$ functions $g$, "$\lambda\le u_c$ for every periodic supply" is equivalent to $g$ being convex.

*Proof.* Let $s_0=g(u_0)>0$. Since $\varphi''(s_0)=-g''(u_0)/g'(u_0)^3>0$, there is $\delta\in(0,s_0)$ such that $\varphi$ is strictly convex on $[s_0-\delta,s_0+\delta]$. Take $s_1=s_0-\delta$ and $s_2=s_0+\delta$. Then $\Delta=\tfrac12(\varphi(s_1)+\varphi(s_2))-\varphi(s_0)>0$, and $u_c=\varphi(s_0)$ for the mean $(s_1+s_2)/2=s_0$. By Equation (4), for $\omega>2MV/(m\Delta)$ we get $\lambda\ge\tfrac12(\varphi(s_1)+\varphi(s_2))-2MV/(m\omega)>u_c$. The converse is Theorem 3. $\square$

### Size of the loss

Let $g\in C^2$, and suppose $\kappa_1\le g''\le\kappa_2$ and $\gamma_1\le g'\le\gamma_2$ on the range $[u_{\min},u_{\max}]$ of the periodic solution. Let $\mathrm{Var}(u^*)=\overline{(u^*-\bar u^*)^2}$ be the variance along the periodic solution.

**Proposition 6.**

$$\frac{\kappa_1}{2\gamma_2}\,\mathrm{Var}(u^*)\le u_c-\lambda\le\frac{\kappa_2}{2\gamma_1}\,\mathrm{Var}(u^*) \tag{5}$$

*Proof.* By Taylor's theorem, $g(u)-g(\bar u^*)-g'(\bar u^*)(u-\bar u^*)\in[\tfrac{\kappa_1}{2},\tfrac{\kappa_2}{2}](u-\bar u^*)^2$. Taking the period average removes the linear term and gives $D:=\overline{g(u^*)}-g(\lambda)\in[\tfrac{\kappa_1}{2},\tfrac{\kappa_2}{2}]\mathrm{Var}(u^*)$. By Equation (3), $D=g(u_c)-g(\lambda)$. Because $g(u_{\min})\le\overline{g(u^*)}=g(u_c)\le g(u_{\max})$, $u_c$ also lies in the range, and the mean value theorem gives $D/\gamma_2\le u_c-\lambda\le D/\gamma_1$. $\square$

### Exact expressions for the transporter model

With $A=M^2+bM$, $g(u)=(bu+u^2)/(M-u)$ can be written $g(u)=A/(M-u)-(2M+b)+(M-u)$. Then $g'(u)=A/(M-u)^2-1$, $g''(u)=2A/(M-u)^3>0$, and $g'(0)=b/M>0$. So $g$ is strictly convex on $[0,M)$ and satisfies A2. Since $g'$ and $g''$ are increasing, the constants in Equation (5) are set by the end points of the range ($\kappa_1=g''(u_{\min})$, $\kappa_2=g''(u_{\max})$, $\gamma_1=g'(u_{\min})$, $\gamma_2=g'(u_{\max})$).

**Proposition 7.** For the transporter model, with $w=M-u^*$,

$$D=\overline{g(u^*)}-g(\lambda)=A\Bigl(\overline{\tfrac1w}-\tfrac{1}{\bar w}\Bigr)\ge0,\qquad u_c-\lambda=\frac{D}{g'(\xi)} \tag{6}$$

($\xi$ lies between $\lambda$ and $u_c$).

*Proof.* In the decomposition of $g$ only the $A/(M-u)$ term is nonlinear, and the $(M-u)$ term preserves the period average. The rest follows from the mean value theorem. $\square$

### Finite observation window

The difference between the growth rate averaged over a window $[0,T]$ and the periodic mean comes from the length of the transient.

**Proposition 8.** For any initial value $v(0)$ and any $T>0$,

$$\Bigl|\frac1T\int_0^Tu\,dt-\bar u^*\Bigr|\le\frac{MV_0/m_0+M\omega}{T}.$$

*Proof.* Add $\int_0^T|u-u^*|dt\le M\int_0^\infty|v-v^*|dt\le MV_0/m_0$ to the end term $|\int_0^Tu^*dt-T\bar u^*|\le M\omega$ that arises when $T$ is not a multiple of $\omega$. $\square$

## Numerical verification

### Methods

The ordinary differential equation (ODE) (2) was integrated numerically by a method different from the derivation (direct integration). For piecewise constant inputs each piece, and for the sinusoid one period, was integrated with the DOP853 method of SciPy (relative tolerance $10^{-11}$); environment and versions are given in "Data and code availability". The periodic solution was found by solving $P(v_0)-v_0=0$ by shooting (Brent's method) and compared with the result of integrating from a different initial value for up to 400 periods. The Floquet multiplier (the factor by which a small perturbation around the periodic solution grows over one period; below 1 the periodic solution is stable) was computed both as $\exp(-\int_0^\omega G'(v^*)dt)$ and by a finite difference of the period map. The mean $\bar u^*$, $\mathrm{Var}(u^*)$, $\overline{g(u^*)}$ and $\overline{1/w}$ were obtained from the same integration as the periodic solution. The random seed was fixed at 20261114. The reference parameters were $b/M=0.5$ (dimensionless), $\bar s=a\bar S/M=1$ and relative amplitude $\alpha=0.8$.

The checking scripts were written after the derivation, by the same author, using the same formulas ($G$, $g$ and the constants of the bounds). They are not blinded and not an independent implementation. The checks show that the statements survived a test that could have found errors in the derivation; they are not independent support for the proofs.

### Three supplies with equal mean

For a constant supply $u_c=0.5000$ ($g(0.5)=1$). Computations were run for seven periods (0.1, 0.3, 1, 3, 10, 30 and 100, in units of $1/M$); Table 1 gives the square wave and the sinusoid for periods 0.1, 1, 10 and 100 (all seven are in `equal_mean_comparison.csv` of the companion archive).

Table 1. Periodic solutions under supplies with the same mean (square wave and sinusoid, $b/M=0.5$, $\bar s=1$, relative amplitude $\alpha=0.8$). $u_c=0.5000$.

| Input | Period (1/M) | Mean u* | Relative loss (%) | Var(u*) | Bound on u_c − mean u* (Equation 5) | Floquet multiplier |
|---|---|---|---|---|---|---|
| Square | 0.1 | 0.49992 | 0.016 | 3.33e-05 | 7.17e-05 to 8.90e-05 | 0.779 |
| Square | 1 | 0.49302 | 1.40 | 2.96e-03 | 2.74e-03 to 1.88e-02 | 0.0832 |
| Square | 10 | 0.43555 | 12.9 | 3.09e-02 | 1.05e-02 to 5.66e-01 | 5.0e-11 |
| Square | 100 | 0.41929 | 16.1 | 3.90e-02 | 1.32e-02 to 7.17e-01 | 2.7e-102 |
| Sine | 0.1 | 0.49995 | 0.0097 | 2.02e-05 | 4.53e-05 to 5.20e-05 | 0.779 |
| Sine | 1 | 0.49578 | 0.84 | 1.78e-03 | 2.26e-03 to 8.12e-03 | 0.0828 |
| Sine | 10 | 0.46625 | 6.75 | 1.59e-02 | 6.29e-03 to 2.47e-01 | 2.7e-11 |
| Sine | 100 | 0.46205 | 7.59 | 1.85e-02 | 6.29e-03 to 3.38e-01 | 5.3e-106 |

Notes: Relative loss is $(u_c-\bar u^*)/u_c$. Var(u*) is the variance along the periodic solution. Bound gives the lower and upper limits of $u_c-\bar u^*$ from Equation (5). The Floquet multiplier is $\exp(-\int G')$, the slope of the period map. $\omega$ is the period and $m$ is the minimum of $G'$. An entry such as 5.0e-11 means $5.0\times10^{-11}$.

The shorter the period, the smaller the loss (the variation is averaged out before it reaches the growth rate), and the longer the period, the larger the loss; the square wave approaches the slow-switching limit $\tfrac12(\varphi(s_1)+\varphi(s_2))=0.41748$ (relative loss 16.5%). Over all seven computed periods and both input types, the loss was non-negative and lay within the range of Equation (5). The difference between the mean growth rate from shooting and from long integration was at most $1.3\times10^{-13}$, the residual of Equation (3) at most $1.0\times10^{-12}$, and the difference between the exact $D$ of Equation (6) and the direct computation at most $1.2\times10^{-15}$. For periods up to 3 the two Floquet methods agreed to a relative difference of at most $7\times10^{-7}$. For periods of 10 and above, the values from integration were at most $5.1\times10^{-11}$, but the finite-difference values were lost in round-off (absolute value up to $2.9\times10^{-8}$, with negative values) and could not be compared. That the multiplier is always below 1 was checked with the integration values.

![Three supplies with the same mean (top) and the specific growth rate of the periodic solution of the transporter model (bottom).](shared/periodic-supply-monod-growth/figures/fig1_equal_mean_inputs.png)

Figure 1. Three supplies with the same mean (top: constant, square wave and sinusoid; $s=aS$, mean $\bar s=1$, relative amplitude $\alpha=0.8$, period $10/M$) and the specific growth rate $u^*(t)$ of the periodic solution of the transporter model ($b/M=0.5$) (bottom). Dotted lines are the mean $\bar u^*$ of each periodic solution (orange: square wave 0.436; blue: sinusoid 0.466) and the thick grey line is the growth rate under constant supply, $u_c=0.500$.

![Relative loss of the growth rate against constant supply as a function of the supply period (square wave and sinusoid).](shared/periodic-supply-monod-growth/figures/fig2_loss_vs_period.png)

Figure 2. Supply period (horizontal axis, units of $1/M$, logarithmic) and the relative loss of growth rate against constant supply, $(u_c-\bar u^*)/u_c$ (vertical axis, %). Transporter model ($b/M=0.5$), mean supply $\bar s=1$, relative amplitude $\alpha=0.8$. The orange dashed line is the slow-switching limit of the square wave.

### Randomised checks

$b/M$ was drawn log-uniformly from 0.05 to 3 and the period log-uniformly from 0.05 to 50. With probability 0.8 the supply was piecewise constant with 2 to 5 pieces (the number of pieces uniform, the piece-length ratios Dirichlet(1.5), the levels lognormal with log standard deviation 0.7, and each piece set to zero supply with probability 0.15); with probability 0.2 it was a sinusoid (mean lognormal with log standard deviation 0.5, relative amplitude uniform from 0.1 to 1). 300 draws were checked in the transporter model. Table 2 gives the results.

Table 2. Checks over 300 random draws (240 piecewise constant, 60 sinusoidal), transporter model, convex $g$.

| Check | Result |
|---|---|
| (a) Identity, Equation (3): max residual | 1.7e-12 |
| (b) Jensen, Theorem 3: draws with loss < 0 | 0 of 300 (smallest loss 2.2e-09) |
| (c) Exact gap, Equation (6): max difference to direct computation | 5.8e-15 |
| (d) Two-sided bound, Equation (5): violations | 0 of 300 |
| (e) Contraction of the period map, Proposition 1: draws with excess over the bound above 1e-10 | 0 of 300 (2 draws have an excess above 1e-12, maximum 4.5e-12; largest ratio to the bound, where the bound is above 1e-8: 0.96) |
| (f) Floquet multiplier ≤ exp(−mω) | 0 violations of 300 |
| Relative growth loss (u_c − mean u*)/u_c | median 0.46%; 75th percentile 2.6%; maximum 44%; above 1% in 40% of draws |

Notes: The excess in (e) is within the ODE tolerance ($10^{-11}$) and was not counted as a violation. In (e) and (f), $m$ is the minimum of $G'$ and $\omega$ is the period. An entry such as 1.7e-12 means $1.7\times10^{-12}$. The ratio of the absolute difference $u_c-\bar u^*$ to the variance $\mathrm{Var}(u^*)$ ranged from 1.25 to 4.42 over the 300 draws of this random design; the range depends on the design and is not a constant given by Equation (5).

![Growth-rate loss and the range of Equation (5) for 300 random draws.](shared/periodic-supply-monod-growth/figures/fig3_jensen_gap_bound.png)

Figure 3. Loss of growth rate against constant supply, $u_c-\bar u^*$ (orange dots), and the range from the lower to the upper bound of Equation (5) (blue lines) for 300 random draws (horizontal axis: draw index sorted by loss). Transporter model.

The upper bound of Equation (5) is loose when $g'$ and $g''$ vary a lot over the range (when the growth rate approaches $M$); the median ratio of upper to lower bound over the 300 draws was 2.7. The lower bound came close to 1 in some draws (largest ratio of lower bound to loss 0.9995).

### A counterexample with non-convex $g$

$g(u)=cu/(1+u/k)+Bu^2/(M-u)$ ($c=1$, $k=0.2$, $B=1$, $M=1$) satisfies $g(0)=0$ and $g'>0$, diverges as $u\to M$, and is concave for $u<0.1058$ (the end of the concave stretch is the root $u=0.105809$ of $g''=0$, which corresponds to a supply of $g(0.105809)=0.0817$). This is an artificial example in which $\varphi$ is convex on the low-supply side ($s<0.0817$, a threshold-like response), not the response of any particular organism. Both input levels (0.005 and 0.08) lie on that side. A supply taking $s=0.005$ and $0.08$ for equal times (mean 0.0425) was computed for different periods (Table 3). As a comparison, the same input was applied to the convex transporter model ($b/M=0.5$).

Table 3. Relative change (%) in mean growth rate against constant supply under a two-level supply (0.005 and 0.08, equal times).

| Period (1/M) | Non-convex g | Convex transport g (b/M = 0.5) |
|---|---|---|
| 0.3 | +0.0089 | −0.0083 |
| 1 | +0.098 | −0.092 |
| 3 | +0.80 | −0.76 |
| 10 | +4.32 | −4.39 |
| 30 | +7.21 | −8.05 |
| 100 | +8.29 | −9.52 |
| 1000 | +8.71 | −10.08 |
| Slow-switching limit | +8.76 | −10.15 |

Notes: The slow-switching limit compares $\tfrac12(\varphi(s_1)+\varphi(s_2))$ with $u_c$. The error bound of Equation (4) held for all periods (for period 1000 the bound is $3.6\times10^{-4}$ and the actual error was $2.3\times10^{-5}$).

![The three panels of the counterexample with non-convex $g$.](shared/periodic-supply-monod-growth/figures/fig4_nonconvex_counterexample.png)

Figure 4. Counterexample with non-convex $g$. Left: $g(u)=cu/(1+u/k)+Bu^2/(M-u)$ ($c=1$, $k=0.2$, $B=1$, $M=1$; orange) and the transporter $g$ ($b/M=0.5$; blue); the light blue band is the stretch where the non-convex $g$ is concave ($u<0.1058$). Middle: $\varphi=g^{-1}$ of the non-convex $g$ (orange) and the chord between the supply levels 0.005 and 0.08 (grey dashed); the blue dot is the growth rate under the constant mean supply (0.0425), 0.0498, and the orange dot is the slow-switching limit, 0.0542. Right: period of the two-level supply (0.005 and 0.08, equal times; horizontal axis, logarithmic) and the change in mean growth rate against constant supply (%); orange: non-convex $g$, blue: convex transporter $g$.

With non-convex $g$, the longer the supply period, the more the growth rate rose above the constant supply, whereas in the convex transporter model the same input lowered it. For short periods both approach 0, because fast variation puts the growth rate near the equilibrium for the mean supply.

### Finite observation window

Proposition 8 was checked in the transporter model ($b/M=0.5$, square wave of period 10, mean 1). The periodic mean is 0.43555. With $v(0)=0$, the difference between the window mean and the periodic mean for window lengths $T=10$, 50 and 500 was $7.2\times10^{-3}$, $1.4\times10^{-3}$ and $1.4\times10^{-4}$, decreasing in inverse proportion to $T$. With $v(0)=V$ it was $1.2\times10^{-2}$, $2.4\times10^{-3}$ and $2.4\times10^{-4}$. The bound of Proposition 8 (1.19, 0.238, 0.0238) held for all windows but was about 100 to 170 times the actual difference, so it is loose.

## An analogy with response curves

Apart from growth, the same curvature argument applies to the average of an effect $E(C)$ that responds instantaneously to an exposure $C(t)$. If $E$ is concave, then at the same mean exposure a varying exposure lowers the mean effect, and if convex it raises it. This was computed with an Emax model (a saturating curve with a maximum effect) $E(C)=C^h/(\mathrm{EC}_{50}^h+C^h)$, where $\mathrm{EC}_{50}$ is the exposure giving half the maximum effect and $h$ is the Hill coefficient (the steepness of the curve); exposure is in units of $\mathrm{EC}_{50}$ (Table 4).

Table 4. Mean effect of a constant exposure and of a two-level exposure (equal times) with the same mean, under the instantaneous response $E(C)=C^h/(1+C^h)$.

| Hill coefficient h | Exposure levels | Mean exposure | Effect, constant | Effect, two-level | Difference |
|---|---|---|---|---|---|
| 1 | 0.2 and 1.8 | 1.0 | 0.500 | 0.405 | −0.095 |
| 1 | 0.5 and 3.5 | 2.0 | 0.667 | 0.556 | −0.111 |
| 3 | 0.2 and 0.9 | 0.55 | 0.143 | 0.215 | +0.072 |
| 3 | 0.4 and 1.6 | 1.0 | 0.500 | 0.432 | −0.068 |
| 3 | 0.2 and 1.8 | 1.0 | 0.500 | 0.431 | −0.069 |

Notes: For $h=1$, $E$ is concave everywhere. For $h=3$, $E''=0$ at an exposure of $0.794\,\mathrm{EC}_{50}$, and the range below it is convex.

For $h=1$ the mean effect always fell. For $h=3$ it rose only for the pair of levels 0.2 and 0.9. The mean exposure of this pair, 0.55, is below the inflection point (0.794), but the higher level, 0.9, is above it, so this result is due not only to curvature but also to the chord between the two points lying above the curve. This is an analogy that transfers only the curvature argument; it contains no pharmacokinetic delay or transfer to the site of action and is not a result for any particular drug. In the growth model, the loss approaching 0 for short periods corresponds to the averaging-out effect that arises when the response follows the exposure with a delay.

## Discussion

The main results here are the application of standard arguments to the model of Equation (1), in which the growth rate follows the supply with a delay. Jensen's inequality ([2](#ref-2)), the fact that the direction of the effect of variation is set by the curvature of the response function ([3](#ref-3)), and relative nonlinearity in competition theory ([4](#ref-4), [5](#ref-5)) are known frameworks; their full texts were not checked here and the accuracy of their statements was not verified. The theory of the chemostat with periodic input ([6](#ref-6)), the derivation of growth laws ([7](#ref-7)) and periodic forcing of the storage-type model ([10](#ref-10)) are references judged related from their titles and bibliographic data, and they differ in model form (here the supply is imposed from outside and the cells do not consume it).

Four points written out here explicitly by standard methods are the following. Each is an application of textbook techniques, and no new theoretical contribution is claimed.

- Existence, uniqueness and attractivity of the periodic solution of the scalar Equation (2) through a contraction map (Proposition 1).
- An explicit error bound $2MV/(m\omega)$ for the slow-switching limit and the equivalence between convexity and the inequality for non-convex $g$ (Proposition 4, Corollary 5).
- The two-sided bound on the loss (Equation (5)).
- The exact expression for the transporter model (Equation (6)).

The point of Theorem 3 is that the static Jensen argument still holds, for every period, in Equation (1), where the growth rate follows the supply with a delay. In the slow-switching limit the result agrees with the static prediction $\tfrac12(\varphi(s_1)+\varphi(s_2))$ (Proposition 4). Whether these appear in the existing literature cannot be told from the sources checked.

To read the results: $\varphi$ is the steady-state growth rate as a function of the supply, so $\varphi$ being concave is the same as $g$ being convex. The constraint-based work ([8](#ref-8)) includes, in the summary checked, a result that growth shows diminishing returns in nutrient influx. Mapping influx to the supply $aS$ of this article is an assumption, and the property points in the same direction as the concavity of $\varphi$, but the correspondence was not checked. From the proofs here, in the range where $\varphi$ is concave, a periodic supply is slower than a constant supply with the same mean. The direction of an experiment that measured reduced growth under fluctuating nutrients ([9](#ref-9)) agrees with this prediction. In the summary checked, however, the reduction was reported to be smaller than the value predicted from a single switch, and the topic of that work is a growth physiology that is not in the model here. Agreement in direction is not a validation, and no explanation or reproduction of the experiment is claimed. No mapping between the experimental periods (30 s to 60 min) and the dimensionless period of this article was made.

## Limitations

- The supply $S(t)$ is imposed from outside and the cells do not consume it. Propositions 1 to 8 do not apply to systems in which cells consume the nutrient and change the concentration (systems with feedback, such as the chemostat). There is no density dependence, and $X$ keeps growing exponentially.
- The comparison was made at equal mean concentration. Comparing at equal total nutrient supplied needs a mass balance, and the conclusions here do not carry over directly.
- This is a deterministic model of a single population. Stochastic extinction and competition among strains are not treated.
- The assumption on $g$ is A2, and Propositions 4 to 7 use $C^2$. The form of the transporter model is given as a definition; its derivation and its fit to real strains were not examined.
- The numerics are a few examples in dimensionless form ($M=1$) and 300 random checks of the transporter model. The non-convex $g$ is an artificial single functional form, not the response of any particular organism. The checks were written after the derivation by the same author using the same formulas, and are neither blinded nor an independent implementation. They show that no counterexample to the derivation was found; they do not replace the proofs.
- The random checks used the distributions given above ($b/M$, period, number of pieces, levels), and numbers such as the median loss depend on that design.
- The upper bound of Equation (5) is loose when the growth rate approaches $M$. The bound of Proposition 8 was about 100 to 170 times the actual difference.
- Reference checking was limited to bibliographic data only (references (1, 2, 4, 5, 7, 10)) and summaries (references (3, 6, 8, 9)); full texts were not checked.

## Conclusion

Under a supply with the same mean, the long-run growth rate under a periodic supply does not exceed that under a constant supply if and only if the supply rate needed to hold the growth rate, $g$, is convex. This conclusion holds for $C^2$ functions $g$, a bounded periodic supply imposed from outside, and a deterministic model in which the cells neither consume the nutrient nor show density dependence. The direction is preserved for every period even though the growth rate follows the supply with a delay (Theorem 3), and in the slow-switching limit it agrees with the static Jensen prediction (Proposition 4). The numerics, for the transporter model with $b/M=0.5$ and an artificial non-convex example, show only that the derivation was not contradicted. The conclusion does not apply to systems with feedback from consumption, to comparisons at equal total nutrient supplied, or to real strains. The mean concentration alone is not enough to compare growth under a varying supply; the curvature of the response function is needed.

## Data and code availability

The material for re-running (the scripts in `analysis/`, the tables, figures and logs in `outputs/`, and the hash list `MANIFEST_SHA256.txt`) is included in the [companion archive](shared/periodic-supply-monod-growth/periodic-supply-monod-growth-companion.zip). There is no input data; everything is computed from the equations. The environment is Python 3.12.4 ([11](#ref-11)), NumPy 2.2.6 ([12](#ref-12)), SciPy 1.14.0 ([13](#ref-13)), pandas 2.2.2 ([14](#ref-14)) and Matplotlib 3.9.1 ([15](#ref-15)), and the random seed is 20261114. Run `python -X utf8 analysis/01_periodic_solution.py`, `02_random_checks.py`, `03_nonconvex_counterexample.py`, `04_finite_window_and_response_analogy.py`, `05_figures.py` and `06_manifest.py` in order.

## References

<span id="ref-1"></span>1. Monod J. The growth of bacterial cultures. Annu Rev Microbiol. 1949;3:371–394. [doi:10.1146/annurev.mi.03.100149.002103](https://doi.org/10.1146/annurev.mi.03.100149.002103). Bibliographic data only.

<span id="ref-2"></span>2. Jensen JLWV. Sur les fonctions convexes et les inégalités entre les valeurs moyennes [On convex functions and the inequalities between mean values; English title translated by the author]. Acta Math. 1906;30:175–193. [doi:10.1007/BF02418571](https://doi.org/10.1007/BF02418571). Bibliographic data only.

<span id="ref-3"></span>3. Ruel JJ, Ayres MP. Jensen's inequality predicts effects of environmental variation. Trends Ecol Evol. 1999;14(9):361–366. [doi:10.1016/S0169-5347(99)01664-X](https://doi.org/10.1016/S0169-5347(99)01664-X). Indexing pages and summaries read; full text not checked.

<span id="ref-4"></span>4. Armstrong RA, McGehee R. Competitive exclusion. Am Nat. 1980;115(2):151–170. [doi:10.1086/283553](https://doi.org/10.1086/283553). Bibliographic data only.

<span id="ref-5"></span>5. Chesson P. Mechanisms of maintenance of species diversity. Annu Rev Ecol Syst. 2000;31:343–366. [doi:10.1146/annurev.ecolsys.31.1.343](https://doi.org/10.1146/annurev.ecolsys.31.1.343). Bibliographic data only.

<span id="ref-6"></span>6. Smith HL, Waltman P. The theory of the chemostat: dynamics of microbial competition. Cambridge: Cambridge University Press; 1995. [doi:10.1017/CBO9780511530043](https://doi.org/10.1017/CBO9780511530043). Bibliographic data and search summaries only; full text not checked.

<span id="ref-7"></span>7. Pandey PP, Jain S. Analytic derivation of bacterial growth laws from a simple model of intracellular chemical dynamics. Theory Biosci. 2016;135(3):121–130. [doi:10.1007/s12064-016-0227-9](https://doi.org/10.1007/s12064-016-0227-9). Bibliographic data only.

<span id="ref-8"></span>8. Yamagishi JF, Hatakeyama TS. Global constraint principle for microbial growth laws. Proc Natl Acad Sci U S A. 2025;122(40):e2515031122. [doi:10.1073/pnas.2515031122](https://doi.org/10.1073/pnas.2515031122). Open-access summary read; full text not checked. The concavity with respect to nutrient influx is as stated in the summary.

<span id="ref-9"></span>9. Nguyen J, Fernandez V, Pontrelli S, Sauer U, Ackermann M, Stocker R. A distinct growth physiology enhances bacterial growth under rapid nutrient fluctuations. Nat Commun. 2021;12:3662. [doi:10.1038/s41467-021-23439-8](https://doi.org/10.1038/s41467-021-23439-8). Abstract-level summary read; full text not checked.

<span id="ref-10"></span>10. Pascual M. Periodic response to periodic forcing of the Droop equations for phytoplankton growth. J Math Biol. 1994;32(8):743–759. [doi:10.1007/BF00168795](https://doi.org/10.1007/BF00168795). Bibliographic data only.

<span id="ref-11"></span>11. Python Software Foundation. Python [Software]. 2024. Version 3.12.4. Available from: [https://www.python.org/](https://www.python.org/)

<span id="ref-12"></span>12. Harris CR, Millman KJ, van der Walt SJ, Gommers R, Virtanen P, Cournapeau D, et al. Array programming with NumPy. Nature. 2020;585(7825):357–362. [doi:10.1038/s41586-020-2649-2](https://doi.org/10.1038/s41586-020-2649-2). Software: NumPy, version 2.2.6.

<span id="ref-13"></span>13. Virtanen P, Gommers R, Oliphant TE, Haberland M, Reddy T, Cournapeau D, et al. SciPy 1.0: fundamental algorithms for scientific computing in Python. Nat Methods. 2020;17(3):261–272. [doi:10.1038/s41592-019-0686-2](https://doi.org/10.1038/s41592-019-0686-2). Software: SciPy, version 1.14.0.

<span id="ref-14"></span>14. McKinney W. Data structures for statistical computing in Python. In: Proceedings of the 9th Python in Science Conference. 2010. p. 56–61. [doi:10.25080/Majora-92bf1922-00a](https://doi.org/10.25080/Majora-92bf1922-00a). Software: pandas, version 2.2.2.

<span id="ref-15"></span>15. Hunter JD. Matplotlib: a 2D graphics environment. Comput Sci Eng. 2007;9(3):90–95. [doi:10.1109/MCSE.2007.55](https://doi.org/10.1109/MCSE.2007.55). Software: Matplotlib, version 3.9.1.
