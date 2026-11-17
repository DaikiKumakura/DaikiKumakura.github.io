A long terminal phase after an oral dose can reflect slow elimination or slow entry from the formulation. Would more concentration measurements tell them apart? In a one-compartment model with first-order absorption and elimination, two explanations can produce exactly the same curve even without measurement noise ([1](#ref-1)).

## Swapping the two rates leaves the oral curve unchanged

Write apparent volume as $v=V/F$ when absolute bioavailability $F$, the fraction reaching systemic circulation, is unknown. Let $D$ denote dose, $a$ the absorption rate constant and $k$ the elimination rate constant. For $a\ne k$, concentration is

$$C(t)=\frac{Da}{v(a-k)}\left(e^{-kt}-e^{-at}\right).$$

Swap $a$ and $k$ and replace $v$ with $vk/a$. Both the coefficient and the bracket change sign, preserving the product. I checked this at 100 mg using pair A $(a,k,v)=(1.0,0.2,40)$ and pair B $(0.2,1.0,8)$, with rates in h⁻¹ and volume in L. Pair B is the flip-flop case, with absorption slower than elimination. Apparent clearance is 8 L/h for both. Under linear superposition, the same formulation gives equal curves for any set of dose amounts and times. Additional oral samples do not break the symmetry.

## Changing only the absorption rate

I set absorption to 1.2 h⁻¹ in both models and left the other parameters, including $F$, fixed. In Table 1 the AUC to infinity remains equal, while pair B gives a peak about 2.9 times as high as pair A. This intervention assumes the new absorption rate is known and shared by both models.

**Table 1.** Calculated values after a single 100 mg dose.

| Scenario | Tmax (h) | Cmax (mg/L) | Concentration at 8 h (mg/L) | AUC to infinity (mg·h/L) |
| --- | ---: | ---: | ---: | ---: |
| Original A or B | 2.012 | 1.672 | 0.630 | 12.500 |
| Faster absorption A | 1.792 | 1.747 | 0.605 | 12.500 |
| Faster absorption B | 0.912 | 5.023 | 0.020 | 12.500 |

Predicting an intervention on absorption alone requires evidence identifying the elimination mode. For instance, after an intravenous dose under the same linear one-compartment model, the decline in concentration provides information on $k$ without oral absorption. This example assumes linearity, one first-order absorption route and an apparent volume that can differ between parameterizations. It does not address between-patient variability or multiple absorption routes.

## Data and code availability

The parameters are hypothetical. The Python code in the [companion ZIP](shared/oral-pk-flip-flop-formulation/companion.zip) reproduces Table 1.

## References

1. <a id="ref-1"></a> Kuan IHS, Wright DFB, Duffull SB. The influence of flip-flop in population pharmacokinetic analyses. CPT Pharmacometrics Syst Pharmacol. 2023;12(3):285–287. [doi:10.1002/psp4.12909](https://doi.org/10.1002/psp4.12909).
