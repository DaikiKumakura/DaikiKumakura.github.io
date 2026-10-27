## 要旨 {#article-abstract}

公開されたマウスの血液・腫瘍・DUSP6モデルを再構築し、同じ正規化1日量のQD・BID・TIDを仮想条件として比較した。公表実装の再現性、仮定したPK/PDから数理的に得られる結果、新規薬剤へは適用できない部分を区別した。結論は条件付きである。**血漿半減期だけでは投与回数は決まらない。** 分布、力価、標的turnover、曝露の低い側の集団が関係する。基準仮想集団では、同じ1日量を分割すると投与間隔の90%以上で濃度閾値を保つ割合は**20.6%から61.5%**へ上がった。これはシミュレーション結果であり、臨床奏効率やdaraxonrasibの推奨投与法ではない。

## 背景と目的 {#article-introduction}

経口薬の1日総量が同じでも、分割によって持続的な標的阻害はどれだけ変わるか。その比較を新規RAS阻害薬へ使うには何を測る必要があるか。

解析の問いは、正規化した1日量を揃えたとき、分割が集団の標的作用維持を実質的に変える条件と、その結論を変えうる未測定の性質である。用途は公開根拠の再構築と研究・学習用のモデル検討とする。初回ヒト投与量、治療域、患者の薬効・毒性は決めない。「実質的」は例示として作用維持割合の10パーセントポイント差とし、臨床的に重要な最小差ではない。

比較するのは仮想薬剤であり、異なるRAS薬を一括したモデルではない。可逆的RAS(ON)阻害薬と共有結合型KRAS阻害薬を、同じRASシグナルに作用するという理由だけで交換可能な観測とは扱えない。

## 方法と結果 {#article-methods-results}

### 対象と確認範囲 {#scope-and-sources}

表1に公開資料から利用できる情報と限界を示す。PKは薬物動態、PDは薬力学、PopPKは母集団薬物動態を指す。投与回数はQDが1日1回、BIDが1日2回、TIDが1日3回である。

**表1　公開根拠の範囲**

| Evidence | Usable information | Boundary |
|---|---|---|
| Daraxonrasib/RMC-6236 mouse supplement | Blood, tumor and DUSP6 group means; equations; point estimates | Sparse means are not repeated individual observations |
| Daraxonrasib human label | Summary systemic PK at a stated clinical dose | Not an individual-data PopPK dataset or tumor PK model |
| RMC-7977 study | Mechanistic context and downloadable source data | Not a human population distribution for another molecule |
| Olomorasib clinical study | Compound-specific exposure and dosing observations | Cannot identify turnover parameters for a new inhibitor |
| Virtual analysis here | Transparent paired comparisons under stated assumptions | Does not estimate drug-specific clinical parameters |

RMC-6236の原著は、各時点3匹の動物から作った疎な平均推移への当てはめを記載している。構造の再構築には使えても、ヒトのランダム効果分布は得られない。出版社配布のSupplementary MethodsとTables S8/S9を取得し、Table S9からモデル構築群と別の検証群を合わせた72の投与・観測記録を抽出した。実験とモデルの文脈は原著を参照した ([1](#ref-1))。

公表された訂正も確認した ([2](#ref-2))。図ラベルと細胞パネルの方法に関する訂正である。選んだ5つの補足資料について、取得した2024年版と2025年版のファイルハッシュは同じだった。これはファイル同一性の確認であり、式のすべての曖昧さを解消するものではない。

RMC-7977の出典データはNature原著から取得でき、確認資料へ保存したが、ヒト縦断PKを作るためには使わなかった ([3](#ref-3))。Olomorasib原著は約3時間の半減期とBID開発、モデルによるTEC80維持を報告する ([4](#ref-4))。薬剤固有の根拠であり、短半減期の全阻害薬にBIDが必要、または共有結合型ならQDが十分と示すものではない。

### マウスの血液・腫瘍・経路モデル {#mouse-model}

経口1コンパートメント血液PK、腫瘍との交換、間接DUSP6応答を組み合わせる。吸収・血液区画の量を (A_a,A_b)、血中濃度を (C_b=A_b/V)、腫瘍濃度を (C_t)、DUSP6の百分率を (E) とする。

\[
\frac{dA_a}{dt}=-k_aA_a,\qquad
\frac{dA_b}{dt}=k_aA_a-CL\,C_b
\]

\[
\frac{dC_t}{dt}=k_{pt}f_u\frac{C_b}{BP(C_b)}-k_{tb}C_t
\]

\[
\frac{dE}{dt}=100k_{out}\left(1-\frac{C_t}{IC_{50}+C_t}\right)-k_{out}E.
\]

**表2　マウスモデルに用いた公表パラメータ**

| Quantity | Value used | Role |
|---|---:|---|
| \(k_a\) | 0.648316 h⁻¹ | Absorption |
| \(V/F\) | 10.199248, printed as L | Apparent volume; normalization caveat below |
| \(CL/F\) | 2.910761 L/h | Apparent blood clearance |
| \(k_{pt}\), \(k_{tb}\) | 115, 0.1 h⁻¹ | Tumor exchange |
| \(f_u\) | 0.011 | Mouse unbound plasma fraction |
| \(IC_{50}\) | 42.261016 nM | Tumor concentration–DUSP6 inhibition |
| \(k_{out}\) | 2.385655 h⁻¹ | DUSP6 turnover |

点推定は[原著Supplementary Table S8](https://doi.org/10.1158/2159-8290.30062210)、式と結合の仮定は[Supplementary Methods](https://doi.org/10.1158/2159-8290.30062234)に基づく ([1](#ref-1))。パラメータ推定値の変動係数（CV）は推定精度を表すので、個体間変動へ読み替えていない。

出典には2つの曖昧さがある。S9の用量はnmol/kgだが、S8の見かけ容積はLと表記される。計算は印字値を使い、nMを得るのに必要な暗黙の用量正規化を置いた。単位まで整合した完全な実装仕様は未確定である。もう1つはMethodsの結合式である。

\[
BP(C_b)=5.5-\frac{5.2C_b}{1819+C_b},
\]

一方、マウス結合表はIC50を約1.8188、単位をnMと記す。分母は約1,000倍異なる。Methodsの式を主実装、表の文字どおりの値を感度条件とし、どちらかを無断で訂正しなかった。腫瘍濃度は総濃度であり、出典の交換項から非結合腫瘍分配係数の同定は示されない。

![マウス公表平均と血液・腫瘍・DUSP6の再構築曲線](shared/ras-inhibitor-target-coverage/figures/01-public-model.png)

**図1　マウスモデルの再構築。** 単回25 mg/kgと10回目の毎日投与について、[原著Supplementary Table S9](https://doi.org/10.1158/2159-8290.30062207)の群平均を示す ([1](#ref-1))。実線はMethodsの結合式、破線は表の分母で、変更が影響するのは腫瘍・PDであり血液PKではない。点は個体縦断データではない。対数軸は相対的な不一致を見やすくする。

図1と表3に再構築の差を示す。抽出したPK/PD群の正の観測値について、絶対相対誤差の中央値を集計した。

**表3　再構築値の記述的な残差**

| Endpoint | Observations | Methods denominator | Literal table denominator |
|---|---:|---:|---:|
| Blood concentration | 43 | 25.9% | 25.9% |
| Tumor concentration | 30 | 45.2% | 557.4% |
| DUSP6 expression | 30 | 62.8% | 80.5% |

新たな尤度で当てはめた適合度推定ではなく、記述的な再現残差である。構築群と検証群へ同じパラメータを使い、図を合わせる再調整はしていない。ゼロに近いDUSP6は相対誤差を大きくするため、元尺度の曲線と配布残差を併せて読む必要がある。実行できるファイルでも予測モデルとして妥当とは限らず、**特に腫瘍・経路予測の再構築は不完全である**。

#### ヒトPK要約の独立した照合 {#human-summary-check}

FDA添付文書は300 mg QDで、AUC 3,760 ng·h/mL、Cmax 365 ng/mL、Tmax中央値2.2 h、終末相半減期9.2 h、見かけクリアランス80.4 L/hとする ([5](#ref-5))。これらの全身PK要約を、マウス全血の観測と混ぜない。

限定的な照合として、クリアランスと終末相半減期を1コンパートメント近似へまとめ、単回Tmaxに合う吸収速度を求めた。周期的なQDのAUCは**3,731 ng·h/mL**だったが、ピークは**287.8 ng/mL**と添付文書より約21%低かった。AUC一致の多くは用量/クリアランスによるもので、濃度時間形状を検証しない。終末相半減期、平均CL、Tmax中央値も、1人の典型患者を表すとは限らない。この近似をヒト腫瘍応答モデルとして移植していない。

### 仮想薬剤の仮定 {#virtual-drug-assumptions}

設計の依存関係を理解するための仮定であり、RAS阻害薬の推定済みPopPK事前分布ではない。表4に設定を示す。

**表4　仮想薬剤の設定**

| Assumption | Reference | Sensitivity |
|---|---|---|
| Apparent normalized volume | 1 | No independent volume variability modeled |
| Absorption rate | 1 h⁻¹ | 0.5–2 h⁻¹ |
| Plasma half-life | 4 h | 2–24 h |
| Reference mean concentration / C90 | 3 | 0.25–8 phase grid |
| Clearance CV | 40% | 20%, 60% |
| Relative exposure multiplier CV | 30% | Multiplicative exposure shifts |
| Tumor/plasma ratio | 1 | 0.5, 2; wider global range |
| Tumor equilibration half-life | Instantaneous | 2, 8 h |
| Target turnover half-life | 24 h | 6, 72 h |

クリアランスと相対曝露倍率は、中央値1の独立な対数正規分布とした。後者は1を超えうるので、**絶対経口バイオアベイラビリティではない**。基準比3は基準被験者の値で、仮想集団の算術平均ではない。潜在曝露の比較であり観測への当てはめではないため、残差観測誤差は加えていない。

消失速度 (k=log(2)/t_{1/2})、間隔 (	au)、正規化1回量 (D) の周期的経口濃度は次式となる。

\[
C_{ss}(t)=\frac{Dk_a}{V(k_a-k)}
\left[\frac{e^{-kt}}{1-e^{-k\tau}}-
\frac{e^{-k_at}}{1-e^{-k_a\tau}}\right],\quad 0\le t\le\tau.
\]

同じシナリオ点ではQD、BID、TIDの1日総量を等しくするので、対応する各被験者の線形全身AUCは変わらない。相図の座標では半減期と基準曝露比を変え、指定比を保つよう格子点間で1日量を調整した。一方、別の大域感度計算では半減期を変えても1日量を固定している。

#### 持続阻害の3つの定義 {#persistent-inhibition}

可逆的な濃度駆動阻害は次式とし、仮定C90を1に正規化する。

\[
I(t)=\frac{C_t(t)}{1/9+C_t(t)}.
\]

遅延経路応答では残存活性 (R) を (dR/dt=k_{out}[1-I(t)-R]) とする。共有結合型の標的阻害では、阻害されていない残存標的 (U) を次式で表す。

\[
\frac{dU}{dt}=k_{deg}(1-U)-
\frac{k_{inact}C_t(t)}{K_I+C_t(t)}U,\qquad TE=1-U.
\]

共有結合型の基準は (K_I=1)、(k_{inact}=18log(2)/24) h⁻¹とし、標的turnover半減期24 hのとき、一定濃度1で90%阻害となる。1つの定常参照点を合わせたのであって、**濃度応答曲線全体の一致ではない**。非線形モデル間には記憶以外の差もあり、結果差を「可逆対共有結合」だけへ帰属できない。この共有結合式をdaraxonrasibに当てはめていない。

腫瘍平衡化の感度条件は (dC_t/dt=k_t(K_pC-C_t)) を使う。選んだ (K_p) がヒト腫瘍で測定されたとは主張せず、平滑化と残留を検討する。

### 集団の作用維持指標と結果 {#coverage-metrics-and-results}

各仮想被験者の**TAT**は、仮定した作用閾値を超える投与間隔内の時間割合である。可逆阻害は濃度≥C90、持続モデルは阻害≥90%を直接使う。**PTC90**はTAT≥90%となる被験者割合であり、2つの90の役割は異なる。PTC80/PTC95は作用閾値を同じに保ち、必要時間割合を変えたものとする。

トラフ、ピーク、全身AUC、正規化した閾値未満の不足量も報告する。不足ゼロは閾値を下回らないことであり、臨床リスクゼロではない。維持確率は仮定した分布と閾値を条件とする。主条件は10,000人とし、投与法間で同じ乱数標本を使った。差の標準誤差は患者内の達成差から求め、QDとBIDを独立集団として扱っていない。

![可逆・共有結合・遅延経路モデルでの半減期とPTC90](shared/ras-inhibitor-target-coverage/figures/02-mechanism.png)

**図2　3つの仮想機構のPTC90。** 基準曝露比3、CLのCV 40%、相対曝露CV 30%。適用する標的・経路turnover半減期は24 hである。

**表5　集団での持続作用の比較**

| Half-life | Model | QD PTC90 | BID PTC90 | BID − QD |
|---|---|---:|---:|---:|
| 4 h | Reversible | 20.6% | 61.5% | +40.9 pp |
| 4 h | Covalent | 29.6% | 79.1% | +49.5 pp |
| 4 h | Delayed pathway | 47.3% | 87.6% | +40.3 pp |
| 8 h | Reversible | 56.8% | 85.5% | +28.7 pp |
| 24 h | Reversible | 90.7% | 96.4% | +5.7 pp |

図2と表5の4時間・可逆基準では、BID−QD差の対応Monte Carlo標準誤差は約**0.49パーセントポイント**だった。この差に対するMonte Carlo不確実性は小さいが、モデル不確実性はこの標準誤差に含まれない。正規化平均1日AUCは両投与法とも約80.4、平均ピークは9.28から5.50へ下がった。線形PKのもとで総曝露を増やさず波形を変えた比較である。

持続性も普遍的な答えにはならない。共有結合モデルの不活化速度を固定し、標的turnover半減期を24から72 hへ変えるとQD PTC90は29.6%から93.4%となり、BIDはこの有限仮想標本で100%となる。6 hのturnoverではどちらもPTC90を達成しない。固定不活化速度の飽和上限は81.8%阻害なので、濃度を増やしても90%閾値へ届かない。標的の速い再生は持続阻害を妨げ、遅い再生は分割の追加利得を減らしうる。シミュレーション100%は普遍的な達成の証明ではない。

### 分割投与の効果が変わる領域 {#dose-splitting-regions}

![半減期と基準曝露比に対するQD・BIDの作用維持相図](shared/ras-inhibitor-target-coverage/figures/03-phase.png)

**図3　作用維持の相図。** 可逆モデル、半減期14値×基準曝露比18値、格子点あたり2,000人。色は確率またはパーセントポイント差で、探索座標であり臨床用量境界ではない。

図3の利得が大きいのは、トラフが制約となり、曝露増加で閾値を超えられる領域である。BIDでもほぼ全員が閾値未満なら、分割では平均曝露の不足を補えない。QDでほぼ全員を覆えていれば追加利得は小さい。「短半減期ならBID」だけでは不完全な理由である。

10ポイントという規則では標本格子の48.0%を実質的な利得ありと分類した。5または20ポイントなら60.7%または30.2%になる。これは**格子の割合**であり、存在する薬剤や患者の割合ではない。範囲と間隔に依存する。

2,000人格子の二項Monte Carlo標準誤差の点ごとの最大は約1.12ポイントである。選んだ3つの基準・境界点で10,000人と細かい積分にすると、PTC90推定は最大2.79ポイント変わった。粗い図は大きなパターンを見るには使えるが、精密な判断境界の推定ではない。確率と確認値は配布表へ記録した。

### 曝露の負担と投与回数 {#exposure-and-burden}

![仮想投与法の作用維持と全身曝露の比較](shared/ras-inhibitor-target-coverage/figures/04-pareto.png)

**図4　仮定した21の投与条件。** 線は同じ投与頻度内の用量を結び、治療推奨を表さない。

図4のPareto比較は、高いPTC90、低い1日AUC、低いピーク、少ない投与回数の4目的を使う。分割は作用維持とピークを改善しうるが回数が増える。1日総量を増やせば曝露負担が増す。測定された安全性関係と選好がないため、単一の最適行動は決められない。ピークとAUCはここでは曝露の負担であり、副作用予測ではない。

配布表には非劣解を記した。他の標本行動が指定目的のすべてを改善しないという意味であり、臨床的優位性ではない。候補集合を増やせばフロンティアは変わりうる。

### 未測定の性質への感度 {#sensitivity}

局所感度表ではCLのCV、腫瘍分配・平衡化、標的turnoverを変えた。別のLatin hypercube設計は400パラメータ組、各512人の対応標本、固定1日量を使い、半減期、CL・曝露倍率、腫瘍分配、力価、吸収、turnoverを指定範囲で変えた。

![BID−QDの作用維持差に対する偏順位相関](shared/ras-inhibitor-target-coverage/figures/05-sensitivity.png)

**図5　感度のスクリーニング。** 偏順位相関（PRCC）は標本範囲とモデルに依存する。ゼロ付近の係数でも非単調な依存を隠しうる。

図5ではMarinoらが述べる方法に従って、PRCCをスクリーニングへ用いた ([6](#ref-6))。単調な関係で特に情報を持つ。相図は利得の非単調なパターンを示すため、係数を**その差の信頼できる大域重要度順位とは扱えない**。Sobol分散割合でも情報価値でもない。設計あたりの集団が小さいため、確率も主条件より不精密である。

共有結合型のQD維持では、この設計で標的turnover半減期との強い正の偏順位関連0.88があった。仮定を検討する根拠であり、測定済み臨床要因ではない。半減期、腫瘍分配、力価は曝露と閾値の計算で部分的に代替でき、現実の相関分布なら独立入力の結果は変わりうる。

新規薬剤へ移すには、対応する血漿・腫瘍または妥当な代替曝露、濃度依存結合、薬物除去後の標的作用回復、反復PK、変動・共変量の情報が必要になる。解析は依存関係を示すが、測定取得の経済価値は計算していない。

### 非線形PKと時間依存への感度 {#nonlinear-time-dependent-pk}

#### 投与の中断 {#interruption}

![欠薬・4時間遅延・24時間と48時間の中断による仮想濃度](shared/ras-inhibitor-target-coverage/figures/06-interruptions.png)

**図6　投与中断。** 基準被験者の可逆濃度と正規化閾値。意図的に変えた数理シナリオであり、飲み忘れへの対処手順ではない。

図6が示すように、定常作用維持と中断への耐性は異なる。規則的BIDの利得は実際に投与されることを条件とする。予定回数の増加は服薬負担も変えるが、このPKモデルでは推定していない。線形PKを保つ軌跡で、臨床的回復や病勢進行も予測しない。

#### 吸収の飽和 {#saturating-absorption}

![同じ1日量で仮定した用量依存吸収倍率による曝露差](shared/ras-inhibitor-target-coverage/figures/07-absorption.png)

**図7　吸収の感度条件。** 正規化量に対する吸収倍率 (1/(1+D_{each}/2)) を仮定した。2は測定されたRAS阻害薬の値ではない。

図7のように曝露が用量比例未満なら、分割で各回の吸収割合が高くなり、同じ1日量でもAUCが増える。線形比較のAUC固定という解釈は成立しない。局所的な用量弾力性は (1/(1+D_{each}/2)) となる。吸収確認の必要性を示す単純モデルで、olomorasibやdaraxonrasibの観測へ当てはめてはいない。

#### クリアランスの変化 {#changing-clearance}

![一定CLと初期値の50%へ低下するCLでの14日間の仮想濃度](shared/ras-inhibitor-target-coverage/figures/09-changing-clearance.png)

**図8　時間依存CL。** 変化の半減期は仮定した3.5日で、特定薬剤へ帰属しない。

図8のようにCLが変われば、単一の定常推移ではすべての治療日を表せない。仮定した低下条件では、用量と間隔を変えなくても後の曝露が増す。終末相半減期を全期間へ写す代わりに、反復観測と時間を扱う実装が必要になる。

### 曝露と転帰の関連の因果解釈 {#exposure-outcome-confounding}

![固定病勢下の曝露効果が正でも周辺関連が負となる合成例](shared/ras-inhibitor-target-coverage/figures/08-confounding.png)

**図9　完全な合成データ。** 臨床患者の観測は含まない。仮想病勢の増加は曝露を増やし、奏効確率を下げる。

図9は20,000人で、病勢とノイズから対数曝露を、曝露と病勢から奏効を生成した。生成した曝露の対数オッズ係数は+0.6だったが、単純ロジスティック推定は**−0.506**、病勢調整モデルは**+0.575**だった。明示した仮定で符号逆転が生じうる例であり、RAS阻害薬試験でこの機構が説明になると実証したものではない。

集約曝露反応曲線だけでは、薬効不足、病勢による交絡、CL変化、選択的な追跡、真の濃度効果を区別できない。臨床解析には適切な縦断データ、時点、特定した因果の問いが必要である。

### 数値実装の検証 {#numerical-checks}

周期的PK・腫瘍の解析解は、独立した反復投与ODE実装と最大絶対誤差 (10^{-7}) 未満で一致した。高解像度AUCは解析的な用量/CL恒等式と0.001%以内で一致し、線形閾値交差の検査も通過した。240から960区間への細分化で基準PTC90変化は可逆・共有結合モデルで0ポイント、遅延経路で0.03ポイントだった。一方、経路閾値付近の個人TAT差は4.1ポイントに達し、集団達成値の安定性から各軌跡も同精度とは言えない。

## 考察 {#article-discussion}

数値検査は実装の整合性を示す。マウス資料の単位曖昧性、再構築残差、未知のヒト腫瘍曝露、未測定turnover、仮想集団分布、臨床安全性との連結欠如は解消しない。Python実装は集約マウス資料と仮想投与法を扱い、ヒト個体間変動を推定していない。

支持されたのは、公開モデルの透明な再構築、不一致の特定、指定した機構と変動のもとで対応させた仮想投与法比較である。新規薬剤の臨床QD/BID選択、安全な初回量、腫瘍応答予測、マウス経路閾値のヒト治療域への直接移植は支持されない。

ヒト腫瘍曝露、標的・経路turnover、患者間変動が未測定である限り、新規薬剤への分割・中断比較の適用はそれらの仮定を条件とする。

## 結論 {#article-conclusion}

仮定したPK/PDと集団分布では分割投与が持続的作用維持を変えた。血漿半減期だけでは比較は決まらず、分布、力価、turnover、曝露変動で解釈が変わった。マウス再構築の不完全さと未測定のヒト特性から、臨床投与法の推奨には至らない。

## データとコードの公開状況 {#availability}

[実行済みノートブック・実行可能コード・公表値由来の表・図・検証結果のダウンロード](shared/ras-inhibitor-target-coverage/ras-coverage-analysis.zip)。`analysis.py`、`extras.py`、`scientific_checks.py`の順に実行し、ノートブックも同じ計算を行う。出典台帳に原資料URLと取得状況を記録した。出典帰属を付けたS9由来の平均値を含み、原補足資料は別途取得できる。すべての図は本解析で作成した。

## 参照 {#article-references}

1. <span id="ref-1"></span>Jiang J, Jiang L, Maldonato BJ, Wang Y, Holderfield M, Aronchik I, et al. Translational and Therapeutic Evaluation of RAS-GTP Inhibition by RMC-6236 in RAS-Driven Cancers. Cancer Discovery. 2024;14(6):994–1017. [doi:10.1158/2159-8290.CD-24-0027](https://doi.org/10.1158/2159-8290.CD-24-0027). [Supplementary Table S8](https://doi.org/10.1158/2159-8290.30062210); [Supplementary Methods](https://doi.org/10.1158/2159-8290.30062234); [Supplementary Table S9](https://doi.org/10.1158/2159-8290.30062207). Original article and supplements: CC BY 4.0; derived group means retain this attribution.
2. <span id="ref-2"></span>Jiang J, Jiang L, Maldonato BJ, Wang Y, Holderfield M, Aronchik I, et al. Correction: Translational and Therapeutic Evaluation of RAS-GTP Inhibition by RMC-6236 in RAS-Driven Cancers. Cancer Discovery. 2025;15(10):2186. [doi:10.1158/2159-8290.CD-25-1519](https://doi.org/10.1158/2159-8290.CD-25-1519).
3. <span id="ref-3"></span>Holderfield M, Lee BJ, Jiang J, Tomlinson A, Seamon KJ, Mira A, et al. Concurrent inhibition of oncogenic and wild-type RAS-GTP for cancer therapy. Nature. 2024;629(8013):919–926. [doi:10.1038/s41586-024-07205-6](https://doi.org/10.1038/s41586-024-07205-6).
4. <span id="ref-4"></span>Murciano-Goroff YR, Hollebecque A, Heist RS, Cassier PA, Han JY, Kim SY, et al. Pan-tumor activity of olomorasib, a next-generation KRAS G12C inhibitor in KRAS G12C-mutant advanced solid tumors: a first-in-human study. Nature Communications. 2026;17(1):3834. [doi:10.1038/s41467-026-69943-7](https://doi.org/10.1038/s41467-026-69943-7).
5. <span id="ref-5"></span>US Food and Drug Administration. RASONQUE (daraxonrasib) prescribing information [Internet]. 2026 [cited 2026 Oct 28]. Section 12.3. [Official label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/220910Orig1s000lbl.pdf).
6. <span id="ref-6"></span>Marino S, Hogue IB, Ray CJ, Kirschner DE. A methodology for performing global uncertainty and sensitivity analysis in systems biology. J Theor Biol. 2008;254(1):178–196. [doi:10.1016/j.jtbi.2008.04.011](https://doi.org/10.1016/j.jtbi.2008.04.011).
