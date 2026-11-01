Once RNA positions are measured, it is tempting to say that the conversations between neighboring cells can be read. One task comes first: deciding which cell owns each measured RNA molecule.

Move that boundary and the expression matrix moves with it. An analysis that links a ligand-producing cell to a receptor-expressing cell can acquire a different partner without a single RNA coordinate changing.

A Nature Methods paper published on October 23, 2026 compared 11 segmentation methods across 15 datasets from five technologies: Stereo-seq, Xenium, CosMx, STARmap PLUS and MERFISH. It examined how segmentation choices affect expression specificity and downstream ligand–receptor inference ([1](#ref-1)).

## Scope and sources

I examined the accessible Results, Methods and figure descriptions, together with the public code README. I did not run the published pipeline to reproduce the complete benchmark ([1](#ref-1), [2](#ref-2)). After a short discussion of the comparison, I calculate a hypothetical example in which only transcript assignment changes. It does not estimate the misassignment rate of any actual segmentation method.

The relevant original analysis is [Figure 5 on marker leakage and ligand–receptor inference](https://www.nature.com/articles/s41592-026-03272-x#Fig5). It compares Giotto inference for three ligand–receptor pairs across combinations of technologies and segmentation methods. This is evidence that upstream assignments propagate downstream in the selected tissue and pairs, rather than a comprehensive validation of communication inference methods ([1](#ref-1)).

## Recovering more cells is not sufficient

Split one cell in two and the cell count increases. Expand a boundary and more transcripts become assigned to cells. Neither change, by itself, establishes accuracy.

The paper therefore evaluates expression, cell identity and morphology as well as cell recovery and assigned transcripts ([1](#ref-1)). Yet comparisons against reference annotations and known markers also have assumptions. Preserving a known cell identity and retaining an unfamiliar intermediate state are different objectives.

Suppose a small amount of receptor RNA is assigned to the wrong cell type. Strong expression of other markers might preserve the cell-type label while increasing the apparent fraction of receptor-positive cells. High agreement in cell labels does not establish that target positivity or communication inference is equally stable.

## Moving transcripts to the neighbor

To isolate this effect, I defined two neighboring cell types, A and B. A has a mean of 50 ligand L transcripts and no receptor R transcripts; B has no L and a mean of 50 R transcripts. These are hypothetical per-cell RNA counts, not observations.

Cell identities are assumed to be known from separate information and remain fixed. A and B have equal cell numbers and one-to-one adjacency. Cell numbers, adjacency and total tissue amounts of L and R also remain fixed. A fraction \(\alpha\) of each transcript population is then symmetrically assigned to the neighboring type. The model isolates mixing from segmentation; it does not represent ambient RNA or biological transcriptional changes.

The assigned means are

\[
L_A=50(1-\alpha),\quad R_A=50\alpha,\qquad
L_B=50\alpha,\quad R_B=50(1-\alpha).
\]

For a downstream readout, I multiply mean ligand expression in the putative sender by mean receptor expression in the putative receiver. This explanatory expression product is not Giotto's significance score, receptor occupancy or a communication rate. Even this simple readout exposes the assignment effect:

\[
S_{A\to B}=2500(1-\alpha)^2,\qquad
S_{B\to A}=2500\alpha^2,\qquad
S_{A\to A}=S_{B\to B}=2500\alpha(1-\alpha).
\]

Table 1. Expression products under hypothetical transcript misassignment.

| Misassigned fraction | A→B | B→A | Each of A→A and B→B |
| --- | ---: | ---: | ---: |
| 0% | 2500 | 0 | 0 |
| 5% | 2256.25 | 6.25 | 118.75 |
| 10% | 2025 | 25 | 225 |
| 20% | 1600 | 100 | 400 |

Values are products of mean RNA counts in arbitrary units. Calculations use representative type means, with no cell-to-cell variation or hypothesis test.

At 10% misassignment, the A→B product falls by 19%. Each originally zero within-type product becomes 225, equivalent to 9% of the original A→B product. B→A also becomes 25, but its fold increase is undefined because the starting value was zero.

![Between-type and within-type expression products as transcript misassignment increases](shared/spatial-segmentation-communication/reassignment.svg)

Figure 1. Hypothetical symmetric reassignment. The vertical axis divides each product by the original A→B value of 2500. Curves describe fixed assumptions, not uncertainty in an estimate. The two within-type curves coincide.

Total tissue expression is unchanged. Cell numbers are unchanged. Only ownership of the transcripts changes, yet ligand–receptor coexpression within a cell type appears. Agreement in aggregate RNA abundance cannot reveal this error.

## More positive cells do not imply more targets

This is where the example meets drug discovery. If an apparent increase in receptor-positive cell types is interpreted as a safety concern or a rationale for another indication, genuine receptor expression must be distinguished from positivity introduced by boundary mixing.

The example does not estimate an actual false-positive rate: it specifies neither a positivity threshold nor detection efficiency or per-cell distributions. RNA detection also does not establish functional receptor abundance at the membrane or drug binding.

Likewise, a communication candidate that disappears under another segmentation is not automatically an error. A stricter segmentation might discard genuine transcripts near the boundary. Robustness across segmentations is informative, but is not a ground-truth label for a mechanism.

## Keeping boundary uncertainty inside the interpretation

The calculation assigns the same mixing fraction to every gene and cell. Actual misassignment depends on subcellular RNA position, morphology, density and distance from the nucleus. Misannotation, altered adjacency and missed transcripts would add further changes. The 10% setting is not a universal error rate measured by the original paper.

A large expression product is also not proof of functional communication. Ligand release, protein localization, receptor activation and a responding cell remain separate stages. This example shows that RNA assignment can change the candidate pattern before any of those stages are considered.

Spatial information enriches interpretation. It also makes the definition of a cell boundary part of that interpretation. For cell–cell communication, the boundary is not a problem that has simply been settled during preprocessing.

## Data and code availability

The independent calculation uses hypothetical assumptions throughout. The [analysis script](shared/spatial-segmentation-communication/analysis.py), [output CSV](shared/spatial-segmentation-communication/reassignment.csv) and [reproduction instructions](shared/spatial-segmentation-communication/REPRODUCE.md) include the formulas and outputs. Original experimental data and published figures are not redistributed.

## References

1. <span id="ref-1"></span>Martínez-de-Morentin X, Khan SA, Maillo A, Lehmann R, Kiani NA, Lagani V, et al. Benchmarking segmentation methods for spatial transcriptomics. Nat Methods. 2026. Published online October 23. [https://doi.org/10.1038/s41592-026-03272-x](https://doi.org/10.1038/s41592-026-03272-x).
2. <span id="ref-2"></span>TranslationalBioinformaticsUnit. Benchmarking-SegmentationMethods-ST [Software]. GitHub; [cited 2026 Nov 1]. Available from: [https://github.com/TranslationalBioinformaticsUnit/Benchmarking-SegmentationMethods-ST](https://github.com/TranslationalBioinformaticsUnit/Benchmarking-SegmentationMethods-ST).
