What caught my attention in the Atomwell announcement was how experimental data were extracted from papers, rather than model size. In his October 19, 2026 UTC thread, Navvye Anand also discussed extraction evaluation and grading criteria ([1](#ref-1)).

When a human-curated dataset and a large language model (LLM) extraction agree, can their agreement stand in for a correct answer? Does a prediction-model comparison restricted to those agreements also apply to the full extracted dataset?

## Scope and sources

Bindwell's technical blog describes matching Datawell and contract research organization (CRO) records by paper, protein sequence, ligand, and measurement type. Of 10,972 matched measurements, 8,566 exact-value agreements were retained for a training-data comparison. A separate LLM-graded extraction evaluation used 20 papers with three repeats; another affinity-model comparison used 1,885 measurements. These evaluations have different denominators and purposes ([2](#ref-2)).

I use the two published counts to calculate the selection fraction and quantities that agreement alone cannot determine. I have not checked the underlying extraction records or adjudicated labels, or run Atomwell. A [separate article](affinity-noise-ceiling-en.html) addresses prediction ceilings from measurement variation. Here the question is extraction fidelity to the source text.

## The denominator behind 78.1%

Table 1 recalculates the aggregate counts. Dividing 8,566 by 10,972 gives 78.1%; the remaining 2,406 measurements account for 21.9%.

Table 1. Agreement and disagreement calculated from the reported matched records.

| Status | Count | Percentage of 10,972 matched measurements |
| --- | ---: | ---: |
| Exact-value agreement | 8,566 | 78.1% |
| Values disagree | 2,406 | 21.9% |

The 78.1% is agreement among records that both sources extracted in a matchable form. Records extracted by only one source, and measurements missed by both, are outside this denominator. It cannot be converted into the fraction of source measurements successfully recovered.

Extraction precision counts correct items among retrieved items; recall counts correctly retrieved items among relevant items. The denominators differ ([3](#ref-3)). Agreement in a number also differs from agreement in its unit, target, and conditions. The number of correct records is not defined until the scoring unit is specified: a normalized value alone, or the complete measurement record.

## Two identical answers can both be wrong

The following is a derivation of what is identifiable, not an estimate from the original study. Assume that each matched record has one correct value that can be established by source adjudication. This is the defined extraction target, not a biological true value. Call the extractors A and B.

On an agreement, A and B are either both correct or both wrong. On a disagreement they cannot both be correct. They can still both be wrong, because numerical errors can take more than two values.

Let $c$ be the number of correct records among the 8,566 agreements, $a$ the number of disagreements on which only A is correct, and $b$ the number on which only B is correct. The constraints are $0\leq c\leq 8{,}566$, $a\geq0$, $b\geq0$, and $a+b\leq2{,}406$. Their accuracies are

$$
p_A=\frac{c+a}{10{,}972},\qquad p_B=\frac{c+b}{10{,}972}.
$$

Both $p_A$ and $p_B$ refer only to this matched set. All four assignments in Table 2 are consistent with the same 78.1% agreement.

Table 2. Accuracies that can be constructed without changing the agreement count. These are not observed results.

| Assignment of correctness | A accuracy | B accuracy |
| --- | ---: | ---: |
| All agreements correct; neither correct on disagreements | 78.1% | 78.1% |
| Both wrong on agreements and disagreements | 0% | 0% |
| All agreements correct; only A correct on disagreements | 100% | 78.1% |
| All agreements correct; only B correct on disagreements | 78.1% | 100% |

The table is not an allegation that both sources are always wrong. It shows that the agreement count alone cannot exclude such assignments. Shared misreading or unit conversion can survive an agreement filter. Conversely, this calculation does not rule out high source fidelity among agreements.

Nor is 21.9% the error rate of A. A disagreement has not yet been assigned to an error by A, B, or both. It is a fraction of records on which at least one source is wrong under the stated assumptions, without identifying how errors are distributed between the extractors.

## The question answered by an agreement-only comparison

Using agreements as shared labels reduces the problem of declaring either dataset alone to be correct. It also changes the evaluation target to measurements on which the two extractions agree. Extending a comparison from that set to all 10,972 matched measurements requires information about the excluded records.

This distinction can be expressed as a weighted mean of losses. Compare prediction models X and Y using mean squared error on a consistent scale. Define $\Delta_A$ as X minus Y error on agreements, and $\Delta_D$ as the corresponding difference on disagreements. If evaluation labels for both groups have been established, for example through source adjudication, the error difference across the complete matched set is

$$
\Delta_{\mathrm{all}}=q\Delta_A+(1-q)\Delta_D,\qquad q=\frac{8{,}566}{10{,}972}.
$$

If X performs better on agreements, $\Delta_A<0$. Its ranking reverses across the full matched set when

$$
\Delta_D>\frac{q}{1-q}|\Delta_A|\approx3.56|\Delta_A|.
$$

The 3.56 is the ratio of weights calculated from the reported counts, not an estimate of an actual model-error difference. This does not establish that a reversal occurs. It shows that the agreement-only result does not identify the overall ranking while disagreement-group error remains unmeasured. The decomposition is for the specified mean squared error. It is not a formula for averaging group-specific R² values, whose variance denominators can differ.

The limitation becomes stronger when the population is expanded to include records extracted by only one source. The 78.1% is a within-matched-set weight, not coverage of all measurements in all source documents.

## Discussion

Agreement does not do the same job as adjudication. A shared evaluation set can nevertheless be useful. What matters is the population to which its comparison applies. Aggregate counts do not even determine whether selecting agreements makes evaluation easier or harder: it might remove difficult records, erroneous labels, or both.

Establishing source fidelity requires checking agreements as well as disagreements against the original documents. Adjudicating only disagreements leaves shared errors unresolved. Estimating recall requires a set of relevant items defined independently of the two extraction outputs. These are different questions even when both involve human review.

The published counts establish the selection from 10,972 to 8,566 records and allow an analysis of what remains unidentified after that selection. They do not determine Atomwell's predictive performance, Datawell's correctness, or the recovery rate of all measurements in the source texts. The 78.1% is best read as a description of the comparison set, rather than a substitute for accuracy.

## Data and code availability

The [Python code](shared/atomwell-extraction-denominators/analysis.py), [aggregate results](shared/atomwell-extraction-denominators/results/summary.json), [logical-case CSV](shared/atomwell-extraction-denominators/results/logical-cases.csv), and [reproduction instructions](shared/atomwell-extraction-denominators/REPRODUCE.md) generate Tables 1–2 and the weight ratio from the reported counts. Only the standard library is required. Underlying extraction records and grading rubrics are not redistributed.

## References {#references}

<span id="ref-1"></span>
1. Anand N [@navvye]. Announcement of Atomwell and its extraction evaluation [description of X thread]. 2026 Oct 19 [cited 2026 Nov 01]. [Post](https://x.com/navvye/status/2112219726474564019).

<span id="ref-2"></span>
2. Anand N, Goel R. The Bitter Lesson for Biology [Internet]. Bindwell; 2026 Oct 18 [cited 2026 Nov 01]. [Technical blog](https://bindwell.com/posts/the-bitter-lesson-for-biology).

<span id="ref-3"></span>
3. Schilling-Wilhelmi M, Ríos-García M, Shabih S, Gil MV, Miret S, Koch CT, et al. From text to insight: large language models for chemical data extraction. Chem Soc Rev. 2025;54:1125–1150. [doi:10.1039/D4CS00913D](https://doi.org/10.1039/D4CS00913D).
