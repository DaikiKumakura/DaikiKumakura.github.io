Sacituzumab govitecan (SG) and datopotamab deruxtecan (Dato-DXd) both target TROP2. Borrowing an existing drug's payload exposure may look attractive when developing another TROP2 ADC. Before matching units, however, a more basic question comes first: **what was measured, and how was “ADC concentration” calculated?**

Between an older SG label and the 2026 version, the reported ADC AUC over the first 168 hours increased 2.136-fold, while the reported free-SN-38 AUC changed by −5.0%. This is not evidence that patient exposure doubled over calendar time. Public assessment documents explain changes in derived ADC concentration and the PopPK model.

I examined whether a numerical exposure ranking between the drugs is supportable. **These aggregate PK and E–R sources do not establish a transferable payload exposure target or potency ranking.** The reasons involve measured versus derived quantities, time windows and outcomes, rather than merely the fact that the drugs differ.

## Question and scope {#_1}

The question is whether published PK and E–R evidence supports a common payload target or ranking across TROP2 ADCs. The context of use is public-data research and discussion of information gaps, not patient treatment or trial-dose selection.

I checked label histories, papers and 2026 assessment documents, then calculated unit conversions and sensitivity of derived concentrations. This is neither PopPK estimation from patient concentrations nor a full reimplementation of the existing models. The plan was fixed after source exploration and before numerical calculation.

## “SG concentration” has more than one derivation {#sg}

The 2024 SG PopPK paper measures total and free SN-38 by LC–MS/MS and total antibody separately. SG concentration is derived from conjugated SN-38 under DAR=8. **Measured total antibody and this derived SG concentration are different quantities** [1].

The 2026 EMA assessment describes an integrated model of total antibody, free SN-38 and total SN-38, deriving SG concentration from a time-varying DAR. It identifies incorporation of DAR as a major contributor to changes in AUC and half-life. It also notes that derived SG concentration is model-dependent and lacks confirmatory data. This is not described as a change in the assays themselves [2, printed pp. 18–20, 34].

| Reported SG label quantity | Older version 18 | 2026 version 20 | Calculated reporting difference |
| --- | ---: | ---: | ---: |
| ADC AUC0–168 (ng·h/mL) | 5,640,000 | 12,049,500 | 2.136-fold |
| Free SN-38 AUC0–168 (ng·h/mL) | 3,696 | 3,510 | −5.0% |
| Free SN-38 Cmax (ng/mL) | 98.0 | 108 | +10.2% |

The older version summarizes monotherapy; the current version includes monotherapy and pembrolizumab-combination populations. Models and patient composition also differ [3, 4]. **The entire 2.136-fold difference cannot be causally attributed to DAR alone.** This is not a paired recalculation of identical patient concentration histories under both definitions, and no confidence interval was attached to reporting differences.

![Comparison of reported SG label values](shared/trop2-payload-exposure/figures/label-version-differences.png)

Figure 1. Current/older reported-value ratios. These are three aggregate metrics, not three patients. The dashed line denotes identical reporting. The figure does not measure a clinical exposure change or improvement in model performance.

## DAR is not a constant scaling correction {#dar}

For molar concentration of conjugated payload $P(t)$, the two definitions are:

$$
C_{old}(t)=\frac{P(t)}{8},\qquad
C_{new}(t)=\frac{P(t)}{DAR(t)}.
$$

With the same $P(t)$, the instantaneous ratio is $8/DAR(t)$. The integrated ratio is not the reciprocal of a simple time-average DAR:

$$
\frac{AUC_{new}}{AUC_{old}}
=8\frac{\int P(t)/DAR(t)\,dt}{\int P(t)\,dt}.
$$

This is a molar-concentration identity, not a cross-drug potency conversion. Moving to mass concentrations also requires molecular weights and analyte definitions.

![Sensitivity of derived concentration to DAR](shared/trop2-payload-exposure/figures/dar-definition-sensitivity.png)

Figure 2. Algebraic $8/DAR$ for fixed conjugated payload; no patient data or estimated DAR trajectory is plotted.

If half the integrated conjugated payload lies at DAR=8 and half at DAR=2, the ratio is 2.5. Fixing DAR to the equally weighted mean of 5 instead gives 1.6. **The same mean DAR does not produce the same AUC conversion.** This verifies a nonlinear transformation; it is not a patient model reproducing the label's 2.136-fold difference.

## Matching units does not match the underlying exposure {#2}

The Dato-DXd paper measures ADC and released DXd in plasma, unlike SG's serum measurements and derived ADC concentration [1, 5]. “Free payload” means unconjugated to antibody; it does not mean unbound to plasma proteins.

| Item | SG | Dato-DXd | Remaining comparison issue |
| --- | --- | --- | --- |
| Payload | SN-38 | DXd | Different potency and intracellular kinetics |
| ADC concentration | Derived from conjugated SN-38; DAR assumption changed | ADC immunoassay | Measurement/derivation definitions and model versions |
| Payload AUC in public labels | 3,510 ng·h/mL over 0–168 h | 18 ng·day/mL, first-cycle AUC | Integration window and dosing history |
| Regimen | Days 1 and 8 of a 21-day cycle | Every 21 days | Number of doses and observation period |

The 18 ng·day/mL converts to 432 ng·h/mL. Identical units do not establish identical 168-hour integrals or bioactive exposure. Because the relevant Dato-DXd label table does not state the integration endpoint, I did not derive a 168-hour or 21-day mean from that row. Using the paper's cycle-1 measure would require alignment with its original definition and population [6].

The 0–168 h mean free-SN-38 concentration for SG can be calculated as 20.89 ng/mL. It is neither a whole-cycle mean nor a protein-unbound-SN-38 mean. A ratio of mass AUCs does not establish a ranking of intratumoral payload, efficacy or safety.

## E–R analyses do not share a common horizontal axis {#er}

The SG mTNBC E–R paper selects treatment-average SG concentration for ORR/CR and average total-antibody concentration for OS/PFS [7]. The 2026 Dato-DXd HR+/HER2− breast-cancer paper associates cycle-1 ADC AUC with OS, while its final PFS model selects baseline tumor size [8]. The September 2026 NSCLC paper uses different ADC exposure metrics for OS, PFS and ORR [9].

The problem is not only different tumor types. Even within one drug, outcome, observation window and patient background affect the selected exposure metric. Treatment-average exposure incorporates interruptions, reductions and time to an event. **An exposure association cannot be interpreted as the causal effect of increasing the same patient's dose.** Nor can an E–R model selecting ADC exposure be reinterpreted as a common free-payload E–R relationship.

## Different analytes do not establish one exposure target {#adc}

Total antibody, conjugated payload and unconjugated payload are different analytes. Derived exposure changes with the conversion to ADC concentration and the handling of DAR. The SG example shows how borrowing AUC without aligning definitions and source versions can make different quantities look like the same target.

Protein-unbound fraction alone does not equate the intracellular activity or tumor delivery of different payloads. FDA ADC guidance also addresses multicomponent bioanalysis and E–R [10]. This comparison establishes neither a common exposure target transferable to another ADC nor a recommended dose.

## Reproduction and limitations {#_2}

Numerical results are in `outputs/tables/`, generated by `analysis/01_audit.py`; the Notebook calls the same functions. Transcription of label numbers is checked by assertions against the originals, with source SHA256 verification. Patient records, concentration histories, paired model estimates and intratumoral bioactive payload were not obtained. This does not validate PopPK predictive performance or cross-drug equivalence.

Public papers and assessments were used for a reading audit. Their figures and tables are not reproduced or modified. Figures here are original calculations from public numbers and the stated algebra.

## Sources {#_3}

1. [Sathe et al. SG PopPK, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11106201/).
2. [EMA Trodelvy variation assessment, 2026](https://www.ema.europa.eu/en/documents/variation-report/trodelvy-vr-0000312649-epar-assessment-report-variation_en.pdf), Sections 2.3.2 and 2.3.4.
3. [TRODELVY US label, version 18](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=57a597d2-03f0-472e-b148-016d7169169d&version=18), Table 9.
4. [TRODELVY US label, version 20](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=57a597d2-03f0-472e-b148-016d7169169d&version=20), Table 13.
5. [Dato-DXd PopPK, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12706414/).
6. [DATROWAY US label, May 2026](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=2950227c-6230-4ca4-a135-46e44d9424a0&type=display), Table 10.
7. [Sathe et al. SG E–R](https://pmc.ncbi.nlm.nih.gov/articles/PMC11739744/), DOI 10.1002/cpt.3495.
8. [Tang et al. Dato-DXd breast-cancer E–R, 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13084299/), DOI 10.1002/jcph.70188.
9. [Hong et al. Dato-DXd NSCLC E–R, 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13572793/), DOI 10.1002/cpt.70477.
10. [FDA. Clinical Pharmacology Considerations for ADCs, March 2024](https://www.fda.gov/media/155997/download).

## Analysis functions and verification code {#_4}

The [ZIP of analysis functions and unit checks](shared/trop2-payload-exposure/trop2-payload-exposure-functions.zip) excludes source data and full-analysis reproduction materials. Constructed test cases verify the implementation, not clinical data validity.
