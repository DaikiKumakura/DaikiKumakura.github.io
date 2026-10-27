## Abstract {#article-abstract}

The ART enzyme-system report was examined by separating large-scale search, fixed-input recognition and molecular-function evidence. A post hoc known-motif search in two public phage genomes confirmed repeated upstream arrangements without rediscovering ART independently. Published campaign accounting uses different units, including 119 tasks and 949 sessions. Zero recorded rediscoveries in ten reruns is not equivalent to zero success probability; an illustrative binomial bound depends on independent comparable trials and the recording rule. Sequence recognition and RNA expression do not establish genome-editing function.

## Introduction {#article-introduction}

An announcement that Claude had identified an enzyme system with CRISPR-like features attracted attention. What was discovered, and what can be reproduced? **Recognizing features of a supplied sequence differs from reaching that sequence through a large database search.**

The initial announcement appeared on September 23, 2026 ([1](#ref-1)). This article examines search records and validation using Yoon and colleagues' preprint v1, released October 11 ([2](#ref-2)). Known-motif positions were independently recalculated in two public genomes to distinguish search reruns from evaluation on fixed inputs.

## What was found around reverse transcriptases {#rt}

ART, or array-associated reverse transcriptase, combines an RT-related protein, a nearby partner gene and repeated sequence arrays. Reverse transcriptases generally synthesize DNA from RNA, but the study does not establish a completed genome-editing tool.

The systems occur in bacteriophage genomes and related contexts. RT sequences themselves were present in earlier records; the focus is the system comprising nearby noncoding repeats, associated RNAs and partners ([original Results and Figures 1–3](https://doi.org/10.64898/2026.10.05.755809), [2](#ref-2)).

The authors analyzed public RNA-seq during phage infection and found expression from repeat arrays. Separate expression experiments also detected short RNAs. That is stronger evidence than sequence appearance alone. The roles of these RNAs, RT and partner remain hypotheses; targeted DNA editing comparable to CRISPR was not demonstrated.

## Public-sequence methods and results {#_1}

GenBank MarsHill MW248466.1 and SA1 MW218148.1 were used ([3](#ref-3), [4](#ref-4)). The paper's 14-base core motif `ATATGAATACGTAT` was fixed before scanning both strands with at most one mismatch.

Hits within 1,500 bases upstream of the corresponding coding sequence (CDS) were extracted. This diagnostic window does not reproduce repeat discovery throughout the ART family. GenBank annotates MarsHill's CDS as RNA-directed DNA polymerase but the corresponding SA1 CDS as hypothetical protein. Function was not independently assigned here.

![Known core-motif positions recalculated from public genomes](shared/ai-enzyme-discovery-evidence/figures/01-known-array-layout.png)

**Figure 1. Upstream core-motif layout.** Zero denotes the corresponding CDS start. Blue marks exact matches and brown one mismatch. Bars show 14-base cores, not whole approximately 200-base repeat units. Arrows indicate CDS orientation, not gene length.

**Table 1. Known-motif hits and spacing**

| Genome | Whole-genome, both-strand hits | Upstream-window hits | Adjacent core-start spacings, bases |
| --- | ---: | ---: | --- |
| MarsHill | 5 | 5 | 213, 197, 210, 173 |
| SA1 | 6 | 5 | 212, 171, 201, 176 |

Both upstream windows contain five copies; mean start-to-start spacings are 198.25 and 190 bases. These distances include the core, rather than measuring spacer length alone. With the known motif specified, repeated arrangements outside coding regions can be confirmed.

SA1 has one additional hit outside the upstream window, beginning at position 31,724 inside another annotated CDS, QPI16945.1. **A short-motif hit alone does not identify a noncoding repeat array.** Copy number, spacing, orientation and neighboring genes also matter.

This is post hoc confirmation after reading the paper and selecting motifs and coordinates, not discovery from unknown sequences. It does not evaluate false positives, function or novelty. Two related phages are not independent replicates across the entire family.

## Search accounting uses different denominators {#_2}

“Approximately 950 agents” does not mean 950 independent researchers. The paper counts 949 **sessions**, including launch, worker, supervisor, consolidation and editing roles, with reruns in some roles. These are neither unique agents nor independent discoveries ([campaign accounting](https://doi.org/10.64898/2026.10.05.755809), [2](#ref-2)).

**Table 2. Reported search stages and units**

| Recorded stage | Count and unit |
| --- | --- |
| Search space | Approximately 1.94 billion protein clusters |
| Filtered RTs | 198,290 clusters |
| Neighborhoods examined | 10,983 loci |
| Candidate partners | 3,564 protein families |
| Deeply examined candidates | 16 plus one additional family |
| Retained novel associations in reports | 3 families |
| Final reports | 19 |
| Execution accounting | 119 tasks, 949 sessions |

This is not a single funnel: clusters, loci, families and reports use different units. The 19 final reports include three about new RT lineages. Two of 17 candidates are combined into one report, so candidate and report counts differ.

Three of 17 families retained gives 17.6%, but this concerns reported novel RT associations, not experimentally functional enzyme hits. The other 14 were rejected or deferred as known systems, annotation issues or merely neighboring genes ([candidate census and deep dives](https://doi.org/10.64898/2026.10.05.755809), [2](#ref-2)).

Code checked transcribed totals, including 949 sessions across roles and 119 completed, rejected or stopped tasks. Token counts exclude cache reads; compatibility of rounded components is documented in reproduction materials.

## Supplied-target recognition and reaching the target {#_3}

The study repeated the search campaign ten times with the same framework and prompt. Some examined ART loci; two additionally investigated the lineage. The authors' audit found no record of reading DNA upstream of the RT and no recorded repeat-array rediscovery.

That audit used RT/contig identifiers attached during the first campaign. Methods explicitly state that ART loci outside that identifier set would not be detected by this search. Zero of ten is therefore not an exhaustive detection rate for every possible ART discovery ([replicate campaigns](https://doi.org/10.64898/2026.10.05.755809), [2](#ref-2)).

A separate benchmark supplied ART sequences from the start: seven models, five input levels and 100 attempts per model–level pair, totaling 3,500. Sequences in prompt text were distinguished from files with analysis tools. Level 4 provided 96 known ART loci as files in an offline environment, adding predicted structures and structural comparison tools.

**Table 3. Different evaluations and reported results**

| Evaluation | Capability evaluated | Reported result |
| --- | --- | --- |
| Repeat large-scale search | Reach a target and identify its features | 0/10 rediscoveries within the identifier-based audit |
| Supply ART loci in prompt text | Recognize supplied-target features | At least 90% repeat recognition for four leading models |
| Supply ART files and tools | Inspect files and recognize features | Example: Opus 5 at level 4, 32% |

The last two rows use known ART inputs and Mythos 5 scoring of repeat-array claims. They do not measure false ART calls on non-ART inputs. “At least 90%” is a reported bound, not an exact count of 90 successes, and cannot be used directly as large-search success probability.

Among leading models' file-input attempts, 39% reportedly never read 200 or more contiguous DNA bases. Recognition was higher among attempts that did. This stratifies observed behavior; it does not establish the causal improvement obtained by forcing sequence reading ([original Figure 4 and fixed-input benchmark](https://doi.org/10.64898/2026.10.05.755809), [2](#ref-2)).

## Illustrative interpretation of zero recorded recoveries {#010}

Assume independent campaigns with common probability \(p\) of a rediscovery recorded under the same rule. The probability of zero in ten is

\[
P(X=0\mid p)=(1-p)^{10}
\]

The one-sided 95% upper bound is

\[
p_{\mathrm{upper}}=1-0.05^{1/10}\approx0.259
\]

![Probability of zero recoveries under independent comparable campaigns](shared/ai-enzyme-discovery-evidence/figures/02-zero-recovery-bound.png)

**Figure 2. Binomial recording model.** The curve gives the probability of no recorded rediscovery in ten attempts at an assumed recording probability. The point corresponds to the one-sided 95% upper bound of 25.9%. It assumes independent comparable trials and one recording rule, rather than measuring functional ART success or a general discovery probability.

Zero of ten does not establish true probability zero; nor does the bound estimate a success rate of approximately 26%. Trial comparability and audit completeness were not independently verified.

The original discovery was not added to form 1/11. That selected observation motivated the rerun benchmark and cannot simply be pooled as an equivalent evaluation trial. Existence of a discovery and reliably reaching it through a method require separate records.

## Discussion {#_4}

A candidate found in large-scale search is not a functionally validated system. Neighborhood arrangements and statistical criteria used for selection differ from subsequent RNA-expression evidence. Search hypotheses and tests need not form one fixed set, so the number 3,564 alone does not establish multiplicity control for the whole analysis.

The sequence recalculation confirms arrangements after the relevant features were known. It does not measure how reliably a search recognizes noncoding components after reaching the associated protein.

## Conclusion {#article-conclusion}

Claude's identification of unusual sequence organization initiated biological research. That finding differs from completing a genome-editing function or establishing a consistently reproducible discovery process. Known-motif confirmation, fixed-input recognition, search recovery and molecular function answer different questions.

## Data and code availability {#_5}

The [recalculation code, public sequences and figures](shared/ai-enzyme-discovery-evidence/ai-enzyme-discovery-evidence.zip) support sequence search, count checks and nine computational tests with the Python standard library. Redrawing figures requires matplotlib. `REPRODUCE.md` states procedures and scope; `input-provenance.json` records versions, sources and hashes.

Inputs are GenBank MW248466.1 and MW218148.1 sequences/coordinates and counts from preprint v1 ([2](#ref-2), [3](#ref-3), [4](#ref-4)). FASTA was extracted from public records; original GenBank-format files, PDFs and paper figures are not redistributed. Figures were created for this article.

This is an exploratory post hoc audit. It does not estimate the entire ART family, process RNA-seq, execute models, independently audit search logs or scoring, measure enzyme activity or genome editing, or validate clinical applications.

## References {#article-references}

1. <span id="ref-1"></span>Anthropic. Claude discovers a novel enzyme system with CRISPR-like repeats [Internet; developer announcement]. 2026 Sep 23. [Announcement](https://www.anthropic.com/research/claude-discovers-novel-enzyme-system).
2. <span id="ref-2"></span>Yoon PH, Athukoralage JS, Ameisen E, Kauderer-Abrams E, Perry NT, Durrant MG. Autonomous AI agents discover reverse transcriptases with tandem repeat arrays. bioRxiv [Preprint]. 2026 Oct 11; version 1. [Version examined](https://www.biorxiv.org/content/10.64898/2026.10.05.755809v1).
3. <span id="ref-3"></span>National Center for Biotechnology Information. Staphylococcus phage MarsHill, complete genome [Sequence record]. GenBank accession MW248466.1. [Versioned record](https://www.ncbi.nlm.nih.gov/nuccore/MW248466.1).
4. <span id="ref-4"></span>National Center for Biotechnology Information. Staphylococcus phage SA1, complete genome [Sequence record]. GenBank accession MW218148.1. [Versioned record](https://www.ncbi.nlm.nih.gov/nuccore/MW218148.1).
