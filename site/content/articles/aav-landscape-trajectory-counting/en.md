Reference date: the facts in this article are as of 4 November 2026.

On 22 October 2026 a preprint on the fitness landscape (the map from sequence to function) of the adeno-associated virus (AAV) capsid protein was posted. One of its authors presented the work as a journey through a vast subspace of functional sequences that does not rely on the evolutionary record (from a post read in a Japanese machine translation; [1](#ref-1)). The preprint measures the packaging ability (how well a variant is recovered as a particle carrying a genome) of more than 230,000 variants, and reports that a sample of a few thousand revealed a huge network of function-preserving ridges, which supports billions of trajectories of up to 667 steps ([2](#ref-2)). This note reads the full text and recomputes, from the printed numbers, what counts such as "billions", "667 steps" and "a few thousand" count (the counting unit) and what the proportions are divided by (the denominator). The subject is a preprint that has not been peer reviewed, and the conclusions are limited to the printed numbers. It deals only with how to read the statistics and does not touch sequences, the content of mutations, designs or experimental procedures.

## Scope and sources

I read the full text of the preprint (PDF, 37 pages) ([2](#ref-2)). I did not use its experimental protocols for this note. The experimental data and analysis code are announced for deposit before peer-reviewed publication and are not available now, so the calculations here use only the numbers printed in the text and tables. The numbers are of two kinds. Values reported by the preprint are quoted as printed. Values I calculated (ratios to the number of orderings, intervals for proportions, back-calculated values) are marked as my calculation. The intervals are exact (Clopper–Pearson) 95% intervals. Terms: QC is the experimental quality control. Negative and positive predictive values (NPV, PPV) are the shares of variants judged "excluded" or "passing" by a rule that were actually non-viable or viable. AUROC is a discrimination measure (0.5 is chance, 1 is perfect). As competing interests, the preprint states that some authors hold equity in an AAV-related company and a related patent (including a Harvard provisional patent application), and that other authors are affiliated with Google, a company that sells machine learning services ([2](#ref-2)). I draw no conclusion from these declarations. Table 1 lists the numbers dealt with and their counting units (as described in the preprint ([2](#ref-2))).

Table 1. Numbers dealt with in this note and their counting units (as described in the preprint).

| Reported number | What is counted | Denominator or unit |
| --- | --- | --- |
| 5.4e9 circuits (at least 2e9 in each of 235 resamplings) | Closed routes visiting each of 15 seed neighborhoods once, built from viable measured variants | Described as "roughly 6% of all possible orderings" (14! = 8.7e10 reproduces it) |
| 212 to 667 steps | Single amino-acid steps along one circuit | One circuit through 15 seeds |
| 85 of 183 complete dense paths viable at every step | Paths between two seeds sampled step by step | 315 dense paths started; 183 passed QC |
| 0.44 viable at one mutation, 0.016 at five | Share of random local variants that package | Variants in the 15 neighborhoods, pooled |
| NPV 0.995, sensitivity 0.985, PPV 0.489 | Exclusion rule from universally lethal single changes | Test set not stated in the text; leave-one-seed-out analysis |
| about 1e36, 1e33 and 1e27 sequences | Combinatorial size of the explored sequence space | Assumption-dependent figures |

## Discussion by issue

### "Billions" is read as a ratio to the total number of ways to order 15 seeds

The "billions of trajectories" are the number of closed routes (Hamiltonian circuits) that visit each of 15 seeds (starting sequences) once and return ([2](#ref-2)). With measured viability calls this number is 5.4×10^9, and in each of 235 resamplings (from 4 sequencing replicates and Poisson resampling of read counts) it stayed at or above 2×10^9 and all 15 seeds remained connected ([2](#ref-2)). The preprint describes this number as "roughly 6% of all possible orderings". The number of orderings of 15 seeds, with the start fixed and direction distinguished, is 14! = 87,178,291,200; 5.4×10^9 is 6.19% of it and 2×10^9 is 2.29% (my calculation), which agrees with the text's 6%. This note therefore reads the number as a few percent of the total number of orderings. The definition of the graph (vertices, edges, whether a pair of seeds can have several paths), however, cannot be told from the text. The legend of Figure 4C says that wider edges mean more distinct paths were found; if path multiplicities are counted, the reading as a share of orderings changes. If circuits are counted without direction, the share is 12.4%. This reading is thus inferred from the agreement with 6%, not stated by the preprint. Under this reading the number is large because the total number of orderings is large (Figure 1).

![Figure 1. Number of closed routes visiting each of 15 seeds once (log axis). Grey: orderings when every pair of seeds is connected (14!); blue: reported values (measured viability calls and the minimum over 235 resamplings). Compared by position of the points only (my calculation, numbers from the preprint).](shared/aav-landscape-trajectory-counting/figures/01-circuit-counts-vs-all-orderings.png)

From the share of 6% one can get a rough density of connections among the 105 seed pairs. Assuming a random graph in which each edge exists independently with probability p and a pair has at most one edge, the expected number of circuits is \(14!\,p^{15}\), so 5.4×10^9 gives p = 0.83 (about 87 of 105 pairs) and 2×10^9 gives p = 0.78 (about 82). Counting without direction gives p = 0.87 (about 91 pairs) and 0.81 (about 86) (my calculation). The inversion fails if edges are not independent, if there are multiple edges or if the distances between seeds are unequal. It is only a scale showing that connectivity is dense, not an estimate of the actual set of edges. What the preprint shows is that all 15 seeds were connected in every resampling. That this connectivity carries more information than the count itself is my interpretation.

Next, "up to 667 steps". The text says circuits span 212 to 667 single amino-acid steps ([2](#ref-2)). Divided over 15 hops this is 14.1 to 44.5 steps per hop on average (my calculation). The seeds are said to be 8 to 26 mutations apart, and 44.5 steps exceeds that distance; a circuit of 667 steps therefore includes routes that are not shortest paths. The abstract's "up to 667 steps" is naturally read as the longest of the reported circuits, but whether it is typical cannot be told from the text.

### The proportion of paths is 27% or 46% depending on the denominator

Of the paths between two seeds followed step by step, 315 were densely sampled, 183 were completely evaluable after QC, and 85 retained viability at every measured step ([2](#ref-2)). 183 ÷ 315 = 58.1% (52.4 to 63.6%) is the QC pass rate, not a discovery rate of viability. The proportion of paths that stayed viable is 27.0% (22.2 to 32.3%) of those started and 46.4% (39.1 to 54.0%) of those completely evaluable (my calculation, Figure 2). The text uses 183 as the denominator. How many of the 132 paths dropped at QC contained non-viable steps cannot be known from what is published. Among random variants 20 or more mutations from wild type, 1,202 of 6,184 (19.4%, 18.5 to 20.4%) were viable ([2](#ref-2)).

![Figure 2. Proportions of paths and variants under different denominators (exact 95% intervals, my calculation, numbers from the preprint). From the top: the QC pass rate, the share that stayed viable (two denominators), and the viable share of random variants (not paths).](shared/aav-landscape-trajectory-counting/figures/02-path-denominators.png)

The abstract's "a few thousand" can be read as the "4,993 dense samples" in the text. The text says 22,500 samples of the sparse mode were also used, so the path samples total 27,493 ([2](#ref-2)). The text does not state whether the unit of a sample is a variant (4,993 ÷ 315 = about 15.9 samples per path), and whether the abstract's "a few thousand" refers to the dense samples alone cannot be told from the abstract's sentence.

### The local decay agrees with single-hit arithmetic at the one point of five mutations

Among random variants in the neighborhoods, the viable share falls steeply, from 0.44 at one mutation to 0.016 at five ([2](#ref-2)). In a single-hit model, in which one lethal mutation breaks the capsid, the prediction at five is \(0.44^5 = 0.0165\), close to the observed 0.016 (my calculation). With the values for random local variants (42.8% at one, 1.6% at five), \(0.428^5 = 0.0144\), a ratio of 0.90 to the observed. This is, however, agreement at the single point of five mutations. The per-mutation viability (slope per mutation) falls from 0.9 at two mutations to 0.52 at five, from the multiplicative expectation of 1. The per-mutation viability at five, the fifth root of 0.016, is 0.437 (my calculation). The text says the per-neighborhood fits gather near a common value of 0.41 and estimates the half-life of the influence of the background at about 5 mutations (95% interval 2.5 to 10.6) ([2](#ref-2)). The interval spans more than a factor of 4, so how many mutations the background influence persists is determined only roughly.

### The positive predictive value of the exclusion rule depends on the viable share

For a rule that excludes variants carrying "universally lethal" changes, the text says exclusion is reliable (NPV 0.995, sensitivity 0.985) but passing the rule does not guarantee viability (PPV 0.489) ([2](#ref-2)). If the three values come from the same 2×2 table (the text does not say which set), they fix the viable share and specificity of that set (my calculation). The viable share is about 19.9% and the specificity about 74.4% (false-positive rate 25.6%); the positive likelihood ratio is 0.985 ÷ 0.256 = 3.84, which turns the prior odds of 0.249 (= 19.9% ÷ 80.1%) into posterior odds of 0.957 (= 0.489 ÷ 0.511). The PPV is low not because the rule is weak but because the set has a viable share of only about 20%. This is an algebraic back-calculation, not a verification that the three values are consistent, and it depends on rounding. The 19.9% is close to the viable share of random variants, 19.4%.

The text says that 51.3% of the 493,816 measured variants are viable and that 98.0% of the viable ones lie within the range this rule defines ([2](#ref-2)). The 51.3% is a value for a set that merges variants from several studies, with designed and sampled variants mixed; it is not the viable rate of random variants.

### 1e36 down to 1e27 are assumption-dependent guides to coverage

The preprint states the size of the explored sequence space as about 10^36 for substitutions alone, about 10^33 after excluding the lethal set and about 10^27 in a more conservative estimate ([2](#ref-2)). Dividing the 493,816 measured variants by each gives 4.9×10^-31, 4.9×10^-28 and 4.9×10^-22 (my calculation). The numerator includes insertions and variants from four studies while the denominator is a substitutions-only space, so the types do not match; these are guides to coverage, not sampling fractions. The authors themselves state that they do not claim the measurements generalize readily to the whole space ([2](#ref-2)).

## Overall assessment

What could be confirmed as fact is as follows. The number of circuits is 6.2% (2.3% for the minimum over resamplings) of the orderings in which 15 seeds can be visited (87 billion, start fixed and direction distinguished), and all 15 seeds were connected in all 235 resamplings. The maximum of 667 steps is the longest of the reported circuits and corresponds to 14.1 to 44.5 steps per hop on average. The proportion of paths that stayed viable is 27.0% (of the 315 started) or 46.4% (of the 183 completely evaluable) depending on the denominator, and 58.1% is the QC pass rate. The decay of viability agrees with single-hit arithmetic (0.44 to the fifth power) at the point of five mutations. The low PPV of the exclusion rule can be back-calculated as the result of a viable share of about 20% in the set examined, and is not determined by the strength of the rule alone.

By interpretation: the information in this result lies in the connectivity, that all 15 seeds were connected in every resampling, more than in the figure of billions. Numbers are best read with their counting unit and denominator attached. The extrapolation of the size of the space is, as the authors say, a guide to coverage that does not claim generalization.

## Limitations

- This note used only the numbers printed in the text and tables of the preprint. The experimental data and analysis code are unpublished (announced for deposit before peer review) and were not recomputed. Values inside figures and details of the supplement were not read in full.
- The graph behind the circuit counts (definition of edges, multiplicity, direction) cannot be told from the text, so the reading as a share of orderings and the back-calculated edge density are scales that depend on assumptions.
- What the paths dropped at QC contained is not known. The unit of a sample (variant or not) is not stated in the text.
- The back-calculation for the exclusion rule depends on the assumption that the three values refer to the same set, and it is algebraic.
- This note does not treat sequences, the content of mutations, designs or experimental procedures.
- The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

"Billions of functional trajectories from a sample of a few thousand" is a count of circuits that is about 6% of the 87 billion orderings of 15 seeds (about 2% for the minimum over resamplings), and its information lies in the fact that all 15 seeds were connected in every resampling. The maximum of 667 steps is the longest of the reported circuits, and the proportion of paths that stayed viable is 27% or 46% depending on the denominator.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive. Run with Python 3.12, NumPy 2.2, SciPy 1.14, pandas 2.2 and Matplotlib 3.9: `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The inputs are the numbers printed in the preprint, written at the top of the code. No random numbers are used. The preprint's experimental data are unpublished at the time of this note.

The full re-run materials are in the [companion archive](shared/aav-landscape-trajectory-counting/aav-landscape-trajectory-counting-companion.zip).


## References

<span id="ref-1"></span>1. Sinai S [@samsinai]. 1/ Like many nerdy teenagers, cosmology was deeply fascinating to me [X post]. X. 2026 Nov 2 [cited 2026 Nov 4]. Available from: https://x.com/samsinai/status/2117002122034020818. The opening post was read in a Japanese machine translation; the English opening words are given as an identifying label and are not a verified quotation.

<span id="ref-2"></span>2. Sinai S, Gane A, Jain N, Bryant D, Bileschi M, Bashir A, et al. A vast navigable protein sequence subspace [Preprint, version 1]. bioRxiv. 2026 Oct 22 [cited 2026 Nov 4]. [doi:10.64898/2026.10.18.759989](https://doi.org/10.64898/2026.10.18.759989). Not peer reviewed. Full text read; data and code announced for deposit, not yet available.
