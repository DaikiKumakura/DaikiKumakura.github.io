## 要旨 {#article-abstract}

SCOT試験の公開結果から、術後補助療法3か月対6か月の有効性維持と毒性低下を再構築した。公表された調整済み無病生存（DFS）のハザード比は試験の非劣性限界を満たしたが、3年DFS差は−0.4パーセントポイント（95%区間−2.6–+1.8）だった。神経毒性のGradeがある安全性集団ではGrade ≥2の神経障害が33.4ポイント減り、同集団内の欠測Gradeの限界分析でも方向は保たれた。異なる解析集団と不明な患者内の結合転帰により、個人の便益・害や「神経障害なく無病」の結合評価項目は推定できない。非劣性は同じ有効性の証明ではない。

## 背景と目的 {#article-introduction}

治療期間を短くすると毒性が減っても、有効性には不確実性が残りうる。異なる解析集団、転帰の欠測、未測定の患者選好を1つの魅力的な数値で隠すことはできない。本記事はSCOTの公開集約結果を用いた根拠の検討であり、個人データの再解析や臨床治療推奨ではない。

無作為化した治療期間比較から、有効性を保つことと毒性を減らすことの釣合いをどこまで読めるかを問う。用途は試験設計と根拠評価とする。誤った推論は、短期治療で維持される内容を過大に述べたり、仮定を隠した効用順位を勧めたりすることにつながる。

SCOTを選んだのは、原著の有効性・安全性の表を公開資料から取得できるためである。個人データは入手しておらず、個人転帰モデル、非線形混合効果（NLME）推定、曝露反応解析は行っていない。

## 方法 {#article-methods}

### 原資料と分母 {#source-denominators}

SCOTは高リスクstage IIまたはstage III大腸がんで、治療期間3か月対6か月を無作為化した。CAPOXかFOLFOXかは割付前に選ばれた。2018年報告の調整済みDFSハザード比の非劣性限界は1.13であり、その表と本文を入力に用いた ([1](#ref-1))。表1に分母を分けて示す。

**表1　公表入力と解析分母**

| Published input | Three months | Six months |
| --- | ---: | ---: |
| Randomized participants | 3,044 | 3,044 |
| DFS intention-to-treat population | 3,035 | 3,030 |
| Three-year DFS | 76.7% | 77.1% |
| Safety cohort | 434 | 434 |
| Sensory-neuropathy grade available | 420 | 409 |
| Grade ≥2 sensory neuropathy | 103 | 237 |
| Grade ≥3 sensory neuropathy | 18 | 67 |
| Missing neuropathy grade | 14 | 25 |

取得スクリプトは公式の公開XMLを取得し、SHA-256を保存する。Grade ≥3人数と欠測は[原著Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC5883334/)から直接抽出し、Grade ≥2人数を原報告と照合した。丸めた生存割合から生存イベント数を作っていない。

### 有効性と毒性を分けた推定 {#separate-quantities}

主要比較では3つの量を別に保った。

1. 公表生存推定とその区間による、3か月から6か月を引いた3年DFS差。
2. 試験限界と比較する、3か月対6か月の調整済みDFSハザード比。
3. 安全性観測人数から再計算する、6か月から3か月を引いた神経障害リスク低下。

ハザード比を引き算して絶対リスク差にはできない。Kaplan–Meier生存推定は無作為化人数を分母とする二項割合ではなく、安全性の一部集団の毒性割合へ有効性集団の分母を使うこともできない。

神経障害について各群のWilson区間を計算し、成分を使う割合差の区間へ組み合わせた。正の差d=p6−p3の下限は、dから(p6−L6)²+(U3−p3)²の平方根を引く。上限には(U6−p6)²+(p3−L3)²を使う。観測された安全性対象内の標本不確実性を表し、安全性集団への選択は考慮しない ([2](#ref-2))。

## 結果 {#article-results}

### 有効性と神経毒性 {#efficacy-and-neuropathy}

図1と表2に、有効性と毒性の異なる量を分けて示す。

![有効性と毒性の根拠を分けた比較](shared/treatment-duration-benefit-risk/figures/benefit-risk-evidence.png)

**図1　別々の有効性・毒性推定と区間。** 解析集団と時間尺度は一致しない。

**表2　有効性と毒性の推定値**

| Quantity | Estimate | 95% interval | Interpretation |
| --- | ---: | ---: | --- |
| Three-year DFS difference, 3 − 6 months | −0.4 percentage points | −2.6 to +1.8 | Published survival estimate; both small loss and gain remain compatible |
| Grade ≥2 neuropathy reduction, 6 − 3 months | 33.4 percentage points | 26.9 to 39.5 | Recomputed in participants with available grades |
| Grade ≥3 neuropathy reduction, 6 − 3 months | 12.1 percentage points | 8.0 to 16.3 | Recomputed from the maximum-grade table |

再計算した毒性差は観測された有効性差と比べて大きいが、患者単位の交換関係ではない。有効性と安全性の対象集団と時間尺度が異なる。

![試験の非劣性限界とハザード比の不確実性](shared/treatment-duration-benefit-risk/figures/noninferiority-margin.png)

**図2　調整済みDFSハザード比。** 公表推定値と信頼区間を、事前に定めた上側限界1.13と比較した。

図2のDFSハザード比は1.006、区間0.909–1.114で、上端は限界1.13未満だった。限界に基づく推論であり、同一の有効性や任意に厳しくした限界を証明しない。逆に、絶対DFS区間は試験の主要な調整済みハザード比検定ではなく、互いに置き換えられない。

### 安全性集団内の欠測Gradeの限界 {#missing-grade-bounds}

安全性集団は各群434人である。短期治療に最も不利な割当では、3か月群の欠測14人を全員Grade ≥2、6か月群の欠測25人を全員イベントなしとする。逆の割当をもう一方の限界とした。

Grade ≥2リスク低下の限界は**27.6–36.6パーセントポイント**だった。欠測Gradeを任意に割り当てた場合の同定限界であり、信頼区間ではない。完全例の標本区間とは別に計算した。

![確認した安全性集団内の欠測Gradeに対する限界](shared/treatment-duration-benefit-risk/figures/missingness-bounds.png)

**図3　各群434人内の同定限界。** 標本信頼区間や全割付患者での限界ではない。

図3の割当でもこの集団内の安全性差の方向は保たれた。しかし、同じ限界が全無作為化患者へ適用できるわけではない。試験患者の大半は詳細安全性集団に含まれず、未測定Gradeに値を作れば別の感度問題になる。代表性、有害事象の確認、観測過程は限界として残る。

### 長期追跡の報告 {#later-follow-up}

2026年の最終報告は5年全生存（OS）82.4%を両群で示し、全体のOSハザード比は0.96、本文区間は0.86–1.07だった。方式別はCAPOX 0.90（0.78–1.03）、FOLFOX 1.10（0.93–1.34）と異なる。要旨の全体区間下限は0.8と本文と違うため、この不一致を記録して本文の値を使った ([3](#ref-3))。

長期報告は文脈を加えるが、その生存追跡を過去の毒性人数と合体させて新たな結合転帰にはしていない。方式選択は無作為化されていないので、部分集団差はCAPOX対FOLFOXの無作為化直接比較ではない。部分集団で非劣性基準を満たさなくても、それだけで劣性を証明しない。

## 考察 {#article-discussion}

3年で重要な神経障害なく無病でいる確率は魅力的な評価項目になりうる。しかし周辺生存と周辺毒性からは、誰が両方を経験したかが分からず、その確率を同定できない。仮に同じ集団の周辺割合でも追加情報か明示的な限界が必要であり、ここでは先に分母が一致していない。

2つの治療効果推定の共分散も不明である。正のnet benefitの確率を作るには、仮定を明示しなければ架空の結合分布へ依存する。本解析はその確率を生成せず、最適投与期間も選ばない。

純粋な仮想選好計算として、両方の周辺差を1集団へ移せると仮定し、便益をDFS確率とw倍のGrade ≥2神経障害回避の和とする。点推定では−0.004+w×0.3342の符号が**w=0.0120**で変わる。有効性の点推定低下を公表DFS区間の最大低下へ替えると算術的な閾値は**0.0778**になる。選好推定、効用の信頼限界、推奨値ではなく、必要な価値付けと移植仮定を可視化する計算である。

公表された有効性・毒性の周辺値は患者内の結合分布を同定せず、有効性低下と累積毒性を患者がどう重くみるかも指定しない。単一の便益・害の数値には観測以上の仮定が要る。集約された期間比較と安全性集団内の毒性感度は示せるが、個人の便益・害、連続的な期間応答、未検討期間、PKに基づく投与規則は同定できない。

## 結論 {#article-conclusion}

短期治療は観測安全性集団の神経障害を減らし、主要有効性解析は規定した非劣性限界を満たした。両者を合わせても有効性の同一性や個人net benefitは確立しない。結合した便益・害の解釈には、集団の対応、患者内の結合転帰、患者選好が依然として必要である。

## データとコードの公開状況 {#availability}

取得・抽出コード、集約入力と結果、図、実行済みノートブックを付属資料に含めた。取得した原著本文は配布物へ含めない。[README](shared/treatment-duration-benefit-risk/README.md)に手順を記し、数値は`results/extracted-inputs.json`と`results/analysis.json`へ遡れる。

[コード・集約結果・実行済みノートブックのダウンロード](shared/treatment-duration-benefit-risk/treatment-duration-benefit-risk-companion.zip)

## 参照 {#article-references}

1. <span id="ref-1"></span>Iveson TJ, Kerr RS, Saunders MP, Cassidy J, Hollander NH, Tabernero J, et al. 3 versus 6 months of adjuvant oxaliplatin-fluoropyrimidine combination therapy for colorectal cancer (SCOT): an international, randomised, phase 3, non-inferiority trial. Lancet Oncol. 2018;19(4):562–578. [doi:10.1016/S1470-2045(18)30093-7](https://doi.org/10.1016/S1470-2045%2818%2930093-7). [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC5883334/). CC BY 4.0.
2. <span id="ref-2"></span>Newcombe RG. Interval estimation for the difference between independent proportions: comparison of eleven methods. Stat Med. 1998;17(8):873–890. [doi:10.1002/(SICI)1097-0258(19980430)17:8<873::AID-SIM779>3.0.CO;2-I](https://doi.org/10.1002/%28SICI%291097-0258%2819980430%2917%3A8%3C873%3A%3AAID-SIM779%3E3.0.CO%3B2-I).
3. <span id="ref-3"></span>Iveson T, Saunders MP, Kelly C, Kerr RS, Cassidy J, Hollander NH, et al. Three versus 6 months of adjuvant oxaliplatin-fluoropyrimidine chemotherapy for colorectal cancer: final results of SCOT—an international, randomized, phase III, noninferiority trial. J Clin Oncol. 2026;44(7):534–539. [doi:10.1200/JCO-25-00621](https://doi.org/10.1200/JCO-25-00621). [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12931879/). The differing overall-HR lower limits in the abstract and main text are retained in the source audit.
