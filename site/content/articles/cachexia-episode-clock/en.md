“A blood signal appears before weight loss” sounds useful for early intervention. But “before” depends on the clock: the last stable measurement, first crossing of a loss threshold, and retrospectively identified start of a loss interval are different dates.

Castillon and colleagues' cancer-cachexia atlas treats weight loss as potentially recurrent episodes in records from 52,236 patients. It was published on October 12, 2026 ([1](#ref-1)), and the journal also [featured it on X](https://x.com/NatureMedicine/status/2111057370008940965). I examined the released episode table and detection code. The table does not contain longitudinal blood measurements; this analysis first establishes what its time variables mean rather than claiming to predict a prodrome.

## One cachexia label per patient is insufficient

The paper links approximately 1.7 million longitudinal body mass index (BMI) measurements with laboratory and tumor information in adults who underwent MSK-IMPACT (the Memorial Sloan Kettering tumor gene-panel test). Eligibility requires adequate weight records and follow-up; this is not an unselected population of all cancer patients ([original Methods](https://www.nature.com/articles/s41591-026-04689-9), [1](#ref-1)).

The basic criterion is at least 5% loss within 180 days, or at least 2% when starting smoothed BMI is below 20. The authors smooth BMI, detect eligible candidate intervals, merge overlaps, and perform quality control including apparent losses following transient gains such as edema. These are weight-defined episodes, not measurements of muscle, metabolic dysfunction, or physical function. An episode ending does not mean the underlying syndrome is cured.

The [public CSV and dictionary](https://doi.org/10.5281/zenodo.22045313) contain 58,817 rows ([2](#ref-2)). Patients with episodes may have multiple rows; patients without an episode have one nonepisode row.

**Table 1.** Patients and intervals in the public episode table.

| Aggregate | Result |
| --- | ---: |
| Unique patients | 52,236 |
| Patients with episodes | 24,357 (46.63%) |
| Episodes | 30,938 |
| Patients with at least 2 episodes | 5,496 |
| Fraction with at least 2 episodes among affected patients | 22.56% |

Patient proportions count each person once. Episode-duration summaries instead count intervals, not patient-average durations. Treating 30,938 episodes as that many patients would repeatedly count recurrent cases.

## The code separates interval start from threshold crossing

The dictionary defines `start_day` as the reference for a 180-day window. The pinned [detection README](https://github.com/reznik-lab/cachexia/blob/5d63b83a7ca3915949d4a0131e8b0c7ec52f8903/episode_identification/README.md) explicitly searches forward from each reference day ([3](#ref-3)). The code separately defines `onset_day`, the first threshold crossing.

Looking ahead is legitimate when defining retrospective intervals. Interpreting the reference day as the day when cachexia could already have been detected changes the use. Consider an illustrative record, not an actual patient:

**Table 2.** Hypothetical weights illustrating information available on each day.

| Day | Weight | Information available by then |
| ---: | ---: | --- |
| 0 | 70.0 kg | Candidate reference measurement |
| 30 | 69.0 kg | From day 0, approximately 1.4% loss |
| 90 | 66.0 kg | From day 0, approximately 5.7% loss |

Using raw measurements in this simple example, loss of at least 5% from day 0 becomes known on day 90. The three-point example does not reproduce the original smoothing and merging procedure. The released episode table lacks `onset_day`: it contains start, nadir, and end, but cannot reconstruct first threshold crossing. Start-to-nadir duration therefore cannot be called detection delay or an intervention window.

## A 180-day detection window can produce longer episodes

Among 30,938 episodes, median start-to-nadir duration is 196 days, with interquartile range 147–273; median start-to-end duration is 212 days. This is compatible with a 180-day search window because overlapping candidates merge into longer intervals.

![Durations calculated from the public episode table](shared/cachexia-episode-clock/figures/episode-clock-distributions.png)

**Figure 1.** Author's calculation from the public episode table: left, reference-day to minimum-BMI duration; right, maximum minus end-of-interval percentage loss. These retrospective quantities do not measure prospective detection time or intervention opportunity.

Nadir precedes end in 11,685 intervals, or 37.77%. Weight can partially recover while merged candidate windows still meet criteria, so end need not coincide with the minimum.

## End weight defines a different event

All 30,938 maximum-loss values meet their applicable thresholds. Using start-to-end loss alone instead places 1,376 episodes, 4.45%, below threshold.

![Maximum loss versus end-of-interval loss](shared/cachexia-episode-clock/figures/end-versus-maximum-loss.png)

**Figure 2.** Author's comparison of two released summary values, retaining the 2% threshold below starting BMI 20 and 5% otherwise. It does not rerun episode detection.

**Table 3.** Starting-BMI-specific thresholds and end-of-interval classifications.

| Starting smoothed BMI | Applicable loss threshold | Episodes | End loss below applicable threshold |
| --- | ---: | ---: | ---: |
| Below 20 | 2% | 2,692 | 140 |
| At least 20 | 5% | 28,246 | 1,236 |

Applying only “end loss below 5%” yields 2,915 intervals, including those originally assigned the 2% criterion. That would overstate missed episodes. This discrepancy does not establish an algorithmic defect: maximum loss within an interval and its final state describe different quantities.

One row ends beyond its recorded observation/survival duration. I retained all rows in the main descriptive summary and checked exclusion sensitivity without inventing a corrected date or using the row for survival analysis. Details are recorded in the distributed archive.

## Blood associations differ from predicting future loss

The paper examines blood features during episodes and tumor-genomic associations. Differences within episodes do not establish anticipation of future loss ([1](#ref-1)). Its risk models address one-, two-, and three-year postdiagnosis horizons; external evaluation uses a reduced lung-adenocarcinoma model restricted to shared variables ([1](#ref-1)). That differs from sequential blood-based forecasting of imminent loss. I neither retrain those models nor test blood-signal lead times.

Future nadir and interval end are unavailable before the interval ends. Information allowed in retrospective labels differs from information available to a predictor on a particular day. An unmeasured blood value is not a normal one, and an absence of weight records does not show that loss stopped. Observation frequency and censoring can mix biological change with changes in opportunities for clinical recording. Even 30,938 episodes do not resolve what was known on each day.

## Data and code availability

The [code, aggregate inputs, outputs, and figures](shared/cachexia-episode-clock/cachexia-episode-clock.zip) document denominators, thresholds, durations, and exclusion sensitivity. Patient identifiers and individual episode records are excluded; acquisition/aggregation scripts and sources are provided. Original figures and implementation are not redistributed.

```sh
python -m pip install -r requirements.txt
python analysis.py
python -m unittest test_analysis.py
python plot.py
```

Sources were checked on October 18, 2026: the original paper ([1](#ref-1)), the released table and dictionary ([2](#ref-2)), and the detection README at the pinned commit ([3](#ref-3)).

## References

1. <span id="ref-1"></span>Castillon VJ, Xie AX, Boscenco S, Tse E, Ruthen N, Wang J, et al. A health-system-scale, episode-resolved multimodal atlas of cancer cachexia. Nat Med. 2026. [doi:10.1038/s41591-026-04689-9](https://doi.org/10.1038/s41591-026-04689-9). Published online 2026 Oct 12.

2. <span id="ref-2"></span>Reznik E, Castillon VJ. A health-system-scale, episode-resolved multimodal atlas of cancer cachexia [dataset]. Zenodo. 2026. [doi:10.5281/zenodo.22045313](https://doi.org/10.5281/zenodo.22045313).

3. <span id="ref-3"></span>Reznik Laboratory. Cancer cachexia episode identification [source code]. Commit 5d63b83a7ca3915949d4a0131e8b0c7ec52f8903. [Detection-code README](https://github.com/reznik-lab/cachexia/blob/5d63b83a7ca3915949d4a0131e8b0c7ec52f8903/episode_identification/README.md).
