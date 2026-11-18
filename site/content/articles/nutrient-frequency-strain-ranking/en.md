Even with the same mean and amplitude, more rapid nutrient fluctuations make an intracellular state harder to track. Bacterial experiments under rapidly fluctuating nutrients reported growth physiology distinct from constant conditions ([1](#ref-1)). I compare a fast-tracking strain that pays more for a mismatch with a slower strain that pays less.

## Change frequency while fixing the input distribution

Let the normalized nutrient response be $h(t)=0.5+0.25\cos(\omega t)$ and the intracellular state satisfy $\tau m'=h-m$. Biomass $X$ follows $X'=[h-c(m-h)^2]X$, where the leading gain on $h$ is $1$ per hour, $c$ is per hour, angular frequency $\omega$ is in radians per hour and relaxation time $\tau$ is in hours. At periodic steady state the sinusoidal component is multiplied by $1/(1+i\omega\tau)$. The squared amplitude of the residual divided by two gives the cycle mean mismatch $0.25^2(\omega\tau)^2/[2(1+(\omega\tau)^2)]$.

For strain 1 take $(c,\tau)=(4,0.25)$ and for strain 2 $(1,1)$. At low frequency, the penalty scales with $c\tau^2$ and strain 1 grows faster. At high frequency, the penalty is controlled by $c$ and strain 2 grows faster. The only positive solution equating the penalties is $\omega=2$ rad/h. Table 1 shows the crossing and a frequency on either side. Fourth-order Runge–Kutta integration over the last simulated cycle independently reproduced the mean squared mismatch to within $10^{-6}$.

**Table 1.** Long-run mean specific growth rates, per hour, with normalized input.

| Angular frequency | Strain 1 | Strain 2 |
| ---: | ---: | ---: |
| 0.5 | 0.4981 | 0.4938 |
| 2.0 | 0.4750 | 0.4750 |
| 8.0 | 0.4000 | 0.4692 |

Only time is rescaled, so the distribution of the input over a cycle stays the same. The reversal concerns strains growing separately under the prescribed input. It provides no estimate for competition over shared substrate or ranking of the strains in the published experiments.

## Data and code availability

The [reproducibility ZIP](shared/nutrient-frequency-strain-ranking/companion.zip) contains the Python code and output.

## References

1. <a id="ref-1"></a> [Nguyen J, Fernandez V, Pontrelli S, Sauer U, Ackermann M, Stocker R. A distinct growth physiology enhances bacterial growth under rapid nutrient fluctuations. Nat Commun. 2021;12:3662.](https://doi.org/10.1038/s41467-021-23439-8)
