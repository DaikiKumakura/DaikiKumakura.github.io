## Execution does not establish scientific validity

LLM agents have reached population-PK model construction and execution, as demonstrated in papers and a tutorial available in 2026. They have not established that an entire analysis can be delegated reliably. Both sources that actually execute analyses, PKGPT and the tutorial, distinguish running code and passing self-checks from scientific validity. Their evaluation units, repetitions and comparators differ, preventing a common performance ranking. Benchmarking initiatives are emerging, but they do not yet evaluate LLM agents.

This is a reading essay based on papers, a tutorial, repositories and conference pages consulted in October 2026. I performed no experiment or recalculation. Numerical results are transcribed from their sources. X and discussion boards were inaccessible, so practitioner reactions are not represented.

## Three meanings of AI in pharmacometrics

Table 1. Predictive models, automated search and LLM agents address different tasks.

| Meaning | Task | Example |
|---|---|---|
| Machine learning as a predictor | Predict concentration or response directly as an alternative to nonlinear mixed-effects modeling, NLME | Mao et al. 2025 ([1](#ref-1)) |
| Automated model search | Select models within a defined search space using optimization rather than an LLM | Richardson et al. 2025, pyDarwin ([2](#ref-2)) |
| An LLM acting as modeler | Write code, execute it and revise it after inspecting results | PKGPT, the context-engineering tutorial, nlmixr2llm |

This article examines the third category. Even there, writing code without execution differs from running an iterative analysis.

## What was evaluated?

Table 2. Source type, evaluation target and execution scope.

| Source | Type | Evaluated task | Scale | Execution |
|---|---|---|---|---|
| Zheng et al. 2025 ([3](#ref-3)) | Paper | Scoring LLM-written NONMEM code | 7 LLMs, 13 tasks | None; code scoring |
| PKGPT, Kwack et al. 2026 ([4](#ref-4)) | Paper and software | Iterative NONMEM execution and revision | 3 datasets, 3 runs each | Yes |
| Pritchard-Bell et al. 2026 ([5](#ref-5)) | Tutorial | Analysis divided into 36 tasks in one synthetic PK/PD scenario | 6 runs: Claude Code 3, Codex 3 | Yes |
| Ponce-Bobadilla et al. 2026 ([6](#ref-6)) | Perspective | Practices for benchmarking predictive AI | No new performance evaluation | Not applicable |
| nlmixr2llm ([7](#ref-7)) | Software | R support tools | No validation description identified | Not applicable |

Writing code, obtaining convergence and producing an expert-defensible model are different outcomes.

### Zheng: scoring code without running it

Seven LLMs answered 13 NONMEM coding tasks, scored on a six-point scale without execution. With optimized prompts, o1 and gpt-4.1 scored six on every task; the original-prompt median was five. Complex PK/PD, including indirect-response models in which a drug changes production or removal of a downstream substance, was difficult. Lag time was an example improved by prompt optimization. The authors still required user verification. These are short tasks assessed against the paper's rubric, not validated complete analyses.

Two 2024 studies, by Shin et al. ([8](#ref-8)) and Cloesmeijer et al. ([9](#ref-9)), reported structural or syntax errors and inconsistent outputs from then-current public ChatGPT or Gemini systems. I read only their abstracts.

### PKGPT: executable models can remain implausible

PKGPT uses Gemini 3.0 Flash to execute and revise NONMEM control files through five stages: base modeling, structural diagnosis, overfitting control, random-effects optimization and covariate analysis. For warfarin, n=32, the best of three runs selected by the authors' composite score had objective function value, OFV, 484.43, versus 294.41 for an expert model. The models differ: the expert includes a 0.825-hour absorption lag and allometric weight effects on clearance and volume, absent from the agent model. Even the selected run had absorption-rate random-effect shrinkage of 42.8%, above the commonly scrutinized 30% level. Other runs had OFVs 1208.94 and 1620.54 and collapsed random effects, with shrinkage 99.3% and 100%.

Results were not uniformly poor. The best theophylline run, n=12, nearly matched expert parameters. The best tobramycin run had lower OFV than the expert, 161.73 versus 173.11. However, its V2 was 149 L rather than 13.2 L and the covariance step failed. Better fit did not establish physiological plausibility. Runs took 20–40 minutes, contrasted by the authors with manual workflows lasting days or weeks.

Each dataset had only three runs, used small classical public datasets, and selected one run using a criterion independent of the expert answer. The authors identify their treatment of weight allometry through the same stepwise criteria as other covariates as a design to reconsider.

### A tutorial: self-checks pass while conclusions differ

Pritchard-Bell et al. divide analysis into 36 tasks, each given to a fresh LLM, with state passed through working files. Claude Code with Opus 4.6 and OpenAI Codex with GPT-5.3 each analyzed one synthetic PK/PD scenario three times.

Initial runs selected four PD structures, produced an eightfold EC50/IC50 range, and recommended monthly doses from 100 to 800 mg. Every model passed its convergence, precision and fit self-checks. Those checks detected mechanical failures but did not assess scientific decisions absent from the checklist. Adding a rule to prioritize indirect-response models led five of six runs to select indirect-response type I and narrowed recommendations to 400–600 mg. Revising bioavailability-estimation rules reduced the between-platform clearance difference from 30% to 10.5%.

The rules were adjusted on the same synthetic scenario with known truth, without evaluation on other scenarios. Even after revision, EC50/IC50 varied approximately fivefold, 0.56–2.80 mg/L. Limitations include one synthetic scenario, N=3 per platform, confounding between model and harness, and review by four experts from the development team. A representative run took approximately four hours and cost about US$70 in API use.

## Discussion

**Success is not a common endpoint.** Executable code, convergence, agreement with an expert model and stable decisions are different standards. Decision stability is closest to pharmacological use, but it was assessed in only one synthetic scenario.

**Run-to-run differences matter.** PKGPT warfarin OFVs ranged approximately 484–1621, while the tutorial initially selected four PD structures. Three runs cannot precisely estimate variability. Some datasets, such as theophylline, were more stable; a forward-only workflow can also contribute. A selected best run or average hides structural variability. Repeated runs under identical conditions are needed to characterize it.

**Self-checks leave unexamined decisions.** PKGPT exposed some failures through convergence and covariance diagnostics. The tutorial passed self-checks despite differing PD structures. These are different failures, but both separate reported checks from validity. In my [warfarin skill-library experiment](agent-pkpd-skills-en.html), code inspection found an ineffective lag specification and cross-validation refits stuck at their initial values. Different LLMs, software and workflows prevent combining these studies into a single score.

**Benchmarking remains incomplete.** Ponce-Bobadilla et al. identify inconsistent metrics, mixed synthetic and real data, discrepancies between papers and implementations, and differing evaluation conventions: held-out evaluation is common in ML, while same-data diagnostics dominate NLME. They propose held-out evaluation across methods and public benchmark datasets. Sale and Zhao's PAGE 2025 proposal describes an annual blinded benchmark with up to three datasets, a public search space and six months ([10](#ref-10)). The ISoP AI/ML SIG at PAGE 2026 prioritizes benchmark data ([11](#ref-11)). Neither initiative specifically evaluates LLM agents.

## Software and engineering descriptions

The BSD-3-licensed R package nlmixr2llm supplies nlmixr2 knowledge through Claude Code or Codex plugins. K-Dense Scientific Agent Skills includes `pkpd-modeling` ([12](#ref-12)). Anthropic's October 2025 engineering article describes skills as folders containing SKILL.md, recommends trusted sources and begins with evaluation ([13](#ref-13)). Within the material I read, nlmixr2llm's README provided no validation guidance and the K-Dense paper abstract no task-level evaluation. This is an impression from README and abstract inspection, not an audit of complete repositories. Deployment components appear ahead of evaluation components.

## Running an analysis is not validating it

The reviewed sources use different meanings of success. Execution, movement of estimates, correct model specification and held-out prediction are separate findings. The best report alone cannot establish reproducible structural choices.

This survey is not an experiment validating an operational procedure or skill. Self-verification is not equivalent to independent human review. The evidence does not support reducing all reported performance to a single decision that complete analyses can be delegated.

## Reading limitations

- Full texts were read for PKGPT, the context-engineering tutorial, Zheng, Richardson, Ponce-Bobadilla and Anthropic. Only abstracts were read for Shin, Cloesmeijer, Cha 2025 ([14](#ref-14)) and Mao 2025; nlmixr2llm and K-Dense were checked through README or overview material.
- PKGPT and tutorial results are transcribed, not reproduced. Developers evaluated their own systems.
- X and Reddit were inaccessible. Product material, including Certara's workshop listing ([15](#ref-15)), was inspected only as an announcement, not a performance demonstration.
- FDA/EMA AI principles and ICH M15 were outside scope.

The [source inventory](shared/pmx-ai-agents-landscape/sources.md) records reading scope. This article introduces no independent analysis dataset or code.

## References {#article-references}

1. <span id="ref-1"></span>Mao B, Gao Y, Xu C, Macha S, Shao S, Ahamadi M. Opportunities for AI-based Model-informed Drug Development: A Comparative Analysis of NONMEM and AI-based Models for Population Pharmacokinetic Prediction. The AAPS Journal. 2026;28(1):21. [doi:10.1208/s12248-025-01121-x](https://doi.org/10.1208/s12248-025-01121-x).
2. <span id="ref-2"></span>Richardson S, Irurzun Arana I, Nowojewski A, Zhou D, Leander J, Tang W, et al. A machine learning approach to population pharmacokinetic modelling automation. Communications Medicine. 2025;5(1):327. [doi:10.1038/s43856-025-01054-8](https://doi.org/10.1038/s43856-025-01054-8).
3. <span id="ref-3"></span>Zheng W, Wang W, Kirkpatrick CMJ, Landersdorfer CB, Yao H, Zhou J. AI for NONMEM Coding in Pharmacometrics Research and Education: Shortcut or Pitfall? CPT: Pharmacometrics & Systems Pharmacology. 2025;14(12):1965-1969. [doi:10.1002/psp4.70125](https://doi.org/10.1002/psp4.70125).
4. <span id="ref-4"></span>Kwack H, Kong H, Lim J, Zhang BT, Hahn J, Chang MJ. PKGPT: Expert-Orchestrated Recursive LLM Agent for Automated NONMEM PopPK Modeling with Human Benchmarking. Pharmaceutics. 2026;18(4):501. [doi:10.3390/pharmaceutics18040501](https://doi.org/10.3390/pharmaceutics18040501).
5. <span id="ref-5"></span>Pritchard‐Bell A, Lin CW, Holmes W, Doshi S. Context Engineering for AI ‐Assisted Pharmacometrics: A Practical Tutorial. CPT: Pharmacometrics & Systems Pharmacology. 2026;15(8):e70317. [doi:10.1002/psp4.70317](https://doi.org/10.1002/psp4.70317).
6. <span id="ref-6"></span>Ponce‐Bobadilla AV, Bräm D, Farnoud A, Fröhlich H, Janssen A, Korsbo N, et al. Predictive AI in Clinical Pharmacology: A Call to Action to Develop Robust Benchmarking Practices. CPT: Pharmacometrics & Systems Pharmacology. 2026;15(1):e70155. [doi:10.1002/psp4.70155](https://doi.org/10.1002/psp4.70155).
7. <span id="ref-7"></span>Fidler M and contributors. nlmixr2llm [software]. [Repository](https://github.com/mattfidler/nlmixr2llm). README consulted.
8. <span id="ref-8"></span>Shin E, Yu Y, Bies RR, Ramanathan M. Evaluation of ChatGPT and Gemini large language models for pharmacometrics with NONMEM. Journal of Pharmacokinetics and Pharmacodynamics. 2024;51(3):187-197. [doi:10.1007/s10928-024-09921-y](https://doi.org/10.1007/s10928-024-09921-y).
9. <span id="ref-9"></span>Cloesmeijer ME, Janssen A, Koopman SF, Cnossen MH, Mathôt RAA, for the SYMPHONY consortium. ChatGPT in pharmacometrics? Potential opportunities and limitations. British Journal of Clinical Pharmacology. 2024;90(1):360-365. [doi:10.1111/bcp.15895](https://doi.org/10.1111/bcp.15895).
10. <span id="ref-10"></span>Sale M, Zhao L. Announcement of Machine Learning Benchmarking. PAGE 2025; abstract 11658. [Abstract](https://www.page-meeting.org/Abstracts/announcement-of-machine-learning-benchmarking/).
11. <span id="ref-11"></span>Raimúndez E, Ponce-Bobadilla AV, Stodtmann S, Knöchel J. Shaping the future of AI/ML in pharmacometrics through collaboration, education and best practices. PAGE 2026; abstract 11999. [Abstract](https://www.page-meeting.org/Abstracts/shaping-the-future-of-ai-ml-in-pharmacometrics-through-collaboration-education-and-best-practices/).
12. <span id="ref-12"></span>K-Dense. Scientific Agent Skills [software and preprint]. 2026. [Repository](https://github.com/K-Dense-AI/scientific-agent-skills); [arXiv:2609.00065](https://arxiv.org/abs/2609.00065). README and abstract consulted.
13. <span id="ref-13"></span>Anthropic. Equipping agents for the real world with Agent Skills. Anthropic Engineering. 2025 Oct 16. [Article](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
14. <span id="ref-14"></span>Cha HJ, Choe K, Shin E, Ramanathan M, Han S. Leveraging large language models in pharmacometrics: evaluation of NONMEM output interpretation and simulation capabilities. Journal of Pharmacokinetics and Pharmacodynamics. 2025;52(3):34. [doi:10.1007/s10928-025-09982-7](https://doi.org/10.1007/s10928-025-09982-7).
15. <span id="ref-15"></span>Certara. ACoP 2026. [Event page](https://www.certara.com/conference/acop/). Announcement only; performance not evaluated.
