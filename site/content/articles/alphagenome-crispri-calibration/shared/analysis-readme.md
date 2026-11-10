# Reproducing the AlphaGenome CRISPRi calibration analysis

This is a reanalysis of published prediction tables, not a rerun of genomic-model inference. Original technical comparison: https://genomicsxai.github.io/blogs/2026-007/ . Input repository commit: b4917f5b1a5ccdac8800d00ed31f65cfcb483093.

## Run

Use Python 3.12 with numpy 2.2.6, pandas 2.2.2, scipy 1.14.0 and matplotlib 3.9.1. Install these packages in your own environment. Extract the archive, then run `python fetch_inputs.py` followed by `python analysis.py`. Download requires internet access. Eight CSVs are fetched from fixed raw GitHub URLs and checked by SHA256. No downloaded code is executed. Original data are not bundled. The input manifest is named source-manifest.json in the downloadable archive.

Outputs: results.json, two pair-level OOF CSVs, and PNG/SVG versions of two figures. Pair tables are generated locally, not included in this archive. Bootstrap uses 2,000 gene-cluster draws, refits all leave-one-gene-out calibrations per draw, and uses seeds 20261110/20261111. Runtime depends on CPU/BLAS.

## Interpretation and estimand

Pair-weighted prediction error among selected positive K562 enhancer–gene pairs covered by all four models. This cannot estimate discovery success or false-positive rates in an unselected candidate population. Missing model coverage is excluded, not imputed. Fulco common set: 62 pairs/20 genes; Gasperini: 352/256. Check data-quality.json for source coverage and key validation.

Calibration fits y=a+b*p on other genes and predicts the excluded gene. The mean baseline also excludes that gene. No clipping. These are supervised corrections requiring experimental effects, not zero-shot gains. The held-out genes are excluded from correction training, not verified absent from genomic pretraining. Bootstrap resamples genes, removes all copies of the held-out gene when refitting, and pairs draws across methods. Component-held-out and native-AlphaGenome-coverage results are sensitivity checks. Reported intervals are percentile 95% intervals and not measurement-error models. Exploratory analysis, not preregistered.

RMSE and bias are stored in fractional units; multiply by 100 for percentage points. CSV y_delta already means fractional decrease. Original inference contrasts 2 kb dinucleotide shuffling with original sequence, which differs from CRISPRi repression.

The independent reanalysis code and original figures are licensed under MIT (LICENSE). Source datasets retain their original terms and attribution; consult the source repository and primary studies. No third-party code is redistributed in this package.
