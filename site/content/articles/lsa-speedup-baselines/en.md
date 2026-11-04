Reference date: the facts in this article are as of 4 November 2026.

A preprint posted on 30 October 2026 reports Latent Sparse Attention (LSA), a method that speeds up the attention computation over long contexts (token sequences) ([1](#ref-1)). A post by the preprint's senior author presented LSA as a step toward subquadratic attention that matches the accuracy of full attention at ultra-long context (from the opening of the post as shown in a search result and a Japanese machine translation; [2](#ref-2)). The abstract states that at 10 million tokens the distilled variant (D-LSA) speeds up one attention layer by 22.7x in prefill and 4.6x in decode over the original sparse attention of GLM-5.3-Flash, and by 72.4x in prefill and 42.5x in decode over the full attention of Qwen-3.8-27B ([1](#ref-1)). The preprint itself states in the text that these are one-layer values and that whole-model speedups are smaller. As a reading aid, this note organizes from the preprint's numbers what these numbers compare (model, baseline and unit of measurement). The subject is a preprint that has not been peer reviewed, and the conclusions are limited to the printed numbers. The design of LSA and a full evaluation of its accuracy are outside this note.

## Scope and sources

I read the text and tables of the preprint; values inside figures and details of the appendices were not read in full ([1](#ref-1)). I did not run the released implementation (an SGLang extension and kernels). The numbers are of two kinds. Values reported by the preprint are quoted as printed. Values I calculated (back-calculation with Amdahl's law, confidence intervals, interpolation-based estimates) are marked as my calculation. Terms: prefill is the stage that processes the input context and decode is the stage that outputs one token at a time. TTFT is the time to the first token and TPOT the time per output token. The indexer is the part of attention that selects which keys to attend to. D-LSA is the variant added to an existing model by distillation (Flat is the flat search over all buckets, Tree a search over a hierarchy), and N-LSA is the variant trained from scratch (native training). SGLang is model-serving software. H200 and B300 are GPU types. TP, CP and DCP are ways of splitting work over several GPUs (tensor parallelism, context parallelism, and context parallelism in decode); the trailing 8 is 8 GPUs. RULER, PaperTrail, MMLU-Pro, GPQA-Diamond, MATH500 and LongBench v2 are evaluation tasks. Table 1 shows the abstract's numbers and what they time in the text.

Table 1. Speedups in the abstract and the unit of measurement in the text (as described in the preprint ([1](#ref-1))).

| Reported number | Model and baseline | What is timed |
| --- | --- | --- |
| 22.7x prefill, 4.6x decode (10M tokens) | GLM-5.3-Flash, over its original block sparse attention | One attention layer on one GPU (H200): prefill of the last chunk of 32,768 queries; decode of one step of one request |
| 72.4x prefill, 42.5x decode (10M tokens) | Qwen-3.8-27B, over full attention | The same, one layer |
| 9.2x TTFT, 2.9x TPOT (10M tokens, Qwen, H200) | Qwen-3.8-27B, over full attention | Whole model in SGLang, one request at a time |
| 2.2x TTFT, 2.1x TPOT (10M tokens, GLM, H200, CP8) | GLM-5.3-Flash, over its sparse attention | Whole model in SGLang |

Table 1 notes: TTFT is time to first token; TPOT is time per output token; CP8 is context parallelism over 8 GPUs; H200 is a GPU type; 10M is 10 million tokens.

## Discussion by issue

### 22.7x and 72.4x are values for different models against different baselines

The two numbers are not the same comparison. 22.7x is against the sparse attention that GLM-5.3-Flash already has (an indexer that scores every block of four keys), and 72.4x is against the full attention of Qwen-3.8-27B ([1](#ref-1)). Both are the time of one global attention layer at 10 million tokens. The ratio is 72.4 ÷ 22.7 = 3.2, which includes the difference between baselines (full versus sparse attention) and between models, not only LSA. The timing is of the whole layer (projections, indexer and attention) on a single GPU; prefill times the last chunk of 32,768 queries before the end of the given context, and decode times one step of one request with CUDA graphs ([1](#ref-1)).

The prefill value is the time of the last chunk, not of the prefill of the whole 10-million-token input. The per-layer prefill speedup grows with the context: on GLM-5.3-Flash it is 2.1x at 512k tokens, 3.5x at 1M and 22.7x at 10M ([1](#ref-1)). As an illustration, assume that the baseline layer time of a chunk is proportional to its position (the number of keys) and that these three points lie on a straight line on log axes; interpolating and summing the chunk times gives a speedup of the attention layers alone over a whole prefill of about 13.4 to 13.7x (with the speedup below 512k tokens set to 1x or to 2.1x; an illustrative estimate from my model, neither an upper nor a lower bound: the projection time does not depend on context, and the shape between 1M and 10M is fixed by only three points). It is not a measurement; it indicates that the whole-input value is smaller than the last-chunk value. The estimate was made for GLM only, not for Qwen.

### The speedup of a layer becomes smaller for the whole model

The preprint also measures TTFT and TPOT of the whole model on a real server (SGLang) (the preprint's Table 3). The speedups of D-LSA (Flat) at 10 million tokens are, on H200, 9.21x TTFT and 2.87x TPOT for Qwen (against 72.4x and 42.5x per layer), and for GLM 2.24x TTFT and 2.10x TPOT with CP8, and 5.83x and 1.91x with TP8 (against 22.7x and 4.6x per layer) ([1](#ref-1)). The preprint explains the gap by saying that only the global attention layers become faster while other layers keep their cost ([1](#ref-1)). Back-calculating with Amdahl's law (from the whole-model speedup S and the speedup s of the accelerated part, the share of the baseline time in the accelerated part) gives about 90% for Qwen TTFT on H200, about 58% for GLM with CP8 and about 87% with TP8, about 85% for Qwen on B300, and about 39% for GLM with CP8 and about 86% with TP8 on B300 (my calculation, Figures 1 and 2). For decode the range is about 33 to 75%.

This back-calculation is an identity, not a measured share of the attention layers, and it rests on several premises. (1) The prefill layer value is a last-chunk value; using the whole-prefill estimate (about 13.5x) raises the shares: for GLM on H200, from 58% to 60% with CP8 and from 87% to 89% with TP8 (my calculation). (2) The layer is timed on one GPU while the server runs split over 8 GPUs; communication and overlap fall into the remainder. (3) GLM with TP8 at 10 million tokens on H200 ran on 2 nodes (PP2), while B300 ran on one node ([1](#ref-1)); why the back-calculated share differs so much between CP8 and TP8 for the same model cannot be told from this alone. (4) The layer mix, and the measurement conditions of batch size 1 with the median of 3 requests, matter. (5) The assignment of the B300 layer values to models is an inference from the order of the text.

![Figure 1. Speedup of one attention layer (blue circles) and of the whole model on a server (orange squares, D-LSA (Flat)) at 10 million tokens. Left: prefill (TTFT); right: decode (TPOT). Log axes (my calculation, numbers from the preprint).](shared/lsa-speedup-baselines/figures/01-layer-vs-whole-model-speedup.png)

![Figure 2. Share of the baseline time in the accelerated part, back-calculated by Amdahl's law from the layer speedup and the whole-model speedup (my calculation, numbers from the preprint). The assignment of B300 values to models is an inference.](shared/lsa-speedup-baselines/figures/02-implied-accelerated-share.png)

### Depending on the configuration, the whole-model gain over the sparse control is 1.1x to 6.8x

Qwen-3.8-27B natively uses full attention, and the sparse-attention control (block sparse attention, Flat) was set up by the authors ([1](#ref-1)). This control is also fast against full attention. On H200 (TP8 with DCP8) at 10 million tokens, the TTFT speedup is 8.02x for block sparse attention and 9.21x for D-LSA (Flat), so D-LSA relative to block sparse attention is 1.15x (my calculation). For TPOT block sparse attention is 0.89x (slower than full attention) and D-LSA 2.87x, a ratio of 3.2. On B300 (TP8), the TTFT is 0.84x for block sparse attention and 5.73x for D-LSA, a ratio of 6.8, but the preprint notes that without DCP the prefill indexer of block sparse attention runs whole on every TP rank ([1](#ref-1)). H200 uses DCP8, so 1.15x is a value in a configuration favourable to the sparse control. It is therefore the lower end of a range of gains, and the same D-LSA value means "9.2x over full attention" or "1.1 to 6.8x over the sparse control", depending strongly on the configuration. For GLM, where the baseline is already sparse attention, the H200 gains are 2.24x (CP8) and 5.83x (TP8) in TTFT and 2.10x and 1.91x in TPOT.

### The layer speedup removes most of the removable indexer time

For GLM-5.3-Flash at 10 million tokens, the preprint estimates that 98% of the prefill time of sparse attention is spent on the indexer, and that if the indexer were free it would make sparse attention a further 58x faster in prefill and 8.9x in decode ([1](#ref-1)). The layer speedups of D-LSA, 22.7x and 4.6x, can be written as 39% and 52% of this ceiling, but as multiplicative ratios they look like less than half. In terms of time, they remove 97% (prefill) and 88% (decode) of the time that can be removed at the ceiling (1 − 1/58 and 1 − 1/8.9) (my calculation).

### "Similar accuracy" is read by sample size

The preprint says that D-LSA stays close to the baselines' accuracy on knowledge, reasoning and long-context tasks ([1](#ref-1)). The numbers of items are 2,000 for MMLU-Pro, 198 for GPQA-Diamond, 100 for MATH500, 60 for LongBench v2, 100 per task (up to 1M tokens) or 20 per task (above) for RULER, and 90 questions × 3 repeats for PaperTrail (the preprint's Table 6). The 95% confidence intervals of the baseline that the preprint's Table 7 gives (Qwen) are ±1.6 for MMLU-Pro, ±4.5 for GPQA-Diamond, ±2.7 for MATH500 and ±11.6 points for LongBench v2, and all D-LSA values lie within them ([1](#ref-1)). This judgement cannot detect differences smaller than the intervals; LongBench v2, with 60 questions, has a wide interval of 11.6 points. (The worst-case width at 50% accuracy, about 10 points for MATH500, is wider than the interval at the actual high accuracy, ±2.7.)

At 10 million tokens on Qwen, the preprint says D-LSA (Flat) exceeds full attention (63.9 versus 59.9 on RULER, 29.1 versus 19.8 on PaperTrail). Most of the gap lies in two tasks, MultiQuery and HotpotQA (92 versus 72 and 35 versus 20; the preprint's appendix). RULER at 10 million tokens is 13 tasks × 20 = 260 prompts, and the two methods answer the same prompts (a paired design). The standard error of each value is about 3.0 points, and that of the difference treated as independent is about 4.3 (z = 0.94), but this is an upper bound for a paired design. The difference becomes significant at the 5% level if the per-prompt correlation of outcomes exceeds about 0.77 (my calculation); the correlation is not reported. The preprint writes "exceeds" for the point estimate and reports no test. The difference is therefore best read as not shown (not established). PaperTrail uses a few samples from three domains and an F1 metric, and the 3 repeats of the same question are correlated, so the effective sample is about 90 questions. On GLM-5.3-Flash, D-LSA trails the baseline by up to 8 points at 2 to 5 million tokens, and the tree-search variant D-LSA (Tree) falls to 55.8 against 66.8 on RULER at 10 million tokens ([1](#ref-1)).

### N-LSA is a small-scale result

N-LSA (native training) is a small-scale result: a hybrid model of about 0.5B parameters pre-trained on 100B tokens and then trained on 12B tokens of long documents up to a 128k-token context, with one run per setting ([1](#ref-1)). The validation loss is 1.085, the same as full attention; the forward and backward pass of a layer is 1.1x faster at 64k and 1.6x at 128k, and the decay phase of the whole model is 1.24x faster to reach the same validation loss. At 128k on RULER, N-LSA is at 32.2 against 34.7 for full attention, 2.5 points lower. Peak memory is 6.8 GiB per layer against 5.8 GiB for full attention (a ratio of 1.17). The authors state that native training with larger models, longer contexts and tree search is left to future work ([1](#ref-1)).

## Overall assessment

What could be confirmed as fact is as follows. 22.7x and 72.4x are speeds of one attention layer at 10 million tokens for different models (GLM-5.3-Flash and Qwen-3.8-27B) against different baselines (sparse and full attention), and the prefill value is the time of the last chunk. The whole-model speedups on a server are smaller (9.21x for Qwen, 2.24x for GLM with CP8), and relative to the sparse control for Qwen the TTFT gain is 1.15x on H200 and 6.8x on B300, and the TPOT gain is 3.2x on H200. The layer speedups remove 97% (prefill) and 88% (decode) of the time removable at the indexer ceiling. The difference by which accuracy is said to exceed the baseline (RULER at 10 million tokens, 260 prompts) would be significant if the per-prompt correlation exceeded about 0.77, and the preprint reports no test.

By interpretation: the main point LSA shows is that the indexer cost, which takes most of the time in sparse attention, can be greatly reduced at 10 million tokens; how large the layer speedup is depends on the choice of baseline and on the share of the attention layers in the whole model. The 72.4x is best read as a layer value against full attention, kept apart from the whole-model speedup. The preprint labels these values correctly, and this note is a reading aid.

## Limitations

- This note used the numbers printed in the text and tables of the preprint and did not run the released implementation. Values inside figures and details of the appendices were not read in full.
- The assignment of the rows of the preprint's Table 3 (baseline, D-LSA (Flat), D-LSA (Tree)) was cross-checked against the numbers in the text (9.2x, 2.9x, 2.2x, 2.1x and so on). The assignment of the B300 layer values (12.5x, 42.9x, 5.2x, 18.4x) to models follows the order of the abstract and is an inference.
- The Amdahl back-calculation depends on the layer value being a last-chunk time on one GPU and ignores differences between configurations. The estimate for a whole prefill is from my model, in which the baseline layer time is proportional to context and the speedup lies on a straight line on log axes.
- The discussion of the RULER difference depends on the per-prompt correlation between methods, which is not reported. The N-LSA results are one run per setting, with no variance shown.
- This note does not treat the design of LSA or a full evaluation of its accuracy.
- The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

The "22.7x and 72.4x" of LSA are speeds of one attention layer at 10 million tokens for different models against different baselines. Whole-model speedups are 9.2x for Qwen and 2.2x for GLM (CP8), and relative to the sparse control for Qwen they range from 1.15x to 6.8x. Numbers are best read with their model, baseline and unit of measurement attached.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive. Run with Python 3.12, NumPy 2.2, SciPy 1.14, pandas 2.2 and Matplotlib 3.9: `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The inputs are the numbers printed in the preprint, written at the top of the code. No random numbers are used. The preprint's implementation was not run for this note.

The full re-run materials are in the [companion archive](shared/lsa-speedup-baselines/lsa-speedup-baselines-companion.zip).


## References

<span id="ref-1"></span>1. Kubicek A, Caciolai A, Peng L, Sumant S, Hoover B, Greenlee F, et al. Latent Sparse Attention: towards subquadratic ultra-long context attention [Preprint, version 1]. arXiv. 2026 Oct 30 [cited 2026 Nov 4]. [doi:10.48550/arXiv.2610.42147](https://doi.org/10.48550/arXiv.2610.42147). Not peer reviewed. Text and tables read; figure values and appendix details not read in full; released code not run.

<span id="ref-2"></span>2. Whittington J [@jcrwhittington]. Today we are happy to share one of our first open research releases: Latent Sparse Attention (LSA) [X post]. X. 2026 Nov 3 [cited 2026 Nov 4]. Available from: https://x.com/jcrwhittington/status/2117317159777177602. Opening text as shown in a search result and in a Japanese machine translation; not read in full. The poster is the senior author listed in the preprint.
