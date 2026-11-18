In a model where cells consume substrate and are inhibited by accumulated metabolites, dense biomass sampling need not establish the concentration scale of the medium. I used a three-state model of allocation between growth and detoxification ([1](#ref-1)), with optional constant substrate feed, to find parameter changes that preserve the biomass trajectory.

The [Kumakura-Lite article](kumakura-lite-model-reduction-en.html) reduced the same three-state model. Here all three states remain and the question is which trajectories the observations can distinguish.

## Concentrations can scale while biomass stays fixed

Let $N$ denote biomass and $R,M$ substrate and metabolite concentrations. Allocation is $p=R/(R+M+h)$ and carrying capacity is $K(M)=K_0+(K_1-K_0)e^{-fM}$. Biomass follows $N'=\mu a_1RNp(1-N/K(M))-dN$. The other equations are $R'=\lambda-a_1RNp-b_1RN(1-p)$ and $M'=a_2RNp+b_2RN(1-p)-cMN(1-p)$. Here $\lambda$ is substrate feed per unit time and $d$ is the biomass loss rate.

Multiply $R,M,h,\lambda$ and initial $R,M$ by a positive factor $k$, and divide $\mu,f$ by $k$. The allocation and products $fM,\mu R$ are unchanged. The right-hand side for $N$ stays fixed and the other two scale by $k$. With the same initial biomass and uniqueness of solutions in the relevant domain, both systems produce the same $N(t)$ at all times. Denser biomass measurements cannot distinguish this family.

**Table 1.** Dimensionless example at time 20 with $k=3$. Fourth-order Runge–Kutta, step 0.01.

| System | Biomass | Substrate | Metabolite |
| --- | ---: | ---: | ---: |
| Original | 2.897 | 0.691 | 0.268 |
| Rescaled | 2.897 | 2.074 | 0.805 |

Across all time points in the comparison behind Table 1, the biomass discrepancy was below $2.3\times10^{-15}$. This checks the algebraic symmetry and does not represent measurement precision. A known nonzero initial substrate concentration or an independently calibrated positive concentration at one time can fix this scale factor. Other equivalences could remain, so a single measurement is insufficient to establish identifiability of all parameters.

## Data and code availability

The [reproducibility ZIP](shared/microbial-growth-concentration-scale/companion.zip) contains the Python code and output.

## References

1. <a id="ref-1"></a> [Kumakura D, Yamaguchi R, Hara A, Nakaoka S. Disentangling the growth curve of microbial culture. J Theor Biol. 2023;573:111597.](https://doi.org/10.1016/j.jtbi.2023.111597)
