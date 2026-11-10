Predicting activity from a small set of experimental measurements could help narrow the compounds tested in drug discovery. The November 6, 2026 MIT News article about CheMeleon foregrounded prediction from scant data [(1)](#ref-1). But that description alone does not tell us whether the advantage is large enough to replace a classical method.

I reanalyzed the authors' released results for 30 MoleculeACE tasks. CheMeleon had, on average, 5.0% lower error than the published random forest (RF). Among the 15 tasks with at most 1,000 compounds in the training pool, the reduction was 1.9%, with a 95% interval including no improvement. Its improvement on activity cliffs was also smaller than on noncliff compounds.

This does not refute CheMeleon. It shows how the size and interpretation of its advantage change with the comparator and evaluation population.

## Scope and sources

CheMeleon learns molecular representations by pretraining to predict computed molecular descriptors, then fine-tunes them on experimental properties. The formal paper appeared in the Journal of Chemical Information and Modeling in 2026 [(2)](#ref-2). I verified its bibliographic information but could not access the publisher's full text. The methodological assessment therefore uses arXiv v2, dated February 9, 2026, and the code and results at a pinned repository commit. I have not established that every method is identical to the version of record [(3)](#ref-3) [(4)](#ref-4).

The reported win rate needs care. In arXiv v2, both the model with the best mean performance and models for which a Tukey multiple comparison detects no difference from that best model receive a win. The Polaris result is 21/28, or 75%; the MoleculeACE result is 29/30, about 97%, under this definition. These are neither exclusive first-place rates nor probabilities of beating RF. Failure to detect a difference does not establish equivalence [(3)](#ref-3).

My question is not whether that win count can be reproduced. It is how much error differs from RF on the same tasks, and how that comparison changes for cliffs and training-pool sizes. Because Polaris mixes endpoints and evaluation metrics, I chose the 30 activity-regression tasks in MoleculeACE for the primary analysis.

## Methods

### Read five repetitions on fixed test sets

Inputs were the released CheMeleon.md, RF.md and Chemprop.md results and the cliff-subgroup CSV. Each task has five seeds: 42, 117, 709, 1701 and 9001. The three primary models contribute 450 runs. I checked model–task–seed keys for duplicates and missing values. I did not retrain models or rerun molecule-level inference [(4)](#ref-4).

The inspected code retains fixed test membership. Seeds change training randomness, early-stopping splits or related procedures; they do not independently sample five new sets of unseen compounds. The 150 runs per model are therefore not 150 independent tasks. Where the figure caption's five-fold wording conflicts with the fixed-split implementation, this analysis is defined by the inspected code and released result files.

Activity cliffs are regions where small structural differences accompany large activity changes. I reused the cliff_mol labels and train/test columns in the pinned MoleculeACE CSVs, without regenerating cliff labels or creating new splits [(5)](#ref-5). Training size in Table 1 is the released training pool before its division into fitting and early-stopping subsets during fine-tuning.

Table 1. Analysis population. Repetitions are not added to the task count.

| Item | Scope |
| --- | --- |
| Tasks | 30 MoleculeACE endpoints |
| Seed runs per task and model | 5 |
| Primary models | CheMeleon, published RF, Chemprop |
| Training-pool compounds | 489–2,924 |
| Tasks with at most 1,000 training-pool compounds | 15 |
| Test split | Fixed published split |

The repository also contains distinct RF_Morgan and RF_Mordred results. I could not fully establish the mapping between the feature configuration described in the paper and the execution history of each RF file. The primary comparator is consequently the result labeled RF in the release; other RF results are sensitivity analyses. This is not a claim of superiority over every optimally tuned random forest.

### Aggregate errors in the right order

The metric is root mean squared error (RMSE), using activity on the logarithmic scale in the released CSVs. Reconstructing overall error from cliff and noncliff errors requires averaging squared errors, not RMSE itself. For subgroup counts n and subgroup RMSE values R, each run's overall value is

$$
R_{\mathrm{total}}=\sqrt{\frac{n_{\mathrm{cliff}}R_{\mathrm{cliff}}^2+n_{\mathrm{noncliff}}R_{\mathrm{noncliff}}^2}{n_{\mathrm{cliff}}+n_{\mathrm{noncliff}}}}.
$$

This matched the overall RMSE displayed in the released Markdown within rounding precision. Subgroup scores also matched the authors' plot-input CSV.

I then averaged the five runs' RMSE for model m on task t, denoting it by \(\bar R_{m,t}\), and formed the CheMeleon/RF ratio. The summary G is the geometric mean of these task ratios:

$$
G=\exp\left[\frac{1}{30}\sum_{t=1}^{30}\log\left(\frac{\bar R_{\mathrm{CheMeleon},t}}{\bar R_{\mathrm{RF},t}}\right)\right].
$$

G below one favors CheMeleon. Each task receives equal weight rather than allowing the largest datasets to dominate. Relative reduction is 100(1−G)%. It is not a pooled molecule-level error reduction or an experimental success rate.

Intervals use 10,000 task-bootstrap draws and the 2.5th and 97.5th percentiles. A task's models, subgroups and runs remain together, with the same draws for paired comparisons. This is an exploratory assessment of variation across released benchmark tasks, not validation on a random sample of future drug-discovery projects.

## Results

### The gain over RF is smaller than the gain over Chemprop

Table 2 reports the comparison with RF.

Table 2. Equal-task error ratios and counts of tasks with lower mean CheMeleon RMSE.

| Evaluation subset | Geometric RMSE ratio | 95% task-bootstrap interval | Relative reduction | Lower mean RMSE tasks |
| --- | ---: | ---: | ---: | ---: |
| Total | 0.950 | 0.927–0.972 | 5.0% | 23/30 |
| Cliff | 0.969 | 0.943–0.995 | 3.1% | 19/30 |
| Noncliff | 0.933 | 0.905–0.961 | 6.7% | 24/30 |

CheMeleon had lower overall mean error on 23 tasks and higher error on seven. This does not contradict the original 29/30 win count: the definitions differ. Table 2 counts strict differences between means, not task-level statistical significance.

![Task-level RMSE ratios against the published RF baseline](shared/chemeleon-low-data/task-ratios.png)

Figure 1. Task-level error ratios computed from released results. RMSE denotes root mean squared error and RF the published RF label. Values left of one favor CheMeleon; each point is a ratio of five-run means. The CHEMBL prefix is omitted from task labels. The original cliff comparison is in [Figure 3 of arXiv v2](https://arxiv.org/html/2506.15792v2#S1.F3). This is a new aggregation with a different metric, not a reproduced figure [(3)](#ref-3) [(4)](#ref-4).

Against the released Chemprop, the overall ratio was 0.800, with a 95% interval of 0.779–0.822, and mean error was lower on all 30 tasks. The gain from the nonpretrained comparator is substantial. Treating that number as the gain over RF, however, would exaggerate the latter advantage. The comparator changes what “stronger” means.

Sensitivity analyses gave overall ratios of 0.961 against RF_Morgan and 0.908 against RF_Mordred. The direction persisted, but the cliff-only comparison with RF_Morgan was 0.975, with a 95% interval of 0.942–1.009. The small cliff advantage is sensitive to the choice of RF comparator.

### Cliff improvements are smaller than noncliff improvements

Beating RF on cliffs does not mean removing the cliff difficulty. CheMeleon's cliff RMSE exceeded its noncliff RMSE on 29 of 30 tasks. The mean task-level gap was 0.151 log-activity units, with a 95% interval of 0.112–0.192.

Nor was improvement over RF concentrated on cliffs. Within each task I divided the cliff error ratio by the noncliff error ratio; their geometric mean was 1.038, with a 95% interval of 1.007–1.071. A value above one means that, in these fixed data, relative improvement over RF was smaller on cliffs. It does not mean CheMeleon increased cliff error. Its advantage over RF was smaller there than on noncliff compounds.

### A smaller gap with at most 1,000 training compounds

![Aggregate error ratios and training-pool sizes](shared/chemeleon-low-data/aggregate-size.png)

Figure 2. Left: Table 2's error ratios and 95% task-bootstrap intervals. Right: training-pool size versus overall error ratio, with each point representing a different task. The right panel is not a learning curve obtained by varying training size within the same task.

For the 15 tasks with at most 1,000 training-pool compounds, the overall ratio was 0.981, with a 95% interval of 0.955–1.008. For the 15 larger tasks it was 0.919, with an interval of 0.889–0.949. Within this collection, the advantage over RF was not uniformly greatest on the smallest-data side.

This does not establish that more data cause a larger CheMeleon advantage. Targets, activity distributions, chemical series and task difficulty change at the same time. The 1,000-compound cutoff is an exploratory low-data stratification. Neither performance with only tens of examples nor the fraction of experiments that could be avoided was measured.

## Discussion and limitations

Leaving out one task at a time kept the overall RF ratio between 0.946 and 0.956. Combining the two endpoints sharing one CHEMBL number and reweighting the resulting 29 groups equally gave 0.949. The direction was not driven by a single task.

Tasks are nevertheless not fully independent. Shared compounds, targets and assay similarities are not fully captured by grouping endpoint names. The intervals do not guarantee performance on new targets, new scaffolds or future temporal splits. Molecule-level predictions and error distributions were not inputs, so I did not separate measurement error, assess calibration or estimate success among top-ranked experimental candidates.

The comparison is also limited to the authors' released training conditions. I did not retrain under matched compute, retune RF, or isolate model-size and pretraining contributions. Nor did I newly certify the original statistical win counts.

CheMeleon showed a large improvement over released Chemprop and a smaller average improvement over released RF. That advantage weakened among the smaller training pools and on activity cliffs. Evaluating a low-data adoption claim therefore depends on comparison with RF and the relevant compound population. The reanalysis supports conditional predictive gains; it does not establish an experiment-reduction rate or a solution to activity cliffs.

## Data and code availability

Inputs were taken from the [pinned author repository](https://github.com/JacksonBurns/chemeleon/tree/b5e5bd88a7070c3f278e7e65e85b792617bf125c) and [pinned MoleculeACE CSVs](https://github.com/molML/MoleculeACE/tree/7e6de0bd2968c56589c580f2a397f01c531ede26/MoleculeACE/Data/benchmark_data). The [analysis code](shared/chemeleon-low-data/analysis.py), [aggregate results](shared/chemeleon-low-data/results.json) and [reproduction instructions](shared/chemeleon-low-data/analysis-readme.md) are available. Inputs are verified by SHA256; the seed is 20261110 and the bootstrap uses 10,000 draws. Original molecular data and third-party code are not bundled in the ZIP; inputs are retrieved from fixed URLs.

[Download code, results and figures](shared/chemeleon-low-data/chemeleon-low-data.zip)

## References

<a id="ref-1"></a>
1. Chandler DL. How to predict the behavior of molecules from scant data [Internet]. MIT News; 2026 Nov 6 [cited 2026 Nov 11]. [Article](https://news.mit.edu/2026/how-to-predict-molecule-behavior-with-scant-data-1106).

<a id="ref-2"></a>
2. Burns JW, Zalte AS, Abreu CRA, Sieg J, Feldmann C, Mathea M, et al. Deep Learning Foundation Models for Low-Data Regimes from Classical Molecular Descriptors. Journal of Chemical Information and Modeling. 2026;66(17):10692–10701. [doi:10.1021/acs.jcim.6c01546](https://doi.org/10.1021/acs.jcim.6c01546).

<a id="ref-3"></a>
3. Burns JW, Zalte AS, Abreu CRA, Sieg J, Feldmann C, Mathea M, et al. Deep Learning Foundation Models from Classical Molecular Descriptors [Preprint]. arXiv; 2026. Version 2, February 9, 2026. [arXiv:2506.15792v2](https://arxiv.org/html/2506.15792v2).

<a id="ref-4"></a>
4. CheMeleon contributors. CheMeleon [Software and benchmark results]. GitHub. Snapshot b5e5bd88a7070c3f278e7e65e85b792617bf125c [cited 2026 Nov 11]. [Repository](https://github.com/JacksonBurns/chemeleon/tree/b5e5bd88a7070c3f278e7e65e85b792617bf125c).

<a id="ref-5"></a>
5. MoleculeACE contributors. MoleculeACE benchmark data [Dataset]. GitHub. Snapshot 7e6de0bd2968c56589c580f2a397f01c531ede26 [cited 2026 Nov 11]. [Benchmark tables](https://github.com/molML/MoleculeACE/tree/7e6de0bd2968c56589c580f2a397f01c531ede26/MoleculeACE/Data/benchmark_data).
