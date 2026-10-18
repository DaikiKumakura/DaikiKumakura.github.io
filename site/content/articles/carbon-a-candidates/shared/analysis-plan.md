# Plan: how much of Carbon-A's "566 million gene candidates" is real?

Fixed 2026-10-18, before downloading any prediction GFF.

## Question
The Carbon-A release reports 566 million predicted protein-coding loci across 48,167 GenBank eukaryotic assemblies
(22,617 taxa). Decompose that count with the public predictions: how many are complete gene models, how confident,
how many are duplicates of the same species, and how well do predictions match RefSeq where RefSeq annotation exists?

## Data (public, HuggingFaceBio/genbank-annotations bucket; NCBI RefSeq)
- `cds/<division>/<accession>/{metadata.json, annotations.gff3.gz}` per assembly. Listing taken 2026-10-18.
- Explorer taxonomy (accession -> taxid, NCBI taxonomy tree) from the Carbon-A database explorer Space.
- RefSeq annotation GFF (NCBI FTP) for paired assemblies with identical sequence.

## Analyses
1. Census (all assemblies): sum of `gene_count` by division; assemblies per species (taxid rolled up to species);
   genes in species with more than one assembly; a per-species count using one assembly (the one with most genes is not used;
   the most recent accession is used).
2. Gene-model status (stratified random sample, 20 assemblies per division, seed 20261018): fraction of genes with
   status=complete; incomplete reasons; confidence distribution; CDS length; relation to assembly fragmentation
   (annotated bases / contig count).
3. RefSeq agreement: sample assemblies with a paired identical RefSeq assembly that carries NCBI annotation, up to 4 per division
   (smallest GFFs first to bound download size). Per prediction: exact CDS-chain match to any RefSeq CDS chain on the same strand;
   any same-strand CDS overlap; by confidence bin. Recall of RefSeq protein-coding genes (overlap). Caveat: RefSeq was the training
   label set, so this is an in-distribution upper bound, not a test on new species.
Reported as counts and proportions with binomial or bootstrap (by assembly) 95% intervals. Exploratory; no hypothesis tests.

## Not done
No new wet-lab or homology search; "real" means agreement with an existing annotation or a complete open reading frame, not proof of a protein.

## Addendum after review (2026-10-18)
- RefSeq comparison: the first selection (GFF size <= division median, 3 per division) over-selected low-yield assemblies; replaced by
  3 random distinct species per division without a size filter. First results kept as *_v1_sizefiltered.csv.
- One assembly per species: latest accession (as planned) is primary; two other rules reported as a range.
- Added after seeing data: minimum processed record length, low-yield vertebrate assemblies and their registration batch (exploratory).
