A report that computation has found a promising candidate is some distance from evidence of benefit in animals or patients. Pointing out that distance is easy. Assessing where an individual study actually stands requires more care.

A study of inhibitors of transmembrane serine protease 2 (TMPRSS2), discussed on X in October 2026, makes the distinction concrete. It includes enzyme and cell experiments, whereas the authors' reported approximately 29-fold improvement concerns computational cost. Calling it computation alone misses evidence. Reading the improvement as 29-fold greater therapeutic efficacy changes the outcome being measured.

## Scope and sources

The starting point was a [post](https://x.com/osYZtdWoeHsph6C/status/2115036216316055875) about the gap between computational discovery reports and in vitro/in vivo efficacy. It quoted a [post](https://x.com/shizuku50312776/status/2114882150172660120) introducing representative structures obtained using molecular dynamics (MD) and Markov models, with a link to a BaraPhaSilico article ([1](#ref-1), [2](#ref-2)).

The underlying paper is Elez et al.'s 2025 study, rather than a new experimental report from 2026. I compared the paper's text, [original Table 1](https://www.nature.com/articles/s41467-025-62139-5#Tab1), [original Figure 4](https://www.nature.com/articles/s41467-025-62139-5#Fig4), and the explanatory article. I did not rerun MD or experiments or evaluate additional compounds ([3](#ref-3), [4](#ref-4)).

## The denominator of the 29-fold improvement

The approximately 29-fold result compares active-learning selection with random selection in a computational search for known inhibitors. It is not a ratio of enzyme inhibition, cellular efficacy, or animal survival. Core hours also measure accumulated resource use rather than elapsed time. Different degrees of parallelization can change waiting time without changing total resource consumption ([3](#ref-3)).

The accounting boundary also needs qualification. The footnote to [original Table 1](https://www.nature.com/articles/s41467-025-62139-5#Tab1) states that marked times include approximately 8,000 h to generate the receptor ensemble. Yet marked entries include 3,403.0 h, which is smaller than 8,000 h. The displayed times and footnote do not provide a consistent account of that preparation cost. I therefore treat the approximately 29-fold figure as an author-reported result, not an independently audited total-cost ratio including preparation ([3](#ref-3)).

Even with that qualification, the intended comparison concerns the cost of reaching a specified search endpoint. Making that search cheaper is useful. Its computational endpoint, however, is distinct from a therapeutic endpoint. Efficiently prioritizing candidates does not establish improved patient outcomes.

MD also has separate roles. The paper evaluates preparing an ensemble of receptor structures separately from moving candidate poses during scoring. In the DrugBank comparison involving known inhibitors, the latter provided limited additional benefit at greater computational cost. That finding does not negate the benefit of using an ensemble of receptor structures ([3](#ref-3)).

The BaraPhaSilico explanation already distinguishes the comparison underlying the 29-fold claim and the additional cost of dynamic scoring. This is not a case of uncovering exaggeration in that explanation. The issue is preserving conditions that both the paper and its explanation state when discussing them in shorter social-media exchanges ([4](#ref-4)).

## Cell experiments and animal efficacy answer different questions

The paper reports enzyme inhibition and cellular activity for BMS-262084. [Original Figure 4](https://www.nature.com/articles/s41467-025-62139-5#Fig4) presents experimental findings, not docking scores. The paper does not evaluate efficacy in animals or therapeutic benefit in humans ([3](#ref-3)).

The supported description is that this study has experimental support through the cellular stage. It is not that the compound fails in animals. Counting a paper without animal efficacy results as a failure combines an unassessed outcome with a negative one. Moving a cellular result into the animal or clinical-success column makes the opposite mistake.

The concentration that inhibits an enzyme and the concentration maintained at a site of action in a living organism are different quantities. Absorption, distribution, metabolism, and excretion affect the latter. Whether target modulation improves disease is another question. An enzyme or cellular result can be correct without establishing that the candidate will become a therapy.

## Where clinical evidence for the same target belongs

A randomized camostat trial provides relevant clinical context for TMPRSS2-directed treatment. The ACTIV-2 phase 2 study compared 109 camostat recipients with 107 placebo recipients among 216 participants who initiated treatment. Median time to symptom improvement was 9 days in both groups. Under the conditions studied, the paper reported no acceleration of viral clearance or symptom improvement ([5](#ref-5)).

This was not a trial of BMS-262084. Results involving a different molecule, exposure, and patient population cannot establish that BMS-262084 will fail. Their relevance is as an example of cellular antiviral activity and patient benefit requiring separate evaluation. Ignoring the camostat trial understates that gap; transferring its outcome directly to another compound overstates it.

For this clinical study, I checked the bibliographic record and principal abstract results. I did not perform a trial meta-analysis, compare exposures, or re-estimate treatment effects.

## The translation rate remains unidentified

A reply to the original post raised publication bias and suggested examining what fraction of cell-active candidates also work in animals. The reply does not provide a candidate inventory or follow-up data from which to calculate that fraction ([6](#ref-6)).

Such a fraction requires, at a minimum, a defined collection of cell-positive candidates and records distinguishing animal studies that were performed, studies that were not performed, and their results. Published success stories alone do not reconstruct that collection. Counting untested candidates as negative and restricting the denominator to animal-tested candidates both measure something different from the translation rate of the original candidate collection.

Consequently, this paper and social-media impressions cannot establish that computational discovery translates to animals less often than conventional methods. The conventional-method comparison would require the same definitions of selection and follow-up. An individual study's evidence and a discovery method's overall success rate are separate assessments.

A contemporaneous Reddit developer post also explicitly distinguishes docking scores from experimental affinity and search animations from MD. It illustrates describing what a tool's output represents; it is neither an independent replication of the TMPRSS2 paper nor evidence of consensus across the forum ([7](#ref-7)).

## Conclusion

The TMPRSS2 study can be evaluated as a progression from computational prioritization to enzyme and cell experiments. The approximately 29-fold claim concerns computational cost, with unresolved preparation-cost accounting. Benefit in animals or patients remains unresolved by these results.

The gap between demonstrating cellular activity and establishing a therapy still needs to be addressed. An unfilled gap, however, is not an observed failure. Preserving that distinction makes both the computational contribution and its limits clearer.

## References

1. <a id="ref-1"></a> osYZtdWoeHsph6C. Comment on the gap between computational drug discovery and in vitro/in vivo efficacy [X post; Japanese]. 2026 Oct 27 [cited 2026 Nov 1]. [Original post](https://x.com/osYZtdWoeHsph6C/status/2115036216316055875). Description in English by the author.
2. <a id="ref-2"></a> shizuku50312776. Comment on representative structures from molecular dynamics and Markov models [X post; Japanese]. 2026 Oct 27 [cited 2026 Nov 1]. [Original post](https://x.com/shizuku50312776/status/2114882150172660120). Description in English by the author.
3. <a id="ref-3"></a> Elez K, Hempel T, Shrimp JH, Moor N, Raich L, Rocha C, et al. Simulations and active learning enable efficient identification of an experimentally-validated broad coronavirus inhibitor. Nature Communications. 2025;16:6949. [doi:10.1038/s41467-025-62139-5](https://doi.org/10.1038/s41467-025-62139-5).
4. <a id="ref-4"></a> BaraPhaSilico. Narrowing inhibitor candidates with computation and active learning [blog; Japanese; title translated by the author]. BaraPhaSilico. 2026 Oct 23 [updated 2026 Oct 24; cited 2026 Nov 1]. [Article](https://baraphasilico.com/articles/tmprss2/).
5. <a id="ref-5"></a> Jilg N, Chew KW, Giganti MJ, Daar ES, Wohl DA, Javan AC, et al. One Week of Oral Camostat Versus Placebo in Nonhospitalized Adults With Mild-to-Moderate Coronavirus Disease 2019: A Randomized Controlled Phase 2 Trial. Clin Infect Dis. 2023;77(7):941–949. [doi:10.1093/cid/ciad342](https://doi.org/10.1093/cid/ciad342).
6. <a id="ref-6"></a> nosuz. Comment on publication bias and the denominator of in vitro-to-in vivo translation [X reply; Japanese]. 2026 Oct 28 [cited 2026 Nov 1]. [Original reply](https://x.com/nosuz/status/2115368877425348689). Description in English by the author.
7. <a id="ref-7"></a> MolDesign. I'm developing a free molecular docking application with AutoDock Vina, reproducible workflows, and 3D visualization [Reddit post]. r/comp_chem. 2026 Oct 23 [cited 2026 Nov 1]. [Discussion](https://www.reddit.com/r/comp_chem/comments/1xd4kvn/im_developing_a_free_molecular_docking/).
