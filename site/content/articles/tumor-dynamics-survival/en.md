## Abstract {#revision-section-1}

In a public subset of a colorectal-cancer trial, adding early tumor change modestly improved held-out discrimination. The uncertainty interval included no improvement, and calibration remained weak. The data therefore support a candidate for further study rather than a survival surrogate or treatment decision rule.

## Introduction {#the-question-comes-before-the-model}

The question of interest was whether an early tumor measurement adds out-of-sample information about later overall survival beyond baseline clinical factors and tumor burden. The context of use is research prioritization: deciding whether early monitoring deserves further predictive study. This analysis does not assess treatment switching, dosing, causal mediation, or qualification of a treatment-effect surrogate.

A tempting analysis uses each patient's smallest tumor measurement, wherever it occurred, to predict survival from treatment initiation. That analysis uses information that was unavailable at the prediction time. It also gives patients who survive longer more opportunities to have a response recorded. Here, the prediction time is explicitly fixed at week 16, and only earlier measurements enter the predictors.

## Methods {#data-and-the-audit-that-changed-the-analysis}

### Data and integrity checks {#revision-section-2}

The `colorectal` and `colorectalLongi` datasets distributed in **frailtypack 3.8.1** contain a random subset of 150 participants from the FFCD 2000–05 trial, comparing sequential and combination chemotherapy for metastatic colorectal cancer. The source-specific description in Chiou et al. establishes the time unit as years and corroborates the stored age categories. This is a secondary analysis of the distributed subset, not a reanalysis of the entire randomized trial ([1](#ref-1), [2](#ref-2)).

<span id="table-1"></span>Table 1. Data-integrity checks

| Audit item | Finding and consequence |
| --- | --- |
| Participants | 150, with 906 longitudinal measurements and 289 survival/recurrent-event intervals |
| Terminal outcome | 121 deaths and 29 right-censored participants before exclusions |
| Record linkage | Participant IDs and stored clinical categories agreed across files |
| Time inconsistency | One measurement followed recorded death; exclude the affected participant in the primary analysis |
| Tumor scale | Box–Cox transformed, lambda 0.3; 34 measurements at a censoring floor |
| Endpoint | Overall survival; new-lesion records are not a qualified PFS definition |
| Age dictionary | Use stored <60, 60–69 and >69 years; preserve the discrepancy with the package help file |

Table 1 summarizes the integrity checks. Neither the time inconsistency nor the age dictionary was silently corrected. A sensitivity analysis retained the affected participant after removing only the inconsistent measurement. Raw participant records are not included in the companion archive; the acquisition and export scripts retrieve the official distribution. A software-package license does not establish every underlying clinical-data right.

### Landmark definition and predictors {#a-conditional-landmark-estimand}

The primary landmark was 16 weeks, converted using 52.1775 weeks per year. Eligibility required survival and observation beyond the landmark, a baseline tumor measurement, and at least one positive-time measurement on or before week 16. After the integrity exclusion, **128 participants with 101 subsequent deaths** entered the primary analysis. The target population is therefore the observed, landmark-eligible subset, not every randomized participant.

Two Cox models used exactly the same participants; fitting used the survival package ([3](#ref-3)). Table 2 lists their predictors:

<span id="table-2"></span>Table 2. Predictors available at the landmark

| Model | Predictors available by the landmark |
| --- | --- |
| Clinical | Treatment arm, two age-category indicators, WHO status ≥1, previous resection, baseline transformed tumor burden |
| Clinical + early change | Clinical predictors plus last early tumor value minus baseline and the time of that measurement |

The measurement time enters because a change observed early and a change observed near week 16 have different observation windows. The extended model is an **observed-feature model**, not a mechanistic tumor-growth inhibition model. Sparse early sampling does not justify estimating individual growth and kill rates.

The floor-censored last measurement occurred in one primary participant. A bounded sensitivity used the transformed nonnegative-size lower bound −1/0.3 and the documented rounded floor −3.33. It is an approximate sensitivity analysis, not a censored longitudinal likelihood. It also does not fully address floor censoring in every baseline or follow-up measurement. Tumor values are not interpreted as millimeters or RECIST percentage changes.

### Validation and uncertainty {#validation-instead-of-an-in-sample-association-claim}

Five patient-separated folds were repeated ten times using a fixed seed. Each Cox model and its baseline hazard were estimated in the training fold. Test participants' later measurements never entered the predictors. Repeated held-out predictions were averaged per participant, yielding a cross-validated ensemble assessment rather than an estimate of the performance of one final deployed fit.

Reported measures were concordance, one-year inverse-probability-of-censoring-weighted (IPCW) Brier score, and calibration. Training-fold censoring survival at one year was at least 0.963, exceeding the prespecified 0.20 support threshold. For the averaged-prediction assessment, censoring estimates were also averaged over repeats; this is an approximation to repeated cross-fitted IPCW evaluation. Paired bootstrap intervals resampled participants 1,000 times conditional on these predictions. They exclude uncertainty from refitting and are not prospective external-validation intervals.

## Results {#revision-section-3}

### Sampling and held-out prediction {#revision-section-4}

Figure 1 summarizes the early sampling density; Figures 2 and 3 show held-out performance and calibration. Table 3 gives the primary scores.

![Early sampling density limits individual kinetic modeling](shared/tumor-dynamics-survival/figures/early-sampling.png)

*Figure 1. Early tumor-sampling density in the public trial subset. Sparse individual measurements limit kinetic modeling. Original analysis.*

![Held-out discrimination and probability scoring](shared/tumor-dynamics-survival/figures/heldout-performance.png)

*Figure 2. Patient-separated held-out concordance and one-year IPCW Brier score for the two models. Intervals are conditional on the averaged cross-validated predictions and exclude uncertainty from refitting. Original analysis.*

<span id="table-3"></span>Table 3. Primary held-out performance

| Primary result | Clinical | Clinical + early change |
| --- | ---: | ---: |
| Held-out concordance | 0.532 | 0.581 |
| One-year IPCW Brier score, lower is better | 0.2543 | 0.2492 |
| Held-out calibration slope | 0.266 | 0.464 |

The concordance difference was **+0.049**, with a conditional 95% interval of **−0.005 to +0.106**. The Brier difference was **−0.0051**, with an interval of **−0.0272 to +0.0172**. Both intervals included zero. The extended model's calibration slope was 0.464 (0.081–0.847); a slope appreciably below one suggests overly strong risk separation in the held-out predictions.

![Held-out probability calibration](shared/tumor-dynamics-survival/figures/heldout-calibration.png)

*Figure 3. Held-out calibration for subsequent survival in the landmark-eligible subset. Predictions were averaged across repeated patient-separated folds. Original analysis.*

The full-data extended model associated increasing transformed tumor burden with worse survival, but that association did not establish useful prediction. Schoenfeld-residual tests did not detect a global proportional-hazards departure (clinical p = 0.58; extended p = 0.76). These tests have limited power and do not certify the model.

### Sensitivity analyses {#sensitivity-changes-the-target-population}

<span id="table-4"></span>Table 4. Landmark and integrity sensitivity analyses

| Landmark or integrity sensitivity | Participants / deaths | Clinical C | Extended C | Clinical Brier | Extended Brier |
| --- | ---: | ---: | ---: | ---: | ---: |
| Week 12 | 116 / 91 | 0.551 | 0.588 | 0.2531 | 0.2469 |
| Week 16, primary | 128 / 101 | 0.532 | 0.581 | 0.2543 | 0.2492 |
| Week 24 | 123 / 97 | 0.514 | 0.550 | 0.2479 | 0.2308 |
| Week 16, retain participant but drop inconsistent row | 129 / 102 | 0.531 | 0.572 | 0.2542 | 0.2485 |

Table 4 compares the landmark and integrity sensitivities. Changing landmarks changes eligibility and the information available. The week-24 result is not evidence that waiting longer is a superior clinical policy. The floor-bound sensitivity used identical primary folds and changed the extended Brier score by less than 0.000001. That small difference concerns this particular bounded numerical assumption; it does not remove selection bias or validate the tumor scale.

## Discussion {#what-the-analysis-supports}

Early tumor change retained some association with subsequent survival and slightly improved held-out scores. The uncertainty and weak calibration prevent a stronger predictive claim. Sparse longitudinal observations and the observation process limit interpretation of fitted trajectories.

## Conclusion {#revision-section-5}

Early tumor change added only modest held-out information beyond the clinical model, with intervals that included no improvement and weak calibration. It does not support a survival surrogate or a treatment decision rule.

The randomized origin does not make this landmark-selected secondary analysis a causal comparison of treatment strategies. Treatment effects on tumor change and survival are not sufficient to qualify a surrogate, and this dataset lacks the PK and dose histories needed for a dose–exposure–tumor–survival chain.

## Data and code availability {#reproduce-the-analysis}

[Download code, aggregate results and executed notebook](shared/tumor-dynamics-survival/tumor-dynamics-survival-companion.zip).

The companion contains acquisition scripts, R estimation code, aggregate tables, figures, and an executed notebook. It excludes participant-level CSVs and private planning documents. Run acquisition, R export, and `analyze.R` in that order. Numerical work used R 4.5.1 and survival 3.8-3. See [the companion instructions](shared/tumor-dynamics-survival/README.md).

## References {#sources}

1. <span id="ref-1"></span>frailtypack developers. frailtypack [Software and dataset documentation]. Version 3.8.1. CRAN. [Longitudinal dataset documentation](https://search.r-project.org/CRAN/refmans/frailtypack/html/colorectalLongi.html). The acquired source archive and extracted files are identified by SHA-256 in the companion acquisition record.
2. <span id="ref-2"></span>Chiou SH, Xu G, Yan J, Huang CY. Regression modeling for recurrent events possibly with an informative terminal event using R package reReg. J Stat Softw. 2023;105(5):1–34. [doi:10.18637/jss.v105.i05](https://doi.org/10.18637/jss.v105.i05).
3. <span id="ref-3"></span>Therneau TM. survival: a package for survival analysis in R [Software]. Version 3.8-3. CRAN. [Package documentation](https://cran.r-project.org/package=survival).
