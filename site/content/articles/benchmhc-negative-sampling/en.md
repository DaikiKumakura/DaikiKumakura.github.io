What does an AI system for cancer-vaccine antigen selection learn to reject? Ideally, peptides observed on major histocompatibility complex (MHC) molecules would be compared with experimentally verified non-presented peptides. But an undetected peptide is not necessarily a non-presented peptide. Artificial competitors fill that gap, and their construction changes the problem being learned.

The new BenchMHC report makes this issue concrete. Its authors report that 86–99% of positive examples in public NetMHCpan-4.1 eluted-ligand datasets occur in the human proteome, compared with approximately 12% of the decoys. Sequence origin could therefore help distinguish the dataset labels before MHC suitability is considered ([1](#ref-1)).

The proportions in original [Figure 3](https://www.biorxiv.org/content/10.64898/2026.10.22.760998v1.full#F3) concern unique training peptides found in the human proteome associated with hg38. The 86–99% range spans data configurations; it is neither a confidence interval nor an AUC measured on the evaluation set ([1](#ref-1)).

Isolating that imbalance produces high discrimination without using MHC binding at all. The calculation below does not prove that an actual predictor learned this shortcut. It asks **how easy negative-example construction alone can make an evaluation**.

## Scope and sources

I checked the authors' public repository and glossary on 1 November 2026. On 3 November 2026, I checked methods, results, limitations, original Table 2 and relevant figure captions in the full HTML preprint. This is neither a retraining of the model nor a reanalysis of patient antigen candidates ([1](#ref-1), [2](#ref-2)).

The repository explicitly describes a partial release. Its reproduction list and the new abstract cannot be assumed to describe exactly the same public implementation state. Reading the paper does not certify complete correspondence between its claims and the currently released implementation.

## Observed positives and constructed negatives

Peptides eluted from MHC and detected by mass spectrometry provide evidence close to natural presentation. In vitro binding affinity instead measures how tightly peptide and MHC bind. The BenchMHC glossary distinguishes these readouts ([3](#ref-3)).

A decoy is not necessarily a sequence experimentally shown never to be presented. It is a competitor supplied for training or evaluation. If positives and negatives arise through different generation processes, sequence properties unrelated to MHC suitability may separate them.

Human-proteome membership is not intrinsically meaningless. Learning biological sequence distributions can be useful. The question is whether this distinction persists among the candidates ultimately being ranked. If every candidate matches the reference human proteome, that matching feature alone cannot order them.

Mutant peptides may not exactly match a reference proteome, however. Treating all real vaccine candidates as matching sequences would also be wrong. The candidate-generation process is part of the evaluation target.

## ROC-AUC from one binary feature

Let \(Y=1\) denote a positive dataset label and \(Y=0\) a decoy. Let \(Z=1\) indicate an exact match in the human proteome, with \(Z=0\) otherwise. These are dataset labels, not independently established biological presentation states.

Define the matching probabilities as

\[
a=P(Z=1\mid Y=1),\qquad b=P(Z=1\mid Y=0).
\]

No model is fitted: \(Z\) itself is the score. For an independently drawn positive and decoy, the area under the receiver operating characteristic curve (ROC-AUC) counts a higher positive score as a success and a tie as half a success. Thus

\[
\begin{aligned}
\mathrm{AUC}
&=a(1-b)+\frac12\{ab+(1-a)(1-b)\}\\
&=\frac12+\frac12(a-b).
\end{aligned}
\]

Neither an MHC allele nor a binding motif enters this calculation.

Table 1 reports the executed calculation. The first two rows use proportions from the abstract as conditional inputs; they are not measured BenchMHC AUCs. The last two rows are hypothetical controls with matching feature distributions.

Table 1. Theoretical ROC-AUC when proteome matching alone is the score

| Condition | Positive matching probability \(a\) | Decoy matching probability \(b\) | ROC-AUC |
| --- | ---: | ---: | ---: |
| Lower end of reported range | 0.86 | 0.12 | 0.870 |
| Upper end of reported range | 0.99 | 0.12 | 0.935 |
| Hypothetical matched distributions | 0.86 | 0.86 | 0.500 |
| Hypothetical universal matches | 1.00 | 1.00 | 0.500 |

The 0.870–0.935 range does not arise from learning MHC selection. It comes entirely from a difference in matching probabilities. A high AUC therefore cannot establish learning of binding in this example.

An actual sequence predictor may not receive this binary feature explicitly. Nor have I measured how well it can infer the relevant distribution difference from sequence alone. These values cannot be subtracted from an existing predictor's AUC to recover its biological performance.

## Correcting decoys does not unify evaluation targets

The authors also report redrawing decoys within each hit's source protein while matching cysteine status. Mean Top-K rises from 0.734 to 0.755 on a regenerated evaluation set, whereas Median FRANK rises from 0.0025 to 0.0053 in a separate CD8-epitope evaluation ([1](#ref-1)).

The source-protein sampler matches cysteine status where possible and falls back to the opposite status when no matching candidate exists. Corrected training data are v1.1.0; the regenerated MS evaluation set is v2.0.0. Table 2 extracts the EL-head rows: compare models within the same evaluation-set column ([1](#ref-1), Section 4).

Table 2. EL-head results from original [Table 2](https://www.biorxiv.org/content/10.64898/2026.10.22.760998v1.full#T2). MS denotes mass-spectrometry ligands; CD8 is a separate epitope evaluation. Arrows indicate the favorable direction.

| Training data / EL head | Mean Top-K: MS v0.0.0 ↑ | Mean Top-K: MS v2.0.0 ↑ | Median FRANK: CD8 epitopes ↓ |
| --- | ---: | ---: | ---: |
| Original v0.0.0 | 0.794 | 0.734 | 0.0025 |
| Re-curated v1.1.0 | 0.733 | 0.755 | 0.0053 |

Those changes do not both indicate improvement. Top-K measures recovery of positives among highly ranked candidates and is better when higher. The paper defines FRANK as the fraction of candidate peptides from an epitope's source protein scoring above that epitope; lower is better ([1](#ref-1), Section 3). Different datasets and metrics preclude direct numerical comparison, but the decoy change did not uniformly improve evaluation.

Matching origin can reduce an unwanted classification cue. It does not establish that the resulting competitors fully represent the candidates of interest in a patient's tumor. Making a benchmark harder and making it closer to a clinical selection problem remain separate judgments.

## Beyond antigen presentation

MHC binding, cell-surface presentation, T-cell recognition and therapeutic effect are different observations. This calculation does not even resolve the first distinction: it concerns only separation of evaluation labels.

That restricted question still matters for cancer vaccines. With a limited number of experimental slots, the desired quantity is ranking among the actual candidate pool. Successful rejection of artificial decoys alone does not establish that ranking.

The calculation omits other sequence features, MHC alleles, dependence among candidates and undetected positives among competitors. The full reported dataset was not reanalyzed. The conclusion is about interpretation, not rejection of NetMHCpan as a whole: **an AUC without a specified negative-generation process cannot establish the ability to select cancer-vaccine candidates**.

The paper explicitly notes that source-species and cysteine corrections were applied together, preventing separation of their effects. Each condition is a single run of a 50-MLP ensemble, without seed-level confidence intervals. The 50 members are not 50 independent estimates of the intervention effect. The evaluation set was also regenerated, so reporting only the improving metric would not establish general improvement ([1](#ref-1), Section 5).

*Revised 3 November 2026: full HTML checked; FRANK candidate set, dataset versions, joint-correction confounding and single-ensemble limitations clarified. Independent calculations are unchanged.*

## Data and code availability

The [code and results archive](shared/benchmhc-negative-sampling/benchmhc-negative-sampling.zip) contains standard-library Python code, Table 1 as CSV, input definitions and environment information. Run `python analysis.py` to regenerate it. No sequence data, third-party model or source-study figures are redistributed. Checks enumerate all binary score pairs and verify the equal-distribution controls.

## References

1. <span id="ref-1"></span>Borck T, Chabrol M, Colombo D, Imbert A, Perier-Dulhoste M, Volzhenin K, et al. BenchMHC: a reproducible framework for peptide-MHC presentation prediction [Preprint]. bioRxiv; 2026. Version 1, 2026 Oct 27. [doi:10.64898/2026.10.22.760998](https://doi.org/10.64898/2026.10.22.760998). Full HTML methods, results, limitations, original Table 2 and relevant figure captions checked on 2026 Nov 3: [version 1 full text](https://www.biorxiv.org/content/10.64898/2026.10.22.760998v1.full). No model retraining or raw sequence recount.
2. <span id="ref-2"></span>InstaDeep. [BenchMHC-public: Open-source reproductions of peptide-MHC presentation prediction models](https://github.com/instadeepai/BenchMHC-public) [Software and documentation]. Partial public release; cited 2026 Nov 1.
3. <span id="ref-3"></span>InstaDeep. [BenchMHC glossary](https://github.com/instadeepai/BenchMHC-public/blob/main/docs/guides/glossary.md) [Internet]. BenchMHC-public; publication date not specified [cited 2026 Nov 1].
