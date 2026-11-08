Did two cells with similar RNA (ribonucleic acid) expression arrive there along the same path? Expression distributions alone need not determine the answer. Different ancestors can converge on similar states, while similar states can diverge toward different futures.

Gowri and colleagues introduce lineage inpainting, a generative approach conditioned on lineage context, including sister and cousin cells. Applied to lineage-traced mouse development, it addresses convergence not resolved by expression alone [(1)](#ref-1). The important change is the observation added to the prediction problem, rather than the generative-AI label.

## Scope and sources

This article examines the October 29, 2026 preprint, version 1, together with the authors' explanation and public code. I checked the methods, evaluation and supplementary held-out-lineage analysis, without retraining the model or reanalyzing mouse data.

The approach imputes unobserved internal states and generates conditional states on supplied lineage trees. It should be distinguished from freely generating tree topology and times [(2)](#ref-2). A small probability example below illustrates how context can reduce distributional ambiguity.

## The same distributions permit different connections

Let \(X\) be current expression state, \(S\) a binary observation from a related cell, and \(Y\) a later binary state. Set \(X=0\) for every cell and let \(S\) be equally likely to be zero or one.

Model A sets \(Y=S\). Model B sets \(Y=1-S\). Both have identical current states and a later population split equally between zero and one. Marginal expression distributions cannot distinguish them.

For cells with \(S=0\), however, \(P(Y=1\mid X=0,S=0)\) is zero in A and one in B. Observing \(S\) alone does not identify whether A or B is correct. Using the conditional prediction requires learning the relationship from paired observations of \(S\) and \(Y\), or equivalent constraints. Additional information helps when it preserves the correspondence lost in the separate current and later distributions.

This artificial example does not claim that relatives perfectly predict development. It shows that lineage context adds observations about relationships, rather than merely adding more cells. Estimating a marginal distribution arbitrarily well cannot necessarily recover a unique, unobserved correspondence.

## Observed trees and inferred ancestors

A known lineage does not mean every ancestral transcriptome was measured. The constraint that two nodes are related and the inference of expression along their connecting branches are separate pieces of information.

Suppose two paths reach the same endpoint without intermediate observations. A lineage constrains the relationship between cells but need not uniquely determine the speed or shape of either path. Smooth generated ancestral states are not direct observations of smooth biological trajectories.

Evaluation must therefore assess both agreement with expression marginals and plausible relationships within the tree. A model ignoring lineage can look good on the former. A model producing attractive trees can satisfy the latter while missing observed state distributions.

The preprint includes training on 45 trees and evaluation on 11 held-out trees [(1)](#ref-1). It would be inaccurate to dismiss it as merely redrawing training lineages. Generalization to unused trees, however, is different from directly validating unobserved ancestral RNA. Separating these claims preserves the value of the evaluation without extending its reach.

## Perturbation is a further inferential step

Imputing a missing state from relatives predicts within observed relationships. Changing a gene can change those relationships themselves.

The authors use the observational model to formulate perturbation hypotheses and compare predictions with a Tbx5 perturbation experiment [(1)](#ref-1). Such a comparison matters, but agreement in one intervention does not establish transportability to arbitrary interventions.

If an intervention changes cellular expression while preserving subsequent transition rules, reconnecting that state to learned dynamics may be defensible. If it also changes proliferation, death or intercellular interactions, it can change the tree or environment. Applying the same conditional law then requires stronger assumptions. The crucial issue is what remains invariant after intervention, not simply whether the gene was absent from training perturbations.

## Conclusion

Lineage observations add constraints beyond RNA distributions. They can keep cells with similar current expression from being forced into the same history.

Inferred ancestors remain inferred, and state completion does not automatically identify intervention effects. The value of lineage inpainting is clearest when the added observations and the ambiguities they resolve remain visible, rather than being compressed into a claim to have recreated development.

## Data and code availability

The artificial example and its conditional probabilities are recorded under `lineage` in the [script](shared/lineage-context-development/reproduce.py) and [output](shared/lineage-context-development/illustration.json). The authors provide [code](https://github.com/g-kl/lineage-inpainting) and [data and weights](https://doi.org/10.5281/zenodo.23750040). Their training and inference pipelines were not rerun.

[Download code and results](shared/lineage-context-development/lineage-context-development.zip).

## References

1. <a id="ref-1"></a> Gowri G, Fishman N, Colgan WN, Wang M, Kijima Y, Kumar SA, et al. Learning developmental dynamics from lineage context [Preprint]. arXiv; 2026. Version 1, submitted 2026 Oct 29. [https://doi.org/10.48550/arXiv.2610.40447](https://doi.org/10.48550/arXiv.2610.40447).

2. <a id="ref-2"></a> Lineage inpainting authors. Lineage inpainting: notes [Internet]. 2026 [cited 2026 Nov 8]. [Author's technical notes](https://lineageinpainting.info/notes/).
