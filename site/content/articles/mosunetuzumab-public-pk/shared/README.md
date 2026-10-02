# Mosunetuzumab: public-model reconstruction

Independent research/learning simulation, not a validated clinical decision tool. No patient-level or proprietary data are used. Figures and tables are original calculations, not reproductions of published artwork.

## Run

Python 3.12. Download `run_analysis.py` and `requirements.txt` into the same directory, then run:

```sh
python -m pip install -r requirements.txt
python run_analysis.py
```

Outputs: `results/*.csv`, `results/run_metadata.json`, and `figures/*.{png,svg}`. Seed 20261002; 2,000 paired virtual patients. Reference covariates are fixed; lognormal IIV follows the published final Omega, without residual observation error. Fixed-effect sensitivity changes one marginal CI bound at a time, not a joint parameter uncertainty distribution.

## Model and events

Parameter order: CLbase, V1, CLss, HLtrans, V2, Q. Time-varying clearance uses time since first dose, not time since latest infusion. Concentration mg/L equals microgram/mL. Infusion times: first three doses 4 hours, subsequent doses 2 hours.

Reference times/doses: 0/1, 7/2, 14/60, 21/60, 42/30, 63/30 (day/mg). When both step-up intervals change to g, the first 60 mg is at 2g, second 60 mg at 2g+7, first 30 mg at 2g+28, followed every 21 days. AUC0-42 uses the fixed calendar window and excludes the infusion beginning exactly at day42. Consequently interval changes also alter large-dose timing and maintenance-dose inclusion.

CRS: published Group B ASTCT Grade >=2 logistic model uses maximum CD20 occupancy during days0-42, percent scale0-100. It is an association model, not a mechanistic history-dependent model. Residual rituximab and obinutuzumab decay with 24- and 28-day half-lives. Binding-only and binding-plus-baseline-CL-covariate assumptions are reported separately. For no residual drug, the CL covariate uses its reference500ng/mL; this is an explicit scenario convention, not reconstruction of all original missing-data rules. Results cannot qualify altered-regimen CRS incidence predictions.

## Sources

- Bender et al. 2024, DOI10.1111/cts.13825, supplementary equation1, TableS2, NONMEM implementation.
- Li et al. 2025, DOI10.1002/cpt.3445, supplementary TablesS3 andS12.
- US IV LUNSUMIO label: DailyMed and FDA2025label.

`results/source_manifest.json` records EuropePMC public source URLs and SHA256 hashes of retrieved XML and supplementary ZIPs. The script embeds only the numeric model inputs; downloading copyrighted source documents is not required to run it. Published geometric-mean exposure summaries are benchmarks with a different estimand from the typical-parameter trajectory, not independent clinical validation data.
