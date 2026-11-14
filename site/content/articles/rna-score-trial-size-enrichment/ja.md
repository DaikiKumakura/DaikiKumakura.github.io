**QOI：RNA基盤モデルが作る患者スコアは、公表されたPOPLAR試験での結果（12か月無増悪生存の割合）が成り立つと仮定したとき、第3相試験の必要症例数をどれだけ減らすか。減るとすれば、予後調整、濃縮、交互作用検定のどれによるか。**

**COU：「AIのスコアで臨床試験を小さくできる」という主張を、設計の種類とその前提に分けて読むための計算である。Ladonそのものの性能評価でも、特定の試験計画への助言でもない。**

QOI（Question of Interest）は本稿が答える問い、COU（Context of Use）はその答えの使い道である。

**答え：公表された4つの割合が成り立つなら、減るのは主に「スコアが高い患者だけを組み入れる」設計（濃縮）であり、予後調整ではない。濃縮は、検証する主張を高スコア群の効果に限る設計でもある。** 12か月無増悪生存（PFS12）の差で80%検出力に必要な症例数を計算すると、全員を組み入れる設計は3,305人、スコアで調整した解析は3,220人（2.6%減）、スコア高群だけを無作為化する濃縮設計は258人（スコアの測定対象としては516人）だった。濃縮の効果は、スコアで調整する効果とは大きさも意味も異なる。ただし、この結論は出典の4つの割合が各群48人程度の標本で推定されたと仮定した場合の計算に強く依存する。その標本誤差を入れると（一様事前分布のBeta抽選）、濃縮設計の必要症例数は中央値が284人でも、4分の1の確率で800人を超える。陽性的中率（陽性と判定した患者のうち本当に高効果の群の割合）が約0.57を下回るか、高スコア群での効果が公表値の約0.365倍（5.1ポイント）に縮むと、濃縮設計のために測定する人数が全員組み入れの症例数を上回る。予後調整だけで20〜30%減らすには、対照群のPFS12が0.14で差が10ポイントという設定では、予後としての群内AUC（受信者動作特性曲線下面積）が0.80〜0.86程度のスコアが要る。

略語と記号は次のとおりである。PFS12は12か月無増悪生存（その時点で無増悪で生存している状態）、ATEZOはアテゾリズマブ、DOCEはドセタキセル、AUCは受信者動作特性曲線下面積、AUROCは同じ指標を予測性能として呼ぶときの名称、ORはオッズ比、$H$/$L$はスコア高群/低群、EMAは欧州医薬品庁、CHMPはその医薬品委員会、FDAは米国食品医薬品局である。$\delta$はPFS12の差（実験群から対照群を引いたもの）で、単位は百分率の差（パーセントポイント。以下、単に「ポイント」と書き、表中ではppと表す）である。陽性的中率（PPV）は、陽性と判定された患者のうち本当に高効果の群に属する割合である。

## 背景と目的

Blank BioのLadon（RNA基盤モデル）の技術報告は、RNA発現から患者の予後や治療反応を予測すると述べ ([1](#ref-1), [2](#ref-2))、「より小さく、より効率的な試験」を目標に掲げている ([1](#ref-1))。ただし技術報告の本文には、検出力や必要症例数の計算は示されていない ([1](#ref-1))。

技術報告は、POPLAR試験（アテゾリズマブ対ドセタキセル、非小細胞肺がんの二次治療の第2相無作為化試験で、アテゾリズマブ144人、ドセタキセル143人を無作為化） ([3](#ref-3)) に、別の5試験（OAK ([4](#ref-4)) を含む）で学習した「治療効果の違い」を表すスコアを適用した結果を載せている ([1](#ref-1))。報告の本文では、アテゾリズマブ群でスコアが高い患者の28%、低い患者の6%が12か月時点で無増悪だった。ドセタキセル群では14%と13%で、ほぼ同じだった ([1](#ref-1))。この4つの割合を、以後「アンカー」と呼ぶ。

スコアが試験の規模を変える経路は、少なくとも3つある。第一に、予後に関わる共変量で調整して推定の精度を上げる方法で、米国FDAの指針は、予後に関する共変量が効率を上げる点を主題にしている ([5](#ref-5))。欧州医薬品庁（EMA）のCHMPが適格性意見を出したPROCOVAは、過去の対照群の資料で作った予後スコアを使う線形調整で、対象は連続量の評価項目である ([6](#ref-6))。線形調整の研究では、臨床的に現実的な説明力のある予後モデルなら症例数を10〜30%減らせると報告されている ([7](#ref-7))。二値の評価項目では、共変量で調整した推定値を共変量について平均して周辺効果にすると、調整が効率を上げうることが示されている ([8](#ref-8))。第二に、効果が見込める患者だけを組み入れる濃縮で、FDAの指針がある ([9](#ref-9))。Simonらは、無作為化する人数とスクリーニングする人数の両方で、濃縮と全員組み入れの効率を比較する式を導いた ([10](#ref-10), [11](#ref-11))。第三に、スコアと治療の交互作用を検定する設計で、全体効果と同じ大きさの交互作用を同じ検出力で検出するには4倍の症例数が要るとされる ([12](#ref-12))。予後を表すスコアでリスクの高低ごとの治療効果を調べる方法（リスクモデリング）と、治療との交互作用を組み込んで効果を予測する方法（エフェクトモデリング）の区別は、PATH声明が整理している ([13](#ref-13))。

これらの結果は、いずれも別の対象と条件で得られたものである。本稿は、上のアンカーという実在の数値の組を入れて3つの経路を同じ尺度で並べ、どれがどれだけ症例数を動かすか、その数値がどれだけ不確かかを計算する。新しい統計手法の提案ではなく、既知の式の適用である。

## 方法

### 入力：4つの割合と仮定

入力は、Ladonの技術報告の本文から読み取った4つの割合と1つの人数だけである（取得日2026年11月14日。原図は確認していない）。PFS12は、ATEZO群でスコア高群0.28、低群0.06、DOCE群で高群0.14、低群0.13である ([1](#ref-1))。スコアの閾値はRNA測定のある192人全体の中央値で、2群で共通である ([1](#ref-1))。このため高群の割合は0.5とした。

報告の本文には、4つの群それぞれの人数、信頼区間、検定結果は書かれていない。POPLARのRNA測定ありの標本が192人であること、ATEZO群の評価可能な95人のうち87人を含む図があることは書かれているが、後者がPFS12の図の分母かどうかは確認できなかった ([1](#ref-1))。そこで1群を $192/4=48$ 人と仮定し、24〜96人でも計算した。この仮定は本稿の入力であり、報告の値ではない。

### 評価項目と設計

評価項目は、12か月後にPFSであるか否かの二値とし、全員が12か月まで追跡されて状態が分かると仮定した（打ち切りの影響は後で別に評価する）。推定対象は、解析対象集団でのPFS12の周辺リスク差 $\delta=p_1-p_0$ である（$p_1$、$p_0$ は実験群と対照群のPFS12）。有意水準は両側5%、検出力は80%、割付比は1:1とし、正規近似を使った。$z=z_{0.975}+z_{0.8}$ とする。

D1（全員組み入れ・調整なし）は、2群の割合の差の標準誤差から次の症例数（1群あたり）になる。

$$n_{\mathrm{arm}}=\frac{z^2\,[\,p_1(1-p_1)+p_0(1-p_0)\,]}{\delta^2}\tag{1}$$

D2（全員組み入れ・スコアで調整）は、各群の中でスコア別に割合を推定し、スコアの分布で平均して周辺効果を出す推定量で、共変量で調整した推定値を共変量について平均して周辺効果にする手順に対応する ([8](#ref-8), [14](#ref-14))。スコア群の構成は標本ごとに確率的とし、平均の重みは観測した割合とする。1群あたりの分散の係数は、$S$ をスコア群（$H$ または $L$）、$p_a(S)$ をスコア群ごとのPFS12として、

$$V_{\mathrm{adj}}=\mathrm{E}_S\bigl[p_1(S)(1-p_1(S))\bigr]+\mathrm{E}_S\bigl[p_0(S)(1-p_0(S))\bigr]+\tfrac12\,\mathrm{Var}_S\bigl(p_1(S)-p_0(S)\bigr)\tag{2}$$

となる。式 (1) の括弧内（$V_{\mathrm{unadj}}$）との差は、$\mathrm{Var}_S(p_1)+\mathrm{Var}_S(p_0)-\tfrac12\mathrm{Var}_S(p_1-p_0)$ である。最後の項は、スコアで治療効果が変わる（交互作用がある）と、周辺効果を出す際の平均化の分散が精度を削ることを表す。スコア群の構成を層別割付で固定すると、この項は消える。

D3（全員組み入れ・交互作用の検定）は、交互作用の対比 $\psi=(p_{H1}-p_{H0})-(p_{L1}-p_{L0})$ を4つの群に等しく割り付けて検定する。総症例数は

$$N_{\mathrm{int}}=\frac{4\,z^2\,\sum_{\text{4 cells}}p(1-p)}{\psi^2}\tag{3}$$

である。D4（濃縮、スコア高群のみ・調整なし）は、高群の2つの割合に式 (1) を当てる。測定（スクリーニング）する人数は、無作為化する人数を高群の割合 $\pi$ と測定成功率 $1-f$ で割った値である。

### 不確かさと感度

4つの割合の標本誤差は、各群の割合に独立なBeta分布（事前分布は一様。割合×人数を事象数とみなし、非整数のまま使う）を当てて200,000回描いた。1群の人数は24、36、48、72、96人で試した。一様事前分布のほかに、Jeffreys事前分布（0.5を加える）と、割合×人数を整数に丸めた事象数（13、3、7、6）でも抽選した。そのうえで、(a) 陽性的中率 $\rho$ を1から0.5まで下げる（$\rho=1$ は報告された高群そのもの、$\rho=0.5$ はスコアに情報がない場合で、濃縮でも全員組み入れでも同じ対比になる。誤って含まれる患者は低群の割合を持つとした）、(b) 高群での効果が14パーセントポイントの何倍に縮むか、(c) 陽性判定の割合、(d) 測定失敗の割合、を動かして必要症例数を再計算した。

予後調整だけの効果は、別の想定で掃引した。スコア $S$ を標準正規分布とし、PFS12のロジットが $\alpha_a+\gamma S$（2群で同じ勾配、交互作用なし）、対照群の周辺PFS12を0.14、実験群を0.24（差10ポイント）とした。$\gamma$ を0から3まで動かし、群内のAUCと必要症例数の比を数値積分（Gauss–Hermite、200点）で計算した。

### 検算

D1とD4の症例数（式 (1)）は、統計ライブラリ（statsmodels）の検出力関数（帰無仮説での分散をプールする検定）でも確かめた。D2（式 (2)）とD3（式 (3)）の症例数は、このライブラリでは確かめていない。4つの設計すべてについて、二項分布の群別カウントを使ったモンテカルロ（各40,000回。症例数は群ごとに切り上げた値で、D1は3,306人、D3は352人）で、検出力と、帰無仮説の下での第一種過誤率、95%区間の被覆率を確かめた。予後調整の式は、ロジスティック回帰の標準化推定量を20,000試験で動かして分散と照合した。打ち切りの影響は、PFS12の事象時間を指数分布とし、12か月までに脱落する割合を10%と20%とするKaplan–Meier推定で、6,000回ずつ評価した。これらはすべて著者が導出の後に書いたコードによる確認であり、盲検でも事前登録でもない。

## 結果

### 4つの設計の必要症例数

表1は、アンカーが成り立つとした場合の症例数である。全員組み入れの平均効果は3.5ポイントしかない（高群の割合が0.5のとき）。高群で $+14$ ポイント（$0.28$ 対 $0.14$）、低群で $-7$ ポイント（$0.06$ 対 $0.13$）と、効果の向きが逆の群が打ち消し合うためである。このため全員組み入れでは3,305人が要る（図1a）。

表1. アンカーでのPFS12の差を80%検出力で検出するのに必要な症例数。Randomisedは2群の合計（1群あたりではない）。D3の350人は交互作用の対比を検出する検出力であり、高群での治療効果の検出力ではない。

| Design | Effect used (pp of PFS12) | Randomised | Screened for the score |
|---|---|---|---|
| D1 all-comers, unadjusted | 3.5 | 3,305 | 3,305 (no score needed) |
| D2 all-comers, adjusted for score | 3.5 | 3,220 | 3,220 |
| D3 all-comers, interaction test | 21.0 (contrast) | 350 | 350 |
| D4 enriched (high score) | 14.0 | 258 | 516 |

![設計ごとの必要症例数（a）と、4つの割合の標本誤差を入れたときの必要症例数の分布（b）。](shared/rna-score-trial-size-enrichment/figures/fig1_designs_and_uncertainty.png)

図1. 設計ごとの必要症例数（a、対数軸）と、各群48人と仮定したときの標本誤差を入れた必要症例数の分布（b、先頭の20,000回を表示し、凡例の中央値と「検出力が得られない確率」は200,000回の値）。

スコアで調整するD2は、D1より2.6%（85人）少ないだけだった。式 (2) の分解では、アンカーでの $\mathrm{Var}_S(p_1)=0.0121$、$\mathrm{Var}_S(p_0)=0.000025$、$\mathrm{Var}_S(p_1-p_0)=0.0110$ なので、予後としての説明力（最初の2項の和0.0121）の半分弱（45%）を、交互作用が削っている（最後の項の半分0.0055）。D4はD1の約12.8分の1（258人）で、測定の人数でも約6.4分の1（516人）である。効果の差の比の二乗 $(14/3.5)^2=16$ は、分散を等しいとした場合の無作為化人数の比にあたり、Simonらが比較した枠組み ([10](#ref-10), [11](#ref-11)) の単純な場合である（式そのものは抄録しか確認していない）。二値の分散は高群の方が大きいため、本稿の比は小さくなる。D3は350人で、全体効果が小さいD1の約0.11倍にとどまる。交互作用の対比（21ポイント）が全体効果（3.5ポイント）の6倍だからで、Brookesらの4倍の目安（同じ大きさの交互作用の場合） ([12](#ref-12)) とは条件が違う。

アンカーから計算したスコアの群内AUC（二値の高低で分けた場合）は、ATEZO群で0.69、DOCE群で0.51である。治療群で予後に関係し対照群で関係しない形は、予後スコアというより治療効果の違いを表すスコアのパターンである。

### 予後調整で減る量

予後のみに関わるスコアの場合、減る量はスコアの説明力で決まる（表2、図2）。群内AUCが0.70で約8%、0.75で約13%、0.83で約23%、0.88で約33%であり、20〜30%減らすには0.80〜0.86程度のAUCが要る。この範囲は、線形調整で報告された10〜30% ([7](#ref-7)) と同じ桁にある。ただし数値は、対照群のPFS12 0.14、差10ポイント、正規分布のスコアという設定に固有で、対照群のPFS12が高ければ同じAUCでも減る割合は大きくなる。アンカーでの2.6%は、AUCを2群の平均（0.60）で見ると予後のみのスコアの曲線の近くにあるが、両者は別の仕組み（予後と交互作用）の結果で、一致は偶然である。同じ生成条件でロジスティック回帰の条件付きオッズ比を検定する場合の減る割合も、ほぼ同じだった（表2の最右列。調整なしの周辺オッズ比の検定との比）。

表2. 予後のみのスコアで減る無作為化人数の割合（対照群のPFS12 0.14、実験群0.24）。最右列のORは、条件付きオッズ比の検定を調整なしの周辺オッズ比の検定と比べた値。

| Logit slope gamma | Within-arm AUC (control) | Outcome variance explained (control) | Reduction, risk difference (%) | Reduction, conditional OR test (%) |
|---|---|---|---|---|
| 0.5 | 0.636 | 3.0% | 3.6 | 3.5 |
| 0.75 | 0.696 | 6.6% | 7.8 | 7.5 |
| 1.0 | 0.747 | 11.2% | 12.8 | 12.3 |
| 1.5 | 0.826 | 21.6% | 23.4 | 22.4 |
| 2.0 | 0.878 | 31.6% | 33.1 | 31.5 |
| 3.0 | 0.934 | 47.3% | 47.7 | 44.9 |

![予後のみのスコアでのAUCと必要症例数の減少率、およびアンカーの位置。](shared/rna-score-trial-size-enrichment/figures/fig2_prognostic_adjustment.png)

図2. 予後のみのスコア（2群で同じロジット勾配）の群内AUCと、無作為化人数の減少率（標準化推定量、リスク差）。四角は、アンカーから計算した値（AUCは2群の平均）。

### 4つの割合の不確かさ

各群48人とすると、4つの割合に含まれる標本誤差だけで、交互作用の対比（21ポイント）のBeta抽選による90%区間は3.5〜36.9ポイントになる（表3）。正規近似の95%区間は1.2〜40.8ポイントである。以下の確率は、一様事前分布の下でのBeta抽選に対する割合である。濃縮設計の高群での効果（14ポイント）が0以下になる確率は4.9%、全員組み入れの平均効果が0以下になる確率は25.4%だった。Jeffreys事前分布では4.6%と24.8%、事象数を整数（13、3、7、6）に丸めると7.0%と27.7%で、濃縮設計の必要症例数の中央値は265人と357人、75%点は738人と1,211人だった。必要症例数でみると、濃縮設計（高群のみ）の無作為化人数は、5%点で71人、中央値で284人、75%点で804人、90%点で約5,600人で、95%点は実質的に意味のある値にならない（高群の効果が0に近い抽選が5%程度ある。「検出力が得られない」は利益の向きでの定義である）。全員組み入れの中央値は3,739人で、75%点でも有限値にならない。点推定（258人）と中央値（284人）は近いが、分布の上側は極端に長く伸びる。

表3. 4つの割合を各群の人数に応じて抽選したときの不確かさ（200,000回、Beta分布、一様事前分布）。確率は抽選に対する割合。

| Patients per cell | Interaction contrast, 90% interval (pp) | P(high-group effect ≤ 0) | P(all-comers effect ≤ 0) | Enriched, randomised: median (5th percentile) |
|---|---|---|---|---|
| 24 | −4.3 to 43.3 | 12.7% | 32.4% | 307 (52) |
| 36 | 0.6 to 39.3 | 7.7% | 28.5% | 291 (62) |
| 48 | 3.5 to 36.9 | 4.9% | 25.4% | 284 (71) |
| 72 | 6.8 to 34.2 | 2.0% | 20.4% | 274 (84) |
| 96 | 8.8 to 32.4 | 0.9% | 17.1% | 271 (94) |

### 濃縮設計がスコアの劣化に耐える範囲

陽性的中率 $\rho$ が1から0.9、0.8、0.7、0.6に下がると、無作為化人数は258人から345、489、758、1,365人になり、測定の人数は516人から690、978、1,517、2,729人になる。$\rho=0.5$（情報なし）では3,305人（全員組み入れ）に戻る。測定の人数が全員組み入れの無作為化人数（3,305人）に等しくなる $\rho$ は0.574である（測定と無作為化の費用を等価とみなした比較）。高群での効果が14ポイントの0.75倍、0.5倍、0.35倍に縮むと、無作為化人数は435、917、1,789人、測定の人数は870、1,834、3,579人になり、損益分岐は0.365倍（5.1ポイント）で、0.36倍なら測定は3,393人、0.37倍なら3,222人である（図3）。

![濃縮設計の必要症例数が、陽性的中率、高群での効果の縮み、測定失敗によってどう変わるか。](shared/rna-score-trial-size-enrichment/figures/fig3_enrichment_sensitivity.png)

図3. 濃縮設計（高群のみ）の無作為化人数と測定人数。(a) 陽性的中率、(b) 高群での効果の縮み、(c) 測定失敗。破線はアンカーでの全員組み入れの無作為化人数（3,305人）。

陽性判定の割合は、測定の人数に比例して効く。割合が0.2、0.35、0.5、0.65、0.8なら、測定の人数は1,289、737、516、397、322人である（各群のリスクはアンカーのまま）。測定に失敗する割合が10、20、30、40%なら、測定の人数は573、645、737、860人に増える。全員組み入れの平均効果は高群の割合 $\pi$ の関数 $\delta(\pi)=0.21\pi-0.07$ で、$\pi=1/3$ で0になる。割合が0.35のとき平均効果は0.35ポイントで、必要症例数は約30万人になり、$\pi<1/3$ では平均効果が負になる。全員組み入れの症例数は、高スコア群の割合が0.5から偏るだけでも極端に変わる。

### 検算の結果

アンカーの症例数で、40,000回のモンテカルロの検出力は、D1が80.1%、D2が79.3%、D3が80.7%（352人）、D4が80.3%、95%区間の被覆率は95.2%、95.2%、94.9%、94.8%だった（D2の79.3%は、別に行った40万回の確認では79.9%で、偶然の範囲と考える）。帰無仮説（効果なし、スコアは予後を持つ）の下で、第一種過誤率は無作為化300人以上で5.0〜5.4%、100人では5.7〜5.9%だった。統計ライブラリの検出力関数でも、D1が0.799、D4が0.792だった。予後調整の式と、ロジスティック回帰の標準化推定量の分散は、20,000試験で2%以内に一致した（分散の比は0.961対0.964、0.879対0.873、0.677対0.669）。

12か月までに脱落する割合が10%なら、PFS12のKaplan–Meier推定で必要症例数は約7%増え（D4は258人から276人、D1は3,306人から3,540人）、20%なら約15〜16%増える（298人、3,818人）。増やした症例数での検出力は、いずれも80.2〜80.7%だった。

## 考察

アンカーが成り立つなら、症例数を動かすのは濃縮である。ただしそれは、スコアが予後を表すからではなく、スコアが治療の効果の違い（ATEZO群でのみPFS12が分かれる）を表すからである。同じスコアで調整するだけなら2.6%しか減らない。予後調整の効果は、スコアの説明力に応じて増える（表2）が、20〜30%減らすには、この設定ではAUCが0.80〜0.86程度のスコアが要る。AUCだけでは症例数は決まらない。群内AUCが0.7前後のスコアでも、予後のみなら減るのは約8%で、効果の違いを表すスコアなら濃縮で約12.8分の1になりうる。AUCは、設計、評価項目、対照群の割合が決まって初めて症例数に変換できる。技術報告のAUROCは奏効の予測であり、本稿の入力ではない。

濃縮の効果は、推定対象を変えて得られる。D4が検出するのは高スコア群での効果であり、全員組み入れの平均効果（3.5ポイント）ではない。低スコア群（0.06対0.13）の患者は、設計上、組み入れられない。この分は症例数の節約ではなく、検証する主張の範囲の変更である。比較は「同じ主張を少ない人数で」ではなく、「別の主張を少ない人数で」と読むべきである。

不確かさの結果は、点推定の数値をそのまま計画に使わないことを示す。各群48人の4つの割合の標本誤差だけで、高群の効果が0以下の確率が4.9%、必要症例数が800人を超える確率が25%ある。さらに、新しい試験でのスコアの閾値、集団、測定は報告と同一にならず、陽性的中率 $\rho$ が約0.57を下回るか効果が公表値の約0.365倍に縮むと、濃縮のために測定する人数が全員組み入れの症例数を超える（測定と無作為化の費用を等価とみなした比較）。この損益分岐は、Simonらが示した、濃縮の有利さは効果のある患者の割合と検査の正確さに依存するという構造 ([10](#ref-10), [11](#ref-11)) を、このアンカーに当てた形である。新規性は主張しない。

EMAのPROCOVAの適格性意見の対象は、連続量の評価項目、線形の共変量調整、独立した過去の対照群のデータで作ったスコアである ([6](#ref-6))。本稿のPFS12は二値で、スコアの学習データもPOPLARとは別の試験（OAKを含む）だが、設計の種類としての濃縮や交互作用検定は、この枠組みの対象ではない。FDAの調整指針についてはウェブの概要だけを確認し、指針の本文は読んでいない ([5](#ref-5))。

## 限界

- 4つの割合は、技術報告の本文から読み取った数値である。原図は確認しておらず、各群の人数と信頼区間も報告されていない。1群48人は仮定で、必要症例数と確率の全体に効く。この4つの割合がスコアの閾値や表示の選択を経て図に載った可能性（結果の良い値が選ばれる偏り）は、本文から評価できない。
- 技術報告によれば、治療効果の違いを表すモデル（benefit head）はOAKを含む5試験で学習され、POPLARに適用された。このモデルの学習にPOPLARは含まれないが、スコアの閾値はPOPLARの192人全体の中央値で決められ、高低の分割はPOPLARに対して標本内である。エンコーダの事前学習データにPOPLARが含まれるかは、本文から確認できなかった ([1](#ref-1))。本稿はスコアの妥当性を再評価していない。報告の手法欄には打ち切りを考慮した重み付きロジスティック回帰の記述があるが、4つの割合がその方法かKaplan–Meier推定によるのかは確認できなかった。これらは、4つの割合を入力とするすべての結論に関わる。
- 評価項目は二値のPFS12で、全員の12か月の状態が分かる前提である。実際の試験は、生存時間解析（ハザード比、ログランク検定、制限付き平均生存時間）を使うことが多く、その必要症例数は別に計算が要る。脱落の影響は10%と20%の2点でのみ、非情報的な脱落を仮定して評価した。この限界は、必要症例数の絶対値に関わる。
- 解析は、スコアを高低2群にした離散スコアである。連続スコアの閾値の選び方、閾値の再調整、複数の閾値の探索は扱っていない。
- 不確かさは4つの割合の標本誤差のみで、独立性を仮定した。事前分布はJeffreysと整数カウントでも試したが（中央値265人と357人）、他の選び方は試していない。新しい試験での集団・測定の違いは、$\rho$ と効果の縮みの感度で代表させた。損益分岐は、測定と無作為化の費用を等価とみなした比較である。これらは、不確かさと損益分岐に関する結論に関わる。
- 検算は導出の後に同じ著者が書いたコードによる確認で、独立した実装ではない。事前登録もない。
- 本稿の症例数は、設計の違いを比べる指標であり、特定の試験の計画値ではない。

## 結論

POPLARの4つの12か月PFSの割合が成り立つなら、症例数を大きく動かすのは濃縮（258人、測定516人、全員組み入れの3,305人に対し約12.8分の1と約6.4分の1）である。予後調整は2.6%で、対照群のPFS12が0.14、差が10ポイントという設定で20〜30%減らすには群内AUCが0.80〜0.86程度のスコアが要る。しかし4つの割合の標本誤差だけで、濃縮設計の必要症例数は中央値284人に対して75%点が804人、効果が0以下になる確率が4.9%で、陽性的中率が約0.57を下回るか効果が公表値の約0.365倍に縮むと、測定の人数が全員組み入れを超える。濃縮が検証する主張は、高スコア群での効果に限られる。「スコアで試験を小さくできる」という主張が成り立つのは、どの設計で、どの推定対象で、どの不確かさの下でかが決まったときである。

## データとコードの公開状況

再実行に必要な資料（`analysis/` のスクリプト、`outputs/` の表・図・ログ、ハッシュ一覧 `MANIFEST_SHA256.txt`、入力の出典の記録 `inputs/PROVENANCE.md`）は[配布アーカイブ](shared/rna-score-trial-size-enrichment/rna-score-trial-size-enrichment-companion.zip)に含めた。入力は技術報告から読み取った4つの割合と1つの人数のみで、個票、モデルの重み、アクセス制限のあるデータは使っていない。環境はPython 3.12.4 ([15](#ref-15))、NumPy 2.2.6 ([16](#ref-16))、SciPy 1.14.0 ([17](#ref-17))、pandas 2.2.2 ([18](#ref-18))、Matplotlib 3.9.1 ([19](#ref-19))、statsmodels 0.14.2 ([20](#ref-20)) で、乱数シードは20261114である。`python -X utf8 analysis/01_anchor_designs.py`、`02_prognostic_adjustment.py`、`03_design_simulation.py`、`04_figures_and_crosscheck.py`、`05_manifest.py` の順に実行し、`05_manifest.py --check` で表のハッシュを照合する。

## 参照

<span id="ref-1"></span>1. Byeon GW, Fradkin P, Hsu J, Nguyen V, Shi I, Tu W, Zhang M. Ladon: an RNA foundation model for predicting patient outcomes [Internet]. Blank Bio; 2026 [cited 2026 Nov 14]. Technical report (not peer reviewed). doi:10.5281/zenodo.24157116 (DOI as given for the report; resolves to Zenodo). Available from: [https://www.blank.bio/ladon-technical-report](https://www.blank.bio/ladon-technical-report). Text read through a fetch tool that returns the passages asked for; the figures were not viewed.

<span id="ref-2"></span>2. Blank Bio. Introducing Ladon: an RNA foundation model for predicting patient outcomes [Internet]. Substack; 2026 Nov 12 [cited 2026 Nov 14]. Available from: [https://blankbio.substack.com/p/introducing-ladon-an-rna-foundation](https://blankbio.substack.com/p/introducing-ladon-an-rna-foundation)

<span id="ref-3"></span>3. Fehrenbacher L, Spira A, Ballinger M, Kowanetz M, Vansteenkiste J, Mazieres J, et al. Atezolizumab versus docetaxel for patients with previously treated non-small-cell lung cancer (POPLAR): a multicentre, open-label, phase 2 randomised controlled trial. Lancet. 2016;387(10030):1837–1846. [doi:10.1016/S0140-6736(16)00587-0](https://doi.org/10.1016/S0140-6736(16)00587-0). Abstract read.

<span id="ref-4"></span>4. Rittmeyer A, Barlesi F, Waterkamp D, Park K, Ciardiello F, von Pawel J, et al. Atezolizumab versus docetaxel in patients with previously treated non-small-cell lung cancer (OAK): a phase 3, open-label, multicentre randomised controlled trial. Lancet. 2017;389(10066):255–265. [doi:10.1016/S0140-6736(16)32517-X](https://doi.org/10.1016/S0140-6736(16)32517-X). Abstract read.

<span id="ref-5"></span>5. U.S. Food and Drug Administration. Adjusting for covariates in randomized clinical trials for drugs and biological products: guidance for industry [Internet]. 2023 May [cited 2026 Nov 14]. Available from: [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/adjusting-covariates-randomized-clinical-trials-drugs-and-biological-products](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/adjusting-covariates-randomized-clinical-trials-drugs-and-biological-products). Web page summary read; the guidance text was not read.

<span id="ref-6"></span>6. European Medicines Agency, Committee for Medicinal Products for Human Use. Qualification opinion for prognostic covariate adjustment (PROCOVA) [Internet]. EMADOC-1700519818-907465; adopted 2022 Sep 15 [cited 2026 Nov 14]. Available from: [https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/qualification-opinion-prognostic-covariate-adjustment-procovatm_en.pdf](https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/qualification-opinion-prognostic-covariate-adjustment-procovatm_en.pdf). Statement and conclusion section read.

<span id="ref-7"></span>7. Schuler A, Walsh D, Hall D, Walsh J, Fisher C. Increasing the efficiency of randomized trial estimates via linear adjustment for a prognostic score. Int J Biostat. 2022;18(2):329–356. [doi:10.1515/ijb-2021-0072](https://doi.org/10.1515/ijb-2021-0072). Abstract read.

<span id="ref-8"></span>8. Moore KL, van der Laan MJ. Covariate adjustment in randomized trials with binary outcomes: targeted maximum likelihood estimation. Stat Med. 2009;28(1):39–64. [doi:10.1002/sim.3445](https://doi.org/10.1002/sim.3445). Abstract read.

<span id="ref-9"></span>9. U.S. Food and Drug Administration. Enrichment strategies for clinical trials to support approval of human drugs and biological products: guidance for industry (title as in the web page heading; the page body gives the final title with "Demonstration of Effectiveness") [Internet]. 2019 Mar [cited 2026 Nov 14]. Available from: [https://www.fda.gov/regulatory-information/search-fda-guidance-documents/enrichment-strategies-clinical-trials-support-approval-human-drugs-and-biological-products](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/enrichment-strategies-clinical-trials-support-approval-human-drugs-and-biological-products). Web page read (title, date, status); the guidance text was not read.

<span id="ref-10"></span>10. Simon R, Maitournam A. Evaluating the efficiency of targeted designs for randomized clinical trials. Clin Cancer Res. 2004;10(20):6759–6763. [doi:10.1158/1078-0432.CCR-04-0496](https://doi.org/10.1158/1078-0432.CCR-04-0496). Abstract read.

<span id="ref-11"></span>11. Maitournam A, Simon R. On the efficiency of targeted clinical trials. Stat Med. 2005;24(3):329–339. [doi:10.1002/sim.1975](https://doi.org/10.1002/sim.1975). Abstract read.

<span id="ref-12"></span>12. Brookes ST, Whitely E, Egger M, Smith GD, Mulheran PA, Peters TJ. Subgroup analyses in randomized trials: risks of subgroup-specific analyses; power and sample size for the interaction test. J Clin Epidemiol. 2004;57(3):229–236. [doi:10.1016/j.jclinepi.2003.08.009](https://doi.org/10.1016/j.jclinepi.2003.08.009). Abstract read.

<span id="ref-13"></span>13. Kent DM, Paulus JK, van Klaveren D, D'Agostino R, Goodman S, Hayward R, et al. The Predictive Approaches to Treatment effect Heterogeneity (PATH) Statement. Ann Intern Med. 2020;172(1):35–45. [doi:10.7326/M18-3667](https://doi.org/10.7326/M18-3667). Abstract read.

<span id="ref-14"></span>14. Daniel R, Zhang J, Farewell D. Making apples from oranges: comparing noncollapsible effect estimators and their standard errors after adjustment for different covariate sets. Biom J. 2021;63(3):528–557. [doi:10.1002/bimj.201900297](https://doi.org/10.1002/bimj.201900297). Abstract read.

<span id="ref-15"></span>15. Python Software Foundation. Python [Software]. Version 3.12.4. 2024. Available from: [https://www.python.org/](https://www.python.org/)

<span id="ref-16"></span>16. Harris CR, Millman KJ, van der Walt SJ, Gommers R, Virtanen P, Cournapeau D, et al. Array programming with NumPy [Software, version 2.2.6]. Nature. 2020;585(7825):357–362. [doi:10.1038/s41586-020-2649-2](https://doi.org/10.1038/s41586-020-2649-2)

<span id="ref-17"></span>17. Virtanen P, Gommers R, Oliphant TE, Haberland M, Reddy T, Cournapeau D, et al. SciPy 1.0: fundamental algorithms for scientific computing in Python [Software, version 1.14.0]. Nat Methods. 2020;17(3):261–272. [doi:10.1038/s41592-019-0686-2](https://doi.org/10.1038/s41592-019-0686-2)

<span id="ref-18"></span>18. McKinney W. Data structures for statistical computing in Python [Software: pandas, version 2.2.2]. In: Proceedings of the 9th Python in Science Conference. 2010. p. 56–61. [doi:10.25080/Majora-92bf1922-00a](https://doi.org/10.25080/Majora-92bf1922-00a)

<span id="ref-19"></span>19. Hunter JD. Matplotlib: a 2D graphics environment [Software, version 3.9.1]. Comput Sci Eng. 2007;9(3):90–95. [doi:10.1109/MCSE.2007.55](https://doi.org/10.1109/MCSE.2007.55)

<span id="ref-20"></span>20. Seabold S, Perktold J. Statsmodels: econometric and statistical modeling with Python [Software, version 0.14.2]. In: Proceedings of the 9th Python in Science Conference. 2010. p. 92–96. [doi:10.25080/Majora-92bf1922-011](https://doi.org/10.25080/Majora-92bf1922-011)
