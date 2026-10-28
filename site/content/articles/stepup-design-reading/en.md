Bispecific antibodies that recruit T cells through CD3 commonly begin with step-up dosing to reduce cytokine release syndrome (CRS). Reading the 2026 exposure–response studies of elranatamab, targeting BCMA×CD3 in multiple myeloma, and epcoritamab, targeting CD20×CD3 in follicular lymphoma, reveals different kinds of evidence for dose design ([1](#ref-1), [2](#ref-2)).

Elranatamab’s first-dose CRS is associated with first-dose concentration and tumor burden. Epcoritamab’s three-step regimen has lower reported CRS than its two-step regimen: 49.4% versus 70.0% for any grade and 9.9% versus 26.9% for grade 2 or higher. Within the three-step regimen, however, no consistent exposure–CRS relationship is observed. Its cohort also receives hydration and dexamethasone prophylaxis, preventing attribution to the added step alone.

The design changes an early treatment procedure, including concentration, step count and prophylaxis. Exposure–response models explain part of that procedure rather than its entirety. This article reviews the full texts of two open-access studies and transcribes their reported numbers; it does not perform a patient-level reanalysis. The epcoritamab study grades CRS using ASTCT criteria.

## Elranatamab and first-dose concentration

Elranatamab uses 12 mg on day 1, 32 mg on day 4 and 76 mg from day 8, a two-step initiation. The population-PK and exposure–response study analyzes CRS after individual doses in 183 participants from the registration study.

After the first dose, 79 of 183 participants develop CRS. Two covariates increase its estimated probability: free concentration immediately before the second dose on day 4, described as approximately the peak concentration during this interval, and high tumor burden. The odds ratio per one log-unit increase in concentration is 3.86 (95% interval 2.38–6.55); the odds ratio for high tumor burden is 3.11 (1.40–7.17). Odds are probability divided by one minus probability; these are not risk ratios.

CRS also occurs after the second dose, but without a significant exposure relationship. More than 90% of participants have no CRS after the first full dose, precluding that analysis. Premedication type and use were candidate covariates but were not retained in the final model. This does not establish that premedication is ineffective or unrelated to CRS.

The findings support an association between the height of the initial concentration step and first-dose CRS. In a [related analysis](elranatamab-stepup-en.html), I use that relationship to compare first-dose designs with the published model. There is no corresponding model for subsequent CRS, so it cannot establish whether lowering the first dose merely shifts risk to later doses.

## Epcoritamab and the treatment procedure

Epcoritamab was developed with two step-up doses, 0.16/0.8/48 mg. A three-step initiation, 0.16/0.8/3/48 mg, was subsequently examined in follicular lymphoma. The 2026 paper compares these regimens in that disease.

PK and B-cell depletion are similar between the two-step group, with 127–128 evaluable participants depending on the assessment, and the three-step group, with 81. Any-grade CRS is 49.4% versus 70.0%, and grade 2 or higher CRS is 9.9% versus 26.9%, favoring the three-step cohort. Tocilizumab, an IL-6 receptor antibody used to treat CRS, is required in 11.1% versus 24.4%.

Median IL-6 remains low after each three-step dose, whereas it rises after the first full dose on day 15 in the two-step regimen. The authors caution that sparse sampling may miss peaks. Within the three-step regimen, neither interval Cmax nor AUC has a consistent relationship with CRS.

The three-step regimen is described together with adequate cycle-1 hydration and dexamethasone prophylaxis. This article has not verified the detailed two-step premedication protocol. The cohorts were enrolled at different times rather than randomized. The effect of the additional step cannot be separated from prophylaxis and other procedural changes. The findings concern follicular lymphoma and do not evaluate regimen design in other disease subtypes.

## Different evidence for different design changes

Table 1. Evidence explaining CRS and its limitations in the two studies.

| | Elranatamab | Epcoritamab |
| --- | --- | --- |
| Explanatory variables | First-dose concentration and tumor burden | Regimen and procedure; no consistent within-regimen exposure relationship |
| Evidence | Dose-specific logistic regression | Between-cohort comparison, IL-6 and cumulative CRS risk |
| Source of variation | Individual first-dose concentrations within the approved regimen | Step count, prophylaxis and hydration |
| Unresolved | CRS after dose 2 and later | Separating the added-step effect from prophylaxis |

### Concentration explains only part of the response

The elranatamab model links initial concentration to initial CRS. The epcoritamab report instead describes a procedural change with lower CRS without a corresponding consistent exposure difference. CRS also depends on the speed of T-cell activation, target abundance and premedication. Target biology differs: soluble BCMA is relevant in myeloma, whereas CD20 is also expressed on normal B cells in lymphoma. These studies do not isolate all those contributions.

### Adding a step differs from lowering the first dose

Lowering the initial dose enlarges the subsequent increment. Adding an intermediate step reduces increments. The lack of a prominent IL-6 increase after the first full dose with three-step epcoritamab is compatible with an increment-related mechanism. It remains a hypothesis because prophylaxis changes concurrently and IL-6 sampling is sparse.

### The evidence is not randomized

Neither comparison randomizes regimen design. Elranatamab provides exposure variation within one regimen; epcoritamab compares cohorts enrolled at different times. Claims of improvement must reflect those different sources of evidence.

## CRS reduction cannot be attributed to step count alone

Reducing first-dose CRS does not establish a reduction after later doses. When hydration and premedication change with step count, aggregate outcomes cannot identify the step-count effect separately. The two papers also do not compare exposure and cytokine trajectories under common conditions. This review cannot establish that a first-dose exposure coefficient transports unchanged to subsequent doses.

## Limitations

Only two papers are reviewed. Other strategies, including anti-CD20 pretreatment with glofitamab, prophylactic tocilizumab and outpatient step-up initiation, are outside scope. Diseases, targets and doses differ, so the drugs’ outcomes cannot be directly compared. The precise denominators for the reported epcoritamab CRS percentages could not be confirmed from the main text reviewed here.

## Data and code availability

The [source record](shared/stepup-design-reading/sources.md) documents reading scope and transcribed values. No original patient-level analysis is performed. Elranatamab odds-ratio intervals come from [original Supplementary Table S2](https://pmc.ncbi.nlm.nih.gov/articles/PMC13461831/).

## References {#references}

<span id="ref-1"></span>
1. Hibma JE, Irby D, Liu A, Elmeliegy M, King LE, Gifondorwa D, et al. Elranatamab population pharmacokinetics and exposure–response for cytokine release syndrome in patients with relapsed or refractory multiple myeloma. Clinical Pharmacokinetics. 2026;65:1173–1192. [doi:10.1007/s40262-026-01663-z](https://doi.org/10.1007/s40262-026-01663-z).

<span id="ref-2"></span>
2. Sinnollareddy M, Sanghavi K, Gibiansky L, Li T, Putnins M, Mohamed MEF, et al. Exposure–response analyses to inform the optimal epcoritamab monotherapy dosing regimen in relapsed or refractory follicular lymphoma. Clinical Pharmacokinetics. 2026;65:1415–1428. [doi:10.1007/s40262-026-01661-1](https://doi.org/10.1007/s40262-026-01661-1).
