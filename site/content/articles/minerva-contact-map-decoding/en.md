Does connecting the darkest spots in a contact map produce an RNA structure? Minerva uses a genome language model to investigate coevolution in prokaryotic non-coding regions. Discovering RNA candidates attracts attention, but the public implementation contains another step: choosing a structure from the map ([1](#ref-1)).

I examined that step with a small artificial example. On the same map, selecting high-scoring pairs one at a time yields one pair; maximizing the total weight across compatible choices yields two. The model has not changed. **The conversion of a fixed output into a structure changes which base pairs are selected.**

## Scope and sources

I checked the official README and RNA-structure code on November 1, 2026. The examined version is 0.2.2, commit `900fb32a427f2ebed601569257877167ea45c9ed`. I did not load Minerva weights or repeat genome-wide discovery. This is not an independent re-evaluation of the full preprint, and it does not assess counts of functionally validated RNAs.

According to the README, the input is not restricted to a plain DNA string. It mixes amino acids for coding regions, nucleotides for non-coding regions and dedicated orientation tokens. Separate output maps address base pairing, proteins and repeats. The discussion below concerns only post-processing of `base_pairing` ([2](#ref-2)).

I extracted four unchanged function definitions, including `call_base_pairs`, and ran them on the artificial map. Only NumPy operations were required; model and plotting modules were not loaded. Their results were compared with an independent small implementation at four thresholds.

## Proposing partners and choosing one

The examined implementation first symmetrizes the matrix with the elementwise maximum of the map and its transpose. It excludes self-pairs and positions that are too close, then proposes the highest-scoring partner for each position. Defaults require a position difference of at least three and a score threshold of 0.6 ([3](#ref-3)).

`match_candidates` then examines candidates above or equal to the threshold in descending score order. It accepts a pair if neither position has already been used. This is a greedy way to give each position at most one partner. The default 0.6 is a software setting; this article has not established that it means a calibrated 60% probability of a true base pair.

The one-partner constraint is respected. However, a pair chosen early can prevent two later candidates from being chosen together. The ranking of individual edges is not the ranking of complete combinations.

## One high pair or two slightly lower pairs

I assigned the weights in Table 1 to an artificial eight-position sequence, `GGAAAACC`. Positions are zero-based, all unlisted weights are zero and the matrix is symmetric. Neither the sequence nor the weights are a Minerva prediction.

**Table 1. Positive weights in the artificial map**

| Position pair | Base pair | Weight |
| --- | --- | ---: |
| 0–6 | G–C | 0.9 |
| 0–7 | G–C | 0.8 |
| 1–6 | G–C | 0.8 |

All three survive the per-position best-partner proposal step and meet the 0.6 threshold. Thus, this example isolates combination selection rather than mixing it with a difference in candidate pruning.

The greedy method first selects 0–6. Pair 0–7 then conflicts at position 0, and 1–6 conflicts at position 6. Both are rejected. The result is one pair with total weight 0.9.

For comparison, I enumerated all eight subsets of the three candidate edges, retained those that do not reuse a position and maximized their summed weight. This selects 0–7 and 1–6, totaling 1.6. The two pairs are nested: allowing a pseudoknot is not the reason for the difference.

![The same artificial map yields one greedy pair or two nested maximum-weight pairs](shared/minerva-contact-map-decoding/figures/decoding.png)

Figure 1. Artificial map and two selections. The left panel displays invented weights, not probabilities. Arcs in the other panels identify position pairs, not molecular three-dimensional geometry or free energy. Sequence and map are fixed.

Table 2 shows the four threshold conditions, including the default. The official functions and independent greedy implementation agreed in every condition.

**Table 2. Thresholds and selected combinations**

| Threshold | Greedy position pairs | Weight sum | Maximum-weight position pairs by enumeration | Weight sum |
| ---: | --- | ---: | --- | ---: |
| 0.60 | 0–6 | 0.9 | 0–7 and 1–6 | 1.6 |
| 0.80 | 0–6 | 0.9 | 0–7 and 1–6 | 1.6 |
| 0.90 | 0–6 | 0.9 | 0–6 | 0.9 |
| 0.91 | None | 0.0 | None | 0.0 |

Raising the threshold can make the outputs agree. That agreement does not establish that the discarded candidates were biologically wrong. The numbers are known here because the input was constructed; interpreting 0.8 in a real map remains a question for the model and its evaluation.

## Maximum weight is not physical ground truth

The calculation establishes only that the examined greedy post-processing does not always maximize the sum of candidate weights. It does not establish that the maximum-weight choice is closer to an actual RNA structure.

Summing weights was a comparison objective chosen here. I did not calculate free energy accounting for loops, stacking, salt, temperature or intermolecular interactions. Even if weights were calibrated probabilities, simply adding probabilities of dependent base pairs would not necessarily identify the most probable complete structure. Neither 1.6 nor 0.9 has units of physical stability.

The implementation's `canonical_fraction` reports the fraction of selected pairs that are Watson–Crick or G–U pairs; it does not use that value to filter the selection. A drawable structure and separate checks of base compatibility or physical plausibility should therefore remain distinct ([3](#ref-3)).

## The region to be structured is another choice

In mixed input, a genome position and a token position are not interchangeable. Coding stretches have been represented by amino acids. Map positions cannot simply be read as nucleotide coordinates. The official `call_structures` processes each contiguous nucleotide-token region separately ([2](#ref-2), [3](#ref-3)).

That is the implementation's analysis unit, not an experimental determination of transcription start and termination sites. Prokaryotic transcripts can span coding regions. The region treated as one RNA candidate is part of the interpretation when converting a map into a structure.

This check is limited to eight positions and three positive candidate edges. It does not measure how often greedy and alternative decoding differ on actual Minerva outputs, which one better recovers experimental structures, or the accuracy of coevolution prediction.

It nevertheless exposes a decision between map and structure. Candidate generation, threshold, partner conflicts and the RNA region must be fixed before a comparison of the predicted structure is well defined. A coevolutionary map is useful input; it does not by itself provide a unique RNA structure or functional validation.

## Data and code availability

The [independent calculation](shared/minerva-contact-map-decoding/analysis.py), [result CSV](shared/minerva-contact-map-decoding/results/decoding.csv), [result JSON](shared/minerva-contact-map-decoding/results/results.json), [figure code](shared/minerva-contact-map-decoding/make_figure.py) and [reproduction instructions](shared/minerva-contact-map-decoding/REPRODUCE.md) are available. Numeric calculations use Python 3.12.4 and the standard library without randomness. The comparison with four official functions used NumPy; a [verification record](shared/minerva-contact-map-decoding/upstream-verification.json) is included. Model weights, experimentally measured structures and original-paper figures are not redistributed.

## References

1. <span id="ref-1"></span>Li DB, Brixi G, Kim AS, Fiamenghi MB, Driscoll CL, Evans SA, et al. Coevolutionary mining of prokaryotic non-coding elements with a genome language model [Preprint]. bioRxiv; 2026. Version 2, 2026 Sep 24. [doi:10.64898/2026.09.22.753630](https://doi.org/10.64898/2026.09.22.753630). Full preprint not independently re-evaluated here.
2. <span id="ref-2"></span>Minerva developers. [Minerva README](https://github.com/garykbrixi/minerva/blob/900fb32a427f2ebed601569257877167ea45c9ed/README.md) [Software documentation]. GitHub; 2026 [cited 2026 Nov 1]. Version 0.2.2, commit 900fb32a427f2ebed601569257877167ea45c9ed.
3. <span id="ref-3"></span>Minerva developers. [rna_structure.py](https://github.com/garykbrixi/minerva/blob/900fb32a427f2ebed601569257877167ea45c9ed/minerva/rna_structure.py) [Software source]. GitHub; 2026 [cited 2026 Nov 1]. Commit 900fb32a427f2ebed601569257877167ea45c9ed; Git blob 7d97d12bf8d909c0bbd7e74025cae789e29a0bd7.
