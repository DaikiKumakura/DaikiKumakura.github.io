<span id="_4"></span>

## Abstract {#_1}

**Problem.** The US Food and Drug Administration (FDA) review of the RAS(ON) inhibitor daraxonrasib states that 300 mg once daily was approved for metastatic pancreatic cancer ([1](#ref-1), p. 17). In the applicant-written part of the same review, one reason given for choosing 300 mg is a translational prediction that bridges animal efficacy data to humans with a pharmacokinetic/pharmacodynamic (PK/PD) model. According to it, 100% of patients at 300 mg reach at least 90% RAS-pathway inhibition (75% reach at least 95%), compared with 91% (38%) at 200 mg ([1](#ref-1), p. 75). The review does not describe the details of this model.

**Methods.** I recomputed the same question using only numbers printed in the review: the coefficients of the human population PK (PopPK) model ([1](#ref-1), Table 59) and the concentration–response of target inhibition in mouse tumours ([1](#ref-1), p. 37). Tumour concentration was simply assumed to be R times whole-blood concentration. Virtual patients (4,096) were generated for each dose and each R.

**Results.** With R set to 4–7, the tumour-to-blood ratio of the area under the concentration–time curve (AUC) measured in mice, the share of patients reaching at least 90% inhibition on day 28 as a 24-hour average was 11.9–54.3% at 300 mg and 1.2–20.5% at 200 mg. By the pre-dose (trough) metric, the shares were 0.9–13.3% at 300 mg and 0.1–2.3% at 200 mg. For 99% of patients at 300 mg to reach at least 90% inhibition by the 24-hour average, R had to be about 22, and at that R, 95% of patients at 200 mg also reached it.

**Conclusion.** Within the published numbers and this simple assumption, the size of the applicant's predicted difference (100% at 300 mg versus 91% at 200 mg) could not be reproduced. This discrepancy is not evidence that the applicant's model is wrong; it is consistent with dependence on assumptions the review does not describe. The FDA assessed 300 mg as acceptable ([1](#ref-1), p. 75), and this calculation does not overturn that dose decision.

## Introduction {#1}

The review does not show how much the target-inhibition prediction separates 200 mg from 300 mg. It contains sections written by the FDA and sections written by the applicant that do not necessarily reflect FDA's views ([1](#ref-1), p. 1). This article recomputes the applicant's prediction from published inputs only and examines which assumptions the conclusion depends on.

**Question of interest (QOI):** At 300 mg and 200 mg once daily, what fraction of patients can suppress the tumour RAS pathway by at least 90%?

**Context of use (COU):** To recompute the applicant's prediction from public material and show the assumptions behind it. It is not used for prescribing decisions.

## Methods {#method}

### Input data {#2}

All inputs were taken from the FDA multidisciplinary review of NDA (new drug application) 220910 ([1](#ref-1)). Table 1 lists the inputs and the type of statement. Tables in the source are written as, for example, "Table 59 of the review" to distinguish them from the tables of this article.

Table 1. Inputs and applicant statements taken from the FDA review.

| Item | Value | Type of statement |
|---|---|---|
| Population PK ([Table 59](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/220910Orig1s000MultidisciplineR.pdf#page=242)) | Two compartments, first-order absorption, lag 0.305 h. CL/F (apparent clearance) 53.8 L/h, Vc/F (apparent central volume of distribution) 516 L, Q/F (apparent intercompartmental clearance) 26.1 L/h, Vp/F (apparent peripheral volume of distribution) 255 L, ka (absorption rate constant) 0.735 /h (2.49-fold at 160 mg or below) | Final PopPK model in the review ([1](#ref-1)) |
| Time-dependent relative bioavailability | Maximum decrease EM 0.357, days to half of it ET50 5.90 d | Same |
| Between-subject variability (variance) | CL 0.139, Vc 0.168 (covariance 0.0949), ka 0.847 | Same |
| Molecular weight | 811.05 g/mol | Review ([1](#ref-1)) |
| Preclinical target inhibition (Capan-2 xenograft, KRAS G12V, single dose) | Inhibition of tumour DUSP6 mRNA against intratumour concentration: EC50 54 nM, EC90 966 nM, maximum inhibition about 99% | Pharmacology section of the review ([1](#ref-1)) |
| Tumour-to-blood exposure ratio (mouse) | Tumour AUC is 4–7 times blood AUC. Tumour concentration persists longer than blood concentration | Same |
| Applicant's prediction (applicant statement) | At 300 mg, 100% with at least 90% inhibition and 75% with at least 95%. At 200 mg, 91% and 38% | Applicant statement ([1](#ref-1)) |
| Phase 3 (RASolute 302, applicant statement) | No significant exposure–response for efficacy (overall survival, progression-free survival, response, duration of response). Safety endpoints (grade 3 or higher adverse events, skin disorders, stomatitis and others) were significantly related to exposure, but the predicted difference between 200 mg and 300 mg was 10% or less. Median relative dose intensity 93.1%, median average daily dose 279.3 mg, interruption 56.0%, reduction 36.1% | Applicant statement ([1](#ref-1)) |

Note: Source pages are p. 47 for molecular weight, p. 37 for the pharmacology section, p. 75 for the applicant's prediction, and pp. 75–76 for the phase 3 exposure–response and dose intensity. Pages are the printed pages of the review; PDF page numbers are one higher. DUSP6 is a gene whose expression changes downstream of RAS signalling and is used as a marker of pathway activity. EC50 and EC90 are the concentrations producing 50% and 90% of the maximum effect. I did not determine whether each paragraph of the pharmacology section was written by the applicant.

The review states that in mice no simple relationship between blood concentration and DUSP6 inhibition could be derived, whereas one was obtained with intratumour concentration ([1](#ref-1), p. 37). It also states that at 25 mg/kg the tumour concentration stayed above the EC90 for at least 24 h and repeated dosing reduced tumours by more than 50% ([1](#ref-1), p. 37).

The phase 3 efficacy exposure–response analysis covers essentially a single dose of about 300 mg and is not a randomized comparison with 200 mg ([1](#ref-1), pp. 75–76). The FDA assessment agrees with the applicant's position and considers the proposed 300 mg once daily acceptable ([1](#ref-1), p. 75).

### Model {#3}

**Pharmacokinetics.** I implemented an approximate model from the published coefficients, supplying functional forms that were not published. Three assumptions were added.

- Relative bioavailability falls with treatment day $t$ (days) as $F(t)=1-0.357\,t/(5.90+t)$, assumed to be an Emax form, that is, saturating towards an upper limit.
- The coefficient 1.49 on ka at 160 mg or below was read as a factor of $(1+1.49)$, as the "2.49-fold" in Table 1. This reading is an assumption and is not used for the 300 mg and 200 mg results.
- Covariates were fixed to the reference patient reported in the review (65 years, 70 kg, bilirubin 8 µmol/L, one or more prior therapies), and individual differences were represented only by between-subject variability.

Dosing was simulated for 28 days, and whole-blood concentration on day 28 was used.

**Target inhibition.** Tumour concentration was set to R times whole-blood concentration, and inhibition $I$ (dimensionless, 0–0.99) was given by

$$I=\frac{0.99\,C_t^{\,h}}{EC_{50}^{\,h}+C_t^{\,h}},\quad C_t=R\cdot C_{\text{blood}}$$

where $C_t$ is tumour concentration and $C_{\text{blood}}$ is whole-blood concentration (converted to nM). The Hill coefficient $h$, which describes the steepness of the concentration–response curve, was set from the EC90 to EC50 ratio as $h=\ln 9/\ln(966/54)=0.76$. R was explored from 1 (tumour equals blood) through the mouse AUC ratio of 4–7. Two inhibition metrics are reported: the inhibition at the day-28 trough (immediately before the next dose) and the average of inhibition over the 24 hours of day 28.

**Weakness of the assumption.** Setting tumour concentration to blood concentration at each time point multiplied by R omits prolonged retention of the drug in tumour. In mice, tumour concentration persists longer than blood concentration, so the tumour-to-blood ratio at trough may exceed the AUC ratio. If such retention also occurs in humans, trough inhibition with a fixed R could be underestimated, but this analysis did not test the direction or size of the effect. Because inhibition is a nonlinear function of concentration, the same AUC with a different time course gives a different average inhibition. There is no guarantee that using the average reduces bias.

**Random numbers and scale.** The random seed for between-subject variability was fixed at 20261023, and 4,096 patients were generated for each dose. All shares use these 4,096 patients as the denominator.

## Results {#4}

### Model check {#result-check}

The median day-28 Cmax (maximum concentration) at 300 mg was 320.5 ng/mL. The review gives the geometric mean total Cmax at 300 mg as 391 ng/mL (0.48 µM) ([1](#ref-1), p. 47). The model median is 18.0% lower. The statistics differ, and the time point and population need not be the same. If model concentrations are low, the shares of inhibition below may also be low.

### Attainment of target inhibition {#result-attainment}

Figure 1 shows day-28 concentrations and the share reaching at least 90% inhibition at trough. Table 2 gives the shares for the main doses. With R of 1, 90% inhibition needs a whole-blood concentration of about 1,100 nM. This is higher than the EC90 in the review (966 nM) because the maximum inhibition is 99% and 90% is about 91% of that maximum.

![Target inhibition of daraxonrasib. A: day-28 whole-blood concentration profiles and the blood concentration needed for 90% inhibition. B: share of patients reaching at least 90% inhibition at trough by dose, with the applicant's prediction.](shared/daraxonrasib-target/figures/daraxonrasib_target.png)

**Figure 1.** Day-28 whole-blood concentrations of virtual patients and attainment of target inhibition at trough. A: whole-blood concentration (median and 5th–95th percentile range of 4,096 virtual patients per dose). Horizontal lines show the blood concentration required for 90% inhibition when tumour concentration is 4 or 7 times blood concentration. B: share of patients reaching at least 90% inhibition at trough. Tumour/blood in the figure is R in the text, with tumour concentration assumed to equal R times blood concentration. Stars show the applicant's prediction (applicant statement in the review). QD, once daily.

Table 2. Conditional predictions based on fixed tumour-to-whole-blood concentration ratios (day 28; share of 4,096 virtual patients per dose).

| Dose | Trough blood concentration (median) | At least 90% by 24-hour average (R = 4) | At least 90% by 24-hour average (R = 7) | At least 90% at trough (R = 4) | At least 90% at trough (R = 7) |
|---|---|---|---|---|---|
| 300 mg | 68 ng/mL (84 nM) | 11.9% | 54.3% | 0.9% | 13.3% |
| 240 mg | 55 ng/mL | 3.6% | 33.8% | 0.2% | 5.3% |
| 200 mg | 46 ng/mL | 1.2% | 20.5% | 0.1% | 2.3% |
| 160 mg | 33 ng/mL | 0.2% | 7.1% | 0.0% | 0.3% |

Note: R is the assumed ratio of tumour to whole-blood concentration. "24-hour average" means that the inhibition at each time point on day 28, averaged over 24 hours, is at least 90%; "trough" means that inhibition immediately before the next dose is at least 90%. Source: `results/target_attainment.csv`.

With R of 4–7, the share reaching at least 90% inhibition by the 24-hour average was 11.9–54.3% at 300 mg and 1.2–20.5% at 200 mg. At trough, it was 0.9–13.3% at 300 mg and 0.1–2.3% at 200 mg.

Rather than matching the applicant's 100% exactly, I used 99% as a convenient target and back-calculated the required R. For 99% of patients at 300 mg to reach at least 90% inhibition by the 24-hour average, R had to be about 22 (about 13 for 90% of patients, and about 7 for half). At R of about 22, 95% of patients at 200 mg also reached at least 90%. By the trough metric, the R required for 99% of patients at 300 mg was about 62, and at that R, 96% at 200 mg also reached it. By either metric, the size of the applicant's predicted difference (100% at 300 mg and 91% at 200 mg) was not reproduced by this simple model.

## Discussion {#5}

Using only the preclinical concentration–response published in the review, the human pharmacokinetics, and the simple assumption that tumour concentration is R times blood concentration, only a fraction of patients at 300 mg reach at least 90% inhibition when R is 4–7. Raising R to about 22 brings 99% of patients at 300 mg to that level, but then 95% of patients at 200 mg also reach it, and the difference in the applicant's prediction does not appear. The applicant's prediction is therefore considered to depend on assumptions not described in the review. Separating 200 mg from 300 mg by target-inhibition prediction requires the human tumour concentration and its time course, and the definition of the inhibition metric (trough or average, DUSP6 or another marker).

Three things cannot be concluded from this calculation.

- **That the applicant's model is wrong.** The applicant may have used an estimate of human tumour concentration, prolonged retention in tumour, mouse-to-human differences in protein binding, or another inhibition metric. Because the model details are not published, it is unknown which assumption differs.
- **That 300 mg is unnecessary.** The dose tested clinically was 300 mg, and the applicant reports improvements in overall survival and progression-free survival in the phase 3 trial ([1](#ref-1), p. 75). Including dose reductions and interruptions, median relative dose intensity was 93.1% ([1](#ref-1), p. 75). This calculation does not overturn that clinical result.
- **The actual value of inhibition in human tumours.** Data on target inhibition in tumour biopsies are not in the material examined.

<span id="6"></span>

Because the human tumour concentration course, the metric definition and the pharmacodynamics after dose reduction cannot be identified from public material, the assumption producing the difference cannot be isolated. The related [dose-fractionation analysis](daraxonrasib-dose-fractionation-en.html) also uses the same published PK coefficients ([2](#ref-2)).

## Limitations {#_2}

- The concentration–response of target inhibition comes from single-dose data in a mouse xenograft (KRAS G12V) and may not apply to human tumours or to tumours with mutations other than G12. The tumour-to-blood ratio is also from mice, and its time course was not included.
- Preclinical concentrations are total concentrations. Differences in protein binding between mice and humans were not handled (the mean maximum unbound blood concentration at 300 mg in humans is 3.56 nM ([1](#ref-1), p. 40)). This difference could change the inhibition prediction substantially.
- Covariates were fixed at the reference patient, and the distribution of patient characteristics was not included. The functional form of the time-dependent bioavailability is an assumption.
- The model equations and the target-inhibition metric actually used by the applicant are not in the examined material. Differences in the computed values cannot separate shortcomings of the approximation here from differences in the applicant's assumptions.

## Conclusion {#conclusion}

Within the published numbers and the simple assumption that tumour concentration is R times blood concentration, the size of the difference between 300 mg and 200 mg in the applicant's prediction (100% versus 91% reaching at least 90% inhibition) was not reproduced. With R of 4–7, the share reaching at least 90% by the 24-hour average was 11.9–54.3% at 300 mg and 1.2–20.5% at 200 mg. From public information and this simple assumption alone, I could not verify how much the target-inhibition prediction separates 200 mg from 300 mg. This calculation does not judge the correctness of the applicant's model or the clinical appropriateness of 300 mg.

## Data and code availability {#_3}

[Code, inputs and results](shared/daraxonrasib-target/daraxonrasib-target.zip) are collected in daraxonrasib-target.zip. The tables and the figure can be regenerated with `python analysis/run_analysis.py` (NumPy, SciPy, pandas and Matplotlib; random seed 20261023). The inputs are values transcribed from the public PDF of the FDA review ([1](#ref-1)); the PDF itself is not redistributed.

## References {#article-references}

1. <span id="ref-1"></span>US Food and Drug Administration, Center for Drug Evaluation and Research. Multi-discipline review: NDA 220910, RASONQUE (daraxonrasib), Reference ID 5858563 [Internet]. Silver Spring (MD): FDA; 2026 [cited 2026 Oct 29]. Available from: [https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/220910Orig1s000MultidisciplineR.pdf](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/220910Orig1s000MultidisciplineR.pdf). Page numbers refer to the printed review pages.
2. <span id="ref-2"></span>Kumakura D. Daraxonrasib dose fractionation: opposing exposure metrics [Internet]. Daiki Kumakura; 2026 Nov 16. Available from: [daraxonrasib-dose-fractionation-en.html](daraxonrasib-dose-fractionation-en.html).
