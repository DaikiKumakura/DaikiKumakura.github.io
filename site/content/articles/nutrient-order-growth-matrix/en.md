If cells spend the same amount of time in each of two nutrient conditions, does grouping the exposures rather than alternating them change long-run growth? Experiments have measured bacterial growth under rapid nutrient fluctuations ([1](#ref-1)). I varied the order in a two-phenotype model with finite switching and a different growth advantage in each condition.

## Matrix products separate the two orders

Use a vector for the two phenotype abundances. They interconvert at 0.1 per hour in each direction. Growth rates before switching are 1 and 0 per hour in condition A and reversed in B. Subtracting the outgoing switch rate gives diagonals $(0.9,-0.1)$ and off-diagonals 0.1 for A, with the diagonals reversed for B. Let $U,V$ be the corresponding propagators for a block of length $\Delta$. AABB has propagator $V^2U^2$ and ABAB has $(VU)^2$. In both cases the long-run rate is the log of the largest eigenvalue divided by the cycle length $4\Delta$.

The determinants are equal. The trace difference is $\mathrm{tr}(V^2U^2)-\mathrm{tr}(VUVU)=-\mathrm{tr}((VU-UV)^2)/2$. Since $U,V$ are symmetric, their commutator $VU-UV$ is skew-symmetric. The difference is half the sum of squared entries of the commutator. A nonzero commutator makes the grouped cycle grow faster because the largest eigenvalue of these positive two-by-two matrices increases with trace when the determinant is fixed. In this example the commutator is nonzero for every $\Delta>0$. Each generator has distinct real eigenvalues, so its exponential is a linear combination of the identity and the generator with a positive coefficient on the generator. The generators themselves do not commute. As a control, AB and BA have the same eigenvalues since changing between them only moves the cycle origin.

**Table 1.** Block duration and long-run growth rates per hour.

| Block duration (h) | AABB | ABAB |
| ---: | ---: | ---: |
| 0.25 | 0.5010 | 0.5003 |
| 1.00 | 0.5172 | 0.5042 |
| 3.00 | 0.6469 | 0.5397 |

For one-hour blocks, Table 1 gives 0.5172 for AABB and 0.5042 for ABAB. The comparison fixes time in each external condition. It includes neither substrate depletion nor competition. The trace argument does not directly extend to nonsymmetric propagators.

## Data and code availability

The [reproducibility ZIP](shared/nutrient-order-growth-matrix/companion.zip) contains the Python code and output.

## References

1. <a id="ref-1"></a> [Nguyen J, Fernandez V, Pontrelli S, Sauer U, Ackermann M, Stocker R. A distinct growth physiology enhances bacterial growth under rapid nutrient fluctuations. Nat Commun. 2021;12:3662.](https://doi.org/10.1038/s41467-021-23439-8)
