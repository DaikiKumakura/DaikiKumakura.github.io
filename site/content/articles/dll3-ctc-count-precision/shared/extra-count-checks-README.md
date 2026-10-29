# Additional count-precision calculations

Place `extra-count-checks.py` beside `dll3-ctc-count-precision-analysis.zip`, or pass the archive with `--archive PATH`. Install numpy and scipy, then run:

```sh
python extra-count-checks.py
```

The script reads the archive without changing it. It prints the aggregate-count reconciliation, conditional interval crossings with alternative interval methods, healthy-control count conversion, effective sample sizes, and fixed-count mismatch boundaries. These are additional calculations for the article, not newly measured patient records. Original analysis and source provenance are in the archive.
