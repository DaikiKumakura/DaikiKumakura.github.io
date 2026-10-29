## 第2相の成功率を支える標本はまだ少ない {#_1}

この話は、数字の裏づけが、論調の強さほどには厚くない。2026年の春から夏にかけて、AI創薬は第1相は通るが第2相では従来の薬と変わらない、律速は分子の設計ではなく臨床での検証だ、という論調の記事が続いた。たどると、第2相の数字の出どころは、2024年の論文の要旨 ([1](#ref-1)) と、2026年の学会抄録の件数、業界調査会社の「同程度」という一文に行き着いた。どれも「小さな標本」「途中の集計」であり、第2相の成功率を測った数字としては弱い。一方で「律速は臨床にある」という議論は、4つの記事で一致しているが、新しい測定ではなく議論として繰り返されている。議論として妥当かどうかと、データで確かめられているかどうかは、別の問いである。

「第2相で止まる」という言い方には、種類の違う三つの主張が混ざっている。第一は、第2相の成功率が過去の業界平均を上回らない、という割合の比較である。第二は、第2相まで進んだAI関連の資産がまだ少ない、という件数の記述である。第三は、律速は分子の設計ではなく臨床での検証にある、という議論である。それぞれ必要な根拠が違う。さらに、第一の主張が成り立っても、同じ定義の比較可能なコホートで第1相の通過率だけが高ければ、第1相に入った候補が第2相を越える確率は、過去より高くなる。第2相の成功率が過去と「同程度」であることは、「止まる」ことを意味しない。以下では、三つの主張を支える資料を順に確認する。

確認した範囲は次のとおりである。Jayatungaらの論文は、Europe PMCの要旨だけを読んだ。ProMarket、Clinical Trial Vanguard、IQVIAのブログは本文を読み、Trey's Thoughtsは無料で公開された部分だけを読んだ。ASCOの抄録は二次資料の解説による。Petrie-Flom Centerの記事は、今回の再確認ではサイトのアクセス制限で開けず、前回の読了記録に依っている。XとLinkedInの投稿は直接読めておらず、記事に引用された範囲しか見ていない。ここに書く数値は各資料の転載で、派生した数値は `numbers.py` の出力である。

## 出発点は2024年の論文の要旨 {#1-2024}

起点となる一次資料は、Jayatungaらの分析（*Drug Discovery Today* 2024）である ([1](#ref-1))。著者の所属は、Europe PMCの記録ではBoston Consulting Group（BCG）である。要旨によれば、AIを中心に据えた新興バイオ企業の臨床パイプラインを集計し、次の結果を得た。

- 第1相：AIで見いだされた分子の成功率は80〜90%で、過去の業界平均より大幅に高い。
- 第2相：成功率は約40%。ただし標本は限られ、過去の業界平均と同程度。

著者らは、第1相の結果は、AIが薬らしい性質を持つ分子を設計・同定できることを示唆する、と解釈している。第2相は「限られた標本」と断っている。ProMarketは、BCGの分析を、臨床試験に入った約24のAI発見分子に基づくものとして紹介している ([2](#ref-2))。これが第1相の標本の大きさを示すなら、第1相も小さな標本である。ProMarketは論文を引用しておらず、この24がJayatungaらの分析と同一かどうかは確認できない。著者の所属から同じ分析を指す可能性は高いが、推測にとどまる。

本文は読めておらず（要旨のみ）、「成功」の定義と第2相の分母・分子は、原著では確認していない。分母が確認できないため、約40%に対応する例として「10件のうち4件」を仮定する。10件中4件なら、成功率の95%信頼区間（Clopper-Pearson法 ([3](#ref-3))。小さな件数でも使える二項分布の区間）は12.2〜73.8%と広く（`results/summary.json`）、業界平均と同じとも違うとも判断できない。この点は[別の記事](ai-phase2-sample-size.html)で詳しく扱った。

比較対象の「過去の業界平均」も、一つの値ではない。臨床試験の成功率の推定は、集計に使う母集団や定義によって、既存の広く引用される値と有意に異なりうることが報告されている ([4](#ref-4))。実際、記事ごとに第1相の過去値の書き方が違う。ProMarketは「約半分」と書き ([2](#ref-2))、Clinical Trial Vanguardは40〜65%と書く ([5](#ref-5))。比較の基準が揃っていないので、「大幅に高い」の大きさも記事の間で変わる。

## 引用の連鎖：数字はどこから来たか {#2}

その後の記事を、数字の出どころの視点で並べた。

**表1．** 二次記事が使う数字と出所の帰属。

| 媒体 | 日付 | 使っている数字 | 出どころの書き方 |
|---|---|---|---|
| Trey's Thoughts（Substack）([6](#ref-6)) | 2026年4月1日 | ヒト初回投与から承認まで6〜10年、第1相に入った候補の10〜15%が承認に至る | 年数の出典は記載なし。承認に至る割合も、直前の文に別の分析（Nature Communications）への言及はあるが、この数値の出典としては示されない（一部有料で未読） |
| ProMarket（Santoro）([2](#ref-2)) | 2026年7月2日 | 第1相80〜90%、第2相約40%、全体の成功確率5〜10%から9〜18% | BCG（Boston Consulting Group）の分析に帰属。Jayatungaらの所属もBCGだが、論文の引用はない。5〜10%から9〜18%は、第3相が過去並みという仮定を置いた推計で、観測値ではない |
| Petrie-Flom（Epstein & Niazi）([7](#ref-7)) | 2026年8月4日 | 「設計が10倍速い」 | Anthropicのモデル発表に帰属し、検証したとの記載はない。この記事は第2相の成功率には触れていない |
| Clinical Trial Vanguard（Alsumidaie）([5](#ref-5)) | 2026年8月11日 | 追跡した117件のうち8件が第2相を通過、第1相80〜90%、約40% | 117と8、80〜90%は、LinkedInの投稿（企業のAI責任者のもの）に帰属。約40%は出典の記載なし。参考文献はLinkedInの投稿のみ |

ProMarketは、数字をBCGの分析に帰属させている点で、確かめやすい ([2](#ref-2))。ただし、第3相に届くAI設計の薬の数は「意味のある一群」とだけ書かれ、件数は示されていない。

Vanguardの117件と8件には、別の出どころがある。2026年の米国臨床腫瘍学会（ASCO）の抄録（*J Clin Oncol* 44(16) suppl、doi:10.1200/jco.2026.44.16_suppl.11072、データの締め切り2025年12月1日）は、AIを使った治療資産117件（63社）のうち、60件（51.3%）が第1相を完了、8件（6.8%）が第2相を完了、と報告している ([8](#ref-8))。抄録そのものは取得できず、数値は二次資料の解説による。数字が一致するので、LinkedInの投稿の元は、この抄録かもしれない。ただしVanguardの記事は、この抄録に言及していない。

この件数の読み方には三つの注意が要る。

第一に、分母である。6.8%の分母は、試験に入った全資産で、まだ第1相や第2相を走っている途中の資産も含む。途中の資産は分母に含まれる一方、8件は成功数と確認できないため、8/117から成功率への過大・過小の方向まで一律には決められない。8を、第1相を完了した60で割った値も、同じ理由で成功率ではない。第二に、動詞である。ASCOの抄録（二次資料の記述）は第2相を「完了」した資産数を数えている。完了には、成功も失敗も含まれる。Vanguardは同じ8件を、第2相を「通過」したと書いている。完了と通過は別の量であり、この言い換えで件数の意味が変わっている。第三に、母集団である。ASCOの117件は、AI対応（AI-enabled）の資産という広い定義で数えられている。二次資料は、分子そのものをAIが設計した資産に限る狭い定義との違いを指摘している。Jayatungaらは、AIを中心に据えた新興企業の分子を集計しており、母集団も定義も同じとは限らない。したがって、8/117は、分母が違うだけでなく、約40%とは対象が違う可能性がある。Vanguardの記事は、「8件のみ」と「約40%」の両方を同じ記事の中に載せており、並べて読まれやすい。

## 業界調査の一文 {#3}

IQVIA Instituteの2026年5月のブログ ([9](#ref-9))（*Global R&D Trends 2026*の紹介）は、新興バイオ医薬企業のAI対応プログラムについて、直近3年の窓の第1相の成功率が75%で、非AIのプログラムより明確に高く、第2相の成功率は非AIと「同程度」と書いている。第2相の数値は示されておらず、対象は「比較的小さい」と断っている。AIの関与は、自己申告ではなく確認されたものである。報告書の本文は読めていない。2024年の要旨と同じ方向の別の観察だが、これも小さな標本であることに変わりはない。

ただし、IQVIAは「同程度」を「止まる」とは読んでいない。ブログは、AI対応のプログラムが、後の段階で失敗する候補を第1相に押し込んでいるだけなら第2相の成功率が下がるはずだが、そうなっていない、という文脈で第2相の同程度を好意的な結果として扱っている。第3相への移行は、意味のある解析をするにはまだ数が足りないと述べる。業界全体の成功率は前年から変わっておらず、改善が見えるのは新興バイオ医薬企業という一つの区分にとどまる。調査対象のプログラムの内訳では、AI利用の最大の部分は、既知の生物学的標的に対する分子設計であり、標的の発見にAIを使う部分はそれより小さい ([9](#ref-9))。第1相の通過率の高さの一部は、標的が既知であることで説明できるかもしれないが、この資料からは分けられない。

## 「律速は臨床にある」という議論 {#4}

数字の裏づけは弱いが、議論の中身は一致している。

- ProMarket ([2](#ref-2))：薬が失敗するのは、分子が間違っているか、背後の生物学的な賭けが間違っているかの二通りで、AIは主に前者に働いた。費用は後ろの段階に積み上がる。
- Petrie-Flom ([7](#ref-7))：予測は、薬が患者を助けることの証拠ではない。FDAは、残る不確かさに応じて証拠の要求を合わせるべきだ。
- Vanguard ([5](#ref-5))：LinkedInの投稿を引き、真の律速は、どの生物学的な機序が人の転帰を変えるかの検証であり、候補分子の生成ではない、と論じる。
- Trey ([6](#ref-6))：律速は、分子の同定から証拠の生成に移った。

読んだ範囲では、これらの記事の間に相互の引用は見当たらない。ただしProMarketとVanguardは、同じ80〜90%と約40%を使っており、独立した確認とは言えない。Vanguardは臨床試験業界の媒体で、実務の視点も含まれる一方、参考文献は4件の投稿であり、一次資料へのリンクはない。したがって「4つの記事で一致」は、独立した4本の分析ではなく、評論と投稿の引用を含む。一致していることは、議論の筋の通りやすさを示しても、データの強さを示すわけではない。

議論そのものの前提は、別の資料で確かめられる。臨床開発の失敗理由についての総説は、2010〜2017年の臨床試験データの解析として、有効性の欠如が40〜50%、制御できない毒性が30%、薬物様性質の不良が10〜15%、商業上の理由と戦略の不備が10%と整理している ([10](#ref-10))。有効性の欠如が最大の失敗理由であることは、「律速は臨床での検証にある」という議論と整合する。ただし、失敗理由の割合は工程の所要時間・費用・処理能力を測っておらず、どこが律速かをそれだけで同定することはできない。また、この総説の数字はAI由来の分子に限ったものではない。また、毒性や薬物様性質は、分子の設計で動かしうる失敗理由でもある。AIが設計を担う範囲で、これらの失敗が減るかどうかは、この総説からは分からない。

## 一つの具体例：rentosertibの第2a相 {#5-rentosertib2a}

ProMarketが「これまでで最も明るい結果」と呼ぶのが、Insilico Medicineのrentosertib（特発性肺線維症）の第2a相である ([2](#ref-2))。第2a相は、71人を30 mg 1日1回、30 mg 1日2回、60 mg 1日1回、プラセボに割り付けた試験で、主要評価項目は治療下で生じた有害事象の割合だった ([11](#ref-11))。[私の別の記事](rentosertib-ph2a.html)では、公表された集計値だけで、60 mg群の努力性肺活量（FVC）の改善（+98.4 mL）の頑健性を調べた。+98.4 mLは60 mg群の群内の変化で、プラセボとの差の95%信頼区間は0を含み、60 mg群で12週目のFVCがない人は8/18（44%）だった。これは試験の失敗を意味しない。第2a相の主要な目的は安全性で、FVCは副次的な指標だからである。この具体例は、「第1相を通る」と「第2相以降で効く」の間の距離が、一つの試験の中でも不確かさを残すことを示すにとどまり、AI創薬全体の成功率については何も言えない。

## 考察 {#discussion}

この確認から、三つの読み方が変わる。

第一に、Jayatungaらの第2相の約40%の読み方である。標本が限られ、成功の定義と分母・分子が確認できないので、この値は、過去の業界平均と同等であることも、劣ることも示さない。「AIは第2相で従来と変わらない」と書く記事は、要旨の「同程度」という記述を、同等性の結論として使っている。仮に10件中4件なら、区間は12.2〜73.8%で、過去平均より高い値も低い値も含む。同等と述べるには、比較する成功率の差について許容幅を決め、その差の区間全体が許容幅の内側に収まる必要がある。この記事の計算では、その条件は満たされていない。

第二に、件数と割合の区別である。8/117のような件数は、第2相の結果が確定した資産だけを分母にした割合とは別物で、追跡の打ち切りと、完了と成功の違いを含む。成功率として読むには、同じコホートについて、結果が出た資産数（分母）、そのうちの成功数（分子）、観察の時間窓が必要になる。ASCOの抄録を引いた記事が増えても、この三つが揃わない限り、割合としての根拠は増えない。

第三に、「止まる」と「同程度」の関係である。ProMarketが引くBCGの推計は、第1相の通過率が高く第2相が過去並みなら、AI設計の薬が承認に至る確率はおおむね倍になる、というものである ([2](#ref-2))。この倍増は第3相が過去並みという仮定に基づく推計で、観測値ではない。それでも、「止まる」を「第2相の成功率が改善しない」の意味で使うなら、第1相の通過率が高い分、全体の確率は上がる方向にあり、「止まる」という語は合わない。「第2相を越えられない」の意味で使うなら、成功率が過去と同程度であることは、それを支えない。IQVIAも、第2相の同程度を後退とは読んでいない ([9](#ref-9))。後者の意味での主張には、第2相を越える資産の絶対数や、第2相以降に特有の失敗の増加が必要になる。この記事で読んだ資料は、そのどちらも示していない。

これらは、AI創薬の第2相以降の成績が良いか悪いかについての判断ではない。読んだ資料が、その判断に必要な分母と定義を欠く、という指摘である。

## 結論 {#6}

「AI創薬は第2相で止まる」という主張が、第2相の成功率の測定としてどこまで言えるかは、今回読んだ範囲では、小さな標本と途中の集計にとどまる。三つの主張に分けると、答えは次のとおりである。第2相の成功率が過去と同程度という主張は、定義が未確認の小さな標本の点推定であり、同等とも差があるとも言えない。第2相まで進んだ資産が少ないことは件数として確認できるが、途中の集計であり成功率ではない。「律速は臨床にある」という議論は、有効性の欠如が主要な失敗理由であるという別資料の整理と整合するが、同じ数字を引く記事の一致は、独立した確認ではない。以上から、「止まる」という主張は、支持も反証もできない。第2相の成功、第2相の完了、追跡資産に占める割合は、同じ量ではない。

## 限界 {#_2}

- Jayatungaらの論文は要旨のみ。「成功」の定義と、第2相の分母・分子は、原著で確認していない。10件中4件は仮定である。
- ASCO抄録とIQVIAの報告書は、二次資料とブログによる。ASCO抄録はそのものを取得できなかった。「AI対応」の定義の違いも二次資料による。
- XとLinkedInの投稿、Redditは直接読めていない。Fast Companyの記事は取得できなかった。Petrie-Flomの記事は今回の再確認ではアクセス制限により開けなかった。
- ProMarketのBCGの分析は、記事の記載の転載で、原文は読んでいない。BCGの分析とJayatungaらの論文が同一であるかは確認していない。
- 失敗理由の割合 ([10](#ref-10)) は総説の記載で、元の解析は読んでいない。
- Exscientia、Schrödinger、BCGの更新版、創薬の専門誌による集計は検索していない。読んだ記事は4本で、代表性は主張しない。

## データとコードの公開状況

確認範囲は [sources.md](shared/ai-drug-claim-chain/sources.md)、派生計算は [numbers.py](shared/ai-drug-claim-chain/numbers.py) と [results/summary.json](shared/ai-drug-claim-chain/results/summary.json) に記録した。独自の臨床試験集団の再解析は行っていない。

## 参照 {#article-references}

1. <span id="ref-1"></span>Jayatunga MKP, Ayers M, Bruens L, Jayanth D, Meier C. How successful are AI-discovered drugs in clinical trials? A first analysis and emerging lessons. Drug Discov Today. 2024;29(6):104009. [doi:10.1016/j.drudis.2024.104009](https://doi.org/10.1016/j.drudis.2024.104009). Abstract only (Europe PMC); the full text was not accessed.

2. <span id="ref-2"></span>Santoro MA. Pharma's AI Boom Has Bet on the Wrong Bottleneck [Internet]. ProMarket; 2026 Jul 2 [cited 2026 Oct 29]. Available from: [https://www.promarket.org/2026/07/02/pharmas-ai-boom-has-bet-on-the-wrong-bottleneck/](https://www.promarket.org/2026/07/02/pharmas-ai-boom-has-bet-on-the-wrong-bottleneck/).

3. <span id="ref-3"></span>Clopper CJ, Pearson ES. The use of confidence or fiducial limits illustrated in the case of the binomial. Biometrika. 1934;26(4):404–413. [doi:10.1093/biomet/26.4.404](https://doi.org/10.1093/biomet/26.4.404).

4. <span id="ref-4"></span>Wong CH, Siah KW, Lo AW. Estimation of clinical trial success rates and related parameters. Biostatistics. 2019;20(2):273–286. [doi:10.1093/biostatistics/kxx069](https://doi.org/10.1093/biostatistics/kxx069). Abstract read; a corrigendum was published (Biostatistics. 2019;20(2):366, [doi:10.1093/biostatistics/kxy072](https://doi.org/10.1093/biostatistics/kxy072)).

5. <span id="ref-5"></span>Alsumidaie M. AI is clearing Phase I. That's the wrong finish line [Internet]. The Clinical Trial Vanguard; 2026 Aug 11 [cited 2026 Oct 29]. Available from: [https://www.clinicaltrialvanguard.com/clinical-bellwether/ai-is-clearing-phase-i-thats-the-wrong-finish-line/](https://www.clinicaltrialvanguard.com/clinical-bellwether/ai-is-clearing-phase-i-thats-the-wrong-finish-line/).

6. <span id="ref-6"></span>Trey. Clinical trials are the new bottleneck [Internet]. Trey's Thoughts on Healthcare Markets & Technology; 2026 Apr 1 [cited 2026 Oct 29]. Freely available part only; the remainder is paywalled. Available from: [https://www.onhealthcare.tech/p/clinical-trials-are-the-new-bottleneck](https://www.onhealthcare.tech/p/clinical-trials-are-the-new-bottleneck).

7. <span id="ref-7"></span>Epstein WN, Niazi SK. AI Can Invent Drugs Faster. It Still Has to Prove They Work [Internet]. Petrie-Flom Center, Harvard Law School; 2026 Aug 4. Not re-opened on 2026 Oct 29 (site access restriction); based on the earlier reading record. Available from: [https://petrieflom.law.harvard.edu/2026/08/04/ai-can-invent-drugs-faster-it-still-has-to-prove-they-work/](https://petrieflom.law.harvard.edu/2026/08/04/ai-can-invent-drugs-faster-it-still-has-to-prove-they-work/).

8. <span id="ref-8"></span>Haque W, Sai-Palm K, Kasparcova MZ, Rana I, Verlingue L, Garassino MC, et al. Clinical-stage AI-enabled therapeutic assets: An industry-wide analysis of scale, clinical progression, and company characteristics. J Clin Oncol. 2026;44(16_suppl):11072. [doi:10.1200/jco.2026.44.16_suppl.11072](https://doi.org/10.1200/jco.2026.44.16_suppl.11072). Conference abstract, not obtained directly; numerical content used via [secondary commentary](https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026) (read 2026 Oct 29).

9. <span id="ref-9"></span>IQVIA Institute. IQVIA Institute's Global R&D Trends 2026 report finds credible signal on AI-enabled programs [Internet]. IQVIA; 2026 May 14 [cited 2026 Oct 29]. Blog commentary; the report itself was not read. Available from: [https://www.iqvia.com/blogs/2026/05/iqvia-institutes-global-r-and-d-trends-2026-report-finds-credible-signal-on-ai-enabled-programs](https://www.iqvia.com/blogs/2026/05/iqvia-institutes-global-r-and-d-trends-2026-report-finds-credible-signal-on-ai-enabled-programs).

10. <span id="ref-10"></span>Sun D, Gao W, Hu H, Zhou S. Why 90% of clinical drug development fails and how to improve it? Acta Pharm Sin B. 2022;12(7):3049–3062. [doi:10.1016/j.apsb.2022.02.002](https://doi.org/10.1016/j.apsb.2022.02.002). Review; failure-reason percentages are quoted from its text, the underlying analyses were not read.

11. <span id="ref-11"></span>Xu Z, Ren F, Wang P, Cao J, Tan C, Ma D, et al. A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial. Nat Med. 2025;31(8):2602–2610. [doi:10.1038/s41591-025-03743-2](https://doi.org/10.1038/s41591-025-03743-2). Abstract read.
