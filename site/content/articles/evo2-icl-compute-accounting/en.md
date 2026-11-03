Reference date: the facts in this article are as of 3 November 2026.

A preprint posted on 29 October 2026 reports that the genome language model Evo 2 can computationally design CRISPR-Cas loci, bacteriophage genomes, antibodies and more from examples placed in the prompt, without additional training (in-context learning, ICL) ([1](#ref-1)). The report includes compute comparisons such as "about 900 H100 hours with fine-tuning versus 81 hours with ICL for a CRISPR-Cas locus" and "about 200 GPU hours with fine-tuning (162 with the evo2-flash engine) versus 2.1 GPU hours with ICL for a phage genome" (H100 is the name of the GPU product used for computation, and an H100 hour is one such unit used for one hour). These numbers compare libraries of 64 passing designs, and this note does not contradict them. It decomposes what the comparisons compare, using pass rate and amortization (spreading a fixed cost), and shows how to read them when the conditions are widened. It deals only with compute accounting and does not touch sequences, how prompts are constructed, or procedures. All results are computational (in silico) metrics, not experimental confirmation of function.

## Scope and sources

I read the full text of the preprint (PDF, 24 pages) ([1](#ref-1)). It has not been peer reviewed. Quoted numbers are from the text, figure legends and methods. The supplementary material was not read. The calculations are arithmetic on the reported numbers, not a re-run of the models. Quantities the preprint does not state (the sampling time within the fine-tuning total of about 900 hours, time per sample, the split of the 162–200 hours for phage) were derived under stated assumptions and are labelled as such. Table 1 shows the reported comparisons (ICL is in-context learning and a GPU is a graphics processing unit used for computation).

Table 1. Compute comparisons reported in the preprint ([1](#ref-1)).

| Task | Reported pass rate (ICL vs fine-tuned) | Reported compute |
| --- | --- | --- |
| CRISPR-Cas locus (Evo 2 7B ICL vs fine-tuned Evo 1) | 0.14% vs 0.39% (pooled over temperatures and prompt settings) | 64 passing designs: 81 H100 hours (ICL) vs about 900 (fine-tuned; 881 of them fine-tuning) |
| Phage genome (ICL vs fine-tuned Evo 2) | 0.25% vs 0.015% (correctness and all novelty filters) | 64 passing designs: 2.1 GPU hours (ICL) vs about 200 (162 with evo2-flash), fine-tuning and inference |
| Antibody (ICL vs three baselines) | ICL yields at least one hit for every antigen tested | Fixed budget per antigen: 1 GPU-hour for design and 1 for scoring |

## Discussion by issue

### The unit of comparison

Consider the compute needed to obtain \(N\) passing designs in a library. Let \(F\) be a fixed cost (such as fine-tuning), \(t\) the compute time per sample and \(p\) the per-sample pass rate. The marginal cost per passing design is \(c=t/p\), and the total is \(F + cN\) (a linear-in-\(N\) assumption). ICL is taken to have \(F\) close to 0 and may have a larger \(t\) (a long prompt must be processed). Fine-tuning has a large \(F\) and a smaller \(t\). Which is cheaper depends on \(N\) and \(p\). The preprint's comparison is at a single point, \(N\) = 64.

### CRISPR-Cas loci: the saving holds only while the library is small

The per-sample pass rate is lower for ICL (0.14%) than for fine-tuning (0.39%) ([1](#ref-1)). To obtain 64 passing designs, about 45,700 samples are needed with ICL and about 16,400 with fine-tuning at these rates (the rates pool settings and are not the pass rates of the best settings used for the time comparison, so these counts are not converted to hours). Even so, the total is 81 hours for ICL and about 900 hours for fine-tuning, of which 881 hours are fine-tuning itself, a difference of about 11-fold (900 ÷ 81).

The preprint writes the fine-tuning total as "about 900 hours" and does not show the sampling time within it. I took the roughly 19 hours left after subtracting 881 from 900 to be sampling. This is my own subtraction, not an estimate by the preprint. The total to obtain \(N\) passing designs is \(81N/64\) for ICL (1.27 hours per design) and \(881 + 19N/64\) for fine-tuning (a marginal cost of 0.30 hours per design). The two are equal at \(N\) of about 909. This value, however, is very sensitive to the rounding of "about 900". If the sampling time is 0–40 hours, it is 696–1,375; if the total were 950 hours (69 hours of sampling), about 4,700; and if the sampling time were 81 hours or more, there is no \(N\) at which fine-tuning is cheaper (Figure 1, Table 2). The break-even lies somewhere between several hundred and several thousand, and about 900 is only a guide.

Table 2. Break-even for CRISPR-Cas loci by assumed sampling time within the fine-tuned total (my calculation).

| Sampling hours assumed inside the fine-tuned total | Break-even number of passing designs |
| ---: | ---: |
| 0 | 696 |
| 19 (900 minus 881) | 909 |
| 40 | 1,375 |
| 69 (total of 950) | 4,699 |
| 81 or more | none (ICL cheaper at every N) |

![Figure 1. H100 hours needed for a given number of passing designs in CRISPR-Cas locus design. Blue: ICL (81 hours for 64 designs). Orange: fine-tuning (a fixed 881 hours plus sampling). The band is sampling of 0–40 hours per 64 designs. Black dots: the values reported in the preprint for 64 designs (81 and about 900). The break-even position depends on the assumption of 19 sampling hours.](shared/evo2-icl-compute-accounting/figures/01-cas9-hours-by-library-size.png)

The conditions of the comparison also differ. According to the methods, the pass rates pool temperatures and settings, whereas the time comparison uses the best ICL setting and the best setting of the fine-tuned side, and the sampling time of the fine-tuned model is an estimate based on measuring generation with the Evo 1 code ([1](#ref-1)). Moreover, the comparison is between fine-tuned Evo 1 and Evo 2 7B ICL, so the models are not the same.

The 881 hours is the cost of the fine-tuning that the preprint performed for its own comparison. For a user who reuses a model that has already been fine-tuned, the fixed cost is already paid (a sunk cost) and only the marginal cost matters. Sharing the fixed cost across several tasks also changes how amortization looks. The break-even in this note is for one task, with the fixed cost paid once, and does not include reuse across tasks.

### Phage genomes: the saving at 64 designs is avoided fixed cost, the marginal advantage is the pass-rate difference

For phage (ΦX174-like), ICL has a higher pass rate. The correctness-filter pass rate is 51.7% versus 13.0%, and the rate of passing correctness plus all three novelty filters is 0.25% versus 0.015% ([1](#ref-1)). To obtain 64 designs, about 25,600 samples are needed with ICL and about 426,700 with fine-tuning, a ratio of 16.7. The reported time ratio is 77 (162 hours, evo2-flash) or 95 (about 200 hours, plain engine), larger than the sample ratio of 16.7.

The remaining difference is in the fixed cost of fine-tuning or in the time per sample, and cannot be separated from the text of the preprint. If the fine-tuned model's time per sample is assumed to equal that of ICL, and the 2.1 and 162 hours are assumed to be values for the same engine, sampling on the fine-tuned side is about 35 hours and the fixed cost is 127 hours (162 − 35) or 165 hours (200 − 35). Under this assumption, fixed cost accounts for about 78% (127 ÷ 162) of the total for 64 designs, and most of the saving at 64 designs is avoided fixed cost. The marginal cost, on the other hand, is 0.033 hours per design for ICL and 0.55 for fine-tuning, so ICL is cheaper even without the fixed cost. For fine-tuning to match ICL in marginal cost, its time per sample would have to be at most 1/16.7 of ICL's (the pass-rate ratio itself). In other words, the difference at 64 designs owes largely to avoiding fixed cost, and the advantage that remains as the library grows comes from the high pass rate. This decomposition assumes equal time per sample and measurement under the same conditions; if the time per sample is smaller on the fine-tuned side, the fixed-cost share is larger still. The pass rate of the fine-tuned side pools several hyperparameters and is not the value of its best setting.

![Figure 2. Reported compute time to obtain 64 phage genomes and an assumed breakdown. Blue: ICL (2.1 hours). Orange: fine-tuning (162 or 200 hours) divided into fixed hours such as fine-tuning (light) and sampling (dark). The breakdown assumes that the fine-tuned model takes the same time per sample as ICL; it is not in the preprint.](shared/evo2-icl-compute-accounting/figures/02-phage-hours-decomposition.png)

### Antibodies: the cost of obtaining examples lies outside the fixed budget

In antibody design, the ICL examples are chosen from candidates that met the acceptance criteria and were obtained beforehand with another design method (Germinal). The comparison uses a fixed budget of 1 GPU-hour for design and 1 GPU-hour for scoring, and ICL was the only method to yield at least one candidate for every antigen tested ([1](#ref-1)). The preprint states that Germinal takes a median of 23.5 GPU hours to design 8 candidates for one target ([1](#ref-1)). Whether the cost of obtaining the examples is included in the fixed budget is not stated in the text I read. Of the comparators, the methods that use the same examples as ICL (AbMPNN and PSSM) share this cost, and it matters as an extra cost of ICL mainly in comparison with the method that continues designing with Germinal without using the examples.

### Computational passing versus function in experiments

The pass criteria are computational filters on sequence validity, gene composition and identity to known sequences. The text shows that the comparison is in computational metrics, and in the text I read there was no statement that the function of the designed sequences was confirmed experimentally ([1](#ref-1)). Pass rates and compute ratios do not directly express the cost of obtaining designs that work in experiments.

## Overall assessment

The preprint's compute comparison is correct as reported, for a library of 64 passing designs. Widening the conditions changes how it reads. For CRISPR-Cas, the roughly 11-fold difference is a value at 64 designs, and once passing designs number from several hundred to several thousand, fine-tuning may become cheaper (depending on the assumed sampling time). For phage, most of the difference at 64 designs is avoided fixed cost, and the advantage that remains as the library grows comes from a 16.7-fold higher pass rate. Whether the antibody hour includes the cost of obtaining examples is unclear. ICL avoids a fixed cost and is especially advantageous when the library is small, but compute ratios should be read by library size and by how the fixed cost is treated.

## Limitations

- The analysis is arithmetic on reported numbers and assumes a cost linear in the number of passing designs. Quantities the preprint does not state (the sampling time within the fine-tuning total, the ratio of time per sample, whether the two phage times are for the same engine) are assumptions, and the results depend on them.
- The supplementary material was not read. Details of best-setting pass rates and times may be there.
- The compared models differ (Evo 1 and Evo 2), and pass rates that pool settings are mixed with times of the best setting.
- The compute for evaluating the filters is not included on either side. Reuse across tasks and sharing of the fixed cost are not modelled.
- The metrics are computational, and experimental function is not addressed. Sequences, prompts and generation procedures are not discussed.
- The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

The compute saving of Evo 2's ICL is reported for a comparison at 64 passing designs: about 11-fold for CRISPR-Cas loci and 77–95-fold for phage genomes. For CRISPR-Cas loci, ICL's pass rate is lower than that of fine-tuning, and once the 881-hour fixed cost of fine-tuning is amortized over from several hundred to several thousand passing designs, fine-tuning may become cheaper. For phage genomes, most of the difference at 64 designs is estimated to be avoided fixed cost, and the advantage that remains as the library grows is due to the 16.7-fold difference in pass rate. Compute ratios should be read by library size and by how the fixed cost is treated.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive. Run with Python 3.12, NumPy 2.2, pandas 2.2 and Matplotlib 3.9: `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. The calculation is arithmetic on reported numbers and uses no random numbers.

The full re-run materials are in the [companion archive](shared/evo2-icl-compute-accounting/evo2-icl-compute-accounting-companion.zip).


## References

<span id="ref-1"></span>1. Brixi G, Hao YA, Nori D, Merchant A, Widatalla T, King SH, et al. Efficient biological design via genomic in-context learning [Preprint, version 1]. bioRxiv. 2026 Oct 29 [cited 2026 Nov 3]. [doi:10.64898/2026.10.28.762643](https://doi.org/10.64898/2026.10.28.762643). Not peer reviewed. Full text read; supplementary material not read.
