## Small samples behind phase 2 success claims

The evidence behind a confident claim can be thinner than its tone. Articles published in spring and summer 2026 argue that AI-designed drugs pass phase 1 but do no better in phase 2, and that clinical validation rather than molecule design is the bottleneck. Tracing their numbers leads to a 2024 abstract, counts in a 2026 conference abstract, and an industry commentary describing similar performance. These are small samples or interim inventories. Agreement about the clinical bottleneck is an argument repeated across four articles, not four new measurements.

I reviewed an abstract, four articles, secondary materials, and my previous articles. Numbers below are transcribed; derived values come from `numbers.py`. X and LinkedIn posts were not read directly, only through quotations in articles.

## The 2024 abstract

Jayatunga and colleagues examine clinical pipelines at AI-centered biotechnology companies ([1](#ref-1)). The abstract reports phase 1 success of 80–90%, substantially above historical industry averages, and approximately 40% in phase 2, comparable to the historical average but based on a limited sample.

The authors interpret phase 1 as suggesting improved identification or design of drug-like molecules. According to ProMarket, even phase 1 involves approximately 24 molecules ([2](#ref-2)). I did not obtain the original full text, definition of success, or phase 2 numerator and denominator. Because the denominator is unverified, I assume four of ten as an example corresponding to approximately 40%. For four of ten, the exact Clopper–Pearson 95% interval is 12.2–73.8%, too wide to establish either equality or a difference from industry performance (`results/summary.json`). A [related article](ai-phase2-sample-size-en.html) examines that calculation.

## Tracing the citation chain

**Table 1.** Numbers and attribution in four secondary articles.

| Outlet | Date | Numbers used | Attribution |
| --- | --- | --- | --- |
| Trey's Thoughts, Substack ([3](#ref-3)) | 2026-04-01 | 6–10 years from first human dosing to approval; phase 1 entrants have 10–15% approval | No source in the accessible portion; some content paywalled |
| ProMarket, Santoro ([2](#ref-2)) | 2026-07-02 | Phase 1 80–90%; phase 2 approximately 40%; overall success from 5–10% to 9–18% | Attributed to Boston Consulting Group (BCG); 5–10% to 9–18% assumes historical phase 3 performance and is not observed |
| Petrie-Flom, Epstein and Niazi ([4](#ref-4)) | 2026-08-04 | Design “10 times faster” | Attributed to an Anthropic model announcement, without independent verification; no phase 2 success estimate |
| Clinical Trial Vanguard, Alsumidaie ([5](#ref-5)) | 2026-08-11 | Of 117 tracked assets, 8 cleared phase 2; phase 1 80–90%; approximately 40% | 117 and 8, and 80–90%, attributed to LinkedIn; approximately 40% has no stated source |


ProMarket makes attribution to BCG explicit, but describes a meaningful phase-3 cohort without its size ([2](#ref-2)). The counts 117 and eight also appear in a 2026 American Society of Clinical Oncology (ASCO) abstract (J Clin Oncol 44(16) suppl): 117 AI-enabled therapeutic assets across 63 companies, 60 completing phase 1 (51.3%) and eight completing phase 2 (6.8%), with a December 1, 2025 cutoff ([6](#ref-6)). I obtained those numbers through secondary commentary, not from the abstract itself. Matching numbers suggest a possible origin for the LinkedIn post, but Vanguard does not cite that abstract and provenance is not established.

The denominator 117 includes assets still in development. They enter the denominator before a phase-2 result, so 8/117 is not phase-2 success among resolved outcomes. Dividing eight by 60 phase-1 completions has the same problem. Neither equals the approximately 40% in the Jayatunga abstract, whose definition is unverified. Vanguard presents both quantities in one article, making them easy to conflate.

## An industry commentary

IQVIA's May 2026 commentary on Global R&D Trends reports 75% phase-1 success in the most recent three-year window for AI-enabled programs at emerging biopharma companies, clearly above non-AI programs, and phase-2 performance “on par” with non-AI ([7](#ref-7)). It supplies no phase-2 percentage and calls that cohort relatively small. AI involvement was confirmed rather than merely self-reported. I did not read the full underlying report. This is another observation pointing in the same direction, still with a small sample.

## The clinical-bottleneck argument

ProMarket ([2](#ref-2)) distinguishes failure of a molecule from failure of its underlying biological hypothesis and argues that AI has mainly addressed the former while costs accumulate later. Petrie-Flom ([4](#ref-4)) distinguishes prediction from evidence that a drug helps patients and argues for evidence requirements proportional to remaining uncertainty. Vanguard ([5](#ref-5)) emphasizes validating human outcome-changing biology rather than generating candidates. Trey ([3](#ref-3)) describes a shift from molecule identification to evidence generation.

I found no explicit cross-citations among these articles in the accessible text. Yet ProMarket and Vanguard reuse 80–90% and approximately 40%; this is not independent confirmation. Agreement can show that an argument is persuasive without increasing the strength of the data. Vanguard also reflects the perspective of a clinical-trials industry publication.

## Rentosertib as one concrete example

ProMarket calls the phase 2a idiopathic pulmonary fibrosis results of Insilico Medicine's rentosertib its brightest result so far ([2](#ref-2)). My [aggregate-data analysis](rentosertib-ph2a-en.html) examined robustness of the 60 mg group's +98.4 mL change in forced vital capacity (FVC). That is a within-group change, not a placebo-adjusted effect. The between-group 95% interval includes zero, and 8/18 (44%) participants in the 60 mg group lacked a week-12 FVC measurement. This does not make the trial a failure: safety was primary and FVC secondary. It illustrates uncertainty between initial human testing and demonstrated benefit within one study, not AI drug-discovery success overall.

## Conclusion

In the material read, the claim that AI-discovered drugs stall in phase 2 rests on small samples and interim counts, not on a measured phase-2 success rate. Phase-2 success, phase-2 completion, and the fraction of all tracked assets are different quantities. More articles repeating a number do not create more independent outcomes. Agreement that clinical validation is the bottleneck must be evaluated separately from measured support for that claim.

## Limitations

Jayatunga's paper was read as an abstract only; its outcome definition and phase-2 counts remain unverified. The ASCO numerical contents and IQVIA findings came through secondary commentary or a blog. X, LinkedIn, Reddit, and the inaccessible Fast Company article were not read directly. BCG attribution was transcribed from ProMarket rather than verified in its original analysis. Updated Exscientia, Schrödinger, BCG, and specialist-journal inventories were not searched. Four articles do not constitute a representative survey.

## Data and code availability

The [source inventory](shared/ai-drug-claim-chain/sources.md) records reading scope. [numbers.py](shared/ai-drug-claim-chain/numbers.py) and [summary outputs](shared/ai-drug-claim-chain/results/summary.json) contain derived calculations. No original clinical cohort was reanalyzed.

## References

1. <span id="ref-1"></span>Jayatunga MKP, Ayers M, Bruens L, Jayanth D, Meier C. How successful are AI-discovered drugs in clinical trials? A first analysis and emerging lessons. Drug Discov Today. 2024;29(6):104009. [doi:10.1016/j.drudis.2024.104009](https://doi.org/10.1016/j.drudis.2024.104009). Abstract only.

2. <span id="ref-2"></span>Santoro MA. Pharma's AI Boom Has Bet on the Wrong Bottleneck. ProMarket. 2026 Jul 2. [Article](https://www.promarket.org/2026/07/02/pharmas-ai-boom-has-bet-on-the-wrong-bottleneck/).

3. <span id="ref-3"></span>Trey. Clinical trials are the new bottleneck. Trey's Thoughts on Healthcare Markets & Technology. 2026 Apr 1. Partially accessible; source inventory linked above. [Article](https://www.onhealthcare.tech/p/clinical-trials-are-the-new-bottleneck).

4. <span id="ref-4"></span>Epstein WN, Niazi SK. AI Can Invent Drugs Faster. It Still Has to Prove They Work. Petrie-Flom Center, Harvard Law School. 2026 Aug 4. [Article](https://petrieflom.law.harvard.edu/2026/08/04/ai-can-invent-drugs-faster-it-still-has-to-prove-they-work/).

5. <span id="ref-5"></span>Alsumidaie M. AI is clearing Phase I. That's the wrong finish line. The Clinical Trial Vanguard. 2026 Aug 11. [Article](https://www.clinicaltrialvanguard.com/clinical-bellwether/ai-is-clearing-phase-i-thats-the-wrong-finish-line/).

6. <span id="ref-6"></span>Haque W, Sai-Palm K, Kasparcova MZ, Rana I, Verlingue L, Garassino MC, et al. Clinical-stage AI-enabled therapeutic assets: An industry-wide analysis of scale, clinical progression, and company characteristics. J Clin Oncol. 2026;44(16_suppl):11072. [doi:10.1200/jco.2026.44.16_suppl.11072](https://doi.org/10.1200/jco.2026.44.16_suppl.11072). Conference abstract; numerical content used via [secondary commentary](https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026).

7. <span id="ref-7"></span>IQVIA Institute. IQVIA Institute’s Global R&D Trends 2026 report finds credible signal on AI-enabled programs. 2026 May 14. [Commentary](https://www.iqvia.com/blogs/2026/05/iqvia-institutes-global-r-and-d-trends-2026-report-finds-credible-signal-on-ai-enabled-programs).
