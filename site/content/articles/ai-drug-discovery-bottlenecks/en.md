Literature and public materials checked on October 6, 2026. This article examines developments in 2026 through shifts in the constraints on drug discovery and development.

What interests me about AI drug discovery is less which model is smartest than **what becomes the next constraint when one part of development gets faster**.

Proposing many molecules does not make it possible to build and test all of them. Faster experiments do not necessarily predict efficacy in patients. Shortening enrollment and operational delays in trials does not shorten the observation of disease or long-term safety by the same amount.

My view is that **the ability to turn experimental results into evidence for development decisions is becoming more important alongside the ability to generate candidates**. That is different from claiming an industry-wide shortage of experimental capacity. Publicly documented changes need to be separated from hypotheses about their consequences.

## Connecting AI design to experiments {#1-ai}

AI developers made conspicuous moves into life sciences in 2026. OpenAI introduced GPT-Rosalind in April and expanded access for eligible organizations in September. Microsoft Research announced Quine on September 29, describing a system that combines biological prediction models with a process for conducting research. Neither announcement establishes clinical drug success ([OpenAI](https://openai.com/index/introducing-gpt-rosalind/); [Microsoft Research](https://www.microsoft.com/en-us/research/blog/introducing-quine-an-ai-research-system-designed-for-the-complexity-of-biology/)).

An experimental example came from Anthropic in August: Claude was combined with specialist protein-design tools. Across 1,320 designs from multiple configurations, 354 binders were obtained against 14 of 15 targets. The pooled fraction is 26.8%, but this is not the performance of one model in one 48-hour run. Results differed by configuration ([experimental report](https://www.anthropic.com/research/Claude-accelerates-protein-design); [technical report](https://www-cdn.anthropic.com/30bf50e22a01388bb29bf077ee3f244531594b7a.pdf)).

In Adaptyv's TREM2 design event, ten teams of people operating design tools and six autonomous-agent teams submitted candidates. One hundred candidates selected by computational ranking were tested. Binding was observed in 37: 25/65 human-team candidates and 12/35 agent-team candidates. An unclear difference does not establish general equivalence of human and agent abilities. There was one target, and experimental candidates had been selected from 141 submissions ([results and selection criteria](https://www.adaptyvbio.com/blog/agents-vs-humans)).

These examples support a bounded conclusion: agents can generate candidates with experimentally confirmed binding in particular design tasks. Binding, function, pharmacokinetics, safety and patient benefit remain separate stages of validation.

The experiments mainly concern protein and antibody design. Their performance cannot be extrapolated to all small-molecule, RNA or cell-therapy design. Acting on a target is also different from improving human disease through that intervention. Manufacturing, formulation, quality and nonclinical safety remain to be evaluated after a preclinical lead is obtained.

On October 2, Xaira reported two X-Design antibody-design cases. One assessed selectivity, cross-species reactivity and developability properties as well as target binding, reaching a preclinical lead in seven weeks. Antigens, reagents and the intended epitope had already been prepared. This was not seven weeks from target discovery to clinical development, and the cases were reported by the organization conducting the work. They illustrate a shift from asking whether a candidate binds to whether it can progress ([Xaira report](https://www.xaira.com/news/de-novo-design-of-progressable-antibodies-to-therapeutic-targets)).

## How far faster design reaches {#2}

The Design–Build–Test–Learn loop helps clarify which parts of discovery a computational improvement can affect.

![A conceptual diagram separating the Design–Build–Test–Learn loop from clinical validation.](shared/ai-drug-discovery-bottlenecks/figures/evidence-loop.svg)

*Figure 1. Author-created conceptual diagram. Stages process different quantities, so this does not compare their speeds on a single scale. Progress from design scores to measurements and clinical evidence requires separate validation.*

Faster design may make waiting for construction or measurement more conspicuous. Better candidate selection can also reduce the number of experiments needed. Automation, parallel operation and overlapping stages can move the constraint again.

Experimental demand therefore need not rise whenever AI improves. A more informative industrial question is **how much the next development decision improves within the same budget and time**.

Obtaining candidates of the same quality more cheaply or quickly has value, as does reaching targets that were previously inaccessible. Those local benefits and a claim of improved end-to-end development success require different comparisons.

A September Perspective in Nature Communications likewise discusses balancing activity with objectives including pharmacokinetics and safety in generative chemistry. Improving one objective does not necessarily move a candidate closer to development ([Torren-Peraire et al.](https://www.nature.com/articles/s41467-026-77324-3)).

## What financial results reveal about experimental demand {#3}

To examine the hypothesis of rising experimental demand, I checked public results from companies involved in synthesis, experiments, instruments and contract research. These are examples illustrating variation, rather than statistics measuring one common market.

| Business | Period and scope | Reported change | Interpretation limit |
|---|---|---|---|
| Twist Bioscience | Total revenue, fiscal Q3 2026 ending June 30 | $118.4 million; +23% year over year | Total sales, not the quantity of AI-related experiments |
| GenScript Life Science Group | Segment revenue, first half of 2026 | $319 million; +28.8% | Different scope from +27.3% on a comparable group-wide basis |
| Tecan | Total sales in local currencies, first half of 2026 | +3.4% | Currency-adjusted measure; AI-specific sales not separated |
| Revvity Life Sciences | Pro forma organic sales, Q2 2026 | −3% | Adjusted for business scope, currency and other factors |
| Charles River DSA | Discovery and Safety Assessment, Q2 2026 | Reported −1.9%; organic +0.2% | Divestiture and currency adjustments alter the comparison |
| Evotec | Total revenue, first half of 2026 | €301 million; −19.2% | Includes effects such as timing of partnership revenue |

Sources: [Twist](https://www.sec.gov/Archives/edgar/data/1581280/000158128026000044/twst-2026630xex991.htm), [GenScript](https://www.genscript.com/genscript-biotech-announces-2026-interim-results.html), [Tecan](https://www.tecan.com/corporate-news/tecan-reports-growth-of-3-4-in-local-currencies-and-adjusted-ebitda-margin-of-15-1-for-the-first-half-of-2026-outlook-confirmed-63595), [Revvity](https://news.revvity.com/press-announcements/press-releases/press-release-details/2026/Revvity-Announces-Financial-Results-for-the-Second-Quarter-of-2026/default.aspx), [Charles River](https://ir.criver.com/news-releases/news-release-details/charles-river-laboratories-announces-second-quarter-2026-results), [Evotec](https://www.sec.gov/Archives/edgar/data/1412558/000110465926095267/tm2623114d1_ex99-1.htm).

The table cannot rank growth on a like-for-like basis or identify companies benefiting most from AI: periods, business scopes and adjustments differ. It does show that experimental and research services are not all moving in the same direction.

Conversely, falling total sales do not establish the absence of capacity constraints for a particular experiment or region. Aggregate growth and local shortages or waiting times require separate evidence.

GenScript also reported that its AI drug discovery-related business doubled year over year. That is relevant evidence of demand, but its revenue and scope cannot be fully reconstructed from this statement. Sales growth alone does not establish shortage: prices, product mix, customer acquisition and outsourcing shifts can also raise sales.

A supply-constraint claim would need information on lead times, utilization, backlogs, unit prices, rejected projects and waiting times after capacity expansion. The materials checked here do not establish an industry-wide shortage caused by AI.

## Experimental APIs and accumulated data {#4-api}

Adaptyv announced an API in April for querying targets, ordering experiments, estimating costs, checking status and retrieving structured results. This can reduce the friction between model output, measurement and another design round. An API does not make experiments instantaneous or entirely unattended ([announcement](https://www.adaptyvbio.com/blog/adaptyv-api)).

Data-generation scale is also increasing. In July, Illumina reported more than 350 million measured cells and over six petabytes generated for the Billion Cell Atlas. This was a progress report, not completion of the billion cells in its name. In August, Lila described proprietary data from physically synthesizing and measuring 950,000 RNA sequences in cells. That organizational report does not establish that all data were released for independent validation ([Illumina](https://www.illumina.com/company/news-center/press-releases/2026/27191.html); [Lila](https://www.lila.ai/news/inside-lilas-rna-discovery-engine)).

Sharing arrangements are changing too. Lilly TuneLab describes federated learning in which participants use models and contribute to learning without directly sharing molecular information. This changes how data are held; it does not give everyone access to the entire training dataset ([TuneLab](https://tunelab.lilly.com/)).

I care less about volume alone than about whether a measurement's meaning can be reconstructed. A protein-design candidate recorded as “did not bind” conveys different information if it truly failed to bind or never expressed in the first place.

The TREM2 event separated 37 binders, 11 non-expressers and 52 non-binders among 100 candidates. That is more useful than collapsing the other 63 into a single negative class. Even non-binding depends on concentration ranges and detection limits. Measurements, failure reasons, selection history and unmeasured candidates affect the quality of the next training round.

Assay details, positive and negative controls and replicate results also matter. Testing only high-scoring candidates leaves the rest of the search space unevaluated. Independently selected exploration candidates or controls within the budget offer one way to examine that bias.

## Why generating data is insufficient {#5}

An August Perspective by Bender and colleagues in Nature Reviews Drug Discovery emphasizes connecting data to clinically relevant decisions rather than data generation itself. I used the publicly available relevant portions. This is an important counterargument to the view that physical experiments must become the next shortage ([Bender et al.](https://www.nature.com/articles/s41573-026-01496-2)).

I do not read it as an argument against investment in experiments. My reading is that **more measurements may do little to reduce decision uncertainty if the assay and the question do not match**.

Improving binding and achieving sufficient patient exposure require different experiments. An easily measured cellular response may not establish action on disease biology. One experiment probing where a prediction's assumptions fail can alter selection more than a large number of similar measurements.

A bottleneck is therefore not necessarily the slowest machine in a sequence. The issue is where evidence capable of changing the next decision can be obtained.

Consider a hypothetical candidate A with high in vitro activity but uncertain safe exposure in humans, and candidate B with somewhat lower activity but a more credible exposure profile. Checking exposure and safety assumptions may change their ranking more than more binding measurements. Evidence that required exposure cannot be achieved safely could justify reconsidering A. This is an illustrative example, not a comparison of actual drugs. Begin with the decision, then prioritize uncertainties whose measurement could change candidate selection or a continuation decision, accounting for cost and time. The most uncertain quantity need not be the most useful one to measure.

## Separate assumptions about experimental demand {#6}

For illustration, approximate total experiments across programs reaching a comparable decision point by program count \(P\), rounds per program \(R\) and candidates per round \(B\):

\[
E=P\times R\times B
\]

This assumes programs with similar decision points and workloads, represented by common values of \(R\) and \(B\). It omits experiment types, repeat measurements, costs and overlapping stages. Heterogeneous programs require summing their individual experiment counts.

| Illustrative assumption | Program-count multiplier | Rounds multiplier | Candidates-per-round multiplier | Experiment-count multiplier |
|---|---:|---:|---:|---:|
| Selection alone improves | 1.0 | 1.0 | 0.5 | 0.5 |
| More programs and better selection | 3.0 | 1.0 | 0.5 | 1.5 |
| More programs and fewer required rounds | 3.0 | 0.5 | 0.5 | 0.75 |

*These are author-specified assumptions, not measurements or market forecasts. Multipliers are relative to a reference scenario. The table does not directly forecast annual experimental demand.*

Fewer required rounds differ from shorter rounds. Faster experiments can permit more rounds within a fixed period, so time savings are not directly modeled here.

Even with the same halving of candidates per round, total experimental counts can rise or fall. Rising counts need not produce proportional external-service revenue if unit prices fall; internal experiments may not appear as supplier revenue at all.

Claims of greater demand should identify which factor AI changed. Current public financial results inform parts of this question, rather than identify every factor in the equation.

## Clinical progress and evidence of an AI advantage {#7-ai}

It matters that candidates involving AI design are reaching clinical tests.

Generate:Biomedicines lists its anti-TSLP antibody GB-0895 for severe asthma in phase III. On September 10, Insilico announced the first patient dosed in the phase III rentosertib trial for idiopathic pulmonary fibrosis (IPF). Reuters reported in January that Isomorphic Labs had shifted its first clinical-trial target from the previous year-end to late 2026. The latter is a reported plan, not confirmation of trial initiation ([Generate pipeline](https://generatebiomedicines.com/pipeline/); [Insilico announcement](https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3); [Reuters report](https://www.investing.com/news/stock-market-news/googlebacked-ai-drug-discovery-startup-isomorphic-labs-delays-clinical-trial-timeline-4456134)).

Even at phase III, target validation differs. TSLP has human validation in severe asthma through approved tezepelumab, whereas rentosertib tests TNIK intervention in IPF. Progress of the former does not validate a new target, and an existing approved drug does not establish GB-0895's own efficacy or safety ([FDA tezepelumab explanation](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-maintenance-treatment-severe-asthma); [rentosertib paper](https://www.nature.com/articles/s41591-025-03743-2)).

Rentosertib also has a peer-reviewed phase IIa trial published in 2025: 71 participants randomized for 12 weeks, primarily assessing safety and tolerability, with lung-function changes secondary. This is patient evidence about a candidate. It is not a matched comparison against non-AI-designed candidates and does not directly establish that AI causally raises success probability ([Xu et al.](https://www.nature.com/articles/s41591-025-03743-2)).

In May, IQVIA compared programs with identified AI involvement in emerging biopharma against non-AI programs in the same company-size category. Its public commentary described a 75% phase I success rate over the latest three years, similar phase II performance and too few phase III programs for analysis. It explicitly noted the small cohort. I used that public commentary, without independently recalculating every program and denominator in the paid report ([IQVIA](https://www.iqvia.com/blogs/2026/05/iqvia-institutes-global-r-and-d-trends-2026-report-finds-credible-signal-on-ai-enabled-programs)).

That is an encouraging signal, but AI use is not the only difference between groups. Indications, targets, modalities, funding, experience and selection remain potential explanations. Phase I progress does not automatically imply better patient efficacy or approval outcomes.

AI involvement in target discovery, molecular design and optimization of existing candidates also describes different processes. Reporting and selection favor visible successes; progress stories alone cannot supply success rates across all candidates.

I would like to know how early failures were recognized and how good the clinical candidates were under comparable tasks, rather than only how quickly a candidate was proposed.

## Nonclinical options still require validation {#8}

In March, the FDA issued draft guidance on New Approach Methodologies (NAMs), their use and validation. It concerns development-stage assessments for regulatory submission, rather than discovery research itself. The question is the purpose and scope within which human-derived test systems or computational models can be relied upon. A draft is not a final implementation standard ([FDA draft guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-considerations-use-new-approach-methodologies-drug-development)).

A September direct final rule also replaces certain references to animal testing with nonclinical terminology. As of October 6, 2026, it was not yet effective: the document gives February 4, 2027 as its effective date and provides for withdrawal in response to significant adverse comments ([Federal Register](https://www.federalregister.gov/documents/2026/09/22/2026-19350/nonclinical-testing-terminology)).

The FDA explains that this terminology change neither requires particular methods nor changes evidentiary standards. It cannot be read as eliminating animal studies or enabling development through computation alone ([FDA NAMs explanation](https://www.fda.gov/science-research/science-and-research-special-topics/new-approach-methodologies-nams)).

As assay options expand, validating what measurements represent and how well they predict human outcomes becomes more important. Fewer experiments and less necessary evidence are different propositions.

## Discovery speed and treatment outcomes use different scales {#9}

Molecular proposals, cellular responses and patient efficacy have different denominators and meanings of failure. Faster candidate generation cannot simply be substituted for clinical development success probability.

The Virtual Biology Initiative's proposed connection between measurement and models also concerns this gap. Announced plans should be distinguished from validated performance ([Biohub announcement](https://biohub.org/news/virtual-biology-initiative/)).

I have not collapsed these materials into one “AI drug discovery success rate” because their scales do not match.

### Scope and limitations

This essay draws across peer-reviewed papers and Perspectives, AI organizations' technical reports, life-science financial results and announcements, FDA and Federal Register materials, and reporting including Reuters. Searches were conducted on October 6, 2026. It is neither an exhaustive survey of news and social media nor an industry-wide statistical study or investment-return forecast.

Organizational self-reports are distinguished from independent validation. When paid material could not be read in full, only public portions were used. Table values retain their reported definitions without conversion to a common basis. The conceptual figure and assumption-based calculations are the author's, rather than observations of a particular development program.
