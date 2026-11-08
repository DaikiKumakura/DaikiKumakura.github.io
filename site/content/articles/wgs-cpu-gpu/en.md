Three hours using a central processing unit (CPU) versus 3.2 hours using a graphics processing unit (GPU): a Reddit post inspected on November 8, 2026, Japan Standard Time, reports these whole-genome sequencing, or WGS, processing times for bwa-mem3 fast mode and Parabricks [(1)](#ref-1).

The possibility that a GPU is not automatically faster is appealing. Before using those numbers to justify a migration, however, the comparison needs a defined endpoint and output. Different processing boundaries and different results create different interpretations of speed.

## Scope and sources

I examined the Reddit post and visible comments, the associated public workflow and official bwa-mem3 and Parabricks documentation. No independent WGS run, alignment comparison or variant-accuracy evaluation was performed. This article evaluates the scope of the public comparison rather than determining empirical CPU–GPU superiority.

The workflow makes commands and processing steps inspectable [(2)](#ref-2). Public instructions, however, are not evidence that all resulting outputs have been quality-validated.

## Fast mode does not promise identical output

The bwa-mem3 documentation explicitly states that `--fast` does not produce the same alignments as the default mode [(3)](#ref-3). The comparison therefore cannot be interpreted solely as a faster implementation of an identical operation.

Different alignments do not automatically mean worse variant calls. Reads can move between similarly plausible locations, or changes can affect reads excluded downstream. Conversely, a small global difference can matter if concentrated near a relevant variant or repetitive region.

Alignment agreement and recovery of true variants must therefore be distinguished. A changed output is not automatically a failure; its location and downstream consequences determine its significance.

## Where the stopwatch starts and stops

WGS processing includes sorting, duplicate handling, base-quality recalibration and file input/output (I/O) beyond alignment. NVIDIA's documentation describes additional operations within `fq2bam`; recalibration depends on supplied input and output options [(4)](#ref-4).

Comparing one command's completion with another pipeline after extra processing can measure different endpoints. Identical command names do not solve this problem when options change the endpoint's contents. A runtime needs an explicit specification of what it measures.

For conceptual serial stages, write \(T=T_{\mathrm{map}}+T_{\mathrm{sort}}+T_{\mathrm{dup}}+T_{\mathrm{other}}\). Accelerating one stage may barely change total time if another dominates. This is an explanatory decomposition, not a measured breakdown of overlapping execution. It separates stage-level performance from end-to-end latency.

## Faster and cheaper are different questions

Suppose the reported 3.0 and 3.2 hours measure the same endpoint and remain stable on repetition. With hourly prices \(p_C,p_G\) for the complete CPU and GPU environments, computation costs are \(3.0p_C\) and \(3.2p_G\). The GPU environment is cheaper when

\[
\frac{p_G}{p_C}<\frac{3.0}{3.2}=0.9375.
\]

Prices refer to complete environments, including CPU and memory, rather than a GPU alone. Storage, transfer and waiting costs are omitted. No current cloud prices were used.

Running multiple samples concurrently can also separate single-sample latency from throughput. Comparing an existing CPU installation with newly acquired GPU capacity introduces another accounting choice. This pair of runtimes alone cannot establish general cost or capacity conclusions.

## Quality requires a benchmark and an evaluation region

When outputs differ, their mutual agreement cannot identify the better output. Both can agree on the same error. An independently defined benchmark sample and evaluation region are needed. Genome in a Bottle provides access points for public benchmark releases [(5)](#ref-5).

Performance inside benchmark regions does not automatically extend to the whole genome. Single-nucleotide variants, insertions and deletions, easy regions and difficult regions can behave differently. Changing callers, reference sequences or benchmark versions adds differences beyond alignment.

The central question is not whether the reported acceleration should be dismissed. It is whether the replacement target is an aligner or an end-to-end analysis including variant calls. A useful comparison of the former does not automatically validate replacing the latter.

## Conclusion

The public post reports CPU processing approaching GPU runtime under particular conditions. It does not establish that CPUs are generally faster or GPUs unnecessary.

With a fast mode, timing must be read alongside changed outputs. Was the processing endpoint preserved, and was variant accuracy retained? The three-hour figure opens those questions; it does not replace the adoption decision.

## Data and code availability

The cost boundary is calculated under `WGS` in the [script](shared/wgs-cpu-gpu/reproduce.py) and [output](shared/wgs-cpu-gpu/illustration.json). Runtime inputs are the poster's reported values, not independent measurements. The workflow was inspected at commit `ba6c6203fc91643d9018f2432bfab12173ca5174` [(2)](#ref-2). No WGS quality-evaluation results are provided here.

[Download code and results](shared/wgs-cpu-gpu/wgs-cpu-gpu.zip).

## References

1. <a id="ref-1"></a> Comparison of bwa-mem, minibwa, bwa-mem3 and Parabricks [Reddit post; editorial description]. r/bioinformatics [cited 2026 Nov 8, JST; exact posting timestamp not independently verified]. [Discussion](https://www.reddit.com/r/bioinformatics/comments/1xqcr6u/i_compared_bwamem_minibwa_bwamem3_and_parabricks/).

2. <a id="ref-2"></a> bio-pype. bwas_comparison [Workflow documentation]. Codeberg; 2026. Commit ba6c6203fc91643d9018f2432bfab12173ca5174 [cited 2026 Nov 8]. [Versioned workflow](https://codeberg.org/bio-pype/test_workflows/src/commit/ba6c6203fc91643d9018f2432bfab12173ca5174/bwas_comparison).

3. <a id="ref-3"></a> fg-labs. bwa-mem3: Three ways to run it [Software documentation]. GitHub [cited 2026 Nov 8]. [Repository](https://github.com/fg-labs/bwa-mem3#three-ways-to-run-it--plain---compat---fast).

4. <a id="ref-4"></a> NVIDIA. fq2bam (BWA-MEM + GATK) [Software documentation]. Parabricks v4.8.0 [cited 2026 Nov 8]. [Official documentation](https://docs.nvidia.com/clara/parabricks/tool-reference/tools/fq2bam).

5. <a id="ref-5"></a> Genome in a Bottle. giab_latest_release [Dataset documentation]. GitHub [cited 2026 Nov 8]. [Benchmark release directory](https://github.com/genome-in-a-bottle/giab_latest_release).
