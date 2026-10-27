## 要旨 {#article-abstract}

少数の免疫指標を加えたモデルは、弱い臨床比較モデルより識別性能を改善したが、外部データ由来の集団で信頼できる奏効予測にはならなかった。外部AUCは**0.554（95%区間0.367–0.725）**で、確率予測の校正も不十分だった。2つのRNAスコアは開発集団で情報を持っていたものの、外部集団への確率予測の移植は十分に成立しなかった。

## 背景と目的 {#article-introduction}

最小限の臨床情報にT-effectorと間質のスコアを加えると、免疫チェックポイント阻害薬を投与された別の尿路上皮がん集団で、報告された完全奏効・部分奏効（CR/PR）の予測は改善するか。これを解析の問いとする。用途は、追加検討に値するバイオマーカー仮説を評価する研究に限る。治療選択、個人の奏効確率、因果的な治療ベネフィット、用量の判断には使えない。

転帰との関連と治療効果の予測は区別する必要がある。両資料とも治療を受けた患者を含む。無治療群や別治療群への無作為割付はなく、転帰と関連する特徴は一般的な予後、治療感受性、RNA測定対象への選択、あるいはそれらの組合せを反映しうる。

Mariathasanらは、免疫排除の文脈も含め、T細胞エフェクター機能と間質のTGFβシグナルをアテゾリズマブ治療下の転帰へ結び付けた。バルクRNAの間質発現だけで、空間的なT細胞排除を測れるわけではない ([1](#ref-1))。Roseらは別の実臨床の尿路上皮がん集団を報告した ([2](#ref-2))。既報の生物学的仮説と集団を用いた再評価であり、新規発見や前向き検証ではない。

## 方法 {#article-methods}

### 患者と出典の確認 {#cohort-audit}

開発用の配布資料には、匿名化された347人に対応する348のRNA検体がある。1人の2検体について奏効と臨床ラベルの一致を確認し、TPM値を平均した。奏効を評価できる患者は298人で、CR/PRは68人だった。判定不明または評価不能（NE）を非奏効には割り当てず、解析から除外した。

外部資料のGSE176307では、公表された臨床集団は103人である ([3](#ref-3))。現在の加工済み行列にはRNAの列が92本あり、対応表で90列をGEO検体へ、さらに89人の患者へ対応付けられた。対応しない2列は除外した。1人の2回のRNA測定は臨床項目の一致を確認して平均した。RNAを持つ奏効評価可能例は88人だが、主要な臨床予測変数が揃うのは72人だった。外部解析の奏効数は11例であり、公表集団全体の解析ではない。

![患者数と解析対象の対応](shared/immune-outcome-validation/figures/cohort-flow.png)

**図1　患者の集計過程。** 外部の主要な完全例解析は72人・奏効11例を対象とし、公表された臨床集団の一部である。

開発用資料の元の配布サーバーは取得時に応答しなかった。そこで、IMvigor210CoreBiologiesの特定コミットに固定したミラーを使い、取得した全ファイルのURL・コミット・SHA-256を保存した ([4](#ref-4))。元の資料の著者はDorothee NicklesとRichard Bourgonである。ミラーのライセンス文書はCreative Commons Attribution 3.0 Unportedとし、元の論文も加工済み資料をCreative Commonsライセンスで自由に利用できると説明している ([1](#ref-1))。ただし、**利用できなかった元の配布サーバーとのバイト単位の一致は検証していない**。チェックサムが示すのは解析したファイルの同一性であり、原配布物としての真正性ではない。

GEOの加工済みデータはNCBIのFTP配布から直接取得した。公開されていることが、すべての参加者記録の再配布を許すとは限らない。付属資料には取得手順と集約結果を含め、患者単位の臨床行列とRNA行列は含めない。別の用途で再利用する際には、出典の利用条件と帰属表示を確認する必要がある。

資料は異なる研究集団に由来するが、匿名化識別子から患者が重複していないことまでは証明できない。統合したメタデータには個々の生検時点が十分に記録されておらず、集団全体の「治療前」という説明を患者単位の確認の代わりにしなかった。全生存期間（OS）と無増悪生存期間（PFS）の項目はあるものの、共通の評価項目・時間単位・打切りの辞書を確立できず、解析しなかった。腫瘍遺伝子変異量（TMB）も、標的パネルと測定の比較可能性を調整できていないため使わなかった。

### 特徴量と推定手順 {#features-and-estimation}

[解析計画](shared/immune-outcome-validation/analysis-plan.md)は、データの利用可能性と奏効数を確認した後、モデル推定と外部性能評価の前に作成した。盲検化した検証や前向き登録ではない。外部資料のRNAアノテーションの利用可能性から共通遺伝子集合を定めたため、遺伝子の前処理から完全に手を触れずに残した検証でもない。

臨床モデルはECOG ≥1と男性であることを使う。拡張モデルは2つの連続スコアを加える。外部集団での奏効との関連によって選択せず、閾値も最適化していない。

- **Teff8:** CD8A, GZMA, GZMB, IFNG, CXCL9, CXCL10, PRF1, TBX21.
- **Stroma19:** ACTA2, ACTG2, ADAM12, ADAM19, CNN1, COL4A1, CTGF, CTPS1, FAM101B, FSTL3, HSPB1, IGFBP3, PXDC1, SEMA7A, SH3PXD2A, TAGLN, TGFBI, TNS1, TPM1.

後者は配布資料の`gene19`シグネチャーである。間質・線維芽細胞に関連した特徴量であり、TGFβ活性や物理的な排除を直接測定するものではない。既報のPanF-TBRSの計算法を厳密に再現したものでもない。

開発データのカウントはアノテーションされた遺伝子長で割り、TPMへ変換した。同じ遺伝子シンボルのTPMは合計した。外部データの加工済みTPMは配布された値を使った。各スコアは、**24,296の共通遺伝子シンボル**の中で求めた検体内パーセンタイル順位を、対象遺伝子間で平均したものである。同順位は平均順位を与えた。27のシグネチャー遺伝子はすべて揃う。この方法は絶対量の尺度への依存を減らすが、シーケンス、アノテーション、細胞組成、検体の違いを解消しない。

確率予測モデルと標準化を式1に示す。

![ロジスティックモデルと学習データだけによる標準化](shared/immune-outcome-validation/figures/model-equation.png)

**式1　ロジスティックモデルと標準化。** 臨床予測変数と2つのRNAスコアを使い、各学習fold内、最終推定では開発データ内だけで尺度を推定する。

推定では、ロジスティック負の対数尤度の総和に、切片を除く係数の二乗和の半分を加えた値を最小化する。切片は罰則を課さず、ridge罰則を1に固定し、ハイパーパラメータ探索は行わない。意図的に小さくしたモデルを安定化する手続きであり、係数を不偏な因果効果にするものではない。

内部評価では、患者単位で層別化した5分割を10回繰り返した。特徴量の尺度推定と係数推定は各学習fold内で行い、各患者の10個の検証用予測確率を平均した。指標は、この反復交差検証（CV）の集約予測を評価する。最終係数と尺度は開発データだけで推定し、外部評価の前に[固定モデル](shared/immune-outcome-validation/results/model-frozen.json)へ保存した。評価後にもハッシュの不変を確認した。外部集団での中心化、係数更新、遺伝子選択、カットオフ最適化は行っていない。

## 結果 {#article-results}

### 識別と確率予測の性能 {#prediction-performance}

表1に、臨床モデルと免疫指標追加モデルの識別性能と確率予測スコアを示す。表中の名称は配布CSVに対応させて英語で記す。AUCはROC曲線下面積、Brierとlog lossは予測確率の誤差を表す。

**表1　識別性能と確率予測スコア**

| cohort | model | metric | value | lower | upper | n | events |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Repeated CV | Clinical | AUC | 0.509 | 0.423 | 0.588 | 298 | 68 |
| Repeated CV | Clinical | Brier | 0.173 | 0.147 | 0.199 | 298 | 68 |
| Repeated CV | Clinical | Log loss | 0.530 | 0.468 | 0.591 | 298 | 68 |
| Repeated CV | Clinical + immune | AUC | 0.645 | 0.567 | 0.720 | 298 | 68 |
| Repeated CV | Clinical + immune | Brier | 0.167 | 0.142 | 0.193 | 298 | 68 |
| Repeated CV | Clinical + immune | Log loss | 0.512 | 0.451 | 0.575 | 298 | 68 |
| External | Clinical | AUC | 0.437 | 0.284 | 0.582 | 72 | 11 |
| External | Clinical | Brier | 0.142 | 0.092 | 0.198 | 72 | 11 |
| External | Clinical | Log loss | 0.461 | 0.341 | 0.594 | 72 | 11 |
| External | Clinical + immune | AUC | 0.554 | 0.367 | 0.725 | 72 | 11 |
| External | Clinical + immune | Brier | 0.135 | 0.079 | 0.200 | 72 | 11 |
| External | Clinical + immune | Log loss | 0.445 | 0.289 | 0.624 | 72 | 11 |

区間は2,000回の患者再標本化によるパーセンタイル区間である。外部の区間は推定済み開発モデルを固定した条件付きの区間で、開発モデルの推定不確実性を含まない。内部の区間も、平均したfold外予測を固定し、CV全体を再推定していない。モデル開発全体の不確実性を網羅したものとして扱えない。

![内部評価と外部評価での識別性能](shared/immune-outcome-validation/figures/discrimination.png)

**図2　識別性能。** 開発データでの反復CV予測と、固定したモデルによる外部予測をそれぞれ評価した。

このデータで臨床比較モデルの識別性能は乏しい。免疫指標を加えると反復CVのAUCは0.509から0.645へ上がる。外部でも0.437から0.554という対応のある数値差は観測されたが、拡張モデルの絶対AUCの区間は0.5を含む。弱い比較モデルを上回ることだけでは、有用な予測とは判断できない。

**表2　拡張モデルから臨床モデルを引いた対応のある差**

| cohort | metric | delta | lower | upper | valid_bootstraps |
| --- | --- | --- | --- | --- | --- |
| Repeated CV | AUC | 0.136 | 0.071 | 0.204 | 2000 |
| Repeated CV | Brier | -0.006 | -0.015 | 0.003 | 2000 |
| Repeated CV | Log loss | -0.018 | -0.041 | 0.005 | 2000 |
| External | AUC | 0.117 | 0.019 | 0.224 | 2000 |
| External | Brier | -0.007 | -0.019 | 0.005 | 2000 |
| External | Log loss | -0.016 | -0.064 | 0.037 | 2000 |

AUCの正の差、Brierとlog lossの負の差が免疫指標追加モデルに有利な方向である。外部では条件付きの対応のあるAUC差の区間がゼロを含まないが、2つの確率予測スコアの改善区間はどちらもゼロを含む。外部の奏効が11例しかないため、頑健な予測上の追加価値は示せていない。

比較の目安として、全員にその集団で観測された奏効割合を予測すると、同じ標本内での定数確率のBrierスコアは開発で約0.176、外部で約0.129となる。外部の定数には外部転帰を使うため、説明のための基準であって運用可能な検証比較モデルではない。拡張モデルの外部Brierスコアは0.135だった。

### 校正と集団の違い {#calibration-and-shift}

**表3　外部予測の校正診断**

| model | offset_intercept | joint_intercept | slope |
| --- | --- | --- | --- |
| Clinical | -0.338 | -2.967 | -0.852 |
| Clinical + immune | 0.172 | -1.226 | 0.242 |

offset_interceptは傾きを1に固定した切片で、平均的な予測水準の校正を表す。joint_interceptとslopeは、外部転帰に対する別の診断用推定であり、固定済み予測の更新には使っていない。拡張モデルの同時推定した校正傾きは0.242に留まる。offset切片はゼロに近いが、平均リスクの一致は個人間の予測確率差が適切であることを意味しない。奏効11例でこれらの診断推定の不確実性は大きく、精密な校正の主張はできない。

![外部データでの予測確率と観測奏効割合](shared/immune-outcome-validation/figures/calibration.png)

**図3　外部校正。** 開発予測の三分位点を境界として固定し、外部の観測奏効割合をWilsonの95%区間と分母とともに示す。記述的な図であり、臨床的なカットオフの選択には使えない。

**表4　集団の構成とRNAスコア**

| cohort | n | responders | response_fraction | ecog_ge1_fraction | male_fraction | Teff_mean | Stroma_mean |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Development | 298 | 68 | 0.228 | 0.594 | 0.782 | 0.605 | 0.805 |
| External | 72 | 11 | 0.153 | 0.708 | 0.597 | 0.467 | 0.807 |

![集団間でのRNAスコア分布の違い](shared/immune-outcome-validation/figures/score-shift.png)

**図4　RNAスコア分布。** 検体内順位を使ってもTeffの分布差は残る。

Teff平均は、検体内順位を使っても0.605から0.467へ下がる。外部では奏効割合が低く、ECOG分布と性別構成も異なる。実臨床資料には、単一のアテゾリズマブの設定とは異なり、複数のPD-1/PD-L1薬が含まれる。生物学的構成の変化と、測定・選択の影響をこのデータから分離できない。外部RNA患者89人のうち17人はECOGを欠き、完全例への限定で奏効評価可能な16人を失うため、性能に偏りが生じうる。開発集団に見かけを合わせるために外部データを再中心化する根拠ではなく、未解決の移植可能性の問題である。

事前に定めた肝転移調整の感度解析は、開発の完全例271人で推定し、変更せず外部72人へ適用した。外部AUCは0.581、Brierは0.133、log lossは0.435だった。記述的な結果であり、信頼できる校正を示すものではない。外部性能から推奨モデルとして選択することもできない。開発の肝病変区分と、外部の累積的な肝転移フラグは、完全に一致した測定ではない。

## 考察 {#article-discussion}

2つの免疫指標は、この最小限の臨床比較モデルを超える奏効情報を開発集団で持っていた。固定した外部予測には小さな相対的識別性能の改善が残るが、絶対性能は弱く、確率予測スコアの改善も不確かだった。校正、検体選択、測定の移植、患者単位の出典確認が解釈を制約する。

検体採取時点、奏効の確認方法、測定の移植、参加者の由来はこの比較の限界として残る。外部の奏効11例で再校正すれば検証転帰を利用することになり、もはや独立したテストではない。

## 結論 {#article-conclusion}

本解析は生物学的仮説の検討順位を考える材料にはなる。一方、臨床的に有用なバイオマーカー、個人の奏効確率、免疫チェックポイント阻害によって誰がベネフィットを得るかは示せていない。

## データとコードの公開状況 {#availability}

付属資料には、固定した計画、出典ハッシュ、遺伝子集合、抽出・解析スクリプト、集約結果表、4つの解析図とモデル式、推定係数、整合性検査、実行済みの確認用ノートブックを含めた。患者単位の観測は別途取得する方式で、配布物には含めていない。[README](shared/immune-outcome-validation/README.md)に版、抽出上の留保、実行順を記載した。全解析は固定した入力から再実行でき、ノートブックは生成物を検査して結果を表示する。

[コード・集約結果・実行済みノートブックのダウンロード](shared/immune-outcome-validation/immune-outcome-validation-companion.zip)

## 参照 {#article-references}

1. <span id="ref-1"></span>Mariathasan S, Turley SJ, Nickles D, Castiglioni A, Yuen K, Wang Y, et al. TGFβ attenuates tumour response to PD-L1 blockade by contributing to exclusion of T cells. Nature. 2018;554(7693):544–548. [doi:10.1038/nature25501](https://doi.org/10.1038/nature25501). [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC6028240/).
2. <span id="ref-2"></span>Rose TL, Weir WH, Mayhew GM, Shibata Y, Eulitt P, Uronis JM, et al. Fibroblast growth factor receptor 3 alterations and response to immune checkpoint inhibition in metastatic urothelial cancer: a real world experience. British Journal of Cancer. 2021;125(9):1251–1260. [doi:10.1038/s41416-021-01488-6](https://doi.org/10.1038/s41416-021-01488-6).
3. <span id="ref-3"></span>National Center for Biotechnology Information. Gene Expression Omnibus: GSE176307 [Dataset]. [Series record](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE176307). The analysis used the processed TPM distribution and associated sample metadata.
4. <span id="ref-4"></span>Nickles D, Bourgon R. IMvigor210CoreBiologies [Dataset and software]. [Mirror pinned to commit 26b8d2b9e6e91f7412646db111c9e567172ed87f](https://github.com/SiYangming/IMvigor210CoreBiologies/tree/26b8d2b9e6e91f7412646db111c9e567172ed87f). Original bundle authors are credited here; the mirror was not byte-verified against the unavailable original distribution server. File hashes and source details are retained in the companion materials.
