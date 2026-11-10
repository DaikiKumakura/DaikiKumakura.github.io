**QOI：Phase 1 の二次治療 26 人のデータで、Phase 3 の RAS G12 集団の奏効率と生存期間をどこまで絞れたか。**

**COU：Phase 1 拡大コホートの結果にもとづいて Phase 3 へ進む判断の根拠になる情報量を評価し、コホートを増やす価値を見積もる。後ろ向きの照合であり、判断そのものには使わない。**

QOI（Question of Interest）は本稿が答える問い、COU（Context of Use）はその答えの使い道である。対象は、GTP 結合型（活性型）の RAS に結合して働きを抑える薬、ダラキソンラシブ（daraxonrasib、RAS(ON) 阻害薬）である。2025 年 9 月に企業が開示した Phase 1 の二次治療（2L）RAS G12X 26 人（奏効 9 人、300 mg を 1 日 1 回）([1](#ref-1)) から、2026 年に報告された Phase 3 試験 RASolute 302 の RAS G12 集団のダラキソンラシブ群 ([2](#ref-2), [3](#ref-3)) の奏効率（ORR）と生存期間を予測し、実測と比べた。答えは次のとおりである。26 人は Phase 3 の ORR を約 18〜55%（95% 予測区間、試験間のずれを許さない場合）に絞り、実測の 33.2% はその内側にあった。試験間のずれを許すと区間は 12〜66% に広がり、コホートを増やしても幅はほとんど縮まなかった。

## 要旨

**問題**　小さな Phase 1 拡大コホートは、Phase 3 の結果についてどれだけの情報を持っていたか。結果が分かっている現在の後ろ向きの照合として、2025 年末までに公開されていた情報だけで予測し、実測と比べた。

**方法**　Phase 1 の ORR 9/26 から Beta-二項モデルで Phase 3 の奏効人数の予測分布を作り、試験間のずれの大きさ τ（ORR ではロジット尺度）を 0、0.25、0.5、0.75 の場合分けとして置いた。無増悪生存期間（PFS）と全生存期間（OS）の中央値は、報告された 95% 信頼区間から対数尺度の標準誤差を復元して照合した。Phase 1 のコホートの大きさ（26〜104 人）を変えた模擬で、予測区間の幅と「進む」判断の確率を見た。機序モデルは当てはめていない。

**結果**　ORR の実測 33.2%（72/217、人数は逆算）は、τ = 0 の 95% 予測区間 17.5〜54.8% と τ = 0.5 の 12.0〜65.9% の内側にあった。Phase 1 を使ったモデルは、弱い基準（Beta(0.5, 0.5)）より対数予測スコアが 1.1〜1.8 nats 良かった。点推定の外挿（9/26 をそのまま使う）はこの 1 組でさらに良かった（2.8 nats）が、繰り返しの模擬では、真の τ が 0 でも 0.5 でも被覆率が最も低かった。PFS の実測 7.3 か月は予測区間 6.6〜11.0 か月の内側、OS の実測 13.2 か月は 9.4〜18.3 か月の内側だったが、標準誤差を 2 倍にすると OS の区間は 6.7〜25.5 か月になり、Phase 3 の追跡が短いため OS の照合はほぼ自明な通過である。Phase 1 を 26 人から 104 人に増やしても、τ = 0.5 の予測区間の幅は 51 から 45 ポイントにしか縮まなかった。

**結論**　Phase 1 の 26 人は、Phase 3 の ORR を試験間のずれの仮定に応じて 12〜66% の範囲に絞り、実測を区間内に置いた。ずれが大きい場合、コホートを増やしても予測区間はほとんど縮まない。「進む」判断の確率が上がる場面はあるが、その大きさは閾値、規則、真の奏効率の置き方に依存する。

## 背景と目的

Phase 1 の拡大コホートは、Phase 3 へ進むかを決める根拠になることが多い。ダラキソンラシブの場合、企業は 2025 年 9 月 10 日の 8-K（米国証券取引委員会への臨時報告書）で、2L の efficacy evaluable 集団（定義は書かれていない）の RAS G12X 26 人について、ORR 35%（9/26）、PFS の中央値 8.5 か月、OS の中央値 13.1 か月を開示した ([1](#ref-1))。後に Phase 3 の RASolute 302 が報告され ([2](#ref-2), [3](#ref-3))、Phase 1 の論文が出版された ([4](#ref-4))。この時間差があるため、2025 年末までの公開情報と 2026 年の実測を分けて、予測と照合を行える。

本稿は、26 人の情報がどこまで Phase 3 を絞ったかと、コホートを増やす価値を数える。これは実測を知った状態で設計した後ろ向きの照合であり、実測に対して盲検ではない。モデルと基準を実行前に固定したことを示す記録はない。基準 (b) と (c)、Beta(1,1) 事前分布、標準誤差の 2 倍の感度解析、繰り返しの模擬は、最初の結果を見た後に説明のために加えた。訓練の区切りを 2025 年末にしたことと、2026 年の Phase 1 論文を事後の資料に分類したことも、後ろ向きの選択である。

## 方法

### 訓練の情報と照合の情報

訓練の情報は、2025 年 12 月 31 日までに公開されていたものに限った。入力は 8-K の数値である ([1](#ref-1))（2L のデータカットオフ 2025 年 6 月 30 日）。RAS G12X は ORR 9/26（35%）、PFS の中央値 8.5 か月（95% 信頼区間 6.7〜10.5）、OS の中央値 13.1 か月（10.9〜NE（推定不能、not estimable））、追跡期間の中央値 16.7 か月（範囲 10.3〜24.6）である。RAS 変異（G12X、G13X、Q61X）全体は 11/38（29%）だった。ORR は固形がんの腫瘍縮小の判定基準 RECIST v1.1 で、確認済みまたは確認の可能性が残る奏効を数えている ([1](#ref-1))。8-K の安全性の集団（83 人）は 2L 以降であり、効果の集団は「2L efficacy evaluable」と表記されて定義は書かれていない。[8-K の Figure 1〜3](https://www.sec.gov/Archives/edgar/data/1628171/000119312525200078/d947102d8k.htm)（腫瘍縮小率の図と PFS・OS の暫定図）は画像であり、読み取りも転載もしていない。

照合の情報は、RASolute 302 の RAS G12 集団のダラキソンラシブ群である。原著 ([2](#ref-2)) は抄録までしか読めず（本文は取得できなかった）、G12 集団の数値は二次情報の報道 ([3](#ref-3)) による。ORR 33.2%（評価可能 217 人）、PFS の中央値 7.3 か月（6.3〜8.1）、OS の中央値 13.2 か月（10.0〜NE）、追跡期間の中央値 8.5 か月（範囲 3.2〜15.9、試験全体）、データカットオフ 2026 年 2 月 10 日である。奏効の人数は報告されておらず、33.2% と 217 人から逆算した 72 人を用いた（72/217 = 33.2% で、71 や 73 では報告値と合わない）。ランダム化 228 人を分母にした 76 人は感度解析とした（76/228 = 33.3% は報告値と丸めが合わない近似である）。Phase 1 の論文 ([4](#ref-4)) と FDA の承認情報 ([5](#ref-5)) は 2025 年末より後の資料であり、事後の解釈にだけ使った。

### 奏効率の予測

Phase 1 の奏効人数 9/26 から、真の ORR $p_1$ の事後分布を Beta(0.5 + 9, 0.5 + 17)（Jeffreys 事前分布。Beta(1,1) を感度解析とした）とした。Phase 3 の真の ORR $p_3$ は、試験間のずれ $\delta$ を許して次のように置いた。

$$\operatorname{logit}(p_3)=\operatorname{logit}(p_1)+\delta,\qquad \delta\sim\mathcal{N}(0,\tau^2)$$

Phase 3 の奏効人数 $Y_3$ は $p_3$ を持つ二項分布 $\operatorname{Binomial}(217, p_3)$ とした。$\tau$（試験間のずれの大きさ）は 0、0.25、0.5、0.75 を場合分けとして置いた。これらのデータから $\tau$ は推定できない。$\tau = 0.5$ は、Phase 3 の奏効のオッズが Phase 1 の約 1.65 倍または 0.61 倍に動く 1 標準偏差に相当する。予測分布は、Beta 事後分布の分位点 4,000 点と $\delta$ の Gauss–Hermite 41 点による数値積分で求め、乱数は使っていない。

評価は、予測区間（50、80、95%）、実測の人数の予測確率、対数予測スコア（実測の人数の予測確率の自然対数。厳密に適正なスコア ([6](#ref-6))。単位は nats で、大きいほど良い）、確率積分変換（PIT）で行った。PIT は予測分布の累積確率で実測が占める位置を表し、0.5 付近なら予測の中央にあたる。離散分布では、実測の直前までの累積確率に実測の確率の半分を加えた中点版を使った。これはランダム化 PIT ([7](#ref-7)) の期待値にあたる。基準は 3 つ置いた。(a) 9/26 をそのまま使う点推定の外挿、(b) Phase 1 の情報を使わない弱い基準（$p_3 \sim$ Beta(0.5, 0.5)。平均 50% で 0〜100% に広がる U 字型であり、2025 年時点の現実的な弱情報事前分布ではない）、(c) RAS 変異全体の 11/38 を事前分布にしたもの（G12X の患者を含み、独立ではない）である。

### 生存期間の中央値

生存期間は集計値のみで扱った。報告された中央値を対数中央値の推定値とし、標準誤差は 95% 信頼区間が対数尺度で対称だと仮定して、$\mathrm{se}=(\ln \mathrm{upper}-\ln \mathrm{lower})/(2\times1.96)$ と復元した。OS は上限が NE のため、下限だけから $\mathrm{se}=(\ln m-\ln \mathrm{lower})/1.96$ とした。26 人の Phase 1 では、指数分布を仮定した事象数ベースの標準誤差 $1/\sqrt{26}\approx0.20$ が復元値（PFS 0.11、OS 0.09）より大きいため、感度解析として OS で 1.5 倍と 2 倍、PFS で 2 倍を置いた。Phase 3 の中央値の対数が従う分布を $\mathcal{N}(\ln m_1,\ \mathrm{se}_1^2+\tau^2)$ とし、実測の中央値の観測誤差（Phase 3 の信頼区間から同様に復元）を加えて、実測が予測区間に入るかを見た。ここでの $\tau$ は対数中央値の尺度であり、ORR のロジット尺度の $\tau$ とは別の量で、同じ 0.5 でも意味が違う。カプランマイヤー曲線の数値化は行っていない。

### 情報価値の模擬

Phase 1 のコホートの大きさ $n_1$ を 26、52、78、104 人とし、真の ORR を 0.20〜0.40 に置いて、奏効人数 $x_1\sim\operatorname{Binomial}(n_1,p)$ を乱数で生成した（シード 20261110、各条件 4,000 回）。事後分布 Beta(0.5 + $x_1$, 0.5 + $n_1-x_1$) から、$p_1$ の 95% 信用区間の幅と、$\tau = 0$ と 0.5 での Phase 3 の真の ORR の 95% 予測区間の幅を求めた（幅は 400 回、各 2,000 抽出で計算した）。また「$P(p>T\mid \text{データ})\ge 0.8$ なら進む」という規則（$T$ は 15、20、25%）で、進む判断になる確率を求めた。閾値は任意の場合分けで、臨床的な基準ではない。繰り返しの模擬では、真の $p_1$ を Phase 1 の事後分布から抽出し、$n_1$ 人の Phase 1 と 217 人の Phase 3 を 3,000 組生成した。模擬の乱数誤差は定量していない。

## 結果

### 訓練と照合の対応

図 1 は、公開の時期と本稿での使い分けである。表 1 は、訓練と照合の数値と、両者の定義の違いを並べたものである。

![2025 年 6 月から 2026 年 8 月までの時間軸に、Phase 1 のデータカットオフ、8-K の開示、訓練の区切り、Phase 3 のデータカットオフ、ASCO での発表、FDA 承認を示した図。](shared/daraxonrasib-phase1-phase3-information/figures/fig1_timeline.png)

図 1. 公開の時期。青は訓練に使った 2025 年末までの情報、橙は照合と事後の資料。ASCO（米国臨床腫瘍学会）の位置は OncLive の記事の日付（2026 年 5 月 31 日）である ([3](#ref-3))。FDA 承認の日付（2026 年 8 月 26 日）は FDA のページによる ([5](#ref-5))。

表 1. 訓練（Phase 1）と照合（Phase 3 の RAS G12 集団のダラキソンラシブ群）の入力。

| Item | Phase 1 (training) | Phase 3, RAS G12 (holdout) |
|---|---|---|
| Population | RAS G12X, 2L, 300 mg once daily, "2L efficacy evaluable" (undefined) | RAS G12, after one prior line ([5](#ref-5)), 300 mg once daily, randomized n = 228 |
| ORR | 35% (9/26) | 33.2% (72/217, count back-calculated) |
| Median PFS, months | 8.5 (6.7–10.5) | 7.3 (6.3–8.1) |
| Median OS, months | 13.1 (10.9–NE) | 13.2 (10.0–NE) |
| Median follow-up, months | 16.7 (range 10.3–24.6) | 8.5 (range 3.2–15.9), whole trial |
| Control-arm ORR (not usable in 2025) | Not applicable | 11.8% (evaluable n = 221) |
| ORR definition | RECIST v1.1, confirmed or potentially confirmable | Not stated in the sources read |
| ORR assessor | Not stated | Not stated in the sources read |
| Data cutoff | 2025-06-30 | 2026-02-10 |
| Sources | [1](#ref-1) | [2](#ref-2), [3](#ref-3), [5](#ref-5) |

注：ORR, objective response rate; PFS, progression-free survival; OS, overall survival; NE, not estimable; 2L, second line; RECIST, Response Evaluation Criteria in Solid Tumors.

### 奏効率の予測

図 2 は、$\tau = 0$ と 0.5 の予測分布と実測である。図 3 は、全モデルの予測区間と対数予測スコアである。表 2 に数値を示す。

![Phase 3 の ORR の予測分布。試験間のずれ τ = 0 と 0.5 の 2 本の曲線と、実測 33.2% の縦線。](shared/daraxonrasib-phase1-phase3-information/figures/fig2_orr_predictive.png)

図 2. Phase 1 の 9/26 から予測した Phase 3 の ORR の分布（Jeffreys 事前分布）。青は τ = 0、赤は τ = 0.5。縦軸は 1 パーセントポイントあたりの予測確率。実測の 33.2% の人数 72/217 は逆算した値である。

![予測モデルごとの 50、80、95% 予測区間（左）と、弱い基準 (b) に対する対数予測スコアの差（右）。](shared/daraxonrasib-phase1-phase3-information/figures/fig3_orr_scenarios.png)

図 3. 予測区間と対数予測スコア（実測 72/217）。青は Phase 1 を使ったモデル（τ ごと）、橙は基準 (a)〜(c)。左は 50%（太線）、80%（中線）、95%（細線）の予測区間で、点線は実測。右は (b) の弱い基準に対するスコアの差（nats、大きいほど良い）。

表 2. Phase 3 の ORR の予測（実測 72/217、`analysis/01_orr_prediction.py`）。

| Model | Mean ORR | 95% predictive interval | Predictive probability of 72 | Log score | PIT |
|---|---|---|---|---|---|
| Phase 1-informed, tau = 0 | 35.2% | 17.5–54.8% | 0.019 | −3.98 | 0.43 |
| Phase 1-informed, tau = 0.25 | 35.4% | 16.1–58.1% | 0.016 | −4.11 | 0.44 |
| Phase 1-informed, tau = 0.5 | 35.9% | 12.0–65.9% | 0.012 | −4.39 | 0.46 |
| Phase 1-informed, tau = 0.75 | 36.6% | 8.3–74.2% | 0.010 | −4.65 | 0.47 |
| (a) Point extrapolation 9/26 | 34.6% | 28.6–41.0% | 0.052 | −2.96 | 0.33 |
| (b) Weak reference Beta(0.5, 0.5) | 50.0% | 0–100% | 0.003 | −5.77 | 0.39 |
| (c) Any-RAS cohort 11/38 | 29.5% | 15.2–45.6% | 0.020 | −3.94 | 0.69 |

注：tau, shift between trials (logit scale); log score, natural logarithm of the predictive probability of the observed count (nats; larger is better); PIT, probability integral transform (midpoint version; 0.5 means the centre of the prediction). The 80% predictive interval is shown in Figure 3.

Phase 1 の ORR の事後分布（Jeffreys）は、平均 35.2%、95% 信用区間 18.7〜53.7% である。Phase 3 の実測は、Phase 1 を使ったすべてのモデルの 95% 予測区間と 80% 予測区間（図 3）に入り、PIT は 0.43〜0.47 で予測の中央付近だった。対数予測スコアは、(b) の弱い基準に対して、$\tau = 0$ で 1.80 nats、$\tau = 0.25$ で 1.66 nats、$\tau = 0.5$ で 1.39 nats、$\tau = 0.75$ で 1.12 nats 良かった。(a) の点推定は 2.82 nats 良く、最もスコアが高かった。(c) は 1.84 nats だった。

分母を 228 人（奏効 76 人）にしても、対数予測スコアは約 0.05 nats 低くなる（悪くなる）だけで、結論は変わらなかった。Beta(1,1) 事前分布では、対数予測スコアが $\tau = 0$ で −3.97、$\tau = 0.5$ で −4.38 となり、Jeffreys と同程度だった。

(a) の点推定のスコアが最も高かったのは、この 1 組の実測が 9/26 に近かったためである。実測が近いのは、試験間のずれ $\tau$ が小さいからか、1 組の偶然かは、1 組の観測からは区別できない。そこで、真の $\tau$ を仮定した繰り返しの模擬を 2 通り行った（どちらも仮定であり、実際の $\tau$ ではない。$\tau = 0$ の模擬は最初の結果を見た後に加えた）。各組で真の $p_1$ を Phase 1 の事後分布から抽出し、$n_1$ 人の Phase 1 と 217 人の Phase 3 を 3,000 組生成した。真の $\tau$ が 0.5 のとき、(a) の 95% 区間の被覆率は $n_1 = 26$ で 33.5%、$n_1 = 104$ で 41.1%（平均対数予測スコア −11.2、−9.2）、$\tau = 0.5$ を見込んだ予測は 94.7〜95.6%（−4.88、−4.67）、$\tau = 0$ を仮定した予測は 81.1% から 64.1% へ下がった。真の $\tau$ が 0 のとき、(a) は 48.1%（$n_1 = 26$）から 73.6%（$n_1 = 104$）にとどまり（−7.40、−4.43）、$\tau = 0$ を仮定した予測は 94.5〜95.4%（−4.45、−3.92）、$\tau = 0.5$ を見込んだ予測は 99.6〜100%（−4.60、−4.30）だった。どちらの真の $\tau$ でも、(a) は被覆率と平均スコアが最も低かった。この 1 組で (a) が最良だったことは、(a) が優れた予測であることを示さない。

### 生存期間の中央値

図 4 と表 3 は、生存期間の中央値の予測区間と実測である。

![PFS（左）と OS（右）の中央値について、試験間のずれ τ ごとの 95% 予測区間と、実測 Phase 3 の中央値の縦線。](shared/daraxonrasib-phase1-phase3-information/figures/fig4_survival_medians.png)

図 4. Phase 3 の中央値の予測区間（実測の観測誤差を含む 95% 予測区間、対数軸）。濃い青は信頼区間から復元した標準誤差（OS は下限のみ）、薄い青はその 2 倍。縦の破線は実測の中央値である。τ は対数中央値の尺度の試験間のずれ。

表 3. 生存期間の中央値の照合（`analysis/02_survival_medians.py`）。

| Endpoint | Phase 1 median (months) | Phase 3 observed (months) | tau | 95% predictive interval for the observed median | z | PIT |
|---|---|---|---|---|---|---|
| PFS | 8.5 (6.7–10.5) | 7.3 (6.3–8.1) | 0 | 6.6–11.0 | −1.16 | 0.12 |
| PFS | | | 0.5 | 3.1–23.4 | −0.29 | 0.38 |
| PFS, se × 2 | | | 0 | 5.1–14.2 | −0.58 | 0.28 |
| OS | 13.1 (10.9–NE) | 13.2 (10.0–NE) | 0 | 9.4–18.3 | 0.05 | 0.52 |
| OS, se × 2 | | | 0 | 6.7–25.5 | 0.02 | 0.51 |
| OS | | | 0.5 | 4.7–36.9 | 0.01 | 0.51 |

注：se, standard error of the log median recovered from the reported confidence interval; z, the observed log median minus the predicted log median, divided by the predictive standard deviation; PIT, normal cumulative probability of z. Phase 1 values in parentheses are the 95% confidence intervals reported in the 8-K.

PFS の実測の中央値 7.3 か月は、Phase 1 の 8.5 か月の 0.86 倍で、$\tau = 0$ の 95% 予測区間（6.6〜11.0 か月）の下側に近い位置（PIT 0.12）にあった。標準誤差を 2 倍にすると区間は 5.1〜14.2 か月に広がり、PIT は 0.28 だった。OS は 13.2 か月で、Phase 1 の 13.1 か月と 1.01 倍だった。OS の z は、標準誤差と $\tau$ のどの設定でも 0.01〜0.05 で、区間の幅の設定にかかわらず内側に入る。つまり OS の照合は、ほぼ自明な通過である。Phase 3 の追跡期間の中央値は 8.5 か月で、Phase 1 の 16.7 か月の約半分であり、Phase 3 の OS の中央値は曲線の後半の少数の事象に依存する可能性がある。上限が NE の信頼区間から標準誤差を復元する仮定にも不確かさがあり、OS の照合は弱い。

### 情報価値

図 5 は、Phase 1 のコホートの大きさと予測区間の幅、進む判断の確率である。表 4 は、実際の 9/26 に対する判定である。

![左は Phase 1 のコホートの大きさと Phase 3 の ORR の 95% 予測区間の幅（τ = 0 と 0.5）。右は閾値 20% と 25% で「進む」判断になる確率。](shared/daraxonrasib-phase1-phase3-information/figures/fig5_information_value.png)

図 5. Phase 1 のコホートの大きさと情報量。左（真の ORR 0.35）：Phase 3 の真の ORR の 95% 予測区間の幅の期待値。青は τ = 0、赤は τ = 0.5、点線は τ = 0.5 で $n_1\to\infty$ のときの幅（41.8 ポイント）。右：「$P(p>T)\ge0.8$ なら進む」とした場合に進む判断になる確率。色は真の ORR（灰 0.25、橙 0.30、青 0.35）、実線は閾値 $T=25\%$、破線は $T=20\%$。閾値は任意である。

左の真の ORR 0.35 は、観測の 9/26 に近い値を後から選んだものである。0.20〜0.40 の結果は配布した表（`info_value_widths.csv`、`info_value_proceed.csv`）にある。予測区間の幅は、$n_1 = 26$ から 104 へ増やすと、$\tau = 0$ では 34.4 から 18.0 ポイントへ縮んだが、$\tau = 0.5$ では 51.4 から 44.6 ポイントにしか縮まなかった。$\tau = 0.5$ で Phase 1 の真の ORR が既知（$n_1\to\infty$）でも、幅は 41.8 ポイント（16.6〜58.4%）で下げ止まる。$\tau$ が 0.25、0.75 のとき、この下限の幅は 21.9、58.8 ポイントだった。

進む判断の確率は、閾値 25% に対して真の ORR が 0.30 のとき、$n_1 = 26$ で 0.37、52 で 0.50、104 で 0.64、真の ORR が 0.35 のとき 0.59、0.78、0.93 だった。真の ORR が 0.25（閾値と同じ）のときは 0.18 から 0.21 でほとんど変わらなかった。この判定は、Phase 3 の $p_3$ ではなく Phase 1 の $p_1$ についての規則であり、$\tau$ は含まない。

表 4. 実際の Phase 1（9/26）に対する判定（規則：$P(p>T)\ge0.8$ なら進む）。

| Threshold T | P(p > T given 9/26) | Proceed at 0.8 |
|---|---|---|
| 15% | 0.994 | Yes |
| 20% | 0.962 | Yes |
| 25% | 0.870 | Yes |
| 30% | 0.703 | No |

### 機序モデルの入力と 2025 年末までの公開状況

機序モデル（腫瘍動態や機序の PK/PD）は当てはめていない。表 5 は、その主な入力が 2025 年末までの資料に記載されていたかを、読んだ範囲で整理したものである。

表 5. 機序モデルの入力と、2025 年末までの公開状況（読んだ範囲）。

| Quantity | Described in material public by 2025-12-31? | Source and status |
|---|---|---|
| Preclinical PK/PD in mice (tumour exposure, DUSP6 inhibition, stasis threshold 158 nM in mice, about 80 nM human-equivalent) | Yes (2024 paper) | Cancer Discovery 2024 ([8](#ref-8)); the numbers come via an earlier article ([9](#ref-9)); the paper was not re-read here |
| Human population PK parameters | Not in the 8-K | Reported in the FDA review (2026, after the cutoff) ([9](#ref-9)) |
| Exposure–response for efficacy in patients | Not in the 8-K | FDA review (after the cutoff): no significant efficacy relation among patients at 300 mg ([9](#ref-9)) |
| Longitudinal tumour size per patient | Not found; the 8-K has a best-percentage-change plot as an image only | 8-K figure; not read |
| Tumour growth and resistance rates | Not found in the material read | Would need longitudinal lesion data |
| Target engagement in patients | Not found in the 8-K | Other public material was not searched |

注：PK/PD, pharmacokinetics and pharmacodynamics; DUSP6, a downstream marker gene of RAS/MAPK signalling.

## 考察

Phase 1 の 26 人から Phase 3 の ORR を予測すると、実測は予測区間の中央付近に入った。ただし、これを予測の成功と呼ぶには条件がある。実測が Phase 1 の点推定（34.6%）に近く、PIT が 0.43〜0.47 だったことは、1 組の観測に基づく事実である。試験間のずれ $\tau$ が小さいのか大きいのかは、この 1 組から区別できない。点推定の外挿が 1 組で最もスコアが高かったことは、その近さが偶然か小さな $\tau$ によるかを分けない。繰り返しの模擬では、真の $\tau$ が 0 でも 0.5 でも点推定の被覆率が最も低く、$n_1 = 26$ では Phase 1 の標本誤差も無視できない。ただし模擬は $\tau$ を仮定した場合の結果である。

Phase 1 の ORR の 95% 予測区間（17.5〜54.8%）に実測が入ることは、区間が約 37 ポイントの幅を持つため、ほぼ当然である。「絞れた」という語は、幅の広さと合わせて読む必要がある。実測が 80% 予測区間にも入ったことも、同じ理由で強い確認にならない。RAS 変異全体の 11/38 を使った基準 (c) の対数予測スコアは $\tau = 0$ の G12X（−3.94 対 −3.98）とほぼ同じで、G12X に絞ることの情報価値は、この 1 組からは読み取れない。

コホートを増やす価値は、予測区間の幅と判定で異なる。$\tau = 0.5$ の下では、Phase 1 を 4 倍にしても Phase 3 の ORR の予測区間はほとんど縮まない。幅を決めるのは Phase 1 の例数ではなく、試験間のずれである。一方で、真の ORR が閾値の近く（0.30 に対して閾値 25%）にあるとき、進む判断の確率は 0.37 から 0.64 に上がった。この値は、閾値、規則、真の ORR の置き方（観測に近い 0.30〜0.35 を中心に示した）に依存し、真の ORR が閾値と同じ 0.25 のときはほとんど変わらなかった（0.18 から 0.21）。この枠内の結果であり、Phase 1 に例数を足す一般的な価値を示すものではない。

実際の判断には、さらに別の問いがある。Phase 1 が示すべきだったのは、化学療法より ORR が高いかであり、後から知った Phase 3 の対照群の ORR は 11.8% だったが ([3](#ref-3))、2025 年の時点でこの数値は使えなかった。対照群との差は本稿でモデル化していない。本稿の閾値 15〜25% は、後ろ向きの場合分けである。

機序モデルについては、2025 年末までの資料から、患者の腫瘍動態や曝露・反応を推定する入力を、読んだ範囲では見つけられなかった（表 5）。2026 年の FDA 審査資料に載った母集団 PK の係数と、有効性の曝露・反応が有意でなかったという記述 ([9](#ref-9)) は、後から使える情報である。これは読んだ資料の範囲についての記述であり、機序モデル一般の価値を否定するものではない。

## 限界

- 結果を知った後の照合であり、盲検の予測ではない。モデルと基準を実行前に固定したことを示す記録はなく、基準 (b)(c)、感度解析、繰り返しの模擬は最初の結果を見た後に加えた。訓練の区切り（2025 年末）と、Phase 1 論文を事後の資料としたことも、後ろ向きの選択である。
- Phase 1 の ORR は確認済みまたは確認の可能性が残る奏効を数え、Phase 3 の奏効の定義と評価者は読んだ資料に書かれていない。Phase 3 が確認済みの奏効だけを数えるなら、Phase 1 の ORR のほうが包括的であり、Phase 1 の値が高く出る向きの差になる。この差は調整していない。また 2L efficacy evaluable は事後的に絞られた部分集団である可能性があり、その場合も ORR は高く出うる。
- Phase 1 の結果を見て Phase 3 へ進む判断をしたため、選ばれた良好な結果は、次の試験で平均へ戻る（勝者の呪い）可能性がある。$\delta$ の平均を 0 とした本稿のモデルはこれを含まず、負の方向へのずれも十分にありうる。
- Phase 1 は単群の拡大コホート（2L efficacy evaluable の定義が不明）で ([1](#ref-1))、Phase 3 は 1 回の前治療後のランダム化試験で ([5](#ref-5))、追跡期間（16.7 か月対 8.5 か月）、奏効の定義、評価可能集団が違う。
- Phase 3 の G12 集団の数値は二次情報による ([3](#ref-3))。NEJM の本文は取得できなかった。奏効の人数 72 は報道の割合と評価可能人数 217 からの逆算で、報告された人数ではなく、217 も報道 1 本に依存する。76/228 は丸めが合わない近似である。
- 試験間のずれ $\tau$ は、これらのデータから推定できず、場合分けとして置いた。結論の幅は $\tau$ に依存する。$\tau = 0.5$ は例示であり、現実の値を示すものではない。生存期間の $\tau$ は ORR とは別の尺度である。
- 生存期間は集計値から標準誤差を復元した近似で、信頼区間が対数尺度で対称という仮定と、OS の上限が NE であることに依存する。事象数ベースでは標準誤差はさらに大きいとみられ、2 倍の感度解析を併記した。Phase 3 の OS の中央値は未成熟な追跡に基づく。
- 進む判断の模擬の閾値と 0.8 は任意である。繰り返しの模擬の真の $p_1$ は Phase 1 の事後分布からの抽出で、現実の分布ではない。模擬の乱数誤差（各条件 4,000 回、繰り返しは 3,000 組）は定量していない。
- 機序モデルは当てはめていない。表 5 は、読んだ資料の範囲での公開状況であり、他の公開資料は探していない。

## 結論

QOI（Phase 1 の二次治療 26 人のデータで、Phase 3 の RAS G12 集団の奏効率と生存期間をどこまで絞れたか）に対し、公開データの範囲で言えるのは次のとおりである。ORR は、試験間のずれの仮定に応じて 95% 予測区間が 17.5〜54.8%（$\tau = 0$）から 12.0〜65.9%（$\tau = 0.5$）で、実測の 33.2% は区間内にあった。区間の幅が広いため、これは強い確認ではない。PFS と OS の中央値の実測も予測区間の内側だったが、標準誤差を 2 倍にした感度解析と Phase 3 の短い追跡を踏まえると、OS の照合はほぼ自明な通過である。Phase 1 を 26 人から 104 人に増やしても、$\tau = 0.5$ の予測区間はほとんど縮まなかった。結果を知った後の照合であり、これを予測能力の証明とは解釈しない。

## データとコードの公開状況

再実行用の資料（`analysis/` のスクリプト、`inputs/` の入力 CSV と出典の記録、`outputs/` の表・図・ログ）は[配布アーカイブ](shared/daraxonrasib-phase1-phase3-information/daraxonrasib-phase1-phase3-information-companion.zip)に含めた。入力は、8-K ([1](#ref-1)) と報道 ([3](#ref-3)) から転記した数値である。再実行：`python analysis/01_orr_prediction.py && python analysis/02_survival_medians.py && python analysis/03_information_value.py && python analysis/04_figures.py`（Windows 11、Python 3.12.4、numpy 2.2.6、pandas 2.2.2、scipy 1.14.0、matplotlib 3.9.1）。乱数のシードは 20261110 で、奏効率の予測分布は乱数を使わない。`03_information_value.py` の実行には数分かかる。

## 参照

<span id="ref-1"></span>1. Revolution Medicines, Inc. Form 8-K: current report, daraxonrasib clinical data in pancreatic cancer [Internet]. U.S. Securities and Exchange Commission; 2025 Sep 10 [cited 2026 Nov 10]. Available from: [https://www.sec.gov/Archives/edgar/data/1628171/000119312525200078/d947102d8k.htm](https://www.sec.gov/Archives/edgar/data/1628171/000119312525200078/d947102d8k.htm). Read as text; the waterfall and survival figures are images and were not read.

<span id="ref-2"></span>2. O'Reilly EM, Wainberg ZA, Hendifar AE, Borad MJ, Pietrantonio F, Pant S, et al. Daraxonrasib or chemotherapy in previously treated metastatic pancreatic cancer. N Engl J Med. 2026;395(4):325–337. [doi:10.1056/NEJMoa2605555](https://doi.org/10.1056/NEJMoa2605555). Abstract level only; the full text was not available.

<span id="ref-3"></span>3. OncLive. Daraxonrasib meets all primary and key secondary efficacy end points in pretreated PDAC [Internet]. 2026 May 31 [cited 2026 Nov 10]. Secondary report of the ASCO 2026 presentation. Available from: [https://www.onclive.com/view/daraxonrasib-meets-all-primary-key-secondary-efficacy-end-points-in-pretreated-pdac](https://www.onclive.com/view/daraxonrasib-meets-all-primary-key-secondary-efficacy-end-points-in-pretreated-pdac)

<span id="ref-4"></span>4. Wolpin BM, Park W, Garrido-Laguna I, Spira A, Starodub A, Sommerhalder D, et al. Daraxonrasib in previously treated advanced RAS-mutated pancreatic cancer. N Engl J Med. 2026;394(18):1790–1802. [doi:10.1056/NEJMoa2505783](https://doi.org/10.1056/NEJMoa2505783). Abstract level only.

<span id="ref-5"></span>5. U.S. Food and Drug Administration. FDA approves daraxonrasib for metastatic pancreatic adenocarcinoma [Internet]. FDA; 2026 [cited 2026 Nov 10]. States the approval date (2026 Aug 26) and the RASolute 302 population (progression after one prior line); overall-population results only. Available from: [https://www.fda.gov/drugs/cancer-approvals/fda-approves-daraxonrasib-metastatic-pancreatic-adenocarcinoma](https://www.fda.gov/drugs/cancer-approvals/fda-approves-daraxonrasib-metastatic-pancreatic-adenocarcinoma)

<span id="ref-6"></span>6. Gneiting T, Raftery AE. Strictly proper scoring rules, prediction, and estimation. J Am Stat Assoc. 2007;102(477):359–378. [doi:10.1198/016214506000001437](https://doi.org/10.1198/016214506000001437)

<span id="ref-7"></span>7. Czado C, Gneiting T, Held L. Predictive model assessment for count data. Biometrics. 2009;65(4):1254–1261. [doi:10.1111/j.1541-0420.2009.01191.x](https://doi.org/10.1111/j.1541-0420.2009.01191.x)

<span id="ref-8"></span>8. Jiang J, Jiang L, Maldonato BJ, Wang Y, Holderfield M, Aronchik I, et al. Translational and therapeutic evaluation of RAS-GTP inhibition by RMC-6236 in RAS-driven cancers. Cancer Discov. 2024;14(6):994–1017. [doi:10.1158/2159-8290.CD-24-0027](https://doi.org/10.1158/2159-8290.CD-24-0027). Not re-read for this article.

<span id="ref-9"></span>9. Kumakura D. Recomputing daraxonrasib 300 mg target-inhibition predictions from FDA-published values [Internet]. Daiki Kumakura; 2026 Nov 22. Available from: [daraxonrasib-target.html](daraxonrasib-target.html). It summarizes the FDA multi-discipline review of NDA 220910 (2026), which is after the training cutoff.
