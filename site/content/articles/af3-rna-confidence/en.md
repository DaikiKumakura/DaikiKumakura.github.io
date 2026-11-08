A protein looks convincingly folded, with a ribonucleic acid (RNA) molecule placed beside it. Does that picture establish the RNA-binding geometry?

A new preprint by Tennie and colleagues reports a failure that makes this inference unsafe for structurally novel RNAs. The protein fold can remain accurate while the RNA fold and relative placement deteriorate, without a corresponding drop in predicted RNA confidence [(1)](#ref-1).

The useful question is more specific than whether AlphaFold 3 works. Which parts of a prediction remain informative, and which cannot support the next experimental inference?

## Scope and sources

This article examines version 1, posted on November 4, 2026. I checked the public abstract and the authors' code and data documentation, rather than independently examining all figures in the full manuscript. The numerical example below is an artificial calculation, not a measurement of AlphaFold 3 performance.

The study evaluates over 1,300 protein–RNA complexes and approximately 270 RNA-only systems, including comparisons by structural novelty [(1)](#ref-1). The authors also provide evaluation code and instructions for obtaining data [(2)](#ref-2).

## Three different kinds of correctness

For a complex, at least three questions matter: whether the protein is folded correctly, whether the RNA is folded correctly, and whether their relative position and orientation are correct.

Correct individual folds do not determine their relative placement. One component can rotate and translate without changing its internal structure. Conversely, locating a short interacting RNA segment does not establish the fold of the entire RNA. Identifying a candidate binding region and explaining atomic interactions require different levels of accuracy.

Evaluation also depends on the alignment convention. Superimposing the protein before assessing RNA placement penalizes displacement within the complex. Independently superimposing the RNA removes that rigid-body displacement and instead tests its fold. A single aggregate score can obscure the distinction.

A misplaced interface matters when residue distances are used to justify molecular design. An approximate region may still help narrow an experimental search. Collapsing both uses into one success rate erases the question the structure is supposed to answer.

## Does a confidence threshold survive a change in targets?

Let \(s\) be a model score, \(A=1\) denote a structure adequate for the intended use, and \(t\) be an acceptance threshold. The decision-relevant quantity is \(P(A=1\mid s\ge t)\), the fraction of accepted structures that are adequate. The score itself is not assumed to equal this probability.

Let \(z\) describe familiarity relative to known RNA structures. Overall precision is a weighted average of group-specific precision:

\[
P(A=1\mid s\ge t)=\sum_z P(A=1\mid s\ge t,z)P(z\mid s\ge t).
\]

Table 1 is an artificial illustration. At the same threshold, 100 structures are accepted from each group, with 90 and 50 adequate structures respectively.

Table 1. Artificial accepted sets at a common threshold.

| Group | Selected structures | Acceptable structures | Precision |
| --- | ---: | ---: | ---: |
| Familiar | 100 | 90 | 90% |
| Novel | 100 | 50 | 50% |

Pooled precision is 140/200, or 70%. If novel targets constitute 80% of the accepted set in use, unchanged within-group performance produces \(0.2\times0.9+0.8\times0.5=0.58\), or 58% precision. The threshold changes meaning simply because the target mixture changes.

This calculation does not estimate the study's performance loss. It explains why a pooled correlation or average error cannot guarantee reliable selection in a novel subgroup. Novelty categories also require scrutiny: defining them after inspecting evaluation outcomes can introduce optimism. The definition of novelty and the threshold must be examined for use of test-set answers.

## Different errors imply different experiments

If only the protein fold is stable, the structure does not yet justify a detailed RNA-binding mechanism. If the interacting RNA region is stable, a regional hypothesis may remain useful. Agreement among multiple predicted poses still comes from a shared modeling procedure; it is not equivalent to independent experimental corroboration.

Partial information should not disappear in an all-or-nothing verdict. Rejecting every prediction and accepting an entire complex from one score both obscure which components are supported. Separating binding, regional localization and atomic geometry makes disagreements with experiments easier to interpret.

## Conclusion

A correct protein fold cannot be promoted into evidence that an RNA-containing complex is correct. The preprint argues that this distinction also matters when interpreting confidence. Its public abstract, however, does not establish subgroup error distributions or a usable operational threshold.

The acceptance criterion should follow the intended use. A prediction that narrows an RNA-binding region and a prediction used to explain an atomic mechanism should not receive the same passing grade.

## Data and code availability

The artificial calculation is in the [calculation script](shared/af3-rna-confidence/reproduce.py) and the `AF3_threshold_illustration` section of the [recorded output](shared/af3-rna-confidence/illustration.json). No empirical structure data were reaggregated. The authors' repository provides their analysis materials [(2)](#ref-2).

[Download code and results](shared/af3-rna-confidence/af3-rna-confidence.zip).

## References

1. <a id="ref-1"></a> Tennie IK, Uhl M, Franke JKH, Backofen R, Runge F. AlphaFold 3 Prediction Accuracy and Reliability across RNA Structures and Protein-RNA Interfaces [Preprint]. bioRxiv; 2026. Version 1, posted 2026 Nov 4. [https://doi.org/10.64898/2026.11.02.763690](https://doi.org/10.64898/2026.11.02.763690).

2. <a id="ref-2"></a> Tennie IK, Uhl M, Franke JKH, Backofen R, Runge F. RNA-Protein-3D-Structure-Evaluation [Software and data documentation]. 2026. Paper-associated tag v1.0.1 [cited 2026 Nov 8]. [Repository](https://github.com/automl/RNA-Protein-3D-Structure-Evaluation).
