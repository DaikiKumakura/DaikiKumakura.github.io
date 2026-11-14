**QOI：どの程度、消失半減期は経口低分子薬の承認された投与頻度（1日1回かどうか）を説明するか。**

**COU：新しい経口薬の用法を考えるとき、半減期の値を「1日1回か複数回か」の目安に使えるかどうかの判断材料にする。承認された薬の記述であり、用法の決定や因果の主張には使わない。**

QOI（Question of Interest）は本稿が答える問い、COU（Context of Use）はその答えの使い道である。ここでの「説明する」は、半減期と承認された投与頻度の記述的な関連の強さを指し、標本外の予測で確かめる。原因は主張しない。対象は、米国食品医薬品局（FDA）が2020–2024年に承認した経口の低分子薬104剤のうち、単一成分で半減期の値がある93剤で、薬ごとの半減期と投与頻度は Brown の論文の補足データを使った ([1](#ref-1), [2](#ref-2))。

**答え：半減期は、1日1回かどうかの弱い手がかりにとどまる。** 半減期が長いほど1日2回以上の投与は少ない傾向があった（半減期が2倍になるごとのオッズ比 0.78、95%区間 0.58–0.98。区間の上端は1に近い）。しかし1剤ずつ除いて予測する標本外の評価では、常に基準率（93剤中29剤、31%）で予測する場合との差を示せなかった（Brier スコア 0.216 対 0.219）。「情報がない」とは言えないが、小さな差は区別できない。1日2回以上の割合は、半減期が6時間未満で42%（24剤中10剤）、24時間以上で24%（34剤中8剤）で、向きは薬物動態の見立てと合う。一方、6時間未満で1日1回の薬が14剤、24時間以上で1日2回以上の薬が8剤あり、どちらの群にも向きが逆の薬が一定数いる。

略語は次のとおりである。QD は1日1回、BID は1日2回、TID は1日3回の投与。FIC（first-in-class）は新規の作用機序の薬。orphan は希少疾病用医薬品の指定。$t_{1/2}$ は消失半減期（時間）。M0、M1、M2 は後述のモデルである。

## 背景と目的

Brown は、2020–2024年にFDAが承認した経口の低分子薬104剤について、用量、投与頻度、ヒトの薬物動態、薬物相互作用を集計した ([1](#ref-1))。承認された投与頻度は QD が67%、BID が28%、TID が4%で、週1回の tovorafenib 1剤（1%未満）が含まれる（原著の本文、第1節と Figure 1）。FIC の薬は BID または TID が50%、そうでない薬は19%、orphan の薬は41%、そうでない薬は20%と報告されている（原著の要旨と第1節の本文）。半減期は104剤で中央値 14.8 時間で（[原著の Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl3)）、半減期の値は排泄相の半減期、平均、実効半減期、母集団薬物動態の推定など、出典ごとに定義が違う ([1](#ref-1))。

半減期は血中濃度が半分になるまでの時間であり、半減期が短い薬ほど濃度が速く下がる。そのため投与間隔を短くする必要が出やすいという見立ては、検証すべき仮説である。本稿は、この見立てが承認された薬の実際の投与頻度にどの程度当てはまるかを、半減期だけを入力にして数える。なぜその薬がその用法に決まったかは、このデータに含まれず、本稿は扱わない。

## 方法

### データと分類

入力は、Brown の論文の補足データ `jm5c02863_si_002.xlsx` で、2枚のシート（`Sheet1`、`Dose_and_Class`）からなる ([2](#ref-2))。著者の元のファイルは再配布しない（入手方法と SHA256 は配布資料に記録した）。`Dose_and_Class` の104行を、承認された1つの項目（エントリ）として扱い、配合剤も1エントリとした。

投与頻度は `Dose_and_Class` の表記を QD（「QD (or less)」や 21日投与7日休薬のような周期投与を含む）、BID、TID、週1回に正規化した。転帰は、BID または TID を1（1日2回以上）、QD または週1回を0とした。「QD or BID」と表記された maralixibat の1剤は、主解析から除き、感度解析で両方の符号を試した。FIC と orphan は `Dose_and_Class` の列を使い、`Sheet1` の列と照合した。

半減期は、主解析では親薬物の値を使った。値は文字列で、範囲（「32 to 57」）、日単位（「6-9 days」）、平均±SD、患者集団の値が混ざるため、範囲は下限と上限の幾何平均、日は 24 倍して時間にし、解析前に94種類の文字列すべてが読めることを確認した。配合剤（10エントリ）は、成分ごとに半減期が違い、投与頻度は配合全体で決まるため、主解析から除いた。主解析の集合は、単一成分で、半減期の値があり、投与頻度の表記が1つに決まる93エントリ（以下、93剤）である。

### 半減期の区分

半減期を、3時間未満、3–6、6–12、12–24、24–48、48時間以上の6区分に分け、区分ごとに BID または TID の割合と Wilson の95%区間を求めた ([3](#ref-3))。

### 予測モデルと評価

転帰は2値（1日2回以上かどうか）で、ロジスティック回帰を使った。M0 は基準率（学習データの割合）、M1 は半減期の対数（底2）だけ、M2 は M1 に FIC、orphan、腫瘍領域か否か、活性代謝物の有無の4項を足したモデルとした。モデルの探索はこれ以上していない。弱い L2 正則化（逆強度 C = 100）を全モデルに使った。

評価は、1エントリずつ除いて学習し、除いたエントリを予測する leave-one-out（LOO。各エントリは別の薬で、同じ成分を学習と評価に跨がせない）と、疾患群ごとに除く leave-one-disease-group-out（LOGO。腫瘍、神経、代謝・腎・心血管、感染症、免疫・消化器、その他の6群）で行った。指標は、Brier スコア（予測確率と実際の結果の二乗誤差の平均。小さいほど良い）([4](#ref-4))、対数損失（予測確率の対数尤度の符号を逆にした平均で、単位は nats。小さいほど良い）([5](#ref-5))、AUC（ROC 曲線下面積。予測の順位づけの指標）、校正の切片と傾き ([6](#ref-6)) で、すべて標本外の予測をまとめて計算した。区間は、エントリを2,000回再標本化するパーセンタイルのブートストラップ ([7](#ref-7)) で、標本外の予測は固定したまま（再標本ごとにモデルを当てはめ直さない近似）である。この近似は、学習データの揺らぎによる不確実性を含まないため、区間は実際より狭めに出る向きに偏る。乱数シードは 20261114 とした。

半減期の係数（傾き）の区間だけは、再標本ごとにモデルを当てはめ直して求めた。半減期6、8、12時間のどれかを閾値とし、閾値未満を「1日2回以上」と予測する規則も評価した。この規則の成績は、正確度に加えて、陽性的中率（PPV。「1日2回以上」と予測した薬のうち実際にそうだった割合）と陽性尤度比（LR+。感度÷（1−特異度））も求めた。

### 参照曲線

投与後のピーク濃度が投与間隔の終わりにどれだけ残るかを、1コンパートメントで瞬時に吸収され一次の消失をする場合の $2^{-\tau/t_{1/2}}$（$\tau$ は投与間隔、時間）と置いた。線形なモデルでは、反復投与の蓄積は絶対濃度を上げるが、定常状態の谷とピークの比 $2^{-\tau/t_{1/2}}$ は変えない。吸収が遅い薬、非線形な薬、薬効の遅れ、活性代謝物は含まない。これは半減期から決まる参照であり、データに当てはめていない。

### ラベルの照合

解析の前に、補足データの行を見たうえで、承認年が散らばり、頻度や半減期の表記が典型的でない薬を含むように10エントリを選び、現在の米国の添付文書（DailyMed）の投与頻度と半減期をワークブックの値と照合した。選んだのは selpercatinib、finerenone、avacopan、maralixibat、futibatinib、olutasidenib、ganaxolone、daprodustat、ritlecitinib、tovorafenib である ([8](#ref-8))。10剤のうち8剤（selpercatinib、finerenone、avacopan、futibatinib、olutasidenib、ganaxolone、daprodustat、ritlecitinib）は、後述の図5の22剤に含まれる。代表標本ではない。

### 解析計画の記録

分類の定義、曖昧な表記の扱い、半減期の区分の境界、閾値、照合する10剤は、補足データの行を一通り見た後（半減期の値を含む）、モデルを当てはめる前に配布資料の README に書いた。データに対して盲検ではなく、この記録には時刻、ハッシュ、コミットがないため、決めた時期は外から確かめられない。最初の結果を見た後に加えた解析は、承認後に撤回された薬を除く感度解析、閾値の規則の陽性的中率と陽性尤度比、LOO の基準率の人為的な悪化の確認である。

## 結果

### データの照合

表1は、ワークブックから数え直した値と、Brown が本文で報告した値の比較である（`analysis/01_build_dataset.py`）。投与頻度の割合、FIC と orphan の別の割合は一致した（maralixibat を QD として数えると完全に一致する。表の注を参照）。承認年ごとの件数は、2022年と2023年で1件ずつ違った（ワークブックは13件と24件、本文は12件と25件）。原因は追っていない。

表1. ワークブックから数え直した値と Brown の本文の値。右列の括弧は、原著の中で値が書かれている場所である。

| Item | Recounted from the workbook | Reported in the original article (location) |
|---|---|---|
| Entries | 104 | 104 (Abstract) |
| Entries per approval year (2020, 2021, 2022, 2023, 2024) | 22, 24, 13, 24, 21 | 22, 24, 12, 25, 21 (text introducing original Table 1) |
| Once daily (QD, including "QD or less") | 69 (66.3%) | 67% (section 1 text) |
| Twice daily (BID) | 29 (27.9%) | 28% (section 1 text) |
| Three times daily (TID) | 4 (3.8%) | 4% (section 1 text) |
| Less often than once daily | 1 (1.0%, tovorafenib weekly) | <1% (section 1 text) |
| Labelled "QD or BID" | 1 (maralixibat) | not stated |
| BID or TID among FIC / non-FIC entries | 21/42 (50.0%) / 12/61 (19.7%) | 50% / 19% (Abstract; section 1 text) |
| BID or TID among orphan / non-orphan entries | 24/58 (41.4%) / 9/45 (20.0%) | 41% / 20% (Abstract; section 1 text) |
| Half-life, median (quartiles) | 15.0 h (5.7–32.0 h), n = 93 single-ingredient entries | 14.8 h (6–30.8 h), n = 104 (original Table 3) |

注：QD、BID、TID、FIC は本文冒頭で定義した。頻度の割合の分母は104。FIC と orphan の割合は maralixibat を除く103エントリ。maralixibat（`Sheet1` は QD、FIC でない、orphan）を QD として数えると、QD は 70/104（67.3%）、非 FIC の BID または TID は 12/62（19.4%）、orphan の BID または TID は 24/59（40.7%）で、Brown の 67%、19%、41% と一致する。配合剤を成分のうち最短の半減期で含めると102エントリの中央値は13.0時間、最長の成分では14.0時間だった。ワークブックの `Sheet1` と `Dose_and_Class` の頻度は、maralixibat を除く103エントリで一致し、FIC は6エントリで2列の値が食い違った（`Dose_and_Class` を使用）。orphan は食い違いがなかった。原著の位置は、[原著の Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl1) の前の本文、第1節の本文、[原著の Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl3) である ([1](#ref-1))。

図1は、データの流れである。104エントリから、配合剤10と maralixibat 1を除いた93エントリが主解析の集合で、29エントリが BID または TID、64エントリが QD または週1回だった。

![104の承認エントリから、配合剤10エントリと maralixibat を除き、主解析の93エントリ（BID または TID が29、QD または週1回が64）になる流れ。](shared/oral-drug-halflife-dosing-frequency/figures/fig1_data_audit_flow.png)

図1. データの流れ。灰色は主解析から除いたエントリ、青は主解析の集合。

### 半減期と投与頻度

図2と表2は、半減期の区分ごとの BID または TID の割合である。割合は区分によって上下し、単調には変わらなかった。3時間未満の区分は20%（10剤中2剤）と低く、3–6時間の区分が最も高く（14剤中8剤、57%）、48時間以上の区分が最も低かった（15剤中2剤、13%）。24–48時間の区分は32%（19剤中6剤）で、12–24時間の区分（18%）より高かった。半減期と転帰の Spearman 順位相関は −0.20（n = 93、p = 0.051）で、境界上の探索的な参考値である。

![半減期の区分ごとの、BID または TID の割合（Wilson の95%区間）。ロジスティック回帰の曲線、基準率、1回投与後24時間でピーク濃度がどれだけ残るかの参照曲線を重ねた図。](shared/oral-drug-halflife-dosing-frequency/figures/fig2_halflife_vs_multi_daily.png)

図2. 半減期の区分ごとの BID または TID の割合（青の点と Wilson の95%区間、点の上は件数）、半減期の対数に対するロジスティック回帰の曲線（橙）、基準率（点線）。赤の破線は、QD の投与間隔（24時間）での参照曲線 $2^{-24/t_{1/2}}$（右軸）で、1コンパートメントの仮定による。データには当てはめていない。BID または TID は「1日2回以上」の薬を指す。

表2. 半減期の区分ごとの BID または TID の割合（`analysis/02_models.py`）。

| Half-life bin (h) | Entries | BID or TID | Share | Wilson 95% interval |
|---|---|---|---|---|
| <3 | 10 | 2 | 20.0% | 5.7–51.0% |
| 3–6 | 14 | 8 | 57.1% | 32.6–78.6% |
| 6–12 | 18 | 8 | 44.4% | 24.6–66.3% |
| 12–24 | 17 | 3 | 17.6% | 6.2–41.0% |
| 24–48 | 19 | 6 | 31.6% | 15.4–54.0% |
| >=48 | 15 | 2 | 13.3% | 3.7–37.9% |

注：93エントリ（単一成分）。「>=48」は48時間以上。BID、TID は本文冒頭で定義した。

全データのロジスティック回帰（M1）の傾きは、半減期が2倍になるごとにログオッズで −0.244（オッズ比 0.78）で、再標本ごとに当てはめ直したブートストラップの95%区間は −0.540 から −0.020（オッズ比 0.58–0.98）だった。区間の上端は0に近い。当てはめた確率は、半減期2時間で0.47、6時間で0.37、24時間で0.27、96時間で0.18だった。観察された割合は、3時間未満の区分の20%から3–6時間の区分の57%へ動き、単調なロジスティック曲線とは合わない。傾きの向きは、感度解析の範囲（−0.220 から −0.294）でも変わらなかった。

### 標本外の予測

図3と表3は、標本外の予測の成績である。M1（半減期だけ）の Brier スコアは LOO で 0.216（95%区間 0.179–0.253）で、基準率 M0 の 0.219（0.182–0.256）との差は −0.003（−0.019 から 0.014）だった。対数損失の差は −0.009（−0.047 から 0.031）で、疾患群ごとに除く評価（LOGO）でも差はなかった（Brier スコアの差 0.000）。M1 の AUC は 0.575（0.456–0.698）で、0.5 を区間が含む。なお LOO の M0 は、1剤を除くたびに学習側の基準率が逆向きにずれる人為的な悪化を含み、標本内の基準率の Brier スコア（0.2146）より 0.0047 大きい。この大きさは、M1 と M0 の差（−0.003）と同程度である。

M2（半減期に4項を足したモデル）は、Brier スコアが 0.202（0.158–0.247）で、M1 との差は −0.015（−0.049 から 0.020）、AUC は 0.693（0.578–0.799）だった。差の区間は0を含み、足した4項（FIC、orphan、腫瘍領域か否か、活性代謝物の有無）で標本外の予測が良くなるとは、この数では言えない。M2 では FIC と orphan の係数の点推定が正（オッズ比 3.6 と 4.5）で、Brown が報告した割合の差と同じ向きだが、区間は求めておらず、この数値は解釈しない。この2項は疾患領域と重なる。LOGO で腫瘍群を除くと、学習データでは腫瘍領域の項が一定になり、その係数は推定できない（正則化で0に縮む）。

![モデル（M0 基準率、M1 半減期のみ、M2 半減期と4項）ごとの、標本外の Brier スコア（左）と対数損失（右）と、ブートストラップの95%区間。](shared/oral-drug-halflife-dosing-frequency/figures/fig3_model_comparison.png)

図3. 標本外の Brier スコア（左）と対数損失（右、単位は nats）。小さいほど良い。丸は LOO（leave-one-out）、四角は LOGO（疾患群ごとに除く評価）。M0 は基準率、M1 は半減期だけ、M2 は半減期に FIC、orphan、腫瘍領域か否か、活性代謝物の有無を足したモデル。区間はエントリを再標本化したパーセンタイル95%区間で、標本外の予測は固定している。

表3. 標本外の予測の成績（n = 93、29 エントリが BID または TID、`analysis/02_models.py`）。

| Evaluation | Model | Brier score (95% interval) | Log loss, nats (95% interval) | AUC (95% interval) |
|---|---|---|---|---|
| Leave-one-out | M0 base rate | 0.219 (0.182–0.256) | 0.632 (0.553–0.710) | not defined |
| Leave-one-out | M1 log2 half-life | 0.216 (0.179–0.253) | 0.623 (0.541–0.705) | 0.575 (0.456–0.698) |
| Leave-one-out | M2 M1 + FIC, orphan, oncology, active metabolite | 0.202 (0.158–0.247) | 0.584 (0.483–0.694) | 0.693 (0.578–0.799) |
| Leave-one-disease-group-out | M0 base rate | 0.218 (0.182–0.255) | 0.628 (0.553–0.706) | not defined |
| Leave-one-disease-group-out | M1 log2 half-life | 0.218 (0.180–0.256) | 0.627 (0.544–0.711) | 0.578 (0.460–0.701) |
| Leave-one-disease-group-out | M2 M1 + FIC, orphan, oncology, active metabolite | 0.197 (0.154–0.243) | 0.576 (0.469–0.691) | 0.709 (0.595–0.812) |

注：M0 は定数予測（学習データの割合）のため、AUC は計算しない。Brier スコアと対数損失は小さいほど良く、AUC は大きいほど良い。AUC は ROC 曲線下面積。

校正の傾き（標本外）は、M1 で 0.44、M2 で 0.63 で、1より小さい。予測された確率の差ほど、実際の割合は離れなかった（図4）。半減期の信号が弱いと LOO の校正の傾きは小さく出やすく、この値自体にも偏りがありうる。4群に分けた各点は約23エントリで、区間は広い。

![標本外の予測確率の四分位ごとの、予測の平均と実際の BID または TID の割合（Wilson の95%区間）。M1 と M2 を重ねた図。](shared/oral-drug-halflife-dosing-frequency/figures/fig4_calibration.png)

図4. LOO の校正。点は予測確率の四分位の群（各約23エントリ）、縦線は Wilson の95%区間。対角線が完全な校正。M1 は半減期だけのモデル、M2 は半減期に4項を足したモデル。

### 単純な閾値の規則

表4は、半減期が閾値未満なら「1日2回以上」と予測する規則の成績である。どの閾値でも正確度は、全剤を「1日1回」と予測する規則の 68.8%（64/93）と区別できなかった（6時間の規則の区間 54.4–73.5% は 68.8% を含む）。正確度は、「1日2回以上」が31%の標本では指標として偏りが大きい。6時間未満では、特異度は 78.1% だが、感度は 34.5% で、1日2回以上の29剤のうち19剤を見逃した。陽性的中率は 41.7%（24.5–61.2%）で、基準率の 31.2% よりやや高く、陽性尤度比は 1.58 だった。基準率を上回る弱い情報はあるが、区間は広い。

表4. 閾値の規則の成績（n = 93、`analysis/02_models.py`）。

| Rule: predict BID or TID if half-life is below | Sensitivity (Wilson 95% interval) | Specificity (Wilson 95% interval) | Accuracy (Wilson 95% interval) | PPV (Wilson 95% interval) | LR+ |
|---|---|---|---|---|---|
| 6 h | 34.5% (19.9–52.7%) | 78.1% (66.6–86.5%) | 64.5% (54.4–73.5%) | 41.7% (24.5–61.2%) | 1.58 |
| 8 h | 48.3% (31.4–65.6%) | 75.0% (63.2–84.0%) | 66.7% (56.6–75.4%) | 46.7% (30.2–63.9%) | 1.93 |
| 12 h | 62.1% (44.0–77.3%) | 62.5% (50.3–73.3%) | 62.4% (52.2–71.5%) | 42.9% (29.1–57.8%) | 1.66 |

注：陽性は BID または TID。PPV は陽性的中率（「1日2回以上」と予測した薬のうち実際にそうだった割合）、LR+ は陽性尤度比（感度÷（1−特異度））。全剤を QD と予測する規則の正確度は 68.8%（64/93）、「1日2回以上」の基準率は 31.2%（29/93）。

### 半減期と投与間隔の関係

表5は、投与頻度ごとの半減期と、投与間隔を半減期で割った値、投与間隔の終わりに残るピーク濃度の割合（参照曲線）である。QD の薬の半減期の中央値は 18.0 時間、BID は 9.4 時間、TID は 3.5 時間で、順に短いが、四分位範囲は大きく重なる。投与間隔を半減期で割った値の中央値は、QD が 1.33、BID が 1.28 で近く、TID だけが 2.36 と大きかった（TID は4剤）。ただし四分位範囲は、QD が 0.67–3.21、BID が 0.48–2.45 と広く重なる。投与間隔の終わりに残る割合の中央値は、QD が 0.40、BID が 0.41、TID が 0.20 だった。QD と BID が近いのは、投与間隔が2倍違う分だけ半減期の中央値も約2倍違うことの算術的な帰結に近く、事後に見つけた探索的な観察である。この計算は1コンパートメント、瞬時の吸収、一次消失の仮定による。

表5. 投与頻度ごとの半減期と、投与間隔と半減期の比（`analysis/02_models.py`、n = 93）。

| Regimen | Entries | Half-life, median (quartiles), h | Dosing interval divided by half-life, median (quartiles) | Median fraction of peak left at the end of its own dosing interval (reference calculation) |
|---|---|---|---|---|
| QD | 63 | 18.0 (7.5–36.1) | 1.33 (0.67–3.21) | 0.40 |
| BID | 25 | 9.4 (4.9–25.0) | 1.28 (0.48–2.45) | 0.41 |
| TID | 4 | 3.5 (2.5–11.5) | 2.36 (1.56–4.04) | 0.20 |
| Once weekly | 1 | 56.0 | 3.00 | 0.12 |

注：投与間隔は QD で24 h、BID で12 h、TID で8 h、週1回で168 h とした。右列は $2^{-\tau/t_{1/2}}$（$\tau$ は投与間隔）を薬ごとに計算した値の中央値で、1コンパートメントと瞬時の吸収を仮定した参照の計算であり、実測の濃度ではない。

### 半減期だけでは向きが逆になる薬

図5は、半減期が6時間未満で QD の14剤と、24時間以上で BID または TID の8剤である。前者は opicapone、ritlecitinib、trofinetide、vamorolone、daprodustat、odevixibat、finerenone、futibatinib、abrocitinib、asciminib、resmetirom、sotorasib、gepirone、momelotinib で、半減期は 0.91 から 5.7 時間だった。後者は iptacopan、pacritinib、voclosporin、selpercatinib、ganaxolone、repotrectinib、olutasidenib、avacopan で、半減期は 25 から 97.6 時間だった。これらの薬の用法が決まった理由は、ワークブックにも読んだ範囲の添付文書にも書かれていない。図5の22剤のうち、添付文書を読んだのは8剤（表6の ritlecitinib、finerenone、futibatinib、daprodustat、selpercatinib、ganaxolone、olutasidenib、avacopan）だけである。候補になりうる要因（共有結合や標的占有の持続による薬効の持続、排泄相と実効の半減期の違い、徐放製剤）は、ワークブックに該当する列がなく、検証していない。daprodustat と gepirone の2剤は、ワークブックで承認後に撤回された薬として記されている。

![半減期が6時間未満で QD または週1回の14剤（左）と、半減期が24時間以上で BID または TID の8剤（右）の半減期。](shared/oral-drug-halflife-dosing-frequency/figures/fig5_case_map.png)

図5. 半減期だけでは投与頻度の向きが合わない薬。左は半減期6時間未満で1日1回または週1回の14剤（半減期6時間未満の24剤のうち）、右は半減期24時間以上で BID または TID の8剤（半減期24時間以上の34剤のうち）。半減期の軸は対数で、単位は時間。

### ラベルとの照合

表6は、事前に選んだ10エントリの、ワークブックと現在の添付文書の照合である（`analysis/04_label_audit_compare.py`）。10剤は代表標本ではなく、全体の誤り率は推定できない。投与頻度は10剤すべてで一致した（maralixibat は添付文書が適応で分かれ、ワークブックの `Dose_and_Class` の「QD or BID」と整合する）。半減期は8剤で一致し、ritlecitinib はワークブックの 1.25 時間が添付文書の範囲 1.3–2.3 時間の下限を下回り、maralixibat はワークブックに値がなく、添付文書は 1.6 時間だった。

表6. 10エントリの、ワークブックと現在の添付文書（DailyMed）の照合。

| Entry (approval year) | Frequency in the workbook | Frequency in the current label | Half-life in the workbook | Half-life in the current label | Half-life check |
|---|---|---|---|---|---|
| selpercatinib (2020) | BID | BID (twice daily; other frequencies in paediatric and dose-reduction tables) | 32 | 32 h | agree |
| finerenone (2021) | QD | QD | 2–3 h | 2–3 h | agree |
| avacopan (2021) | BID | BID | 97.6 | 97.6 h | agree |
| maralixibat (2021) | QD or BID (Sheet1: QD) | QD for Alagille syndrome, BID for PFIC | no value | 1.6 h | workbook has no value |
| futibatinib (2022) | QD | QD | 2.9 | 2.9 h | agree |
| olutasidenib (2022) | BID | BID | 67 | about 67 h | agree |
| ganaxolone (2022) | TID | TID | 34 | 34 h | agree |
| daprodustat (2023) | QD | QD | 1–4 h | 1–4 h | agree |
| ritlecitinib (2023) | QD | QD | 1.25 | 1.3–2.3 h | below the label range |
| tovorafenib (2024) | weekly | weekly | 56 | about 56 h | agree |

注：PFIC は progressive familial intrahepatic cholestasis。半減期の単位は時間。添付文書は2025年3月から2026年11月の版（DailyMed が示す版の日付、`inputs/label_audit.csv`）。

### 感度解析

半減期の取り方、配合剤の扱い、maralixibat の符号、週1回の薬の有無、承認後に撤回された薬の有無を変えても、傾きは −0.220 から −0.294 の範囲で負のままで、M1 の LOO の Brier スコア（0.216–0.221）は、各設定の基準率（0.218–0.225）に対して 0.002–0.007 小さいだけだった（配布資料の `sensitivity.csv`）。M1 の AUC は 0.56–0.61 だった。ワークブックで撤回された薬として記された6剤（主解析に4剤）を除いた89剤でも、傾きは −0.258、Brier スコアの差は 0.004 だった。

## 考察

半減期と投与頻度の関係は、方向は薬物動態の見立てと同じ（半減期が長いほど1日2回以上が少ない）で、傾きの区間は0を含まない（オッズ比 0.58–0.98）が、上端は0に近い境界的な結果である。その大きさは小さく、標本外の予測は基準率との差が区間に収まった。半減期の区分ごとの割合も、区間が広く、単調ではない。この数では、半減期は1日1回かどうかの弱い手がかりであり、「半減期を見れば1日1回かどうか分かる」とは言えない。解析は探索的で、閾値、区分、感度解析の多重性は補正していない。

投与間隔を半減期で割った値の中央値は QD（1.33）と BID（1.28）でほぼ同じで、中央値の水準では、BID の薬の半減期が短い分だけ投与間隔も短い（表5）。しかし、この比の四分位範囲は QD で 0.67–3.21、BID で 0.48–2.45 と広く重なり、半減期の四分位範囲も大きく重なって、同じ半減期の薬で両方の頻度が承認されている。半減期以外に、頻度を左右する要因が働いている可能性はあるが、ワークブックにはその要因の列がない（吸収の速さ、薬効の持続、血中濃度の山に関連する有害事象、製剤、対象集団など）。本稿は、これらの寄与を検証していない。

M2 で足した4項は、標本外の予測の成績を良くする方向の点推定を示したが、区間は0を含み、足した項の効果を確かめた結果ではない。FIC と orphan は、疾患領域と重なる。Brown が報告した FIC、orphan と頻度の関係は、数え直しで再現した（表1）。

## 限界

- **承認された薬だけの記述である。** 開発中に別の頻度で試され、承認時に今の頻度に決まった薬、承認に至らなかった薬は含まれない。承認後に撤回された薬は含まれ、ワークブックで撤回と記された6剤のうち4剤が主解析に入る（daprodustat、gepirone、infigratinib、umbralisib）。承認された用法は、半減期と頻度が合うものが残った結果である可能性があり、半減期が頻度を決めたという因果は主張できない。
- **半減期の定義が不均一である。** ワークブックの値は、排泄相、平均、実効、母集団の推定、患者集団の値が混ざる ([1](#ref-1))。範囲の値は幾何平均を使い、下限または上限を使う感度解析で傾きの向きは変わらなかった。単回投与と反復投与の値、食事の条件、特殊集団の値の違いは調整していない。
- **用法は主な適応と用量の1つに丸めた。** 適応や年齢で頻度が変わる薬（selpercatinib、maralixibat など）は、ワークブックの1つの表記を使った。週1回、周期投与、短期投与の薬は、頻度の表記に従った。修飾放出の製剤かどうかの列がなく、短い半減期で QD の薬が徐放製剤で成立している可能性は排除できない。
- **標本が小さく、薬同士の依存を扱っていない。** 93剤のうち BID または TID は29剤で、半減期の区分や疾患群は各10–20剤程度である。同じクラス、同じ開発企業、同じ承認時期の薬は用法の設計が似るが、クラスタ化は考慮しておらず、区間は独立を仮定するため実際より狭い可能性がある。区間は標本外の予測を固定したブートストラップによる近似で、狭めに出る向きに偏る。LOGO の「その他」と「感染症」は各6剤で、差がないことの確認にはならず、判断できない。
- **除外が傾きを弱める可能性がある。** 主解析から除いた配合剤は、複数回投与の割合が高い方向にあり（9エントリのうち4エントリ）、除外が傾きを0に近づけた可能性がある（感度解析に含めた）。
- **M2 の4項の効果は同定していない。** FIC、orphan、疾患領域は互いに重なり、因果の主張はできない。M2 の係数に区間は求めていない。
- **多重性を補正していない。** 区分、3つの閾値、9通りの感度解析、Spearman の相関は、探索的な解析で、p 値や区間の補正をしていない。Spearman の p = 0.051 と傾きの区間の上端 −0.020 は境界的である。
- **参照曲線は仮定に依存する。** 1コンパートメント、一次消失、瞬時の吸収、線形の薬物動態の仮定による。半減期の値の多くは、これらの仮定が成り立たない薬（多相の消失、標的介在の消失、活性代謝物）を含む。
- **ワークブックの不一致は直さなかった。** 承認年ごとの件数が本文と1件ずつ違う点、FIC の列が6エントリで食い違う点、maralixibat の半減期がない点は、そのまま報告した。FIC は `Dose_and_Class` の列を使った。
- **ラベルの照合は10エントリだけである。** 他の94エントリは添付文書と照合していない。10エントリは代表標本ではなく、半減期の一致は8、差は1、値なしは1だったが、これを全体の誤り率に当てはめることはできない。
- **原著の Table 1 の画像は読んでいない。** 行の値はワークブックだけから得た。[原著の Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl1) は画像で、原著の本文は先頭の約7割（145,798文字のうち100,000文字まで）を読んだ。

## 結論

QOI に対し、2020–2024年にFDAが承認した経口低分子薬のうち単一成分93剤では、半減期は1日2回以上かどうかの弱い手がかりにとどまった。半減期が長いほど1日2回以上は少ない傾向があるが（オッズ比 0.78、95%区間 0.58–0.98）、標本外の評価では基準率（31%）との差を示せなかった（Brier スコアの差 −0.003、95%区間 −0.019 から 0.014）。この結果は小さな差を排除せず、半減期が6時間未満または24時間以上でも向きが逆の薬が一定数いる。

COU に関しては、半減期だけを「1日1回か複数回か」の目安に使うことは、この93剤の記述では支持されない。この結果は承認された薬の記述であり、用法の選択や、半減期が頻度を決めるという因果についての結論ではない。

## データとコードの公開状況

再実行用の資料（`analysis/` のスクリプト、`inputs/` の出典の記録とラベルの照合表、`outputs/` の集計表・図・ログ、表のハッシュの一覧 `MANIFEST_SHA256.txt`）は[配布アーカイブ](shared/oral-drug-halflife-dosing-frequency/oral-drug-halflife-dosing-frequency-companion.zip)に含めた。Brown の補足データ `jm5c02863_si_002.xlsx`（SHA256 `796452e02efe3edd647375d15d5b1911682ef44d2709499f8846387fdf950213`）は出版社の著作物であり、アーカイブに含めていない。論文のページの Supporting Information から入手し、`inputs/raw/` に置く（`analysis/01_build_dataset.py` は SHA256 が違うと止まる）。薬ごとの値を含む表（整理後のデータ、主解析の集合、標本外の予測、事例の表）は、ワークブックから `01_build_dataset.py` と `02_models.py` で再生成される。

環境は Python 3.12.4 ([9](#ref-9))、NumPy 2.2.6 ([10](#ref-10))、SciPy 1.14.0 ([11](#ref-11))、pandas 2.2.2 ([12](#ref-12))、Matplotlib 3.9.1 ([13](#ref-13))、openpyxl 3.1.5 ([14](#ref-14))、scikit-learn 1.8.0 ([15](#ref-15))、乱数シードは 20261114 である。実行は `python -X utf8 analysis/01_build_dataset.py`、`02_models.py`、`03_figures.py`、`04_label_audit_compare.py`、`05_manifest.py` の順で、`python -X utf8 analysis/05_manifest.py --check` が出力の表を一覧のハッシュと照合する。ラベルの読み出しに使った `analysis/00_label_audit_fetch.py` はネットワークが必要で、再実行には含まれない。

## 参照

<span id="ref-1"></span>1. Brown DG. What do oral drugs really look like? Dose regimen, pharmacokinetics, and safety of recently approved small-molecule oral drugs. J Med Chem. 2025 Nov 18;68(22):23751–23780. PMID: 41252611. [doi:10.1021/acs.jmedchem.5c02863](https://doi.org/10.1021/acs.jmedchem.5c02863). Full text: [PMC12670434](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/) (text read up to about 100,000 of 145,798 characters; [original Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl1) is an image and was not read; [original Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670434/#tbl3) values were read from the text).

<span id="ref-2"></span>2. Brown DG. Supporting Information: data files (jm5c02863_si_002.xlsx) for "What do oral drugs really look like?" [Dataset]. ACS Publications; 2025. [doi:10.1021/acs.jmedchem.5c02863](https://doi.org/10.1021/acs.jmedchem.5c02863). SHA256 796452e02efe3edd647375d15d5b1911682ef44d2709499f8846387fdf950213; saved by hand from the publisher site on 2026 Nov 14.

<span id="ref-3"></span>3. Wilson EB. Probable inference, the law of succession, and statistical inference. J Am Stat Assoc. 1927;22(158):209–212. [doi:10.1080/01621459.1927.10502953](https://doi.org/10.1080/01621459.1927.10502953)

<span id="ref-4"></span>4. Brier GW. Verification of forecasts expressed in terms of probability. Mon Weather Rev. 1950;78(1):1–3. DOI: 10.1175/1520-0493(1950)078&lt;0001:VOFEIT&gt;2.0.CO;2. Link: [doi.org](https://doi.org/10.1175/1520-0493(1950)078%3C0001:VOFEIT%3E2.0.CO;2)

<span id="ref-5"></span>5. Gneiting T, Raftery AE. Strictly proper scoring rules, prediction, and estimation. J Am Stat Assoc. 2007;102(477):359–378. [doi:10.1198/016214506000001437](https://doi.org/10.1198/016214506000001437)

<span id="ref-6"></span>6. Van Calster B, McLernon DJ, van Smeden M, Wynants L, Steyerberg EW; Topic Group "Evaluating diagnostic tests and prediction models" of the STRATOS initiative. Calibration: the Achilles heel of predictive analytics. BMC Med. 2019;17:230. [doi:10.1186/s12916-019-1466-7](https://doi.org/10.1186/s12916-019-1466-7)

<span id="ref-7"></span>7. Efron B. Bootstrap methods: another look at the jackknife. Ann Stat. 1979;7(1):1–26. [doi:10.1214/aos/1176344552](https://doi.org/10.1214/aos/1176344552)

<span id="ref-8"></span>8. National Library of Medicine. DailyMed: current prescribing information, read on 2026 Nov 14 [Internet]. Bethesda (MD): NLM. Labels (DailyMed set IDs): selpercatinib [7fa848ba-a59c-4144-9f52-64d090f4d828](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7fa848ba-a59c-4144-9f52-64d090f4d828); finerenone [fc726765-5d5a-4d6e-b037-b847bda9fb7c](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fc726765-5d5a-4d6e-b037-b847bda9fb7c); avacopan [c93cbc0b-29a3-46a5-9c85-41815ea5cf4a](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c93cbc0b-29a3-46a5-9c85-41815ea5cf4a); maralixibat [64000394-1ef6-4e76-8ba8-11f25ba1b167](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=64000394-1ef6-4e76-8ba8-11f25ba1b167); futibatinib [0b1332a1-0581-4707-9bf6-1eccfa39bef4](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0b1332a1-0581-4707-9bf6-1eccfa39bef4); olutasidenib [4a0c7c8b-b95f-455d-9600-b7351e4397fe](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a0c7c8b-b95f-455d-9600-b7351e4397fe); ganaxolone [d91612c4-b03a-4be4-a1ee-6a13e3b83d4e](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d91612c4-b03a-4be4-a1ee-6a13e3b83d4e); daprodustat [d82aa06e-5a33-4844-99b7-4701313455a4](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d82aa06e-5a33-4844-99b7-4701313455a4); ritlecitinib [1882f799-61b0-4813-965a-4910c4ae419c](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1882f799-61b0-4813-965a-4910c4ae419c) (two set IDs exist for this product; the first was read); tovorafenib [ea3a9631-3a66-6a7c-e053-2995a90ae2ad](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ea3a9631-3a66-6a7c-e053-2995a90ae2ad).

<span id="ref-9"></span>9. Python Software Foundation. Python [Software]. Version 3.12.4. Available from: [https://www.python.org/](https://www.python.org/)

<span id="ref-10"></span>10. Harris CR, Millman KJ, van der Walt SJ, Gommers R, Virtanen P, Cournapeau D, et al. Array programming with NumPy [Software, version 2.2.6]. Nature. 2020;585(7825):357–362. [doi:10.1038/s41586-020-2649-2](https://doi.org/10.1038/s41586-020-2649-2)

<span id="ref-11"></span>11. Virtanen P, Gommers R, Oliphant TE, Haberland M, Reddy T, Cournapeau D, et al. SciPy 1.0: fundamental algorithms for scientific computing in Python [Software, version 1.14.0]. Nat Methods. 2020;17(3):261–272. [doi:10.1038/s41592-019-0686-2](https://doi.org/10.1038/s41592-019-0686-2)

<span id="ref-12"></span>12. McKinney W. Data structures for statistical computing in Python [Software: pandas, version 2.2.2]. In: Proceedings of the 9th Python in Science Conference. 2010. p. 56–61. [doi:10.25080/Majora-92bf1922-00a](https://doi.org/10.25080/Majora-92bf1922-00a)

<span id="ref-13"></span>13. Hunter JD. Matplotlib: a 2D graphics environment [Software, version 3.9.1]. Comput Sci Eng. 2007;9(3):90–95. [doi:10.1109/MCSE.2007.55](https://doi.org/10.1109/MCSE.2007.55)

<span id="ref-14"></span>14. Gazoni E, Clark C. openpyxl [Software]. Version 3.1.5. Available from: [https://openpyxl.readthedocs.io/](https://openpyxl.readthedocs.io/)

<span id="ref-15"></span>15. Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B, Grisel O, et al. Scikit-learn: machine learning in Python [Software, version 1.8.0]. J Mach Learn Res. 2011;12:2825–2830. Available from: [https://jmlr.org/papers/v12/pedregosa11a.html](https://jmlr.org/papers/v12/pedregosa11a.html)
