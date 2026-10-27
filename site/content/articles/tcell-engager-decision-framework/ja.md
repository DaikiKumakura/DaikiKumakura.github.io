## 要旨 {#article-abstract}

薬剤固有のデータが揃う前にも公開臨床薬理情報から投与法の問いを検討できるが、根拠の限界は明示する必要がある。タルラタマブの基準共変量における2コンパートメントモデルを再構築し、公表された個体間変動を5,000人の仮想被験者へ伝播させ、公表ORR・DCRのEmaxパラメータを用いた。重複患者を含む3つのCRS集計期間について、9つの一般化Bayesモデル・感度条件を検討した。14のstep-up投与法と定常状態の維持投与も比較した。これとは別の仮想モデルでは、無次元の薬剤成立条件、測定の近似的な意思決定価値、PK・サイトカインの採血設計を計算した。初期平均曝露は添付文書の要約値に近かったが、定常トラフは十分に一致しなかった。曝露履歴モデルと投与回カテゴリーのモデルはいずれも3つのCRS集計を説明し、サンプリング診断が良好でも履歴時間尺度は事前分布に依存した。同じ用量強度は平均曝露を保ったがピークとトラフを変えた。仮想シナリオでpriming測定には価値があったものの、その順位は効用と測定の仮定に依存した。局所情報量の計算では初期採血だけによるCLの同定は弱かった。公開根拠から測定要件へつなぐ再実行可能な解析であり、臨床の最適投与法を特定したものではない。個人別臨床データは使わず、CRS外挿と仮想測定の順位は検証済み臨床予測ではない。

## 背景と目的 {#article-introduction}

投与法には有効性に必要な曝露、急性の免疫刺激、時間を通じた薬理作用の維持という異なる問題がある。小さい初回量は急性刺激を減らしうる一方、十分なpriming応答を生じない可能性もある。維持期の投与間隔を延ばすと、平均曝露を保っても濃度の波形は変わる。

先のPK解析ではこれらを分けて検討した ([1](#ref-1))。今回は、曝露履歴と追加測定の意思決定価値へ解析を広げた。この拡張には仮定を加えている。疎な公開データの情報量を増やして見せるためではなく、どの仮定が判断を動かすかを調べるためである。

![公開根拠から測定要件への解析の流れ](shared/tcell-engager-decision-framework/figures/01-workflow.png)

**図1　解析の流れ。** 臨床モデルの再構築と仮想的な意思決定シナリオは別の根拠として扱う。臨床データに当てはめた事後分布が、そのまま新規薬剤へ移せるわけではない。

### 問いと利用範囲 {#question-and-use}

解析の問い（question of interest、QoI）は、T-cell engagerの投与法比較のどの部分が公開根拠に支持され、どの部分が曝露履歴とprimingの仮定に依存し、どの測定がその仮定を検討できるか、である。

利用範囲（context of use、CoU）は公開データの再構築、方法論上のシナリオ比較、測定要件の整理とする。患者の用量、初回ヒト投与量、臨床のstep-up・維持投与法は選ばない。後述の仮想スコアは、臨床成功確率やサイトカイン放出症候群（CRS）の発症確率ではない。

有効性・安全性・忍容性を併せて考える点は、FDA Project OptimusとOncology Dosing Tool Kitの方針に対応する ([2](#ref-2), [3](#ref-3))。FDAが2026年6月に最終ガイダンスを発行したICH M15も、モデルの利用目的と根拠を定める文脈になる ([4](#ref-4))。これらが本シミュレーションを承認・推奨するわけではない。

## 方法と結果 {#article-methods-results}

### 根拠と再構築と仮定 {#evidence-and-assumptions}

表1に資料の用途を示す。表中の名称は配布資料との対応のため英語で示す。PKは薬物動態、PDは薬力学、PopPKは母集団薬物動態、IIVは個体間変動、ORRは奏効率、DCRは病勢制御率、ROは受容体占有率を指す。

**表1　出典の用途と限界**

| 根拠 | 用途 | 限界 |
| --- | --- | --- |
| FDA tarlatamab review, [Tables 66–67](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2024/761344Orig1s000MultidisciplineR.pdf) ([5](#ref-5)) | PK構造と個体間変動 | 基準パラメータでは試験の共変量分布を再現できない |
| Tarlatamab PopPK ([6](#ref-6)) and label [Table 17](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=1e7b6163-5d83-42ea-82c9-cf7620cdc782) ([7](#ref-7)) | モデルの位置付けと曝露の照合 | 比較値はモデル由来の平均であり生の観測値ではない |
| Formal tarlatamab E–R, [Supplementary Table S1](https://doi.org/10.1158/1078-0432.30618111) ([8](#ref-8)) | ORR/DCRのEmax | 患者単位の投与記録と転帰は得られない |
| DeLLphi-301 AE-management [Figure 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC11775405/) ([9](#ref-9)) | 全Grade CRSの54/133、39/133、10/133 | 患者が重複し期間は7、7、14日 |
| Epcoritamab RTTE analysis ([10](#ref-10)) | 構造の比較 | Grade ≥2 CRS、CD20疾患、皮下投与。数値は移植しない |
| Teclistamab modeling ([11](#ref-11)) | 薬理的な曝露の余裕の例 | 薬剤・評価項目・奏効例集団が異なる |
| Mosunetuzumab step-up analysis ([12](#ref-12)) | 薬剤固有のPK/RO/CRS連結の例 | 抗CD20競合と曝露指標を相互に置き換えられない |

個人別の臨床データは使っていない。公表された人数を観測値、出典のパラメータ推定値を公表モデル由来、本記事の計算を再構築、未検証投与法と仮想薬剤を探索的と区別する。図1は公開情報の再構築と仮想シナリオを区別している。元の文献確認日は2026年10月3日である。公開資料は確認用に保存したが、ダウンロード資料には含めず、出典URLを記載した。

### 基準共変量の2コンパートメントPopPK {#reference-pk}

量はmg、容積はL、時間は日とする。

\[
\dot A_c=R_{in}-(CL+Q)A_c/V_c+QA_p/V_p,\qquad
\dot A_p=QA_c/V_c-QA_p/V_p,\qquad C=A_c/V_c.
\]

点滴時間は1時間である。FDA資料の値はCL=0.649 L/day、Vc=3.44 L、Vp=5.06 L、Q=1.11 L/dayである ([5](#ref-5))。基準は73 kg、White、結合性抗薬物抗体（ADA）陰性とする。CLとVcは対数正規分布に従い、ηの標準偏差は0.437と0.387、相関は0.535とした。これらは**標準偏差と相関**であり、変動係数として再変換する値ではない。潜在曝露に残差誤差は加えていない。

点滴の解析解を、行列指数、AUCの数値積分、反復投与時の蓄積と照合した。基準の終末相半減期は約11.2日である。5,000人全員の共変量は基準値に保ち、投与法間で同じ被験者を使った。2コンパートメントの**構造**の再現であり、試験全体の共変量分布や実際の投与履歴の再現ではない。

![公表平均曝露と基準共変量集団での再構築値](shared/tcell-engager-decision-framework/figures/02-pk-validation.png)

**図2　公表値と再構築値。** 単位はng/mL。1と10は最初の1 mgと最初の10 mgの区間、SSは10 mg・2週ごと投与の定常状態を指す。公表平均と仮想平均は異なる集団に由来し、公表点要約に区間を付与していない。

**表2　公表曝露と再構築曝露**

| Period | Metric | Published mean | Virtual mean | Difference |
| --- | --- | ---: | ---: | ---: |
| First 1 mg | Cavg | 106 | 106.2 | +0.2% |
| First 1 mg | Cmax | 314 | 308.1 | −1.9% |
| First 1 mg | Ctrough | 49 | 51.6 | +5.4% |
| First 10 mg | Cavg | 1,100 | 1,103.4 | +0.3% |
| First 10 mg | Cmax | 3,190 | 3,132.8 | −1.8% |
| First 10 mg | Ctrough | 517 | 550.0 | +6.4% |
| Steady Q2W | Cavg | 1,040 | 1,211.7 | +16.5% |
| Steady Q2W | Cmax | 3,640 | 3,742.4 | +2.8% |
| Steady Q2W | Ctrough | 472 | 662.5 | +40.4% |

図2と表2に示した定常トラフの不一致があるため、添付文書の集団曝露を完全に再現したとは扱えない。η=0でも対応する差は約+16%あり、IIVを加えると平均は変わる。典型値と集団平均を一致させる比較では、この違いを隠してしまう。モデル内の相対比較は計算できるが、この照合だけから絶対的な閾値の主張はできない。

出典は体重、ADA、人種の影響を報告している ([5](#ref-5), [6](#ref-6))。別の共変量範囲の計算では、公表された比例係数を使い、体重の線形形式と指数形式の両方を検討した。正確な体重関数を独立に確認できていないためである。これらは仮定と表示し、完全な共変量モデルの再現とは呼ばない。

### 公表された有効性の曝露反応モデル {#efficacy-model}

公表モデルは次式である。

\[
p(E)=E_{max}E/(EC_{50}+E),\qquad E=C_{avg,\mathrm{first\ cycle}}.
\]

[原著Supplementary Table S1](https://doi.org/10.1158/1078-0432.30618111)は、ORRのEmax=0.339、EC50=57.4 ng/mL（95% CI 22.5–146）、DCRのEmax=0.650、EC50=49.4 ng/mL（20.9–117）と報告する ([8](#ref-8))。再構築した有効性の計算はこの正式な推定値を用いた。

![公表ORR・DCR曲線と再構築した曝露位置](shared/tcell-engager-decision-framework/figures/03-efficacy.png)

**図3　公表Emaxモデル。** 縦線は共通の1 mg→目標量→目標量の投与法から再構築した第1サイクルCavg中央値で、観測集団の曝露中央値ではない。曲線は点推定であり予測帯ではない。

図3の3/10/100 mgの再構築中央値でORRは28.2/31.7/33.7%、原著の報告は26.2/31.4/33.6%だった。DCRは55.3/61.4/64.6%、原著は52.0/60.8/64.5%だった ([8](#ref-8))。共通投与法と基準共変量集団では、元の統合された実投与記録を再構築できない。再現したのは**関数**であり、すべての集団予測の厳密な一致は主張しない。

E90=9×EC50はモデル最大値の90%を意味し、奏効率90%ではない。この第1サイクル平均曝露の関係も、そのプラトーも、維持トラフの閾値にはならない。新しい投与法へ移した応答モデルは探索計算であり、有効性の同等性を実証しない。全投与法についてEC50区間端点を一つずつ変えた感度結果を`results/efficacy-sensitivity.csv`に含めたが、Emax・EC50の同時事後分布は伝播していない。

### CRS集計が示すモデル上の問題 {#crs-summaries}

全Gradeの観測割合は、D1–7、D8–14、D15–28で40.6%、29.3%、7.5%だった ([9](#ref-9))。基準モデルのピークは対応する投与回で増加する。

![曝露ピークと観測CRS割合を分けた表示](shared/tcell-engager-decision-framework/figures/04-crs-evidence.png)

**図4　曝露とCRSの集計。** 左は仮想ピーク中央値（µg/mL）、右は観測された期間別割合である。患者単位で対応した曝露・イベントの組ではない。最後の期間は最初の2期間の2倍の長さである。

図4の順序を、共通の単調増加の曝露項だけを持つモデルでは、その仮定のもとで説明できない。制約しない曝露モデルなら負の傾きを学習しうる。しかし、いずれも生物学的適応を証明しない。予防処置、病勢変化、選択、時点、反復イベントも説明候補に残る。投与回カテゴリー項も記述的な解になる。

Epcoritamabの600人に対する反復イベント時間（RTTE）解析は、刺激と抑制の成分、予防処置、CAR-T歴の影響を用いた ([10](#ref-10))。曝露履歴を考える構造上の根拠にはなるが、そのGrade ≥2のハザードパラメータを全Gradeのタルラタマブ確率モデルへ入れられない。数値的なepcoritamab事前分布は借用していない。

### 一般化Bayesの曝露履歴モデル {#history-model}

正規化ピークを (x_{ik}=C_{max,ik}/(1,mu g/mL)) として、次式を置く。

\[
H_{ik}=\sum_{m<k}\frac{x_{im}}{r+x_{im}}
\exp\{-\ln(2)(t_k-t_m)/T_H\},
\qquad p_{ik}=\operatorname{logit}^{-1}(\alpha+\beta\log x_{ik}-\gamma H_{ik}).
\]

固定した基準共変量256人の積分標本でpを平均する。Hは現象論的な曝露履歴の状態であり、確立された免疫寛容ではない。その効果は、測定されていない期間差を吸収しうる。

**表3　履歴モデルの基準事前分布**

| Parameter | Baseline prior | Interpretation |
| --- | --- | --- |
| α | Normal(logit(0.4), 1.5²) | 探索的な基準対数オッズ |
| log β | Normal(log(0.43), 0.7²) | 正の急性傾きを仮定。外部推定値ではない |
| log γ | Normal(log(2), 0.7²) | 仮定した抑制強度 |
| log TH | Normal(log(20), 0.8²) | 仮定した履歴時間尺度（日） |
| log r | Normal(log(0.1), 1.5²) | 仮定した無次元飽和尺度 |

同じ患者が複数期間に含まれるため、3つの二項尤度の積から結合尤度は復元できない。代わりに、探索的な**べき複合尤度**を使った。

\[
q(\theta\mid y)\propto p(\theta)
\left\{\prod_{k=1}^3\mathrm{Binomial}(y_k;133,\bar p_k(\theta))\right\}^{w},\quad w=0.5.
\]

感度解析はw=0.25と1で行った。重みを下げても未知の依存は解決せず、仮定した情報量への感度を調べるに留まる。得られる区間は一般化事後区間であり、校正された患者リスクの信頼区間ではない。

正の傾きの曝露単独モデル、傾きを制約しない曝露単独モデル、投与回カテゴリー、連続履歴モデル、広い事前分布、速い・遅い履歴条件を当てはめた。各条件でNUTSの4チェーン、調整1,500回、保存1,200回/チェーンを使った。9条件すべてで最大R-hatは1.008未満、最小bulk ESSは816超、発散はゼロだった。この診断はサンプリングの評価であり、モデルの同定可能性の証明ではない。

### 当てはまりと同定可能性 {#fit-and-identification}

![期間別CRSの適合と事前分布に依存する履歴時間尺度](shared/tcell-engager-decision-framework/figures/05-crs-posterior.png)

**図5　CRSの適合と履歴時間尺度。** 左は各期間の一般化事後中央値と90%区間、十字は観測割合である。右は異なる事前分布での履歴時間尺度の区間。周辺確率の当てはめであり、結合した縦断データの検証や標本外評価ではない。

**表4　観測割合とモデルの適合値**

| Window | Observed | Positive exposure-only | Category | History |
| --- | ---: | ---: | ---: | ---: |
| D1–7 | 40.6% | 22.8% | 38.8% | 39.9% |
| D8–14 | 29.3% | 27.2% | 29.3% | 28.5% |
| D15–28 | 7.5% | 27.5% | 8.2% | 8.4% |

図5・表4は期間別の適合を示し、図6は履歴時間尺度の事前依存とチェーンを示す。周辺の再生成人数チェックを`results/crs-ppc.csv`に保存した。各期間は適合確率を条件としてシミュレーションし、期間間の未知の結合依存を復元していない。カテゴリーと履歴の両モデルで集計を説明でき、履歴モデルを唯一の機序として選べない。基準履歴モデルの中央値（90%区間）はβ=0.334（0.121–0.751）、γ=2.38（1.42–4.42）、TH=24.1日（8.3–81.0）、r=0.088（0.0087–0.549）だった。

事前分布の中心を5日と60日にすると、TH区間は約4.7–29.1日と17.6–231.5日へ動く。3つの集計への妥当な当てはまりから、20日の適応定数が確立されたとは言えない。

![履歴時間尺度の事前分布・一般化事後分布・4チェーンのトレース](shared/tcell-engager-decision-framework/figures/11-prior-trace.png)

**図6　事前・事後分布とチェーン診断。** トレースが収束しても広い区間と事前分布への依存が残る。結果はチェーン順のNPZと診断表に保存した。

### Step-upシナリオと不確実性 {#step-up-scenarios}

7日間隔の14通りの導入投与を比べた。最初の10 mgの目標量投与から7日後に10 mgを追加し、その後は14日ごとにする。1→10はD1/D8/D15、直接10 mgはD1/D8/D22となる。定めた反実仮想の投与配置であり、承認された直接投与法ではない。第1サイクルは全比較で0–28日とした。

**表5　Step-up条件の抜粋**

| Prefix | Target day | Transferred DCR median | Maximum marginal CRS median |
| --- | ---: | ---: | ---: |
| Direct 10 | 0 | 62.3% | 59.0% |
| 0.1→10 | 7 | 61.2% | 46.8% |
| 0.5→10 | 7 | 61.3% | 38.2% |
| 1→10 | 7 | 61.4% | 40.7% |
| 3→10 | 7 | 61.7% | 49.5% |
| 0.3→1→10 | 14 | 60.6% | 31.7% |
| 0.3→1→3→10 | 21 | 58.2% | 31.5% |

CRS集計は400の事後標本と250人の仮想被験者を組み合わせ、感度比較は200標本と100人を使った。各投与回の周辺確率区間、曝露分布、感度結果は結果表に含めた。最大周辺確率は**投与法全体で一度でもCRSが起こる確率ではない**。イベント依存が不明なため後者は計算できない。拡張モデルは1つの観測期間を1つのピークへ対応させ、イベント時間ハザードは推定していない。投与回の出力も共通追跡長でのリスクではなく、7日・14日の観測期間差は集計から補正できない。

![Step-up配置間の探索的な交換関係](shared/tcell-engager-decision-framework/figures/06-step-up.png)

**図7　Step-up比較。** 点は中央値、色は目標量の日、サイズは段階数である。読みやすさのためラベルは一部に限定し、14条件と区間はCSVに記載した。軸は移植したモデル出力で、臨床的に検証した転帰ではない。Pareto解析はDCR、最大周辺CRS、目標量の日、投与回数を含むが、非劣解であることは臨床推奨を意味しない。

図7は投与法間の探索的な交換関係を示す。直接10 mgの感度計算では、基準条件で約59.6%（47.1–80.7%）だった。この区間は事前分布、尤度の扱い、積分集団、投与配置を条件としたもので、外部検証されたリスク推定ではない。

このモデルでは0.1 mgの導入量は目標量までの履歴抑制が小さく、極小のpriming用量が予測CRSを最小にするとは限らない。一方、どれだけのprimingが十分かも確立できない。仮定による絶対CRS値や順位の変化は、最適化の証拠ではなく結論の不安定さとして読む必要がある。

### Priming応答の測定上の不足 {#priming-measurement}

有界なpriming応答の候補を次式とした。

\[
P(E)=E^{h_p}/(P_{50}^{h_p}+E^{h_p}).
\]

確率的な評価項目と観測モデルを定義しない限り、この表記は応答指標である。初回刺激、washout、再刺激を一定の標的細胞・T細胞条件で測定すれば、2回目のサイトカイン応答低下と細胞傷害機能の維持を併せて検討できる。細胞喪失や殺傷機能低下によってサイトカインが減っただけでは、十分なprimingと扱えない。

必要な測定には用量・濃度、曝露時間、刺激間隔、生存率、CD69/CD25、サイトカイン、T細胞依存性細胞傷害（TDCC）がある。ドナーと標的密度の違いは条件間で対応付ける必要がある。安全性だけの最適化では不十分だが、任意のpriming閾値を加えても臨床的な十分性は得られない。

### 維持曝露と薬剤固有の余裕 {#maintenance-exposure}

図8では6条件の定常状態をシミュレーションし、各被験者の指標を本人の10 mg・2週ごとの値で割った。

![同じ仮想被験者内での維持曝露比](shared/tcell-engager-decision-framework/figures/07-maintenance.png)

**図8　維持曝露の比。** 中央値とIIVの5–95%範囲。用量強度を等しくするとCavgは保たれるが、15 mg・3週ごとではピークが約38%増え、トラフが約22%減る。20 mg・4週ごとでは約78%増、約40%減となる。PK比較であり有効性同等の主張ではない。

別の根拠連鎖の例として、teclistamabでは推定トラフ中央値20.4、14.4、11.7 µg/mLをex-vivo細胞傷害EC90,maxの6.039 µg/mLと比べた ([11](#ref-11))。算術的な余裕は3.38、2.38、1.94となる。閾値の出典は患者5人の骨髄検体で、切替解析も奏効例を対象とする。普遍的なTCE閾値や全患者の十分条件ではない。タルラタマブに同様の検証済み維持曝露の余裕を導入したわけではない。

### 無次元の薬剤成立条件 {#molecule-feasibility}

別の仮想1コンパートメントbolusモデルを定義した。正規化TDCC E90を1、機能的治療域（TI）をサイトカインE50/TDCC E90とする。単位はタルラタマブのmgへ換算できず、臨床CRS尤度を当てはめたモデルでもない。

用量D、容積尺度V、間隔τ、消失k=ln2/半減期について次式を使う。

\[
C_{max,ss}=\frac{D/V}{1-e^{-k\tau}},\quad
C_{trough,ss}=C_{max,ss}e^{-k\tau},\quad C_{avg,ss}=\frac{D}{Vk\tau}.
\]

正規化用量1/2/4/8、間隔3/7/14/21/28日、priming割合0.03/0.1/0.3/0.5、7日間隔のprimingを1回または2回とする160の候補行動を使った。仮想免疫刺激はS(C)=C/(cytokine E50+C)、再刺激時はexp(−γH)で抑制するとした。P50=0.3、γ=2、履歴半減期10日は仮定である。残存薬物のピークと過去の各priming投与を含め、最悪の初期刺激スコアを保持した。

図9に示すTI=1–100、半減期1–21日の各条件で500人を用い、半減期のlog標準偏差0.35、容積0.30とした。90%以上がtrough/E90>1、80%以上が初期刺激限度未満、80%以上がpriming応答限度を満たす場合だけ成立とした。例示用の制約である。

![3つの制約条件での仮想薬剤の成立領域](shared/tcell-engager-decision-framework/figures/08-feasibility.png)

**図9　有限候補集合での成立条件。** 少なくとも1つ成立する候補があるかを二値で示す。青は臨床成功確率ではなく、白も候補集合外に成立する投与法がないとは示さない。この構造では広いTIと長い半減期が有利になりうるが、用量集合、変動、priming、閾値が境界を大きく変える。

### 3つの効用仮定における測定価値 {#measurement-value}

測定の目的は、定義した判断を変える、または安定させることである。そこで、パラメータ分散の減少を情報価値と呼ぶのではなく、期待効用を計算した。

正規化有効性E、刺激S、priming指標P、維持余裕M、priming回数N、間隔τを使う。

\[
U=E-w_S S-w_P\max(0.8-P,0)
-w_M\frac{\max(1-M,0)}{1+\max(1-M,0)}-0.02N-0.02(7/\tau).
\]

E=Cavg/(Cavg+E90/9)に仮定した標的密度の倍率を含めた。重みは無次元の選好であり健康効用ではない。(wS,wP,wM)=(1,1,0.3)、(2,1,0.3)、(1,2,0.6)の3条件を比べた。

半減期、TDCC E90、サイトカインE50、priming P50、履歴半減期、履歴強度、標的密度係数、容積尺度に、独立な対数正規の不確実性を置いた。中央値とlog標準偏差は`data/generic-assumptions.json`に記録した。学習用と評価用の独立な6,000標本により、同じ標本で条件付き判断を選び評価することを避けた。

完全情報の期待価値（EVPI）はE[maxa U(a,θ)]−E[U(a0,θ)]で推定する。部分情報では1パラメータまたは誤差を含む対数測定を12区間に分け、各学習区間で行動を選び、標本外で評価した。これは**区間化したEVPPI/EVSIの近似**であり、厳密な事後積分ではない。測定のlog誤差標準偏差0.15と0.40も仮定である。

![3つの効用条件での近似測定価値](shared/tcell-engager-decision-framework/figures/09-information-value.png)

**図10　測定価値の近似。** 固定した学習済み方策に対する評価標本の平均効用増分とMonte Carloの±1.96 SE。学習方策や構造の不確実性は含めない。測定費用を引いた投資順位でもない。

**表6　測定の近似情報価値**

| Measurement, log-error SD 0.15 | Utility scenario 1 | Scenario 2 | Scenario 3 |
| --- | ---: | ---: | ---: |
| Priming P50 | 0.0277 | 0.0138 | 0.0394 |
| Cytokine E50 | 0.0109 | 0.0091 | 0.0020 |
| PK half-life | 0.0058 | 0.0043 | 0.0118 |
| TDCC E90 | 0.0001 | 0.0005 | 0.0045 |

図10・表6の条件でpriming情報に価値があるのは、primingの不確実性と不足を明示的に罰しているためである。実験の普遍的な順位ではない。ゼロ付近やわずかに負の近似増分は有限標本・区間化誤差と不完全な判断規則を反映する。元の判断を保持できるなら、厳密な情報価値は負にならない。これを不確実性減少の割合や金銭的便益へ換算していない。

腫瘍増殖・殺傷の測定に数値の情報価値順位は付けなかった。この仮想効用には、推定した腫瘍増殖成分がないためである。ここで値を付ければ、実際には解析していない意思決定モデルを作ったことになる。

### PKとサイトカインの採血設計 {#sampling-design}

log(CL,Vc,Q,Vp)の局所Fisher情報量を、独立な対数濃度誤差標準偏差0.30を仮定して計算した。0/7/14日に1→10→10 mgを投与する濃度を使う。残差標準偏差は**設計用の仮定値**であり、FDAの報告残差ではない。情報量は1人あたりで、定量下限未満（BLQ）、ランダム効果、脱落、機会間変動を含まない。投与前のゼロ濃度は対数情報に寄与しない。

**表7　PK採血と局所情報量**

| Design | Postdose sampling times | Reference SE log(CL) |
| --- | --- | ---: |
| Sparse early | 1/6/24 h, day 7 | 85.16 |
| Intermediate early | 1/4/8/24/48 h, day 7 | 12.49 |
| Dense early | 1/2/4/8/24/48/72 h, day 7 | 5.39 |
| Sparse + late | Sparse plus days 14 and 28 | 0.324 |
| Dense + late | Dense plus days 14 and 28 | 0.278 |

図11・表7の7日と14日の採血はその日の点滴前である。初期設計の極端に大きい値は悪条件性を示し、その範囲では局所近似を利用可能な精度予測として扱えない。QとVpを固定すれば問題を人為的に易しくしてしまう。CL倍率0.5と3.33も検討したが、2コンパートメント系を通じて終末相半減期が変わるので、半減期そのものの倍率ではない。

![採血情報量と仮想サイトカインピークの捕捉](shared/tcell-engager-decision-framework/figures/10-sampling.png)

**図11　採血設計。** 左は3つのCL条件でのlog(CL)標準誤差で、初期採血を密にするだけでは不十分だった。右は仮想サイトカイン条件でのピーク捕捉であり、観測した臨床動態ではない。

サイトカインはピーク時刻を2–12時間の一様分布、応答をexp{−0.5[log(t/tpeak)/0.6]²}と仮定し、測定誤差は置かなかった。真のピークの80%以上を捉えたシミュレーションの割合は、0/6/24時間で49.2%、0/2/6/12/24時間で89.6%、0/2/4/6/12/24時間で100%だった。最後の100%は滑らかな仮定曲線と時刻範囲によるもので、臨床のピーク捕捉を保証しない。実際の採血推奨へ使う前には、動態と測定ノイズへの感度が必要である。

## 考察 {#article-discussion}

### 測定と判断の対応 {#measurement-and-decision}

**表8　測定が与える情報と判断の対応**

| 測定 | 得られる情報 | 検討できる判断 |
| --- | --- | --- |
| 多ドナーのTDCC濃度応答 | E50/E90とHill曲線形状 | 必要曝露の仮定 |
| 標的密度パネル | 力価変化とドナー変動 | 病態間での作用維持の頑健性 |
| TDCCと併せたサイトカイン応答 | 殺傷と刺激の分離 | 機能的TIの仮説 |
| Priming・washout・再刺激 | P50、殺傷の維持、履歴・時間依存 | 導入量の割合と間隔の仮説 |
| マウスPK・濃度・反復投与下の腫瘍体積 | PKと増殖・殺傷動態 | 曝露・有効性と維持投与の仮説 |
| 腫瘍免疫細胞の浸潤・活性化 | 組織PDと時間経過 | 機序の妥当性。単独の有効性閾値にはならない |
| 薬理的に関連するNHPの反復PK・サイトカイン | 種間の刺激と反復応答のパターン | 割引を要する橋渡しの仮定 |
| 対応したヒトの用量・PK・PD・CRS記録 | 薬剤固有の縦断モデル | 臨床投与法比較の更新 |

細胞実験で標的量の低・中・高、多ドナー、濃度応答、時間依存の殺傷とサイトカイン、制御した再刺激を組み合わせれば、仮定した応答を区別する情報になる。マウス実験は適切なヒト免疫・標的条件、vehicle対照、経時腫瘍体積、対応する曝露・PD測定時点を必要とし、総量、頻度、step-upの影響を区別する群構成が問題になる。マウスのサイトカイン測定だけではヒトCRSリスクを確立できない。

非ヒト霊長類（NHP）の情報も、標的とCD3への交差反応性と薬理学的関連性がある場合に限られる。反応しない種から関連する刺激の事前分布は得られない。反応する種でもヒトCRS予測を保証するわけではない。

### 新規薬剤への更新と借用の条件 {#updating-and-borrowing}

外部の構造知識、薬剤固有のin-vitro情報、関連する動物情報、ヒト縦断観測という順に根拠は変わる。数値の借用には評価項目と尺度の対応、交換可能性の論拠が必要である。頑健な事前分布や割り引いた事前分布は、矛盾する薬剤固有データが優位になる余地を持つ必要がある。

PKの置換だけでは不十分で、サイトカイン力価、標的密度、組織分布、priming、有効性の関係も変わりうる。タルラタマブの外部履歴モデルは探索的な参照であり、移植可能な臨床事前分布ではない。情報価値を資源配分へ使うには、仮想効用を候補薬剤の測定費用と結果の重大さへ置き換える必要もある。

### 検証された範囲と限界 {#validation-and-limits}

**表9　結論の根拠区分**

| 結論 | 分類 | 理由 |
| --- | --- | --- |
| 基準2コンパートメント実装は内部整合する | 数理上の頑健な確認 | 独立解法・積分・蓄積の照合 |
| 添付文書の集団曝露を完全に再現した | 支持されない | 定常トラフ平均は約40%高いままである |
| 正式Emax関数は曝露増加とともに飽和する | 出典モデルを条件とした再構築 | Parameters verified in [Supplementary Table S1](https://doi.org/10.1158/1078-0432.30618111) |
| 正の単調曝露項だけでCRSの順序を説明する | 検討した仮定では支持されない | カテゴリー・履歴項または負の傾きの方が適合する |
| 臨床的な生物学的適応が確立した | 支持されない | 疎で重複した集計と未測定の期間変化 |
| 同じ用量強度は平均を保つが波形を保たない | 線形PK構造内で頑健 | 解析的恒等式と対応したシミュレーション |
| 特定のstep-upが臨床的に優れる | 支持されない | 未検証の投与法と安全性・有効性の移植 |
| Priming測定は高い意思決定価値を持つ | 探索的 | 仮定した分布・効用・測定精度 |
| 初期採血だけで4つのPKパラメータをよく同定する | 検討設計では支持されない | Fisher情報量の悪条件性 |

限界は、個人別データとイベント時刻の欠如、期間間依存の不明、予防処置の差、標的・疾患・経路の違い、共変量再構築の不完全さ、事前分布に依存する履歴パラメータ、有限候補集合にある。3つの割合への一致は外部検証ではない。新規薬剤の検証、臨床推奨、因果機序、最適投与法の特定は行っていない。

## 結論 {#article-conclusion}

履歴時間尺度は事前分布に依存した。遅いPK採血は検討した局所近似の範囲でCL情報を改善したが、いずれも臨床の最適step-up・維持投与法を確立する結果ではない。

一般化CRSモデルは、集計記録から曝露履歴と他の期間効果を分離できない。採血計算にも仮定したモデルを超える測定誤差、BLQ、ランダム効果、脱落は含まれない。これらは報告結果の境界であり、後続試験の検証済みプロトコルではない。

## データとコードの公開状況 {#availability}

[コード・実行済みノートブック・入力表・事後標本・結果表のダウンロード](shared/tcell-engager-decision-framework/tcell-decision-analysis.zip)。図は本解析から作成し、論文の図を転載していない。

```bash
python -m pip install -r requirements.txt
python bayes.py
python design.py
python analysis.py
python scientific_checks.py
```

乱数seedは20261006に固定した。保存済み推定は再利用し、再推定する場合は対象の保存済み標本と診断ファイルを取り除く。ノートブックはPK、投与法・設計計算、検査を再実行し、保存されたNUTS診断・標本を表示する。9条件のNUTS推定全体は`bayes.py`で別に実行する。出典台帳、モデル仮定、実行環境の版、出力を含めた。

## 参照 {#article-references}

1. <span id="ref-1"></span>Kumakura D. Can matching average exposure alone set the tarlatamab dosing interval? [Internet; technical note]. 2026 Oct 5. [English article](https://daikikumakura.github.io/writing/tcell-engager-regimen-design-en.html).
2. <span id="ref-2"></span>US Food and Drug Administration. Project Optimus [Internet; cited 2026 Oct 28]. [Official resource](https://www.fda.gov/about-fda/oncology-center-excellence/project-optimus).
3. <span id="ref-3"></span>US Food and Drug Administration. Oncology Dosing Tool Kit [Internet; cited 2026 Oct 28]. [Official resource](https://www.fda.gov/about-fda/oncology-center-excellence/oncology-dosing-tool-kit).
4. <span id="ref-4"></span>US Food and Drug Administration. M15 General Principles for Model-Informed Drug Development [Internet; final guidance]. 2026 Jun [cited 2026 Oct 28]. [Guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m15-general-principles-model-informed-drug-development).
5. <span id="ref-5"></span>US Food and Drug Administration. Tarlatamab multidisciplinary review [Internet]. 2024. Tables 66–67, printed pp. 294–295; Table 71, pp. 310–311. [Review document](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2024/761344Orig1s000MultidisciplineR.pdf).
6. <span id="ref-6"></span>Kong S, Minocha M, Chen PW, Martinez P, Anderson ES, Parkes A, et al. Population pharmacokinetics of tarlatamab, a half-life extended DLL3-directed bispecific T-cell engager in patients with previously treated small cell lung cancer. Clin Pharmacokinet. 2025;64(5):729–741. [doi:10.1007/s40262-025-01499-z](https://doi.org/10.1007/s40262-025-01499-z).
7. <span id="ref-7"></span>Amgen Inc. IMDELLTRA (tarlatamab-dlle) prescribing information [Internet]. DailyMed [cited 2026 Oct 3]. Sections 2 and 12.3, Table 17. [Product information](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=1e7b6163-5d83-42ea-82c9-cf7620cdc782).
8. <span id="ref-8"></span>Chen PW, Minocha M, Kong S, Jiang T, Anderson ES, Parkes A, et al. Tarlatamab exposure–efficacy and exposure–safety relationships to inform dose selection in patients with small cell lung cancer. Clin Cancer Res. 2025;31(22):4688–4697. [doi:10.1158/1078-0432.CCR-25-2134](https://doi.org/10.1158/1078-0432.CCR-25-2134). [Full text and supplementary materials](https://pmc.ncbi.nlm.nih.gov/articles/PMC12616239/). [Supplementary Table S1](https://doi.org/10.1158/1078-0432.30618111).
9. <span id="ref-9"></span>Sands JM, Champiat S, Hummel HD, Paulson KG, Borghaei H, Bustamante Alvarez J, et al. Practical management of adverse events in patients receiving tarlatamab, a delta-like ligand 3–targeted bispecific T-cell engager immunotherapy, for previously treated small cell lung cancer. Cancer. 2025;131(3):e35738. [doi:10.1002/cncr.35738](https://doi.org/10.1002/cncr.35738). [Full text, Figure 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC11775405/).
10. <span id="ref-10"></span>Li T, Tredennick A, Polhamus D, Putnins M, Liu S, Sanghavi K, et al. Epcoritamab Step‐Up Dosing Regimen Selection and Optimization Using Repeated Time‐to‐Event Modeling for Cytokine Release Syndrome Risk Mitigation. Clinical Pharmacology & Therapeutics. 2026;120(2):542–551. [doi:10.1002/cpt.70362](https://doi.org/10.1002/cpt.70362).
11. <span id="ref-11"></span>Guo Y, Niu J, Cardé NAQ, Wu L, Miao X, Hanson S, et al. Teclistamab Dosing in Responders: Modeling and Simulation Results from the MajesTEC-1 Study in Relapsed/Refractory Multiple Myeloma. Targeted Oncology. 2025;20(4):651–661. [doi:10.1007/s11523-025-01149-1](https://doi.org/10.1007/s11523-025-01149-1).
12. <span id="ref-12"></span>Li CC, Bender B, Wilkins J, Li F, Turner DC, Wang B, et al. A Novel Step‐Up Dosage Regimen for Enhancing the Benefit‐to‐Risk Ratio of Mosunetuzumab in Relapsed or Refractory Follicular Lymphoma. Clinical Pharmacology & Therapeutics. 2025;117(2):465–474. [doi:10.1002/cpt.3445](https://doi.org/10.1002/cpt.3445).
