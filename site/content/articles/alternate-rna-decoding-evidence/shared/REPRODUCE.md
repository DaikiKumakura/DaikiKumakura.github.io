# Reproduce the supplementary-table audit

This original analysis audits published tables. It does not reanalyse mass spectra, matched genomic data, or protein function. The source XLSX files are not redistributed.

## Environment and execution

Python 3.12.4 and openpyxl 3.1.5 were used. All other dependencies are in the Python standard library. No random number generator is used.

```bash
python -m pip install openpyxl==3.1.5
python fetch_supplement.py
python analysis.py
```

Run from the directory containing the scripts. The fetch script obtains selected members from the publisher's public supplementary ZIP using HTTP byte ranges. It requires range support and refuses a full 633 MB download. ZIP size and CRC are validated; the SHA-256 hashes of the retrieved files are recorded in `sources/download-manifest.json`.

The sources are Supplementary Data 2, 3 and 8 linked by the authors at https://github.com/SlavovLab/decode/blob/main/docs/mass-spec/data.md. The publisher ZIP is https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-026-10678-2/MediaObjects/41586_2026_10678_MOESM3_ESM.zip. Keep the source files unchanged.

Outputs are `results/table-counts.csv`, `results/dataset-counts.csv` and `results/summary.json`. The included outputs were generated from the file hashes listed in summary.json. Re-running with a different Python version changes the recorded version string; numerical counts should remain the same when source hashes agree.

## Definitions

The global sequence-pair key is `(SAAP, BP)`. A dataset-level pair adds `Dataset`. The Table 3/8 observation key also includes `TMT/Tissue` and `Digest`. These are not patient identifiers or independent biological-replicate counts. Source Table 2 has 10,086 rows and 8,746 global pairs; Table 3 has 19,480 rows and 8,944 pairs; Table 8 has 5,873 rows and 1,955 pairs.

All Table 8 observation keys occur in Table 3. Only 1,899 Table 8 global pairs also occur in Table 2, with 56 pairs found only in Table 8. The latter difference is described, not attributed to an identified upstream cause. The code does not reapply the localization filter: four Table 8 exported probabilities equal 0.900, and unrounded values are unavailable.

No source rows are imputed, reassigned or corrected. Peptide counts are not treated as proof of altered translation or function. The publisher-provided data may be updated; a changed hash is a changed input version and must be investigated rather than silently accepted as identical.
