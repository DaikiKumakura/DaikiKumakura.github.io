First place identifies the top row of a leaderboard, not necessarily a method reliably better than its competitors. I compared three 2026 examples: the OpenADMET PXR challenge, LifeSciBench and AIntibody. Published numbers were transcribed; derived quantities come from the distributed `numbers.py`. I could not read the AIntibody full paper or Inductive Bio release, so corresponding claims remain secondary-source observations.

## Conditions behind a ranking

I considered five questions: whether test information was hidden or contaminated; whether an official ranking exists; whether uncertainty is reported; whether design, grading and participation are separated; and whether random, simple or experimental baselines are included.

Table 1. Scope of the comparison.

| | PXR challenge | LifeSciBench | AIntibody |
|---|---|---|---|
| 1 Test information | Hidden test data | Developer runs all models; no contamination discussion found in inspected text | Designs preregistered; common experimental conditions |
| 2 Official ranking | Organizer leaderboard | Developer paper table | Paper; full text not read |
| 3 Uncertainty | Bootstrap-based tiers | None found in inspected material | Depends on source; see fourth section |
| 4 Separation of interests | Organizer differs from entrants | Developer created evaluation and participates; disclosed | Specifica organizes separately from participants |
| 5 Baselines | Leaderboard only | Other vendors' models, without Claude | Experimental, random and simple methods |

## PXR ranks and uncertainty

The blind PXR induction challenge ran March 17–July 1, 2026, with activity and structure tracks, over 350 activity participants and over 5,500 entries overall. Activity test data comprised 513 compounds, 253 initially and 260 subsequently. Final ranks used only the hidden second analogue set.

The organizer reports bootstrap estimates and statistical comparisons, forming tiers from the top entry down: a new tier begins at the first entry distinguishable from the current tier leader. All 4,950 pairs among 100 entries were compared with Benjamini–Hochberg false discovery rate control at 5% under its assumptions. FDR is the expected proportion of false rejections among rejected null hypotheses, not a guarantee on each observed comparison set. This describes the organizer's procedure; I did not recompute every test ([1](#ref-1)). Activity ranks use mean absolute error (MAE), lower being better.

Table 2. Top three activity entries.

| Rank | Entry | MAE (reported ± width) |
|---|---|---|
| 1 | matcha-croissant | 0.4061 ± 0.0280 |
| 2 | AIDD-LiLab | 0.4092 ± 0.0281 |
| 3 | AIDD-LiLab-Aggressive | 0.4104 ± 0.0282 |

The inspected post calls these bootstrap widths without defining the ± convention. Tier 1 contains 28 entries, ranks 1–28. The first–second gap is 0.0031, approximately 0.11 times the first width of 0.0280 (`results/summary.json`). That ratio is not a significance test; tier judgments come from the organizer.

Nondistinguishability is nontransitive: A may not differ detectably from B, and B from C, while A differs from C. Thus lower-tier entries can be indistinguishable from some higher-tier entries. First place does not show superiority over all other 27 tier-1 entries.

A July 14 Inductive Bio release claiming victory was identifiable in search, but I could not obtain its text or determine the track and metric. The inspected organizer post names only three leaders and not that company. I cannot assess the claim's validity.

Two Acellera blog posts, including one dated July 29, withhold quantitative placement claims pending a result source. This is a specific reporting choice, not evidence for a particular placement ([2](#ref-2)).

## LifeSciBench as a developer-run evaluation

Announced June 17, LifeSciBench includes 750 tasks written by 173 external experts and 19,020 rubric criteria, about 25 per task. Passing requires at least 70% of rubric points. The developer ran five models in a single-turn setting with browsing allowed. Numbers matched the inspected preprint ([3](#ref-3)).

Table 3. Published scores and approximate task-level intervals.

| Model | Normalized score | Pass rate | Approximate 95% pass-rate interval |
|---|---|---|---|
| GPT-Rosalind | 0.576 | 36.1% | 32.7–39.6% |
| GPT-5.5 | 0.519 | 25.7% | 22.7–28.9% |
| Gemini 3.1 Pro | 0.515 | 23.6% | 20.7–26.8% |
| GPT-5.4 | 0.479 | 20.7% | 18.0–23.7% |
| Grok 4.3 | 0.399 | 13.0% | 10.8–15.6% |

My Wilson intervals treat 750 tasks as independent samples and describe only task-sampling uncertainty, not a comparative hypothesis test. They omit multiplicity adjustment across five models. The preprint suggests multiple samples per task, which may make this unit inappropriate. I found neither confidence intervals nor repeat-run variation in the inspected text.

Because task-level outcomes are unavailable, I used an unpaired approximation for differences: GPT-Rosalind minus GPT-5.5 gives 5.8–15.0 percentage points; GPT-5.5 minus Gemini 3.1 Pro gives −2.3 to 6.5. Positive covariance of paired pass outcomes could narrow those intervals, but neither its sign nor magnitude can be established without paired data. Which differences exclude zero in a paired analysis therefore remains unknown.

The preprint discloses that OpenAI developed the benchmark and that evaluated models include OpenAI models. Claude is absent. Grading is automated or model-assisted without naming the grading model. Conversely, 453 independent experts participated in task validation, grading was spot-checked against expert judgments, and the single-turn limit is acknowledged. Even the leading model passes only 36.1%. Licensing and safety may constrain release of tasks and rubrics.

This is evidence for the developer's specified evaluation setting pending independent reproduction. Disclosure helps identify the context; it does not supply a numerical correction to the reported scores.

## AIntibody and the strength of its headlines

Specifica, an IQVIA business, designed this blinded evaluation and published its design in 2024 before outcomes. It received 511 designs from 29 organizations; another source says 33 teams. Each team had 14 days per challenge and could submit ten sequences, synthesized and measured under common conditions. The original appeared in Nature Biotechnology; Crossref lists online publication August 19, whereas commentary and the company release date to August 26–27 ([4](#ref-4)). I did not read its full text. The following evidence is from commentary, a newsletter and a release, kept distinct from the original ([5](#ref-5), [6](#ref-6)).

Table 4. Three challenges as described by secondary sources.

| Challenge | Secondary-source result |
|---|---|
| 1 Affinity maturation | Best AI 94.7 pM versus experimental phage maturation over approximately 3 months, 113 pM; commentary calls them statistically indistinguishable. A statistical consensus baseline ranks 3rd, 540 pM. |
| 2 Affinity ranking | Models beat selecting the most abundant clone in 9.8–13.8% of cases; the newsletter reports random selection beating models in 39%, but the precise interpretation of 39% is unresolved from the inspected source. |
| 3 De novo CDR design | Best affinity 2.9 pM fails developability; best passing result 8.69 pM versus experimental 9.2 pM. Nonbinding submissions: 30.4%. |

Here pM is a concentration unit for a dissociation constant. Under comparable conditions, a lower constant means higher affinity. The 94.7-pM value is 16.2% below 113 pM, or a 1.19-fold ratio (`results/summary.json`); this is not a general measure of binding being “16% stronger.” Measurement variation and repeat-assay details were absent from the inspected material. Challenge 2–3 values and the consensus baseline depend on one newsletter.

Aureka's headline says its AI design surpasses the best experimental result. Its release compares 94.7 and 113 pM and reports challenge-1 places 1, 2 and 5; challenge-2 place 3; and challenge-3 place 9, without significance, intervals or repeat-assay variation ([7](#ref-7)). Commentary calls the leading comparison a statistical tie and warns against interpreting it as field-wide computational superiority. Nondistinguishability is not a demonstrated equivalence margin.

Including random selection and a simple consensus baseline helps test the added value of complex methods. Random selection is not intrinsically the strongest baseline for every task.

## Interpretation of ranks and performance gaps

Blind design and an official leaderboard do not alone establish superiority. PXR's top tier contains 28 entries; the small numerical AIntibody affinity difference is reported as indistinguishable in commentary. OpenADMET explicitly supplied comparative tiers, whereas I found no corresponding uncertainty in the inspected LifeSciBench text.

Baselines also delimit the claim: AIntibody includes simple selection and experimental approaches; LifeSciBench compares other models. A company headline can be stronger than the interpretation of its own numbers, as in this AIntibody example, without proving a general pattern across all announcements. Across these three examples, ordinal ranks alone do not establish certainty or transferability of a difference.

## Limitations

I could not read the AIntibody full paper or cross-check its secondary values against the original. I read the LifeSciBench preprint but did not establish the grading model, task-release status or multiple-sample treatment. Inductive Bio's full release was unavailable. My LifeSciBench intervals omit run and grading variability. The inspected PXR leaderboard excerpt contains only three entries; the count of 28 comes from the organizer. These are selected examples, not a representative survey; X and forum responses were not read.

## Data and code availability

[Sources and reading scope](shared/benchmark-ranking-claims/sources.md), [derived calculations](shared/benchmark-ranking-claims/numbers.py) and [summary results](shared/benchmark-ranking-claims/results/summary.json) document the calculation and provenance.

## References {#article-references}

1. <span id="ref-1"></span>OpenADMET. It's the end of the PXR challenge as we know it (and I feel fine). 2026 Jul 3. [Organizer report](https://openadmet.ghost.io/its-the-end-of-the-pxr-challenge-as-we-know-it-and-i-feel-fine/).
2. <span id="ref-2"></span>Acellera. An AceProp submission to the PXR Blind Challenge. 2026 Jul 9. [Challenge report](https://www.acellera.com/blog/reaching-the-top-tier-of-the-pxr-blind-challenge-with-an-ai-agent-black-box-trainer/); Evaluating AceProp on public Polaris benchmarks. [Benchmark report](https://www.acellera.com/blog/aceprop-polaris/).
3. <span id="ref-3"></span>OpenAI. LifeSciBench. Preprint. 2026 Jun. [Full preprint](https://cdn.openai.com/pdf/b4299379-0a97-4ffa-8b9b-c3fbb299caa9/lifescibench_preprint.pdf).
4. <span id="ref-4"></span>Erasmus MF, Bedinger D, Hopkins E, Ferguson G, Strickler J, Graff CP, et al. A blinded, prospective benchmark of in silico antibody discovery anchored to experimental affinity and developability. Nat Biotechnol. Published online 2026 Aug 19. [doi:10.1038/s41587-026-03238-6](https://doi.org/10.1038/s41587-026-03238-6). Full text not read.
5. <span id="ref-5"></span>Nani D. An AI-designed antibody matched months of lab work in the first blinded test of its kind. Sovereign Magazine. 2026 Aug 27. [Commentary](https://www.sovereignmagazine.com/article/aintibody-ai-antibody-design-nature-biotech-212438).
6. <span id="ref-6"></span>The Signal. Bio/Health: Week of Aug 31, 2026, edition 3. 2026 Sep 1. [Newsletter](https://buttondown.com/fjgoff/archive/the-signal-biohealth-week-of-aug-31-2026-edition-3/).
7. <span id="ref-7"></span>Aureka Biotechnologies. Nature Biotechnology: Aureka wins the global blinded AI antibody benchmark: AI design surpasses the best experimental result. Press release. 2026 Aug 26. [Syndicated release](https://www.thailand-business-news.com/pr-news/nature-biotechnology-aureka-wins-the-global-blinded-ai-antibody-benchmark-ai-design-surpasses-the-best-experimental-result).
