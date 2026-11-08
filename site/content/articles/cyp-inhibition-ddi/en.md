Predicting metabolic enzyme inhibition from molecular structure could help identify interaction liabilities early. But predicting inhibition and predicting how much a coadministered drug's area under the concentration–time curve (AUC) will increase are different tasks.

On November 5, 2026, OpenADMET released final results from its cytochrome P450 (CYP) inhibition challenge. Direct inhibition, time-dependent inhibition and binding structure were evaluated separately, with experimental data released for further analysis [(1)](#ref-1). These divisions help identify which part of the interaction problem a model answers.

## Scope and sources

This article uses the organizers' final report, public data documentation and the M12 guideline of the International Council for Harmonisation (ICH). It does not retrain individual submissions or validate patient-level interaction predictions. The calculation below is an artificial example showing why identical inhibition can have different exposure consequences.

CYP enzymes participate in drug metabolism. ICH M12 distinguishes reversible from time-dependent inhibition and connects in vitro assessment with clinical studies and modeling [(2)](#ref-2). A high competition score does not complete that translation.

## The same inhibition can produce different exposure increases

Consider a simplified reversible-inhibition model. Let \(f_m\) be the fraction of a coadministered drug's total clearance mediated by the affected enzyme, \(I_u\) a constant unbound inhibitor concentration at the relevant site, and \(K_{i,u}\) the unbound inhibition constant. Assume enzyme activity is reduced to \(1/(1+I_u/K_{i,u})\).

Clearance relative to baseline is the sum of the unaffected contribution, \(1-f_m\), and the inhibited contribution, \(f_m/(1+I_u/K_{i,u})\). With unchanged dose and bioavailability and linear kinetics, the area-under-the-curve ratio is its inverse:

\[
\mathrm{AUCR}=\frac{1}{(1-f_m)+f_m/(1+I_u/K_{i,u})}.
\]

AUCR is the dimensionless ratio of exposure with and without the inhibitor. This explanatory hepatic-clearance approximation omits intestinal metabolism, induction, transporters, time variation and blood-flow effects.

The challenge's direct-inhibition target is pIC50, the negative base-ten logarithm of the numerical IC50 in mol/L, where IC50 is the half-maximal inhibitory concentration [(1)](#ref-1). It cannot simply be substituted for the unbound inhibition constant in this equation. The relationship between IC50 and an inhibition constant depends on substrate concentration and inhibition mechanism; the following example therefore does not convert challenge predictions into clinical AUC ratios [(2)](#ref-2).

Table 1 holds \(I_u/K_{i,u}=1\) constant. The dependence on the affected pathway alone changes the exposure ratio.

Table 1. Artificial reversible-inhibition calculation.

| Fraction of clearance affected | Unbound inhibitor / inhibition constant | AUC ratio |
| ---: | ---: | ---: |
| 0.20 | 1.0 | 1.11 |
| 0.90 | 1.0 | 1.82 |

AUC: area under the concentration–time curve. AUC ratio is AUC with the inhibitor divided by AUC without it and is dimensionless.

Even a perfect molecular prediction of inhibition strength cannot identify which row applies without the coadministered drug's elimination pathways. Changing dose can also change \(I_u\). An inhibitor does not carry a single interaction magnitude independent of its partner and exposure.

## Time-dependent inhibition introduces recovery kinetics

Time-dependent inhibition is not simply stronger direct inhibition. When enzyme is inactivated, its activity can remain depressed after inhibitor concentration declines.

A minimal explanatory model for active enzyme amount \(E\) is

\[
\frac{dE}{dt}=k_{\mathrm{syn}}-k_{\mathrm{deg}}E-k_{\mathrm{inact}}(I_u)E.
\]

Here \(k_{\mathrm{syn}}\) is a synthesis rate with units of enzyme amount per time. The degradation and concentration-dependent inactivation rate constants, \(k_{\mathrm{deg}}\) and \(k_{\mathrm{inact}}(I_u)\), have inverse-time units. This general equation explains the distinction; it does not reproduce a challenge submission.

After inactivation stops, recovery depends on \(k_{\mathrm{deg}}\). A binary time-dependent-inhibition label therefore does not determine either effect magnitude or duration. Classifying a liability and predicting active enzyme over time are separate outputs.

## Read the conditions of missed positives

Direct-inhibition regression carries concentration-response information, whereas time-dependent-inhibition classification separates candidates at a threshold. Calling both simply accuracy obscures the consequences of error.

Sensitivity measures the fraction of positives recovered. Precision measures the fraction of positive predictions that are truly positive. Similar composite scores can conceal different numbers of missed positives and follow-up experiments. Precision also changes with prevalence; an early discovery collection need not share the evaluation set's positive fraction.

This does not make a zero-miss threshold automatically useful. Calling every compound positive removes false negatives but performs no triage. Under a finite experimental budget, the more relevant question is which enzymes and chemical series remain among the missed positives at a feasible selection rate.

## Conclusion

AI-based CYP inhibition prediction addresses an entry point to drug interactions. It can help narrow molecular liabilities, but does not automatically supply partner-drug metabolism, inhibitor exposure or enzyme recovery kinetics.

The released challenge creates material for evaluating distinct inhibition tasks. Its ranking alone does not establish clinical false-negative rates or patient-level interaction prediction accuracy.

## Data and code availability

Table 1 is generated in the `DDI` section of the [script](shared/cyp-inhibition-ddi/reproduce.py) and [output](shared/cyp-inhibition-ddi/illustration.json). The [challenge data](https://huggingface.co/datasets/openadmet/cyp-challenge-train-test) are available from the organizers [(1)](#ref-1). No submission predictions were reevaluated and no patient-specific estimates were made.

[Download code and results](shared/cyp-inhibition-ddi/cyp-inhibition-ddi.zip).

## References

1. <a id="ref-1"></a> Castellanos M, Swain J, MacDermott-Opeskin H. Take Me Heme, Binding Modes: Wrapping up the CYP Inhibition Challenge [Internet]. OpenADMET; 2026 Nov 5 [cited 2026 Nov 8]. [https://doi.org/10.5281/zenodo.23985044](https://doi.org/10.5281/zenodo.23985044).

2. <a id="ref-2"></a> International Council for Harmonisation. Drug Interaction Studies M12 [Guideline]. Final version; 2024 May 21. [Official guideline](https://database.ich.org/sites/default/files/ICH_M12_Step4_Guideline_2024_0521_0.pdf).
