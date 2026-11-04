Reference date: the facts in this article are as of 4 November 2026.

A blog post published on 2 November 2026 reports that a frontier large language model (LLM), GPT-6 Astra, edited 0.016% of the weights of the 0.8B-scale model Qwen3.5-0.8B, with no gradients and no training, raising accuracy on the mathematics problem set MATH-500 from 7.9% to 48.1% and on the instruction-following evaluation IFEval about 3x ([1](#ref-1)). As a ratio the MATH-500 change is 6.09x (my calculation; the blog itself does not write "6x"). The blog's authors disclose that the baseline model repeats the same text and rarely reaches an answer, state that removing the repetition only lets the model finish answers it could already work out, report a result on another model where no ability was added, and released the logs of their experiments (what was sent to the model, its replies, the code it ran and the evaluation behind each number) under CC BY 4.0 ([1](#ref-1), [2](#ref-2)). This note recomputes from the published numbers what these figures count: (1) the uncertainty of the difference, (2) the share of baseline outputs that hit the length limit and its effect on correct answers, (3) what the comparison across budgets of 10, 25 and 50 passes compares, (4) what 0.016% means, and (5) how the gains outside mathematics relate to it. It does not dispute the authors' explanation; it separates what the numbers can support from what cannot be known from what is published. An evaluation of the post's overall claim that LLMs can read and write weights is outside this note.

## Scope and sources

I read the full text of the blog post and, in the public logs repository, the [description of Experiment 8](https://github.com/RikiyaT/lm_understand-logs/blob/main/exp8_math/README.md), the results table (`eval/RESULTS_excerpt.md`) and the per-problem MATH-500 scoring ([1](#ref-1), [2](#ref-2)). I did not rerun Astra or the models. The blog and the logs are the same authors' publication, not a third-party replication. The numbers are of two kinds. Values reported by the blog and the logs are quoted as printed. Values I calculated (intervals, paired differences, correlations) are marked as my calculation. The intervals are percentile bootstrap over the 500 problems (10,000 resamples, fixed seed), with the 4 samples per problem averaged. The logs give the evaluation settings (thinking on, temperature 0.6, top-p 0.95, top-k 20, presence penalty 1.5, at most 32,768 tokens). Terms: MLP is the fully connected part of each transformer layer. MATH-500 is a 500-problem mathematics set. IFEval evaluates instruction following. MMLU-Pro and GPQA Diamond are multiple-choice knowledge and reasoning evaluations. p10c, p25c and p50c are run names (not p-values).

The three edits are separate runs, one per budget. Table 1 lists the Qwen3.5-0.8B attempts in the logs' results table (section "Experiment 6") ([2](#ref-2)).

Table 1. Qwen3.5-0.8B attempts listed in the logs' results table (prompt versions v2 to v4). "Edit submitted" for v4 at 25 passes is inferred from scores identical to p25c; the excerpt leaves its note blank. The table also has v5 rows whose results are not filled in.

| Attempt | Passes | MATH-500 (%) | GSM8K (%) | Edit submitted |
| --- | ---: | ---: | ---: | --- |
| v2, 0 passes | 0 | 7.9 | 13.8 | no |
| v3, 5 passes | 5 | 7.9 | 13.8 | no |
| v3, 10 passes (p10c) | 10 | 12.3 | 25.7 | yes |
| v3, 25 passes (p25c) | 25 | 14.1 | 25.1 | yes |
| v3, 50 passes (p50c) | 50 | 48.1 | 67.1 | yes |
| v4, 10 passes | 10 | 7.9 | 13.8 | no |
| v4, 25 passes | 25 | 14.1 | 25.1 | yes (inferred) |

## Discussion by issue

### The difference is about 40 points and is clear within the 500 problems

MATH-500 accuracy is 7.9% for the baseline (95% interval 6.1 to 9.9%, my calculation) and 48.1% for the 50-pass edit (p50c; 44.4 to 51.8%). The ratio is 6.09 and the difference 40.2 points (36.9 to 43.6). Paired by problem, 306 of the 500 problems have more correct samples, none have fewer, and 194 are unchanged (my calculation; this compares per-problem counts of correct samples and is not a test). Problems with at least one correct sample rose from 77 to 320. Within this evaluation, that a difference exists is clear. It is, however, one run of one edit, on a fixed set of problems (MATH-500) with 4 samples per problem, and the interval does not include run-to-run variation of the editing.

### The baseline is a model whose outputs hit the length limit 93% of the time

The denominator of the difference (7.9%) is the accuracy of a baseline in which 93.0% of samples were cut off at the 32,768-token limit ([2](#ref-2)). The blog itself says that the baseline repeats the same text and rarely reaches an answer, that Qwen's model card warns of this tendency, and that fixing the loops lets the model finish answers it could already work out ([1](#ref-1)); the blog's table also has a column for the share hitting the limit. What this note adds is the size in numbers. On MATH-500 the share of samples that finished was 7.0% for the baseline and 66.9% for p50c, a 9.6-fold rise (my calculation), larger than the ratio of accuracies (6.09). Since easier problems are more likely to finish, this is an exploratory number.

Being cut off is not the same as having no answer. The logs grade the last `\boxed{}` answer ([2](#ref-2)). For the baseline, of 2,000 samples 1,860 were cut off and 140 finished, and 158 were correct. Even if every finished sample were correct there would be only 140, so at least 18 correct samples (at least 11.4% of the correct ones) were graded from an answer inside a cut-off output (my calculation; a lower bound under the assumption that the set of cut-off samples and the set of graded samples are the same, and the actual number could be counted from the generated texts in the logs). For p50c, 1,339 finished and 962 were correct, and this lower bound is 0.

### The budgets of 10, 25 and 50 passes are separate runs with different edits, not one edit with a changed budget

The blog compares budgets of 10, 25 and 50 forward passes, but according to the logs the three runs proceeded separately and arrived at different edits ([2](#ref-2)). The 10-pass run (p10c) removes a loop direction from 30 output matrices in layers 8 to 22 (\(W' = W - 1.5\,u(u^\top W)\)), an edit that touches almost every entry. The 25-pass run (p25c) switches off attention head 7 of layer 15 (zeroing its 256 output columns). The 50-pass run (p50c) subtracts the direction from the 64 columns, per layer, of the MLPs of layers 15 and 19 that write it most. The blog does not claim a dose-response with budget on the axis, but a table that lines up the three numbers invites that reading. In fact they are three separate runs with different budgets, and the reported runs are one per budget (Table 1 shows other attempts at the same budgets).

The differences over the baseline are 4.45 points (2.8 to 6.2) at 10 passes, 6.2 points (4.6 to 7.9) at 25 passes and 40.2 points at 50 passes. The difference between 10 and 25 passes is 1.75 points, and the lower end of its interval (0.05 to 3.6) is near 0 and, depending on the random seed, includes 0. The five paired differences were not corrected for multiplicity. From 25 to 50 passes the jump is 34.0 points (30.9 to 37.0) (Figure 1, Table 2). Accuracy did not grow smoothly with budget; what the numbers show is that the 50-pass run reached an edit that lowers the cut-off share from 93% to 33%. The logs' results table also lists runs that did not submit an edit (5 passes, v4 at 10 passes) and rows that evaluate candidates that were not submitted (p05c at 8.6%, p10d at 10.1%; not in Table 1), and the logs say they include only the runs the blog reports ([2](#ref-2)). The total number of attempts and how the reported ones were chosen cannot be known from what is published.

![Figure 1. MATH-500 accuracy (bars, 95% bootstrap interval over 500 problems) and the share of samples cut off at the 32,768-token limit (dashed line). The three edits are separate, one run each (my calculation, numbers from the logs).](shared/weight-space-programming-qwen-loop/figures/01-math500-runs.png)

Table 2. MATH-500 results (my calculation; intervals are bootstrap over 500 problems).

| Run | Edit (from the logs) | Accuracy (%) | 95% interval | Cut at limit (%) | Problems with any correct |
| --- | --- | ---: | --- | ---: | ---: |
| Unedited | none | 7.9 | 6.1 to 9.9 | 93.0 | 77 |
| p10c | rank-one removal in 30 matrices, layers 8-22 | 12.3 | 10.2 to 14.6 | 87.2 | 126 |
| p25c | attention head 7 of layer 15 switched off | 14.1 | 11.8 to 16.5 | 86.4 | 140 |
| p50c | loop direction removed from 64 columns of the MLPs of layers 15 and 19 | 48.1 | 44.4 to 51.8 | 33.1 | 320 |

### 0.016% is the size of the p50c edit, not the size of its effect

The 0.016% is the 131,072 weights of the p50c edit (two MLP matrices × 64 columns × 1,024 rows, from the logs' description) divided by 0.8B (a nominal size; 0.0164% in my calculation). According to the logs, 130,188 of these weights differ from the original after rounding to bfloat16. The 10-pass edit touches almost every entry of 30 matrices, so 0.016% does not apply to the other runs. Nor does a small share of touched weights mean a small effect: the edit removes one direction, and how strongly that direction acts on the model's output decides the effect. The blog itself explains that it traced the looping to one direction ([1](#ref-1)).

### Gains outside mathematics move together with the drop in cut-off outputs

The 50-pass edit also raises non-mathematical measures: IFEval from 21.0% to 62.3% (about 3x), MMLU-Pro from 40.3% to 45.5% and GPQA Diamond from 22.7% to 36.6% ([2](#ref-2)). Across the same ten benchmarks, the rise in accuracy (points) against the baseline and the drop in the cut-off share (points) are strongly correlated (Pearson 0.88, Spearman 0.90, my calculation; Figure 2). Part of this correlation is expected by construction: a cut-off sample is unlikely to be correct, so accuracy can hardly rise unless samples finish. The ten points also include MATH-500 and GSM8K themselves, differ in sample counts and difficulty, and come from the same model and the same runs, so this is exploratory. IFEval is graded on the answer after `</think>`, so a cut-off output can be a non-answer (the logs do not say how a missing `</think>` is handled). The baseline had 74.9% cut off and the edited model 2.2%. The blog explains that the loops are not special to mathematics, so performance beyond mathematics improved too ([1](#ref-1)). The numbers in the logs do not contradict that explanation.

![Figure 2. Across ten benchmarks, the gain in accuracy (vertical) of the 50-pass edit (p50c) over the baseline against the drop in the share of samples cut off at the length limit (horizontal). Exploratory (my calculation, numbers from the logs).](shared/weight-space-programming-qwen-loop/figures/02-gain-vs-truncation-drop.png)

The blog reports that the same method did not establish an improvement on a model that rarely loops (Gemma 3 270M, 8.5% cut off, but at an 8,192-token limit, different from Qwen's 32,768) ([1](#ref-1)). MATH-500 was 6.8% for the baseline; after editing it was 7.0 to 7.7% for runs whose prompt stated lenient grading and 6.1 to 6.7% for runs whose prompt stated strict grading, the latter at or below the baseline (all values under lenient grading, from the logs' results table). The blog's authors state that editing cannot add an ability but can remove an obstacle that hid one ([1](#ref-1)). This interpretation is consistent with the numbers above. The contrast with Gemma is not, however, a controlled comparison: model, sampling and limit differ.

### Questions this experiment does not answer

The experiment has no comparison with simple ways of suppressing repetition without editing (changing the sampling settings, evaluating with thinking off, changing the token limit). The baseline is a value measured with thinking on, sampling settings that include a presence penalty of 1.5, and 32,768 tokens. The authors do not claim that the edit beats such simple measures. For that reason, whether the edit's effect is large compared with them cannot be known from what is published. The computational cost of the edit is also not shown in a comparable form: p50c took 158 turns, 80 Python runs and about 20.3 hours (including 4.7 hours waiting for a model connection; from the logs' description), which is not a comparison with the cost of fine-tuning.

## Overall assessment

What could be confirmed as fact is as follows. On MATH-500, the difference from 7.9% to 48.1% is clear within the 500 problems (40.2 points, interval 36.9 to 43.6), with 306 problems having more correct samples and none fewer. The baseline has 93% of samples at the length limit, and at least 11.4% of its correct samples were graded from an answer inside a cut-off output. The three budgets are separate runs with different edits, and the reported runs are one per budget. The 0.016% is the size of the p50c edit. The size of the gains outside mathematics goes with the size of the drop in cut-off outputs.

By interpretation: the main content of the difference is naturally read as the effect of reducing outputs cut off by repetition (which agrees with the blog authors' own explanation). According to the blog, Astra identified the cause as a direction and wrote the edit; this note did not verify that. A relation in which more budget gives more performance cannot be stated from these three runs.

## Limitations

- This note uses only the numbers in the published blog and logs and did not rerun Astra or the edited model. The edited model is released on Hugging Face, but I did not check it.
- The experiment covers one model (Qwen3.5-0.8B), one evaluation setting and, for the reported runs, one run per budget. The total number of attempts and how they were selected cannot be known from what is published.
- The intervals are bootstrap over 500 problems, do not include run-to-run variation of the editing, and the several paired differences are not corrected for multiplicity.
- The correlation between cut-off share and accuracy is from ten points, partly true by construction, exploratory, and does not show causation.
- A comparison with a simple baseline for suppressing repetition without editing is not published.
- The blog's other experiments (such as writing game networks from scratch) are not treated.
- The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

The difference from 7.9% to 48.1% is clear within the 500 problems (40.2 points), but the baseline is a model in which 93% of samples hit the length limit, and the improvement shows up on other benchmarks together with the drop in cut-off outputs. The three budgets are separate runs with different edits, and 0.016% is the size of the p50c edit. The numbers are consistent with the blog authors' own reading that this is the effect of one edit that removes repetition.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`), the input tables (per-problem correct counts, sample totals and a benchmark summary extracted from the public logs, which are CC BY 4.0, by Rikiya Takehi, [license](https://creativecommons.org/licenses/by/4.0/); this note extracted numbers and recomputed from them) and result tables are in the companion archive. Run with Python 3.12, NumPy 2.2, pandas 2.2 and Matplotlib 3.9: `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The seed of the bootstrap is fixed at 20261104. The output can be compared with the tables in `results/`. Astra and the models are not run.

The full re-run materials are in the [companion archive](shared/weight-space-programming-qwen-loop/weight-space-programming-qwen-loop-companion.zip).


## References

<span id="ref-1"></span>1. Takehi R, Teoh J, Zhang A, Khattab O. Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights [Internet]. rikiyat.github.io. 2026 Nov 2 [cited 2026 Nov 4]. Available from: https://rikiyat.github.io/blog/weight-space-programming/. Blog post, not peer reviewed. Full text read.

<span id="ref-2"></span>2. Takehi R. lm_understand-logs: logs of the Weight-Space Programming experiments [Dataset]. GitHub. 2026 [cited 2026 Nov 4]. Available from: https://github.com/RikiyaT/lm_understand-logs. Data under CC BY 4.0. Experiment 8 README, results table (eval/RESULTS_excerpt.md) and MATH-500 per-problem scores read; the repository state at the cited date, no release tag.
