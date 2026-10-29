[日本語](dll3-il2-combination-prediction.html)

Combining a delta-like ligand 3 (DLL3)-directed T-cell engager with an IL-2 variant suppressed tumor growth more strongly than either monotherapy. How far can that result be explained simply by adding the effects of the two monotherapies?

For the KP1 small-cell lung cancer (SCLC) model, I estimated growth rates from published control and monotherapy mean trajectories and predicted the combination without fitting to its outcomes. At day 22, the digitized combination mean was approximately 385 mm³, whereas an independent-effect prediction was approximately 810 mm³: about 2.10 times the observed volume. That discrepancy alone does not prove pharmacological synergy or identify its mechanism.

## Four arms from the same experiment

The source is the January 27, 2026 version of a preprint, not a peer-reviewed study. [The original Figure 3H and I](https://pmc.ncbi.nlm.nih.gov/articles/PMC12822708/#F3) show HBS control, TCE, IL2REH, and combination arms. HBS is the vehicle control. IL2REH is an IL-2 variant that the source describes as CD25 biased; it was not pooled with wild-type IL-2 ([1](#ref-1)).

**Table 1.** Models and treatment schedules.

| Model | TCE | TCE schedule | IL2REH schedule | Reported mice per arm |
| --- | --- | --- | --- | --- |
| B16 melanoma | TRP2 TCE | 5 mg/kg every 6 days | 3 µg IL-2 component every 2 days | Control 5; TCE 11; IL2REH 5; combination 11 |
| KP1 SCLC | DLL3 TCE | 5 mg/kg every 4 days | 3 µg IL-2 component every 2 days | 10 in each arm |

Those sample sizes refer to mice. The reanalysis obtained 49 plotted mean symbols, not 49 individual animals. Individual variability, longitudinal covariance, and changes in the composition of the measured groups were not reconstructed. B16/TRP2 (TRP2, tyrosinase-related protein 2) and KP1/DLL3 were analyzed separately rather than pooled as one drug or model.

The question is whether the effects of the monotherapies on net tumor growth transfer independently to the combination. The context of use is testing this simple hypothesis in these nonclinical experiments, not selecting human combination doses or treatment sequence.

The B16 target is not the TRP2 protein itself but a TRP2-derived peptide presented by mouse MHC-I H2-Kb, TRP2/Kb. Its presentation differs from the surface DLL3 target in KP1. The source's IL2REH is also fused to mouse serum albumin; the listed 3 µg denotes the IL-2 component. These doses cannot be transferred to wild-type IL-2 or another formulation ([1](#ref-1)).

## Estimation uses only control and monotherapy outcomes

For each arm, \(V_a(t_0)\) denotes tumor volume at treatment start. The control and monotherapy mean trajectories were approximated by

\[
\log\frac{V_a(t)}{V_a(t_0)}=g_a(t-t_0).
\]

The coefficient \(g_a\) is an interval-specific net log-growth rate, not a direct tumor-killing rate of TCE or IL2REH. The fitted intervals were days 6–19 for B16 and days 14–22 for KP1, starting from the treatment arrows in the source and ending within the common observation window of the three fitted arms.

If the two agents independently change net growth rate, the combination rate is

\[
g_{TI}^{\mathrm{ind}}=g_T+g_I-g_C,
\]

where \(C,T,I\) denote control, TCE, and IL2REH. Subtracting the control rate avoids counting natural growth twice. The combination's treatment-start volume supplies its scale; subsequent combination volumes do not enter parameter estimation.

To examine dependence on an exponential time shape, I also predicted from ratios of observed same-time monotherapy and control means:

\[
V_{TI}^{\mathrm{point}}(t)=V_{TI}(t_0)
\frac{V_T(t)/V_T(t_0)\;V_I(t)/V_I(t_0)}{V_C(t)/V_C(t_0)}.
\]

Both are multiplicative assumptions about normalized tumor volumes. Neither directly tests cellular Bliss independence or Loewe additivity.

## Independent-effect predictions exceeded the combination means

![Figure 1. Control and monotherapy means with combination outcomes excluded from estimation](shared/dll3-il2-combination-prediction/figures/combination-prediction.svg)

**Figure 1.** Control and monotherapy means with combination outcomes excluded from fitting. Dashed curves are predictions from exponential fits; black crosses use pointwise mean ratios. The three fitted arms are used only through the vertical dotted line, and combination outcomes in that same interval are compared with predictions. The volume axis is logarithmic.

**Table 2.** Net growth rates estimated from control and monotherapies.

| Model | Control rate | TCE rate | IL2REH rate | Predicted combination rate |
| --- | ---: | ---: | ---: | ---: |
| B16/TRP2 | 0.285 | 0.173 | 0.242 | 0.130 |
| KP1/DLL3 | 0.245 | 0.190 | 0.190 | 0.135 |

Rates are in day⁻¹. Unrounded values and fitted intervals are in `outputs/tables/net-growth.csv`.

**Table 3.** Observed and predicted combination means.

| Model and comparison day | Observed combination mean | Exponential prediction | Pointwise prediction | Exponential / observed |
| --- | ---: | ---: | ---: | ---: |
| B16/TRP2, day 19 | 22.7 | 122.4 | 144.8 | 5.39 |
| KP1/DLL3, day 22 | 384.8 | 809.8 | 761.7 | 2.10 |

Volumes are in mm³; see `outputs/tables/comparison.csv`. The KP1 comparison has only two days, 18 and 22; the exponential ratio is 2.10 on day 22 and 1.63 on day 18. Without the exponential approximation, the day 22 prediction remained approximately 1.98 times the observed volume. The discrepancy therefore cannot be attributed solely to the chosen exponential time shape.

![Figure 2. Predicted-to-observed combination volume ratios](shared/dll3-il2-combination-prediction/figures/prediction-discrepancy.svg)

**Figure 2.** Ratios of predicted combination volumes to observed means. B16 and KP1 are separate experimental models. Reading-sensitivity ranges are not confidence intervals across mice.

## Small B16 volumes are sensitive to figure reading

In 2,000 reading scenarios, each arm's mean symbols were shifted coherently by ±1 vertical pixel. The exponential predicted-to-observed ratio ranged from 1.84 to 2.41 for KP1 and from 1.43 to 19.91 for B16. These are not mouse-population confidence intervals.

For B16, both treatment-start and combination volumes lie close to the zero tick. One pixel represents a large fraction of these volumes. Consequently, 5.39 is not a precise interaction magnitude. For KP1, overprediction remained throughout the specified reading scenarios (`outputs/tables/reading-sensitivity.csv`). The two model-specific ratios were not averaged into a general combination effect.

## The two predictions are not independent corroboration

The constant-rate equation and pointwise ratios use the same control and monotherapy means. The latter removes exponential time dependence but retains the multiplicative normalized-volume reference. Overprediction by both therefore argues against the time shape alone explaining the discrepancy; it is not independent experimental replication of synergy.

Monotherapy observations also extend through the same times as the predicted combination. This is an arm holdout excluding later combination outcomes, not a forecast from early information alone. The source's combination-versus-monotherapy group differences and deviation from the present multiplicative reference are different comparisons ([1](#ref-1)).

## A model discrepancy is not a mechanism

The preprint discusses TCE-induced T-cell recruitment and IL2REH-induced effector differentiation together with single-cell analyses ([1](#ref-1)). The present tumor-volume benchmark does not independently establish those mechanisms. Immune-cell dynamics, delayed effects, time-varying growth, and changes in the composition of group means can also produce deviations from constant-rate addition.

The supported result is that, under this KP1/DLL3 condition, the constant-rate independent-effect model fitted to monotherapies underestimated the combination's growth suppression. Net monotherapy growth rates omitted suppression observed only in the combination. The same result cannot optimize dose response, sequencing, or dosing intervals: only the source experiment's one combination schedule was compared.

## Data and code availability

[Code, reading coordinates, and result tables](shared/dll3-il2-combination-prediction/dll3-il2-combination-prediction-analysis.zip). Run `analysis/download_sources.py` to obtain the public image and `analysis/run.py` to regenerate every figure and table. `python -m unittest discover -s tests` checks monotherapy-only fitting and the independent-effect equation. The original figure is not included in the companion; its URL, SHA-256, and reading rules are recorded.

## References

1. <span id="ref-1"></span>Obenaus M, Poupault CL, McGinnis CS, Prange C, Jiang H, Su LL, et al. T cell engagers control solid tumors through clonal replacement and IL2-driven effector differentiation of CD8 T cells [Preprint]. bioRxiv; 2026. Version 2, posted 2026 Jan 27. [Version 2](https://www.biorxiv.org/content/10.64898/2025.12.04.692214v2). [doi:10.64898/2025.12.04.692214](https://doi.org/10.64898/2025.12.04.692214).


<span id="cite-this-article"></span>
<span id="reproducibility"></span>
