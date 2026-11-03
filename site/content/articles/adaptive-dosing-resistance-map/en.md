Reference date: the facts in this article are as of 3 November 2026.

## Introduction

A review of colorectal cancer evolution lists, among evolution-informed strategies, tracking by liquid biopsy, molecular hyperselection and adaptive dosing, and states that both genetic and non-genetic mechanisms contribute to treatment resistance ([1](#ref-1)). I could read only the abstract and key points of the review; the full text is behind a subscription and was not read.

As a concrete example of adaptive dosing, a scheme in metastatic castration-resistant prostate cancer has been reported in which abiraterone is stopped when prostate-specific antigen (PSA) falls to 50% of the pre-treatment baseline and restarted when PSA returns to baseline. In a pilot trial of 11 patients, the median time to progression was at least 27 months and cumulative abiraterone use was about 47% of standard dosing, compared with 16 contemporaneous patients receiving standard care ([2](#ref-2)). These are results of a small pilot trial.

The idea that sensitive cells suppress resistant cells by competition underlies this report's model as the rationale for adaptive dosing ([2](#ref-2)). This note restates that idea in a minimal model and maps how much dosing with treatment breaks delays progression compared with continuous dosing across the way resistance arises (strength of competition, initial fraction of resistant cells, the drug effect that remains on resistant cells, and the cost of resistance), by scanning parameters. It is not a prediction for a specific cancer or drug.

## Methods

Competition between sensitive cells \(S\) and resistant cells \(R\) was described by the ordinary differential equations below. Time is dimensionless, in units of the inverse of the growth rate of sensitive cells, and the carrying capacity of the environment is 1.

\[
\frac{dS}{dt}=S\,(1-S-R)-k_{\max}\,S\,u,\qquad
\frac{dR}{dt}=(1-c)\,R\,(1-aS-R)-\rho\,k_{\max}\,R\,u
\]

\(u\) is 1 on treatment and 0 off treatment. \(k_{\max}\) is the maximal drug effect, fixed at 2. Pharmacokinetics is not included (the drug has a constant effect while given). The parameters are:

- \(c\): reduction of the resistant cells' growth rate without drug (cost of resistance).
- \(a\): strength of suppression of resistant cells by sensitive cells (competition coefficient). The effect of resistant cells on sensitive cells was fixed at 1, so \(a>1\) means that sensitive cells suppress resistant cells more strongly than resistant cells suppress sensitive cells.
- \(\rho\): the fraction of the drug effect that remains on resistant cells (0 for full resistance, 1 for no resistance).
- \(f_0\): initial fraction of resistant cells. The initial total burden \(N_0=S+R\) was 0.5 of the carrying capacity.

Continuous dosing treats until progression. Adaptive dosing stops treatment when the total burden \(N\) has fallen to \(0.5N_0\) and restarts when it returns to \(N_0\) (the same rule as in the prostate cancer report ([2](#ref-2))). Progression was defined as \(N\) reaching \(1.2N_0\). The outcomes are the time to progression and the ratio (adaptive / continuous). The observation horizon was 600 (dimensionless time); if no progression occurred by then, the time was censored and the ratio is shown as a lower bound, namely the horizon divided by the time to progression under continuous dosing.

The baseline condition was \(c=0.2\), \(a=1.5\), \(\rho=0\), \(f_0=0.01\). Three scans were run: \(a\) (0.5, 1.0, 1.5, 2.0, 3.0) against \(f_0\) (0.001, 0.01, 0.05, 0.1, 0.2, 0.4); \(\rho\) (0, 0.05, 0.1, 0.15, 0.2) against \(a\); and \(c\) (0, 0.2, 0.4, 0.6) against \(a\). The parameters are not measured values. No random numbers were used; the equations were solved by numerical integration with event detection (SciPy `solve_ivp`, relative tolerance \(10^{-9}\), absolute tolerance \(10^{-12}\)). In addition, a sensitivity analysis varying the stop level (0.3, 0.5, 0.7) and the progression criterion (1.1, 1.2, 1.5) was run for five representative conditions.

## Results

At baseline, the time to progression was 7.73 with continuous dosing and 11.99 with adaptive dosing (ratio 1.55) (Figure 1). Under continuous dosing, the sensitive cells disappear and the resistant cells then grow alone and cause progression. Under adaptive dosing, sensitive cells regrow at each treatment break, and the total burden oscillates between \(0.5N_0\) and \(N_0\). Meanwhile the resistant cells increase gradually and eventually cause progression.

![Figure 1. Time courses at the baseline condition (c = 0.2, a = 1.5, rho = 0, initial resistant fraction 0.01). Left: continuous dosing. Right: adaptive dosing (stop when the total burden falls to 0.5 N0, restart when it returns to N0). Dotted line: the progression criterion (1.2 N0).](shared/adaptive-dosing-resistance-map/figures/01-example-time-courses.png)

The stronger the suppression by sensitive cells, the larger the benefit of adaptive dosing (Figure 2, left). At \(f_0=0.01\), the ratio was 1.11 for \(a\)=0.5, 1.29 for 1.0, 1.55 for 1.5 and 2.17 for 2.0. At \(a\)=3, adaptive dosing did not reach progression by the horizon (600), and the ratio was at least 72 (a lower bound). This lower bound is set by the observation horizon and does not express an effect size. The larger the initial resistant fraction, the smaller the benefit. At \(a\)=1.0, the ratio was 1.37 for \(f_0\)=0.001, 1.11 for 0.1, and 1.00 (no difference) for 0.2 and above. At \(f_0\)=0.2 and above, the total burden does not fall to the stop level (\(0.5N_0\)), no treatment break occurs, and the two regimens are identical.

![Figure 2. Maps of the ratio of time to progression (adaptive / continuous). Left: strength of suppression of resistant cells by sensitive cells, a, against the initial resistant fraction. Right: the fraction of drug effect remaining on resistant cells, rho, against a (initial resistant fraction 0.01). The colour is the common logarithm of the ratio. ">" means the adaptive arm did not reach progression by the horizon and the ratio is a lower bound; "none" means neither arm progressed.](shared/adaptive-dosing-resistance-map/figures/02-ratio-maps.png)

When part of the drug effect remains on resistant cells, the benefit shrinks and in some conditions turns into a disadvantage (Figure 2, right). At \(a\)=0.5, the ratio was 1.11 for \(\rho\)=0, 1.05 for 0.05, 0.98 for 0.10 and 0.93 for 0.15. At \(\rho\)=0.2, the drug kept suppressing the growth of resistant cells (the equilibrium of resistant cells under drug is \(1-\rho k_{\max}/(1-c)=0.5\), below the progression criterion of 0.6), and neither dosing approach progressed by the horizon. The equilibrium at \(\rho\)=0.15 is 0.625, just above the criterion, so the ratios in this column are sensitive to the criterion. For \(a\) of 1.0 and above, the ratio exceeded 1 for every \(\rho\) up to 0.15.

The effect of the cost of resistance was small (Table 1). For \(a\)=0.5–2, the ratio changed by only about 0.03–0.2 when \(c\) changed from 0 to 0.6. For \(a\)=3, the lower bound of the ratio decreased as the cost increased, because the time to progression under continuous dosing lengthens with the cost.

Table 1. Ratio of time to progression (adaptive / continuous) by \(c\) and \(a\) (\(\rho\)=0, \(f_0\)=0.01). ">" marks a lower bound where adaptive dosing did not reach progression by the horizon.

| Cost c | a = 0.5 | a = 1.0 | a = 1.5 | a = 2.0 | a = 3.0 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0.0 | 1.09 | 1.26 | 1.53 | 2.07 | >86.8 |
| 0.2 | 1.11 | 1.29 | 1.55 | 2.17 | >72.0 |
| 0.4 | 1.11 | 1.29 | 1.60 | 2.15 | >56.0 |
| 0.6 | 1.12 | 1.32 | 1.60 | 2.26 | >38.8 |

In the threshold sensitivity analysis, with the stop level varied from 0.3 to 0.7 and the progression criterion from 1.1 to 1.2, the ordering (the larger \(a\), the larger the benefit) and the disadvantage at \(\rho\)=0.15 and \(a\)=0.5 (ratio 0.88–0.94) were retained. The "no progression" at \(a\)=3 became a finite value (ratio about 3.0) when the stop level was 0.3. With a progression criterion of 1.5, neither regimen progressed by the horizon in the partial-resistance conditions.

## Discussion

In this model, the benefit of adaptive dosing was determined mainly by three things: strong suppression of resistant cells by sensitive cells (large \(a\)), a small initial resistant fraction, and a drug with no effect on resistant cells (\(\rho\)=0). The cost of resistance had little effect in this formulation. \(c\) multiplies the whole growth term of resistant cells and acts in the same way in both regimens, so it tends to cancel in the ratio. There may be models in which the cost matters; this note did not examine them.

What is already known and what this scan adds should be separated. That competition among sensitive cells is the rationale for adaptive dosing is assumed by the model of the prostate cancer report ([2](#ref-2)). What this note showed is that, in this minimal model, the benefit varies greatly with \(a\) and the initial resistant fraction and is concentrated on the side of \(a>1\), and that when the drug partly acts on resistant cells (\(\rho\) of 0.10–0.15 with \(a\)=0.5) the benefit disappears and turns into a slight disadvantage. The size of the disadvantage stays within 0.88–0.94 across the thresholds tested, so it is not large.

Interpretation: adaptive dosing works as a strategy that keeps a population of sensitive cells during treatment breaks and uses their competition to suppress resistant cells. When suppression is weak or resistant cells are already abundant, the preserved sensitive cells cannot hold resistant cells in check and there is almost no benefit. When the drug partly acts on resistant cells, the treatment break stops that treatment, so the benefit shrinks. This note's model, however, does not reproduce the prostate cancer report.

This is not a result for colorectal cancer. Non-genetic resistance (such as drug-tolerant persister states) and polyclonal resistance, which the review discusses, are not in this model, and the full text of the review was not read.

## Limitations

- The parameters are not measured values. Time is dimensionless and cannot be converted to months. \(k_{\max}\) (2), the range of \(\rho\) (0–0.2) and the initial total burden (0.5) are fixed or limited, and were not validated with values for an actual drug.
- Pharmacokinetics, pharmacodynamics (dose–response), between-patient variability, stochastic extinction, spatial structure and measurement error in tumor burden from imaging or blood markers are not included.
- The stop and restart rule (0.5 N0 and N0), the definition of progression (1.2 N0) and the observation horizon are assumptions. The sensitivity analysis covers only five representative conditions, and with a progression criterion of 1.5 the conclusion changes (neither regimen progresses).
- The competition coefficient \(a\) was scanned in one direction only (sensitive cells suppressing resistant cells); the opposite effect was fixed.
- The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

In a sensitive–resistant competition model, how much adaptive dosing delays progression compared with continuous dosing varied greatly with the strength of suppression of resistant cells by sensitive cells, the initial resistant fraction, and the effect the drug retains on resistant cells. The benefit was large when suppression was strong, resistant cells were few and the drug had no effect on resistant cells; it was small when suppression was weak, and in some conditions where the drug partly acted on resistant cells it turned into a slight disadvantage. The cost of resistance had little effect in this formulation. This map organizes conditions; it does not show clinical efficacy for a specific cancer or drug.

## Data and code availability

The calculation code (`analysis.py`, `sensitivity.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive. Run with Python 3.12, NumPy 2.2, SciPy 1.14, pandas 2.2 and Matplotlib 3.9: `python analysis.py`, `python sensitivity.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The calculation is deterministic and uses no random numbers. Outputs are written as CSV files in `results/`. The inputs are assumed parameters; no data were used.

The full re-run materials are in the [companion archive](shared/adaptive-dosing-resistance-map/adaptive-dosing-resistance-map-companion.zip).


## References

<span id="ref-1"></span>1. Sng CCT, Starling N, et al. The genomic and epigenomic evolution of colorectal cancer. Nat Rev Gastroenterol Hepatol. 2026 Nov 2 [cited 2026 Nov 3]. [doi:10.1038/s41575-026-01265-x](https://doi.org/10.1038/s41575-026-01265-x). Abstract and key points read; full text not read.

<span id="ref-2"></span>2. Zhang J, Cunningham JJ, Brown JS, Gatenby RA. Integrating evolutionary dynamics into treatment of metastatic castrate-resistant prostate cancer. Nat Commun. 2017;8:1816. [doi:10.1038/s41467-017-01968-5](https://doi.org/10.1038/s41467-017-01968-5)
