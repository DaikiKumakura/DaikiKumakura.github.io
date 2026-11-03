Reference date: the facts in this article are as of 3 November 2026.

If transcription were a Poisson process with a constant probability of firing, the variance of mRNA counts across single cells would equal the mean. Golding et al. counted mRNA one molecule at a time in living *Escherichia coli* and reported a variance about four times the mean ([1](#ref-1)). This note compares that observation with a transcriptional bursting model, derives the model's formulas, and checks them numerically against the measurements in the original paper. It then examines how much of the burst frequency, burst size and speed of mRNA loss can be identified from snapshots of a cell population, such as the mean and the variance.

## Problem formulation

There are two questions. (1) How does a transcriptional bursting model account for a variance about four times the mean? (2) Which of the burst frequency, burst size and speed of mRNA loss are determined by the mean and variance alone?

Notation and terms: \(n\) is the number of mRNA molecules in one cell, \(\langle n\rangle\) is its mean and \(\sigma^2\) its variance. Variance / mean (the Fano factor) is 1 for a Poisson distribution. P0(t) is the fraction of cells that have not yet made any mRNA at time \(t\) after induction. The inducer IPTG starts transcription of the reporter gene. MS2 is a protein that binds a specific RNA sequence; fused to GFP, it makes the RNA visible by fluorescence.

## The original measurements

Golding et al. tagged an RNA carrying MS2 binding sites with an MS2 protein fused to GFP. A single mRNA appears as one bright focus where 50–100 MS2-GFP molecules gather ([1](#ref-1)). After induction with IPTG, the mean transcript number approached a steady value (about 10 per cell) in about 100 minutes. The production rate obtained from the steady state was k1 = 0.14 ± 0.02 per minute (an estimate from the initial rise, about 0.10 per minute, is also reported), the loss rate was k2 = 0.014 ± 0.002 per minute, and the generation time was about 50 minutes ([1](#ref-1)). The tagged mRNA is stable; k2 was obtained from the approach of the mean to its steady value and agreed with the value computed from the generation time. k2 is therefore dilution at cell division approximated as a first-order loss ([1](#ref-1)).

This note uses three measurements from the paper.

- The steady-state variance / mean was 4.1 ± 0.5 (37 °C). Over a 100-fold range of induction, the variance stayed nearly proportional to the mean ([1](#ref-1)).
- After induction, P0(t) decreased exponentially. Its rate (0.032 ± 0.005 per minute) was about 4.4 ± 1.4 times smaller than k1 (37 °C). For a Poisson process, this rate would equal k1 ([1](#ref-1)).
- Direct time-lapse observation (22 °C, 20 cells, more than 77 transcription events) gave a mean inactive period of about 37 minutes, a mean active period of about 6 minutes, and a mean of about 2.2 mRNA molecules added per burst ([1](#ref-1)).

## Assumptions and definitions

Let bursts occur as a Poisson process with rate \(k_b\). Each burst adds \(B\) mRNA molecules at once, where \(B\) takes the values 1, 2, … with a geometric distribution of mean \(b\). \(b\) is the mean number added when a burst occurs, and k1 corresponds to the effective production rate including bursts (the product of \(k_b\) and \(b\)). Each molecule disappears independently at rate \(d\).

Switching of the gene between ON and OFF, together with Poisson-like transcription while ON, takes this burst form in the limit where ON periods are short and transcription during ON is fast. The paper states that, because the effective ON periods are relatively short, the process can be condensed approximately into this form ([1](#ref-1)). In the paper's measurements, however, the active period (about 6 minutes) and the inactive period (about 37 minutes) differ by only about six-fold, so the approximation is not exact.

## Derivation of the mean and variance

The mean and second moment of the model evolve as

\[
\frac{d\langle n\rangle}{dt}=k_b E[B]-d\langle n\rangle,\qquad
\frac{d\langle n^2\rangle}{dt}=k_b\left(E[B^2]+2E[B]\langle n\rangle\right)+d\left(\langle n\rangle-2\langle n^2\rangle\right)
\]

At steady state, \(\langle n\rangle = k_b E[B]/d\) and \(\sigma^2 = k_b\,(E[B^2]+E[B])/(2d)\). Therefore

\[
\frac{\sigma^2}{\langle n\rangle}=\frac{E[B^2]+E[B]}{2E[B]}.
\]

For a geometric distribution on 1, 2, …, \(E[B]=b\) and \(E[B^2]=2b^2-b\), so variance / mean equals \(b\). When \(b=1\) (no bursting), variance / mean is 1 and the Poisson distribution is recovered.

## Numerical check

I used the paper's measurements as inputs. With k1 = 0.14 per minute and k2 = 0.014 per minute (37 °C), the mean was fixed at 10, and the burst rate was set to \(k_b = k_1/b\) (so the mean is equal across the three models by construction). I compared three values of \(b\): 1 (Poisson), 2.2 (direct time-lapse observation) and 4.1 (variance / mean). The stationary distribution was obtained as the solution of a truncated master equation. Its mean and variance / mean agreed with theory (Table 2). A separate Gillespie simulation of 2,000 cells run to 3,000 minutes gave variance / mean of 2.25 ± 0.07 for \(b\)=2.2 and 4.19 ± 0.15 for \(b\)=4.1 (bootstrap standard errors), consistent with theory.

Table 1. Burst size \(b\) implied by the three measurements of the original paper ([1](#ref-1)). In the model, \(b\) equals variance / mean and also equals k1 divided by the early decay rate of P0(t) (the decay rate of P0(t) equals \(k_b\) at early times, when loss of mRNA is negligible). The ± values are as written in the paper; whether they are standard deviations or standard errors was not checked.

| Measurement | Value | Implied b |
| --- | ---: | ---: |
| Variance / mean at steady state (37 °C) | 4.1 ± 0.5 | 4.1 |
| k1 / decay rate of P0(t) (37 °C) | 4.4 ± 1.4 | 4.4 |
| Burst size from the time series (22 °C) | 2.2 | 2.2 |

The two 37 °C measurements agreed that \(b\) is about 4. In the model, for \(b\)=4.1 the early decay rate of P0(t) equals \(k_b\) = 0.034 per minute, close to the observed 0.032 ± 0.005 per minute. In contrast, \(b\)=2.2 obtained directly from the 22 °C time series did not agree with them. The paper notes that the four-fold effect in the 37 °C statistics is not identical to the 2–3-fold effect predicted from the 22 °C burst measurements and attributes the difference to the microscopy conditions ([1](#ref-1)). That explanation was not tested in the paper. The small number of observed cells (20) and events (more than 77), and the difference in temperature, also remain candidates. This note's calculation cannot close the gap.

With the same mean of 10, the distributions differ greatly with \(b\) (Figure 1, Table 2). For \(b\)=4.1, 1.1% of cells have no mRNA and 8.4% have 20 or more; for the Poisson distribution the figures are 0.0% and 0.35%.

![Figure 1. Steady-state distributions of mRNA counts at a fixed mean of 10 per cell: Poisson (b = 1), b = 2.2 from the time series, and b = 4.1 from variance / mean. Parameters are from the paper's measurements (k1 = 0.14 per minute, k2 = 0.014 per minute) ([1](#ref-1)).](shared/transcriptional-bursting-fano/figures/01-stationary-distributions.png)

Table 2. Stationary distributions of the three models (mean 10 per cell in all, k2 = 0.014 per minute). The b = 2.2 row combines a burst size measured at 22 °C with k1 and k2 at 37 °C; it is an illustration, not a prediction for 22 °C.

| Model | Burst rate k_b (per min) | Variance / mean | P(n = 0) | P(n ≥ 20) |
| --- | ---: | ---: | ---: | ---: |
| Poisson (b = 1) | 0.140 | 1.0 | 0.0000 | 0.0035 |
| b = 2.2 | 0.064 | 2.2 | 0.0014 | 0.037 |
| b = 4.1 | 0.034 | 4.1 | 0.0106 | 0.084 |

The time course in a single cell differs greatly between the models (Figure 2).

![Figure 2. Example time courses of mRNA counts in single cells (three cells each). Left: Poisson (b = 1). Right: b = 4.1. Random seeds fixed.](shared/transcriptional-bursting-fano/figures/02-example-time-courses.png)

## Limits of identification

The mean alone cannot distinguish the three models, because all have a mean of 10 (Table 2). Measuring the mean and variance / mean determines, within the model, \(b\) (variance / mean) and \(k_b/d\) (the mean divided by \(b\)). However, \(k_b\) and \(d\) are not determined separately. Multiplying \((k_b, d)\) by 3 leaves the stationary distribution unchanged (the maximum difference between the two distributions is \(1.4\times10^{-13}\)); even the whole stationary distribution cannot separate the two. Only the time course changes: the rate at which the first burst occurs goes from 0.034 to 0.102 per minute. The paper avoids this ambiguity by obtaining k2 from the approach of the mean to its steady value and checking it against the independently measured generation time, and by using the time course of P0(t) ([1](#ref-1)).

As interpretation, two cells of the same gene with different mRNA counts are not, on that evidence alone, in different states, because the moment at which cells are taken for a snapshot cuts through burst histories that differ from cell to cell (Figure 2).

## Scope

- The original work is in *E. coli*, with an inducible promoter and a reporter gene. Bursting from gene activation and inactivation has also been reported in mammalian cells ([2](#ref-2)). However, the numbers in this note are from *E. coli* and do not carry over directly to eukaryotic cells or endogenous genes.
- Burst sizes were assumed to follow a geometric distribution. For another distribution, variance / mean is not \(b\) but \((E[B^2]+E[B])/(2E[B])\), as the formula shows.
- This note's calculation checks consistency using the paper's reported values as inputs; it is not a reanalysis of the original data.
- The model does not include gene copy number changes over the cell cycle or cell size (the paper normalizes its measurements by cell size).
- The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

The observation that the variance of mRNA counts in single cells is about four times the mean was consistent with a transcriptional bursting model in which each burst adds about four mRNA molecules on average. In this model, variance / mean equals the burst size. The paper's two 37 °C measurements (variance / mean and the decay of P0(t)) agreed on \(b\) of about 4 but not with the 2.2 obtained directly from the 22 °C time series, and this note cannot identify the reason. Distributions differ greatly even at the same mean, and snapshots of the mean and variance cannot identify the burst frequency and the speed of mRNA loss separately.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive. Run with Python 3 (numpy, scipy, pandas, matplotlib): `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The random seed is 20261103. The inputs are published values from the original paper; no new measurement data were used.

The full re-run materials are in the [companion archive](shared/transcriptional-bursting-fano/transcriptional-bursting-fano-companion.zip).


## References

<span id="ref-1"></span>1. Golding I, Paulsson J, Zawilski SM, Cox EC. Real-time kinetics of gene activity in individual bacteria. Cell. 2005;123(6):1025–1036. [doi:10.1016/j.cell.2005.09.031](https://doi.org/10.1016/j.cell.2005.09.031)

<span id="ref-2"></span>2. Raj A, Peskin CS, Tranchina D, Vargas DY, Tyagi S. Stochastic mRNA synthesis in mammalian cells. PLoS Biol. 2006;4(10):e309. [doi:10.1371/journal.pbio.0040309](https://doi.org/10.1371/journal.pbio.0040309)
