An AI-designed virus was administered to a person. The virus in question is a bacteriophage, which infects bacteria. On October 20, 2026, Radical Numerics announced administration of a preparation containing phages designed with its genome language model Omnii-1 to a patient with an antibiotic-resistant infection ([1](#ref-1)).

The question here is what that announcement shows, and what it does not show, about the search for phage candidates suited to individual patients. What interested me was less the headline that AI made a drug than how the step of finding candidates for each patient changes. Finding a compatible candidate is substantial work. Whether it reaches the infection site, remains active there and improves the patient's condition are further, separate questions.

## Scope and sources {#scope}

The central source is the technical report published by Radical Numerics ([1](#ref-1)). It is a company report, not a peer-reviewed paper or a clinical trial report. I read its text on October 24 and 29, 2026. I did not extract numbers from the images of its figures, so the figures are treated only as far as the text describes them.

Related sources were checked as follows. The consensus guideline on personalized phage therapy was read in full. Only the abstracts were read for the phase 2 trial of LBP-EC01, the earlier work on generative phage genome design, the strain-level host-prediction study, the case report of antibody neutralization, the first engineered-phage case report and the article on the kinetics of self-replicating agents. The WHO Regional Office for Europe explainer was read as a web document. For sources read only as abstracts, claims are limited to what the abstract states.

This article contains two calculations of its own: arithmetic and interval estimation on counts and proportions given in the report, and a dimensionless synthetic example that illustrates differences in exposure. Neither uses patient data or the report's underlying data.

## What is known about the patient {#_1}

According to the primary report, a cocktail containing AI-designed phage variants cleared the patient's resistant bacterial isolate in vitro and was subsequently administered through an authorized, physician-led compassionate-use pathway. This permits investigational treatment under oversight for patients with serious conditions and inadequate alternatives.

The patient's clinical course and treatment outcomes were not disclosed. The report says it withholds them because even limited clinical information could identify the patient, and it states that observations from a single patient cannot establish general safety or efficacy ([1](#ref-1)). Clearing bacteria in vitro does not establish resolution of infection in the patient. Nor can a cocktail result isolate the contribution of the AI-designed component. The patient's bacterial species, the number of phages in the preparation, whether any components were not AI-designed, the manufacturing method and concomitant treatment are not stated in the text I read.

The meaning of "AI-designed" also needs checking. The design the report presents as its example is for the E. coli phage T7 (genome about 40 kb): Omnii-1 regenerates the region encoding gp17, the receptor-binding tail fiber protein, conditioned on the surrounding sequence, while the rest of the genome is kept. The report says it uses this design round to illustrate its approach, and the text does not say whether the preparation given to the patient used the same design ([1](#ref-1)). "AI-designed virus" is therefore best read as modification of selected regions, not as a genome written wholesale by AI.

The claimed world first refers to administration of AI-designed phages as described by the announcing organization. Neither phage therapy nor administration of engineered phages began here. A 2019 case report described engineered phages for a drug-resistant Mycobacterium abscessus infection ([2](#ref-2)). Generating phage genomes with a genome language model also has precedent. King et al. state in their abstract that complete genomes generated using the 5.4 kb phage ΦX174 as a template yielded phages viable in the laboratory, and that a cocktail of them overcame ΦX174-resistant E. coli strains ([3](#ref-3)). That abstract describes laboratory results and does not mention administration to patients.

The development is that a model supporting candidate design and selection entered a workflow that reached patient administration, rather than replacing the whole therapeutic process with AI.

## Bacterial species alone does not determine compatibility {#_2}

Phages do not act equally against all bacteria. The WHO Regional Office for Europe explainer says that phages used for therapy are highly specific to their hosts, that therapy can be tailored to individual infections, that phage therapy cannot be used against all infections, and that bacteria can develop resistance to phages ([4](#ref-4)). This specificity offers selectivity but also complicates preparation of a suitable therapy. It does not stop at the species level: Gaborieau et al. measured infection outcomes between 403 Escherichia strains and 96 phages strain by strain and reported predicting them from genomic information alone ([5](#ref-5)). That is why candidates matched to a patient's isolate must be sought.

The public Omnii-1 report distinguishes recovery of designed candidates in experiments from prioritization of candidates with high activity against particular bacterial strains. Recovery is the fraction of designs detected with sufficient sequencing support and serves as a proxy for viability; an undetected design is not necessarily nonviable. For designs with 11–15 amino acid changes from wild type, 69.9% were recovered, compared with 4.8% of random controls. Recovery is not efficacy in a patient. For activity, the report states that 2,161 of 6,694 variants with measurable activity exceeded wild type, and that random controls that did so had at most five amino acid changes ([1](#ref-1)).

Next comes the evaluation of candidate prioritization. For one evaluation strain, 4.5% of the measured library exceeded the activity threshold. Among the model's top 100 candidates, 24 exceeded it. Dividing the published percentages gives approximately 5.33-fold enrichment. The report also states that 97 and 96 of the top 100 candidates exceeded the threshold for the other two strains ([1](#ref-1)).

![Recalculation of reported candidate prioritization](shared/omnii-phage-translation/figures/reported-prioritization.png)

Figure 1. Calculated from aggregate values in the primary report. The 4.5% library-wide value is rounded; its comparison with 24% among the top 100 is descriptive. This was not a trial randomly administering candidates to patients, and the percentages are not clinical response rates.

The 5.33-fold value describes this fixed candidate set. The following intervals are sensitivity calculations under a hypothetical binomial model of repeated independent candidates with a common success probability. The selected top 100 is not a random sample, so these are not validated confidence bounds for the observed enrichment. The proportion 24/100 has a 95% Clopper–Pearson confidence interval ([6](#ref-6)) of 16.0–33.6%, assuming independent Bernoulli trials. Dividing those bounds by a fixed 4.5% gives enrichment of about 3.6–7.5-fold; rounding of the 4.5% alone gives 5.27–5.39. These come from the separately provided `extra-ranking-checks.py`. The top 100 may contain closely related sequences derived from the same parent phage and so need not be independent, and the uncertainty of the 4.5% itself is not included because the library size is not stated in the text. Even a lower bound above three-fold remains a result inside that hypothetical model. It does not guarantee several-fold gain in another design round or unseen strain.

For the other two strains, 97/100 and 96/100 have 95% confidence intervals of 91.5–99.4% and 90.1–98.9%, but these cannot be called a prioritization gain. The text does not give the library-wide proportion above threshold for these strains (it only describes a broad range of activity), so no enrichment can be computed, and the definition of the threshold is not in the text either. In addition, 57 of the top 100 candidates were shared between the two strains. This establishes shared ranking between two strains, but unknown library-wide copositivity prevents judging excess overlap relative to random ranking or broad host range. The report notes that the top candidates for the third strain did not overlap with the others, showing different selected sets without by itself establishing accurate strain-specific activity prediction; its result, 24/100, is however the lowest of the three.

Some points remain unresolved. The text does not say whether the evaluation candidates described as excluded from training were separated with sequence similarity taken into account, so performance inflated by closely related training sequences cannot be ruled out. The public description also does not establish that the evaluation strain was the patient's isolate. Design evaluation, ranking evaluation and patient administration should not be assembled into one continuous performance series from the same data.

The meaning of this evaluation is limited but concrete. Model-prioritized candidates are tested experimentally, and the results inform subsequent decisions. The process that may accelerate is the search for compatible candidates. These ranking results do not determine a patient's dose or treatment duration.

## In-vitro activity and infection-site exposure differ {#_3}

Acting on a target and reaching the required location are distinct problems even for conventional drugs. Phages add replication in susceptible bacteria to distribution and removal. It has long been argued that the pharmacokinetics of self-replicating agents differ from those of ordinary drugs, with outcome depending on density-dependent thresholds ([7](#ref-7)). The consensus on personalized phage therapy published in September 2026 lists, as topics needing systematic study, the effect of site-specific conditions such as low pH and bile acids on phage behavior and the ability of the host immune system to alter kinetics through phage uptake and pre-existing or induced antibodies ([8](#ref-8)). The same document expects artificial intelligence and mathematical modeling to reduce laboratory screening through host-range prediction and to contribute to pharmacokinetic–pharmacodynamic optimization ([8](#ref-8)).

A clinical case illustrates the point. A patient with M. abscessus lung infection received a three-phage cocktail active against the strain for 6 months. Sputum bacterial load fell tenfold within a month but rose again after two months. The authors associated this with the patient's neutralizing IgM and IgG antibodies against the phages and reported that it limited efficacy ([9](#ref-9)). This is one observation, but it shows that a cocktail active in vitro does not necessarily stay active in the body.

A deliberately simple dimensionless example illustrates this gap. I did not fit it to the Omnii-1 patient or to a particular phage.

Let the initial input be 1 and the relative amount of activity available at the infection site be

\[
a(\tau)=q\exp(-c\tau)
\]

where \(q\) is the fraction available at that site, \(c\) the rate of activity loss and \(\tau\) dimensionless time. Over an observation interval from 0 to 4, an integrated exposure measure is

\[
E=\int_0^4 a(\tau)\,d\tau
=q\frac{1-\exp(-4c)}{c}
\]

Replication, bacterial killing, bacterial regrowth and resistance are omitted. The calculation isolates exposure differences.

Table 1. Dimensionless synthetic examples varying site availability and activity loss.

| Hypothetical condition | \(q\) | \(c\) | Integrated exposure \(E\) |
| --- | ---: | ---: | ---: |
| High availability, slow activity loss | 1.0 | 0.25 | 2.528 |
| High availability, fast activity loss | 1.0 | 2.00 | 0.500 |
| Low availability, slow activity loss | 0.2 | 0.25 | 0.506 |
| Low availability, fast activity loss | 0.2 | 2.00 | 0.100 |

![Exposure differences in a dimensionless synthetic example](shared/omnii-phage-translation/figures/illustrative-exposure.png)

Figure 2. Synthetic values calculated from the equations, not measurements. Left: activity over time. Right: its integral from 0 to 4. Time represents neither hours nor days, and the vertical axis is neither plaque-forming units nor dose. Parameters were chosen for illustration and do not describe a patient population.

These four settings produce an approximately 25.3-fold exposure difference. That number has no intrinsic biological meaning; changing the values changes the difference. The point is that equal in-vitro activity does not determine infection-site exposure without information about delivery and activity loss.

Conversely, the second and third rows have nearly identical integrals. An integrated measurement alone cannot distinguish poor delivery from rapid loss. Time-resolved and location-specific measurements address different aspects of this ambiguity.

Real phages can replicate in bacteria, so a decay-only equation cannot predict therapy ([7](#ref-7)). This is not a dosing or interval-selection model. It illustrates why candidate-selection performance does not fill the kinetic information gap.

## An earlier trial measured both blood and infection-site exposure {#_4}

Clinical development addressed this issue before AI-designed phages. Part 1 of the ELIMINATE trial of LBP-EC01, reported in 2024, was an open-label dosing study of a six-phage preparation with 39 randomized participants. Its primary outcome measured phage levels in urine and blood ([10](#ref-10)).

Randomization was between dosing groups; this first part had no phage-free efficacy comparator, and all groups received an antibiotic (trimethoprim–sulfamethoxazole). Reduced bacterial counts and symptom resolution were reported in 16 participants meeting the specified conditions and evaluable through day 10. These findings do not isolate phage-only efficacy, and the 16 formed an exploratory pharmacodynamic population, not the outcome of all 39 ([10](#ref-10)).

What I noted is that the study measured blood and urine while assessing safety and tolerability to examine dosing. The reported maximum mean concentrations were 6.3×10⁸ PFU/mL in urine after intraurethral dosing and, in plasma, 4.0×10³, 2.5×10³ and 8.0×10⁵ PFU/mL in the three intravenous groups. Plasma levels depended on the intravenous dose, higher intravenous doses produced more adverse events, and some patients given 1×10¹¹ PFU intravenously had non-serious tachycardia and chills ([10](#ref-10)). Urine and plasma differ in matrix and route of dosing, so the ratio of these maxima (about 1.6×10⁵-fold for group A) is not treated as a measure of efficiency. Still, the numbers show site concentration and systemic exposure moving separately, the latter bearing directly on safety.

It involved a different preparation and patient population, so its pharmacokinetics cannot be transferred to Omnii-1. It nevertheless makes the measurements needed after candidate identification concrete.

The relevant correspondence links isolate susceptibility, active phage at the required site, changes over time, symptoms and safety. The consensus likewise asks for susceptibility to be checked as close to treatment initiation as possible, for phage distribution at the target site and immune responses to be analyzed where appropriate, and for systematic study of how laboratory susceptibility relates to clinical outcome ([8](#ref-8)). Advances in sequence generation or host prediction do not remove the need to measure these relations.

## The gap between candidate preparation and clinical course {#ai}

The report connects preparation of candidates for an individual resistant infection with in-vitro evaluation and patient administration. Manufacturing, quality, pharmacokinetics, changing susceptibility and concomitant therapy intervene between candidate search and treatment outcome. AI origin does not separate their contributions.

Three concrete consequences follow for reading the report. First, the ranking results (24/100, 97/100, 96/100) are performance in reordering candidates excluded from training within the library of one design round. Correspondence between the evaluation strains and the patient isolate is unconfirmed. A descriptive enrichment is available for the strain with a reported 4.5% baseline; baselines for the other two, the threshold definition and handling of related sequences remain unclear. Candidate costs and elapsed time were not measured, so hit-fraction enrichment is not a search-speed ratio. Second, even if the patient's course is published later, a single case potentially involving concomitant treatment and components that were not AI-designed, gives no basis for assigning the outcome to the AI design; doing so would require an evaluation that separates designed from non-designed components. Third, as Table 1 shows, between in-vitro clearance and infection-site exposure lie two factors, delivery and loss, that an integrated quantity cannot separate. A design like ELIMINATE, which follows urine and blood separately, is an example of reporting site-specific concentrations separately, and such observations determine how far kinetics can be evaluated independently of candidate selection.

## Limitations {#limits}

This article reads mainly a company's public technical report; I did not check the report's underlying data, figure values or supplementary materials. The interval estimate rests only on the counts given in the report and assumes the top 100 candidates are independent. The fold-enrichment for the top 100 depends on the rounded 4.5% and on a library size not given in the text. The exposure example is illustrative, and none of the conclusions estimates a patient's pharmacokinetics. For sources read only as abstracts ([2](#ref-2), [3](#ref-3), [5](#ref-5), [7](#ref-7), [9](#ref-9), [10](#ref-10)), methods and supplementary descriptions were not checked.

## Conclusion {#conclusion}

The announcement shows that a model supporting candidate design and selection entered a workflow that went through in-vitro clearance to patient administration, and that in one design round the model's top-ranked candidates contained many with high activity. It does not show the patient's outcome, the contribution of the AI-designed component, phage exposure at the infection site, or how the ranking performance relates to the patient's isolate. The announcement is therefore best read as a report on the step of candidate search for individual patients, and not yet as evidence of improved patient treatment outcomes.

## Data and code availability {#_5}

The [calculation code, aggregate inputs, figures and results](shared/omnii-phage-translation/omnii-phage-translation.zip) are provided. `analysis.py` and `plot.py` regenerate the figures and table. Arithmetic using reported values is stored separately from the dimensionless synthetic example. The Clopper–Pearson intervals and the enrichment range for the top-100 proportions were computed with a separate [supplementary script](shared/omnii-phage-translation/extra-ranking-checks.py) ([instructions](shared/omnii-phage-translation/extra-ranking-checks-README.md)) that takes only the reported counts 24, 97 and 96 and the proportion 4.5% as input. I did not retrain the model, design sequences, reanalyze the original experiments or fit patient data.

Sources were first checked on October 24, 2026, and the report text was read again on October 29. Omnii-1 claims were read from the October 20 public technical report as available then, not treated as independently peer-reviewed clinical trial findings. Source text, images and sequences are not redistributed in the package.

## References

1. <span id="ref-1"></span> Iyengar A, Siranosian B, Sarkar A, Noonan A, Poli M, Nguyen E, et al. [Radical Numerics creates first AI-generated phages to reach human patient with Omnii-1](https://www.radicalnumerics.ai/blog/omnii-phage) [technical report]. Radical Numerics. 2026 Oct 20 [cited 2026 Oct 29].
2. <span id="ref-2"></span> Dedrick RM, Guerrero-Bustamante CA, Garlena RA, Russell DA, Ford K, Harris K, et al. [Engineered bacteriophages for treatment of a patient with a disseminated drug-resistant Mycobacterium abscessus](https://doi.org/10.1038/s41591-019-0437-z). Nat Med. 2019;25(5):730–733.
3. <span id="ref-3"></span> King SH, Driscoll CL, Li DB, Guo D, Merchant AT, Brixi G, et al. [Generative design of bacteriophages with genome language models](https://doi.org/10.1126/science.aec2657). Science. 2026;393(6811):eaec2657.
4. <span id="ref-4"></span> WHO Regional Office for Europe. [Bacteriophages and their use in combating antimicrobial resistance](https://www.who.int/europe/news-room/fact-sheets/item/bacteriophages-and-their-use-in-combating-antimicrobial-resistance) [fact sheet; cited 2026 Oct 29].
5. <span id="ref-5"></span> Gaborieau B, Vaysset H, Tesson F, Charachon I, Dib N, Bernier J, et al. [Prediction of strain level phage-host interactions across the Escherichia genus using only genomic information](https://doi.org/10.1038/s41564-024-01832-5). Nat Microbiol. 2024;9(11):2847–2861.
6. <span id="ref-6"></span> Clopper CJ, Pearson ES. [The use of confidence or fiducial limits illustrated in the case of the binomial](https://doi.org/10.1093/biomet/26.4.404). Biometrika. 1934;26(4):404–413.
7. <span id="ref-7"></span> Payne RJ, Jansen VA. [Phage therapy: the peculiar kinetics of self-replicating pharmaceuticals](https://doi.org/10.1067/mcp.2000.109520). Clin Pharmacol Ther. 2000;68(3):225–230.
8. <span id="ref-8"></span> Würstle S, Lieberknecht-Jouy SC, Düchting A, Lößner H, Ceyssens PJ, Pirnay JP, et al. [A consensus-based guideline for personalized bacteriophage therapy](https://doi.org/10.1038/s41591-026-04654-6). Nat Med. 2026;32(10):3578–3594. Published online 2026 Sep 21.
9. <span id="ref-9"></span> Dedrick RM, Freeman KG, Nguyen JA, Bahadirli-Talbott A, Smith BE, Wu AE, et al. [Potent antibody-mediated neutralization limits bacteriophage treatment of a pulmonary Mycobacterium abscessus infection](https://doi.org/10.1038/s41591-021-01403-9). Nat Med. 2021;27(8):1357–1361.
10. <span id="ref-10"></span> Kim P, Sanchez AM, Penke TJR, Tuson HH, Kime JC, McKee RW, et al. [Safety, pharmacokinetics, and pharmacodynamics of LBP-EC01, a CRISPR-Cas3-enhanced bacteriophage cocktail, in uncomplicated urinary tract infections due to Escherichia coli (ELIMINATE): the randomised, open-label, first part of a two-part phase 2 trial](https://doi.org/10.1016/S1473-3099(24)00424-9). Lancet Infect Dis. 2024;24(12):1319–1332.
