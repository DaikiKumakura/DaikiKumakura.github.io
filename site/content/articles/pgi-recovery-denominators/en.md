Reference date: the facts in this article are as of 3 November 2026.

A preprint posted on 27 October 2026 reports Post-GWAS Intelligence (PGI), a system for automated interpretation of genome-wide association studies (GWAS), and its analysis engine VariantAgent. The abstract's main numbers are a mean per-study recovery of 82.1% of directly comparable findings across 34 published GWAS, and 530,949 evidence units generated from 1,041 GWAS ([1](#ref-1)). A post by a researcher introduced this as covering "370 traits" ([2](#ref-2)). The post is not evidence for the numbers in this note; it is only the occasion for writing it. This note reads the full text of the preprint, sets out what these numbers count (the denominators), computes intervals from the reported counts, and shows how to read the numbers. The preprint has not been peer reviewed.

## Scope and sources

I read the full text of the preprint (PDF, 33 pages) ([1](#ref-1)). Details of the Extended Data figures were read only to the extent described in the main text. The numbers in this note are of two kinds. Values reported by the preprint (82.1% and its interval, 7.7 points and its interval, the expansion ratios and so on) are used as printed. Values I calculated are exact Clopper–Pearson intervals for single proportions, Newcombe intervals for a difference of two proportions (assuming independence), and values back-calculated from reported intervals; each is marked as my calculation. The 82.1% mean and the expansion ratios cannot be recomputed from counts, because per-study counts are not in the text. Table 1 lists the numbers dealt with and their denominators. The abstract's "1,041 GWAS" and the post's "370 traits" do not conflict: the main text says that 1,041 GWAS span 370 harmonized traits ([1](#ref-1)).

Table 1. The numbers dealt with in this note and their denominators (as printed in the preprint).

| Number | What is counted | Denominator |
| --- | --- | --- |
| 82.1% (95% CI 75.3 to 88.9) | Recovered share of directly comparable findings, averaged over studies | 34 GWAS (findings per study not printed) |
| 81.9% | Source-study paths recovered or extended | 739 directly comparable paths |
| 5 of 7 (71.4%) | Prespecified directly comparable findings recovered (T1D) | 7 findings |
| 3 of 12 (25.0%) | Source-study paths recovered (T1D) | 12 paths |
| 86.3% (270 of 313) | Correct answers to published genetic-reasoning questions | 313 questions |
| 86.3 (score) | Full-process rubric score over ten workflows | 10 workflows, 8 dimensions |

## Discussion by issue

### The same "86.3" is two different quantities

The value 86.3 appears twice in the preprint. One is the full-process score over ten analysis workflows (VariantAgent 86.3, Claude Code 70.4, Biomni 65.7); the other is the accuracy on 313 published genetic-reasoning questions (270 correct, 86.3%) ([1](#ref-1)). The former applies a rubric of eight dimensions scored 0–100, applied by a large language model (Codex with GPT-5.5), and agreement was checked with three blinded experts who scored five tasks (intraclass correlation coefficient, ICC = 0.91). The latter is the proportion of answers that GPT-5.5 judged correct against reference answers. The preprint itself says these are separate benchmarks that cannot be compared directly. The identical value is a coincidence.

### The denominator of the 82.1% recovery

For each of 34 published GWAS, the 82.1% is the proportion of the original study's "directly comparable findings" recovered by the reanalysis, averaged over studies (95% CI 75.3–88.9%). Findings were compared across eight categories (independent association signals, fine-mapped candidate variants, prioritized candidate genes, cellular or tissue contexts, in silico mechanisms, perturbation-screen evidence, candidate drugs and pathogenicity-related evidence) ([1](#ref-1)). From the reported interval, the standard deviation of per-study recovery can be estimated. If the interval is taken to be a normal or t-distribution interval for the mean of 34 studies, it is about 20 points (my calculation: 20.2 with a normal approximation, 19.5 with a t distribution). The preprint does not state, in the text I read, how this interval was obtained, so the estimate is an inference and only suggests that recovery differs greatly between studies.

At the level of variant-centred evidence paths, of 739 directly comparable source-study paths, 155 (21.0%) were fully recovered, 450 (60.9%) were recovered and extended, 89 (12.0%) were partially recovered and 45 (6.1%) were not recovered (Figure 1) ([1](#ref-1)). The preprint counts "recovered and extended" as recovery and reports 605 recovered-or-extended paths as 81.9% (in my calculation the exact interval is 78.9–84.6%; because paths within a study are not independent, this interval is too narrow). The 82.1% (a mean over findings) and the 81.9% (all paths) are different values with different counting units, and neither confirms the other. "Recovered and extended" reproduces the original path and adds evidence, and is reported separately from "fully recovered" (reproducing the original path as it is), 155 paths. Of the 584 paths that were not fully recovered, 450 (77.0%, my calculation) are recoveries with extension.

![Figure 1. Breakdown of the 739 directly comparable source-study paths (from the main text of the preprint; drawn for this note). Fully recovered 155 (21.0%), recovered and extended 450 (60.9%), partially recovered 89 (12.0%), not recovered 45 (6.1%).](shared/pgi-recovery-denominators/figures/01-path-level-recovery.png)

The preprint attaches careful reservations to the meaning of recovery. Recovery does not mean an independently rediscovered source of evidence, and additional evidence does not imply biological novelty or validation. The source publication and supplementary material were excluded from the analysis context and masked by identifiers, but public evidence retrieval was kept, so indirect leakage through secondary resources could not be excluded; agreement is recovery under controlled retrieval, not fully blinded independent replication ([1](#ref-1)).

### An example in type 1 diabetes (T1D): two denominators for one study

In the type 1 diabetes (T1D) GWAS, 5 of 7 prespecified directly comparable findings were recovered (71.4%, exact interval 29.0–96.3% by my calculation). In the same study, using the same path definition, 3 of the original study's 12 paths were recovered (25.0%, interval 5.5–57.2%) ([1](#ref-1)). The former are findings at the trait level and the latter paths at the locus level, so they are not the same quantity counted at different granularity. With small samples and overlapping intervals, this is only a single-study example. VariantAgent assembled 608 paths (50.7 times the 12 of the source study; my calculation), of which 566 contained only source-backed relationships, 18 combined source-backed and predictive evidence, and 24 were graph-nominated candidates. Paths containing predictions or nominations number 42 (6.9%; my calculation) ([1](#ref-1)). The preprint states that this expansion does not mean an equivalent number of experimentally confirmed mechanisms.

### Expansion ratios and the number of evidence units

The ratio of reanalysis to source-study evidence counts was 3.4 for independent signals, 4.7 for prioritized variants, 57.9 for prioritized genes, 6.2 for cellular or tissue contexts, 34.7 for mechanistic hypotheses, 79.6 for perturbation evidence and 1.3 for pharmacological links ([1](#ref-1)). The ratio is computed as a ratio of means only over studies and conditions where the source study has a non-zero countable output that is comparable with the reanalysis output; combinations with zero in the source, and uncountable or non-comparable outputs, were excluded from the ratio. The text also says these are measures of analytical breadth, not increases in biological validation. The 530,949 evidence units likewise are the number of output records.

### Benchmark differences and intervals

On 313 published questions, VariantAgent answered 270 correctly (86.3%, exact interval 81.9–89.9% by my calculation) and the highest comparator, OpenCode (another automated analysis system used for comparison), 246 (78.6%, 73.6–83.0%). The difference is 7.7 points, for which the preprint reports a 95% confidence interval of 3.8–11.8 from a paired bootstrap. Because the two systems answer the same questions, the paired interval is the appropriate one; the Newcombe interval that I computed, treating the two proportions as independent, is 1.7–13.6 and wider, and is a reference value (Figure 2). On 26 GWAS-grounded questions, VariantAgent answered 17 correctly (65.4%, interval 44.3–82.8%), Biomni (another automated analysis system) 14 (the preprint prints 53.9%; 14/26 is 53.846%; interval 33.4–73.4%) and Claude Code 12 (46.2%, 26.6–66.6%), with widely overlapping intervals. Process-validated correct answers (correct and methodologically supported) were 16 (61.5%), 8 (30.8%) and 2 (7.7%), and the proportions of correct answers with a valid supporting trace were 16/17 (94.1%), 8/14 (57.1%) and 2/12 (16.7%). These judgements were made by GPT-5.5 and Codex, and experts checked a subset of tasks and the evidence-admission decisions (agreement in 92.3% of the 26 execution traces) ([1](#ref-1)). With small samples, the differences in point estimates are large but so are the interval widths, and a ranking cannot be asserted. The preprint argues that answer correctness alone obscures differences in analytical validity, and the process-validated measure is central to that claim ([1](#ref-1)).

![Figure 2. Proportions in the benchmarks (exact 95% intervals, my calculation). From the top: correct answers on 313 published questions, correct answers on 26 GWAS-grounded questions, process-validated correct answers on the same questions, and the two denominators in the T1D example. Denominators (k/n, k the count and n the denominator) are shown at the right. From the counts in the main text of the preprint; drawn for this note.](shared/pgi-recovery-denominators/figures/02-benchmark-proportions.png)

## Overall assessment

Most of the preprint's numbers can be reproduced from the counts in the text. How to read them, however, is set by the denominator. The 82.1% is a mean of per-study recovery, which is suggested to vary greatly between studies, and at the path level fully recovered paths are 21.0% and recovered-or-extended 81.9%. Counting "recovered and extended" as recovery is the preprint's definition, and its report shows all four categories. The same T1D study gives 71% at the level of trait-level findings and 25% at the level of locus-level paths. Expansion ratios and the number of evidence units are measures of breadth, not numbers of validated mechanisms. On the small benchmark (26 questions), the point estimates differ but the intervals overlap. The preprint itself states these reservations in the text.

## Limitations

- Counts are as printed in the text. Details of the Extended Data figures and supplementary material were not checked beyond the text. The 82.1% mean and the expansion ratios cannot be recomputed because per-study counts are not in the text.
- The intervals were computed here. Where paths or questions are not independent within a study or analysis context, the intervals are too narrow (especially the path-level interval). The estimate of the per-study standard deviation is an inference, because the method of the reported interval is unknown.
- The selection of benchmark questions, the fairness of comparator settings and scoring details are not evaluated in this note. That the scoring was done by a large language model, with expert checks limited to a subset, bears on how to read the results.
- The judgement of recovery follows the preprint's matching rules (including manual review), and this note did not verify its validity.
- The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

PGI's "82.1% recovery" is the mean over 34 GWAS of the per-study recovery of directly comparable findings; at the path level, fully recovered paths were 21.0% and recoveries including extension 81.9%. Even within one study (T1D), the figure is 71% or 25% depending on whether the denominator is findings or paths. "86.3" is a rubric score in one place and an accuracy in another, different quantities. Evidence units and expansion ratios are measures of breadth. The numbers should be read with their denominators and with the reservations that the preprint itself states (controlled retrieval, not independent replication).

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive. Run with Python 3.12, NumPy 2.2, SciPy 1.14, pandas 2.2 and Matplotlib 3.9: `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The calculation is arithmetic on the counts printed in the preprint and uses no random numbers.

The full re-run materials are in the [companion archive](shared/pgi-recovery-denominators/pgi-recovery-denominators-companion.zip).


## References

<span id="ref-1"></span>1. Qiao L, Gu S, Yang Y, Han Y, Li X, Wan X, et al. Scaling genetic discovery through automated post-GWAS interpretation [Preprint, version 1]. bioRxiv. 2026 Oct 27 [cited 2026 Nov 3]. [doi:10.64898/2026.10.23.761278](https://doi.org/10.64898/2026.10.23.761278). Not peer reviewed. Full text read.

<span id="ref-2"></span>2. Yu F [@fulong_yu]. GWAS signals accumulate. Biological insight should too. Introducing PGI [X post]. X. 2026 Nov 3 [cited 2026 Nov 3]. Available from: https://x.com/fulong_yu/status/2117465653003403717
