> **Conflict-of-interest disclosure:** AI (Claude) was used to write this article. Claude is a model of Anthropic, the company that acquired Mithril Medicine. The article reports only what Anthropic's own announcement and the technical report it published state, and does not go beyond them to third-party verification or to the internal circumstances of the transaction. At the author's direction the article was reviewed by three AIs; this is not confirmation by an independent human.

On 27 October 2026, Anthropic announced that it had acquired Mithril Medicine, a drug-development company with one employee ([1](#ref-1)). The announcement says the company took a possible treatment for one form of muscular dystrophy from an idea to "promising results in mice" in less than 18 months ([1](#ref-1)). What does this interval cover, and what does it not cover? And how far does the accompanying technical report support the interval and the mouse results? This article examines both questions using the two published documents.

## Scope and sources

Two documents are examined. The first is Anthropic's article published on 27 October 2026, which contains the acquisition announcement ([1](#ref-1)). The second is a technical report on Mithril Medicine's antibody work dated 26 October 2026. Each page of this report carries the label "Not peer reviewed", so it is not treated as a peer-reviewed paper ([2](#ref-2)). Both documents were produced by the acquiring party.

The announcement was reread in full on 2 November 2026. The technical report could not be retrieved in the current verification environment, and no PDF or extracted text corresponding to the earlier reading notes was retained. Report-derived numbers, page references and experimental conditions below therefore remain provisional transcriptions from those notes, rather than results rechecked against the primary document in this audit. In particular, Table 2 effect sizes and confidence intervals, experimental group details and Claude workflow counts remain unverified against the original and should not be quoted as established values. Individual animal records and supplementary-table values have not been validated either.

This article does not reanalyze any statistics. It performs only an arithmetic check (2/35) on the lower bound of the report's P value. Because there is no computational deliverable, no data and code availability section is provided. Transaction terms, and the timing and investor details that appear only in secondary news reports, could not be confirmed in the primary sources and are not used.

## What the sources state

Table 1 lists the announcement claims and the report description retained in earlier reading notes.

Table 1. Announcement claims and report description. Report-derived entries have not been reverified in this audit.

| Item | What the sources state |
| --- | --- |
| Announcement date | 27 October 2026 ([1](#ref-1)) |
| Company | Mithril Medicine, a company with one employee. Its founder, Cody Tranbarger, is at Anthropic as of the announcement ([1](#ref-1), [2](#ref-2)) |
| Disease targets | Two rare forms of muscular dystrophy ([1](#ref-1)). The report addresses LAMA2-related congenital muscular dystrophy (LAMA2-CMD) and lists α-dystroglycanopathy among the programs to be continued ([2](#ref-2)) |
| Type of drug | A bispecific "bridging" antibody designed to link laminin-α4 to α-dystroglycan and thereby reconnect muscle fibers to the basement membrane ([2](#ref-2)) |
| Stage | The announcement says the research as a whole is mostly preclinical and has not yet reached testing in humans ([1](#ref-1)) |
| Transaction terms | Not stated in either document |
| Technical report | Dated 26 October 2026; not peer reviewed ([2](#ref-2)) |

## What the "under 18 months" interval refers to

The announcement states that the founder used Claude to organize contracts, logistics and experiments with 11 external laboratories, and delegated many other aspects of the company's operations to Claude. As a result, the possible treatment for one form of muscular dystrophy went from an idea to "promising results in mice" in less than 18 months ([1](#ref-1)).

This interval has two features. First, its end point is a mouse result. The announcement expects that a drug could be ready to start clinical trials in humans as soon as late 2028, counted from the announcement, if the candidates continue to hold up ([1](#ref-1)). That is a conditional projection, separate from the 18 months. Second, the figure of 18 months appears only in the announcement. The earlier reading notes record no passage corresponding to 18 months in the report text, and its start point (the "idea") cannot be defined from it. The timeline of the pilot study in Figure 10C was not used to examine the interval ([2](#ref-2)).

Near the end point, the report itself states the status of the experiments. They were exploratory and not conducted under Good Laboratory Practice. Unless stated otherwise, experiments were neither randomized nor blinded, group sizes were not set by a sample-size calculation, and no primary endpoint was prespecified ([2](#ref-2), PDF p. 25). The earlier notes record no statements about an investigational new drug application (IND), toxicology studies or costs; this absence could not be rechecked against the report.

The molecules tested also need to be identified. The report states that the hypothesis was tested with two "tool molecules" built on published variable regions. It says that testing and optimizing novel constructs (individual molecular designs) requires screens far larger than the work with two tool molecules, and describes a panel of 113 constructs that was produced for that purpose ([2](#ref-2)). The result at the end of the 18 months therefore comes from tool molecules based on published sequences, which appears to precede selection among novel constructs (the author's reading).

This article does not rate the 18 months as fast or slow. A comparison needs the start and end points used in other programs. Neither document provides a comparator, and external figures could not be checked against their original sources, so none are set beside it.

## How far the mouse results support the claim

The report describes a pilot study in dyW mice, which lack laminin-α2 ([2](#ref-2)). Mice received the drug for six weeks and were compared with vehicle-treated dyW mice and wild-type mice. The molecules were a bivalent 1+1 CrossMab and a tetravalent 2+2 IgG-scFv. The measures were the maximum nerve-evoked force of the triceps (peak force) and forelimb grip strength.

According to [Figure 11B of the report](https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf#page=18), peak force in the 2+2 group was 1.95 times the mean of the vehicle group (95% confidence interval 1.51–2.51; 7 mice in the 2+2 group versus 4 in the vehicle group). With mouse as the unit, Welch's t test gave P = 0.0001 (unadjusted for multiplicity). With the litter (the pups of one mother) as the unit, an exact rank test on litter means gave P = 0.057 (4 litters in the 2+2 group versus 3 in the vehicle group). The 1+1 CrossMab showed no difference distinguishable from the vehicle group (1.08-fold; 0.67–1.76). In a comparison of the two molecules at the same nominal molar dose, the 2+2 group was reported at 1.80-fold (1.12–2.91) ([2](#ref-2), PDF p. 18).

For P = 0.057, the report states that it is the smallest value possible with seven litters ([2](#ref-2), [limitations passage of the report](https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf#page=21)). In the author's arithmetic check, there are 35 ways to choose 3 of 7 ranks for a 4-versus-3 comparison, and the smallest two-sided P is 2/35 = 0.057, which agrees with the report.

The report lists the following limitations of the results ([2](#ref-2), [limitations passage of the report](https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf#page=21)).

- Groups were enrolled in sequence, and the vehicle group followed a different dosing regimen.
- Each litter received a single treatment, and allocation was not randomized.
- After losses before week 6 (26 of 58 dyW mice), the treated groups had four to seven mice.
- Six treated groups and at least 11 endpoints were examined, so a chance finding is possible.
- Muscle exposure to the 2+2 was not measured; muscle levels were measured only for the 1+1 CrossMab.

The report also shows that the conclusion depends on the analysis chosen. Comparing the five groups of the main text (wild type included) by one-way analysis of variance with Tukey's test gave P = 0.43 on raw values and P = 0.023 on log-transformed values ([2](#ref-2), PDF p. 29).

The report's own wording should also be noted. The effect is described as "associated with" the treatment, and the data are said to "suggest" a partial restoration of force. The report calls the result a proof of principle, while stating that this interpretation requires a concurrent, blinded replication ([2](#ref-2)).

**Interpretation (the author's reading):** The report itself states that statistical support depends on whether mice or litters are the unit of analysis ([2](#ref-2), PDF p. 21). Pups in the same litter share genetic background and rearing conditions, and each litter received only one treatment. Because treatment and litter are confounded, the test with the litter as the unit answers the question that fits this design. At this sample size its P value cannot fall below 0.057. What the report shows is therefore not evidence of "no effect" but a power limit: the design cannot discriminate at the conventional threshold. P = 0.0001, with mouse as the unit, treats pups from the same litter as independent and may be smaller than the data warrant.

What the results support is that, in a pilot study, force tended to be higher in the 2+2 group. They do not establish efficacy in humans, durability of the effect, or mechanism.

## Division of labor between Claude and the team in one week

The report contains a section titled "Working with Claude" that describes one week of work, including review of data delivered by a manufacturing contractor ([2](#ref-2), [Figure 12 of the report](https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf#page=19)). The report states that this section was compiled by Claude from its own threads and notes and therefore carries a risk of bias. The report also states that Claude searched the literature, performed re-analyses, prepared figures and drafted the manuscript ([2](#ref-2), PDF p. 30).

Table 2 gives the numbers for that week.

Table 2. Values reported for the one-week case. CRO: contract research organization.

| Item | What the report states |
| --- | --- |
| Data | A 341-page report arrived from the production contractor on day 4. Claude took 2 min 40 s to give a first answer and 7 min 53 s to produce a visual synthesis of all 113 constructs |
| Triage | Claude marked 82 constructs for screening as is, seven for additional polishing, and 24 (constructs with three laminin-binding arms) to be held back |
| Human ruling | Claude recommended binding kinetics for all 113 constructs; the team overruled this and set the three arms aside on production criteria. About four minutes later Claude had revised the memo, schedule and drafts from 113 to 89 constructs |
| Emails | Claude drafted 17 emails and the team sent 12, each of which had been edited. Claude listed 41 points for which it had found no written statement, for confirmation before sending |
| Errors | Of six errors examined in detail, Claude found five (one after a question from a CRO and two before the affected email was sent). At least three reached a CRO in emails the team had edited and sent. One of these (a request for less material per tube than the assay CRO had asked for) was corrected within a day, before any tube was filled. Two others, both statements in Claude's review of the production data, went unnoticed for more than 4 days, and one remains unsettled |
| Pace | All 89 constructs were shipped for the two cell-based assays within a week of the ruling. Claude's median response times were 96 s for a first answer and 10 min for a full answer; the median first reply of a CRO took 8.5 h |

These values are the report authors' description of their own work. The report interprets the pace as set by the CROs' replies and by the team's decisions. It says that Claude performed reading, calculation, drafting and tracing a decision through every dependent step, while the judgments remained with the team ([2](#ref-2)). The report also states that, from these cases, human editing appears to test the decisions in an email more reliably than the details and premises the email carries ([2](#ref-2)).

**Interpretation (the author's reading):** The six errors in Table 2 are the number examined in detail, not an error rate. The denominator (the total number of Claude's drafts and statements) is not given in the report, so the frequency of errors cannot be assessed from this description alone. The one-week case was chosen and described by the report's authors, and the sources do not show whether it represents the work as a whole. What can be read is both that errors reached an external party even after human editing, and that Claude found five errors itself in the same week.

## Limitations

- Both sources were produced by the acquiring party. The report was drafted with the involvement of Claude. There is no third-party verification.
- The report is not peer reviewed. The mouse experiment is a single pilot study, and no independent replication is reported.
- This article does not reanalyze the mouse data. Report-derived numbers remain provisional because the original PDF could not be rechecked; individual supplementary-table values were not validated.
- The 18 months was not compared with other programs. No verified information on IND, toxicology or cost is used.
- The announcement was checked on 2 November 2026; later updates to Anthropic's article or report, and any disclosure of transaction terms, are not reflected.

## Conclusion

"Under 18 months from idea to promising mouse results" is the interval stated in Anthropic's announcement, and its end point is the result of a preliminary mouse study. The report’s treatment of this interval, its start point, IND, toxicology and costs could not be rechecked against the original. The announcement itself places the end point before readiness for clinical trials. The prospect of being ready to start trials in humans is a conditional projection: as soon as late 2028, counted from the announcement, if the candidates continue to hold up.

The mouse result remains a pilot showing a tendency toward higher force in the 2+2 group. P = 0.057 for the litter-level test is the smallest value attainable with seven litters, and the design lacked randomization and blinding. The report itself calls the result a proof of principle and asks for a concurrent, blinded replication. The report therefore supports neither the 18-month interval itself nor the size of the AI's contribution directly. What it supports is the scope of the preliminary mouse study and the one-week description of the work. The latter includes both the five errors Claude found itself and errors that reached an external party even after human editing.

## References

<span id="ref-1"></span>1. Anthropic. Early progress on accelerating drug development with Claude [Internet]. Anthropic; 2026 Oct 27 [cited 2026 Oct 31]. Available from: [https://www.anthropic.com/research/early-progress-drug-development](https://www.anthropic.com/research/early-progress-drug-development).

<span id="ref-2"></span>2. Tranbarger C, Mithril Medicine. Preclinical characterization of a bispecific bridging antibody for the treatment of LAMA2-related congenital muscular dystrophy [Technical report; not peer reviewed] [Internet]. Anthropic; 2026 Oct 26 [cited 2026 Oct 31]. 38 p. Available from: [https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf](https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf).
