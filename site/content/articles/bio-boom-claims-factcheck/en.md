Lists of "bio boom" topics that put cancer, gene editing, obesity, AI-assisted drug discovery and xenotransplantation side by side tend to carry headlines in which the definition of the number is left out. This article takes ten such headlines and checks, against journal abstracts, company releases, FDA pages and trial registries, what quantity each number measures and at which regulatory or development stage each item stands. There are two questions. Of the ten items, how many of the eight that are drugs, vaccines or therapies are approved? Do the headline numbers agree with the public sources? Approval status is stated as of October 30, 2026 (rechecked October 31). No journal full text was read, and most numbers rest on abstracts, company releases or tool-generated extractions.

## Scope and sources

The ten items are second-hand summaries of headlines from a list reported to have been widely read on social media. The post itself has not been found, and its original wording is unknown. Whether it contained a phrasing that reads as "87% attack-free" is also unknown. The sections below show only how public sources define the numbers closest to each headline. Approval status is as of October 30, 2026; the FDA pages and trial registry records were retrieved on October 31, 2026 to confirm it. For the other items, a search for approval reports on the same day found no additional approvals.

The level at which each source was read is recorded in five tiers. Tier 1 is a journal abstract: the XML retrieved from the PubMed API was read, and no journal full text was read. Tier 2 is a trial registry: the record returned by the ClinicalTrials.gov API was read. Tier 3 is the full text of a company release: for the Merck and Moderna release, text was extracted from the PDF and the results section was read. Tier 4 is a web-page extraction: FDA, company and news pages were read through the summary returned by a page-fetching tool, without verbatim comparison with the original. Tier 5 is a search-result excerpt: the page itself could not be retrieved. For VDPHL01, the author subsequently read the Form 8-K text on November 2, replacing the earlier excerpt-only assessment. Table 1 gives the type of source reached for each item. The origin and tier of every number are listed in the distribution file `source-notes.md`.

Table 1. Reading level and status of the ten items (as of October 30, 2026).

| # | Headline (summary) | Type of source reached | Status |
| --- | --- | --- | --- |
| 1 | Daraxonrasib, pancreatic cancer, overall survival 13.2 vs 6.6 months | Journal abstract ([1](#ref-1)); extraction of the FDA page ([2](#ref-2)) | Approved by the FDA (August 26, 2026) |
| 2 | Gene editing, hereditary angioedema, 87% and 62% | Journal abstract ([3](#ref-3)) (87%); extraction of the company release ([4](#ref-4)) (62%) | Not approved. BLA accepted with priority review (September 8, 2026) ([5](#ref-5)) |
| 3 | Gene editing, LDL cholesterol −62% | Journal abstract ([6](#ref-6)) | Not approved (phase 1) |
| 4 | Personalized mRNA vaccine, 1,137 patients, 42% | Full text of the company release ([7](#ref-7)); extraction of a news report ([8](#ref-8)) | Not approved. Paper reported by the companies as accepted by NEJM, not yet published |
| 5 | Retatrutide, about 28% weight loss | Extraction of the company's medical information page ([9](#ref-9)); extraction of the company release ([10](#ref-10)) | Not approved. BLA submission planned for the first quarter of 2027 |
| 6 | Rentosertib, phase 3 | Trial registry ([11](#ref-11)); abstract of the phase 2a paper ([12](#ref-12)) | Not approved |
| 7 | Oral hair-growth drug, phase 3 | Company Form 8-K, Item 8.01 ([13](#ref-13)); trial registry ([14](#ref-14)) | Not approved |
| 8 | Dostarlimab, rectal cancer, FDA approval | Extraction of the FDA page ([15](#ref-15)); trial registry ([16](#ref-16)); journal abstract ([17](#ref-17)) | Accelerated approval (October 19, 2026) |
| 9 | Pig kidney, 271 days | Journal abstract ([18](#ref-18)); extraction of the company release ([19](#ref-19)) | Not approved. Expanded access continues; the RESTORE trial has not started |
| 10 | Transfer of chromosome-sized DNA between cells | Journal abstracts ([20](#ref-20), [21](#ref-21)) | Basic research, not subject to approval |

Differences and ratios in the text are the values reported by the sources unless stated otherwise. Values computed by the author by subtraction are marked "author's calculation".

## Two approved items

### Overall survival with daraxonrasib

On August 26, 2026, the FDA approved daraxonrasib (brand name Rasonque) for adults with metastatic pancreatic adenocarcinoma who have received at least one prior systemic therapy or are not candidates for multiagent systemic therapy ([2](#ref-2), [22](#ref-22)). The headline numbers come from the phase 3 RASolute 302 trial. In total, 500 patients were randomized (248 to daraxonrasib and 252 to chemotherapy), and 91.8% had RAS G12 mutations. The primary endpoints were overall survival and progression-free survival in the RAS G12 population ([1](#ref-1)).

Median overall survival was 13.2 versus 6.6 months in the RAS G12 population and 13.2 versus 6.7 months in the overall population, with a hazard ratio of 0.40 in both ([1](#ref-1)). The difference between "6.6" and "6.7" reflects the population, not a contradiction between sources. In the FDA page, the overall-population medians were 13.2 months (95% confidence interval [CI] 10.0 to not estimable) versus 6.7 months (5.8 to 8.0), with a hazard ratio of 0.40 (0.30 to 0.53) ([2](#ref-2)). The one-year survival of 53.3% versus 18.7% is the RAS G12 value given in a news report and does not appear in the abstract ([23](#ref-23)). The comparator was investigator's-choice chemotherapy, and the trial was open label ([1](#ref-1)). The FDA page does not state whether the approval is regular or accelerated ([2](#ref-2)).

### Clinical complete response with dostarlimab

On October 19, 2026, the FDA granted accelerated approval to dostarlimab (Jemperli) for adults with stage II or III locally advanced rectal cancer classified as MSI-H or dMMR by an FDA-authorized test ([15](#ref-15)). The basis is AZUR-1, a single-arm, open-label trial in which 154 previously untreated patients were treated. The registry classifies it as phase 2 ([16](#ref-16)). The primary endpoint is clinical complete response sustained for 12 months after the end of treatment (cCR12). The FDA page gives 47% by independent central review (116 evaluable patients) and 68% by investigators (144 patients) ([15](#ref-15)).

The two values differ not only in who assessed but in who was evaluable. Thirty-eight patients (33%) reached clinical complete response by independent review but had less than 12 months of follow-up ([15](#ref-15)). The journal abstract likewise states that cCR12 by independent review was less mature because the first responses were identified at later time points ([17](#ref-17)). The 47% and 68% are separate assessments, and neither contradicts the other.

The FDA page also lists a cCR12 of 93% and a response rate of 100% from a different trial (investigator-led, single-arm, 50 patients). These are not AZUR-1 values ([15](#ref-15)). Under the accelerated approval program, sponsors must still conduct studies to confirm clinical benefit ([24](#ref-24)); the portion of the dostarlimab page that was extracted did not include a statement on a confirmatory trial ([15](#ref-15)). Median follow-up was 26.3 months, and the FDA states that no patient with cCR12, cCR or near-complete response had progression ([15](#ref-15)). The trial is single-arm and contains no direct comparison with standard treatment.

## Four items whose number definitions differ from the headline reading

### 87% and 62% in hereditary angioedema

In the phase 3 HAELO trial, 80 patients aged 16 years or older with hereditary angioedema with C1 inhibitor deficiency were randomized to a single 50 mg infusion of lonvo-z (52 patients) or placebo (28 patients). Median follow-up was 7.5 months (range 4.9 to 12.8). From week 5 through week 28, the least-squares mean monthly attack rate was 0.26 (95% CI 0.15 to 0.45) versus 2.10 (1.55 to 2.86), a relative difference of −87% (−93 to −78) ([3](#ref-3)). The 87% is a reduction in attack rate, not the proportion of patients without attacks.

The company reports that 62% of lonvo-z patients, versus 11% of placebo patients, were attack-free and had no long-term prophylaxis over the six-month efficacy period ([4](#ref-4)). This value is not in the abstract, and the full text has not been read, so it is treated as a value taken from an extraction of the company release. The abstract reports no serious adverse events and no grade 3 or higher adverse events in the lonvo-z group ([3](#ref-3)). The FDA accepted the BLA on September 8, 2026 with priority review and a PDUFA target date of March 10, 2027; no advisory committee is currently planned ([5](#ref-5)). This is a single-dose therapy with median follow-up of 7.5 months, so these sources do not allow a judgment on durability.

### LDL cholesterol −62%

The phase 1 trial of VERVE-102 was an open-label, single-ascending-dose study. Adults with heterozygous familial hypercholesterolemia or premature coronary artery disease received one infusion at one of six doses from 0.3 to 1.0 mg/kg, and 35 participants were analyzed. Mean LDL cholesterol reduction was 9% at 0.3 mg/kg and 62% at 1.0 mg/kg (78 mg/dL in absolute terms). PCSK9 fell by 51% to 88%, and the reductions persisted through follow-up, which exceeded one year in 15 participants ([6](#ref-6)).

The "62%" is the mean of the highest-dose group in a dose-escalation study without a control group. The number of participants in that group is not in the abstract and has not been verified. The abstract reports transient ALT elevations and one case of aspiration pneumonitis ([6](#ref-6)). "Gene editing lowers LDL by 62%" therefore holds only for this population and this dose.

### 42% with the personalized mRNA vaccine

The phase 3 INTerpath-001 trial randomized 1,137 patients with completely resected stage IIB to IV melanoma 2:1 to intismeran autogene plus pembrolizumab or placebo plus pembrolizumab. The primary endpoint is investigator-assessed recurrence-free survival. In the primary prespecified intention-to-treat analysis, with median follow-up of 24.6 months, the hazard ratio for recurrence or death was 0.58 (95% CI 0.45 to 0.75). The companies describe this as a 42% reduction in the risk of recurrence or death ([7](#ref-7)). A hazard ratio of 0.58 is a ratio of event rates, and 1 − 0.58 = 0.42 is a reduction in the hazard. It does not mean that 42% of patients did not relapse.

The two-year recurrence-free survival was 82.2% (79.3% to 84.8%) versus 70.0% (65.0% to 74.5%), a difference of 12.2 percentage points (author's calculation). Two-year distant-metastasis-free survival was 88.5% versus 80.2%, and the hazard ratio for distant metastasis or death was 0.62 (0.45 to 0.85) ([7](#ref-7)). The hazard ratio varied over time: it was 0.99 (0.66 to 1.49) in the first six months, showing no difference, and 0.42 (0.30 to 0.58) after six months in a prespecified sensitivity analysis. In an analysis excluding patients who did not receive the planned dose, it was 0.51 (0.39 to 0.67) ([7](#ref-7)). Overall survival is immature, and the company release gives no hazard ratio ([7](#ref-7)). A news report gives 0.77 (0.45 to 1.31), which did not reach the prespecified significance boundary ([8](#ref-8)). The company states that the results have been accepted for publication; the author's PubMed search did not find the paper ([7](#ref-7)).

### 28% with retatrutide

TRIUMPH-1 followed 2,339 adults with obesity or overweight without diabetes for 80 weeks. According to the company's medical information page, the mean body-weight change at 12 mg was −28.3% (placebo −2.2%) under the efficacy estimand, which describes the effect before treatment discontinuation or other intercurrent events, and −25.0% (placebo −3.9%) under the treatment-regimen estimand, which applies regardless of adherence. For 4 mg the values were −19.0% and −17.6%, and for 9 mg −25.9% and −23.7% ([9](#ref-9)). The differences from placebo are 26.1 and 21.1 percentage points respectively (author's calculation). The headline of about 28% is the highest-dose value under the efficacy estimand. In people with type 2 diabetes (TRIUMPH-2), the maximum at the same 12 mg and 80 weeks was 20.8% ([10](#ref-10)). Lilly states that it plans to submit a BLA in the first quarter of 2027, and the drug is not approved by any regulator at present ([10](#ref-10)).

## Two items still in development

### Phase 3 of rentosertib

According to the ClinicalTrials.gov record, the phase 3 trial of rentosertib in idiopathic pulmonary fibrosis is randomized, double blind and placebo controlled, with once-daily dosing for 52 weeks. Planned enrollment is 320, the start date is September 9, 2026, the primary outcome is the annual rate of decline in forced vital capacity over 52 weeks, and primary completion is estimated for October 30, 2029 ([11](#ref-11)). Starting a phase 3 trial is not a result showing efficacy. The only published efficacy-related data come from phase 2a. That trial randomized 71 patients for 12 weeks to 30 mg once daily, 30 mg twice daily, 60 mg once daily or placebo, and its primary endpoint was the proportion with adverse events. Forced vital capacity was a secondary endpoint: +98.4 mL (95% CI 10.9 to 185.9) at 60 mg once daily versus −20.3 mL (−116.1 to 75.6) with placebo, and the intervals overlap ([12](#ref-12)).

### Phase 3 of an oral hair-growth drug

The drug in the headline remains unidentified. One candidate is VDPHL01, extended-release oral minoxidil. On November 2, 2026, the author read Item 8.01 of Veradermics' October 19 Form 8-K. It reports that Study 304 randomized 536 men with male pattern hair loss to 8.5 mg once daily, 8.5 mg twice daily or placebo. Mean month-6 increases from baseline in non-vellus target-area hair count were 28.6, 36.4 and 6.6 hairs/cm², respectively ([13](#ref-13)). Placebo-subtracted differences are 22.0 and 29.8 hairs/cm² (author's calculation). These are changes in hair count, not proportions of patients growing hair. They are company-reported topline results, not findings verified in a peer-reviewed paper.

The author also read registry NCT06972264. Its retrieved record was last updated February 12, 2026 and lists estimated enrollment of 480, rather than the 536 in the October report. The records describe different dates; no results are posted in the retrieved registry record ([14](#ref-14)). The numerical outcomes therefore rest on the Form 8-K, not independent verification in registered results. Whether the original headline referred to this drug remains unknown.

## A single case report and basic research

### The 271 days of the pig kidney

The Lancet report describes the first of three patients planned in a study under FDA expanded access. A gene-edited pig kidney, EGEN-2784 (glycan antigen deletions, inactivation of porcine endogenous retroviruses, seven human transgenes), was transplanted on January 25, 2025, and the patient remained dialysis-independent for 271 days. T-cell-mediated rejection on day 14 resolved with treatment. After immunosuppression was reduced, microvascular inflammation progressed and the graft failed through thrombotic microangiopathy. A human kidney was transplanted 82 days after explantation, and no sensitization was seen over 231 days of follow-up ([18](#ref-18)). This is the course of a single patient and cannot be generalized.

The word "record" also needs a qualification. In its release of September 3, 2026, eGenesis states that five patients have received transplants under expanded access, and that another patient has remained on the study without dialysis for more than nine months, which it describes as a new global record ([19](#ref-19)). The company plans to start the FDA-cleared phase 1/2/3 RESTORE trial (33 patients aged 50 to 70) in the first quarter of 2027 ([19](#ref-19)). The company's own release therefore does not support 271 days as the longest.

### Transfer of chromosome-sized DNA between cells

The 2026 Cell paper showed that cytoplasmic DNA derived from micronuclei or fragmented chromosomes moves to adjacent human cells through contact-dependent nanotubes, and that transferred fragments are stably inherited by the recipient cells. The material was cultured human cells ([20](#ref-20)). The 2025 Science paper reported a method that transfers human chromosomes from human cells to mouse embryonic stem cells, returns them to human cells, and eliminates the endogenous chromosomes ([21](#ref-21)). Which paper the headline refers to could not be confirmed, and "chromosome-sized" is confirmed in the abstract only for the methodology of the latter. Both are basic research in cultured cells and are not subject to approval.

## Limitations

- The original post could not be confirmed. Because the exact wording of the headlines is unknown, it cannot be said that the post conveyed any number incorrectly.
- No journal full text was read. Among numbers such as 87%, 62% and 42%, those not in the abstracts (62% attack-free, one-year survival, the hazard ratio for overall survival) rest on extractions of company releases or news reports.
- FDA, company and news pages were read through summaries returned by a tool, without verbatim comparison with the original screens or documents. For VDPHL01, the author subsequently compared the numbers with Item 8.01 of the Form 8-K on November 2. This does not constitute independent verification in a peer-reviewed paper or registered results.
- Approval status is stated as of October 30, 2026 and may change before publication.
- The independent-review confidence interval for the dostarlimab 47% is not discussed, because the original could not be read directly.
- The article was written with an AI (Claude) and reviewed three times by AI reviewers commissioned by the same author; this is not confirmation by a human third party.

## Conclusion

As of October 30, 2026 (rechecked October 31), and within the range checked, 2 of the 8 drug, vaccine and therapy items among the ten are approved: daraxonrasib for pancreatic cancer received FDA approval, and dostarlimab for rectal cancer received accelerated approval. The BLA for lonvo-z has been accepted and is under review, and the other five items are pre-submission or in development. The pig kidney and the DNA transfer are not subject to approval.

The headline numbers did not contradict the sources that could be checked. However, each number carries a condition on what it measures. The 87% in hereditary angioedema is a reduction in attack rate, while attack-free patients were 62%. The LDL 62% is the mean of the highest-dose group, and the vaccine 42% is a reduction in the hazard, with no difference in hazard during the first six months. The retatrutide figure of about 28% is the efficacy-estimand value, which excludes events such as treatment discontinuation, and the regardless-of-adherence estimand gives about 25%. The dostarlimab 47% and 68% are separate assessments differing in assessor and evaluable patients. Because the original post cannot be confirmed, how it described these conditions cannot be judged.

Update, November 2, 2026: VDPHL01 numbers were checked against the Form 8-K text; the reading level and registry-date difference were updated. The drug in the original social-media post remains unidentified.

Recheck, November 3, 2026: no change was found in the approval status of the 10 items (lonvo-z is under review with a PDUFA target date of March 10, 2027; retatrutide's BLA submission is planned for the first quarter of 2027; dostarlimab remains under the accelerated approval of October 19; the registry start date of the rentosertib phase 3 is September 9, 2026). For INTerpath-001, one news report said the accepted paper is scheduled to appear in NEJM on November 11, 2026; this was not confirmed, and the text on the paper (accepted, not found in PubMed) stands as of October 31.

## References

<span id="ref-1"></span>1. O'Reilly EM, Wainberg ZA, Hendifar AE, Borad MJ, Pietrantonio F, Pant S, et al. Daraxonrasib or chemotherapy in previously treated metastatic pancreatic cancer. N Engl J Med. 2026;395(4):325–337. [doi:10.1056/NEJMoa2605555](https://doi.org/10.1056/NEJMoa2605555).

<span id="ref-2"></span>2. U.S. Food and Drug Administration. FDA approves daraxonrasib for metastatic pancreatic adenocarcinoma [Internet]. Silver Spring (MD): FDA; 2026 Aug 26 [cited 2026 Oct 31]. Available from: [https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-daraxonrasib-metastatic-pancreatic-adenocarcinoma](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-daraxonrasib-metastatic-pancreatic-adenocarcinoma).

<span id="ref-3"></span>3. Cohn DM, Gurugama P, Longhurst HJ, Aygören-Pürsün E, Craig TJ, Farkas H, et al. Lonvoguran ziclumeran: in vivo CRISPR gene editing in hereditary angioedema. N Engl J Med. 2026;395(15):1471–1482. [doi:10.1056/NEJMoa2600931](https://doi.org/10.1056/NEJMoa2600931).

<span id="ref-4"></span>4. Intellia Therapeutics. Intellia Therapeutics reports positive phase 3 results in hereditary angioedema, marking a global first for in vivo gene editing [press release]. Cambridge (MA): Intellia Therapeutics; 2026 Apr 27 [cited 2026 Oct 31]. Available from: [https://www.biospace.com/press-releases/intellia-therapeutics-reports-positive-phase-3-results-in-hereditary-angioedema-marking-a-global-first-for-in-vivo-gene-editing](https://www.biospace.com/press-releases/intellia-therapeutics-reports-positive-phase-3-results-in-hereditary-angioedema-marking-a-global-first-for-in-vivo-gene-editing) (reprint of the company release).

<span id="ref-5"></span>5. Intellia Therapeutics. Intellia Therapeutics announces FDA acceptance of Biologics License Application with priority review for lonvoguran ziclumeran (lonvo-z) for hereditary angioedema (HAE) (Exhibit 99.1 to Form 8-K) [press release]. U.S. Securities and Exchange Commission; 2026 Sep 8 [cited 2026 Oct 31]. Available from: [https://www.sec.gov/Archives/edgar/data/0001652130/000119312526385194/ntla-ex99_1.htm](https://www.sec.gov/Archives/edgar/data/0001652130/000119312526385194/ntla-ex99_1.htm).

<span id="ref-6"></span>6. Vafai SB, Täubel J, Ashdown T, Patel RS, Diamondali S, Cegla J, et al. In vivo base editing of PCSK9 with VERVE-102 for hypercholesterolemia. N Engl J Med. 2026;395(7):648–659. [doi:10.1056/NEJMoa2601283](https://doi.org/10.1056/NEJMoa2601283).

<span id="ref-7"></span>7. Merck, Moderna. Merck and Moderna will present results from landmark phase 3 INTerpath-001 trial for intismeran autogene plus KEYTRUDA (pembrolizumab) at ESMO 2026 Presidential Symposium [press release]. Rahway (NJ), Cambridge (MA): Merck; 2026 Oct 22 [cited 2026 Oct 31]. Available from: [https://s2.q4cdn.com/584635680/files/doc_news/Merck-and-Moderna-Will-Present-Results-From-Landmark-Phase-3-INTerpath-001-Trial-for-Intismeran-Autogene-Plus-KEYTRUDA-pembrolizumab--RDG7J.pdf](https://s2.q4cdn.com/584635680/files/doc_news/Merck-and-Moderna-Will-Present-Results-From-Landmark-Phase-3-INTerpath-001-Trial-for-Intismeran-Autogene-Plus-KEYTRUDA-pembrolizumab--RDG7J.pdf).

<span id="ref-8"></span>8. CancerNetwork. INTerpath-001 data detail survival, subgroup, and safety findings in melanoma [Internet]. CancerNetwork; 2026 Oct 24 [cited 2026 Oct 31]. Available from: [https://www.cancernetwork.com/view/interpath-001-data-detail-survival-subgroup-and-safety-findings-in-melanoma](https://www.cancernetwork.com/view/interpath-001-data-detail-survival-subgroup-and-safety-findings-in-melanoma).

<span id="ref-9"></span>9. Eli Lilly and Company. What are the results of retatrutide from TRIUMPH-1 in participants with obesity or overweight without type 2 diabetes? [Internet]. Lilly Medical Information; date of last review 2026 Aug 26 [cited 2026 Oct 31]. Available from: [https://medical.lilly.com/us/products/answers/what-are-the-preliminary-results-of-retatrutide-from-triumph-1-in-participants-with-obesity-or-overweight-without-type-2-diabetes-386151](https://medical.lilly.com/us/products/answers/what-are-the-preliminary-results-of-retatrutide-from-triumph-1-in-participants-with-obesity-or-overweight-without-type-2-diabetes-386151).

<span id="ref-10"></span>10. Eli Lilly and Company. Lilly's triple agonist, retatrutide, successful in two additional phase 3 obesity trials, delivering significant improvements in weight and A1C [press release]. Indianapolis (IN): Eli Lilly and Company; 2026 Jul 23 [cited 2026 Oct 31]. Available from: [https://www.biospace.com/press-releases/lillys-triple-agonist-retatrutide-successful-in-two-additional-phase-3-obesity-trials-delivering-significant-improvements-in-weight-and-a1c](https://www.biospace.com/press-releases/lillys-triple-agonist-retatrutide-successful-in-two-additional-phase-3-obesity-trials-delivering-significant-improvements-in-weight-and-a1c) (reprint of the company release).

<span id="ref-11"></span>11. InSilico Medicine Hong Kong Limited. Study evaluation rentosertib (INS018_055) administered orally in patients with idiopathic pulmonary fibrosis (IPF); ClinicalTrials.gov identifier NCT07687459 [Internet]. National Library of Medicine (US); last update posted 2026 Oct 13 [cited 2026 Oct 31]. Available from: [https://clinicaltrials.gov/study/NCT07687459](https://clinicaltrials.gov/study/NCT07687459).

<span id="ref-12"></span>12. Xu Z, Ren F, Wang P, Cao J, Tan C, Ma D, et al. A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial. Nat Med. 2025;31(8):2602–2610. [doi:10.1038/s41591-025-03743-2](https://doi.org/10.1038/s41591-025-03743-2).

<span id="ref-13"></span>13. Veradermics, Incorporated. Current report, Form 8-K, October 19, 2026. Item 8.01: Other events [Internet]. U.S. Securities and Exchange Commission; 2026 Oct 19 [cited 2026 Nov 2]. Available from: [https://www.sec.gov/Archives/edgar/data/1827635/000182763526000036/mane-20261019.htm](https://www.sec.gov/Archives/edgar/data/1827635/000182763526000036/mane-20261019.htm).

<span id="ref-14"></span>14. Veradermics, Inc. Safety and efficacy of VDPHL01 in males with AGA; ClinicalTrials.gov identifier NCT06972264 [Internet]. National Library of Medicine (US); last update posted 2026 Feb 12 [cited 2026 Nov 2]. Available from: [https://clinicaltrials.gov/study/NCT06972264](https://clinicaltrials.gov/study/NCT06972264).

<span id="ref-15"></span>15. U.S. Food and Drug Administration. FDA grants accelerated approval to dostarlimab for locally advanced rectal cancer [Internet]. Silver Spring (MD): FDA; 2026 Oct 19 [cited 2026 Oct 31]. Available from: [https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-dostarlimab-locally-advanced-rectal-cancer](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-dostarlimab-locally-advanced-rectal-cancer).

<span id="ref-16"></span>16. GlaxoSmithKline. A study of dostarlimab in untreated dMMR/MSI-H locally advanced rectal cancer (AZUR-1); ClinicalTrials.gov identifier NCT05723562 [Internet]. National Library of Medicine (US); last update posted 2026 May 26 [cited 2026 Oct 31]. Available from: [https://clinicaltrials.gov/study/NCT05723562](https://clinicaltrials.gov/study/NCT05723562).

<span id="ref-17"></span>17. Cercek A, Bachet JB, Folprecht G, Bando H, Seligmann J, Starling N, et al. Clinical complete response with dostarlimab monotherapy in dMMR/MSI-H locally advanced rectal cancer: first results from the global AZUR-1 trial. Ann Oncol. 2026 Oct 25:S0923-7534(26)08070-1 [Epub ahead of print]. [doi:10.1016/j.annonc.2026.10.1280](https://doi.org/10.1016/j.annonc.2026.10.1280).

<span id="ref-18"></span>18. Riella LV, Borges TJ, Rosales IA, Avillach CT, Palsson R, Hullekes F, et al. Porcine kidney xenotransplantation as a bridge to allotransplantation: a first-in-human study. Lancet. 2026;408(10559):1029–1040. [doi:10.1016/S0140-6736(26)01295-X](https://doi.org/10.1016/S0140-6736(26)01295-X).

<span id="ref-19"></span>19. eGenesis. eGenesis announces clinical update in ongoing expanded access study of EGEN-2784 in patients with kidney failure [press release]. Cambridge (MA): eGenesis; 2026 Sep 3 [cited 2026 Oct 31]. Available from: [https://egenesisbio.com/news-media/press-releases/egenesis-announces-clinical-update-in-ongoing-expanded-access-study-of-egen-2784-in-patients-with-kidney-failure](https://egenesisbio.com/news-media/press-releases/egenesis-announces-clinical-update-in-ongoing-expanded-access-study-of-egen-2784-in-patients-with-kidney-failure).

<span id="ref-20"></span>20. Maurais EG, Mazzagatti A, Lin YF, Narozna M, Hu Q, Dahiya R, et al. Genome instability triggers intercellular DNA transfer between human cells. Cell. 2026;189(15):4548–4561.e14. [doi:10.1016/j.cell.2026.04.041](https://doi.org/10.1016/j.cell.2026.04.041).

<span id="ref-21"></span>21. Petris G, Grazioli S, van Bijsterveldt L, Murat P, Liu KC, Birnbaum J, et al. High-fidelity human chromosome transfer and elimination. Science. 2025;390(6777):1038–1043. [doi:10.1126/science.adv9797](https://doi.org/10.1126/science.adv9797).

<span id="ref-22"></span>22. U.S. Food and Drug Administration. FDA approves first in class targeted therapy for metastatic pancreatic cancer [Internet]. Silver Spring (MD): FDA; 2026 Aug 26 [cited 2026 Oct 31]. Available from: [https://www.fda.gov/news-events/press-announcements/fda-approves-first-class-targeted-therapy-metastatic-pancreatic-cancer](https://www.fda.gov/news-events/press-announcements/fda-approves-first-class-targeted-therapy-metastatic-pancreatic-cancer).

<span id="ref-23"></span>23. The ASCO Post. Daraxonrasib nearly doubles survival in previously treated metastatic pancreatic cancer [Internet]. The ASCO Post; 2026 Jun 10 [cited 2026 Oct 31]. Available from: [https://ascopost.com/news/june-2026/daraxonrasib-nearly-doubles-survival-in-previously-treated-metastatic-pancreatic-cancer/](https://ascopost.com/news/june-2026/daraxonrasib-nearly-doubles-survival-in-previously-treated-metastatic-pancreatic-cancer/).

<span id="ref-24"></span>24. U.S. Food and Drug Administration. Accelerated approval program [Internet]. Silver Spring (MD): FDA; content current as of 2026 Aug 25 [cited 2026 Oct 31]. Available from: [https://www.fda.gov/drugs/nda-and-bla-approvals/accelerated-approval-program](https://www.fda.gov/drugs/nda-and-bla-approvals/accelerated-approval-program).
