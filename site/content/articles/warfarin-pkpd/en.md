*Research reanalysis. Not peer reviewed.*

## A warfarin reanalysis of the value of limited PK measurements

Additional concentration measurements did not consistently improve prediction of subsequent prothrombin complex activity (PCA) in this reanalysis. A turnover model described the delay between concentration and response better than direct inhibition, but more PK information was not enough to recover individual PD sensitivity. This is an exploratory assessment of publicly distributed observations, not a dosing recommendation.

**日本語要約：** 公開された単回投与の個人別PK/PCAデータを解析した。作用の遅れを表現するturnoverモデルはdirect-effectモデルより良好だった。一方、24・48時間までの濃度情報を追加しても、その後のPCA予測は一貫して改善しなかった。個別化の価値は情報量だけでなく、何の個人差を測定できるかに依存する。推定警告が残るため、投与条件比較は探索的な感度分析と位置づける。

## The decision question

Can weight or limited postdose PK observations reduce uncertainty in a person's later PD response? The context of use is a research evaluation of the value of information under a single oral challenge. PCA is an activity measure. It is not interchangeable with a measured INR, a bleeding probability, or a therapeutic target. The work does not address chronic anticoagulant treatment.

The distinction matters: better concentration prediction need not imply better response prediction. PK variability and PD sensitivity are different quantities. A repeat-challenge simulation can explore this distinction, but it cannot establish benefit to patients.

## Audit the observations before fitting

The [nlmixr2data documentation](https://nlmixr2.github.io/nlmixr2data/reference/warfarin.html) describes a 32-subject warfarin dataset. I acquired a pinned upstream commit, saved source hashes, and checked the numerical records against the [University of Auckland original-data download](https://holford.fmhs.auckland.ac.nz/research/nlmixr/). That page also supplies a separate simulated dataset; it was not used here. All seven numerical columns match exactly, and endpoint and sex recodings match.

| Audit item | Actual input / treatment |
|---|---|
| Subjects / records | 32 / 515; documentation states 519 records |
| Dose / PK / PCA records | 32 / 251 / 232 |
| Administration | One oral dose per subject, approximately 1.5 mg/kg |
| Concentration / time units | mg/L / h |
| Measured PCA baselines | 30; values range from 82 to 100 |
| Primary PD likelihood | 188 postbaseline observations in those 30 subjects |
| Missing baseline | Two subjects excluded from PD, retained for PK |
| Zero concentrations | Four early observations, retained; no supplied LLOQ |
| Repeated PK time keys | Four in one subject, with different values; retained |

Each PCA observation was divided by that subject's measured baseline. The baseline itself was then excluded from the PD likelihood: using it both as a fixed normalizer and a residual observation would artificially lower the residual variance. Normalization still propagates baseline assay error and creates within-subject correlation that this minimal residual model does not represent. One subject has no PCA beyond 48 h, so the 48 h validation contains 29 subjects rather than 30. No later response was imputed.

The administered dose already depends on weight. This is not an experiment contrasting randomly assigned fixed and weight-based doses. Age, sex and genotype effects were not searched. Individual trial provenance, duplicate-sample provenance, assay censoring and interoccasion variability are not supplied. Upstream package licensing and acquisition information accompany the code; raw records are acquired rather than bundled.

![Observed concentration, PCA, dose–weight relation and sampling](shared/warfarin-pkpd/figures/01-data-audit.png)

*Figure 1. Actual observations and design. Unequal early sampling matters: 19 subjects first have PK measured at 24 h, leaving absorption chiefly informed by the densely sampled subset.*

## The minimum models

The oral one-compartment model has first-order absorption, apparent clearance CL/F and apparent volume V/F. Bioavailability cannot be separated from clearance or volume using these oral data. Individual CL/F, V/F and absorption rate are lognormally distributed with diagonal covariance. Concentration error is normal on the natural scale, with standard deviation sqrt(add² + (prop × concentration)²), matching nlmixr2's combined2 implementation. The four zeros therefore enter as observations, not logged zeros or invented BLQ values.

Prespecified allometry scales CL/F by (weight/70)^0.75 and V/F by weight/70. The comparator has no weight scaling. These are candidate PK descriptions, not discovered causal weight effects.

For normalized PCA R and concentration C, the direct model is R = 1/(1+C/IC50). The turnover alternative is:

    dR/dt = kout [1/(1+C/IC50) − R],   R(0) = 1.

Maximum inhibition and the Hill exponent are fixed to one. The turnover rate delays the response even when plasma concentration changes promptly. This is consistent with the distinction between concentration and the time course of effect described by [Wright, Winter and Duffull (2011)](https://doi.org/10.1111/j.1365-2125.2011.03925.x). It is a deliberately reduced biomarker model, not a model of individual clotting factors.

PK is estimated first with FOCEi; its empirical Bayes individual estimates drive the PD model. PD has random IC50 and, for turnover, random kout, with additive normalized-PCA error. This is **sequential conditional estimation**, not simultaneous PK/PD estimation. PD random effects may absorb PK estimation error. Subject resampling refits both stages, but does not remove this conditioning limitation or baseline-normalization bias.

## What the fit and diagnostics show

Typical constant-PK estimates were CL/F 0.134 L/h, V/F 7.84 L and ka 0.567 h⁻¹. Turnover estimates were IC50 1.15 mg/L and kout 0.0515 h⁻¹, corresponding to a turnover half-life of 13.5 h. These are conditional estimates from this implementation, not replacements for a clinically qualified model.

| model | AIC | warning |
| --- | --- | --- |
| direct-refined | -177.7213 | True |
| pk-refined | 900.6745 | True |
| turn-refined | -556.7973 | True |
| weight-refined | 870.8254 | True |
| weight-turn | -553.3664 | True |

Compare AIC only within the PK candidates or within the two PD candidates, where the likelihood observations are identical. AIC across PK and PD is not meaningful. The refined candidates follow a second optimizer initialized from the first fit; all original outputs and warnings are preserved. The turnover model improves conditional PD fit substantially, but PK optimization still reports failure to establish a minimum. A small objective difference between starts does not resolve that warning.

![Conditional fit and residual diagnostics](shared/warfarin-pkpd/figures/02-model-diagnostics.png)

*Figure 2. Conditional predictions use the subjects' fitted random effects; these panels are in-sample diagnostics, not validation. Time-patterned residuals, especially around 48 h, leave possible structural misspecification; a good conditional fit is not proof of a biological mechanism.*

Absorption-rate variance shrinkage and residual diagnostics are supplied in the tables. Sparse early sampling makes individual absorption weakly informed. Removing the four zero PK values and averaging the four repeated time keys were separate sensitivity refits, not changes to the primary data. Results and warnings for both remain available. No formal parameter confidence intervals are claimed from warning-bearing fits. Of 60 planned subject-bootstrap sequences, 60 produced both stages; 0 passed the explicit optimization-warning screen. Parameter variation from the other finite fits is retained only as sensitivity.

## Does limited PK information help a held-out subject?

Five deterministic folds split **subjects**, not observations. Each fold reestimates PK and both PD structures without its held-out subjects. Baseline PCA is available in every strategy. Population prediction uses typical constant PK and PD parameters; weight prediction uses the fitted allometric PK parameters and the same turnover structure reestimated after allometric PK. Neither uses test-subject postdose measurements. The direct-effect comparison belongs to the constant-PK sequence; no unestimated allometric direct-effect result is shown.

PK-informed prediction estimates individual PK random effects by MAP using only actual concentration measurements at or before 24 or 48 h, with the fitted population prior and combined measurement error. It does not use future PK or any postbaseline PCA. Subsequent PCA is scored strictly after the cutoff. Prediction integrates the turnover equation using typical PD sensitivity, because this strategy has not measured individual PD sensitivity. It is a conditional point-prediction comparison, not a claim that the MAP estimate is known truth or a fully Bayesian predictive distribution.

| cutoff | strategy | subjects | RMSE | direct_RMSE | mean_PK_measurements |
| --- | --- | --- | --- | --- | --- |
| 24 | PK-informed | 30 | 0.0887 | 0.1346 | 2.7333 |
| 24 | population | 30 | 0.0799 | 0.1061 | 0.0000 |
| 24 | weight | 30 | 0.0817 | — | 0.0000 |
| 48 | PK-informed | 29 | 0.1079 | 0.1487 | 4.6552 |
| 48 | population | 29 | 0.0978 | 0.1179 | 0.0000 |
| 48 | weight | 29 | 0.0993 | — | 0.0000 |

Errors are normalized PCA units, computed by averaging squared error within each subject, then across subjects before taking the square root. Different cutoffs contain different future windows and must not be compared as if the scored outcomes were identical. “24 h” also does not mean one sample: the actual earlier sampling varies. The 48 h subset excludes the subject with no later PCA.

| cutoff | subjects | mean_MSE_difference | low | high |
| --- | --- | --- | --- | --- |
| 24 | 30 | 0.0015 | -0.0012 | 0.0043 |
| 48 | 29 | 0.0021 | -0.0026 | 0.0064 |

Negative MSE difference favors PK information. Both paired intervals include zero. These 2,000 subject-resampling intervals condition on the existing folds and fitted training models; they do not include model-selection uncertainty and are not external-validation intervals. The numerical comparison is exploratory because some training PK fits also have optimization warnings. Nevertheless, these results do not support a confident claim that extra PK alone improves subsequent PCA prediction in this dataset.

![Subject-level held-out PCA prediction](shared/warfarin-pkpd/figures/03-held-out-predictions.png)

*Figure 3. Turnover-model RMSE and subject-bootstrap intervals. The direct model's errors are reported in the table. Population prediction is a typical-individual predictor, not integration over the full random-effect distribution.*

## A paired dose experiment, with information available at the right time

To examine the consequence for dose design, I simulated a **second single challenge after complete washout**, with invariant individual PK/PD parameters. A subject's noisy concentration at 24 h, or at both 24 and 48 h, comes from a preceding reference challenge of 1.5 mg/kg. This makes the information available before the hypothetical second dose. Applying the same postdose information to the already administered first dose would be impossible.

The experiment uses 300 virtual subjects sharing the same random effects across strategies. Weight is sampled from the observed distribution. The comparator's fixed dose is calibrated to a typical individual's normalized PCA nadir of 0.25; weight scaling and PK-informed MAP estimates are alternatives. A separate oracle knows all true PK and PD parameters. It is an ideal upper bound, not a usable strategy. The acceptance band 0.20–0.30 is **an arbitrary algorithm test**, with no clinical therapeutic interpretation. Every strategy is constrained to the observed dose range of 60–153 mg.

| strategy | n | nadir_median | nadir_SD | target_fraction | dose_bound_fraction |
| --- | --- | --- | --- | --- | --- |
| PK24 | 300 | 0.2508 | 0.0832 | 0.4600 | 0.1667 |
| PK24+48 | 300 | 0.2495 | 0.0818 | 0.4933 | 0.2133 |
| fixed | 300 | 0.2561 | 0.0858 | 0.4667 | 0.0000 |
| oracle | 300 | 0.2500 | 0.0408 | 0.7800 | 0.4633 |
| weight | 300 | 0.2528 | 0.0866 | 0.4667 | 0.2500 |

![Paired virtual repeat-challenge comparison](shared/warfarin-pkpd/figures/04-paired-dose-scenarios.png)

*Figure 4. Simulated normalized PCA nadirs and arbitrary target attainment. These are model-generated outcomes, not observed treatment effects.*

A further 20 evenly selected finite subject-bootstrap parameter sets repeat the experiment in 150 paired virtual subjects each, with the same seeds. They include estimation variation and PK measurement noise, but remain warning-dependent sensitivity rather than a formal probability of clinical success. Changing from constant PK to fitted allometry also changes the relation between weight and exposure:

| PK_structure | strategy | target_fraction | nadir_SD | dose_bound_fraction |
| --- | --- | --- | --- | --- |
| constant | PK24 | 0.4600 | 0.0832 | 0.1667 |
| constant | PK24+48 | 0.4933 | 0.0818 | 0.2133 |
| constant | fixed | 0.4667 | 0.0858 | 0.0000 |
| constant | oracle | 0.7800 | 0.0408 | 0.4633 |
| constant | weight | 0.4667 | 0.0866 | 0.2500 |
| allometry | PK24 | 0.4367 | 0.0833 | 0.2333 |
| allometry | PK24+48 | 0.4633 | 0.0820 | 0.2567 |
| allometry | fixed | 0.4167 | 0.0893 | 0.0000 |
| allometry | oracle | 0.7700 | 0.0418 | 0.5233 |
| allometry | weight | 0.4633 | 0.0838 | 0.2500 |

A weight-based strategy cannot be judged solely under a truth model that assumes no weight effect. Both structures are therefore retained. For the allometric sensitivity, turnover PD was reestimated after allometric PK; this remains sequential conditional estimation, not a joint likelihood. There is no observed repeated challenge to validate parameter stability, washout, the counterfactual dose responses or absence of interoccasion variability. Dose bounds also limit what even the oracle can attain.

## Numerical checks and uncertainty

Independent Python concentration formulas and fine-grid turnover integration were checked against R's individual predictions:

| check | max_absolute_error |
| --- | --- |
| pk-refined | 6.75e-14 |
| turn-refined | 2.81e-05 |
| direct-refined | 1.56e-06 |

Agreement verifies implementation, not biology or clinical validity. The in-sample predictive check uses 500 subject-level random-effect draws per original subject at actual sampling times, then adds PD residual error. Its bands include IIV and residual error at fixed fitted parameters; they are not parameter confidence bands or held-out coverage.

![In-sample predictive check](shared/warfarin-pkpd/figures/05-predictive-check.png)

*Figure 5. Pointwise predictive limits summarized across subjects, with normalized observations. The exact subject/time quantiles remain in the private analysis archive; aggregate review files accompany the article.*

## What can be concluded?

This measured-data example supports a limited methodological conclusion: representing effect delay matters, while additional PK measurements need not resolve response heterogeneity. The held-out comparison gives no consistent evidence of improved PCA prediction from PK alone. It does not prove PK monitoring has no value in other settings.

The next discriminating experiment would measure information about PD sensitivity, assess baseline measurement uncertainty and test prediction in an independent cohort or repeat occasion. It should be motivated by a clearly defined future decision rather than by collecting more concentrations automatically. No comparison here justifies a patient dose, chronic regimen, INR target or bleeding-risk claim. A simultaneous PK/PD likelihood, better characterized assay error and robust optimization would be necessary before stronger quantitative qualification.

## Sources and reproducibility

- [nlmixr2data warfarin reference](https://nlmixr2.github.io/nlmixr2data/reference/warfarin.html), pinned source commit `f2cfb01ade88d4d30e66f56b19efce2a2c6e26bd`; acquisition records distinguish documented and actual row counts.
- [University of Auckland original and simulated datasets](https://holford.fmhs.auckland.ac.nz/research/nlmixr/), used to establish which file contains the original observations.
- [O’Reilly, Aggeler and Leong, 1963](https://doi.org/10.1172/JCI104839), *Studies of the coumarin anticoagulant drugs: The pharmacodynamics of warfarin in man*. Historical provenance cited by the data distributor; record-level mapping to the original publications is unavailable.
- [Wright, Winter and Duffull, 2011](https://doi.org/10.1111/j.1365-2125.2011.03925.x), *Understanding the time course of pharmacological effect: a PKPD approach*.

See [the executed review notebook](shared/warfarin-pkpd/analysis.ipynb), [reproduction instructions](shared/warfarin-pkpd/README.md), and [the downloadable reproduction bundle](shared/warfarin-pkpd/warfarin-pkpd-companion.zip). The notebook executes aggregate checks and figure display; full estimation is a documented separate command, not silently rerun when opening the notebook. Individual observation files, fitted RDS objects and private planning materials are not distributed. 


[Download the companion: code, aggregate results and executed notebook](shared/warfarin-pkpd/warfarin-pkpd-companion.zip)
