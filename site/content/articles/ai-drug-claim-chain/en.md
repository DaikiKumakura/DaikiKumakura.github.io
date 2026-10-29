## Small samples behind phase 2 success claims

The evidence behind a confident claim can be thinner than its tone. Articles published in spring and summer 2026 argue that AI-designed drugs pass phase 1 but do no better in phase 2, and that clinical validation rather than molecule design is the bottleneck. Tracing their numbers leads to a 2024 abstract ([1](#ref-1)), counts in a 2026 conference abstract, and an industry commentary describing similar performance. These are small samples or interim inventories. Agreement about the clinical bottleneck is an argument repeated across four articles, not four new measurements. Whether an argument is reasonable and whether it has been tested against data are separate questions.

The phrase “AI drugs stall in phase 2” mixes three different claims. The first is a comparison of proportions: phase 2 success does not exceed the historical industry average. The second is a count: few AI-related assets have progressed through phase 2 so far. The third is an argument: the bottleneck lies in clinical validation rather than molecule design. Each needs different evidence. Moreover, even if the first claim holds, a higher phase 1 pass rate, in comparable cohorts using the same outcome definitions, raises the probability that a candidate entering phase 1 gets past phase 2 relative to the past. Phase 2 success “on par” with history does not mean stalling. The sections below check the sources for each claim in turn.

The scope of reading was as follows. For Jayatunga and colleagues I read only the abstract at Europe PMC. I read the full text of the ProMarket and Clinical Trial Vanguard articles and the IQVIA blog, and only the freely available part of Trey's Thoughts. The ASCO abstract is known through secondary commentary. The Petrie-Flom Center article could not be opened in this re-check because of site access restrictions, so it rests on my earlier reading record. X and LinkedIn posts were not read directly, only through quotations in articles. Numbers below are transcribed; derived values come from `numbers.py`.

## The 2024 abstract

Jayatunga and colleagues examine clinical pipelines at AI-centered biotechnology companies ([1](#ref-1)). According to the Europe PMC record, the authors are affiliated with Boston Consulting Group (BCG). The abstract reports phase 1 success of 80–90%, substantially above historical industry averages, and approximately 40% in phase 2, comparable to the historical average but based on a limited sample.

The authors interpret phase 1 as suggesting improved identification or design of drug-like molecules. ProMarket describes the BCG analysis as based on about two dozen AI-discovered molecules that had reached clinical trials ([2](#ref-2)). If that indicates the phase 1 sample size, phase 1 is also a small sample. ProMarket does not cite the paper, so I cannot confirm that its 24 molecules are the same analysis as Jayatunga and colleagues. The shared BCG affiliation makes that likely, but it remains an inference.

I did not obtain the original full text, definition of success, or phase 2 numerator and denominator. Because the denominator is unverified, I assume four of ten as an example corresponding to approximately 40%. For four of ten, the exact Clopper–Pearson ([3](#ref-3)) 95% interval is 12.2–73.8%, too wide to establish either equality or a difference from industry performance (`results/summary.json`). A [related article](ai-phase2-sample-size-en.html) examines that calculation.

The comparator, the “historical industry average,” is not a single value either. Estimates of clinical trial success rates are reported to differ significantly from widely cited statistics depending on the sample and definitions ([4](#ref-4)). Articles in fact describe the historical phase 1 rate differently: ProMarket writes “about half” ([2](#ref-2)), whereas Clinical Trial Vanguard writes 40–65% ([5](#ref-5)). Because the benchmark is not aligned, the size of “substantially higher” also changes between articles.

## Tracing the citation chain

**Table 1.** Numbers and attribution in four secondary articles.

| Outlet | Date | Numbers used | Attribution |
| --- | --- | --- | --- |
| Trey's Thoughts, Substack ([6](#ref-6)) | 2026/4/1 | 6–10 years from first human dosing to approval; phase 1 entrants have 10–15% approval | No source stated for the duration. The approval fraction is also not sourced, although the preceding sentence mentions another analysis (Nature Communications) (some content paywalled) |
| ProMarket, Santoro ([2](#ref-2)) | 2026/7/2 | Phase 1 80–90%; phase 2 approximately 40%; overall success from 5–10% to 9–18% | Attributed to Boston Consulting Group (BCG); the Jayatunga authors are also BCG-affiliated, but the paper is not cited. 5–10% to 9–18% assumes historical phase 3 performance and is not observed |
| Petrie-Flom, Epstein and Niazi ([7](#ref-7)) | 2026/8/4 | Design “10 times faster” | Attributed to an Anthropic model announcement, without independent verification; no phase 2 success estimate |
| Clinical Trial Vanguard, Alsumidaie ([5](#ref-5)) | 2026/8/11 | Of 117 tracked assets, 8 cleared phase 2; phase 1 80–90%; approximately 40% | 117 and 8, and 80–90%, attributed to a LinkedIn post (by a corporate AI head); approximately 40% has no stated source. The reference list consists of LinkedIn posts only |

ProMarket makes attribution to BCG explicit, but describes a meaningful phase-3 cohort without its size ([2](#ref-2)).

The counts 117 and eight also appear in a 2026 American Society of Clinical Oncology (ASCO) abstract (J Clin Oncol 44(16) suppl): 117 AI-enabled therapeutic assets across 63 companies, 60 completing phase 1 (51.3%) and eight completing phase 2 (6.8%), with a December 1, 2025 cutoff ([8](#ref-8)). I obtained those numbers through secondary commentary, not from the abstract itself. Matching numbers suggest a possible origin for the LinkedIn post, but Vanguard does not cite that abstract and provenance is not established.

Three cautions apply to reading these counts.

First, the denominator. The denominator 117 includes assets still in development. They enter the denominator before a phase-2 result, so 8/117 is not phase-2 success among resolved outcomes. Dividing eight by 60 phase-1 completions has the same problem. Second, the verb. The ASCO abstract, as described in secondary commentary, counts assets that completed phase 2, and completion includes both successes and failures. Vanguard describes the same eight as having cleared phase 2. Completing and clearing are different quantities, and the paraphrase changes what the count means. Third, the population. The ASCO count of 117 uses the broad definition of AI-enabled assets, and the secondary commentary points out the difference from a narrower definition limited to molecules designed by AI. Jayatunga and colleagues tabulate molecules from AI-centered emerging companies, so population and definition need not be the same. Beyond the different denominator, 8/117 may therefore concern a different group from the approximately 40%. Vanguard presents both “only 8” and “approximately 40%” in one article, making them easy to conflate.

## An industry commentary

IQVIA's May 2026 commentary on Global R&D Trends reports 75% phase-1 success in the most recent three-year window for AI-enabled programs at emerging biopharma companies, clearly above non-AI programs, and phase-2 performance “on par” with non-AI ([9](#ref-9)). It supplies no phase-2 percentage and calls that cohort relatively small. AI involvement was confirmed rather than merely self-reported. I did not read the full underlying report. This is another observation pointing in the same direction, still with a small sample.

IQVIA does not read “on par” as stalling, however. The commentary treats phase-2 parity favorably: if AI were merely pushing programs that would fail later into phase 1, phase-2 success would fall, and it did not. It says phase 3 transitions are not yet numerous enough to analyze meaningfully. Industry-wide success rates are unchanged from the prior year, and the improvement is visible only in one segment, emerging biopharma. In the breakdown of programs behind the analysis, the largest share of AI use is molecule design, typically against an already known biological target, and a smaller share involves target discovery ([9](#ref-9)). Part of the high phase-1 pass rate might be explained by known targets, but this source cannot separate that.

## The clinical-bottleneck argument

ProMarket ([2](#ref-2)) distinguishes failure of a molecule from failure of its underlying biological hypothesis and argues that AI has mainly addressed the former while costs accumulate later. Petrie-Flom ([7](#ref-7)) distinguishes prediction from evidence that a drug helps patients and argues for evidence requirements proportional to remaining uncertainty. Vanguard ([5](#ref-5)) quotes LinkedIn posts and argues that the real bottleneck is validating which biological mechanism changes human outcomes rather than generating candidates. Trey ([6](#ref-6)) describes a shift from molecule identification to evidence generation.

I found no explicit cross-citations among these articles in the accessible text. Yet ProMarket and Vanguard reuse 80–90% and approximately 40%; this is not independent confirmation. Vanguard reflects the perspective of a clinical-trials industry publication, and its references are four posts with no link to primary sources. “Agreement across four articles” therefore includes commentary and quoted posts rather than four independent analyses. Agreement can show that an argument is persuasive without increasing the strength of the data.

The premise of the argument can be checked against other material. A review of reasons for clinical drug development failure, summarizing analyses of 2010–2017 clinical trial data, lists lack of clinical efficacy (40–50%), unmanageable toxicity (30%), poor drug-like properties (10–15%), and lack of commercial needs and poor strategic planning (10%) ([10](#ref-10)). Lack of efficacy being the largest reason is compatible with the clinical-validation argument. Failure-reason shares do not measure duration, cost or throughput and cannot alone locate a rate-limiting stage. These figures are not limited to AI-derived molecules, however. Toxicity and drug-like properties are also failure reasons that molecule design can influence, and the review does not show whether those failures decline where AI does the designing.

## Rentosertib as one concrete example

ProMarket calls the phase 2a idiopathic pulmonary fibrosis results of Insilico Medicine's rentosertib its brightest result so far ([2](#ref-2)). That phase 2a trial randomized 71 participants to 30 mg once daily, 30 mg twice daily, 60 mg once daily, or placebo, and its primary endpoint was the percentage of participants with treatment-emergent adverse events ([11](#ref-11)). My [aggregate-data analysis](rentosertib-ph2a-en.html) examined robustness of the 60 mg group's +98.4 mL change in forced vital capacity (FVC). That is a within-group change, not a placebo-adjusted effect. The between-group 95% interval includes zero, and 8/18 (44%) participants in the 60 mg group lacked a week-12 FVC measurement. This does not make the trial a failure: safety was primary and FVC secondary. It illustrates uncertainty between initial human testing and demonstrated benefit within one study, not AI drug-discovery success overall.

## Discussion

Three readings change after this check.

First, how to read the approximately 40% in phase 2 from Jayatunga and colleagues. Because the sample is limited and the definition of success and the counts cannot be verified, the value shows neither equivalence to nor inferiority against the historical industry average. An article saying that AI is no different in phase 2 uses the abstract's “comparable” as a conclusion of equivalence. For four of ten, the interval is 12.2–73.8%, which includes values both above and below the historical average. Asserting equivalence would require a prespecified margin for the difference between success rates and an interval for that difference lying entirely within it. This article's calculation does not meet that condition.

Second, the distinction between counts and proportions. A count such as 8/117 differs from a proportion whose denominator contains only assets with resolved phase-2 outcomes, and it embeds follow-up censoring and the difference between completion and success. Reading it as a success rate would require, for the same cohort, the number of assets with a result (denominator), the number of successes (numerator), and the observation window. More articles quoting the ASCO abstract add no proportion-level evidence unless these three are present.

Third, the relationship between “stalls” and “on par.” The BCG estimate quoted by ProMarket says that with a high phase 1 pass rate and historical phase 2 performance, the probability that an AI-designed drug reaches approval roughly doubles ([2](#ref-2)). The doubling is an estimate under an assumption that phase 3 performs historically, not an observation. Even so, if “stalls” means that phase 2 success does not improve, the higher phase 1 pass rate pushes the overall probability upward, and the word does not fit. If it means that assets cannot get past phase 2, parity of the success rate with history does not support it. IQVIA likewise does not read phase-2 parity as a setback ([9](#ref-9)). The second meaning would require absolute numbers of assets passing phase 2, or an increase in failures specific to phase 2 and later. The material read here shows neither.

None of this judges whether AI drugs perform well or badly in phase 2 and later. It points out that the sources read lack the denominators and definitions such a judgment needs.

## Conclusion

In the material read, the claim that AI-discovered drugs stall in phase 2 rests on small samples and interim counts that do not establish a reliable comparative phase-2 success rate. Split into three claims, the answer is as follows. The claim that phase-2 success is similar to history is a point estimate from a small sample with an unverified definition, and it supports neither equivalence nor a difference. That few assets have progressed through phase 2 can be confirmed as a count, but it is an interim tally, not a success rate. The argument that clinical validation is the bottleneck is consistent with an independent summary identifying lack of efficacy as the main reason for failure, but agreement among articles quoting the same numbers is not independent confirmation. Hence “stalls in phase 2” can be neither supported nor refuted. Phase-2 success, phase-2 completion, and the fraction of all tracked assets are different quantities.

## Limitations

- Jayatunga's paper was read as an abstract only; its outcome definition and phase-2 counts remain unverified. Four of ten is an assumption.
- The ASCO numerical contents and IQVIA findings came through secondary commentary or a blog. The ASCO abstract itself was not obtained. The difference in the definition of “AI-enabled” also rests on secondary commentary.
- X, LinkedIn, Reddit, and the inaccessible Fast Company article were not read directly. The Petrie-Flom article could not be opened in this re-check because of access restrictions.
- BCG attribution was transcribed from ProMarket rather than verified in its original analysis. I have not confirmed that the BCG analysis and the Jayatunga paper are the same.
- The failure-reason percentages ([10](#ref-10)) are from a review; the underlying analyses were not read.
- Updated Exscientia, Schrödinger, BCG, and specialist-journal inventories were not searched. Four articles do not constitute a representative survey.

## Data and code availability

The [source inventory](shared/ai-drug-claim-chain/sources.md) records reading scope. [numbers.py](shared/ai-drug-claim-chain/numbers.py) and [summary outputs](shared/ai-drug-claim-chain/results/summary.json) contain derived calculations. No original clinical cohort was reanalyzed.

## References

1. <span id="ref-1"></span>Jayatunga MKP, Ayers M, Bruens L, Jayanth D, Meier C. How successful are AI-discovered drugs in clinical trials? A first analysis and emerging lessons. Drug Discov Today. 2024;29(6):104009. [doi:10.1016/j.drudis.2024.104009](https://doi.org/10.1016/j.drudis.2024.104009). Abstract only (Europe PMC); the full text was not accessed.

2. <span id="ref-2"></span>Santoro MA. Pharma's AI Boom Has Bet on the Wrong Bottleneck [Internet]. ProMarket; 2026 Jul 2 [cited 2026 Oct 29]. Available from: [https://www.promarket.org/2026/07/02/pharmas-ai-boom-has-bet-on-the-wrong-bottleneck/](https://www.promarket.org/2026/07/02/pharmas-ai-boom-has-bet-on-the-wrong-bottleneck/).

3. <span id="ref-3"></span>Clopper CJ, Pearson ES. The use of confidence or fiducial limits illustrated in the case of the binomial. Biometrika. 1934;26(4):404–413. [doi:10.1093/biomet/26.4.404](https://doi.org/10.1093/biomet/26.4.404).

4. <span id="ref-4"></span>Wong CH, Siah KW, Lo AW. Estimation of clinical trial success rates and related parameters. Biostatistics. 2019;20(2):273–286. [doi:10.1093/biostatistics/kxx069](https://doi.org/10.1093/biostatistics/kxx069). Abstract read; a corrigendum was published (Biostatistics. 2019;20(2):366, [doi:10.1093/biostatistics/kxy072](https://doi.org/10.1093/biostatistics/kxy072)).

5. <span id="ref-5"></span>Alsumidaie M. AI is clearing Phase I. That's the wrong finish line [Internet]. The Clinical Trial Vanguard; 2026 Aug 11 [cited 2026 Oct 29]. Available from: [https://www.clinicaltrialvanguard.com/clinical-bellwether/ai-is-clearing-phase-i-thats-the-wrong-finish-line/](https://www.clinicaltrialvanguard.com/clinical-bellwether/ai-is-clearing-phase-i-thats-the-wrong-finish-line/).

6. <span id="ref-6"></span>Trey. Clinical trials are the new bottleneck [Internet]. Trey's Thoughts on Healthcare Markets & Technology; 2026 Apr 1 [cited 2026 Oct 29]. Freely available part only; the remainder is paywalled. Available from: [https://www.onhealthcare.tech/p/clinical-trials-are-the-new-bottleneck](https://www.onhealthcare.tech/p/clinical-trials-are-the-new-bottleneck).

7. <span id="ref-7"></span>Epstein WN, Niazi SK. AI Can Invent Drugs Faster. It Still Has to Prove They Work [Internet]. Petrie-Flom Center, Harvard Law School; 2026 Aug 4. Not re-opened on 2026 Oct 29 (site access restriction); based on the earlier reading record. Available from: [https://petrieflom.law.harvard.edu/2026/08/04/ai-can-invent-drugs-faster-it-still-has-to-prove-they-work/](https://petrieflom.law.harvard.edu/2026/08/04/ai-can-invent-drugs-faster-it-still-has-to-prove-they-work/).

8. <span id="ref-8"></span>Haque W, Sai-Palm K, Kasparcova MZ, Rana I, Verlingue L, Garassino MC, et al. Clinical-stage AI-enabled therapeutic assets: An industry-wide analysis of scale, clinical progression, and company characteristics. J Clin Oncol. 2026;44(16_suppl):11072. [doi:10.1200/jco.2026.44.16_suppl.11072](https://doi.org/10.1200/jco.2026.44.16_suppl.11072). Conference abstract, not obtained directly; numerical content used via [secondary commentary](https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026) (read 2026 Oct 29).

9. <span id="ref-9"></span>IQVIA Institute. IQVIA Institute's Global R&D Trends 2026 report finds credible signal on AI-enabled programs [Internet]. IQVIA; 2026 May 14 [cited 2026 Oct 29]. Blog commentary; the report itself was not read. Available from: [https://www.iqvia.com/blogs/2026/05/iqvia-institutes-global-r-and-d-trends-2026-report-finds-credible-signal-on-ai-enabled-programs](https://www.iqvia.com/blogs/2026/05/iqvia-institutes-global-r-and-d-trends-2026-report-finds-credible-signal-on-ai-enabled-programs).

10. <span id="ref-10"></span>Sun D, Gao W, Hu H, Zhou S. Why 90% of clinical drug development fails and how to improve it? Acta Pharm Sin B. 2022;12(7):3049–3062. [doi:10.1016/j.apsb.2022.02.002](https://doi.org/10.1016/j.apsb.2022.02.002). Review; failure-reason percentages are quoted from its text, the underlying analyses were not read.

11. <span id="ref-11"></span>Xu Z, Ren F, Wang P, Cao J, Tan C, Ma D, et al. A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial. Nat Med. 2025;31(8):2602–2610. [doi:10.1038/s41591-025-03743-2](https://doi.org/10.1038/s41591-025-03743-2). Abstract read.
