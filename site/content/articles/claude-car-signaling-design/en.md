A CAR design with a signaling domain about 70% shorter than its reference produced more receptors on the cell surface. Generate Biomedicines' work with Claude raises a question beyond how bold the design was: a cell that performs better does not necessarily contain receptors that each perform better ([1](#ref-1)).

That distinction affects the interpretation of efficacy. Does the design produce enough receptors from less messenger RNA (mRNA), or recognize targets carrying less antigen? These are different advantages, with different uses and comparison conditions.

## Scope and sources

The source is Bai et al.'s technical report, *Refactored intracellular domains enhance CAR expression and function*. I checked the publicly available PDF's main text, methods and supplementary-figure text on October 30, 2026. I do not treat it as a peer-reviewed paper. The calculations below check reported aggregate values and illustrate how receptor abundance, response and duration can be separated. They are not a reanalysis of individual-cell or patient data ([1](#ref-1)).

The reference intracellular domain combines 4-1BB and CD3ζ and contains 154 amino acids; I call it BBζ below. The compact candidate, krgr–ζ1–40, contains 45 amino acids. The reduction is \(1-45/154=70.8\%\). This does not mean that the entire CAR was shortened by 70% ([1](#ref-1)).

## What does matching mRNA input compare?

A chimeric antigen receptor (CAR) has an extracellular region that recognizes its target and an intracellular region that activates the cell. Even with the same antigen specificity, the number of receptors reaching the surface and the signal following recognition are different quantities.

This distinction predates AI-guided CAR design. Feucht et al. showed that altering the number and position of activation motifs changes the balance between effector function and memory-associated properties. Increasing activation does not necessarily improve long-term antitumor activity in a single direction ([2](#ref-2)). Majzner et al. examined how responses to antigen-low targets depend on the hinge and transmembrane regions as well as intracellular signaling design ([3](#ref-3)).

For the compact candidate, [Figure 4 of the report](https://generatebiomedicines.com/publications/refactored-intracellular-domains-enhance-car-expression-and-function/#page=8) shows increased surface CAR at matched mRNA input and reference-level expression at a lower input. A stronger cellular response at the same mRNA input therefore cannot be attributed entirely to more efficient intracellular signaling ([1](#ref-1)).

Changing the denominator changes the question. Matched mRNA input compares the whole design from delivered material to cellular output. Matched surface CAR abundance comes closer to comparing function after removing the advantage mediated by higher expression. Both comparisons are useful, but they estimate different things.

Table 1. Comparison conditions and their interpretation.

| Condition held equal | Main question | Differences that remain |
| --- | --- | --- |
| Input mRNA | How much cellular response follows the same amount of material? | Delivery, expression and downstream signaling |
| Surface CAR abundance | Does response differ at comparable receptor abundance? | Receptor organization, assembly and cell state |
| Antigen molecules per target | At what antigen abundance does the response emerge? | CAR abundance, response maximum and background |
| Measurement time | How much function remains at that time? | Initial abundance, production and loss, and cell-number history |

This is an interpretation table prepared for this article, not a reproduction of a table in the report.

## Antigen sensitivity does not move with expression

[Supplementary Figure S10](https://generatebiomedicines.com/publications/refactored-intracellular-domains-enhance-car-expression-and-function/#page=34) is particularly informative. At matched mRNA input, the reported B-cell maturation antigen (BCMA) abundance needed for half-maximal, background-subtracted antigen-specific interferon-γ (IFN-γ) response is 650 molecules per target cell for BBζ and 1,130 for the compact candidate. Their ratio is 1.74: the compact candidate did not reach half-maximum at a lower antigen abundance. The report discusses the possibility that its 8.4-fold higher surface CAR abundance in this setting offsets lower antigen sensitivity per receptor ([1](#ref-1)).

The ratio 1,130/650 does not, however, directly estimate the efficiency of one receptor. Half-maximum here is half of each construct's own background-subtracted response span. If the maximum IFN-γ response differs, the same “50%” represents different absolute quantities. Nor is this number a BCMA–CAR binding dissociation constant: it is a functional-response measure for a cell population.

Figure 1 uses only the published half-maximal values and fixes the Hill slope at 1 to draw \(f(A)=A/(K_{50}+A)\). Here, \(A\) is antigen molecules per target cell, \(K_{50}\) is the half-maximal value in the same units, and \(f\) is the fraction of each curve's own response span. These are explanatory curves, not fits to the original measurements.

![Illustrative response curves normalized to each construct's own response span. Curves pass through half-maximal antigen abundances of 650 and 1130 molecules; the compact curve is shifted right.](shared/claude-car-signaling-design/figures/antigen-normalized.png)

Figure 1. Explanatory curves through published half-maximal values. Assumptions are Hill slope 1, background 0 and each curve's maximum 1. Individual observations, errors and actual maximum responses are not used. This is neither a reproduction nor a refit of the report's Figure S10.

This normalization removes any increase in maximum response. Conversely, examining IFN-γ only at abundant antigen can conceal differences at low antigen abundance. Collapsing both into one efficacy multiplier obscures the distinction.

## Can response alone separate expression from signaling?

A simple equation illustrates the problem. Let \(R\) be surface receptor abundance at a given time, \(p(A)\) the fraction of stimulation associated with the antigen condition, and \(g\) a coefficient converting receptor abundance to stimulation. Define the dimensionless stimulus

\[
Z=gR p(A).
\]

Assume that the observed response is \(Y=Y_0+Y_{\max}Z/(H+Z)\). The quantities \(Y_0\) and \(Y_{\max}\) are background and response span above background, while \(H\) is the half-maximal dimensionless stimulus. The coefficient \(g\) has reciprocal units of \(R\), and \(p\) is dimensionless. This is an explanatory model for this article, not an identified mechanism of CAR signaling.

Multiplying \(R\) by eight and dividing \(g\) by eight leaves \(Z\) unchanged. Within this model, repeated response measurements cannot distinguish the two. More precise measurements of the same output and measurements of a different quantity play different roles.

Measuring surface CAR constrains one part of the product. It still does not make \(g\) a molecular mechanism: that coefficient folds together intracellular abundance, organization and activation state. Matching expression is a comparison that separates higher expression as an explanation, rather than proof of a mechanism.

## Longer function need not mean a longer half-life

The report also provides measured time-course evidence. In [Figure 4b,c](https://generatebiomedicines.com/publications/refactored-intracellular-domains-enhance-car-expression-and-function/#page=8), the compact candidate had about twelvefold more surface CAR on day 1 after mRNA delivery, followed by a similar decline in both constructs. Longer function therefore cannot simply be attributed to slower receptor loss ([1](#ref-1)).

Initial abundance and loss rate can be confused in a similar way. Suppose \(t=0\) is the time when new receptor production has ended, and subsequent abundance follows

\[
R(t)=R_0\exp(-kt),\qquad k=\frac{\ln 2}{t_{1/2}}.
\]

Here, \(R_0\) is initial abundance, \(k\) is the loss constant per day, and \(t_{1/2}\) is the half-life in days. Assume that function requires a fixed threshold \(R_*\), initially exceeded by \(R_0\). The time until the threshold is crossed is then \(T=\ln(R_0/R_*)/k\).

If the two designs have the same loss rate and threshold, and differ only by an initial-abundance multiplier \(q\), their difference in functional duration is

\[
\Delta T=\frac{\ln q}{k}=t_{1/2}\log_2 q.
\]

Using \(q=8.4\) as an illustrative multiplier borrowed from the separate mRNA-dose comparison gives an extension of 3.07 half-lives. Hypothetical half-lives of 1, 2 and 3 days give extensions of 3.07, 6.14 and 9.21 days. The 8.4-fold multiplier is not the initial ratio measured in the time-course experiment. These are not predictions fitted to the experimental data. They are sensitivity calculations showing that a higher initial abundance alone can extend duration without changing the loss rate.

![Two hypothetical receptor-abundance curves with the same two-day half-life. Increasing the initial abundance 8.4-fold delays crossing of the same threshold.](shared/claude-car-signaling-design/figures/threshold-duration.png)

Figure 2. Hypothetical curves differing only in initial abundance. Both half-lives are set to 2 days. The reference starts at twice the assumed threshold and the other at 16.8 times the threshold. Threshold crossing occurs at 2.00 and 8.14 days. These are not estimates of actual CAR-T receptor half-life or efficacy duration.

In practice, mRNA-driven production continues for some time, while cell division, receptor internalization and encounters with targets also occur. Estimating \(k\) from the number of days with detectable function is therefore even harder. Before adding complexity to the equation, it is necessary to distinguish what has actually been observed.

## How far does the evidence support compact design?

The work can be read as a report of a compact design that retained function and yielded promising candidates in expression and cellular function. Several stages nevertheless separate design from a clinical dose: input mRNA, delivery to the intended T cells, surface CAR, antigen distribution and cellular response. A reduction in mRNA required in culture need not translate proportionally into a lower administered dose in patients.

Likewise, failure to detect IFN-γ without antigen does not establish the absence of every form of persistent basal signaling. Cytotoxicity, cytokine release, exhaustion and long-term persistence are distinct measurement targets. The report itself notes that exhaustion was not measured directly and in vivo performance remains to be established ([1](#ref-1)).

The contribution of AI also presents a comparison problem. Obtaining a functional candidate and outperforming expert design at the same experimental budget are separate claims. The candidate's value need not be discounted, but its existence cannot replace an unperformed comparison.

The first conclusion to retain is that a compact receptor design can change cellular function obtained from the same mRNA input. Moving from that conclusion to performance per receptor, sensitivity to antigen-low cells or lower clinical doses adds a new comparison condition at each step. Higher expression is an advantage of the design; the scale on which that advantage is assessed determines the scope of the conclusion.

## Data and code availability

The arithmetic checks and illustrative calculations for Figures 1 and 2 can be rerun with the [analysis code](shared/claude-car-signaling-design/analysis.py). The [results and environment](shared/claude-car-signaling-design/outputs/results.json), [Figure 1 curve values](shared/claude-car-signaling-design/outputs/antigen_illustration.csv) and [Figure 2 curve values](shared/claude-car-signaling-design/outputs/decay_illustration.csv) are provided. The script was run with Python 3.12.4, NumPy 2.2.6 and Matplotlib 3.9.1. No random numbers are used. Original individual-cell data are not included.

## References

<span id="ref-1"></span>1. Bai L, Kumar A, Desai H, Li J, de Alwis D, Hazuda D, et al. Refactored intracellular domains enhance CAR expression and function [Technical report; not treated here as peer reviewed]. Generate Biomedicines; 2026 [cited 2026 Oct 30]. [Full report](https://generatebiomedicines.com/publications/refactored-intracellular-domains-enhance-car-expression-and-function/).

<span id="ref-2"></span>2. Feucht J, Sun J, Eyquem J, Ho YJ, Zhao Z, Leibold J, et al. Calibration of CAR activation potential directs alternative T cell fates and therapeutic potency. Nat Med. 2019;25:82–88. [doi:10.1038/s41591-018-0290-5](https://doi.org/10.1038/s41591-018-0290-5).

<span id="ref-3"></span>3. Majzner RG, Rietberg SP, Sotillo E, Dong R, Vachharajani VT, Labanieh L, et al. Tuning the antigen density requirement for CAR T-cell activity. Cancer Discov. 2020;10(5):702–723. [doi:10.1158/2159-8290.CD-19-0945](https://doi.org/10.1158/2159-8290.CD-19-0945).
