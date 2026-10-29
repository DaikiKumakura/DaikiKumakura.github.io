Weaker CD3 binding in a T-cell engager (TCE) can sometimes reduce cytokines while retaining activity. Low cytokines alone, however, do not justify selecting a weaker molecule.

I digitized activity (T-cell-dependent cellular cytotoxicity, TDCC) and TNFα measurements from public FOLR1 and CEACAM5 experiments. Comparisons require retained activity relative to the high-CD3-affinity molecule under the same conditions. Results depend on tumor-antigen affinity, reference choice and interpolation between sparse concentrations.

## Question and intended use

The question is whether weaker-CD3 molecules have concentration ranges retaining an activity signal while reducing TNFα. Intended use is selecting molecules and concentrations for further in-vitro study, not clinical dosing, probabilities of cytokine release syndrome (CRS) or a clinical safety window. TNFα is the representative cytokine; rankings using IL-6 or IFNγ and overall toxicity including normal tissues were not evaluated.

## Tumor-antigen affinity changes the comparison

Abdelmotaleb and colleagues compare related CD3 clones called high, intermed, low and vlow, with recombinant-human-CD3 KD values of 1.56, 29.1, 41.0 and 82.4 nM. These names are specific to these molecules, not universal affinity classes ([1](#ref-1)).

**Table 1.** Tumor-antigen (TA) affinities and source panels.

| Target and line | Tumor-antigen KD | Label | Original figure |
| --- | ---: | --- | --- |
| FOLR1, SK-OV-3 | Approximately 57 nM | TA high | Figure 1 |
| FOLR1, SK-OV-3 | Approximately 1,000 nM | TA low | Figure 2 |
| CEACAM5, LS-180 | Approximately 0.1 nM | TA high | Figure 5 |
| CEACAM5, LS-180 | Approximately 5.5 nM | TA low | Figure 6 |

Cultures use peripheral blood mononuclear cells (PBMCs) and target cells at an effector-to-target (E:T) ratio of 10:1, with tenfold concentration steps from 5,000 pM. Figures show technical-duplicate means and are described as representative experiments using two PBMC donors. Symbols are not pooled two-donor means, nor are concentration points biological replicates ([1](#ref-1)).

## AUCE is not a fraction of cells killed

The activity readout is CytoTox-Glo protease release from damaged cells. Both activity and TNFα measurements at 24, 48 and 72 hours are summarized as area under the curve of effect (AUCE), integrating time-course responses at a given concentration rather than blood drug concentrations ([1](#ref-1), [2](#ref-2)).

Activity AUCE has considerable background. Dividing uncorrected values by their maximum can make weak molecules appear to retain activity. I subtract each curve's lowest-concentration signal as an approximate background, then normalize to the largest observed increment for CD3 high within the same target and TA-affinity condition:

\[
r_{m,e}(C)=
\frac{Y_{m,e}(C)-Y_{m,e}(C_{\min})}
{\max_CY_{\mathrm{high},e}(C)-Y_{\mathrm{high},e}(C_{\min})}
\]

Here \(m\) is the CD3 molecule and \(e\) activity (TDCC) or TNFα. Endpoints have separate denominators; molecules are not normalized to their own maxima. The reference maximum and low-concentration value are shared by all candidates within a condition, so their reading errors propagate jointly into relative values. A small value above one, such as 1.03, is not evidence of superiority over the reference molecule. A relative activity of 0.8 means 80% of the reference increment, not 80% cell killing. Relative TNFα of 0.25 is 25% of the reference signal, not 25% CRS risk.

The lowest concentration is not untreated control, making background subtraction an assumption. TA high and low also have different reference denominators; their normalized values cannot directly establish absolute superiority. \(C_{\min}\) is endpoint-specific: CEACAM5 activity starts at 0.05 pM and TNFα at 0.5 pM, so their joint comparison is limited to 0.5 pM and above.

## Candidate ranges from observed points

I digitized 183 coordinates in 32 series from symbols in [the original Figures 1, 2, 5 and 6](https://doi.org/10.1080/19420862.2025.2584374), not fitted lines. Some low-signal overlaps require approximate displayed positions; individual original values were not all clearly recoverable. CSV files retain reading-status flags. CD3 intermed at 500 pM in [the original Figure 5A](https://doi.org/10.1080/19420862.2025.2584374) was excluded because its blue observed symbol could not be identified. No value was imputed from the fitted curve. Other coordinate errors found by independent checks were corrected before recalculation.

The main analysis connects adjacent readings linearly on log concentration and finds ranges satisfying

\[
r_{\mathrm{TDCC}}(C)\geq\alpha,
\qquad r_{\mathrm{TNF}}(C)\leq\beta
\]

Illustrative thresholds are \(\alpha=0.8\) and \(\beta=0.25\), not clinically validated boundaries. Sensitivity varies activity thresholds over 0.5, 0.7, 0.8 and 0.9, and TNFα over 0.1, 0.25 and 0.5. Interpolation is restricted to concentrations observed for both endpoints, without extrapolation. Counts of actually tested concentrations meeting both criteria are recorded separately.

![Relative activity and TNFα tradeoffs under four conditions](shared/tce-affinity-cytokine-window/figures/01-observed-tradeoffs.png)

**Figure 1.** Background-subtracted relative TDCC versus relative TNFα. Squares indicate concentrations with both displayed measurements. Lines follow increasing concentration and represent log-concentration interpolation. Lower right of the dashed boundaries satisfies the example criteria. Colors denote CD3 clones; TA high/low refers to tumor-antigen affinity.

## Low cytokines alone do not retain a candidate

**Table 2.** Maximum relative TDCC within observed concentrations.

| Condition | CD3 intermed | CD3 low | CD3 vlow |
| --- | ---: | ---: | ---: |
| FOLR1, TA high | 1.03 | 0.53 | 0.25 |
| FOLR1, TA low | 0.56 | 0.17 | 0.12 |
| CEACAM5, TA high | 0.90 | 0.72 | 0.36 |
| CEACAM5, TA low | 0.93 | 0.59 | 0.32 |

These values derive from `normalized-points.csv` generated by `analysis/run.py`. CD3 high is 1 by reference definition. Values above 1 are permitted rather than clipped. Vlow reduces TNFα but never meets activity 0.8 here. Low qualifies in some conditions when activity requirements fall to 0.7 or 0.5. Choosing the lowest-cytokine molecule alone can implicitly discard required activity.

**Table 3.** First concentration reaching relative activity 0.8 and corresponding TNFα.

| Condition | High concentration, pM | High relative TNFα | Intermed concentration, pM | Intermed relative TNFα |
| --- | ---: | ---: | ---: | ---: |
| FOLR1, TA high | Approximately 30 | 0.92 | Approximately 37 | 0.26 |
| FOLR1, TA low | Approximately 1,100 | 0.69 | Not reached | — |
| CEACAM5, TA high | Approximately 33 | 0.28 | Approximately 1,500 | 0.31 |
| CEACAM5, TA low | Approximately 190 | 0.36 | Approximately 1,500 | 0.13 |

These are interpolated, not direct measurements at those concentrations. The missing 500 pM CEACAM5 TA-high intermed point leaves a broad 50–5,000 pM interpolation. That row does not establish that intermed is inferior; it identifies a sparsely measured interval.

## Classification depends on boundaries

With activity ≥0.8 and TNFα ≤0.25, the main interpolation retains a nonzero-width range only for CEACAM5 TA-low intermed: approximately 1,500–5,000 pM. One jointly observed concentration, 5,000 pM, satisfies both criteria. This is the observed upper concentration, not evidence that the range ends beyond it.

FOLR1 TA-high intermed reaches activity 0.8 at TNFα approximately 0.26, just above 0.25. Excluding it on that difference would overinterpret coarse digitization.

![Intermed concentration windows and matched-activity comparisons](shared/tce-affinity-cytokine-window/figures/02-screening-windows.png)

**Figure 2.** Left: interpolated candidate ranges, with black points for jointly observed concentrations meeting criteria. “None” means no nonzero-width range under these boundaries and interpolation, not absent efficacy. Right: Table 3's matched-activity comparison.

Across 128 vertical ±2-pixel perturbations, FOLR1 TA-high intermed retains a range in 32 scenarios, while CEACAM5 TA-low intermed does so in 128. These are digitization scenarios, not biological confidence intervals or success probabilities. They do not evaluate series misidentification or donor variability.

## Hill assumptions change candidate ranges

I also approximate background increments using

\[
\hat r(C)=a\left[
\frac{C^h}{EC_{50}^h+C^h}
-\frac{C_{\min}^h}{EC_{50}^h+C_{\min}^h}
\right]
\]

Slope \(h\) is fixed at 0.5, 1 or 2, fitting increment coefficient \(a\) and EC50 by least squares. Search remains within observed concentrations. EC50 is an empirical shape parameter, not a cytotoxic-mechanism constant. The monotonically increasing function cannot represent high-dose decline or hook effects.

**Table 4.** Candidate-range log-width under interpolation and Hill assumptions.

| Condition and CD3 molecule | Point interpolation | Hill h=0.5 | Hill h=1 | Hill h=2 |
| --- | ---: | ---: | ---: | ---: |
| FOLR1, TA high, intermed | 0 | 0.04 | 0.13 | 0.12 |
| CEACAM5, TA high, intermed | 0 | 0.01 | 0.34 | 0.63 |
| CEACAM5, TA low, intermed | 0.52 | 0.46 | 0.71 | 0.96 |

Width is \(\log_{10}(C_{\mathrm{upper}}/C_{\mathrm{lower}})\); 0.52 corresponds to approximately a 3.3-fold range, and zero to no nonzero-width range. Smoothing creates ranges absent under interpolation without establishing the Hill model as correct. Of 96 sensitivity fits, 29 put EC50 outside observed concentrations. Weak or unsaturated series do not provide precise EC50 estimates. Even an in-range estimate need not be identifiable; parameters are used to examine model dependence, not rank affinity.

![Sensitivity to interpolation, Hill shape and reference choice](shared/tce-affinity-cytokine-window/figures/03-assumption-sensitivity.png)

**Figure 3.** Range widths for four conditions and four molecules. “Common high-TA reference” applies the same target's TA-high/CD3-high reference to TA-low conditions. Whether the TA-high and TA-low figures used the same donors is unconfirmed, so differences between them are not causal effects of TA affinity. An alternative background uses the smaller of the two lowest-concentration values.

## Discussion

Comparisons of weaker CD3 binders depend on what is matched. Lower cytokines at the same concentration may simply accompany lower activity. Table 3 instead matches relative activity, but its concentrations are interpolated and activity and TNFα use separate reference increments. The resulting comparison is neither a clinical therapeutic index nor an absolute safety window.

Tumor-antigen KD alone also does not determine candidate rank. These molecules bind tumor antigen bivalently and CD3 monovalently in a 2+1 format, so avidity, antigen abundance, epitope and cell background accompany monovalent affinity ([1](#ref-1)). FOLR1 and CEACAM5 comparisons change both target and cell line. Differences across the four conditions cannot be reduced to a causal effect of tumor-antigen KD alone.

The original paper additionally examines healthy jejunal organoids in [Figure 7](https://doi.org/10.1080/19420862.2025.2584374) and mouse experiments in [Figures 4, 8 and 10](https://doi.org/10.1080/19420862.2025.2584374) ([1](#ref-1)). These do not validate the present TNFα threshold against normal-tissue injury or in-vivo safety. In Figure 10, tolerability required a lower CD3-high dose than for the other molecules, precluding a simple equal-dose comparison. Those animal and normal-tissue results were not fitted or used to rank candidates here.

AUCE also compresses time-course differences into one integrated value ([2](#ref-2)). Equal AUCE need not distinguish an early large response from a sustained later response. Choosing TNFα alone, using representative donor curves and sharing reference/background errors directly limit what these sparse observations establish. A smooth Hill curve cannot supply those unmeasured distinctions.

## Sparse measurements and boundaries constrain the result

FOLR1 TA-high intermed reaches activity 0.8 at a low TNFα of approximately 0.26, but this lies near the chosen 0.25 boundary, and the main interpolation retains no nonzero-width range. Only the Hill-shape assumptions yield a narrow range (log-width 0.04–0.13). Unreadable CEACAM5 points remain. Smooth curves cannot substitute for missing observations: candidate ranges depend on interpolation and model assumptions. These ranges neither universally prioritize weaker-affinity molecules nor establish clinical concentration thresholds.

## Data and code availability

[Download coordinates, all-condition results and analysis code](shared/tce-affinity-cytokine-window/tce-affinity-cytokine-window-analysis.zip).

```bash
python analysis/download_sources.py
python analysis/digitize.py
python analysis/run.py
python -m unittest discover -s tests
```

Source material is [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Figures were digitized to create new comparisons, fitted quantities and sensitivities. Original text, supplements and figures are not included in the ZIP. The recorded seed is 2026102607.

## References

1. <span id="ref-1"></span>Abdelmotaleb O, Schneider A, Waldhauer I, Sam J, Hofer T, Lechmann M, et al. Optimizing efficacy and safety of T cell bispecific antibodies: the interdependence of CD3 and tumor antigen binder affinities in FOLR1 and CEACAM5 2+1 TCBs. mAbs. 2025;17(1):2584374. [doi:10.1080/19420862.2025.2584374](https://doi.org/10.1080/19420862.2025.2584374).
2. <span id="ref-2"></span>Van De Vyver A, Eigenmann M, Ovacik M, Pohl C, Herter S, Weinzierl T, et al. A Novel Approach for Quantifying the Pharmacological Activity of T-Cell Engagers Utilizing In Vitro Time Course Experiments and Streamlined Data Analysis. AAPS J. 2022;24(1):7. [doi:10.1208/s12248-021-00637-2](https://doi.org/10.1208/s12248-021-00637-2).
