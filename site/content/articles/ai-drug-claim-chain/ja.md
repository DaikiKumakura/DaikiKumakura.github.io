## 第2相の成功率を支える標本はまだ少ない {#_1}

この話は、数字の裏づけが、論調の強さほどには厚くない。2026年の春から夏にかけて、AI創薬は第1相は通るが第2相では従来の薬と変わらない、律速は分子の設計ではなく臨床での検証だ、という論調の記事が続いた。たどると、第2相の数字の出どころは、2024年の論文の要旨と、2026年の学会抄録の件数、業界調査会社の「同程度」という一文に行き着いた。どれも「小さな標本」「途中の集計」であり、第2相の成功率を測った数字としては弱い。 一方で「律速は臨床にある」という議論は、4つの記事で一致しているが、新しい測定ではなく議論として繰り返されている。議論として妥当かどうかと、データで確かめられているかどうかは、別の問いである。

読んだのは、論文の要旨、記事4本、二次資料、私の過去の記事である。ここに書く数値は各資料の転載で、派生した数値は `numbers.py` の出力である。XとLinkedInの投稿は直接読めておらず、記事に引用された範囲しか見ていない。

## 出発点は2024年の論文の要旨 {#1-2024}

起点となる一次資料は、Jayatungaらの分析（*Drug Discovery Today* 2024）である ([1](#ref-1))。要旨によれば、AIを中心に据えた新興バイオ企業の臨床パイプラインを集計し、次の結果を得た。

- 第1相：AIで見いだされた分子の成功率は80〜90%で、過去の業界平均より大幅に高い。
- 第2相：成功率は約40%。ただし標本は限られ、過去の業界平均と同程度。

著者らは、第1相の結果は、AIが薬らしい性質を持つ分子を設計・同定できることを示唆する、と解釈している。第2相は「限られた標本」と断っている。第1相も、ProMarketの記事によれば、約24分子の分析に基づく小さな標本である ([2](#ref-2))。本文は読めておらず（要旨のみ）、「成功」の定義と第2相の分母・分子は、原著では確認していない。分母が確認できないため、約40%に対応する例として「10件のうち4件」を仮定する。10件中4件なら、成功率の95%信頼区間（Clopper-Pearson法。小さな件数でも使える二項分布の区間）は12.2〜73.8%と広く（`results/summary.json`）、業界平均と同じとも違うとも判断できない。この点は[別の記事](ai-phase2-sample-size.html)で詳しく扱った。

## 引用の連鎖：数字はどこから来たか {#2}

その後の記事を、数字の出どころの視点で並べた。

**表1．** 二次記事が使う数字と出所の帰属。

| 媒体 | 日付 | 使っている数字 | 出どころの書き方 |
|---|---|---|---|
| Trey's Thoughts（Substack）([3](#ref-3)) | 2026年4月1日 | ヒト初回投与から承認まで6〜10年、第1相に入った候補の10〜15%が承認に至る | 読めた範囲では記載なし（一部有料で未読） |
| ProMarket（Santoro）([2](#ref-2)) | 2026年7月2日 | 第1相80〜90%、第2相約40%、全体の成功確率5〜10%から9〜18% | BCG（Boston Consulting Group）の分析に帰属。5〜10%から9〜18%は、第3相が過去並みという仮定を置いた推計で、観測値ではない |
| Petrie-Flom（Epstein & Niazi）([4](#ref-4)) | 2026年8月4日 | 「設計が10倍速い」 | Anthropicのモデル発表に帰属し、検証したとの記載はない。この記事は第2相の成功率には触れていない |
| Clinical Trial Vanguard（Alsumidaie）([5](#ref-5)) | 2026年8月11日 | 追跡した117件のうち8件が第2相を通過、第1相80〜90%、約40% | 117と8、80〜90%は、LinkedInの投稿に帰属。約40%は記載なし |

ProMarketは、数字をBCGの分析に帰属させている点で、確かめやすい ([2](#ref-2))。ただし、第3相に届くAI設計の薬の数は「意味のある一群」とだけ書かれ、件数は示されていない。

Vanguardの117件と8件には、別の出どころがある。2026年の米国臨床腫瘍学会（ASCO）の抄録（*J Clin Oncol* 44(16) suppl、doi:10.1200/jco.2026.44.16_suppl.11072、データの締め切り2025年12月1日）は、AIを使った治療資産117件（63社）のうち、60件（51.3%）が第1相を完了、8件（6.8%）が第2相を完了、と報告している ([6](#ref-6))。抄録そのものは取得できず、数値は二次資料の解説による。数字が一致するので、LinkedInの投稿の元は、この抄録かもしれない。ただしVanguardの記事は、この抄録に言及していない。

この件数の読み方には注意が要る。6.8%の分母は、試験に入った全資産で、まだ第1相や第2相を走っている途中の資産も含む。途中のものは分母に入るが分子には入らないので、8/117は成功率よりも低く出る。8を、第1相を完了した60で割った値も、同じ理由で成功率ではない。Jayatungaらの要旨にある約40%（定義は未確認）とは別の量である。Vanguardの記事は、「8件のみ」と「約40%」の両方を同じ記事の中に載せており、並べて読まれやすい。

## 業界調査の一文 {#3}

IQVIA Instituteの2026年5月のブログ ([7](#ref-7))（*Global R&D Trends 2026*の紹介）は、新興バイオ医薬企業のAI対応プログラムについて、直近3年の窓の第1相の成功率が75%で、非AIのプログラムより明確に高く、第2相の成功率は非AIと「同程度」と書いている。第2相の数値は示されておらず、対象は「比較的小さい」と断っている。AIの関与は、自己申告ではなく確認されたものである。報告書の本文は読めていない。2024年の要旨と同じ方向の別の観察だが、これも小さな標本であることに変わりはない。

## 「律速は臨床にある」という議論 {#4}

数字の裏づけは弱いが、議論の中身は一致している。

- ProMarket ([2](#ref-2))：薬が失敗するのは、分子が間違っているか、背後の生物学的な賭けが間違っているかの二通りで、AIは前者にだけ働いた。費用は後ろの段階に積み上がる。
- Petrie-Flom ([4](#ref-4))：予測は、薬が患者を助けることの証拠ではない。FDAは、残る不確かさに応じて証拠の要求を合わせるべきだ。
- Vanguard ([5](#ref-5))：真の律速は、どの生物学的な機序が人の転帰を変えるかの検証であり、候補分子の生成ではない。
- Trey ([3](#ref-3))：律速は、分子の同定から証拠の生成に移った。

読んだ範囲では、これらの記事の間に相互の引用は見当たらない。ただしProMarketとVanguardは、同じ80〜90%と約40%を使っており、独立した確認とは言えない。一致していることは、議論の筋の通りやすさを示しても、データの強さを示すわけではない。 Vanguardは臨床試験業界の媒体で、実務の視点も含まれている。

## 一つの具体例：rentosertibの第2a相 {#5-rentosertib2a}

ProMarketが「これまでで最も明るい結果」と呼ぶのが、Insilico Medicineのrentosertib（特発性肺線維症）の第2a相である ([2](#ref-2))。[私の別の記事](rentosertib-ph2a.html)では、公表された集計値だけで、60 mg群の努力性肺活量（FVC）の改善（+98.4 mL）の頑健性を調べた。+98.4 mLは60 mg群の群内の変化で、プラセボとの差の95%信頼区間は0を含み、60 mg群で12週目のFVCがない人は8/18（44%）だった。これは試験の失敗を意味しない。第2a相の主要な目的は安全性で、FVCは副次的な指標だからである。この具体例は、「第1相を通る」と「第2相以降で効く」の間の距離が、一つの試験の中でも不確かさを残すことを示すにとどまり、AI創薬全体の成功率については何も言えない。

## 結論 {#6}

「AI創薬は第2相で止まる」という主張が、第2相の成功率の測定としてどこまで言えるかは、今回読んだ範囲では、小さな標本と途中の集計にとどまる。第2相の成功、第2相の完了、追跡資産に占める割合は、同じ量ではない。同じ数値を使う記事が増えても、独立した結果が増えたことにはならない。「律速は臨床にある」という議論の一致は、その仮説を測定で支持する証拠とは分けて評価する必要がある。

## 限界 {#_2}

- Jayatungaらの論文は要旨のみ。「成功」の定義と、第2相の分母・分子は、原著で確認していない。
- ASCO抄録とIQVIAの報告書は、二次資料とブログによる。ASCO抄録はそのものを取得できなかった。
- XとLinkedInの投稿、Redditは直接読めていない。Fast Companyの記事は取得できなかった。
- ProMarketのBCGの分析は、記事の記載の転載で、原文は読んでいない。
- Exscientia、Schrödinger、BCGの更新版、創薬の専門誌による集計は検索していない。読んだ記事は4本で、代表性は主張しない。


## データとコードの公開状況

確認範囲は [sources.md](shared/ai-drug-claim-chain/sources.md)、派生計算は [numbers.py](shared/ai-drug-claim-chain/numbers.py) と [results/summary.json](shared/ai-drug-claim-chain/results/summary.json) に記録した。独自の臨床試験集団の再解析は行っていない。

## 参照 {#article-references}

1. <span id="ref-1"></span>Jayatunga MKP, Ayers M, Bruens L, Jayanth D, Meier C. How successful are AI-discovered drugs in clinical trials? A first analysis and emerging lessons. Drug Discov Today. 2024;29(6):104009. [doi:10.1016/j.drudis.2024.104009](https://doi.org/10.1016/j.drudis.2024.104009). Abstract only.

2. <span id="ref-2"></span>Santoro MA. Pharma's AI Boom Has Bet on the Wrong Bottleneck. ProMarket. 2026 Jul 2. [Article](https://www.promarket.org/2026/07/02/pharmas-ai-boom-has-bet-on-the-wrong-bottleneck/).

3. <span id="ref-3"></span>Trey. Clinical trials are the new bottleneck. Trey's Thoughts on Healthcare Markets & Technology. 2026 Apr 1. Partially accessible; source inventory linked above. [Article](https://www.onhealthcare.tech/p/clinical-trials-are-the-new-bottleneck).

4. <span id="ref-4"></span>Epstein WN, Niazi SK. AI Can Invent Drugs Faster. It Still Has to Prove They Work. Petrie-Flom Center, Harvard Law School. 2026 Aug 4. [Article](https://petrieflom.law.harvard.edu/2026/08/04/ai-can-invent-drugs-faster-it-still-has-to-prove-they-work/).

5. <span id="ref-5"></span>Alsumidaie M. AI is clearing Phase I. That's the wrong finish line. The Clinical Trial Vanguard. 2026 Aug 11. [Article](https://www.clinicaltrialvanguard.com/clinical-bellwether/ai-is-clearing-phase-i-thats-the-wrong-finish-line/).

6. <span id="ref-6"></span>Haque W, Sai-Palm K, Kasparcova MZ, Rana I, Verlingue L, Garassino MC, et al. Clinical-stage AI-enabled therapeutic assets: An industry-wide analysis of scale, clinical progression, and company characteristics. J Clin Oncol. 2026;44(16_suppl):11072. [doi:10.1200/jco.2026.44.16_suppl.11072](https://doi.org/10.1200/jco.2026.44.16_suppl.11072). Conference abstract; numerical content used via [secondary commentary](https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026).

7. <span id="ref-7"></span>IQVIA Institute. IQVIA Institute’s Global R&D Trends 2026 report finds credible signal on AI-enabled programs. 2026 May 14. [Commentary](https://www.iqvia.com/blogs/2026/05/iqvia-institutes-global-r-and-d-trends-2026-report-finds-credible-signal-on-ai-enabled-programs).
