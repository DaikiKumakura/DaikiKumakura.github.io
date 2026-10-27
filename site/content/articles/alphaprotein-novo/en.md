## Abstract {#article-abstract}

AlphaProtein Novo combines catalytic motifs, protein generation and reaction-specific structural filters to select enzymes for experiments. The preprint and official implementation were examined, with reference Wilson intervals recalculated from two reported counts. The intervals concern different reactions and success definitions and cannot compare method performance. Multiple prediction seeds and redesigned sequences assess computational consistency, not experimental success probabilities. Reported activity and the performance of candidate selection require distinct interpretation.

## Introduction {#article-introduction}

If AI can design enzymes, does specifying a desired reaction deliver a catalyst? AlphaProtein Novo exposes the work between those steps: hypothesizing reactive atomic arrangements, generating candidates and selecting which predicted structures to test. Its selection procedure is also refined in response to experiments.

The study uses reaction-informed metrics to narrow experimental candidates, rather than treating structure prediction as activity itself. A favorable structural score still supplies neither a reaction rate nor a success probability. The candidate population, success definition and number selected matter.

## Scope and sources {#article-scope}

This examination uses preprint v1, released October 5, 2026 ([1](#ref-1)), and the official implementation ([2](#ref-2)). The paper has not been peer reviewed. I neither executed the model nor measured enzymes. Calculations below interpret published counts and an explicitly hypothetical example.

## Mechanistic assumptions as design inputs {#_1}

Enzymes catalyze reactions as well as bind substrates. A substrate is the molecule intended to react; catalytic residues are amino acids participating in catalysis. Which atoms approach one another and which intermediates are stabilized are consequential assumptions.

The implementation accepts a motif specifying three-dimensional arrangements of catalytic residues and ligands. Here ligands include substrates, intermediates or other molecules interacting with the protein. Transition-state analogues or reaction intermediates supply arrangements around which proteins are generated. Partial atom constraints and partial diffusion that modifies existing designs are available.

The serine-esterase example includes the Ser–His–Asp catalytic triad and hydrogen-bond arrangements stabilizing a reaction intermediate. Some motifs come from natural-enzyme crystal structures. De novo design here therefore combines new scaffolds with established chemical knowledge.

The broad workflow supplies a motif, generates structure and sequence, uses LigandMPNN to redesign sequences on a scaffold, predicts structures with AlphaFold 3 (AF3), calculates metrics and tests candidates. A scaffold is the protein framework supporting catalytic geometry; LigandMPNN designs amino-acid sequences compatible with a structure. Downstream structural scores do not validate the input motif's chemistry.

## Structural confidence and catalytic geometry {#_2}

Confidence metrics such as pLDDT describe a model's confidence in its predicted structure. Selecting a catalyst also requires inspecting local arrangements involved in the reaction.

The implementation changes the states and geometric metrics evaluated for each reaction.

**Table 1. Predicted properties and experimental measurements by reaction**

| Reaction | Evaluated in predictions | Evaluated experimentally |
| --- | --- | --- |
| Kemp elimination | Catalytic base and transition-state-analogue geometry | Activity and kinetic parameters |
| Ester hydrolysis | Catalytic-triad interactions and consistency between substrate-bound and intermediate geometries | Hydrolysis activity and substrate-dependent rates |
| Nitrene transfer | Heme/substrate geometry and distances between bond-forming atoms | Product yield, ring-size selectivity and enantioselectivity |

Predicting a substrate-bound state well does not establish a viable catalytic arrangement if intermediate geometry changes substantially. Multiple states are therefore evaluated. Comparing static predicted states is still different from dynamically calculating a reaction pathway.

For example, `piperidine_propensity` is the distance from nitrogen to the carbon for six-membered-ring formation minus the distance to the carbon for five-membered-ring formation:

\[
D=d(N,C_{\mathrm{PIP}})-d(N,C_{\mathrm{PYR}}).
\]

It is negative when the six-membered-ring side is relatively closer. Despite “propensity” in its name, its unit is Å, not probability. Distances of 2.5 and 3.5 Å give −1.0 Å, but the metric contains no conversion from that value to a product ratio. The [distance implementation](https://github.com/google-deepmind/alphaprotein-novo/blob/e7ce276cb4a1f68c2ba7d5aa793192cfcb4845c8/src/alphaprotein_novo/metrics/nitrene_metrics.py) makes this distinction explicit ([2](#ref-2)).

## Consistency across redesigned sequences {#_3}

Selection goes beyond scoring one predicted structure. Multi-seed evaluation varies prediction seeds; multi-resequence (MR) designs multiple sequences on the same scaffold.

Each sequence undergoes structure prediction and filtering. The number passing indicates how consistently the scaffold supports the geometry across redesigned sequences, rather than only for one fortunate sequence. The authors interpret this as scaffold evaluation.

AF3 seeds are not experimental replicates, and redesigned sequences are not independent samples of natural enzymes. A pass count of 8/10 does not mean an 80% probability of activity after synthesis. Predictions sharing a model and motif can share errors.

The study includes retrospective filtering of experimentally tested candidates and prospective selection of new designs with improved filters. That prospective component matters for judging selection utility. The [original Figure 4 and main text](https://www.biorxiv.org/content/10.64898/2026.10.01.756017v1.full) distinguish these stages ([1](#ref-1)).

## Reported counts and illustrative recalculation {#_4}

Hit rates in [original Table 1](https://www.biorxiv.org/content/10.64898/2026.10.01.756017v1) are not success rates over every generated candidate ([1](#ref-1)). Experimentally tested candidates are grouped into facets generated under common pipeline settings, and the best facet is reported. Reaction-specific hit definitions also prevent direct comparison of the rates.

Stricter filtering can leave few candidates. A retrospective serine-esterase analysis reports five hits among nine designs after stringent seed and resequencing filters. A hit shows multiple-turnover kinetics and \(k_{\mathrm{obs}}>0.003\ \mathrm{s}^{-1}\) at 100 µM 4MU-Ac. Here \(k_{\mathrm{obs}}\) is product formation per enzyme amount at a fixed substrate concentration. In contrast, five of 90 novel-scaffold Kemp designs in the final round exceeded the stricter \(k_{\mathrm{obs}}>1.0\ \mathrm{s}^{-1}\) criterion.

These counts concern different reactions and success conditions; they are not a performance comparison. They can nevertheless illustrate the information lost when denominators are omitted. Wilson binomial intervals were calculated from the counts ([3](#ref-3)).

**Table 2. Reported counts and reference binomial intervals**

| Reported aggregation | Proportion | Wilson 95% interval |
| --- | ---: | ---: |
| Serine esterase: five hits among nine retrospectively selected designs | 55.6% | 26.7–81.1% |
| Kemp elimination: five of 90 final-round designs above the stated rate criterion | 5.6% | 2.4–12.4% |

These reference intervals illustrate small-count uncertainty under independent Bernoulli trials with a common success probability. They omit best-setting selection bias, dependence between scaffolds and uncertainty in applying the method to new reactions. They are not predictive intervals for future experimental hit rates.

![Proportions and reference intervals with denominators retained](shared/alphaprotein-novo/figures/01-denominators.png)

**Figure 1. Reference intervals from two separate reported aggregations.** Reactions and success criteria differ; higher rates do not demonstrate a better method.

Selection also depends on how many candidates remain. In a hypothetical example, selecting 20 of 100 candidates and recovering eight hits gives 40%. Tightening filters to retain four candidates containing three hits gives 75%, but recovers only three hits. With a budget of 20 experiments, that stringent filter does not determine how the other 16 slots are filled.

These are not measured AP Novo results. The selection fraction and experimental budget change recovered hit counts even at a given hit rate. A high rate alone does not determine the number of useful candidates produced by the whole search.

## Discussion {#_5}

The piperidine results demonstrate altered product selectivity. The reported lead delivered 22 turnovers, a PIP:PYR ratio of 99:1 and 94% enantiomeric excess. Turnover measures product relative to enzyme amount, not a rate constant. PIP:PYR compares six- and five-membered-ring products. Enantiomeric excess is the difference between proportions of two mirror-image isomers; 94% corresponds to 97:3 ([original Table 1](https://www.biorxiv.org/content/10.64898/2026.10.01.756017v1.full), [1](#ref-1)).

DEHP hydrolysis does not show a uniform activity advantage over natural enzymes under ordinary aqueous conditions. The designed enzyme's strength is retaining activity at high temperature or high acetonitrile concentrations where the natural comparator loses activity. The measured product is MEHP, produced by one hydrolysis step, rather than complete DEHP degradation or demonstrated environmental remediation. Ranking candidates depends on the conditions required by the application.

A generated scaffold can resemble natural-enzyme structures even without copying natural sequences. The paper examines the relationship between highly active serine esterases and natural topologies. New sequence, new scaffold, structural difference from known enzymes and new reaction selectivity are distinct properties.

The immediate connection to drug discovery is expanding catalysts and synthetic routes for making desired molecules. Piperidine's use in medicinal chemistry does not make this study a prediction of efficacy, pharmacokinetics, safety or clinical success.

## Conclusion {#article-conclusion}

A high structural score does not determine activity across reaction states or redesigned sequences. Experimentally measured AlphaProtein Novo activity and computational selection performance are different results. Selection needs interpretation in terms of reaction-specific success definitions, retained candidates and experimental budgets.

## Data and code availability {#_6}

The [calculation code and results](shared/alphaprotein-novo/alphaprotein-novo.zip) contain Python code, input and result CSVs, and reproduction instructions for the Wilson intervals and hypothetical example. Aggregation uses only the standard library; plotting uses matplotlib. The package excludes original paper figures, sequences, model weights and official code.

The implementation was inspected at commit `e7ce276cb4a1f68c2ba7d5aa793192cfcb4845c8`. README examples reduce settings such as resequencing counts and folding seeds for runtime. Running an example is different from reproducing the paper's full experiments. Model weights and outputs have conditions separate from the source-code license ([fixed README](https://github.com/google-deepmind/alphaprotein-novo/tree/e7ce276cb4a1f68c2ba7d5aa793192cfcb4845c8), [2](#ref-2)).

## References {#article-references}

1. <span id="ref-1"></span>Wu Z, Abramson J, Frerix T, Chu AE, Zhang RK, Schulz L, et al. Designing enzymes for new-to-nature chemistry and non-natural substrates with AlphaProtein Novo. bioRxiv [Preprint]. 2026 Oct 5; version 1. [Version examined](https://www.biorxiv.org/content/10.64898/2026.10.01.756017v1).
2. <span id="ref-2"></span>Google DeepMind. AlphaProtein Novo: official implementation [Software]. Commit e7ce276cb4a1f68c2ba7d5aa793192cfcb4845c8. [Fixed version and README](https://github.com/google-deepmind/alphaprotein-novo/tree/e7ce276cb4a1f68c2ba7d5aa793192cfcb4845c8).
3. <span id="ref-3"></span>Wilson EB. Probable Inference, the Law of Succession, and Statistical Inference. Journal of the American Statistical Association. 1927;22(158):209–212. [doi:10.2307/2276774](https://doi.org/10.2307/2276774).
