Reference date: the facts in this article are as of 3 November 2026.

Studies that search for novel proteins and peptides by mass spectrometry enlarge the search space to examine candidates that are not in the database. A news article in Nature Biotechnology says, in its summary line, that mining the "dark proteome" has uncovered thousands of previously missed proteins, including some that may be targets for cancer immunotherapy ([1](#ref-1)). Of that news article, I could read only the bibliographic details and the summary line; the full text is behind a subscription and was not read. This note therefore does not address the methods or results used there. It addresses a statistical point about the target-decoy method generally used for peptide identification in mass spectrometry: even when the overall false discovery rate (FDR) is controlled at 1%, the error proportion among the candidates added by enlarging the search space (the novel candidates) need not be 1%. A simulation is used to show this.

## Problem formulation

There are two questions. (1) When the overall FDR is set to 1%, what fraction of the peptides called novel are wrong, and how much does that depend on the breadth of the search space and on the prior share of novel peptides (how rare novel peptides are to begin with)? (2) What happens to that fraction, and what is lost, when the FDR is set separately for the novel part?

## Assumptions and definitions

Terms: a peptide-spectrum match (PSM) is one pairing of a spectrum with a candidate peptide in the database. A canonical candidate is a sequence from a known protein; a noncanonical candidate is a sequence from, for example, an open reading frame (ORF) whose translation is unconfirmed. In this note, the noncanonical candidates added by enlarging the search space are called novel candidates. In the target-decoy method, fake sequences (decoys) of the same size as the real ones (targets) are included in the same database; for PSMs above a score threshold, the number of decoys divided by the number of targets is the FDR estimate ([2](#ref-2)). The true false discovery proportion (FDP) is the proportion of accepted PSMs that are actually wrong; in a simulation, the truth is known, so it can be computed.

## Known points

Studies searching for noncanonical proteins have made the following points. When all-frame translation enlarges the database, false positives increase at an unacceptable rate, and because the target-decoy FDR depends on database size, comparing databases of very different sizes is difficult ([3](#ref-3)). In a study that searched more than 640,000 predicted noncanonical ORFs, 2.2% were supported by at least one peptide; because a large search space produces many false positives, global FDR control was followed by peptide-centric validation ([4](#ref-4)). Another study argued that a combined canonical and noncanonical FDR badly underestimates noncanonical errors and proposed estimating the two separately; it cites, as a report by Woo et al., about 36% for noncanonical versus 0.03% for canonical at a nominal 1% ([5](#ref-5)). I did not check the original source of these numbers. The statements attributed to references 3–5 were checked by reading the full-text page of each (PMC or the publisher).

## Simulation methods

I simulated target-decoy competition at the PSM level. All parameters are assumptions (Table 1). Each spectrum truly comes from a canonical peptide, a noncanonical peptide, or neither (not in the database). The score of a true candidate follows a normal distribution with mean 5 and standard deviation 1, and that of a wrong candidate a normal distribution with mean 0 and standard deviation 1. Each spectrum is compared with 300 canonical candidates within the precursor tolerance and \(F\) times as many novel candidates. The best wrong score among \(n\) candidates was drawn exactly as the maximum of \(n\) standard normal variables by inverse cumulative distribution. The decoy database has the same size and composition, and for each spectrum the higher of the best target and best decoy hits is kept. The FDR estimate is the number of decoy PSMs above a threshold divided by the number of target PSMs.

Table 1. Simulation assumptions.

| Parameter | Value |
| --- | --- |
| Spectra per replicate | 200,000 |
| Share of spectra from a canonical peptide | 0.30 |
| Share of spectra from a noncanonical peptide | 0.003 (1% of identifiable spectra) |
| Share of spectra from neither (no true match in the database) | 0.697 |
| Score of a true match / a wrong candidate | Normal, mean 5 / mean 0 (SD 1) |
| Canonical candidates per spectrum | 300 |
| Noncanonical candidates per spectrum | 300 × F, F = 1, 10, 30, 100 |
| Global FDR target | 1% |
| Replicates / random seed | 20 / 20261103 |

The "global threshold" is the lowest score at which the combined canonical and noncanonical FDR is 1%. The "separate threshold" is the threshold set so that the FDR of the novel candidates alone is 1%, using their own targets and decoys.

## Results

With the global FDR at 1%, both the estimated FDR and the true FDP were about 1.0%, so the overall rate was controlled correctly (Table 2). However, the true FDP among PSMs called novel reached about half: 34.7% for \(F\)=1, 48.3% for 10, 50.5% for 30 and 50.8% for 100 (Figure 1, Table 2). The true FDP of canonical PSMs fell from 0.52% to 0.01%.

![Figure 1. True false discovery proportion among accepted novel (noncanonical) PSMs against the search-space factor F (mean of 20 replicates, error bars: standard deviation). Solid orange: global threshold (true FDP). Dashed orange: FDR estimated from the same PSMs' own decoys. Blue: threshold set on the novel candidates alone (true FDP). Dotted line: 1%. Parameters are assumptions.](shared/dark-proteome-fdr-search-space/figures/01-subset-fdp-by-search-space.png)

The effect of the breadth of the search space is limited, and the effect of the low prior is large. As \(F\) rose from 1 to 10, the true FDP rose from 34.7% to 48.3%, but above 10 it plateaued at about 50%. Even at \(F\)=1, where the numbers of canonical and novel candidates are equal, the true FDP was 34.7%. In this case wrong candidates fall half and half into the two parts, while only 1% of the true matches lie on the novel side. The rarity of novel peptides is the main cause of the error proportion. Because the global threshold is set to match the overall FDR, it is too lenient when looking at the novel part alone.

When the FDR was estimated from decoys within the novel part alone, the estimate (49.6% for \(F\)=30) nearly matched the true FDP (50.5%). This is because targets and decoys compete under the same conditions within the novel part; it is not an independent check. Setting the threshold at 1% in the novel part alone lowered the true FDP to 0.8–1.7%. In exchange, fewer novel PSMs remained: for \(F\)=30, true novel PSMs fell from 274 (global threshold) to 77 (separate threshold).

Table 2. Results by search-space size \(F\) (mean ± standard deviation of 20 replicates).

| F | Global estimated FDR | Global true FDP | Noncanonical accepted (global threshold) | Noncanonical true FDP (global threshold) | True noncanonical PSMs, global threshold | True noncanonical PSMs, separate threshold | Noncanonical true FDP (separate threshold) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 1.00% | 1.02% | 647 | 34.7 ± 2.0% | 422 ± 15 | 215 ± 36 | 1.3 ± 0.9% |
| 10 | 1.00% | 1.03% | 664 | 48.3 ± 2.5% | 342 ± 16 | 118 ± 31 | 0.8 ± 0.8% |
| 30 | 1.00% | 1.02% | 554 | 50.5 ± 2.3% | 274 ± 13 | 77 ± 32 | 1.4 ± 2.1% |
| 100 | 1.00% | 1.00% | 422 | 50.8 ± 2.7% | 207 ± 7 | 51 ± 20 | 1.7 ± 2.1% |

Changing the prior share of novel peptides moved the error proportion greatly (Figure 2; \(F\)=30, mean of 10 replicates; the baseline 0.3% row differs slightly from the 20-replicate mean in Table 2, 50.3% versus 50.5%). When 0.03% of spectra were novel, the true FDP of novel PSMs at the global threshold was 90.3%; it was 74.8% at 0.1%, 50.3% at 0.3% and 23.6% at 1%. At the separate threshold, the corresponding values were 7.1%, 3.3%, 1.8% and 1.0%; the lower the prior, the further even the separate threshold departed from 1%.

![Figure 2. Share of spectra from noncanonical peptides and the error proportion among accepted novel PSMs (F = 30, mean of 10 replicates, error bars: standard deviation). Orange: global threshold; blue: threshold set on the novel candidates alone.](shared/dark-proteome-fdr-search-space/figures/02-prior-sensitivity.png)

In a sensitivity analysis varying the score separation and the number of candidates (\(F\)=30, mean of 10 replicates), the true FDP of novel PSMs at the global threshold was again 49–51%. At the separate threshold, the true FDP was 1.0% when the mean score of true matches was 6, 1.8% when it was 5, and 7.6% when it was 4 (with about 10 novel PSMs accepted). With small separation between true and wrong scores, even the separate threshold accepts few PSMs and the error proportion far exceeds 1%.

## What validation with synthetic peptides can show

Comparing the spectrum of a synthetic peptide with the observed spectrum supports the sequence assignment for the candidates that were chosen. In the pXg paper, of 18 noncanonical peptides chosen, 14 of the 16 that could be synthesized (14 of the 18 chosen) exceeded the similarity threshold ([5](#ref-5)). This validation has limits. It checks the chosen candidates, not the error rate of the whole candidate set, and the proportion depends on which candidates are chosen. In addition, a correct sequence does not mean that it comes from a novel protein, nor that it is valuable as a target.

## Scope

- All parameters are assumptions, not values from an actual experiment. Changing the prior, the score separation or the number of candidates changes the numbers (the scans are shown above). The 35–51% figure is for a prior of 0.3%; varying the prior from 0.03% to 1% gives 24–90% (\(F\)=30).
- The simulation is at the PSM level and does not include aggregation of PSMs into peptides or proteins, precursor mass or enzyme constraints, or correlation between scores.
- Scores were taken as independent and normally distributed. Actual search-engine score distributions and biases from how decoys are built (for example reversal) are not included.
- The results do not estimate the error rate of any actual study. The numbers from the literature are as described in each paper and were not recalculated here.
- The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

Even with the overall FDR controlled at 1%, the error proportion among novel candidates alone reached 35–51% under the assumed conditions (a novel prior of 0.3%). The main cause is that novel peptides are rare a priori; the breadth of the search space (\(F\)) added about 14 points between 1 and 10 and then plateaued. Setting the FDR in the novel part alone lowers the error proportion to 0.8–1.7% in this condition, but fewer novel PSMs remain, and with a low prior or small score separation the proportion departs substantially from 1%. Validation with synthetic peptides supports the assignment of chosen candidates and does not give the error rate of the whole set.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive. Run with Python 3.12, NumPy 2.2, SciPy 1.14, pandas 2.2 and Matplotlib 3.9: `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The random seed is 20261103. The inputs are assumed parameters; no experimental data were used.

The full re-run materials are in the [companion archive](shared/dark-proteome-fdr-search-space/dark-proteome-fdr-search-space-companion.zip).


## References

<span id="ref-1"></span>1. Eisenstein M. Startups mine 'dark proteome' for new drug targets. Nat Biotechnol. 2026;44:1419–1422. Published 2026 Sep 10 [cited 2026 Nov 3]. [doi:10.1038/s41587-026-03306-x](https://doi.org/10.1038/s41587-026-03306-x). Bibliographic details and summary read; full text not read.

<span id="ref-2"></span>2. Elias JE, Gygi SP. Target-decoy search strategy for increased confidence in large-scale protein identifications by mass spectrometry. Nat Methods. 2007;4(3):207–214. [doi:10.1038/nmeth1019](https://doi.org/10.1038/nmeth1019)

<span id="ref-3"></span>3. Ruiz Cuevas MV, Hardy MP, Hollý J, Bonneil É, Durette C, Courcelles M, et al. Most non-canonical proteins uniquely populate the proteome or immunopeptidome. Cell Rep. 2021;34(10):108815. [doi:10.1016/j.celrep.2021.108815](https://doi.org/10.1016/j.celrep.2021.108815)

<span id="ref-4"></span>4. Othoum G, Maher CA. CrypticProteinDB: an integrated database of proteome and immunopeptidome derived non-canonical cancer proteins. NAR Cancer. 2023;5(2):zcad024. [doi:10.1093/narcan/zcad024](https://doi.org/10.1093/narcan/zcad024)

<span id="ref-5"></span>5. Choi S, Paek E. pXg: comprehensive identification of noncanonical MHC-I-associated peptides from de novo peptide sequencing using RNA-Seq reads. Mol Cell Proteomics. 2024;23(4):100743. [doi:10.1016/j.mcpro.2024.100743](https://doi.org/10.1016/j.mcpro.2024.100743)
