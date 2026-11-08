Three years after one dose sounds like durable pharmacology. But three years of what: target-protein reduction, lipid lowering or prevention of cardiovascular events? These cannot be assigned the same duration without corresponding observations.

A study released early on November 6, 2026 targets the gene encoding angiopoietin-like 3 (ANGPTL3) protein with base editing. The authors report sustained circulating ANGPTL3 protein reduction in nonhuman primates out to three years after one dose [(1)](#ref-1). Its interpretation requires separating persistence of the administered material from persistence of the biological state it changes.

## Scope and sources

This article uses the public abstract of the peer-reviewed, accepted early-release article and the sponsor's Pulse-1 description. Dose-specific figures, individual trajectories and detailed safety materials were not available within this review. No reduction rates were reestimated and no quantitative animal-to-human projection was made.

The sponsor describes Pulse-1 as a phase 1b study of VERVE-201 [(2)](#ref-2). The existence of that trial does not establish long-term human benefit.

## Three different clocks

One clock concerns the components delivered to cause editing. Another concerns the altered gene state and resulting protein production. A third concerns downstream lipid metabolism and clinical outcomes.

One half-life cannot describe them all. If production remains altered after delivered components disappear, protein abundance need not recover. Conversely, persistent protein reduction does not establish equally persistent or proportionate lipid lowering. Linking the time courses requires observations of each relationship.

The abbreviated phrase “works for three years” removes those links. In the abstract, the explicit long-term durability claim concerns circulating ANGPTL3 protein [(1)](#ref-1). It should not be silently extended to equally long lipid or event follow-up.

## Changing production changes the pharmacodynamic clock

Consider a minimal model of target-protein amount \(P(t)\). Before treatment, production \(k_{\mathrm{syn}}\) balances first-order degradation \(k_{\mathrm{deg}}\), giving \(P_0=k_{\mathrm{syn}}/k_{\mathrm{deg}}\).

Assume production changes to a fraction \(r\) of baseline at time zero and remains at that level throughout the modeled period:

\[
\frac{dP}{dt}=r k_{\mathrm{syn}}-k_{\mathrm{deg}}P,\qquad
\frac{P(t)}{P_0}=r+(1-r)e^{-k_{\mathrm{deg}}t}.
\]

Protein amount uses arbitrary units; \(k_{\mathrm{syn}}\) has amount-per-time units, \(k_{\mathrm{deg}}\) inverse-time units and \(r\) is dimensionless. Time begins when production changes. The model omits any delay between administration and editing.

For an artificial example, set \(r=0.1\) and express time in protein half-lives, \(\log(2)/k_{\mathrm{deg}}\). Table 1 is not fitted to the study and does not estimate human or animal half-lives.

Table 1. Artificial protein kinetics after a persistent reduction of production to 10%.

| Protein half-lives elapsed | Production fraction | Protein / baseline |
| ---: | ---: | ---: |
| 0 | 0.10 | 1.000 |
| 1 | 0.10 | 0.550 |
| 3 | 0.10 | 0.213 |
| 5 | 0.10 | 0.128 |

Even instantaneous alteration of production does not produce an instantaneous protein steady state. Turnover determines the initial decline; persistence subsequently depends on whether \(r\) remains changed. The equation does not require a long circulating half-life of the delivered components.

Nor does a 90% production reduction mean that 90% of cells were edited. With unequal production or editing states across cells, the fraction of cells and the fraction of population-level production are different quantities. Inferring an edited-cell fraction directly from circulating protein reduction requires additional assumptions.

## Persistence can contribute to both benefit and burden

A persistent production change could reduce dependence on daily dosing. It also differs from an intervention whose effect rapidly disappears when administration stops. Persistence alone does not establish clinical value; the question is whether the effect persists within a desirable range.

Following target protein and following clinical events answer different questions. The first tests sustained target action. The second tests benefit in a defined population under its concomitant care. Animal evidence for the former cannot quantify human benefit for the latter.

Duration alone also does not establish the ability to detect rare adverse events. Sample size, attrition and the measurements performed matter. The sources reviewed here do not support a comprehensive safety conclusion, including one about off-target effects.

## Conclusion

The ANGPTL3 follow-up informs sustained target action that dose count alone cannot describe. Removing the measured endpoint and species, however, turns it into an unsupported claim of three years of clinical efficacy after one treatment.

If altered production persists, the model can explain target action continuing beyond residence of the delivered components. The three-year figure in this study should likewise be read as the observed duration of target-protein reduction, not as the half-life of the administered components.

## Data and code availability

Table 1 is in `protein_turnover` in the [script](shared/angptl3-duration/reproduce.py) and [output](shared/angptl3-duration/illustration.json). It is a deterministic illustration without empirical input, not a dose recommendation or human efficacy model.

[Download code and results](shared/angptl3-duration/angptl3-duration.zip).

## References

1. <a id="ref-1"></a> Mizoguchi T, DeNizio JE, Chadwick AC, Mazzola AM, Brown MP, Mishra S, et al. In Vivo CRISPR Base Editing of ANGPTL3 for Durable Lipid Lowering. Nature. 2026 Nov 6. Accepted article, early release. [https://doi.org/10.1038/s41586-026-11233-9](https://doi.org/10.1038/s41586-026-11233-9).

2. <a id="ref-2"></a> Verve Therapeutics. Pulse-1 [Internet]. Verve Clinical Trials [cited 2026 Nov 8]. [Study sponsor's description](https://verveclinicaltrials.com/pulse-1/).
