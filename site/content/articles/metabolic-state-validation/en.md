Literature and public materials checked on October 14, 2026. This is a literature-based discussion without new analysis.

MeRN, a preprint released in September 2026, infers metabolic states from single-cell transcriptional data ([1](#ref-1)). Its variational autoencoder incorporates metabolic-network structure and learns cell states and latent representations of reaction and pathway activity. The paper compares estimates with protein measurements along mouse intestinal villi, benchmarks against methods including scFEA, and applies the model to Folr1-deficient embryos and immune cells from lung-cancer patients treated with anti-PD-1 therapy.

Directly measuring metabolism in individual cells remains difficult. Single-cell metabolomics has sensitivity and coverage limits, whereas single-cell RNA-seq is abundant. Inferring metabolism from transcription is appealing; earlier methods such as Compass and scFEA pursue this direction and have their own validation experiments ([2](#ref-2), [3](#ref-3)).

The first question is what an estimated “metabolic state” represents, and which independent observation was used to check it.

## Three different meanings of metabolism

Methods differ in their targets. At least three quantities require separation.

1. **Metabolite abundance:** the amount present at a particular time, measured by metabolomics. Many large cell-line datasets report relative abundances rather than absolute concentrations.
2. **Metabolic flux:** the rate at which a reaction proceeds. Flux is not directly read from an abundance measurement. Isotope-labeled nutrients and metabolite-labeling patterns can be fitted to a network model, as in carbon-13 metabolic flux analysis.
3. **Metabolic capacity:** the potential to support reactions inferred from enzyme-gene or protein abundance.

Transcription is most closely related to the third category. Enzyme abundance is not necessarily proportional to mRNA, and enzyme activity also depends on post-translational modification, substrate concentration and allosteric regulation. Metabolite abundance reflects the balance between production and consumption. High flux can coexist with a small pool, and the reverse is possible.

Table 1. Metabolic estimates from transcription and the validation targets in their original papers.

| Method | Principal estimate | Main validation reported |
|---|---|---|
| Compass ([2](#ref-2)) | Potential reaction activity based on flux-balance analysis, related to capacity and flux | Metabolic assays; chemical and genetic intervention in polyamine metabolism; in-vivo phenotypic intervention |
| scFEA ([3](#ref-3)) | Cell-wise metabolic flux | Comparison with matched metabolomics under altered oxygen and genetic conditions |
| MeRN ([1](#ref-1)) | States representing reaction and pathway activity | Comparison with protein measurements along intestinal villi; method benchmarks; applications to knockout embryos and treatment data |

All three use some independent information. The quantity validated differs, however. Compass tests phenotypes arising from prediction-derived hypotheses; scFEA compares inferred flux with changes in metabolite abundance; MeRN compares estimates with proteins, closer to capacity. Direct, independent, cell-wise measurements of the estimated quantity itself remain uncommon.

## Bulk cell-line studies disagree on abundance prediction

Bulk cell-line datasets can measure expression and metabolite abundance in the same lines. Here the target is the first category, abundance, rather than single-cell capacity or flux. Three studies illustrate different results using cancer-cell-line CCLE data.

Li and colleagues fitted metabolite-specific LASSO regressions in 454 cancer cell lines ([4](#ref-4)). Few metabolites were predicted accurately even after accounting for culture conditions and lineage. The NNMT–1-methylnicotinamide relationship was among the robust findings, and validation was restricted to high-purity cancer samples.

Cavicchioli and colleagues constructed metabolite–transcript correlation networks using CCLE and reported prediction of abundances and between-group differences in the independent NCI-60 dataset ([5](#ref-5)).

The 2026 Metab8D study used eight molecular data types, including transcription, proteins, phosphorylation and DNA methylation, across approximately 1,000 cell lines ([6](#ref-6)). Transcription was a leading predictor, but relationships were heterogeneous. Peripheral metabolites could be predicted by corresponding enzyme levels; central metabolites required combinations of factors and did not always reflect expression of their own pathway.

These results can differ because the metabolites and prediction criteria differ, without one study necessarily being wrong. Pathway-enzyme expression does not directly reveal pathway-metabolite abundance. This does not refute methods estimating capacity or flux; it cautions against relabeling their scores as high or low metabolite abundance.

## What independent comparisons can establish

Table 2. Different ways to check metabolic-state estimates and their limits.

| Comparison | What it can establish | Limitation |
|---|---|---|
| Matched bulk metabolomics or isotope tracing and flux analysis | Agreement with abundance or flux averaged across a population | Cannot establish cell-wise variation |
| Spatial metabolomics, including mass-spectrometry imaging, with spatial transcriptomics | Agreement with spatial metabolite distributions | Restricted metabolite coverage and resolution |
| Metabolomics after cell separation | Abundance differences between cell types | Separation can itself change metabolites |
| Metabolic intervention: nutrient removal, enzyme knockout or inhibitors | Whether estimates change in the expected direction | Interpretation depends on the issues below |

Reproducing known biology, such as intestinal spatial differences, is useful. Stronger evidence also asks how much information the estimate adds beyond a simple comparator using only cell-type identity.

## Pitfalls in intervention-based validation

As discussed in my [article on prediction and mechanism](prediction-vs-mechanism-en.html), reproducing observational patterns does not guarantee correct intervention predictions. Using metabolic estimates for target discovery or patient stratification requires checking intervention outcomes. Transcription-based estimators introduce particular complications.

### Changes already implied by the input

An enzyme-gene knockout lowers its expression, so an estimator may mechanically report lower activity for the corresponding reaction. That alone is weak evidence of predictive ability. Propagation to distant reactions or pathways is a less trivial target.

### Timing and adaptation

An inhibitor can immediately reduce enzyme activity before mRNA changes. Transcription may instead describe later adaptation, sometimes in the opposite direction through feedback. Inhibiting cholesterol synthesis, for example, can induce transcription of pathway genes. The prediction target must identify what is being predicted and when after intervention.

### Independent measurements of the intended target

A cellular phenotype, metabolite abundance and flux are different intervention readouts. Independent metabolomics or isotope-tracing measurements provide more direct checks than reuse of transcriptional input alone.

### Fitting after intervention versus predicting beforehand

Applying a model to post-intervention data and describing differences is different from making a prospective intervention prediction and testing it. The latter provides stronger evidence of predictive capability.

## Drug-discovery context

Even a valid estimate may not transfer to another environment. Cells with the same oncogenic mutation can have different metabolic dependencies in culture and in vivo ([7](#ref-7)). Simply making medium more plasma-like can substantially change cellular metabolism ([8](#ref-8)). Tumors add competition between cancer and immune cells and spatial oxygen gradients.

Preclinical metabolic rationale has also failed to translate into clinical benefit. The IDO1 inhibitor epacadostat did not add benefit to anti-PD-1 treatment ([9](#ref-9)). The glutaminase inhibitor telaglenastat did not improve progression-free survival in a renal-cancer combination trial ([10](#ref-10)). These failures are not failures of the estimators discussed here. They illustrate the distance between metabolic knowledge and a therapeutic decision.

## Abundance and flux are different validation targets

A large metabolite pool is not the same as high flux through it. An association between a transcription-derived score and metabolite abundance or phenotype does not validate flux itself.

MeRN's comparisons and applications likewise depend on the estimated quantity, environment and measurement. An association under a culture condition cannot simply be read as a quantitative metabolic flow that also holds in another tissue or in vivo.

## References

1. <span id="ref-1"></span>Lewinsohn DP, Dias N, Chau A, Koike Y, Smith ZD, Ioannidis NM, et al. Extracting interpretable single-cell metabolic states with graph-guided representation learning. bioRxiv [preprint]. 2026 Sep 24. [doi:10.64898/2026.09.17.751504](https://doi.org/10.64898/2026.09.17.751504).
2. <span id="ref-2"></span>Wagner A, Wang C, Fessler J, DeTomaso D, Avila-Pacheco J, Kaminski J, et al. Metabolic modeling of single Th17 cells reveals regulators of autoimmunity. Cell. 2021;184(16):4168–4185.e21. [doi:10.1016/j.cell.2021.05.045](https://doi.org/10.1016/j.cell.2021.05.045).
3. <span id="ref-3"></span>Alghamdi N, Chang W, Dang P, Lu X, Wan C, Gampala S, et al. A graph neural network model to estimate cell-wise metabolic flux using single-cell RNA-seq data. Genome Research. 2021;31(10):1867–1884. [doi:10.1101/gr.271205.120](https://doi.org/10.1101/gr.271205.120).
4. <span id="ref-4"></span>Li H, Barbour JA, Zhu X, Wong JWH. Gene expression is a poor predictor of steady‐state metabolite abundance in cancer cells. The FASEB Journal. 2022;36(5):e22296. [doi:10.1096/fj.202101921RR](https://doi.org/10.1096/fj.202101921RR).
5. <span id="ref-5"></span>Cavicchioli MV, Santorsola M, Balboni N, Mercatelli D, Giorgi FM. Prediction of Metabolic Profiles from Transcriptomics Data in Human Cancer Cell Lines. International Journal of Molecular Sciences. 2022;23(7):3867. [doi:10.3390/ijms23073867](https://doi.org/10.3390/ijms23073867).
6. <span id="ref-6"></span>Schildcrout R, Smith K, Bhowmick R, Lu Y, Menon S, Kapadia M, et al. Metab8D: a metabolic regulome network from multiomics and machine learning. Communications Biology. 2026;9(1):1161. [doi:10.1038/s42003-026-10409-3](https://doi.org/10.1038/s42003-026-10409-3).
7. <span id="ref-7"></span>Davidson SM, Papagiannakopoulos T, Olenchock BA, Heyman JE, Keibler MA, Luengo A, et al. Environment Impacts the Metabolic Dependencies of Ras-Driven Non-Small Cell Lung Cancer. Cell Metabolism. 2016;23(3):517–528. [doi:10.1016/j.cmet.2016.01.007](https://doi.org/10.1016/j.cmet.2016.01.007).
8. <span id="ref-8"></span>Cantor JR, Abu-Remaileh M, Kanarek N, Freinkman E, Gao X, Louissaint A, et al. Physiologic Medium Rewires Cellular Metabolism and Reveals Uric Acid as an Endogenous Inhibitor of UMP Synthase. Cell. 2017;169(2):258–272.e17. [doi:10.1016/j.cell.2017.03.023](https://doi.org/10.1016/j.cell.2017.03.023).
9. <span id="ref-9"></span>Long GV, Dummer R, Hamid O, Gajewski TF, Caglevic C, Dalle S, et al. Epacadostat plus pembrolizumab versus placebo plus pembrolizumab in patients with unresectable or metastatic melanoma (ECHO-301/KEYNOTE-252): a phase 3, randomised, double-blind study. The Lancet Oncology. 2019;20(8):1083–1097. [doi:10.1016/S1470-2045(19)30274-8](https://doi.org/10.1016/S1470-2045(19)30274-8).
10. <span id="ref-10"></span>Tannir NM, Agarwal N, Porta C, Lawrence NJ, Motzer R, McGregor B, et al. Efficacy and Safety of Telaglenastat Plus Cabozantinib vs Placebo Plus Cabozantinib in Patients With Advanced Renal Cell Carcinoma. JAMA Oncology. 2022;8(10):1411. [doi:10.1001/jamaoncol.2022.3511](https://doi.org/10.1001/jamaoncol.2022.3511).
