To ask whether T cells lie near tumour cells, a coordinate and a cell-type label must refer to the same cell. Zhang and colleagues studied 105 primary and lymph node specimens from small cell lung cancer using CosMx ([1](#ref-1)). The released coordinates and annotations looked like a route to an alternative neighbourhood measure. I first counted which cells could be joined from the available files.

## Unique within a file

The pinned author repository contains two coordinate RDS files and a CSV of cell annotations with slide labels ([2](#ref-2)). Each coordinate file has `cell_id, x, y`; the annotation table has `slide, cell_id, cell_type`. The coordinate files contain 426,822 and 314,447 rows, respectively. Cell IDs are unique within each file, but 279,603 occur in both files. The slide and cell-ID pair is unique in the annotation table. With no explicit slide column in the coordinate files, these two kinds of uniqueness do not determine the join.

Table 1 gives the match count for each candidate.

**Table 1.** Candidate matches between annotated IDs and the two coordinate files.

| Annotation and candidate ID | Annotation rows | Matched in coordinate file 1 | Matched in coordinate file 2 |
| --- | ---: | ---: | ---: |
| Slide1, unmodified | 360,169 | 360,169 | 234,360 |
| Slide2, unmodified | 244,061 | 0 | 0 |
| Slide2, terminal `_2` replaced by `_1` | 244,061 | 215,386 | 244,061 |

The bottom-right count makes coordinate file 2 a plausible match for Slide2 after suffix replacement. Yet 215,386 of those candidate IDs also occur in file 1. The match count suggests a candidate and leaves the meaning of the suffix and the provenance of the coordinates unresolved.

## Labels collide when the slide is discarded

I matched the normalized Slide2 IDs against the Slide1 annotations without using either coordinate file. There were 180,027 matches, with different labels in 115,671. Restricting the comparison to the 116,649 matches where both labels were other than `Undefined` left 57,553 differences (49.34%). These are candidate mismatches from a slide-blind join. They do not count errors in the published study.

The data dictionary distinguishes local and global pixel coordinates from the field-of-view locations in mm ([2](#ref-2)). The materials I checked did not establish which transform produced the short `x,y` columns in the released RDS files. Without confirmed coverage and a patient-to-specimen map, a cell with no observed T cell nearby cannot be distinguished reliably from one near an unobserved boundary. The audit gives a concrete reason to verify file provenance and slide-specific IDs before calculating distances in µm or ranking patients by proximity. It does not re-evaluate the reported spatial effects or DLL3 drug activity.

## Data and code availability

The [companion ZIP](shared/sclc-spatial-cell-id-collisions/companion.zip) contains the pinned source locations, R audit and aggregate tables. Download the original files from the source.

## References

1. <a id="ref-1"></a> Zhang Z, Wu D, Chen Z, Dai M, Yang F, Wang J, et al. Single-cell spatial transcriptomics reveals tumor microenvironment heterogeneity in primary and lymph node-metastatic small cell lung cancer. Cell Rep Med. 2026;7(4):102713. [doi:10.1016/j.xcrm.2026.102713](https://doi.org/10.1016/j.xcrm.2026.102713).
2. <a id="ref-2"></a> Zhang Z, et al. SCLC-LNM-SMI. [Coordinate and annotation repository at commit 1c6ed2c](https://github.com/ZhoulabCPH/SCLC-LNM-SMI/tree/1c6ed2c985a79ee55371865f3ccc9a10f9d64581) · [SMI data file README](https://github.com/ZhoulabCPH/SCLC-LNM-SMI/blob/1c6ed2c985a79ee55371865f3ccc9a10f9d64581/SMI%20Data%20File%20information/SMI%20Data%20File%20ReadMe.pdf).
