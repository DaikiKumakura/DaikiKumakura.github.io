A peptide contains an amino acid that was not predicted. Does that establish that the cell changed how it reads the genetic code? Counting more unexpected sequences is only part of the problem. Their origin and the reason they persist must also be distinguished.

A thread by Nikolai Slavov leads from a book discussion to research on peptides that depart from standard translation predictions ([1](#ref-1)). The Nature study by Tsour et al. reports many amino acid substitutions in existing data that include more than 1,000 human samples ([2](#ref-2)). Here I examine that claim through the published supplementary tables. Recounting them reproduced the numbers 8,746 and 1,955. However, dividing those two numbers did not give a valid fraction surviving stricter validation.

## Scope and sources

On November 1, 2026, I examined methods, validation descriptions and figure legends accessible through the final article's search index, the authors' public code and data documentation, and publisher-hosted Supplementary Data 2, 3 and 8. I did not read every page of the publisher's full text or reanalyse mass spectra, patient-level DNA and RNA, or functional experiments.

Below, I call those supplementary datasets Table 2, Table 3 and Table 8, following the authors' numbering. Only the three required files were retrieved from the 633 MB public ZIP, with their sizes and CRCs checked against the archive. The original Excel files were left unchanged. Column definitions were examined before aggregation ([3](#ref-3)). The original analysis here audits rows, sequence pairs and correspondence between tables. It does not independently validate the substitutions.

## From a mass difference to a sequence

The study calls a substituted amino acid peptide an SAAP and its corresponding canonical sequence a base peptide, or BP. The starting observation is a mass-spectrometry (MS) signal with a mass different from that of a canonical peptide. An amino acid substitution is not the only possible explanation for such a difference.

The authors removed mass shifts consistent with known post-translational or chemical modifications, searched again against databases augmented with candidate sequences, and examined fragments supporting the substitution site, retention times and other evidence. They controlled false discovery rate (FDR) for SAAPs rather than pooling them with canonical peptides. [Figure 1 of the original article](https://www.nature.com/articles/s41586-026-10678-2#Fig1) shows this validation process ([2](#ref-2)). These checks bring different information to bear on the signals. They are not equivalent to replication in an independent patient cohort.

Support for peptide identification also differs from confidence in a unique substitution position. The article acknowledges that unknown combinations of modifications cannot be completely excluded where the position is not confidently localized ([2](#ref-2)). Reducing detection to a single pass-or-fail label loses that distinction.

## What the numbers 8,746 and 1,955 count

One row of Table 2 represents an SAAP–BP sequence pair within a dataset. The same pair appearing in another dataset contributes another row. Tables 3 and 8 contain finer observations associated with a measurement set using tandem mass tag (TMT) chemical labels, or with a healthy-tissue sample ([3](#ref-3)). Their row counts cannot be read as patient numbers or independent replicate counts.

For the recount, I used the two sequence strings in `SAAP` and `BP` as the identity key, without imputing blanks or collapsing by gene name. Table 1 gives the results.

Table 1. Recount of rows and sequence pairs in the public supplementary tables

| Published table | Rows | Distinct sequence pairs within datasets | Distinct sequence pairs across datasets |
| --- | ---: | ---: | ---: |
| Table 2 | 10,086 | 10,086 | 8,746 |
| Table 3 | 19,480 | 10,285 | 8,944 |
| Table 8 | 5,873 | 2,503 | 1,955 |

A sequence pair means an SAAP–BP combination. Position, protein, gene and patient were not added to the identity key. Reproducing two headline counts does not establish that they describe the input and output of one filtering step.

In fact, Tables 2 and 8 shared 1,899 sequence pairs. Table 8 contained 56 pairs absent from Table 2, corresponding to 81 healthy-tissue observations. This audit did not determine which generation step produced that difference. It is not a finding that the paper is erroneous. It does establish that these two exported tables cannot be treated as a simple nested set under the stated sequence-pair key.

The authors identify Table 3, rather than Table 2, as the parent of Table 8 ([3](#ref-3)). Using the five columns `Dataset`, `SAAP`, `BP`, `TMT/Tissue` and `Digest`, I found every Table 8 observation key in Table 3. For that comparison, row retention was 5,873/19,480, or 30.1%, whereas sequence-pair retention was 1,955/8,944, or 21.9%. Even for the same two tables, the percentage changes with the counted unit.

I used Table 8 as the authors' exported set, without reapplying a localization filter. Although the article describes a localization probability greater than 0.9, four exported rows show exactly 0.900. Values before rounding were unavailable, so I did not move those observations across the threshold and redefine the published set. The 1,955 pairs constitute the authors' high-localization-confidence set. They do not classify every other pair as a false positive.

## Where the sequence difference arose

Finding a sequence different from a canonical translation prediction does not immediately identify translation as its origin. DNA variation, changes to the RNA sequence, translational misreading, modifications and identification ambiguity need to be considered. A single spreadsheet cannot resolve all those questions simultaneously.

The authors' pipeline includes construction of sample-specific protein databases from matched RNA-seq. It can also operate without matched RNA-seq, but its README explicitly notes lower confidence that the resulting substitutions are not encoded in the genome ([4](#ref-4)). Some patient-level DNA and RNA used in the article require application-based access. I did not repeat the authors' sequence-matching analyses ([2](#ref-2)).

Moran's blog and its comments also discuss what was observed and how to distinguish transcriptional from translational origins ([5](#ref-5)). The comments contain conflicting interpretations, so the existence of that debate is not itself a refutation. The relevant issue is which observation narrows which alternative explanation.

## Abundant products need not be frequently synthesized

Abundance creates another interpretive gap. A substituted product can persist at high abundance without being synthesized at a high relative rate.

Let the substituted and canonical protein amounts be \(P_s,P_b\), their synthesis rates \(v_s,v_b\), and first-order degradation-rate constants \(k_s,k_b\). If the two independent pools are at steady state, \(P=v/k\), giving

\[
\frac{P_s}{P_b}=\frac{v_s}{v_b}\frac{k_b}{k_s}.
\]

A large abundance ratio does not uniquely determine the synthesis and degradation ratios. This is a simple mass-balance relation, not a model fitted to the study's data. The original article also examines protein stability as a contributor to substituted-product abundance ([2](#ref-2)).

Moreover, turning a relative MS peptide signal into a molecule-count ratio for intact proteins requires assumptions about measurement response and the proteins from which the peptides originate. An SAAP–BP ratio cannot simply be inverted into the probability that the translation machinery reads a particular codon differently.

## From detected sequences to drug-discovery candidates

The study opens a route to peptides that cannot be exhaustively listed from reference sequences alone. Connecting those observations to tumour function or therapeutic targets requires additional evidence. Enrichment in a tumour does not establish a causal role in tumour growth. A peptide detected in a whole-cell proteome is also not identical to an antigen presented on major histocompatibility complex molecules and recognized by T cells.

This recount did not determine whether individual sequence identifications are correct or functional. It reproduced two published totals and established that they cannot be interpreted as one filtering pass rate. Even with the correct parent table, the retained percentage depended on the observation unit. What remains is evidence connecting identification, origin, abundance and function. Unexpected sequences are worth finding. Their counted unit must not change unnoticed when the argument moves toward translational regulation or a therapeutic target.

## Data and code availability

The [public-table retrieval script](shared/alternate-rna-decoding-evidence/fetch_supplement.py), [aggregation script](shared/alternate-rna-decoding-evidence/analysis.py), [Table 1 CSV](shared/alternate-rna-decoding-evidence/results/table-counts.csv), [dataset-level counts](shared/alternate-rna-decoding-evidence/results/dataset-counts.csv), [results and input hashes](shared/alternate-rna-decoding-evidence/results/summary.json), and [reproduction instructions](shared/alternate-rna-decoding-evidence/REPRODUCE.md) are available. Original XLSX files are not redistributed; they are retrieved from the publisher's public archive. The analysis ran with Python 3.12.4 and openpyxl 3.1.5. No random numbers were used.

## References

1. <span id="ref-1"></span>Slavov N [@slavov_n]. Thread linking genome metaphors to RNA decoding research [X post; editorial description]. 2026 Oct 18 [cited 2026 Nov 1]. Available from: [https://x.com/slavov_n/status/2111826378257793117](https://x.com/slavov_n/status/2111826378257793117).
2. <span id="ref-2"></span>Tsour S, Machné R, Leduc A, Widmer S, Koo E, Guez J, et al. Alternate RNA decoding results in stable and abundant proteins in mammals. Nature. 2026;656:506–515. [https://doi.org/10.1038/s41586-026-10678-2](https://doi.org/10.1038/s41586-026-10678-2).
3. <span id="ref-3"></span>Slavov Laboratory. Download alternate RNA decoding results: supplementary data descriptions [Internet]. Decode; [cited 2026 Nov 1]. [Author documentation](https://github.com/SlavovLab/decode/blob/main/docs/mass-spec/data.md). [Publisher supplementary data ZIP](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-026-10678-2/MediaObjects/41586_2026_10678_MOESM3_ESM.zip).
4. <span id="ref-4"></span>Slavov Laboratory. Decode: computational pipeline for quantifying amino acid substitutions from alternate RNA decoding [Software and documentation]. [cited 2026 Nov 1]. Available from: [https://github.com/SlavovLab/decode](https://github.com/SlavovLab/decode).
5. <span id="ref-5"></span>Moran L. What is alternate RNA decoding? [Internet]. Sandwalk; 2026 Aug 23 [cited 2026 Nov 1]. Available from: [https://sandwalk.blogspot.com/2026/08/what-is-alternate-rna-decoding.html](https://sandwalk.blogspot.com/2026/08/what-is-alternate-rna-decoding.html).
