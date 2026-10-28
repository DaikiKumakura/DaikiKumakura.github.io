How would reducing divarasib from 400 to 200 mg change response in lung and colorectal cancer? I combined phase I dose-group responses with 400-mg pharmacokinetics and compared doses in 4,096 virtual patients. This is an exploratory calculation from two grouped observations, not an individual-level exposure–response analysis.

The phase III Krascendo 1 study compared divarasib with sotorasib or adagrasib in 338 previously treated patients with lung cancer. Improvements in progression-free and overall survival had been announced in July 2026. This analysis uses that historical announcement and phase I material rather than reassessing detailed phase III results. I did not read the original phase I full text; PK and response inputs came from secondary reporting and reconstruction of percentages ([1](#ref-1)).

The median predicted 400-minus-200-mg response difference was 6 percentage points in lung cancer, with a wide 95% interval of −11 to 23, and 24 points (3–43) in colorectal cancer. These are conditional results from small nonrandomized groups and an assumed lower-dose mixture, not a basis for prescribing or deciding whether to reduce treatment.

## The dose-comparison question

The question of interest is the predicted response change between 400 and 200 mg and whether it differs by cancer type. The context of use is to assess what public data support before dose-optimization study design, not regulatory or prescribing decisions.

KRAS G12C is a KRAS protein mutation targeted in non-small cell lung cancer (NSCLC), colorectal cancer (CRC) and other settings. Dose selection has been contentious for this inhibitor class: sotorasib required a 960-versus-240-mg comparison ([related analysis](sotorasib-dose-comparison-en.html)) ([2](#ref-2)). Divarasib phase I tested 50–400 mg and selected 400 mg once daily.

## Data used

Table 1. Published aggregate inputs. AUC is area under the concentration–time curve; Cmax is maximum concentration; SD is standard deviation.

| Item | Value | Source |
|---|---|---|
| Steady-state AUC over 0–24 h at 400 mg | Mean 9,130 ng·h/mL (SD 3,160), 76 patients | Phase I paper through reporting |
| Steady-state Cmax at 400 mg | Mean 657 ng/mL (SD 185) | Same |
| Half-life after a single 400-mg dose | 17.6 h (SD 2.7), 4 patients | Same |
| Median time to maximum concentration | 2.0 h | Same |
| Confirmed NSCLC responses | All doses 31/58; 400 mg 22/39; below 400 mg 9/19 | Same; counts reconstructed from percentages |
| Confirmed CRC responses | All doses 16/55; 400 mg 14/39; below 400 mg 2/16 | Same |
| NSCLC dose counts at long-term follow-up | 400 mg: 44; 200 mg: 10; 100 mg: 5; 50 mg: 6 | PMC12527784, April 2024 cutoff |
| Safety across doses | Nausea 74%, diarrhea 61%, vomiting 58% (mostly grade 1–2); dose reduction 14% | Phase I through reporting |

The original below-400-mg dose composition was unavailable. I assumed the later NSCLC mixture, 50:100:200 mg = 6:5:10, for both cancers. That follow-up has a different cutoff from the NEJM report ([3](#ref-3)). Sensitivities place everyone at 200 mg or everyone at 50 mg.

## Model and estimation

The oral one-compartment PK model uses first-order absorption and elimination. Apparent clearance is CL/F = 400 mg divided by 9,130 ng·h/mL = 43.8 L/h, assuming dose proportionality, which I did not verify in primary material for 50–400 mg. Individual AUC is lognormal with a 35% coefficient of variation, approximated from SD/mean.

Half-life and time to peak imply a typical Cmax of 549 ng/mL, 16% below the reported mean. Predicted accumulation is 1.64 versus the reported 1.4. Thus the concentration shape is approximate. Its mismatch does not directly enter an AUC-only response model, but whether AUC adequately represents efficacy-driving exposure is untested.

Response probability is logistic in steady-state AUC:

$$\mathrm{logit}\,P(\text{response})=a+b\,\ln\frac{AUC}{AUC_{\text{ref}}}$$

Here AUCref is the mean AUC at 400 mg; b = 0 means a constant response probability regardless of exposure. 

For each dose group, predicted response is averaged over virtual-patient AUC variability. A binomial likelihood for the two observed groups, 400 mg and below 400 mg, yields a posterior over a fine grid of a and b under a flat prior. Two groups and two parameters leave no independent assessment of goodness of fit. The slope largely reexpresses the observed group difference through the assumed dose mixture.

## Predicted responses

![Divarasib exposure–response fits and dose comparisons](shared/divarasib-dose/figures/divarasib_er.png)

Figure 1. A: typical steady-state concentration profiles assuming dose proportionality. B: response versus dose, with posterior medians and 95% credible intervals, based on 58 NSCLC and 55 CRC patients. Circles show observed 400-mg responses (39 patients each); squares show below-400-mg responses (19 NSCLC, 16 CRC) at the assumed mean dose, 133 mg. A mixed-dose response is not a single point on the dose curve.

Table 2. Conditional posterior summaries. Intervals are 95% credible intervals.

| | NSCLC | CRC |
|---|---|---|
| Slope b (95% interval) | 0.35 (−0.63–1.50) | 2.15 (0.23–7.10) |
| Posterior probability of nonpositive slope | 26% | 0.8% |
| Predicted response at 200 mg | 51% (35–66%) | 13% (3–32%) |
| Predicted response at 300 mg | 54% | 25% |
| Predicted response at 400 mg | 57% (41–72%) | 37% (23–54%) |
| Difference, 400 minus 200 mg | 6 points (−11–23) | 24 points (3–43) |
| Posterior probability of a difference above 10 points | 29% | 88% |

The CRC slope upper bound, 7.1, approaches the grid limit of 8 and is sensitive to the flat prior. Its low-dose evidence comprises only two responses among sixteen patients.

Changing dose composition changes the strength of inference. In NSCLC, placing all lower-dose patients at 200 mg gives a median difference of 11 points (−18–40), versus 3 points (−6–12) if all were at 50 mg. In CRC, all assumptions give a positive median difference; the all-50-mg scenario gives 11 points with an interval of 0–24.

### Sample size under the assumed effect

If posterior-median NSCLC responses, 57% at 400 mg and 51% at 200 mg, were the true values, approximately 1,200 patients per arm would be needed for a two-sided 5% superiority test with 80% power. Demonstrating noninferiority with a 10-point margin, a true difference of approximately 6 points and one-sided 2.5% testing requires approximately 2,100 per arm. These assumptions produce a large trial for a small response difference. Tolerability and dose-intensity study sizes were not calculated. An efficacy sample-size calculation cannot establish an adequate safety-study size.

## Comparison with related evidence

The public sotorasib 960-versus-240-mg comparison in NSCLC gave a response difference of +7.8 points (95% interval −4.3 to +19.8), whereas grade ≥3 treatment-related adverse events were 16 points more frequent at 960 mg ([related analysis](sotorasib-dose-comparison-en.html)). A weakly identified divarasib response slope is compatible with that experience, but the other drug's toxicity difference cannot quantify the benefit of reducing divarasib.

KRAS G12C inhibitor monotherapy is less active in CRC than NSCLC, and combinations with EGFR antibodies are prominent in development, including divarasib with cetuximab. The positive CRC slope is compatible with incomplete target suppression under monotherapy, but early escalation patients can differ from 400-mg patients. This is not evidence that exposure itself causes the observed difference.

## Scope of the grouped comparison

These grouped observations do not clearly identify NSCLC dose dependence. CRC monotherapy may have a positive relationship, but it remains distinct from a causal exposure effect. Small NSCLC response differences would be difficult to distinguish at modest trial sizes under the stated assumptions.

Dose-specific safety is missing: pooled nausea and diarrhea rates cannot predict how much toxicity changes with dose. Progression-free survival, response duration and brain-metastasis outcomes are outside this calculation. Nonrandomized escalation groups may differ in prognostic features.

Divarasib's covalent KRAS G12C inhibition is described in the discovery study, but target binding and downstream response are not modeled here ([4](#ref-4)).

## Limitations

I did not read the original phase I full text. PK and response values depend on reporting and reconstructed percentages, and the lower-dose mixture is assumed. PK is dose proportional by assumption. With two dose groups, the prior, grid limits and mixture substantially influence the slope. No dose-specific safety model supports a reduction recommendation.

## Data and code availability

[Code, inputs and results](shared/divarasib-dose/divarasib-dose.zip) regenerate the table and figure using `python analysis/run_analysis.py` with a fixed random seed.

## References {#article-references}

1. <span id="ref-1"></span>Sacher A, LoRusso P, Patel MR, Miller WH, Garralda E, Forster MD, et al. Single-agent divarasib (GDC-6036) in solid tumors with a KRAS G12C mutation. N Engl J Med. 2023;389(8):710–721. [doi:10.1056/NEJMoa2303810](https://doi.org/10.1056/NEJMoa2303810). Full text not read; numerical inputs were taken from secondary reporting and reconstructed percentages. The original reporting URLs were not retained in the analysis record.
2. <span id="ref-2"></span>Kumakura D. How far does a dose-comparison trial support dose selection? Arm-level data for sotorasib 960 mg and 240 mg. [Related analysis](sotorasib-dose-comparison-en.html).
3. <span id="ref-3"></span>Sacher AG, Miller WH Jr, Patel MR, Paz-Ares L, Santoro A, Ahn MJ, et al. Single-agent divarasib in patients with KRAS G12C-positive non-small cell lung cancer: long-term follow-up of a phase I study. J Clin Oncol. 2025;43(30):3249–3253. [doi:10.1200/JCO-25-00040](https://doi.org/10.1200/JCO-25-00040); [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12527784/).
4. <span id="ref-4"></span>Endres NF, Do S, Mroue R, Terrett JA, Saabye M, Oh A, et al. Discovery and characterization of divarasib (GDC-6036), a potent covalent inhibitor of KRAS G12C. J Med Chem. 2026;69(5):5147–5165. [doi:10.1021/acs.jmedchem.5c02272](https://doi.org/10.1021/acs.jmedchem.5c02272).
