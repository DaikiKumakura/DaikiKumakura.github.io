# Immune outcome validation

Status: published research companion, 2026-10-04.

Python 3.11+ with numpy, pandas, scipy, matplotlib; R 4.5.1 with Biobase 2.70.0. Notebook requires nbformat, nbclient, ipykernel, jupyter_client, Markdown. Exact installed Python versions are recorded in environment.json.

Run in a new working copy to preserve the original frozen artifact:

```text
python download_pinned.py
Rscript inspect.R
python audit.py
python analyze.py
python render_figures.py
python validate.py
```

Download checks every SHA against sources.json and aborts if source bytes change. inspect.R extracts serialized attributes from the legacy CountDataSet without running third-party package code or substituting an unverified DESeq transformation. Biobase is needed to deserialize metadata. Raw files and patient-level derived features remain local and are excluded from the release. Counts are length-normalized TPM, not DESeq-normalized values.

analyze.py follows analysis-plan.md, writes model-frozen.json before external scoring, then verifies its unchanged hash. Re-running fits does not retroactively make the plan prospective or external outcomes blinded. Keep old artifacts if changing a model; use a new dataset for subsequent confirmatory validation. CV fold records contain source patient identifiers and stay private. Results and figures are aggregate only.

Source limitations: pinned third-party development mirror not compared byte-for-byte to unavailable publisher distribution; source cohorts cannot establish no participant overlap; biopsy timing not verified per person. Creative Commons attribution is recorded for the development bundle, and original authors Nickles/Bourgon and both papers are credited. GEO public availability does not waive all downstream reuse obligations. No raw participant records are redistributed.
