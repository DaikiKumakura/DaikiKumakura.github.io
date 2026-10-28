MTAP欠失を持つ腫瘍でPRMT5を狙うVopimetostatと、RAS(ON)阻害剤Daraxonrasibの併用が開発されている。2026年6月の公開資料で気になったのは、奏効率だけではない。**Daraxonrasib 100 mgの併用時AUCが、単剤300 mgと同程度と説明されている**点である。[Public presentation, slide 20](https://www.sec.gov/Archives/edgar/data/1819133/000119312526260679/d158334dex992.htm) ([1](#ref-1))

用量は3分の1でも、曝露は3分の1とは限らない。ただし、この記載から「併用で曝露が3倍になる」「低用量でも同じ薬効がある」と直ちに進めることもできない。AUCを比べるには、区間、採血時点、集計方法、対象集団を揃える必要がある。

本記事では、公開集計値の定義を監査したうえで、**仮に同じ定常24時間AUCだった場合**の曝露合わせを計算する。さらに、公表ヒトPopPK係数を使い、同じAUCに合わせてもピークと最低濃度がどこまで違い得るかを調べた。4,096組の仮想個体による解析である。

## 何を判断したいか {#_1}

QOI（Question of Interest）は、比較可能なAUCという仮定の下で、併用時50、75、100、150 mg QDのDaraxonrasib曝露が、単剤300 mg QDの分布とどう重なるか、そしてAUCだけで濃度推移も絞れるか、とした。QDは1日1回を指す。

COU（Context of Use）は、公開資料に基づいてPK比較の仮説と次に必要な測定を整理する研究・学習用途である。治療や試験用量の決定には使わない。新規の個人別NLME推定や、検証済みの併用PBPKモデルの構築ではない。

## 4,106という数値の定義を確認する {#4106}

2026年6月8日の公開資料では、Vopimetostat 200 mg＋Daraxonrasib 100 mg、いずれもQDのdose level 1について、Daraxonrasib AUC 4,106 ng·h/mL、n=13、CV 40.5%が示されている。見出しは膵癌と肺癌を含む集団であり、Vopimetostat 250 mg側の別PK集計ではない。[Same presentation, slides 13, 19 and 20](https://www.sec.gov/Archives/edgar/data/1819133/000119312526260679/d158334dex992.htm)

表1．公表された併用PKの定義と未確認事項。

| 項目 | 公開資料で確認できたこと | 確認できないこと |
| --- | --- | --- |
| 併用条件 | Vopimetostat 200 mg＋Daraxonrasib 100 mg QD | 250 mg側の別AUC |
| PK集計 | AUC 4,106、n=13、CV40.5% | 算術／幾何平均、CVの種類 |
| 測定条件 | 2026年5月28日データ抽出 | AUC区間、採血日、定常状態の定義、全血／血漿などの測定対象 |
| 対象 | 資料の該当欄は膵癌・肺癌 | PK評価13人の内訳・個体別共変量 |
| 単剤との比較 | 「300 mg単剤と同程度」という記述 | 同じ条件の対照群との個体別比較 |

Daraxonrasibの米国添付文書には、幾何平均Cmax 365 ng/mL、AUC 3,760 ng·h/mLとある。ただし、その段落ではAUCの積分区間や正確な測定時点が明記されていない。したがって、4,106/3,760を確定した曝露比として、さらに用量補正してDDI倍率とすることは避けた。[US prescribing information 12.3](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/220910Orig1s000Lbl.pdf) ([2](#ref-2))

2026年10月23日朝（JST）の確認時点では、同日米国東部時間7:30の説明会と10月25日のESMO発表が予告されている。以下はそれらの未発表結果を含めない、日付を固定した解析である。[10/16 presentation announcement](https://tangotx.gcs-web.com/news-releases/news-release-details/tango-therapeutics-present-updated-vopimetostat-rason) ([3](#ref-3))

## まず平均の種類だけを変えて計算する {#_2}

元資料の平均・CVの定義が未確認なので、二つの仮定を分けた。

一つは4,106を幾何平均、40.5%を幾何CVとする場合。もう一つは4,106を算術平均、40.5%をSD/平均とする場合である。いずれも対数正規分布を仮定し、後者では、

\[
\sigma^2=\log(1+CV^2),\qquad
GM=\frac{AM}{\sqrt{1+CV^2}}
\]

として幾何平均に変換した。算術平均という仮定では、GMは3,805.7 ng·h/mLになる。これは元データから平均の種類を特定した結果ではなく、未報告の定義を変えた感度解析である。

比較用にはFDA審査資料のヒトPopPK係数を再利用した。参照個体は65歳、70 kg、総ビリルビン8 µmol/L、既治療の膵癌で、CL/Fは53.8 L/h、定常相対Fは1−0.357=0.643とする。[FDA assessment report / Table 59 / PDF242 pages](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/220910Orig1s000MultidisciplineR.pdf) ([4](#ref-4))

このモデルの100 mg QDの参照定常AUCは、

\[
AUC_{100,ss}=\frac{1000\times100\times0.643}{53.8}
\]

となる。集計値をこのAUCに対応させるための**条件付きスケール**を、

\[
K=\frac{GM_{combo}}{AUC_{100,ss}}
\]

と定義した。ここでは、併用AUCもモデルと同じ全血中の同一測定対象の曝露だと仮定するが、スライドからその点も確認できない。Kには集団差、測定対象・条件差、未確認の定義差も入り得るため、臨床DDIの推定値とは呼ばない。

表2．集計方法による条件付き曝露スケール。

| 集計の仮定 | 併用AUCの仮定GM | 条件付きK | 単剤300 mgのAUCに合う計算上の量 |
| --- | ---: | ---: | ---: |
| GM＋幾何CV | 4,106.0 | 3.44（2.71–4.35） | 87.3 mg（69.0–110.5） |
| AM＋SD/平均CV | 3,805.7 | 3.18（2.52–4.03） | 94.2 mg（74.4–119.2） |

括弧は\(\log GM\pm t_{12,0.975}\sqrt{\log(1+CV^2)/13}\)から計算した近似的な位置の感度範囲である。AMからの変換では分散の推定誤差も単純化しており、原試験の信頼区間ではない。区間・集団・平均定義の不一致は、この範囲では解消されない。

計算上の曝露合わせ量は\(300/K\)である。87.3 mgや94.2 mgは処方量の提案ではない。50 mg、75 mgも仮想量で、承認錠剤を分割して作る指示ではない。添付文書は錠剤の分割を認めていない。[US prescribing information 2.2 , 3](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/220910Orig1s000Lbl.pdf)

![集計方法を変えた場合の条件付きスケール。比較可能な定常24時間AUCを仮定する。](shared/vopimetostat-daraxonrasib-exposure/figures/conditional-scale.png)

図1：点は条件付きK、線は上記の近似的な位置の感度範囲。定義が未確認という問題まで含めた区間ではなく、同等性試験でもない。

## 同じAUCに合う二つのモデル {#auc}

量を消化管\(A_g\)、中央\(A_c\)、末梢\(A_p\)に分け、経口入力に0.305時間のラグを置く。

\[
\dot A_g=-k_aA_g,\qquad
\dot A_c=k_aA_g-\frac{CL+Q}{V_c}A_c+\frac{Q}{V_p}A_p,
\]
\[
\dot A_p=\frac{Q}{V_c}A_c-\frac{Q}{V_p}A_p,\qquad
C(t)=1000A_c/V_c.
\]

時間h、量mg、濃度ng/mL。濃度は全血中であり、血漿・非結合・腫瘍内濃度へ読み替えない。見かけのPK係数に対し、定常相対Fを入力へ1回だけ適用した。

表3．再利用したPK係数と仮想個体の設定。

| パラメータ・仮想個体 | 値・扱い |
| --- | --- |
| CL/F、Vc/F、Q/F、Vp/F | 53.8 L/h、516 L、26.1 L/h、255 L |
| ka、Tlag | 0.735 /h、0.305 h |
| 160 mg以下のka効果 | 公表カテゴリ式から2.49倍。効果なしも別計算 |
| η分散（CL、Vc、ka） | 0.139、0.168、0.847 |
| η共分散（CL–Vc） | 0.0949。その他は0と仮定 |
| 個体数・seed | 4,096組、20261023 |
| 共変量・誤差 | 参照共変量固定、残差誤差なし |

出典は同Table 59。相対Fの初期時間関数が完全には確認できないため、今回は定常状態のみを比較する。個体別係数は\(\theta_i=\theta\exp(\eta_i)\)、ηは上記の共分散を持つ正規分布とし、同じηを全条件に与えた。これは実際の併用集団を復元したものではない。

二つの構造シナリオを置く。

1. **入力スケール型**：投与後の相対入力をK倍し、消失・分布係数は変えない。
2. **CLスケール型**：CL/FをKで割り、入力・分布係数は変えない。

どちらでもAUCはK倍になる。しかし後者では消失の時間スケールも変わる。AUC一つからこの二つは区別できない。これは実際のF上昇やCYP阻害を同定したモデルではなく、**AUCだけでは決まらない波形を調べるための仮想構造**である。相対入力の倍率は絶対Fではない。

Vopimetostatの非臨床公開資料は、治療濃度でのCYP・輸送体DDIリスクを低いと予測している。これも臨床DDIがない証明ではないが、今回のAUCから「強いCYP3A阻害」と断定する根拠にもならない。[TNG462 nonclinical materials, PDF p. 15](https://www.tangotx.com/wp-content/uploads/TNG462-First-time-disclosure-ACS-August-2023.pdf) ([5](#ref-5))

## 100 mgのAUCが似ていても波形は似るとは限らない {#100-mgauc}

以下は4,106をGMと仮定した中心シナリオである。比の分母は同じ仮想個体の単剤300 mg QD。

表4．同じAUCスケールを持つ構造シナリオの曝露比。

| 併用Daraxonrasib量 | AUC24比 | 入力型Cmax比 | CL型Cmax比 | 入力型最低濃度比 | CL型最低濃度比 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 50 mg QD | 0.573 | 0.668 | 0.397 | 0.545 | 1.07 |
| 75 mg QD | 0.859 | 1.00 | 0.596 | 0.818 | 1.61 |
| 100 mg QD | 1.15 | 1.34 | 0.794 | 1.09 | 2.14 |
| 150 mg QD | 1.72 | 2.00 | 1.19 | 1.64 | 3.22 |

表は個体内比の中央値。AUC比に個体差がないのは、全個体に同じKを使い、線形収支で比を取るためである。臨床予測が精密だからではない。最低濃度は24時間内の最小値で、ラグがあるため服薬直前とは限らない。

100 mgのAUC比はどちらも1.15だが、Cmax比の中央値は入力型1.34に対しCL型0.794、最低濃度比は1.09に対し2.14となった。入力型のCmax比の5–95パーセンタイルは1.21–1.50、CL型では0.616–1.03である。**同じAUC合わせが、ピーク合わせにもトラフ合わせにもなるとは限らない。**

![二つの構造シナリオによる、単剤300 mgに対する個体内曝露比。](shared/vopimetostat-daraxonrasib-exposure/figures/paired-exposure.png)

図2：点は中央値、線は条件付き個体差の5–95パーセンタイル。Kの位置の不確実性や、平均の種類の違いはこの線に混ぜていない。両モデルは可能性の例であり、真の波形を挟む上下限でもない。

## 集団の端を見ると候補の違いが見える {#_3}

平均だけでなく、単剤参照集団のAUCの5・95パーセンタイルを下回る／上回る割合も計算した。この参照範囲は薬効や毒性の閾値ではない。

表5．単剤参照分布の端を超える仮想個体割合。

| 併用量 | GM仮定：参照P05未満 | GM仮定：参照P95超 | AM仮定：参照P05未満 | AM仮定：参照P95超 |
| --- | ---: | ---: | ---: | ---: |
| 50 mg QD | 44.2% | 0.07% | 52.7% | 0.05% |
| 75 mg QD | 10.7% | 1.90% | 14.6% | 1.15% |
| 100 mg QD | 2.08% | 10.7% | 3.61% | 7.25% |
| 150 mg QD | 0.05% | 43.6% | 0.17% | 35.8% |

4,096個体の経験的な割合であり、下回ることを無効、上回ることを危険とは解釈しない。同じAUCになる二つの構造ではこの割合も一致する。濃度推移の不確実性は、この表だけでは見えない。

![同じAUCの二つの濃度波形と、単剤参照分布の端を超える割合。](shared/vopimetostat-daraxonrasib-exposure/figures/shape-and-tails.png)

図3：左は参照共変量、η=0の定常波形。同じAUCなのは100 mg併用の二つのモデル同士であり、単剤300 mg参照のAUCとは異なる。右は平均の種類を変えたAUC分布の比較で、治療域や有害事象発生率を示す図ではない。

この仮定の下では、50 mgは参照より低いAUC側へ多く移り、150 mgは高い側へ多く移る。75 mgと100 mgは、その間を検討する候補になる。ただし、これは安全性・有効性を最適化した用量選択ではない。

## どの不確実性を計算に入れたか {#_4}

表6．感度分析に含めた不確実性と残る制約。

| 不確実性 | 実施したこと | 残る制約 |
| --- | --- | --- |
| 平均・CV定義 | GM/GCVとAM/CVを別計算 | 元資料の定義を確定していない |
| 小標本の集計位置 | n=13から近似範囲を計算 | 個人データ、欠測・選択の影響は不明 |
| 個体差 | 公表η分布でpaired比較 | 併用集団の共変量分布・Kの個体差なし |
| 波形の構造 | 入力型／CL型 | 二つで全可能性を網羅しない |
| 低用量吸収 | ka効果あり／なし | 併用時に同じ効果が成立するか不明 |
| 用量–AUC関係 | 100 mgを固定し指数0.8・1・1.2のシナリオ | 実測した併用用量指数ではない |

中心シナリオではKを50–150 mgで一定にした。特に50 mgは添付文書が近似的な用量比例性を記す80–300 mgの範囲外である。用量指数の感度は、その外挿を検証済みにするものではない。

集計位置の近似範囲を使うだけでも、GM仮定の75 mgのAUC比は0.679–1.087となる。中心値から計算した87.3 mgを精密な選択量として扱えない理由である。また、入力型100 mgで低用量ka効果を外すと、Cmax比の中央値は1.34から1.15へ変わる。AUCだけでなく吸収構造の仮定も波形比較に影響する。

公表係数を再構成した単剤300 mgの参照Cmaxは296.7 ng/mLで、ラベルの幾何平均365 ng/mLより低い。集団や集計時点も一致していないため、今回の波形を絶対濃度の検証済み予測とはしない。Kの仮定範囲や個体差を増やしても、未確認のAUC定義や構造の問題は解消されない。

単回応答は独立のODE解、AUCは数値積分、参照分布の端は対数正規分布の解析解、極値は細かい時間格子と照合した。これは実装検証であり、併用患者での予測検証ではない。

## AUCの一致から入力と消失は分離できない {#auc_1}

公表された4,106には、区間・採血日・平均の定義が未確認という問題がある。今回の計算は、その不確かさを仮定として残したまま行っている。同じAUCに合う二つの構造が異なる波形を作るため、値を合わせても入力と消失のどちらが変わったかは決まらない。

また、200 mg側の情報をVopimetostat 250 mgへ移す根拠はなく、併用開始直後や中止後の回復も定常モデルの対象外である。非対照の早期試験の奏効には未確認奏効も含まれ、今回の曝露合わせから薬理学的な相乗効果や安全性改善は証明できない。([Public presentation, slide 15](https://www.sec.gov/Archives/edgar/data/1819133/000119312526260679/d158334dex992.htm))

## データとコードの公開状況 {#_5}

入力値、解析・検査コード、8点のCSV、図3点を配布する。原資料の図や個人別臨床データは再配布しない。資料確認日は2026年10月23日朝（JST）。図は本解析から作成した。


[解析コード・入力値・集計表・再実行手順](shared/vopimetostat-daraxonrasib-exposure/combination-analysis.zip)
## 参照 {#article-references}

1. <span id="ref-1"></span>Tango Therapeutics. Vopimetostat and RAS(ON) combination data. 2026 Jun 8. [Public presentation](https://www.sec.gov/Archives/edgar/data/1819133/000119312526260679/d158334dex992.htm). Slides 13, 15, 19 and 20.
2. <span id="ref-2"></span>US Food and Drug Administration. Rasonque (daraxonrasib): US prescribing information. 2026 Aug. [Label](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/220910Orig1s000Lbl.pdf). Sections 2.2, 3 and 12.3.
3. <span id="ref-3"></span>Tango Therapeutics. Tango Therapeutics to Present Updated Vopimetostat + RAS(ON) Combination Data at European Society For Medical Oncology (ESMO) Congress 2026. 2026 Oct 16. [Announcement](https://tangotx.gcs-web.com/news-releases/news-release-details/tango-therapeutics-present-updated-vopimetostat-rason).
4. <span id="ref-4"></span>US Food and Drug Administration. Daraxonrasib: multidisciplinary review, NDA 220910. 2026. [Review](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/220910Orig1s000MultidisciplineR.pdf). Table 59, PDF p. 242.
5. <span id="ref-5"></span>Cottrell K. Discovery of TNG462: a highly potent and selective MTA-cooperative PRMT5 inhibitor synthetic lethal for MTAP deleted cancers. ACS National Meeting. 2023 Aug 16. [Presentation](https://www.tangotx.com/wp-content/uploads/TNG462-First-time-disclosure-ACS-August-2023.pdf). PDF p. 15.
