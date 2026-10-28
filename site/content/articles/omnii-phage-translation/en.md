An AI-designed virus was administered to a person. The virus in question is a bacteriophage, which infects bacteria. On October 20, 2026, Radical Numerics announced administration of a preparation containing phages designed with its genome language model Omnii-1 to a patient with an antibiotic-resistant infection ([1](#ref-1)).

The question that interests me is how this changes the search for candidates suited to individual patients. Finding a compatible candidate is substantial work. Whether it reaches the infection site, remains active there and improves the patient's condition are further, separate questions.

## What is known about the patient {#_1}

According to the primary report, a cocktail containing AI-designed phage variants cleared the patient's resistant bacterial isolate in vitro and was subsequently administered through an authorized, physician-led compassionate-use pathway. This permits investigational treatment under oversight for patients with serious conditions and inadequate alternatives.

The patient's clinical course and treatment outcomes were not disclosed. Clearing bacteria in vitro does not establish resolution of infection in the patient. Nor can a cocktail result isolate the contribution of the AI-designed component ([1](#ref-1)).

The claimed world first refers to administration of AI-designed phages as described by the announcing organization. Neither phage therapy nor administration of engineered phages began here. A 2019 case report described engineered phages for a drug-resistant Mycobacterium abscessus infection ([2](#ref-2)).

The development is that a model supporting candidate design and selection entered a workflow that reached patient administration, rather than replacing the whole therapeutic process with AI.

## Bacterial species alone does not determine compatibility {#_2}

Phages do not act equally against all bacteria. Susceptibility can differ between strains of the same species, requiring candidates matched to a patient's isolate. This specificity offers selectivity but also complicates preparation of a suitable therapy ([3](#ref-3)).

The public Omnii-1 report distinguishes recovery of designed candidates in experiments from prioritization of candidates with high activity against particular bacterial strains. Recovery is a proxy for viability, not efficacy in a patient.

For one evaluation strain, 4.5% of the measured library exceeded the activity threshold. Among the model's top 100 candidates, 24 exceeded it. Dividing the published percentages gives approximately 5.33-fold enrichment. The report also states that 97 and 96 of the top 100 candidates exceeded the threshold for the other two strains ([1](#ref-1)).

![Recalculation of reported candidate prioritization](shared/omnii-phage-translation/figures/reported-prioritization.png)

Figure 1. Calculated from aggregate values in the primary report. The 4.5% library-wide value is rounded; its comparison with 24% among the top 100 is descriptive. This was not a trial randomly administering candidates to patients, and the percentages are not clinical response rates.

This is useful evidence for prioritizing experiments. The public description does not establish that the evaluation strain was the patient's isolate. Design evaluation, ranking evaluation and patient administration should not be assembled into one continuous performance series from the same data.

The report states that candidates in this ranking evaluation were excluded from activity-prediction training. Model-prioritized candidates were tested experimentally, with results informing subsequent decisions. The process that may accelerate is the search for compatible candidates. These ranking results do not determine a patient's dose or treatment duration.

## In-vitro activity and infection-site exposure differ {#_3}

Acting on a target and reaching the required location are distinct problems even for conventional drugs. Phages add replication in susceptible bacteria to distribution and removal. Immune uptake and antibodies can also alter their kinetics, as discussed in the personalized-phage-therapy consensus published in September 2026 ([4](#ref-4)).

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

Real phages can replicate in bacteria, so a decay-only equation cannot predict therapy. This is not a dosing or interval-selection model. It illustrates why candidate-selection performance does not fill the kinetic information gap.

## An earlier trial measured both blood and infection-site exposure {#_4}

Clinical development addressed this issue before AI-designed phages. Part 1 of the ELIMINATE trial of LBP-EC01, reported in 2024, was an open-label dosing study with 39 randomized participants. Its primary outcome measured phage levels in urine and blood ([5](#ref-5)).

Randomization was between dosing groups; this first part had no phage-free efficacy comparator, and all groups received antibiotics. Reduced bacterial counts and symptom resolution were reported in 16 participants meeting the specified conditions and evaluable through day 10. These findings do not isolate phage-only efficacy.

What matters for the present comparison is that the study measured blood and urine while assessing safety and tolerability to examine dosing. It involved a different preparation and patient population, so its pharmacokinetics cannot be transferred to Omnii-1. It nevertheless makes the measurements needed after candidate identification concrete.

The relevant correspondence links isolate susceptibility, active phage at the required site, changes over time, symptoms and safety. Advances in sequence generation or host prediction do not remove the need to measure these relations.

## The gap between candidate preparation and clinical course {#ai}

The report connects preparation of candidates for an individual resistant infection with in-vitro evaluation and patient administration.

Manufacturing, quality, pharmacokinetics, changing susceptibility and concomitant therapy intervene between candidate search and treatment outcome. AI origin does not separate their contributions.

The information examined here does not provide a quantitative chain from predicted ranking through in-vitro response and infection-site exposure to bacterial and symptom trajectories. Administration to a patient and a causal claim that AI improved treatment outcomes remain different conclusions.

## Data and code availability {#_5}

The [calculation code, aggregate inputs, figures and results](shared/omnii-phage-translation/omnii-phage-translation.zip) are provided. `analysis.py` and `plot.py` regenerate the figures and table. Arithmetic using reported values is stored separately from the dimensionless synthetic example. I did not retrain the model, design sequences, reanalyze the original experiments or fit patient data.

Sources were checked on October 24, 2026. Omnii-1 claims were read from the October 20 public technical report as available then, not treated as independently peer-reviewed clinical trial findings. Source text, images and sequences are not redistributed in the package.

## References

1. <span id="ref-1"></span> Iyengar A, Siranosian B, Sarkar A, Noonan A, Poli M, Nguyen E, et al. [Radical Numerics creates first AI-generated phages to reach human patient with Omnii-1](https://www.radicalnumerics.ai/blog/omnii-phage) [technical report]. Radical Numerics. 2026 Oct 20 [cited 2026 Oct 24].
2. <span id="ref-2"></span> Dedrick RM, Guerrero-Bustamante CA, Garlena RA, Russell DA, Ford K, Harris K, et al. [Engineered bacteriophages for treatment of a patient with a disseminated drug-resistant Mycobacterium abscessus](https://doi.org/10.1038/s41591-019-0437-z). Nat Med. 2019;25(5):730–733.
3. <span id="ref-3"></span> WHO Regional Office for Europe. [Bacteriophages and their use in combating antimicrobial resistance](https://www.who.int/europe/news-room/fact-sheets/item/bacteriophages-and-their-use-in-combating-antimicrobial-resistance) [fact sheet; cited 2026 Oct 24].
4. <span id="ref-4"></span> Würstle S, Lieberknecht-Jouy SC, Düchting A, Lößner H, Ceyssens PJ, Pirnay JP, et al. [A consensus-based guideline for personalized bacteriophage therapy](https://doi.org/10.1038/s41591-026-04654-6). Nat Med. 2026;32(10):3578–3594. Published online 2026 Sep 21.
5. <span id="ref-5"></span> Kim P, Sanchez AM, Penke TJR, Tuson HH, Kime JC, McKee RW, et al. [Safety, pharmacokinetics, and pharmacodynamics of LBP-EC01, a CRISPR-Cas3-enhanced bacteriophage cocktail, in uncomplicated urinary tract infections due to Escherichia coli (ELIMINATE): the randomised, open-label, first part of a two-part phase 2 trial](https://doi.org/10.1016/S1473-3099(24)00424-9). Lancet Infect Dis. 2024;24(12):1319–1332.
