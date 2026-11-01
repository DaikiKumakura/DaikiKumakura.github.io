# Reproduction

Run `python analysis.py` with Python 3.12 or later. Only the standard library is used; there is no random sampling, model inference, or corpus download.

The two input counts, 10,972 matched measurements and 8,566 exact-value agreements, are reported in the "Datawell vs CRO data" section of Anand and Goel, *The Bitter Lesson for Biology* (2026-10-18), https://bindwell.com/posts/the-bitter-lesson-for-biology . They are transcribed aggregate counts, not independently verified raw records.

The script exports `results/summary.json` and `results/logical-cases.csv`. The latter contains possible assignments of correctness under a single adjudicated source value per matched record. These are logical examples consistent with the aggregate agreement count, not measurements of Datawell or CRO correctness. Extraction errors can take more than two distinct values, so both extractors can be wrong even where they disagree.

Expected outputs: 2,406 disagreements; agreement 0.7807145461173898; disagreement 0.21928545388261028; crossover multiplier 3.5602660016625105. Inspect the generated JSON for unrounded values. The article reports 78.1%, 21.9%, and 3.56.

The counts do not establish extraction precision, recall, source-document truth, biological reproducibility, or relative predictive performance outside the selected validation stratum. No third-party extraction records, rubrics, or article text are redistributed.
