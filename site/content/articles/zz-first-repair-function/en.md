A DNA-repair pathway score falls after treatment. Adding a drug that exploits repair defects might seem a natural conclusion. Yet repair-related RNA may fall because repair capacity is impaired, or because fewer cells are replicating DNA and require that machinery. A pathway score alone does not readily distinguish those explanations.

Published on 14 October 2026, ZZ-FIRST combines transcriptional changes after androgen-receptor (AR) pathway suppression with functional markers and a randomized trial ([1](#ref-1); [X discussion](https://x.com/Adam_Weiner535/status/2110731166865363212)). The question here is how far an expression change that might motivate combination treatment can be interpreted as altered function. I also examine the public expression data.

## Biopsies precede addition of the PARP inhibitor

ZZ-FIRST is a small randomized phase 2 trial in high-volume metastatic hormone-naive prostate cancer, not castration-resistant disease. Fifty-four participants start enzalutamide and androgen-deprivation therapy (ADT). After two induction cycles, 17 continue treatment and 37 receive additional talazoparib. On-treatment biopsies are taken at approximately four weeks, before talazoparib. Their changes therefore reflect AR suppression and ADT rather than the effect of adding the PARP inhibitor ([original Methods](https://www.nature.com/articles/s41591-026-04671-5)).

The authors select tumor-rich spatial-transcriptomic regions and aggregate expression by specimen. This enriches tumor signal but does not measure every tumor cell under identical conditions. Treatment-related tumor loss can also change which regions and specimens remain measurable.

AR and proliferation programs decline, as does an HRR gene-set score. However, HRR expression closely tracks E2F-related cell-cycle scores. Analyses of shared genes and cell-cycle-related components lead the authors to interpret HRR-expression suppression mainly as a consequence of reduced proliferation ([original Fig. 4 and Extended Data Fig. 7](https://www.nature.com/articles/s41591-026-04671-5)).

## A pathway name does not define cellular capacity

Homologous recombination is linked to S and G2 phases. When treatment reduces proliferating cells, repair genes used in those phases can decline. At least three measurement targets must be distinguished.

Table 1. Transcription, proliferation and functional-repair measurements.

| Measurement | What it describes | What it does not establish alone |
| --- | --- | --- |
| HRR-related RNA | State of a repair-associated transcriptional program | Capacity to repair damage when required |
| Proliferation and cell-cycle markers | Changes in proliferating cells or their programs | Direct suppression of HRR |
| Functional markers such as RAD51 | Formation of repair responses in evaluable cells | Patient benefit from adding a PARP inhibitor |

Low pathway scores summarize expression rather than identify a mechanism by themselves. Overlapping gene sets can count the same RNA twice; even disjoint sets can move together with cell state. Removing shared genes does not eliminate all dependence.

## Paired changes in public expression data

The following is an additional analysis of the [public data](https://doi.org/10.5281/zenodo.21218835) ([2](#ref-2)), not a reproduction of the authors’ ssGSEA or GSEA. The released matrix contains normalized, batch-corrected logCPM for 34 specimens. Similar specimen names can misidentify pairs, so pairing uses metadata `Subject_ID`. Twelve participants have complete before–after pairs, totaling 24 specimens. They need not represent all 54 trial participants.

Before calculating, I selected six repair-related genes, RAD51, BRCA1, BRCA2, PALB2, RAD54L and RAD51AP1, and six cell-cycle-related genes, PCNA, MCM2, MCM4, CDC6, CCNB1 and CDK1. These small, nonexhaustive panels contain no shared genes. They are not functionally independent: repair-panel genes may also depend on cell-cycle state.

Each gene is standardized using its mean and sample standard deviation across all 24 specimens, then averaged within the panel:

$$
z_{gi}=\frac{x_{gi}-\bar{x}_g}{s_g},\qquad
S_i=\frac{1}{6}\sum_{g\in\mathrm{panel}}z_{gi}
$$

The same reference is used for every pair, and change is post-treatment minus pretreatment. Units are means of gene-standardized expression, not standard deviations of the panel score or units of repair activity. Standardization across all specimens is descriptive and is not presented as future-patient prediction evaluation.

![Paired repair and cell-cycle panel changes for twelve participants](shared/zz-first-repair-function/figures/paired-panel-trajectories.png)

Figure 1. Independent calculations from public logCPM. Lines connect specimens from the same participant. These descriptive scores do not reproduce KEGG HR, E2F, ssGSEA or a clinical HRD assay.

Table 2. Descriptive summaries of author-defined panels in 12 paired participants.

| Summary | Repair-related panel | Cell-cycle-related panel |
| --- | ---: | ---: |
| Mean within-participant change | −0.548 | −0.807 |
| Participants with a decrease | 8/12 | 10/12 |
| Mean-change range leaving out 1 participant at a time | −0.621–−0.469 | −0.922–−0.679 |

The correlation between within-participant changes is r=0.735. This compares how much each participant changes, not the correlation of all pretreatment and on-treatment specimens pooled together. Not every participant showed a decrease in both scores.

![Relationship between within-participant panel changes](shared/zz-first-repair-function/figures/paired-panel-changes.png)

Figure 2. Independent additional analysis, distinguishing the participant whose biopsy site changes. The correlation does not identify causal direction or repair function.

One participant’s biopsy site changes from prostate to lymph node. Excluding that participant gives mean changes of −0.489 for repair and −0.685 for cell cycle, with r=0.689. Leaving out one participant at a time gives correlations of 0.653–0.832; removing one gene at a time from either panel gives 0.609–0.780. Mean changes remain negative for both panels. Standardization remains fixed to the original 24 specimens; these ranges are not confidence intervals.

The calculation shows coordinated repair- and cycle-related changes even with nonoverlapping panels. Shared-gene double counting is not the whole explanation. It does not estimate what fraction of change is explained by growth arrest. The original paper already examines cell-cycle dependence and shared-gene sensitivity. This is a descriptive check using another panel definition and confirmed pairs, not a new mechanistic discovery. Author-provided normalization, batch correction and tumor-region selection are reused rather than repeated.

## Treatment also reduces cells eligible for RAD51 assessment

The paper examines nuclear RAD51 foci and the DNA-damage marker γH2AX by immunofluorescence. RAD51 is evaluated among geminin-positive tumor cells, addressing a different question from an average over all cells, including nonproliferating cells.

Eligibility requires at least 30 geminin-positive cells and γH2AX positivity in more than 25% of geminin-positive tumor cells, among other conditions. The assay first establishes adequate proliferating cells and damage for evaluating repair ([original functional-immunofluorescence Methods](https://www.nature.com/articles/s41591-026-04671-5)).

AR suppression reduces proliferating cells themselves. In ZZ-FIRST, RAD51 is evaluable in 17 pretreatment and four on-treatment specimens; these are not 21 paired participants. The authors also examine specimens from another ADT study and report no clear decline in RAD51 foci.

This does not prove completely preserved repair function. Few post-treatment specimens are evaluable, and strongly responding tumors may be preferentially lost from assessment. It does, however, avoid equating lower RNA directly with functional deficiency and adds a measurement conditioned on proliferative state.

## Combination benefit requires a treatment comparison

Confirmed PSA below 0.2 ng/mL at 12 months after randomization occurs in 27/37 participants receiving talazoparib and 11/17 controls. The paper reports meeting its primary endpoint, but its primary test compares the combination-arm response rate against a prespecified threshold, not against the control arm for superiority. An exploratory between-arm Fisher test gives p=0.54 ([original Results and Statistical analysis](https://www.nature.com/articles/s41591-026-04671-5)).

Table 3. Trial response and severe treatment-emergent adverse events by group.

| Outcome | Talazoparib addition | Control |
| --- | ---: | ---: |
| PSA response at 12 months | 27/37 (73.0%) | 11/17 (64.7%) |
| Grade 3 or higher treatment-emergent adverse events | 25/37 (67.6%) | 6/17 (35.3%) |

Grade 3 or higher anemia occurs in 15/37 combination participants, with frequent reductions and interruptions. The radiographic progression-free-survival hazard ratio is 0.64 with a wide 95% confidence interval, 0.28–1.42. Two fatal AML cases are reported during long-term follow-up in the combination group, with underlying genomic predisposition identified. These counts do not estimate a general incidence rate.

Failure to establish clear added benefit in a small trial proves neither equivalence nor absence of benefit in every participant. If transcriptional suppression associates with response duration in both groups, it may reflect response to AR suppression. Prognostic association differs from predicting extra benefit from PARP inhibition, and the trial does not make these interchangeable. Participants were not selected for HRR mutations; results cannot be transferred directly to molecularly selected trials or different disease stages.

## Repair-expression decline and growth arrest are not independent

Repair- and cycle-related scores move together within participants. Even if cell-cycle adjustment removes an association in regression, that alone does not establish confounding: cell cycle can itself be downstream of treatment.

A tumor with less repair demand because it stops proliferating differs biologically from a proliferating tumor unable to form a repair response. Lower pathway scores alone distinguish neither state and do not establish benefit from adding PARP inhibition. That distinction remains between an expression result and a treatment decision.

## Data and code availability

The [additional-analysis archive](shared/zz-first-repair-function/zz-first-repair-function.zip) contains code, inputs, results and figures, excluding original figures and implementation. REPRODUCE.md records data, panel definitions, exclusions, pairing and limitations.

```sh
python -m pip install -r requirements.txt
python analysis.py
python -m unittest test_analysis.py
python plot.py
```

Sources were checked on 18 October 2026. The released expression matrix is the Zenodo dataset accompanying the original study.

## References {#references}

<span id="ref-1"></span>
1. Zacchi F, Castro E, Imbach K, Rodriguez-Vida A, Simonetti S, Mellado B, et al. Talazoparib plus enzalutamide in high-volume metastatic hormone-naive prostate cancer: a randomized phase 2 trial. Nature Medicine. Published online 14 October 2026. [doi:10.1038/s41591-026-04671-5](https://doi.org/10.1038/s41591-026-04671-5).

<span id="ref-2"></span>
2. Zacchi F, Imbach K, Aguilar D, Mir Arnau G, Mateo J. Talazoparib plus enzalutamide in high-volume metastatic hormone-naïve prostate cancer (ZZ-FIRST): a randomized phase 2 clinical trial. Zenodo. 2026. Dataset; record 21218835. [doi:10.5281/zenodo.21218835](https://doi.org/10.5281/zenodo.21218835).
