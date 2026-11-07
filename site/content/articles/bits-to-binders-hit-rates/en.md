In October 2026, experimental results for AI-designed proteins were reported in quick succession. Anthropic reported that Claude selected 180 toxin-binder designs over 64 hours, 31 more were added with Claude's help, and of the 211 tested, 17 met its binding criteria ([1](#ref-1)). Pythia Labs reported testing AI-designed full-length antibodies against 22 targets, with binders obtained for 8 of 15 soluble targets and all 7 GPCR (G protein-coupled receptor, a family of membrane receptors) targets ([2](#ref-2)). In March, results for 12,000 CAR-T binding domains designed by teams from 42 countries had appeared as a preprint (not peer reviewed) together with public data ([3](#ref-3), [4](#ref-4)).

Each reports a "hit rate", but the definitions differ. This article counts, from public data, how much a hit rate moves with its definition, and sets out the conditions under which the hit rates of the three reports can be placed on one scale. It does not judge which report is better or which design method is better.

**Reference date:** The facts and numbers here reflect public information as of October 30, 2026. Preprints may have been revised and data updated before publication.

**Disclosure:** The AI I use (Claude) is a model from Anthropic, the source of one of the compared reports. The Pythia Labs preprint states that the work was conducted by employees of Pythia Labs ([2](#ref-2)).

## Abstract

For the same 12,000 designs, changing the "hit" threshold and denominator moved the hit rate from 0.7% to 16.7% (the widest range obtained by varying both threshold and denominator; 16.7% uses the 6,814 recovered designs as denominator). Claude's toxin binders were 17/211 (8.1%) under the published criteria; relaxing them gave 18.5–19.4% for one laboratory and 23.2% for either. The Bits to Binders team hit rates of 0.6–38.4% are not a single yardstick: one team contributes heavily, and the low end includes teams with low recovery and teams with more depletion than enrichment. For Pythia-1, per-design numbers could not be confirmed and no hit rate was calculated. The three reports differ in six conditions: assay, threshold, replication, controls, prior selection and denominator.

## Scope and sources

Table 1 shows the three reports and the information available.

Table 1. Reports covered and information used.

| Report | Targets and scale | Information used here |
| --- | --- | --- |
| Bits to Binders (report by Kosonocky et al. ([3](#ref-3))) | One target (CD20), 12,000 designs (80 amino acids), 28 teams | Sequences, pooled-screen results and team information ([4](#ref-4)) |
| Anthropic (report on scorpion-toxin binders ([1](#ref-1))) | 5 toxins, 211 designs, 2 laboratories | Table of results for all 211 designs (CC BY 4.0) ([5](#ref-5)) |
| Pythia-1 (Pythia Labs report ([2](#ref-2))) | 22 targets (15 soluble, 7 GPCR) | Numbers in the main text; no per-design table was found in the portion read |

Some values come from the sources' own statements rather than from recalculation of public data: "64 hours", "42 countries", "211 designs, being 180 chosen by Claude plus 31 added later with Claude's help", and "3 replicates in the pooled screen". "5 of 48 for IL11" is the Pythia Labs preprint's statement ([2](#ref-2)). All other hit counts and intervals were calculated by `analysis.py` from fixed versions of the public data.

The sources checked on October 30, 2026 were: the full Anthropic page; the abstract of the Bits to Binders preprint; and the relevant main-text parts of version 1 of the Pythia Labs preprint (Sections 2.3 and 2.5.1, the Figure 1 legend and Section 5.16), which I read myself. The Pythia-1 main-text numbers have not been confirmed by a third party. I did not check the report PDF that Anthropic cites, nor the Pythia Labs statement that 12 of the 31 soluble-target binders have single- to double-digit nM KD. The Bits to Binders main text was not used to check the numbers here.

## Methods

**Hit-rate intervals:** 95% Wilson intervals (a confidence interval for a binomial proportion) were computed from hits and tests. They assume the results for individual designs are independent.

**Bits to Binders:** From the public pooled-selection results (counting sequences enriched under CAR-T proliferation), the number of "Up" designs (FDR below 0.05, where FDR is the false discovery rate, and enrichment above twofold) was reproduced: 707, matching the report. Counts were redone with other thresholds and denominators. The number of "Down" calls (change opposite to enrichment) was also counted as an observation in the opposite direction. Differences in hit rate between teams were tested with a chi-square test that assumes independent designs.

**Claude:** In the public table, counts were redone under other criteria using per-laboratory results. KD is the dissociation constant, a measure of binding strength; smaller means tighter binding. Binding was measured by methods such as surface plasmon resonance (SPR). Counts by KD threshold are designs called hits at Adaptyv Bio whose mean KD (arithmetic mean) was at or below the threshold.

**Pythia-1:** Only numbers written in the paper were used. Per-design results could not be confirmed.

**Status of the analysis:** The analysis plan was not fixed before calculation. The scope was set while looking at the structure of the public data. The threshold sensitivity analysis, the breakdowns by team and method, and the analysis excluding the largest team were added after seeing results (post hoc, exploratory). They are recorded in `analysis-plan.md`.

## Results

### Bits to Binders: hit rates move with the definition for the same 12,000 designs

Figure 1 shows the results for the 28 teams.

![Hit rate, recovery and Up and Down counts for the 28 Bits to Binders teams](shared/bits-to-binders-hit-rates/figures/01-team-hit-rates.png)

Figure 1. Bits to Binders results by team. Each row is a team. A: Up count divided by submissions (%, 95% Wilson interval). B: share of designs detected in the pooled screen (%). C: numbers of Up and Down designs (symmetric-log axis). Blue points are teams with more Up than Down; red points are teams with Down at least equal to Up. Submissions total 12,000, including organizer control sequences.

Table 2 shows counts and rates by threshold and denominator.

Table 2. Bits to Binders: hits and hit rates by definition of a hit (FDR below 0.05).

| Definition | Hits | Denominator: all 12,000 | Denominator: 6,814 recovered |
| --- | ---: | ---: | ---: |
| Direction of enrichment only (no fold condition) | 1,137 | 9.5% | 16.7% |
| Enrichment above 2-fold (the report's definition) | 707 | 5.9% | 10.4% |
| Enrichment above 4-fold | 86 | 0.7% | 1.3% |

- **Denominator:** Of the 12,000 designs, 6,814 were detected in the pooled screen, and 5,186 (43%) were not recovered. Unrecovered designs may reflect synthesis or expression failure and do not necessarily reflect design quality.
- **Threshold:** Raising the enrichment condition from 2-fold to 4-fold reduces hits from 707 to 86. At FDR below 0.001 there are 473 hits (3.9%).

**Differences between teams:**
- **Overall:** For 28 teams (11,984 designs excluding organizer control sequences; 704 Up), hit rates ranged from 0.6% (Perforators) to 38.4% (Nucleate UK London), with a median of 3.8%.
- **Dispersion:** A rough test assuming independent designs found that team hit rates were not explained by chance variation (chi-square 1,054, 27 degrees of freedom). The result was the same after excluding the largest team (chi-square 288, 26 degrees of freedom). Dispersion relative to the binomial expectation was about 39-fold (`summary.json`). Because correlation among designs within a team is ignored, the size of the p-value should not be read as strong evidence.
- **Concentration:** Nucleate UK London (a language model) contributed 22.6% of Up calls (159) from 3.5% of designs (414). The top 3 teams account for 39.2% and the top 5 for 51.4%.

**What the low end contains:**
- **Low recovery:** For Perforators (9.3% recovered) and Evaneil (10.5%), about 90% of designs were not detected in the screen. Their low rates reflect few detectable designs and cannot be read as design ability.
- **More depletion than enrichment:** Four teams, CAD Pro (Up 4, Down 50), Team Anonymous (7, 35), Picaso Protein (15, 29) and Bryant Lab (6, 11), had more Down than Up. This ordering alone does not determine whether enrichment exceeds noise.
- **Up and Down counts:** Overall there were 166 Down against 707 Up, a ratio of 4.3 to 1. Counting "Up minus Down" gives 541 (4.5%). Five percent of 707 is about 35, but that arithmetic is not an estimate of the expected false-positive count in this experiment. FDR concerns the expected false-discovery proportion over repeated analyses ([6](#ref-6)); multiplying the realized number of Up calls by 0.05 does not determine this experiment's false-positive count. Down also includes truly depleted designs, so the 166 Down calls cannot quantify false positives or the amount of noise.

**Method differences:** Teams using language models had a hit rate of 10.7% (194/1,812) and diffusion-based teams 5.4% (495/9,192). Excluding Nucleate from the language-model group gives 2.5% (35/1,398), reversing the order. The method effect cannot be separated from one team's result. Because team, compute and strategy are confounded with method, a causal reading that method changed the hit rate is not supported.

### Claude: hit rate runs from 8.1% to 23.2% as the criterion changes

The right panel of Figure 2 recounts Anthropic's public table under different criteria.

![Hit rates under different definitions of a hit in the same experiment](shared/bits-to-binders-hit-rates/figures/02-definition-sensitivity.png)

Figure 2. Hit rate by definition of a hit (95% Wilson intervals). Left: Bits to Binders (12,000 designs, one target). Right: Claude scorpion-toxin campaign (211 designs, 5 toxins). The horizontal axis is the hit rate (%).

According to the dataset description, the published criteria have four conditions ([5](#ref-5)): (1) a hit against the toxin at both laboratories in every replicate; (2) every main-screen KD at 1 µM or tighter; (3) a fitted maximum response (Rmax) at Twist Bioscience within the theoretical value; (4) no signal against the unrelated protein CLEC12A. LqhIII was measured only at Adaptyv Bio, so it requires a hit there plus conditions (2) and (4). The 17 under the "published criteria" are the count in the public table's binder-assignment column (`binder_against`); this analysis did not independently reproduce condition (3) from the input table. "Published criteria" below refers to these 17.

Table 3 shows counts and rates under different criteria.

Table 3. Claude's 211 toxin-binder designs: hits and hit rates under different criteria.

| Criterion | Hits | Hit rate (95% interval) |
| --- | ---: | ---: |
| Published criteria (from the `binder_against` column; both laboratories, all replicates, KD 1 µM or tighter, Rmax condition, CLEC12A negative) | 17 | 8.1% (5.1–12.5%) |
| Binding at both laboratories (no other criteria) | 34 | 16.1% (11.8–21.7%) |
| Binding at one laboratory (Twist) | 39 | 18.5% (13.8–24.3%) |
| Binding at one laboratory (Adaptyv) | 41 | 19.4% (14.7–25.3%) |
| Binding at either laboratory | 49 | 23.2% (18.0–29.4%) |
| Either laboratory, including "weak or ambiguous" (reference) | 62 | 29.4% (23.7–35.9%) |

Notes: LqhIII was measured only at Adaptyv Bio, so the denominators for "Twist", "Adaptyv" and "both" are all 211 but LqhIII is treated asymmetrically. The 39 "Twist" hits are not the laboratory's own call but a call from a fixed rule that Anthropic applied afterwards ([5](#ref-5)); the 62 including "weak or ambiguous" follow the same rule. The main range is 8.1–23.2%; 29.4% is a reference value for an extended criterion. The intervals assume independent designs and do not include uncertainty from prior selection or from grouping by toxin and design set.

- **KD thresholds:** Among Adaptyv results, 6 designs (2.8%) had mean KD at or below 10 nM, 23 (10.9%) at or below 100 nM, and 35 (16.6%) at or below 1 µM.
- **Design type:** Grouped by the number of toxins targeted at design, single-toxin designs (60) gave 11 hits (18.3%, 10.6–29.9%), two- or three-toxin designs (60) gave 5 (8.3%), and designs for all five (91) gave 1 (1.1%). Even for designs made against several toxins, the criteria were met for one toxin only, consistent with Anthropic's statement ([1](#ref-1)).
- **By toxin:** Cn2 7, AaH II 4, AaH I 4, LqhIII 2, Ts-1 0.
- **KD at the two laboratories:** Of the 17, 15 had KD from both laboratories (the 2 LqhIII designs have one laboratory only); the two laboratories' values differed by a median of 2.0-fold and a maximum of 50.6-fold. The stricter the KD threshold, the more the laboratory difference matters.

**What the controls do:** Four designs had a binding call at both laboratories for more than one toxin. One of them (AaHII-B4) was excluded for Ts-1 by the Rmax condition and is counted among the 17 as an AaH II binder. The other three also bound the unrelated protein CLEC12A in both Twist runs. Without a control, a design that "sticks to anything" would be counted as a hit. The published criteria have the effect of excluding this type of design.

### Pythia-1: different criteria, and no per-design hit rate

The numbers in the main text are as follows ([2](#ref-2)); they have not been confirmed by a third party.
- **Targets and tests:** 22 targets (15 soluble, 7 GPCR). At most 48 selected designs were tested per target (6 for CCR8).
- **Targets with hits:** 8 of 15 soluble targets, with 31 binders (12 of them with single- to double-digit nM KD; this 12 is unchecked). All 7 GPCR targets, with 18 binders.
- **Example by target:** IL11, 5 of 48.
- **Criteria:** For soluble targets, the primary hit was a bio-layer interferometry (BLI) response above 0.06 nm at 150 s; a confirmed binder had KD below 5 µM in five-concentration BLI. For GPCRs, a flow-cytometry z-score above 10 (confirmation: EC50 below 1 µM).

Counts are made from at most 48 pre-filtered designs, under a definition looser than Claude's (KD 1 µM or tighter, two laboratories, all replicates, controls). Per-design hit rates cannot be calculated here because the number tested per target is unknown. Target-level success (8 of 15 targets) is a different quantity from a per-design hit rate.

### Six conditions that differ among the three reports

Table 4 shows the conditions in the three reports.

Table 4. Six conditions that differ among the three reports.

| Condition | Bits to Binders | Claude | Pythia-1 |
| --- | --- | --- | --- |
| Assay | Enrichment under CAR-T proliferation (pooled) | SPR (2 laboratories, some BLI) | BLI, flow cytometry |
| Threshold | FDR below 0.05, enrichment above 2-fold | KD 1 µM or tighter | Response above 0.06 nm, KD below 5 µM |
| Replication | 3 replicates in the pool | Binding in all replicates | Five BLI concentrations (a concentration series, not replicates) |
| Controls or opposite-direction comparison | Down calls; not a calibrated negative control | CLEC12A, OVA | Not confirmed in the main text |
| Prior selection | Depends on the team | 180 chosen by Claude plus 31 added later with Claude's help | After narrowing to at most 48 |
| Denominator | Total submitted and recovered counted separately | 211 tested | At most 48 per target |

Target difficulty, binder length and format (80-amino-acid CAR binding domains, toxin binders, full-length antibodies) and sample size also differ. Sample size alone changes the 95% interval around a hit rate of about 8% to 1.5–35% for 12 designs, 3.6–18% for 60, 5.1–12.5% for 211 and 5.8–10.8% for 466 (the interval-width examples use integer hit counts obtained by multiplying each n by 0.08).

## Discussion

A "hit rate" cannot be compared without stating threshold, denominator, replication and controls. For the same experiment, the definition moved it across 0.7–16.7% (Bits to Binders) and 8.1–23.2% (Claude). The Bits to Binders range is the widest, obtained by varying both threshold and denominator.

The Bits to Binders spread of 0.6–38.4% cannot be read as a range of design ability. The low end mixes teams with few detectable designs and teams whose Up calls do not exceed Down, and the high end depends heavily on one team. The method comparison also depends on one team's result.

Of Claude's 17, 15 are binding confirmed at both laboratories and the 2 LqhIII designs are binding confirmed at Adaptyv Bio only. The published criteria give fewer hits than the other criteria in Table 3. The relaxed counts show sensitivity to definition, not which definition is better.

Pythia-1 uses looser criteria than the other two, reports counts after prior selection, and permits no per-design hit rate. Placing all three on one scale is not supported by the data here. This article shows only that hit rates from reports with different conditions are hard to place side by side; it does not examine whether reports that state their conditions are easier to compare.

## Limitations

- **Ranking:** The three reports differ in target and assay, so which is better cannot be stated.
- **Claude's result:** Of the 17 under the published criteria, 15 are binding confirmed at both laboratories and the 2 LqhIII designs at Adaptyv Bio only. Binding is not neutralization, and no animal efficacy test was done; Anthropic's page states that neutralization was not confirmed ([1](#ref-1)).
- **Pythia-1:** Per-design hit rates and the handling of controls could not be confirmed here.
- **Bits to Binders:** Down includes truly depleted designs and cannot quantify noise or false-positive counts. The between-team test assumes independent designs and ignores within-team correlation.
- **Affiliations and disclosure:** This article is a recount of public data. The AI I use (Claude) is an Anthropic model, and one compared item is Anthropic's own Claude result. Claude's results were therefore counted using only public data and the published criteria, with no added evaluation or speculation. The Pythia Labs preprint reports work by company employees ([2](#ref-2)).
- **Interval assumptions:** Wilson intervals assume independent results across designs. Claude's 211 designs were pre-selected and fall into groups sharing a target and design, so the actual uncertainty may be wider than the intervals shown.
- **Scope of verification:** The recalculation is a separate implementation by the same author, not third-party confirmation. The R recount covers counts, Up and Down, Claude's 17 and 11, and the Wilson interval for 17/211; it does not cover team-level results, the chi-square test, method groups or the sensitivity analysis.

## Conclusion

By threshold and denominator alone, the hit rate for the same experiment moved over 0.7–16.7% for Bits to Binders and 8.1–23.2% for Claude's toxin binders (29.4% including "weak or ambiguous" as a reference). The three reports differ in assay, threshold, replication, controls, prior selection and denominator, and the data here give no basis for placing the three on one scale.

Correction, 2026-11-02: clarified the definition of FDR and why Down counts do not quantify noise. Hit counts, rates and calculated intervals are unchanged.

## Data and code availability

Inputs are fixed versions of public data: `data/12k_all_results.csv` and `data/individual/master_data_teams.csv` from Bits to Binders (GitHub, commit 43eeeaf7e6ab629e796c9fe8d20b0ef70a3610d9) ([4](#ref-4)) and Anthropic's `design.csv` (Hugging Face, revision 0bac3d0286f7f83b5339f5b4f1e67fbe47a6e7c1, CC BY 4.0) ([5](#ref-5)). The inputs are pinned by SHA-256 (`input-provenance.json`); the data themselves are not bundled in the release materials. Pythia-1 numbers were transcribed from the paper into `results/pythia-reported.csv`.

The code is `acquire.py`, `analysis.py`, `figures.py`, `test_analysis.py` (5 unit checks) and `validate.R`; outputs are in `results/`. To rerun: `python acquire.py && python test_analysis.py && python analysis.py && python figures.py && Rscript validate.R` (Python 3.12, numpy, pandas, scipy, matplotlib, requests; R 4.5.3, jsonlite). No random numbers are used, and rerunning reproduced the result files byte for byte.

The full re-run materials are in the [companion archive](shared/bits-to-binders-hit-rates/bits-to-binders-hit-rates-companion.zip).


## References

<span id="ref-1"></span>1. Anthropic. How Claude designed protein binders against scorpion neurotoxins [Internet]. Anthropic; 2026 Oct 20 [cited 2026 Oct 30]. Available from: https://anthropic.com/research/claude-scorpion-toxin-binder-design

<span id="ref-2"></span>2. Aglietti RA, Ansari R, Bowers PM, Buelles TH, Chauvin H, Duplay TM, et al. Design of full-length agonist and antagonist antibodies for hard targets [Preprint]. bioRxiv; 2026. Version 1, posted 2026 Oct 26; not peer reviewed. [doi:10.64898/2026.10.21.760573](https://doi.org/10.64898/2026.10.21.760573)

<span id="ref-3"></span>3. Kosonocky CW, Abel AM, Feller AL, Cifuentes Rieffer AE, Woolley PR, Lála J, et al. Validation and analysis of 12,000 AI-driven CAR-T designs in the Bits to Binders competition [Preprint]. bioRxiv; 2026. Version 1, posted 2026 Mar 3; not peer reviewed. [doi:10.64898/2026.03.03.709355](https://doi.org/10.64898/2026.03.03.709355)

<span id="ref-4"></span>4. Kosonocky CW, et al. bits-to-binders [Dataset and software]. GitHub; 2026. Commit 43eeeaf7e6ab629e796c9fe8d20b0ef70a3610d9 [cited 2026 Oct 30]. [https://github.com/kosonocky/bits-to-binders](https://github.com/kosonocky/bits-to-binders)

<span id="ref-5"></span>5. Anthropic. scorpion-toxin-binder-design [Dataset]. Hugging Face; 2026. Revision 0bac3d0286f7f83b5339f5b4f1e67fbe47a6e7c1. CC BY 4.0 [cited 2026 Oct 30]. [https://huggingface.co/datasets/Anthropic/scorpion-toxin-binder-design](https://huggingface.co/datasets/Anthropic/scorpion-toxin-binder-design)

<span id="ref-6"></span>6. Benjamini Y, Hochberg Y. Controlling the false discovery rate: a practical and powerful approach to multiple testing. Journal of the Royal Statistical Society: Series B (Methodological). 1995;57(1):289–300. [doi:10.1111/j.2517-6161.1995.tb02031.x](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x).
