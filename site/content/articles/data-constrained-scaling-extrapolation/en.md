Reference date: the facts in this article are as of 3 November 2026.

In an explainer published in November 2026, the AI company Q Labs states that extrapolating a fixed-data scaling law to 5 trillion tokens and 10^29 FLOPs prescribes about 7,000 times the parameter count of the Chinchilla law, with an ensemble holding over 300 parameters per token ([1](#ref-1)). The source is a data-constrained scaling law (an equation giving loss as a function of unique tokens, model size, epochs and ensemble size) in a preprint posted on 27 October 2026 ([2](#ref-2)). The experiments in the preprint cover at most 400 million unique tokens and models of at most 398 million parameters. This note rebuilds the equation from the constants printed in the preprint and asks by calculation: (1) whether the preprint's prescriptions are reproduced inside the fitted range, (2) what is prescribed at 5 trillion tokens and 10^29 FLOPs, and (3) how well determined that prescription is against differences in loss and shifts in the exponents. Chinchilla is the compute-optimal training law, which prescribes about 20 tokens per parameter ([3](#ref-3)). The subjects are a preprint that has not been peer reviewed and a company explainer, and the conclusions hold only for what was reproduced here.

## Scope and sources

I read the full text of the preprint (PDF, 22 pages) and the full Q Labs explainer ([1](#ref-1), [2](#ref-2)). The preprint's authors include people affiliated with Q Labs. I did not read the released training code. The "reproduction" below is therefore my own rebuild from the equation and constants printed in the text, not the output of the authors' code.

The equation is the preprint's Eq. 3.

\[
L(U,N,R,M)=E+\frac{A}{N^{\alpha}}+\frac{B}{(UR)^{\beta}}+P\,(R-1)^{\delta}\left(\frac{N}{U^{\gamma}}\right)^{\kappa}-\frac{F}{N^{\nu}U^{\epsilon}R^{\rho}}\left(1-\frac1M\right)^{\mu}
\]

\(U\) is unique tokens, \(N\) the non-embedding parameters of one model (one ensemble member), \(R\) the epochs and \(M\) the number of members; compute is approximated as \(C\approx 6UNRM\). The printed constants are E=2.18, A=165, α=0.298, B=1759, β=0.408, P=117, δ=0.0791, κ=0.162, γ=3.04, F=192, μ=1.12, ν=0.224, ε=0.137 and ρ=0.263 ([2](#ref-2)). The power laws for the hyperparameters (effective learning rate and weight decay) are also printed.

The numbers here are of two kinds. Values reported by the preprint or the explainer are quoted as printed. Values I calculated (optimization of the equation, flatness of the loss, change under shifted exponents) are marked as my calculation. The exponent shifts are not uncertainty intervals: the preprint prints no covariance, and because one exponent is moved while the other constants stay fixed, the shifted equation no longer fits the data. They show sensitivity to the structure of the equation; sensitivity to the rounding of the printed digits was examined separately. Terms: nats is the unit of loss measured with the natural logarithm; T is trillion (10^12); a rung is one point of the preprint's experimental grid (a combination of unique tokens, model size and epochs); "x Chinchilla" is total parameters divided by unique tokens/20. Table 1 sets the explainer's main numbers ([1](#ref-1)) beside the preprint's corresponding statements ([2](#ref-2)).

Table 1. Main numbers of the Q Labs explainer and their counterparts in the preprint (as stated in the text).

| Claim in the post | Counterpart in the preprint | Reading in this note |
| --- | --- | --- |
| Extrapolated to 5T tokens and 1e29 FLOPs: about 7,000x Chinchilla's parameters, over 300 parameters per token | Not stated; fitted on 25M to 400M unique tokens, 30M to 398M parameters (per member); production budgets up to 1e20 FLOPs, 12x the sweep budget | Extrapolation by 12,500x in tokens and 1e9x in compute |
| Hyperparameter law near-optimal at 16x the fitted compute | Section 4.2: a refit on a 16x smaller sweep, one target rung (100M tokens, 398M parameters, 32 epochs) | One rung |
| Within 0.01 nats of optimal on every axis tested | Figure 8: transfer from one rung to 2x in tokens, size or epochs | Tested at 2x per axis |
| Loss keeps falling with compute on fixed data | Section 6.1: four budgets up to 1e20 FLOPs at 100M tokens | Observed over about one decade of compute |
| Chinchilla stops at 250B parameters | 5T tokens / 20 tokens per parameter | Arithmetic: 2.5e11 |

## Discussion by issue

### The explainer's arithmetic is internally consistent

The explainer's numbers agree as arithmetic. At 20 tokens per parameter (Chinchilla), 5 trillion tokens give 250 billion parameters; 7,000 times that is 1.75×10^15, or 350 parameters per token. Learning from about 200 million tokens with 10^14 synapses is 2×10^-6 tokens per parameter (1:500,000), and the ratio to the Chinchilla value is 10^7 (my calculation). These hold if one accepts the explainer's premise that human learning volume and synapse count map onto tokens and parameters; the premise itself is outside this note.

### Inside the fitted range, the preprint's prescriptions are largely reproduced

At 100 million unique tokens and 10^19 to 10^20 FLOPs I optimized Eq. 3 (with \(R\ge 2\) and the per-member \(N\) at most 848M, the largest size the preprint used for validation). Table 2 shows the result. Parameters per member are 0.47 to 0.79 billion, epochs 35 to 71 and members 1 to 3, all within the axis ranges of the preprint's Figure 5 (400M to 800M, 16 to 128, 1 to 8). The member-count rule of thumb (\(C_2=1.4\times10^4U^{1.9}\), \(C_3=4.8\times10^4U^{1.9}\), \(M^*\approx 2+C/C_3\)) gives 1, 2.4 and 3.3 in my calculation, in line with the optimized 1, 2 and 3. The predicted losses are 3.285, 3.236 and 3.204, against observed losses reported by the preprint of 3.27 at 10^19 and under 3.20 at 10^20: 0.015 higher at 10^19 and above the reported "under 3.20" at 10^20 (3.204; prediction and observation are different quantities). This agreement is at the level of ranges, and it is consistent with the calculation below not contradicting the preprint's equation. The gap between prediction and observation (0.004 to 0.015) also serves as a yardstick for model error when the flatness of the loss is read later.

Table 2. Optimal allocation by Eq. 3 at 100 million unique tokens (my calculation). M: ensemble members, R: epochs, N: parameters per member.

| C (FLOPs) | M | R | N per member | Predicted loss | Domain |
| --- | ---: | ---: | ---: | ---: | --- |
| 1e19 | 1 | 35.2 | 4.7e8 | 3.285 | R >= 2, N <= 848M |
| 3e19 | 2 | 43.8 | 5.7e8 | 3.236 | R >= 2, N <= 848M |
| 1e20 | 3 | 70.8 | 7.9e8 | 3.204 | R >= 2, N <= 848M |
| 1e19 | 2 | 1 | 8.3e9 | 3.278 | R >= 1, any N |
| 3e19 | 3 | 1 | 1.7e10 | 3.236 | R >= 1, any N |
| 1e20 | 3 | 1 | 5.6e10 | 3.203 | R >= 1, any N |

The bottom three rows of Table 2 are the equation's optimum with the lower bound on epochs and the upper bound on member size removed: ensembles of single-epoch models that are larger (5.6×10^10 in the 10^20 row, about 70 times the row above). The loss differences are at most 0.007 (10^19), 0.000 (3×10^19) and 0.001 (10^20). Even inside the fitted range, then, which domain is allowed changes the optimal allocation greatly while the loss barely moves. The preprint's Figure 5 prescriptions are consistent with restricting the domain to the fitted and validated sizes and epoch counts (my reconstruction, an inference). How the domain was set in the extrapolation to 5 trillion tokens is not stated in the explainer.

### At 5 trillion tokens and 10^29 FLOPs, how the domain is set decides the result

I optimized the same equation at 5 trillion unique tokens and 10^29 FLOPs (my calculation, Table 3). With the epoch lower bound at 1, the optimum is one epoch, one model and 3.3×10^15 parameters (667 per token, about 13,300 times Chinchilla), with a predicted loss of 2.1955. The \(R=1\) domain is legitimate: the preprint treats it as the case that recovers Chinchilla and uses the single-epoch recipe as a baseline. But \(R=1\) is a singular end point. The overfitting term is exactly zero at \(R=1\) by its form, yet already about 48% of its size at \(R=2\) at \(R=1.0001\) (from the form \(P(R-1)^{0.0791}\)); the preprint's data exist only for \(R\ge2\), and the ensemble term at \(R=1\) with \(M>1\) has no data behind it. With the lower bound at 2, the optimum is 3 members, 8.3 epochs, 1.34×10^14 per member and 4.0×10^14 in total (80.6 per token, about 1,611 times Chinchilla), with a predicted loss of 2.2090.

The point closest to the explainer's "over 300" and "nearly 7,000x" (its wording) is the one where the epoch count is exactly 2: 1.67×10^15 in total (333 per token, 6,667 times Chinchilla), 9 members and a predicted loss of 2.2097. This correspondence is not stated in the explainer; it is my inference. Moreover, the explainer's own numbers (about 7,000x, over 300 parameters per token) and \(C=6U\times(\text{total parameters})\times R\) alone fix the epoch count at about 2.2 to 1.9 for 300 to 350 parameters per token, an identity that does not use Eq. 3. The match with 333 per token and 6,667x is therefore nearly a computational equivalence, not evidence about where the optimum of Eq. 3 lies. The 9 members at this point also exceed the member counts the preprint fitted (up to 8). The difference from the \(R\ge2\) optimum is 0.0007 nats and from the \(R\ge1\) optimum 0.014 nats.

Table 3. Prescriptions of Eq. 3 at 5 trillion unique tokens and 10^29 FLOPs (my calculation). Total is N x M.

| Domain / point | M | R | Total parameters | Parameters per token | x Chinchilla | Predicted loss |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| R >= 1 optimum | 1 | 1.0 | 3.3e15 | 667 | 13,333 | 2.1955 |
| R >= 2 optimum | 3 | 8.3 | 4.0e14 | 80.6 | 1,611 | 2.2090 |
| R = 2 exactly | 9 | 2.0 | 1.67e15 | 333 | 6,667 | 2.2097 |

I examined how flat the predicted loss is (Figure 1). Moving the total parameters within \(R\ge2\), the range over which the loss stays within 0.001 nats of the optimum runs from 8.1×10^13 to 1.67×10^15, a factor of 20.7. Within 0.004 nats (the standard deviation from seeds alone, which the preprint's Table 7 reports for one setting) the range is 75.8-fold, and within 0.01 nats about 270-fold (the upper end is set by the \(R=2\) boundary; the ratios move by about 1% with the search grid). Members were searched up to 64; the preprint fitted up to 8, so these ranges are lower bounds. However, 0.004 nats is the seed-to-seed spread of observed loss at one setting (25 million tokens, about 101 million parameters, 128 epochs), whereas what is examined here is a difference in predicted loss; they are different kinds of quantity. The gap between prediction and observation in the reproduction above (0.004 to 0.015) is the more appropriate yardstick for the model error of the equation, and at that size the range from about 21-fold to about 270-fold cannot be distinguished. All of this is within the equation.

![Figure 1. Predicted loss against total ensemble parameters at 5 trillion unique tokens and 10^29 FLOPs (my calculation). Blue solid: epochs R >= 2; grey dashed: R < 2 (outside the preprint's fitted range). The grey band is the R >= 2 optimum plus 0.004 nats. The green dotted line is the R >= 2 optimum (4.0e14); the orange dashed line is the point with exactly 2 epochs (1.67e15).](shared/data-constrained-scaling-extrapolation/figures/01-flat-loss-vs-total-parameters.png)

### Shifting the exponents moves the prescription by orders of magnitude (sensitivity to structure)

I shifted each of the nine printed exponents (α, β, κ, γ, ν, ε, ρ, δ, μ) by ±0.05 one at a time, with the other constants fixed (nothing refitted), and recomputed the 5-trillion-token, 10^29 FLOPs prescription within \(R\ge2\) (Figure 2, my calculation). ±0.05 is about 6% to 63% of the exponents (63% for δ), and the shifted equations no longer fit the data (for example κ−0.05 gives a predicted loss of 2.379). This is therefore sensitivity to the structure of the equation, not to the rounding of the printed digits. The total parameters scattered from 3.3×10^13 to 1.67×10^15, a 51-fold range. Six of the 18 shifts (α−0.05, β+0.05, κ−0.05, ν−0.05, ε−0.05, δ+0.05) landed on the \(R=2\) boundary (1.67×10^15), 11 fell between 1.3×10^14 and 5.6×10^14, and only β−0.05 gave 3.3×10^13 (101.7 epochs). By contrast, moving each of the 14 constants by half of its last printed digit left the prescription almost unchanged: 3 members, 8.05 to 8.50 epochs and 3.92 to 4.14×10^14 total parameters (about ±3%; my calculation, results/rounding_5T_1e29.csv). Rounding of the printed digits is not the issue; what can be read is that, under large changes of the equation's exponents, whether the optimum sits on the boundary or in the interior swaps "7,000x" for "1,600x".

![Figure 2. Prescription (total parameters, log axis) at 5 trillion tokens and 10^29 FLOPs when each of nine exponents is shifted by ±0.05 one at a time (other constants fixed, nothing refitted; not an uncertainty interval). Green dotted: optimum with the printed constants (4.0e14); orange dashed: the point with exactly 2 epochs (1.67e15).](shared/data-constrained-scaling-extrapolation/figures/02-exponent-sensitivity.png)

### At the extrapolated point, the hyperparameters lie outside the tested range

The preprint's hyperparameter laws set the effective learning rate as \(3.95\times10^{4}\,U^{-1.014}N^{0.273}R^{0.120}\) and weight decay as \(1.08\times10^{2}\,U^{-0.870}N^{0.398}R^{0.660}\) ([2](#ref-2)). In the optimization at 100 million tokens the weight decay is 0.35 to 0.68, increasing with model size and epochs. The explainer's summary statement that bigger models on repeated data need much more weight decay ([1](#ref-1)) therefore holds in that range. At 5 trillion tokens the \(U^{-0.870}\) factor dominates, and the same law gives, at the \(R\ge2\) optimum, a weight decay of 1.6×10^-3 and an effective learning rate of 4.9×10^-5 (my calculation). The preprint tested weight decay from 0.0017 to 5.8 and effective learning rate from 0.0022 to 0.87 ([2](#ref-2)). The extrapolated effective learning rate is about 1/45 of the tested minimum. Whether this law holds at the extrapolated point cannot be judged from this note. The loss equation also presumes tuned hyperparameters, so the loss prediction there is also in an unvalidated region. The weight decay (1.6×10^-3) is also slightly below the tested minimum (0.0017), but the argument rests mainly on the effective learning rate.

## Overall assessment

What could be confirmed as fact is as follows. The explainer's arithmetic is consistent. From the preprint's equation and constants, the prescriptions inside the fitted range (model size, epochs, members) are largely reproduced. The extrapolation spans a factor of 12,500 in unique tokens, 10^9 in compute and about 340,000 in per-member model size (1.34×10^14 ÷ 3.98×10^8, at the \(R\ge2\) optimum). At the extrapolated point, the equation's optimum moves in total parameters from about 1,600 to about 13,000 times Chinchilla depending on where the bounds on epochs and size are set, and the loss differs by at most 0.014 nats between them.

By interpretation: if the explainer's number was derived from Eq. 3 with a lower bound of 2 epochs (an inference; the explainer does not say), "7,000x" lies at a boundary point where the bound binds, rather than at an optimum of the equation, and the loss surface is flat around it. The number is better read as one point in a range the equation barely distinguishes, not as a value the equation uniquely prescribes. The preprint itself does not claim an extrapolation to 5 trillion tokens; that extrapolation belongs to the explainer. The preprint reports that, in 100-million-token experiments up to 10^20 FLOPs (12 times the sweep budget), hyperparameter transfer and ensembling give a loss at least 0.15 nats lower than the prior prescriptions. This note did not test that claim; it examined only the prescription at the extrapolated point.

## Limitations

- The equation and constants were read from the text of the preprint. The authors' code, supplementary material and values inside figures were not checked. If the optimization domain (integer epochs, upper limit on members, grid of model sizes) differs from the authors', the results can change.
- Neither the preprint nor the explainer gives the derivation of the 5-trillion-token numbers. The correspondence with the exactly-2-epochs point is my inference.
- The exponent perturbations are not uncertainty intervals but sensitivity to the structure of the equation (other constants fixed, nothing refitted). Correlations between parameters are not treated here.
- Members were searched up to 64; the preprint fitted up to 8, so the flatness ranges are lower bounds.
- The losses are for FineWeb, the GPT-2 tokenizer, a dense transformer with a fixed aspect ratio and the Muon optimizer; generalization to other settings is outside this note. Parameters are non-embedding parameters; the value-embedding tables are not counted.
- The seed spread (0.004 nats) is the spread of observed loss at a single setting; as a yardstick for differences in predicted loss, the gap between prediction and observation in this note's reproduction (0.004 to 0.015) is more appropriate.
- The note was checked by three reviews performed by AI used by the author; this is not confirmation by a human third party.

## Conclusion

Q Labs' "about 7,000 times" is a number extrapolated 12,500-fold in tokens and 10^9-fold in compute beyond the fitted range. Rebuilding the equation from the printed constants shows that the prescription at the extrapolated point moves from about 1,600 to about 13,000 times Chinchilla depending on how the domain of epochs and size is set, with predicted loss differing by at most 0.014 nats. The number is best read as one point in a range of near-equal loss, not as a prescription of how many times larger a model should be.

## Data and code availability

The calculation code (`analysis.py`, `figures.py`), tests (`test_analysis.py`) and result tables are in the companion archive. Run with Python 3.12, NumPy 2.2, SciPy 1.14, pandas 2.2 and Matplotlib 3.9: `python analysis.py`, `python figures.py`, then `python -m pytest test_analysis.py`. No random numbers are used. The preprint's training code was not run for this note.

The full re-run materials are in the [companion archive](shared/data-constrained-scaling-extrapolation/data-constrained-scaling-extrapolation-companion.zip).


## References

<span id="ref-1"></span>1. Vegesna A, Baron E, Satheesh A, Dahal S. Quadrillion-parameter transformers and how to train them [Internet]. Q Labs Research. 2026 Nov [cited 2026 Nov 3]. Available from: https://qlabs.sh/research/parameters

<span id="ref-2"></span>2. Baron E, Berman S, Satheesh A, Vegesna A, Dahal S, Wilson AG. Improving data-constrained scaling with hyperparameter transfer and ensembling [Preprint, version 1]. arXiv. 2026 Oct 27 [cited 2026 Nov 3]. arXiv:2610.37842. Available from: https://arxiv.org/abs/2610.37842. Not peer reviewed. Full text read; released code not read.

<span id="ref-3"></span>3. Hoffmann J, Borgeaud S, Mensch A, Buchatskaya E, Cai T, Rutherford E, et al. Training compute-optimal large language models [Preprint]. arXiv. 2022 [cited 2026 Nov 3]. arXiv:2203.15556. Available from: https://arxiv.org/abs/2203.15556. Not read here; the 20 tokens-per-parameter figure is as cited by [1] and [2].
