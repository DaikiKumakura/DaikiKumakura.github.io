A study of resistance after daraxonrasib detected acquired mutant KRAS amplification in 16 of 44 patients with paired pretreatment and progression circulating tumour DNA (ctDNA). These patients had RAS-mutant metastatic pancreatic ductal adenocarcinoma, received 160–300 mg/day of single-agent daraxonrasib as second- or later-line treatment in a single-arm phase 1/2 study, and had progression-free survival longer than three months before subsequent progression. [Figure 1 of the paper](https://www.nature.com/articles/s41591-026-04537-w/figures/1) describes the patients profiled under those conditions ([1](#ref-1)). Planning repeat blood collection raises the question of which population the 36% can describe.

## Different populations can produce the same 36%

Let $p$ be the fraction that would test positive for acquired KRAS amplification if everyone with the same eligible progression history could be evaluated using a common assay. Let $s_1,s_0$ be the probabilities that positive and negative cases enter the paired analysis. The observed fraction is $q=ps_1/[ps_1+(1-p)s_0]$. Given $r=s_1/s_0$, the target fraction is $p=q/[q+r(1-q)]$. I held $q$ at $16/44$ and varied the ratio.

**Table 1.** Positive fraction as the relative probability of inclusion changes.

| Inclusion probability ratio | Target positive fraction |
| ---: | ---: |
| 0.5 | 53.3% |
| 1.0 | 36.4% |
| 2.0 | 22.2% |

The 22.2–53.3% range in Table 1 is a set of selection scenarios. Timing, ctDNA shedding, follow-up at progression and sample quality can affect evaluability. These data do not estimate $r$. The calculation neither extrapolates to early progression nor corrects assay sensitivity or discordance across tissues. A design that targets the eligible progression population needs a patient flow for cases who were eligible but did not enter the paired analysis.

## Data and code availability

The [reproducibility ZIP](shared/daraxonrasib-resistance-sampling/companion.zip) contains the Python code and output.

## References

1. <a id="ref-1"></a> [Aronchik I, Kar S, Zhuang Y, Ahler E, Lai LP, Seshadri V, et al. Acquired resistance to the RAS(ON) multi-selective inhibitor daraxonrasib guides rational combination therapy strategies in pancreatic cancer. Nat Med. 2026;32:2865–2877.](https://doi.org/10.1038/s41591-026-04537-w)
