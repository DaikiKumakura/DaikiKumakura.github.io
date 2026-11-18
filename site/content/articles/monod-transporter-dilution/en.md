Growth rates saturate when transporters approach saturation at a fixed substrate concentration. The Monod equation describes this shape ([1](#ref-1)). However, dividing occupied transporter by biomass introduces an additional loss term as biomass increases. The [note on periodic supply](periodic-supply-monod-growth-en.html) took the equation with this term as its starting point. Here the reaction model supplies its derivation and indicates when the term can be dropped.

## The dilution term in transporter occupancy

Let $S$ be external substrate, $X$ biomass, $eX$ total transporter and $C$ occupied transporter, with amounts per culture volume and transporter abundance $e$ per unit biomass. Transporter synthesis adds free transporter. With binding rate $aS$, combined dissociation and processing rate $b$, and common culture dilution rate $D$, the occupied pool satisfies $C'=aS(eX-C)-(b+D)C$. With processing rate $k_c$ and yield $Y$, let $X'=(Yk_c C/X-D)X$. Synthesizing total transporter at rate $eYk_c C$ preserves the constraint $eX$.

Set $u=Yk_c C/X$ and $L=Yk_c e$. The quotient rule gives $u'=aS(L-u)-bu-u^2$. Culture dilution $D$ cancels, while growth dilution contributes $u^2$. At constant $S>0$, denote the positive equilibrium specific growth rate before culture dilution by $u_*$. Dropping the quadratic term gives the Monod approximation $v=LaS/(aS+b)$. The equilibrium equation gives $v-u_*=u_*^2/(aS+b)$, so the relative error with the Monod value as denominator, $(v-u_*)/v$, is $u_* /(aS+b+u_*)$.

**Table 1.** Examples at $L=4$. Rates are per hour.

| Binding rate | Exit rate | Monod approximation | Equilibrium rate | Relative error |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 2.000 | 1.236 | 38.2% |
| 1 | 10 | 0.364 | 0.352 | 3.1% |
| 10 | 10 | 2.000 | 1.832 | 8.4% |

Writing the relative error as $E$, the equilibrium equation gives $E/(1-E)^2=LaS/(aS+b)^2$. The right-hand side reaches its maximum $L/(4b)$ at $aS=b$. The exact criterion for at most 5% relative error at every constant substrate concentration is therefore $b/L\geq361/80$, about 4.51. At $S=0$ both rates are zero and the absolute error is zero. In Table 1 the gap is 38.2% of the Monod value at $aS=1,b=1$, and 3.1% at the same $aS$ with $b=10$. This is the equilibrium approximation error at fixed substrate. It does not describe how quickly a system follows a change in substrate or quantify error for a measured strain.

## Data and code availability

The [reproducibility ZIP](shared/monod-transporter-dilution/companion.zip) contains the Python code and output.

## References

1. <a id="ref-1"></a> [Monod J. The growth of bacterial cultures. Annu Rev Microbiol. 1949;3:371–394.](https://doi.org/10.1146/annurev.mi.03.100149.002103)
