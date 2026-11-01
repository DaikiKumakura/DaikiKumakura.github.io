Two rows acquire the same Ensembl ID after gene-name conversion. Should their counts be added? A recent Reddit question about integrating single-cell atlases raised exactly this problem, together with a separate question about gene-length correction before scVI ([1](#ref-1)).

The answer depends on more than the destination string. The two rows might count **different molecules or the same molecules twice**. Treating identifier conversion and count aggregation as one operation hides that distinction.

## Scope and sources

On November 1, 2026, I checked the official IDTrack 0.0.5 API documentation, Ensembl identifier documentation, and the scvi-tools FAQ and Tabula Muris tutorial. I did not verify the particular gene-name correspondence in the forum question. The examples below use no real gene names. They are deterministic counterexamples examining when addition is valid, not a reanalysis of an atlas or a fitted scVI model.

## An identifier does not specify the counting operation

Ensembl identifiers distinguish objects such as genes and transcripts and include model versions. Human gene and transcript identifiers are not interchangeable numbers with dispensable prefixes ([2](#ref-2)). A gene groups transcripts, so adding transcript-level rows to a gene-level row can mean adding children to their parent ([3](#ref-3)).

IDTrack's `build_graph` can fix the Ensembl release, and its conversion classifications distinguish missing, one-to-one and one-to-many matches. External mappers also offer version-suffix stripping ([4](#ref-4)). Recording only that identifiers were converted is therefore insufficient: the original identifiers, destinations, release, assembly, object type and handling of ambiguous matches matter.

Even complete annotation provenance does not establish whether the original counting procedure counted a molecule twice. Tracking gene history cannot recover molecule assignments that were discarded when a count matrix was produced.

## The condition for adding counts

Let \(A\) and \(B\) be the sets of molecules counted in two rows of one cell. If the desired output is the number of distinct molecules after combining the rows,

\[
|A\cup B|=|A|+|B|-|A\cap B|.
\]

The molecule identities here are assumed to be resolved after error correction and deduplication. They are not raw unique molecular identifier (UMI) strings: equal UMI strings alone do not define equal molecules.

Table 1 shows three examples checked in Python. All inputs are artificial integer sets, not experimental measurements.

**Table 1. Adding two rows versus counting distinct molecules**

| Condition | Row A count | Row B count | Naive sum | Shared molecules | Distinct molecules |
| --- | ---: | ---: | ---: | ---: | ---: |
| Disjoint molecules | 8 | 5 | 13 | 0 | 13 |
| Partial overlap | 8 | 5 | 13 | 4 | 9 |
| A duplicated row | 8 | 8 | 16 | 8 | 8 |

The first two cases both appear as counts of 8 and 5 in a matrix. Yet the desired totals are 13 and 9. Counts and destination identifiers alone cannot determine which total is correct.

Conversely, addition is justified if the original quantification establishes that the rows partition molecules belonging to the same gene, with every molecule assigned exactly once. If a row was copied under another name, deduplication rather than addition is appropriate. Equal numerical values do not prove duplication either: distinct features can coincidentally have equal counts.

Estimated transcript counts require another distinction. Values produced by allocating ambiguously mapped reads and accounting for effective length are not sets of observed UMIs. Table 1 is not an aggregation algorithm that replaces the quantifier's measurement model.

## Normalization does not remove double counting

Could scaling total counts remove an error made earlier? Consider two cells with 10 true target molecules and 90 background molecules each. Suppose the target's 10 molecules are duplicated in the matrix for only the second cell.

After naive aggregation, target counts are 10 versus 20 and library totals are 100 versus 110. Scaling to 10,000 counts produces target values of 1000 versus 1818.2, an apparent 1.82-fold difference despite equal true target abundance. The background total instead falls from 9000 to 8181.8. This is arithmetic for two artificial cells, not an experimental batch effect or a differential-expression test.

Conservation of total counts across aggregation does not exclude duplication. If the input already contains a copied row, its erroneous total is faithfully conserved. Preserving the matrix numerically and preserving the meaning of an observation are different checks.

## scVI input depends on how counts were measured

scVI models expression counts. Its official FAQ warns against inadvertently supplying normalized or transformed values to models expecting raw counts, including scVI ([5](#ref-5)). Ordinary UMI input does not acquire a need for automatic gene-length division, cell-wise total-count scaling or logarithmic transformation simply because identifiers were converted.

There is an important qualification. The official Tabula Muris tutorial applies gene-length normalization to Smart-seq2 read counts without UMIs. It distinguishes their length dependence from UMI measurements ([6](#ref-6)). A universal ban on length correction for every scVI workflow would therefore also be wrong. The model and measurement protocol must be identified before choosing the corresponding implementation.

Length correction and aggregation are not generally interchangeable operations. With artificial counts of 8 and 5 and lengths of 1 kb and 2 kb, division followed by summation gives \(8/1+5/2=10.5\). Adding first and dividing by an arbitrary 1.5 kb gives 8.67. The latter length is only an illustrative choice, not a valid definition of gene length. Harmonizing a name does not determine the measurement model needed for correction.

## What provenance can and cannot establish

The useful record includes counting provenance, not just a conversion table. Table 2 is an audit derived from these counterexamples, not an official acceptance criterion of IDTrack or scVI.

**Table 2. Records separating identifier conversion from count aggregation**

| Record | Question it supports |
| --- | --- |
| Original feature identifiers and names | Was only a display label changed, or was a different feature involved? |
| Species, assembly, annotation release and ID version | Are the reference systems comparable? |
| Object type such as gene or transcript | Were aggregation levels mixed? |
| Quantifier, assignment and deduplication settings | Could the rows contain the same molecules? |
| One-to-many and missing matches with selection rules | Were ambiguous mappings silently collapsed? |
| Per-cell totals and retained features before and after aggregation | Did implementation lose or multiply entries? |

Requantifying original data with a common annotation and counting procedure can at least align the observational units. With only aggregated matrices, the shared component in Table 1 may remain unidentifiable. Comparing analyses that retain or exclude questionable features can examine sensitivity to that uncertainty; it cannot recover the correct molecule count.

A shared Ensembl destination supports annotation harmonization. Whether counts should be added still depends on what the original rows counted. Before a more sophisticated normalization, the indispensable information is the counting definition that cannot be reconstructed once lost.

## Data and code availability

The [Python script](shared/ensembl-count-aggregation/analysis.py), [result JSON](shared/ensembl-count-aggregation/results/results.json) and [reproduction instructions](shared/ensembl-count-aggregation/REPRODUCE.md) reproduce the artificial-set, duplication and length-correction examples. The script ran with Python 3.12.4 using only the standard library and no random numbers. It does not perform real gene mapping, analyze molecule-level data or train scVI.

## References

<a id="ref-1"></a>
1. Reddit user. Handling many-to-one gene name mappings [Reddit discussion; editorially shortened title]. r/bioinformatics. [cited 2026 Nov 1]. Available from: [Discussion permalink](https://www.reddit.com/r/bioinformatics/comments/1xjdmkb/handling_manytoone_gene_name_mappings_eg/).

<a id="ref-2"></a>
2. Ensembl. I have an Ensembl ID, what can I tell about it from the ID? Ensembl release 116 documentation [Internet]. [cited 2026 Nov 1]. Available from: [Ensembl FAQ](https://jun2026.archive.ensembl.org/Help/Faq?id=488).

<a id="ref-3"></a>
3. Ensembl. Ensembl Core API Tutorial: Genes, Transcripts, and Exons [Internet]. [cited 2026 Nov 1]. Available from: [Core API tutorial](https://asia.ensembl.org/info/docs/api/core/core_tutorial.html).

<a id="ref-4"></a>
4. IDTrack developers. Reference; External Mappers. IDTrack 0.0.5 documentation [Internet]. [cited 2026 Nov 1]. Available from: [Reference](https://idtrack.readthedocs.io/en/latest/reference.html); [External Mappers](https://idtrack.readthedocs.io/en/latest/reference/external_mappers.html).

<a id="ref-5"></a>
5. scvi-tools developers. Frequently asked questions. scvi-tools documentation [Internet]. [cited 2026 Nov 1]. Available from: [Frequently asked questions](https://docs.scvi-tools.org/en/stable/faq.html).

<a id="ref-6"></a>
6. scvi-tools developers. Integration and label transfer with Tabula Muris. scvi-tools documentation [Internet]. [cited 2026 Nov 1]. Available from: [Tabula Muris tutorial](https://docs.scvi-tools.org/en/stable/tutorials/notebooks/scrna/tabula_muris.html).
