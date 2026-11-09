300 mgを6週ごとに投与する代わりに、150 mgを3週ごとに投与する。長い期間で見た投与量は同じである。それなら、効き方を変えずにピーク濃度だけを下げられるのだろうか。

PasritamigとJNJ-9401を組み合わせる前立腺がん治療について、2026年11月8日にMark Wildgustが投稿した [(1)](#ref-1)。スポンサー発表によれば、推奨レジメンの15人中11人で前立腺特異抗原（prostate-specific antigen：PSA）が50%以上低下した。両剤の投与間隔は6週で、pasritamigは300 mg静脈内、JNJ-9401は200 mg皮下投与だった [(2)](#ref-2)。

この結果を、投与量の分割という別の問いから読む。Pasritamigだけを半量・半間隔へ変えた仮想比較を置き、何を揃えれば同じ曝露と言えるのかを計算した。結果は、定常状態の平均濃度は等しくても、最初の8週間の平均濃度は等しくならない、というものだった。しかも、こちらの初期曝露が公開された曝露反応解析の評価対象になっている。

## 対象と確認範囲

併用試験NCT06095089の臨床結果はスポンサー発表で確認した。SITC 2026の全スライドは確認できていない。以下の薬物動態（pharmacokinetics：PK）計算は、併用患者のデータを解析した結果ではない。

Pasritamig単剤の第I相論文では、3.5 mgをDay 1、18 mgをDay 8、300 mgをDay 15に投与し、その後6週ごととする用法が選択された。静脈内投与後の平均終末半減期は約15.2日と報告されている [(3)](#ref-3)。

さらに、PAGE 2026では、2コンパートメントと線形・非線形消失を含む母集団PKモデル、治療開始後8週間の平均曝露と確認済みPSA反応を結ぶ解析が発表されている。著者らは300 mgの6週投与を支持すると結論した [(4)](#ref-4)。ただし、[公開ポスターのFigure 1とFigure 3](https://www.page-meeting.org/wp-content/uploads/pdf_abstracts/2026/8ad6b057fde94ae2a2fa7c37f3925aac.pdf#page=1)には、実薬の濃度推移を再現するためのPK数値パラメータ一式は示されていない。

本記事では、未知の数値を補ってそのモデルを再現する方法は採らない。線形の比較モデルを明示的に置き、投与履歴と評価時間窓によって比較の意味がどう変わるかを調べる。3週ごと150 mgの効果や安全性が臨床的に確認されたという主張ではない。

## 方法

### 維持投与の速度と濃度の形を分ける

基準を300 mg・42日間隔、分割を150 mg・21日間隔とする。どちらも維持投与の速度は \(300/42=150/21=7.14\) mg/日である。PKは線形で時間によって変わらず、静脈内投与を瞬時入力と近似する。

単一指数モデルの速度定数を \(k=\ln 2/t_{1/2}\) 日\(^{-1}\)、投与間隔を \(\tau\) 日とする。定常状態の共通平均濃度 \(\bar C_{\mathrm{ss}}\) で濃度を割ると、各投与直後を \(t=0\) として、

\[
\frac{C_{\mathrm{ss}}(t)}{\bar C_{\mathrm{ss}}}
=\frac{k\tau e^{-kt}}{1-e^{-k\tau}},\qquad 0\leq t<\tau
\]

となる。絶対濃度を決めるクリアランスや分布容積は使わない。両条件で同じものとして比を取るためである。したがって、図の濃度はµg/mLではなく無次元量である。

半減期15.2日を中心例にした。感度分析には、ASCO GU 2026の[Table 2](https://www.jnjmedicalconnect.com/media/attestation/congresses/oncology/2026/asco-gu/phase-1-safety-efficacy-pharmacokinetics-pk-and-pharmacodynamics-pd-of-pas.pdf#page=1)の13.8日と16.5日 [(5)](#ref-5)、PAGEの18.3日も用いた [(4)](#ref-4)。異なる資料・解析で得られた代表値であり、この範囲を患者間変動の分布や信頼区間とは扱わない。

### 分布相を加えて結論の依存性を調べる

単一指数だけに依存しないよう、単位投与量当たりの応答を非負の指数成分の和へ広げる。

\[
h(t)=\sum_j w_j\lambda_j e^{-\lambda_j t},
\qquad w_j\geq0,\quad \sum_jw_j=1.
\]

ここでは全時間AUCを1へ正規化したため、\(w_j\) は各成分のAUCへの寄与割合である。濃度の振幅の割合とは異なる。遅い成分の半減期を上記の値とし、仮想的な速い成分の半減期を1日または3日、AUC割合を0、25%、50%とした。組合せは24通りになる。速い成分の値は実測推定ではなく、構造への依存を調べる条件である。

### 治療開始後56日を別に計算する

Day 1を \(t=0\)、Day 8を7日、Day 15を14日とする。両条件のステップアップ量3.5 mg・18 mgは共通にし、最初の本投与以降を変える。基準では14日に300 mg、分割では14日と35日に150 mgずつ投与する。次の投与は両方とも56日、すなわちDay 57である。

評価窓は \(0\leq t<56\) 日とした。これはDay 1から56日間という連続時間の定義で、56日の投与はこの窓のAUCへ寄与しない。公表モデルの個別患者データ処理まで再現したわけではない。

単位投与後 \(s\) 日までの正規化AUCを \(F(s)=\int_0^s h(u)\,du\) とすると、共通ステップアップの寄与は \(S=3.5F(56)+18F(49)\) であり、

\[
A_{\mathrm{ref}}=S+300F(42),\qquad
A_{\mathrm{split}}=S+150F(42)+150F(21)
\]

となる。\(A\) は共通の濃度換算係数を省いた正規化曝露であり、患者のh·µg/mLの値ではない。両方を同じ56日で割るので、このAUC比は平均濃度比でもある。維持投与速度が同じでも、投与を後ろへ分けた分だけ評価窓内で濃度に寄与する時間は短くなる。

## 結果

### 定常平均は同じでも閾値以上の時間は逆転する

単一指数の場合、\(a=e^{-21k}\) とおけば、分割後のピーク濃度比は \((1+a)/2\)、トラフ濃度比は \((1+1/a)/2\) となる。半減期15.2日の中心例では、ピークは0.692倍、トラフは1.803倍だった。これらは定常状態の比であり、初回投与後の値ではない。

しかし、トラフが上がることをそのまま薬効の改善とは読めない。未知の作用閾値を、共通の定常平均濃度で割った比として置き、閾値以上にある時間を計算すると表1になる。

**表1．仮想的な閾値を超える時間の割合。半減期15.2日の単一指数モデル。**

| Threshold / common steady mean | 300 mg every 6 weeks | 150 mg every 3 weeks |
| --- | ---: | ---: |
| 0.5 | 78.4% | 100.0% |
| 1.5 | 21.1% | 3.7% |

閾値は薬効の実測値ではない。必要な濃度が低ければ分割に有利な形になるが、高いピークが必要な条件では、閾値を超える時間がかえって短くなる。どちらの時間割合も、患者の反応率ではない。

![Normalized steady concentrations and threshold-dependent coverage](shared/pasritamig-dose-fractionation/regimen-steady.png)

**図1．同じ維持投与速度で濃度を平滑化した場合。** 自作の条件付き計算。左は共通の定常平均濃度で正規化した濃度、右は仮想閾値以上の時間割合である。絶対的な有効濃度は推定していない。

この平滑化自体は、単一指数に特有の現象ではない。線形・時不変なら、21日間隔の濃度は、42日間隔の濃度とそれを21日ずらした濃度との平均になる。

\[
C_{21}(t)=\frac{C_{42}(t)+C_{42}((t+21)\bmod42)}{2}.
\]

したがって、定常平均を維持しながら濃度の最大値を下げ、最小値を上げる。ただし、この関係だけでどの濃度指標が薬効を支配するかは決まらない。

### 初期8週間の曝露は一致しない

表2に、単一指数の各半減期で得られた比を示す。初回の本投与から150 mgにする分割では、初期AUCは基準の85.6–88.0%になった。維持投与の速度が同じという説明だけでは、この12.0–14.4%の差を落としてしまう。

**表2．分割投与の条件付き計算。比の分母は300 mg・6週投与。初期AUCはステップアップを含む0–56日。**

| Half-life, days | Steady peak ratio | Steady trough ratio | First-56-day AUC ratio | Exposure-matching first target dose, mg |
| --- | ---: | ---: | ---: | ---: |
| 13.8 | 0.674 | 1.936 | 0.880 | 188.7 |
| 15.2 | 0.692 | 1.803 | 0.871 | 191.6 |
| 16.5 | 0.707 | 1.708 | 0.864 | 193.9 |
| 18.3 | 0.726 | 1.608 | 0.856 | 196.7 |

曝露を揃えるために初回だけ300 mgを維持し、35日から150 mgに変えるとどうなるか。この場合の初期AUC比は1.320–1.345で、逆に基準を上回った。評価窓内に投与される本投与量が300 mgから450 mgへ増えるため、初期の総投与量まで等しい比較ではない。

そこで、初回本投与を \(L\) mg、その21日後を150 mgとして初期AUCを一致させる逆問題を解いた。

\[
S+LF(42)+150F(21)=S+300F(42),
\qquad
L=300-150\frac{F(21)}{F(42)}.
\]

解は表2の188.7–196.7 mgだった。これは仮定モデル内の曝露一致解であり、安全な初回量や推奨量の算出ではない。約190 mgを臨床で採用すべきだという意味もない。初回量をどう定めるかによって、投与頻度の比較に別の初期曝露差が加わることを示している。

![Early exposure and structural sensitivity to a hypothetical fast component](shared/pasritamig-dose-fractionation/regimen-early.png)

**図2．初期曝露を揃える比較と構造感度。** 自作の条件付き計算。左は半減期15.2日で、基準、最初から半量にした分割、初期AUCを一致させる初回量を使った分割を比較した。Day 57の投与による点での上昇は0–56日AUCに寄与しない。右は速い成分の半減期を1日、遅い成分の半減期を12–22日の連続した仮想範囲とした感度分析であり、線の間隔は信頼区間ではない。

24通りの構造感度分析でも、最初から半量にした分割の初期AUCは基準を下回った。実は、この向きは数値の選び方より強い条件で決まる。非負の応答なら \(F(42)\geq F(21)\) なので、

\[
A_{\mathrm{ref}}-A_{\mathrm{split}}
=150\{F(42)-F(21)\}\geq0.
\]

線形モデルの範囲では、単位投与後21日から42日の間にも曝露があれば差は正になる。速い分布相の寄与を増やすと差は小さくなるが、平均曝露が同じ定常状態と、まだ立ち上がっている初期期間を区別する必要は変わらない。

## 考察

### 比較する曝露の時間窓が結論を変える

PAGEの曝露反応解析は、治療開始後8週間の個別平均曝露を用いている [(4)](#ref-4)。それを読むときに「半量・半間隔ならAUCは同じ」とだけ説明すると、定常状態の平均と初期平均を取り違える。投与頻度の影響を調べる比較に、初回本投与量の違いによる曝露差が混ざるからだ。

この計算が示すのは、頻度を比べる前に揃えるべき曝露指標が複数あるという点である。維持投与速度、定常平均濃度、初期8週間の平均濃度は、同じ条件ではない。初期平均を一致させる解を持っていても、ピーク、トラフ、作用の休止期間まで一致するわけではない。

また、公開された曝露反応関係を、この仮想分割の反応率へ変換することもしない。PAGE抄録の平均曝露は遊離薬物として記載され、実際の母集団モデルには標的を介する非線形な消失が含まれる [(4)](#ref-4)。本記事の正規化した線形濃度とは同一ではない。公開資料の結論である「300 mg付近で増量の利得が小さい」という評価も、半量分割が同じ結果を出すことの検証にはならない。

### 併用の価値を一剤のトラフで説明しない

PasritamigはKLK2×CD3、JNJ-9401はPSMA×CD28を標的にする。KLK2はkallikrein-related peptidase 2、PSMAはprostate-specific membrane antigenである [(2)](#ref-2)。Pasritamigの濃度を平滑化しても、JNJ-9401の作用との時間的な重なりが保たれるかは、このモデルでは分からない。

PAGEの著者らは、6週投与の評価にT細胞の疲弊や活性化誘導性細胞死を減らす考え方も挙げている [(4)](#ref-4)。それは、一定濃度以上に長く保つほど有利という単純な仮説とは違う。今回の閾値解析は免疫細胞の回復をモデル化しておらず、低い閾値での被覆時間の増加を、そのまま臨床的な利得にはできない。

併用の15人におけるPSA低下も、JNJ-9401を加えた因果効果や生存利益そのものではない [(2)](#ref-2)。本記事には、個別患者のPK、曝露と反応の共変量、JNJ-9401の吸収・消失パラメータがない。免疫応答を含む実薬モデルの代わりに、仮想比較の一方を臨床的な勝者にすることはできない。

同量分割で同じになるのは、この線形モデルでは維持期の平均曝露である。濃度の形、閾値以上の時間、開始後8週間の曝露は同じにならなかった。したがって、6週投与を評価する問いは「半減期に比べて長すぎないか」から、「どの曝露とどの時間経過を揃えて比較しているか」へ移る。この区別を外すと、PK計算が正しくても、投与頻度について別の問いへ答えてしまう。

## データとコードの公開状況

[計算コード](shared/pasritamig-dose-fractionation/regimen_model.py)、未丸めの[計算結果](shared/pasritamig-dose-fractionation/regimen-results.json)、導出と再実行方法を記した[解析資料](shared/pasritamig-dose-fractionation/regimen-readme.md)を添付した。仮定した条件はコードと結果に含めた。個別患者データや原資料の図は再配布していない。

[計算コード・結果・図のZIP](shared/pasritamig-dose-fractionation/pasritamig-dose-fractionation.zip)

## 参照

<a id="ref-1"></a>
1. Wildgust M [@MAWildgust]. [Post describing pasritamig plus JNJ-9401 at SITC 2026; editorial description] [X post]. 2026 Nov 8 [cited 2026 Nov 9]. Available from: [original post](https://x.com/MAWildgust/status/2119408231529275687).

<a id="ref-2"></a>
2. Johnson & Johnson. Johnson & Johnson reports 73% PSA response rate with investigational pasritamig-based immunotherapy combination in advanced prostate cancer [press release]. PR Newswire. 2026 Nov 8 [cited 2026 Nov 9]. Available from: [sponsor release](https://www.prnewswire.com/news-releases/johnson--johnson-reports-73-psa-response-rate-with-investigational-pasritamig-based-immunotherapy-combination-in-advanced-prostate-cancer-302932750.html). Reporting SITC 2026 abstract 1175.

<a id="ref-3"></a>
3. Stein MN, Vinceneux A, Robbrecht D, Doger B, Autio KA, Schweizer MT, et al. Pasritamig, a first-in-class, bispecific T-cell engager targeting human kallikrein 2, in metastatic castration-resistant prostate cancer: a phase I study. J Clin Oncol. 2025;43(22):2515–2526. doi: [10.1200/JCO-25-00678](https://doi.org/10.1200/JCO-25-00678). [Open-access full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12288886/).

<a id="ref-4"></a>
4. T’jollyn H, Valenzuela B, Woot de Trixhe X, Jaiprasart P, Villalobos V, Wang SC, et al. Model-informed drug development to support dose selection of pasritamig, a KLK2×CD3 bispecific antibody, in metastatic castration-resistant prostate cancer [conference abstract and poster]. PAGE 34; 2026. Abstract 12211, poster III-036. Available from: [official abstract](https://www.page-meeting.org/Abstracts/model-informed-drug-development-to-support-dose-selection-of-pasritamig-a-klk2xcd3-bispecific-antibody-in-metastatic-castration-resistant-prostate-cancer/) and [poster PDF](https://www.page-meeting.org/wp-content/uploads/pdf_abstracts/2026/8ad6b057fde94ae2a2fa7c37f3925aac.pdf).

<a id="ref-5"></a>
5. Dai J, Liu N, Li Y, Yu Z, Zhang S, Kawahara T, et al. Phase 1 safety, efficacy, pharmacokinetics (PK) and pharmacodynamics (PD) of pasritamig in Asian population with metastatic castration-resistant prostate cancer (mCRPC) [conference poster]. ASCO Genitourinary Cancers Symposium; 2026 Feb 26–28; San Francisco, CA. Poster 172. Available from: [public poster](https://www.jnjmedicalconnect.com/media/attestation/congresses/oncology/2026/asco-gu/phase-1-safety-efficacy-pharmacokinetics-pk-and-pharmacodynamics-pd-of-pas.pdf). Table 2.
