In October 2026, Roche and Hansoh announced their second antibody-drug conjugate (ADC) collaboration. The press headline read "more than $15 billion." Hansoh, however, receives $400 million at signing and a further $110 million at the first anniversary. The remaining roughly $15 billion consists of development, regulatory and sales milestones ([1](#ref-1)).

Pharmaceutical deal headlines usually state a total that adds the upfront payment and the milestones. Contingent payments are sometimes called "biobucks" in industry writing ([2](#ref-2)). What is fixed at signing is the upfront payment; most of the headline total is contingent. This article counts how much of the headline total the upfront payment accounts for in 18 publicly reported deals.

**Reference date:** The facts and numbers in this article reflect public information as of October 30, 2026. Updates to contract terms after the publication date are not reflected. The bibliographic details of the cited sources were checked on October 31, 2026.

## Abstract

**Problem:** What share of the headline total is the upfront payment? Do AI-discovery deals differ from the others?

**Methods:** I collected upfront payments and headline totals by hand from public information for 18 deals, mostly from September–October 2026, and calculated the share (upfront ÷ headline total) for the 15 deals in which the upfront payment was disclosed. Of the 18 deals, I could check the announcement document itself for five.

**Main results:** The upfront payment was a median 4.1% of the headline total (interquartile range, IQR, 3.3–7.6%; range 2.5–18.8%). Pooled over the 15 deals, the upfront payments were $3,255 million of $65,661 million in headline totals (5.0%). The five AI-discovery deals had a median of 3.0% and the other ten 6.1%; this is an exploratory comparison. The definition of "upfront" differs between deals, and the choice of definition moved the share by up to about 2.2-fold. No relation between headline size and share could be detected in these 15 deals.

**Conclusion:** In this sample the upfront payment is a few percent of the headline total. The sample is biased and does not serve as a benchmark for deals in general. The figures do not predict the value or eventual success of any individual deal.

## Introduction

The aim is a reference value for reading the headline total of a deal report as a part fixed at signing and a contingent part. Because the sample is biased, the shares obtained here cannot serve as a benchmark for deals in general. They are not used to evaluate an individual deal or for investment decisions.

## Methods

### Data

I collected 18 deals: 11 from September–October 2026, five from January–May 2026 and two from January 2024 (the two Isomorphic Labs deals). Shares were calculated for the 15 deals in which both the upfront payment and the headline total were disclosed. Three deals without a disclosed upfront payment (Lilly–Gate, AI Proteins–Astellas, Roche–Rona) were excluded because no share can be calculated. Deal names, dates, amounts, definitions, source URLs and source types are recorded in `deals.csv` (included in the [companion archive](shared/biobucks-upfront-ratio/biobucks-upfront-ratio-companion.zip)).

The AI-discovery deals were Generate–Zealand, Insilico–Lilly, Insilico–Servier, Isomorphic–Lilly and Isomorphic–Novartis. I assigned this classification.

The quality of sources differs between deals. On October 31, 2026, I read the announcement documents themselves for five deals and confirmed that the amounts agree with `deals.csv`: Merck–SciBrunch ([3](#ref-3)), Novo Nordisk–Hengrui ([4](#ref-4)), Genentech–Alector (Alector's Form 8-K filing) ([5](#ref-5)), Gilead–Vir ([6](#ref-6)) and Servier–Insilico ([7](#ref-7)). The Generate–Zealand release ([8](#ref-8)) could not be read in full that day because the page returned HTTP 403; I could only see that the amounts agree with summaries of other reports. For Roche–Hansoh I read a news report ([1](#ref-1)) and confirmed the upfront payment, the payment at the first anniversary and the "more than $15 billion" statement. The remaining 12 deals rely on the news reports and newsletters recorded in `deals.csv`, and I did not check the primary documents. The `verified_level` column of `deals.csv` records the level of checking (read_full, press_read, press_only). No paid deal database was used.

Selection is biased. I collected the deals mainly from those for which both the upfront payment and the total were reported, and I did not measure what was missed. Small deals and deals with undisclosed terms are less likely to be included.

### Definitions and analysis

- **Headline total:** The amount in the press headline, taken as the sum of the upfront payment and the maximum milestones, excluding royalties. When a source gives the upfront payment and the milestones separately, I used their sum. For Roche–Hansoh I took $400 million upfront, $110 million at the first anniversary and more than $15 billion in milestones, giving $15,510 million. Because the milestones are "more than $15 billion," this is a lower bound.
- **Upfront share:** Upfront ÷ headline total. The upfront payment in the main definition is the amount the source calls the "upfront payment."
- **Alternative definition:** Some sources include near-term payments or early milestones in the upfront payment. For the four deals where such a value was found (Generate–Zealand, Gilead–Vir, BMS–Hengrui, Roche–Hansoh), I also recorded the alternative value.
- **Group comparisons:** I calculated medians and IQRs for AI discovery, seller country (Chinese companies) and headline total of $5 billion or more. The 95% interval of the median was obtained by bootstrap (2,000 resamples, seed 20261030). I used the two-sided Mann–Whitney U test for the difference between AI-discovery deals and the others, and Spearman rank correlation for the relation between headline total (logarithm) and share.
- **Crude risk adjustment:** I multiplied the full milestone amount by the Phase I-to-approval probability of 7.9% (all areas, 2011–2020) and calculated the upfront share as upfront ÷ (upfront + 0.079 × milestones). The 7.9% is the all-indications value in the report by the Biotechnology Innovation Organization, Informa Pharma Intelligence and QLS Advisors ([9](#ref-9), p. 10).

The analysis plan was not fixed before the calculations. I decided on the metric (upfront ÷ headline total) before collecting the deals, but I added the AI-discovery comparison, the sensitivity analysis on the definition of upfront, and the crude correction by approval probability after looking at the data (post hoc). The scope is recorded in `analysis-plan.md`.

## Results

### The upfront payment was 2.5–19% of the headline total, with a median of 4.1%

Figure 1 shows the share for the 15 deals with a disclosed upfront payment.

![Upfront share for 15 deals with disclosed upfront payments, sorted from low to high. Orange marks AI-discovery deals and blue the others. Open circles show values under the alternative definition and the dotted line the median of the 15 deals.](shared/biobucks-upfront-ratio/figures/01-upfront-share.png)

Figure 1. Upfront share (upfront ÷ headline total). The vertical axis lists deal names (headline total in $ million in parentheses) and the horizontal axis the upfront share (%). Filled circles use the main definition, open circles the alternative definition (four deals), and the dotted line the median of the 15 deals (4.1%). Orange: AI discovery; blue: others. n = 15. Source: `deals.csv`; drawn with `figures.py`.

Table 1. Summary of the upfront share by group.

| Group | n | Median (95% interval) | IQR | Range |
| --- | ---: | ---: | ---: | ---: |
| All deals with a disclosed upfront | 15 | 4.1% (3.6–7.9%) | 3.3–7.6% | 2.5–18.8% |
| AI-discovery deals | 5 | 3.0% (2.5–4.2%) | 2.6–3.6% | 2.5–4.2% |
| Other deals | 10 | 6.1% (4.0–9.7%) | 4.0–8.6% | 2.6–18.8% |
| Chinese seller | 7 | 7.4% (3.9–11.5%) | 4.0–10.2% | 2.6–18.8% |
| Non-Chinese seller | 8 | 3.8% (2.6–4.8%) | 2.9–4.3% | 2.5–7.9% |
| Headline total of $5 billion or more | 4 | 4.0% (2.6–7.4%) | 3.6–4.8% | 2.6–7.4% |
| Headline total below $5 billion | 11 | 4.2% (3.0–8.8%) | 3.3–8.3% | 2.5–18.8% |

Note: The 95% interval is the bootstrap interval of the median (2,000 resamples). In groups with fewer than 10 deals the interval is unstable; for the group of five it coincides with the range, and for the group of four it is only indicative. Source: `results/upfront-share-summary.csv`.

The lowest share was Generate–Zealand (2.5%; upfront $30 million, headline about $1.2 billion), followed by Isomorphic–Lilly (2.6%) and Roche–Hansoh (2.6%). The highest was Merck–SciBrunch (18.8%; upfront $400 million, headline $2.13 billion), followed by Novo–Hengrui (11.5%).

All five AI-discovery deals were at or below 4.2%. The difference between the AI-discovery deals and the other ten was p = 0.02 (0.0193) by the two-sided Mann–Whitney U test (no ties, exact method). This comparison was decided post hoc and no multiplicity correction was applied. The groupings in Table 1 (AI discovery, seller country, headline total) were also tried post hoc; the only tests run were the one above and the Spearman correlation. The five AI-discovery deals include platform-type collaborations and two deals from 2024. Period, development stage and counterparty could not be separated.

Deals with a Chinese seller had a higher median, 7.4%. The shares in this group are pushed up by Merck–SciBrunch (18.8%), Novo–Hengrui (11.5%) and Sanofi–Sino Biopharm (8.8%). Another Hengrui deal, BMS–Hengrui, is at the low end with 3.9%.

The Spearman rank correlation between the headline total (logarithm) and the share was 0.14 (p = 0.63); no relation could be detected in these 15 deals. The sample is small, and this is not evidence of no relation (power is insufficient).

Figure 2 plots the headline total on the horizontal axis and the upfront payment on the vertical axis, both on logarithmic scales.

![Log–log scatter plot of headline total against upfront payment. Dashed lines mark 2%, 5%, 10% and 20% of the headline total; 13 of the 15 deals fall between the 2% and 10% lines.](shared/biobucks-upfront-ratio/figures/02-upfront-vs-total.png)

Figure 2. Headline total and upfront payment. The horizontal axis is the headline total ($ million, logarithmic) and the vertical axis the upfront payment ($ million, logarithmic). Dashed lines mark upfront payments equal to 2%, 5%, 10% and 20% of the headline total. Orange: AI discovery; blue: others. n = 15. 13 of the 15 deals fall between the 2% and 10% lines. Source: `deals.csv`.

### The definition of upfront moves the share by up to 2.2-fold

The range covered by the "upfront payment" differs between sources. An alternative definition was found for four deals.

Table 2. Effect of the definition of the upfront payment on the share.

| Deal | Upfront (main definition) | Alternative definition | Headline total | Share (main → alternative) |
| --- | ---: | ---: | ---: | --- |
| Generate–Zealand | $30 million | $65 million (includes $35 million in early preclinical milestones) | about $1,200 million | 2.5% → 5.4% |
| Gilead–Vir | $90 million ($65 million cash, $25 million equity) | $135 million (includes up to $45 million in near-term preclinical milestones) | $1,870 million | 4.8% → 7.2% |
| BMS–Hengrui | $600 million | $950 million (includes near-term payments) | $15,200 million | 3.9% → 6.3% |
| Roche–Hansoh | $400 million | $510 million (includes the $110 million at the first anniversary) | $15,510 million or more | 2.6% → 3.3% |

Note: The 950/15,200 share for BMS–Hengrui is 6.25%, rounded half up to 6.3%. The cash/equity split and the composition of the $135 million for Gilead–Vir come from the announcement document ([6](#ref-6)). The first-anniversary payment for Roche–Hansoh comes from a news report ([1](#ref-1)). The Generate–Zealand values are based on summaries of reports because the release ([8](#ref-8)) could not be read. News reports describe the $950 million for BMS–Hengrui as the $600 million upfront plus a $175 million payment at the first anniversary and a contingent $175 million payment in a later year; I did not check this composition against a primary source. Shares were calculated from the values in `deals.csv`.

Under the alternative definitions, the median of all 15 deals rose from 4.1% to 5.4% (95% interval 3.6–7.4%). The largest ratio of the alternative to the main definition was about 2.2-fold (Generate–Zealand, 65/30).

Inconsistency in definition also remains on the main-definition side. The announcement for Insilico–Servier states "up to $32 million in upfront and near-term R&D payments" ([7](#ref-7)). The upfront payment alone is not disclosed. I treated the $32 million as the upfront payment in the main definition, although it is of the same nature as the values "including near-term payments" that I assigned to the alternative definition for other deals. The treatment is asymmetric, and the main-definition share for Servier (3.6%) overestimates the share of the upfront payment alone. The $45 million for Menarini–Georgiamune has the same nature: the company wording quoted in press reports is "$45 million in upfront and near-term payments," and I treated it as the main-definition upfront payment (share 4.1%). I did not correct this in the calculations. Because the upfront payment alone is unknown, I made an ad hoc check of the extreme case in which both upfront payments are set to zero. The median of the AI-discovery group fell from 3.0% to 2.6% and the median of the other group stayed at 6.1%, so the direction of AI discovery being lower did not change, but the p-value of the Mann–Whitney U test rose from 0.02 to 0.057. This check is not saved in the result files or the companion archive.

The treatment of equity also varies. For Gilead–Vir, part of the $90 million upfront payment ($25 million) is equity ([6](#ref-6)). Few announcements separate cash and equity. The definition of the headline total also differs between sources: some say "milestones only," some "including the upfront," and some do not state that royalties are excluded. I aligned all of them to the total including the upfront payment, but some deals with ambiguous source wording remain. For Gilead–Vir, summing the terms in the announcement gives 90 + 45 + 1,740 = $1,875 million. I used $1,870 million from a news report; the shares do not change at one decimal place (4.8% and 7.2%).

### The probability that the full milestone amount is paid is low

Most of the headline total is development, regulatory and sales milestones. The full milestone amount is paid when the program advances to approval, or to the achievement of post-approval sales.

As a crude calculation, multiplying the full milestone amount by the Phase I-to-approval probability of 7.9% ([9](#ref-9), p. 10) gives the upfront payment a median share of 35% (IQR 30–51%) of "upfront plus risk-adjusted milestones."

This calculation is crude. The 7.9% is an average over all areas and drugs, whereas the development stage differs between deals. Several factors act in different directions.

- For preclinical deals, the probability of approval is lower than 7.9%, which makes the expected milestone value smaller still. The upfront share would be larger than 35%.
- For late-stage (Phase II or later) deals, the probability is higher than 7.9% and the upfront share would be smaller than 35%.
- Milestones paid at early stages have a high probability. Discounting them by 7.9% underestimates the expected value and makes the upfront share look larger.

Because these factors act in different directions, I cannot say whether the calculation is too high or too low overall. The 35% is not an estimate of the value of an individual deal. It shows only that reading the headline total as value counts the contingent part (about 96% at the median) with the same weight as the upfront payment fixed at signing.

## Discussion

In this sample, the upfront payment was a few percent of the headline total. The median was 4.1% and the pooled share 5.0%, and 13 of the 15 deals fell within 2–10% (Figure 2). In the pooled data, about 95% of the headline total is not fixed at signing. A headline figure such as "$15 billion" states the upper limit if all conditions are met ([1](#ref-1)).

The low share in AI-discovery deals (all five at or below 4.2%) is an exploratory observation. Period, development stage and counterparty are mixed, and the result of p = 0.02 for five versus ten deals is an uncorrected post hoc comparison. It cannot be said that being an AI-discovery deal lowered the share.

Differences in definition directly affected the comparison of shares. Changing the definition moved the median of the 15 deals from 4.1% to 5.4% and individual deals by up to about 2.2-fold (Table 2). The same word "upfront" sometimes means only the payment at signing and sometimes includes early milestones or near-term payments. To compare shares, the definition of the upfront payment would have to be aligned across deals. The main definition in this article also retains inconsistency, as in the Servier and Menarini–Georgiamune cases.

No relation between the headline total and the share could be detected in 15 deals. The sample is small, and this is not evidence of no relation. The higher median for deals with Chinese sellers (7.4%) is the result of a few deals pushing it up. These data give no basis for attributing it to the licensing terms of Chinese companies.

## Limitations

- **Sample:** 18 deals (15 with a calculable share), biased toward deals whose upfront payment and total were disclosed. This is not the distribution of all deals. Three of the 18 had an undisclosed upfront payment, but that is a count within the sample and not a rate among deals in general. The comparison of AI-discovery deals with the others is exploratory.
- **Sources:** I could read the announcement documents for 5 of the 18 deals; the rest rely on news reports and newsletters (see "Data" under Methods). The numbers differ slightly between reports for some deals (for example, Lilly–Innovent). The values announced by the companies are transcribed as they are.
- **Dates:** The dates in `deals.csv` are those of reports, filings or announcement documents and may differ from the announcement date by about a day. For Sanofi–Sino Biopharm the date is that of the filing (March 3); some reports give the company release as March 4 local time. The analysis does not use dates.
- **Meaning of the headline total:** The headline total is the upper limit if all milestones are achieved. It is not the amount an individual deal will actually pay, the probability of success, or an estimate of value.
- **Risk adjustment:** The 7.9% is an average over all areas and drugs, and the 35% is a crude reference value.
- **Verification:** The recalculation in R is a separate implementation by the same author and is not third-party confirmation. It checked the counts, medians, IQRs, group medians, the pooled share and the median after risk adjustment, with a maximum difference of 3.0 × 10⁻⁶. The bootstrap intervals and the p-values of the Mann–Whitney U test and Spearman correlation were not verified in R. The article was written with an AI (Claude) and reviewed three times by AI reviewers commissioned by the same author; this is not confirmation by a human third party.

## Conclusion

In the sample of 15 deals with a disclosed upfront payment, the upfront payment was a median 4.1% of the headline total of a drug-discovery deal and 5.0% when pooled. 13 of the 15 deals fell within 2–10%, and most of the headline total is contingent payments not fixed at signing. All five AI-discovery deals were at or below 4.2%, a lower share on exploratory inspection. The definition of the "upfront payment" differs between deals, and the choice of definition moved the share by up to about 2.2-fold. No relation between headline size and share could be detected in 15 deals. Because the sample is biased and announcement documents were checked for only five deals, these values cannot be read as a benchmark for deals in general.

## Data and code availability

The input (`deals.csv`), the analysis plan, the analysis code (`analysis.py`, `test_analysis.py`, `figures.py`, `validate.R`), the results and the figures are included in the [companion archive](shared/biobucks-upfront-ratio/biobucks-upfront-ratio-companion.zip). To rerun, use `python test_analysis.py && python analysis.py && python figures.py && Rscript validate.R` (Python 3.12, numpy, pandas, scipy, matplotlib; R 4.5.3, jsonlite). The random seed is fixed at 20261030, and rerunning with the same seed reproduces the result files. The Mann–Whitney U test used the scipy default (the exact method, since there are no ties). The ad hoc check of the extreme case described under Results is not included in the result files or the companion archive. There are four unit checks: the median calculation, table consistency (the upfront payment is smaller than the total, the alternative definition is at least the main definition, and a source URL is present), and that the risk-adjusted share is larger than the original. The amounts transcribe the sources' statements and are not a database licensed for redistribution. The source type (company release, SEC filing, news report) is recorded in the `source_type` column.

## References

<span id="ref-1"></span>1. Philippidis A. Roche, Hansoh launch up-to-$15B+ cancer ADC collaboration [Internet]. GEN Genetic Engineering & Biotechnology News; 2026 Oct 20 [cited 2026 Oct 31]. Available from: [https://www.genengnews.com/topics/cancer/roche-hansoh-launch-up-to-15b-cancer-adc-collaboration/](https://www.genengnews.com/topics/cancer/roche-hansoh-launch-up-to-15b-cancer-adc-collaboration/)

<span id="ref-2"></span>2. Booth B. Hitting the milestones: update on earning "biobucks" [Internet]. LifeSci VC; 2016 Dec 8 [cited 2026 Oct 31]. Available from: [https://lifescivc.com/2016/12/hitting-milestones-update-earning-biobucks/](https://lifescivc.com/2016/12/hitting-milestones-update-earning-biobucks/). The author name is taken from the site's author profile; the page text carries no explicit byline.

<span id="ref-3"></span>3. Merck & Co., Inc. Merck enters into exclusive global license agreement with SciBrunch Therapeutics for SPR2015, an investigational oral KRAS G12D (ON) inhibitor [Internet]. Merck; 2026 Sep 28 [cited 2026 Oct 31]. Available from: [https://www.merck.com/news/merck-enters-into-exclusive-global-license-agreement-with-scibrunch-therapeutics-for-spr2015-an-investigational-oral-kras-g12d-on-inhibitor/](https://www.merck.com/news/merck-enters-into-exclusive-global-license-agreement-with-scibrunch-therapeutics-for-spr2015-an-investigational-oral-kras-g12d-on-inhibitor/)

<span id="ref-4"></span>4. Novo Nordisk. Novo and Hengrui Pharma enter exclusive license agreement for once-weekly oral GLP-1/GIP dual receptor agonist HRS-1596 [Internet]. Novo Nordisk; 2026 Sep 29 [cited 2026 Oct 31]. Available from: [https://www.novonordisk.com/news-and-media/news-and-ir-materials/news-details.html?id=917052](https://www.novonordisk.com/news-and-media/news-and-ir-materials/news-details.html?id=917052)

<span id="ref-5"></span>5. Alector, Inc. Form 8-K, current report (event date 2026 Sep 30; signed 2026 Oct 5) [Internet]. U.S. Securities and Exchange Commission [cited 2026 Oct 31]. Available from: [https://www.sec.gov/Archives/edgar/data/0001653087/000119312526413090/alec-20260930.htm](https://www.sec.gov/Archives/edgar/data/0001653087/000119312526413090/alec-20260930.htm)

<span id="ref-6"></span>6. Vir Biotechnology, Inc. Vir Biotechnology enters multi-program collaboration and license agreement with Gilead Sciences to discover and develop novel PRO-XTEN dual-masked T-cell engagers for solid tumors [Internet]. Vir Biotechnology; 2026 Oct 14 [cited 2026 Oct 31]. Available from: [https://s203.q4cdn.com/628578897/files/doc_news/Vir-Biotechnology-Enters-Multi-Program-Collaboration-and-License-Agreement-with-Gilead-Sciences-to-Discover-and-Develop-Novel-PRO-XTE-EY8Z3.pdf](https://s203.q4cdn.com/628578897/files/doc_news/Vir-Biotechnology-Enters-Multi-Program-Collaboration-and-License-Agreement-with-Gilead-Sciences-to-Discover-and-Develop-Novel-PRO-XTE-EY8Z3.pdf)

<span id="ref-7"></span>7. InSilico Medicine Cayman TopCo. Voluntary announcement on multi-year collaboration with Servier for drug discovery and development in oncology [Internet]. Hong Kong Exchanges and Clearing Limited; 2026 Jan 5 [cited 2026 Oct 31]. Available from: [https://www.hkexnews.hk/listedco/listconews/sehk/2026/0105/2026010500029.pdf](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0105/2026010500029.pdf)

<span id="ref-8"></span>8. Generate Biomedicines; Zealand Pharma. Generate Biomedicines and Zealand Pharma enter collaboration and license agreement to develop protein therapeutics engineered with AI for metabolic diseases [Internet]. GlobeNewswire; 2026 Oct 13 [cited 2026 Oct 31]. Available from: [https://www.globenewswire.com/news-release/2026/10/13/3380182/0/en/generate-biomedicines-and-zealand-pharma-enter-collaboration-and-license-agreement-to-develop-protein-therapeutics-engineered-with-ai-for-metabolic-diseases.html](https://www.globenewswire.com/news-release/2026/10/13/3380182/0/en/generate-biomedicines-and-zealand-pharma-enter-collaboration-and-license-agreement-to-develop-protein-therapeutics-engineered-with-ai-for-metabolic-diseases.html). The full text was not read: the page returned HTTP 403 on the cited date.

<span id="ref-9"></span>9. Biotechnology Innovation Organization; Informa Pharma Intelligence; QLS Advisors. Clinical development success rates and contributing factors 2011–2020 [Internet]. Biotechnology Innovation Organization; 2021 Feb [cited 2026 Oct 31]. Available from: [https://www.bio.org/clinical-development-success-rates-and-contributing-factors-2011-2020](https://www.bio.org/clinical-development-success-rates-and-contributing-factors-2011-2020). The 7.9% value (all indications, Phase I to approval) was checked on p. 10 of a PDF copy of the report hosted by CPHI Online.
