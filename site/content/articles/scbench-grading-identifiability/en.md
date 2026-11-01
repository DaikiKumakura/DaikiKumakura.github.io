An AI has answered a single-cell analysis task correctly. How much responsibility does that justify handing over? Kenny Workman argues that executable, feedback-rich data analysis can provide an entry point for biology agents. He also distinguishes it from the harder problems of defining scientific ground truth and obtaining experimental feedback ([1](#ref-1)).

I examined that distinction using published scBench grading conditions. In a differential-expression task, passing a gene-count check does not establish agreement about which genes were found. In a quality-control task, matching summaries does not identify the reasoning that produced them.

## Scope and sources

On November 1, 2026, I read the scBench repository and three public evaluation specifications. Two specifications, differential expression and quality control, were selected for small checks. The README accessed describes 195 evaluations in six categories ([2](#ref-2)). The February 2026 preprint instead describes 394 problems in seven categories. These are different versions or scopes; their denominators and reported accuracies must not be combined ([3](#ref-3)).

I did not rerun the biological analyses or evaluate an AI model. I executed the published numeric grader and compared it with an independently written arithmetic checker. Their decisions agreed in nine cases that required no biological input. The upstream source is not redistributed; the distributed code contains only the independent numeric-condition implementation.

## A task that grades gene counts

`DE01_pseudobulk_de` asks for differential expression in CD14 monocytes responding to IFN-beta in a multi-donor single-cell RNA sequencing (scRNA-seq) experiment. It specifies cell-count eligibility by donor and condition, total-count gene filtering, adjusted p-value and fold-change thresholds. The requested answer is one field, `n_degs`, the number of differentially expressed genes (DEGs) ([4](#ref-4)).

The public configuration uses a reference value of 1150 and an absolute tolerance of 350. With reference \(c\), submitted value \(x\) and tolerance \(\delta\), the condition is

\[
|x-c|\leq\delta.
\]

The implementation reads the configured numeric fields and checks this condition. It does not recover a gene set or an analytical method from that number ([5](#ref-5)).

Table 1 reports the executed boundary checks using the public configuration. Only integer submissions were considered.

**Table 1. Boundaries of the DEG-count grading condition**

| Submitted DEG count | Numeric-condition decision |
| ---: | --- |
| 799 | Fail |
| 800 | Pass |
| 1150 | Pass |
| 1500 | Pass |
| 1501 | Fail |

The independent checker and retrieved upstream grader produced the same decisions. This is a check of the accepted interval, not a model-accuracy result.

There is a reason to allow a range. The specification describes variation across pseudobulk tools and donor cell-count eligibility. Requiring one exact number could reject defensible implementation choices. A tolerance is not inherently an error ([4](#ref-4)).

## Matching counts do not imply matching genes

I constructed two artificial gene sets, A and B. Both contain 1150 entries, but they have no entries in common. No biological gene labels or scBench data were used.

Their Jaccard similarity is

\[
J(A,B)=\frac{|A\cap B|}{|A\cup B|}=0/2300=0.
\]

However, the submitted answer is `n_degs=1150` in both cases, so both pass the numeric condition.

The gene sets were not passed to the grader. The construction shows that **a grade that does not request a gene set cannot establish agreement about that set**. It is not evidence that an actual agent reported unrelated genes, and it does not estimate the frequency of false passes.

This matters when response genes are to be selected for experimental follow-up. Equal candidate counts do not align the decision if the genes to be tested differ. Conversely, a count check can be useful for detecting processing errors that greatly inflate or reduce the number of DEGs. The meaning of a pass depends on the object being graded.

## Identical summaries can have different rationales

The public QC example, `bd_rhapsody_tnbc_panel_aware_qc`, targets the mistake of importing whole-transcriptome filtering thresholds into a small targeted panel. It grades three summaries: retained peripheral-blood mononuclear cell (PBMC) count, median detected genes and classical-monocyte count ([6](#ref-6)).

The specification explicitly documents what it permits. Because the panel contains no mitochondrial genes, a mitochondrial-fraction filter is a no-op. An agent can choose that filter for an inappropriate reason yet pass numerically if the resulting summaries are unchanged. The authors document this as a case where downstream biology is unaffected. This is not a hidden defect discovered here.

For the check, I supplied the same reference summaries in two answers. I labelled one explanation as panel-aware processing and the other as a no-op filter, but those explanatory labels were not submitted to the numeric grader. Both passed. The check confirms that identical numeric inputs cannot distinguish a rationale that the grader never observes.

There is a reasonable case for not penalizing an operation that changes no result. But calling that pass evidence of understanding the assay would broaden the claim beyond the grade. Reaching the same answer on this dataset and responding appropriately to a different panel are separate questions.

## Read a pass within its scope

Local grading helps isolate failures and track improvements. That benefit remains. Workman's essay itself does not claim that local verification immediately supplies a correct answer for all of science ([1](#ref-1)).

scBench-Long also proposes a separate evaluation of multi-step analysis leading to scientific conclusions. I checked the abstract and bibliography of its June 2026 preprint describing 21 evaluations; I did not re-evaluate its data or full grading scheme. The local tasks examined here cannot stand for the entire field of biology-agent evaluation ([7](#ref-7)).

This check covers numeric conditions in two public examples. It does not establish the same limitation in withheld problems, trajectory evaluation or other grader families. Nor does the independent checker reproduce answer extraction, every malformed-value case or the full execution harness.

Within that scope, a DEG-count pass does not guarantee agreement about the gene set, and a QC-summary pass does not identify an analyst's rationale. Reading an AI analysis accuracy figure requires retaining the object that the evaluation actually observed alongside the percentage.

## Data and code availability

The [independent code](shared/scbench-grading-identifiability/analysis.py), [boundary CSV](shared/scbench-grading-identifiability/results/de-boundaries.csv), [result JSON](shared/scbench-grading-identifiability/results/results.json) and [reproduction instructions](shared/scbench-grading-identifiability/REPRODUCE.md) are available. They were run with Python 3.12.4 and the standard library, without randomness. The [verification record](shared/scbench-grading-identifiability/upstream-verification.json) contains the nine comparisons with the published grader. Biological data, upstream grader source and model outputs are not included.

## References

1. <span id="ref-1"></span>Workman K. [Agentic biology is shaped like software](https://blog.latch.bio/p/agentic-biology-is-shaped-like-software) [Internet]. LatchBio; 2026 Apr 30 [cited 2026 Nov 1].
2. <span id="ref-2"></span>LatchBio. [scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis](https://github.com/latchbio/scbench) [Software and documentation]. GitHub; [cited 2026 Nov 1]. README version accessed describes 195 evaluations.
3. <span id="ref-3"></span>Workman K, Yang Z, Muralidharan H, Abdulali A, Le H. scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis [Preprint]. arXiv; 2026. Version 1, 2026 Feb 9. [doi:10.48550/arXiv.2602.09063](https://doi.org/10.48550/arXiv.2602.09063).
4. <span id="ref-4"></span>LatchBio. [DE01_pseudobulk_de.json](https://github.com/latchbio/scbench/blob/main/evals/differential_expression/DE01_pseudobulk_de.json) [Evaluation specification]. GitHub; [cited 2026 Nov 1]. Git blob SHA: 473eaaf2eb8da8e92e722fab20da15492357362e.
5. <span id="ref-5"></span>LatchBio. [NumericToleranceGrader](https://github.com/latchbio/latch-eval-tools/blob/main/src/latch_eval_tools/graders/numeric.py) [Software source]. GitHub; [cited 2026 Nov 1]. Git blob SHA: 4fe0a812d3abc52f0efcfc69fd204eefa713f930.
6. <span id="ref-6"></span>LatchBio. [bd_rhapsody_tnbc_panel_aware_qc.json](https://github.com/latchbio/scbench/blob/main/evals/qc/bd_rhapsody_tnbc_panel_aware_qc.json) [Evaluation specification]. GitHub; [cited 2026 Nov 1]. Git blob SHA: 5540b13fe58289b313dfaad515de9d0d4ef235e7.
7. <span id="ref-7"></span>Diks I, Yang Z, Banerjee A, Proctor T, Workman K. scBench-Long: Verifiable Benchmarking of Long-Horizon Single-Cell Biology [Preprint]. arXiv; 2026. Version 1, 2026 Jun 25. [doi:10.48550/arXiv.2606.26563](https://doi.org/10.48550/arXiv.2606.26563). Abstract consulted; full benchmark not re-evaluated.
