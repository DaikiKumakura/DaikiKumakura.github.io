文献・公開資料の確認日：2026年10月6日。文献の報告、本記事の解釈、本記事で作成した合成データの計算例を区別して書く。

あるモデルが、未知データを非常によく予測したとする。では、そのモデルが内部で表現している関係を、病態機序や薬理機序として解釈してよいだろうか。

逆に、ODEや反応ネットワークから作った「機序的な」モデルであれば、そのパラメータや構造を生物学的機序として信じてよいだろうか。

私の答えは、**どちらも、そのままではNo**である。予測と機序推論は重なる部分を持つが、同じ最適化問題ではない。前者には予測の試験が、後者には機序の試験が要る。両方を主張するモデルには、両方の試験を求めたい。

## 1. まず、何を最適化したいのかを分ける

予測の目的を単純化すると、未知データでの期待損失を小さくする関数を選ぶことである。

\[
f^{*}=\arg\min_{f}\ \mathbb{E}\left[L\bigl(Y,f(X)\bigr)\right]
\]

一方、機序について知りたいときの問いは、例えば次のようなものである。

- このタンパク質を阻害すると、下流のシグナルは変わるか。
- 曝露量を変えたときの薬効の変化は、受容体占有を介しているか。
- バイオマーカーと予後の関連は、介入可能な経路を表しているか。

これらは一種類の問いではない。本記事では、少なくとも三つの層を区別する。

1. **観察のもとでの予測**：同じ条件で得られる次のデータを当てる。対象は \(P(Y\mid X)\) である。
2. **介入のもとでの予測**：\(A\) を変えたら \(Y\) がどうなるかを当てる。対象は \(\mathbb{E}[Y\mid do(A=a)]\) や、二つの値 \(a_1,a_0\) の間でのその差である。
3. **機序の主張**：その効果が、どの経路・どの媒介変数を通って生じるかを述べる。二つ目の問い（受容体占有を介しているか）は、全体の介入効果ではなく媒介の問いである。

観察データで \(Y\) をよく当てられることは、二層目・三層目の問いに答えられることを意味しない。逆に、介入の結果をよく当てられること（二層目）も、それだけでは経路の主張（三層目）を支えない。

Hernánらは、データサイエンスの課題を記述・予測・反事実的予測（因果推論を含む）に分けた。[1] 臨床予測モデルの文脈でも、van Gelovenらは、治療を受けないと仮定したリスクを予測したいのか、現在の診療のもとでのリスクを予測したいのかで、推定対象とデータの扱いが変わると論じている。[2] 反事実的予測は因果推論のためだけのものではない、という指摘もある。[3] 本記事の出発点も同じで、**最初に推定対象を書く**ことである。

なお、本記事では「識別」という語を二つの意味で使う。因果推論の識別（介入効果が観察データの分布から一意に決まるか）と、パラメータの識別性（モデルのパラメータがデータから一意に決まるか）である。前者は第4節、後者は第5・6節の話題で、混同しないよう節ごとに明記する。

## 2. 「モデルの同定と回帰関数の推定」のtrade-offは、何を言っているのか

この問題を考えるきっかけとして面白いのが、Yuhong Yangの2005年の論文である。[4]

Yangは回帰のモデル選択について、BIC型の性質（候補に真の有限次元モデルが含まれるとき、それを選ぶ確率が1に近づく一致性）と、AIC型の性質（回帰関数の推定でminimax rateを達成すること）を、一つの選択基準で同時に得られるかを調べた。結論は否定的だった。**一致性を持つモデル選択基準は、回帰関数の推定で、最悪の場合（minimaxの意味で）最適な収束率を達成できない。** 同じ論文は、Bayesian model averagingもこの意味でminimax-rate optimalにはなれないと示している。

ここで注意したい。Yangの定理は「予測モデルでは因果推論ができない」という一般定理ではない。対象は特定の回帰モデル選択の設定であり、示されたのは「モデルの同定」と「回帰関数の推定」の間の数学的なtrade-offである。介入効果の識別についての定理でもないし、個々のデータセットで必ず損をするという主張でもない。

それでも、この結果は重要な警告になる。**一つの「最良モデル」という概念が、異なる科学的目的に対して自動的に最良になるとは限らない。** 何を「正しい」とするかが変わると、最適な選び方自体が変わりうる。

Galit Shmueliも2010年に、説明（explanation）と予測（prediction）を区別する必要を体系的に論じた。[5] 説明モデルでは変数と構造の意味が重要になり、予測モデルでは未知データへの汎化性能そのものが評価対象になる。この二つを区別しないと、次の二方向の飛躍が起こる。

- 「よく予測できたので、この変数が原因だ」
- 「この機序モデルはもっともらしいので、未知の患者もよく予測できるはずだ」

## 3. 最近のVirtual Cell研究は、この問題を評価の側から見せている

single-cell perturbation predictionは、この違いを見るよい例である。詳細は[Virtual Cellの評価指標を点検した別記事](virtual-cell-target-evaluation.html)に書いたので、ここでは本記事の論点に必要な部分だけをまとめる。

先に一点、整理しておく。Perturb-seqのような摂動データは、もともと遺伝子への介入の結果を測ったデータである。したがってここでの課題は、第1節の一層目と二層目の違い（観察か介入か）ではない。**未知の摂動や未知の細胞背景へ汎化できるか**と、**介入の結果を当てられたとしても、その背後の経路やネットワークを回復したと言えるか**（二層目と三層目の違い）の二つである。

2025年、Ahlmann-Eltzeらは、五つのfoundation modelと二つの深層学習モデルを、意図的に単純なbaselineと比較した。単一・二重の遺伝子摂動後の転写変化の予測で、いずれもbaselineを上回らなかった。[6] これは「深層学習は生物学に使えない」という結果ではない。重要なのは、**モデルの複雑さや表現力そのものは、対象とする予測課題での価値を証明しない**という点である。

Systemaは、摂動細胞と対照細胞の間に、摂動の種類を問わず共通して現れる系統的な差（systematic variation）があり、一般的な指標ではそれを当てるだけで性能が高く見えることを、10データセットで示した。[7] 高い予測スコアは、摂動固有の応答を捉えた証拠とは限らない。

ところが2026年10月1日、Millerらは反対方向の重要な指摘を加えた。[8] 陽性対照となる予測と、情報を持たないbaselineを用いて、14データセット・18指標を点検すると、MSEや対照との差に基づくPearson相関など一部の一般的な指標は、本当に情報を持つ予測を検出する感度が低かった。感度の良い指標（論文ではwell-calibrated metricsと呼ぶ）では、深層学習モデルが情報を持たないbaselineを上回る場合が確認された。ここでのcalibrationは予測確率の校正ではなく、**指標が良い予測と情報のない予測を区別できるか**の点検である。

2025–2026年の文献を並べると、話は単純ではない。

- 複雑なモデルだから良いとは限らない。単純なbaselineに負けるモデルも多い。
- しかし、評価指標そのものの感度が低ければ、実在する予測情報も見えなくなる。
- そして、介入の結果を予測できることと、正しい機序を回復したことは、さらに別の問題である。

モデル評価は「モデルだけ」の評価ではない。**データ分割、baseline、損失、指標まで含めた一つの実験**である。2026年のVirtual Cell Challengeが、摂動データのない細胞背景への予測（zero-shot）と、六つの指標の集約で順位を決める形を採ったのも、この問題意識と整合する。[9] 確認日時点で最終結果は未発表であり、本記事は結果を予想しない。

## 4. 予測できても、介入の答えは一意には決まらない

この節の「識別」は、因果推論の意味である。簡単な例を考える。

\[
U\rightarrow X,\quad U\rightarrow Y,\quad X\rightarrow M\rightarrow Y,\quad X\rightarrow Z
\]

\(U\) は測っていない共通の原因（交絡）、\(M\) は媒介変数、\(Z\) は \(X\) の下流にあるが \(Y\) には影響しない代理変数である。観察データの範囲で \(X\) と \(M\) が非常に強く連動しているとする。

予測問題としては、\(Y=f(X)\) でも \(Y=g(Z)\) でも、高い精度で当たるかもしれない。しかし介入の問いでは、答えがそれぞれ違う。

- \(Z\) を操作しても \(Y\) は変わらない。\(g(Z)\) の予測精度は、\(Z\) の効果を何も保証しない。
- \(X\) を操作した効果は、\(U\) を経由する見かけの関連を含む \(P(Y\mid X)\) とは一致しない。\(P(Y\mid do(X))\) を得るには、\(U\) の調整、介入データ、外部の構造知識などの追加条件が必要になる。
- 薬で \(M\) だけを阻害したらどうなるか、という問いには、このデータは答えられない。観察の範囲で \(X\) と独立に \(M\) が動いた例がほとんどなく、答えは実質的な外挿になるからである（正値性がほぼ欠けている）。

なお、交絡がなく、\(X\) を変えても他の関係が変わらない単純な \(X\rightarrow M\rightarrow Y\) であれば、\(P(Y\mid do(X))=P(Y\mid X)\) となり、予測と介入の答えは一致する。両者がずれるのは、例えば交絡、選択バイアス、代理変数、データにない変動への外挿が入るときである。現実のデータでは、それがないことを示す方が難しい。

だから、SHAP値が大きい、attention weightが大きい、feature importanceが高い、という理由だけで機序を決めることはできない。これらはまず、**予測器の内部で、その入力がどれだけ使われたか**を表す量である。介入効果そのものではない。SHAPの公式ドキュメント自体も、予測モデルの解釈から因果的な示唆を引き出すことへの注意を独立した章で説明している。[10]

## 5. では、mechanistic modelなら安全なのか

ここには反対方向の落とし穴がある。この節と次節の「識別性」は、パラメータの意味である。

例えば、薬物が応答 \(R\)（標的量やバイオマーカー）の消失を速めるturnoverモデルを書いたとする。

\[
\frac{dR}{dt}=k_{\mathrm{in}}-k_{\mathrm{out}}R-k_{\mathrm{drug}}C(t)R,
\qquad R(0)=R_0=\frac{k_{\mathrm{in}}}{k_{\mathrm{out}}}
\]

これはJuskoらの間接反応モデル（indirect response model）のうち、消失を促進する型に線形の薬効を入れたものである。\(S=k_{\mathrm{drug}}/k_{\mathrm{out}}\) と置くと \(\dfrac{dR}{dt}=k_{\mathrm{in}}-k_{\mathrm{out}}\bigl(1+S\,C(t)\bigr)R\) と書け、\(S\) はこの型の慣用の傾きパラメータにあたる。[11, 12] この式には、標的の産生と消失（turnover）、薬物曝露、薬物による消失の促進という機序的な解釈がある。

しかし、データから観測できるのが \(R(t)\) だけなら、\(k_{\mathrm{in}}\)、\(k_{\mathrm{out}}\)、\(k_{\mathrm{drug}}\) をそれぞれ十分に識別できるとは限らない。識別性の問題は、少なくとも二種類に分けて考える必要がある。

**構造的識別性**は、無限に正確なデータがあってもパラメータが一意に決まるかという問題である。例えば濃度 \(C(t)\) を測らず投与量だけが分かっている場合、1-コンパートメントのPKでは \(C(t)=\mathrm{Dose}/V\cdot e^{-k_e t}\) なので、\(R(t)\) には \(k_{\mathrm{drug}}/V\) という比としてしか現れない。分布容積 \(V\) と薬効の強さ \(k_{\mathrm{drug}}\) は、\(R(t)\) だけからは原理的に分けられない。

**実用的識別性**は、実際の測定時点・個数・誤差のもとで、パラメータが十分に狭く決まるかという問題である。構造的には識別可能でも、測定の設計によっては、異なるパラメータの組合せがほとんど同じ \(R(t)\) を作る。系統生物学のモデルでは、多くのパラメータの組合せに対してモデル出力が鈍感な「sloppy」な構造が広く見られることが報告されている。[13] プロファイル尤度は、構造的・実用的な非識別性の両方を検出する実用的な方法であり、[14] 同じ考え方で、パラメータではなく予測値そのものの信頼区間も求められる。[15]

さらに、モデル構造そのものが間違っている可能性もある。よく当てはまるODEを書けたことは、「自然がこのODEで動いている」ことの証明ではない。機序モデルにも、少なくとも次の確認が必要である。

1. 構造的識別性
2. 実用的識別性
3. モデルの誤指定（misspecification）
4. 外部データや介入実験による検証

黒箱だけが危険なのではない。

## 6. 計算例：同じデータに当てはまるパラメータは、問いによって違う答えを出す

非識別性が実際に何を意味するかを、合成データで確かめた。上のturnoverモデルで、真の値を \(k_{\mathrm{out}}=2\)/日、\(S=0.075\) L/mg（\(k_{\mathrm{drug}}=0.15\) L/mg/日）とし、100 mgを1回静注した（1-コンパートメント、\(V=5\) L、\(k_e=0.1\)/日で半減期約6.9日、\(R_0=100\)）。投与後1, 2, 4, 7, 14, 21, 28日に \(R\) を測り、対数スケールで標準偏差0.10の測定誤差を加えた（乱数シード20261024）。\(R_0\)、\(C(t)\)、誤差の標準偏差は既知とし、\(k_{\mathrm{out}}\) と \(S\) の尤度を計算した。

\(C(t)\) が既知なので、このモデルは構造的には識別可能である。以下で見るのは、**初回の採血を投与1日後に置いた測定設計による、実用的な非識別性**である。

区間は、\((k_{\mathrm{out}},S)\) の2次元格子（\(k_{\mathrm{out}}\) は0.1〜1000/日の対数等間隔81点、\(S\) は0.03〜0.15の121点）で尤度を計算し、\(2\Delta\mathrm{NLL}\le3.84\) を満たす格子点（1,619点）での最小値・最大値として求めた。これは各量のプロファイル尤度に基づく95%区間の、格子による近似である。

![データと矛盾しないパラメータの組が、未観測の投与レジメンでは k_out の違いだけではほぼ同じ予測を、未観測の初期24時間では大きく異なる予測を出す。](shared/prediction-vs-mechanism/figures/identifiability.png)

**図1.** 合成データによる計算例（実データではない）。(a) 観測データと、95%尤度集合に入る3組のパラメータによる当てはめ（3組は \(k_{\mathrm{out}}\) だけでなく \(S\) も少しずつ異なる）。灰色の破線はturnoverを含まない直接効果モデル \(R=R_0/(1+S\,C)\)。(b) \(k_{\mathrm{out}}\) のプロファイル尤度。青は観測設計、紫は投与3・6時間後の採血を加えた設計。破線は自由度1のカイ二乗分布の95%点（3.84）。(c) 観測していない25 mg週1回・12回投与の予測。(d) 100 mg投与後24時間の予測。縦線は6時間。

結果は次のとおりである（出力：`results/summary.json`、`results/likelihood_set.csv`、`results/kout_profile.csv`）。

| 量 | 95%区間（格子近似） | うち \(S=0.073\) に固定し \(k_{\mathrm{out}}\) だけを動かした幅 |
| --- | --- | --- |
| \(k_{\mathrm{out}}\)（/日） | 約0.77以上。上限は決まらない | — |
| \(S\)（L/mg） | 0.059〜0.086（真値0.075） | — |
| 25 mg週1回、84日目の \(R\) | 69.2〜77.1 | 71.7〜73.5 |
| 25 mg週1回、期間中の最小の \(R\) | 54.0〜65.2 | 58.0〜61.9 |
| 100 mg投与6時間後の \(R\) | 37.3〜77.3 | 41.2〜77.3 |

読み取れることを四つに分けて書く。

**第一に、\(k_{\mathrm{out}}\) は下限しか決まらない。** 尤度は \(k_{\mathrm{out}}\) を大きくするほどわずかに良くなり、有限の最尤推定値は存在しなかった（格子の上端1000/日で最小）。ノイズを加えない真の値のデータでも、\(k_{\mathrm{out}}=1000\) での \(2\Delta\mathrm{NLL}\) は0.017にとどまった。上限が決まらないのはこの乱数の偶然ではなく、測定設計の性質である。

**第二に、このデータはturnoverがある機序とない機序を区別できない。**支持も否定もしていない。turnoverを含まない直接効果モデル \(R=R_0/(1+S\,C)\) の最良の負の対数尤度（0.72033）は、turnoverモデルの最良値（0.72034）と同じだった。直接効果モデルは \(k_{\mathrm{out}}\to\infty\) の極限にあたる。濃度の変化が標的のturnoverより十分に遅いと、\(R\) はほぼ準定常状態 \(R\approx R_0/(1+S\,C)\) に従い、データには主に \(S\) だけが現れるためである。間接反応モデルでこうした時間スケールの分離が起こりうることは、古くから知られている。[11, 12]

**第三に、非識別性が問題になるかどうかは、問いによって変わる。** 観測していない25 mg週1回投与（図1c）の予測幅は、主に \(S\) の不確実性から来ていた。\(S\) を固定して \(k_{\mathrm{out}}\) だけを尤度集合内の範囲（約0.8〜1000/日）で動かしても、84日目の \(R\) は約2、最小値は約4しか変わらなかった。一方、測定していない投与直後の数時間（図1d）では、\(k_{\mathrm{out}}\) だけで6時間後の \(R\) が約41から約77まで変わった。前者で答えがそろうのは、週1回投与でも、各投与直後の数時間を除けば濃度の変化がturnoverより遅く、準定常近似が成り立つ範囲にとどまるからである。最小値に残る約4の差は、この投与直後の過渡応答から来ている。半減期の短い薬剤や、濃度が数時間で大きく変わる投与では、この条件は崩れる。

**第四に、この非識別性は測定設計で解消できる。** 推定できた下限 \(k_{\mathrm{out}}\approx0.77\)/日からは、応答の時間スケールは長くても1日程度と見込める。薬物がないときの標的の半減期（\(\ln 2/k_{\mathrm{out}}\)）は真の値で約8時間、投与直後は消失が速まって約3時間になる。この時間帯に当たる投与3時間後と6時間後の2点を加えると、\(k_{\mathrm{out}}\) の95%区間は約1.5〜4.1/日に収まった（図1bの紫。一つの乱数系列での結果である）。どの問いに答えたいかが決まれば、どの時点を測るべきかも決まる。

逆に言えば、「\(k_{\mathrm{out}}\) が推定できなかったので、このモデルは役に立たない」とも言えない。曝露の変化が遅い投与レジメンの比較という問いには、\(S\) の精度の範囲で答えられる。必要なのは、**問いが依存するパラメータの組合せを、データが決めているか**を確認することである。

ただし、この計算例はモデルの構造が正しく、投与レジメンを変えてもその構造とパラメータが変わらないと仮定している。これは第4節の因果推論における識別の仮定に相当し、計算例では正しいと決めてある。実際には、この仮定自体を介入データで検証する必要がある。また、この例が示すのは一つの仕組みであり、実在の薬剤や標的について何かを示すものではない。

## 7. PK/PDやMIDDでは、この区別は実務的である

例えば、次の測定時点の腫瘍径を当てたいなら、予測性能が第一になる。単純なlast-observationのモデルが複雑なtumor-growthモデルよりよく当たるなら、その目的には前者を使えばよい。

一方、「投与間隔を延ばしても薬効が維持されるのはなぜか」を知りたいなら状況が変わる。AUC、\(C_{\max}\)、\(C_{\min}\)、標的のturnover、受容体占有のどれが反応を支配しているかを区別できなければ、観察されていないレジメンへの外挿は危うい。既存の用量範囲の中で当てることと、

\[
\text{未観測の用量}\rightarrow\text{未観測の曝露プロファイル}\rightarrow\text{反応}
\]

を外挿することでは、必要な仮定が違う。第6節の計算例でも、曝露の変化がturnoverより遅い時間帯では予測がそろい、投与直後の時間帯では割れた。機序モデルの価値が大きくなるのは、単にfitが良いからではない。**介入を変えたときに、何を保存し、何を変えるべきかを明示できるから**である。

規制の枠組みも、モデルの種類ではなく、問いと判断への影響から評価を組み立てている。ICH M15（MIDDの一般原則）は2026年1月29日にStep 4で採択された。question of interest（何を判断したいか）とcontext of use（モデルがその判断でどんな役割と範囲を担うか）を定め、モデルが判断に与える影響の大きさと、誤った判断の帰結からモデルリスクを評価して、必要な検証の程度を決める枠組みである。対象となる手法の例として、PopPK、PBPK、曝露反応、QSP、疾患進行モデルに加え、AI/MLも挙げられている。[16] FDAは2026年6月3日に、これを最終ガイダンスとして発出した。[17]

AIについては、FDAが2025年1月に、context of useごとに信頼性を評価する7段階のリスクベースの枠組みをドラフトガイダンスとして示した（確認日時点でドラフト）。[18] 2026年1月には、FDAとEMAが創薬・開発の全段階を対象とする10の原則を共同で公表している。[19] FDA–EMAの原則は初期研究も含む高水準の原則で、具体的な評価手順は定めていない。一方、FDAのドラフトガイダンスは創薬段階での利用を対象外としている。その信頼性評価の枠組みをVirtual Cellのような研究用途に当てはめるのは、本記事の類推である。

この枠組みの言葉で言えば、本記事の主張は次のようになる。**同じモデルでも、question of interestと、モデルがその判断で担う役割が違えば、必要な証拠は変わる。** 観察条件での予測に使うモデルと、未観測の介入や機序の主張に使うモデルでは、モデルリスクも、求められる検証の種類も違う。

## 8. 予測と機序推論を両方したいならどうするか

私は、一つの総合スコアでモデルを選ばない方がよいと考える。少なくとも二つの軸に分けたい。

**予測性能**は、意図した利用場面と対象集団でのデータで評価する。臨床予測であれば、一つの損失だけでなく、判別能、校正、意思決定上の有用性を分けて見る。時間外検証、施設外検証、別の細胞型、未知の摂動などの検証は、実際の利用場面がそれを要求するときに価値が高い。単純なbaselineとの比較と、指標の感度の確認も含める。

**機序の妥当性**は、別に次を見る。

| 確認すること | 例 |
| --- | --- |
| パラメータは識別可能か | 構造的識別性の解析、プロファイル尤度、感度解析、識別できるように採血・測定を設計する |
| 介入実験の方向と大きさを当てるか | 阻害・ノックダウン・用量変更の結果を事前に予測して照合する |
| 別条件へパラメータを固定して移せるか | 別の用量群、別の集団、別の細胞背景で再推定せずに予測する |
| 予測された媒介変数を直接測ると合うか | 作用部位の曝露、標的への結合（target engagement）、標的のturnover、下流マーカーを実測する |
| 競合する機序を区別できるか | 二つの機序で予測が分かれる条件（第6節なら投与直後の数時間）を設計して測定する |

概念的には、

\[
\text{モデルの品質}\neq\text{一つのスカラー値}
\]

であり、(予測性能, 機序の証拠) という二軸で見た方がよい。Pareto frontierとして考えてもよい。予測をほとんど改善せず、解釈だけを大きく不安定にする複雑化なら採用しない。逆に、予測精度が少し低くても、重要な介入への外挿が独立した実験で確認されているなら、その機序モデルには別の価値がある。

## 9. 結論

「最もよく当たるモデルは、最も正しく理解しているモデルか」。この問いには、一般にはYesと答えられない。

Yangの結果は限定された統計問題についての定理だが、モデルの同定と回帰関数の推定を一つの目的として扱えない場合が、数学的に存在することを示している。single-cell perturbation predictionの最近の議論は、モデル、baseline、評価指標の選び方によって「何が予測できたか」という結論そのものが変わることを示している。一方、mechanistic modelも、その名前だけでは機序を保証しない。本記事の計算例では、turnoverを含むモデルと含まないモデルがデータに同じように当てはまり、データと矛盾しない（95%尤度集合に入る）パラメータが、ある問いには近い答えを、別の問いには大きく異なる答えを出した。

重要なのは、モデルの種類より先に、次の三つを決めることである。

- 何を予測したいのか。
- 何を原因として知りたいのか。介入の結果か、その経路か。
- その二つを、どのデータが識別できるのか。

予測モデルには予測の試験をする。機序モデルには機序の試験をする。両方を主張するモデルには、両方の試験を求める。この区別が、AI創薬、Virtual Cell、PK/PD、QSPのモデルを評価するときの、最も単純で有用な出発点だと私は考えている。

## 計算例の再実行と限界

[再実行資料ZIP](shared/prediction-vs-mechanism/prediction-vs-mechanism.zip)を展開し、Python 3.11以上で、展開先のフォルダから以下を実行する。確認したNumPy・SciPy・Matplotlibの版は`requirements.txt`に固定した。実行時間は環境によって約2〜4分である。

```sh
python -m pip install -r requirements.txt
python identifiability_demo.py
```

[計算コード](shared/prediction-vs-mechanism/identifiability_demo.py)は、`results/likelihood_set.csv`、`results/kout_profile.csv`、`results/summary.json`、図1を生成する。ODEは \(R\) について線形なので、0.002日刻みで、各区間の消失速度を中点の値に固定し、その区間を解析的に解く方法（指数積分）で順に計算した。[照合用コード](shared/prediction-vs-mechanism/check_integrator.py)で独立なODEソルバー（Radau、許容誤差 \(10^{-10}\)）と25 mg週1回投与で比較した差は、\(k_{\mathrm{out}}=2\)/日で \(10^{-5}\) 未満、格子上端の \(k_{\mathrm{out}}=1000\)/日で約0.001（\(R\) の単位）だった。

限界を書いておく。測定誤差の標準偏差、\(R_0\)、濃度推移は既知とした。個体間変動、PKパラメータの不確実性、モデルの誤指定は含めていない。区間は格子による近似で、端点は格子の解像度（\(S\) は0.001刻み）に依存する。\(k_{\mathrm{out}}\) の下限は格子点の間を対数スケールで線形補間した値である。カイ二乗近似による95%の閾値は、パラメータが境界へ流れる場合には近似にとどまる。

## 参考文献

1. Hernán MA, Hsu J, Healy B. A second chance to get causal inference right: a classification of data science tasks. *CHANCE*. 2019;32(1):42–49. [10.1080/09332480.2019.1579578](https://doi.org/10.1080/09332480.2019.1579578).
2. van Geloven N, Swanson SA, Ramspek CL, et al. Prediction meets causal inference: the role of treatment in clinical prediction models. *Eur J Epidemiol*. 2020;35:619–630. [10.1007/s10654-020-00636-1](https://doi.org/10.1007/s10654-020-00636-1).
3. Dickerman BA, Hernán MA. Counterfactual prediction is not only for causal inference. *Eur J Epidemiol*. 2020;35:615–617. [10.1007/s10654-020-00659-8](https://doi.org/10.1007/s10654-020-00659-8).
4. Yang Y. Can the strengths of AIC and BIC be shared? A conflict between model identification and regression estimation. *Biometrika*. 2005;92(4):937–950. [10.1093/biomet/92.4.937](https://doi.org/10.1093/biomet/92.4.937).
5. Shmueli G. To explain or to predict? *Statistical Science*. 2010;25(3):289–310. [10.1214/10-STS330](https://doi.org/10.1214/10-STS330).
6. Ahlmann-Eltze C, Huber W, Anders S. Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines. *Nature Methods*. 2025;22(8):1657–1661. [10.1038/s41592-025-02772-6](https://doi.org/10.1038/s41592-025-02772-6).
7. Viñas Torné R, et al. Systema: a framework for evaluating genetic perturbation response prediction beyond systematic variation. *Nature Biotechnology*. 2026;44(6):1050–1059（オンライン公開2025年8月25日）. [10.1038/s41587-025-02777-8](https://doi.org/10.1038/s41587-025-02777-8).
8. Miller HE, et al. Deep learning perturbation models can outperform baselines on calibrated metrics. *Nature Biotechnology*. オンライン公開2026年10月1日. [10.1038/s41587-026-03307-w](https://doi.org/10.1038/s41587-026-03307-w).
9. Arc Institute. [The 2026 Virtual Cell Challenge](https://arcinstitute.org/news/virtual-cell-challenge-2026)（2026年8月20日）. 最終テストセット公開は10月22日、最終提出期限は11月5日と記載。
10. SHAP documentation. [Be careful when interpreting predictive models in search of causal insights](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/Be%20careful%20when%20interpreting%20predictive%20models%20in%20search%20of%20causal%20insights.html).
11. Dayneka NL, Garg V, Jusko WJ. Comparison of four basic models of indirect pharmacodynamic responses. *J Pharmacokinet Biopharm*. 1993;21(4):457–478. [10.1007/BF01061691](https://doi.org/10.1007/BF01061691).
12. Sharma A, Jusko WJ. Characteristics of indirect pharmacodynamic models and applications to clinical drug responses. *Br J Clin Pharmacol*. 1998;45(3):229–239. [10.1046/j.1365-2125.1998.00676.x](https://doi.org/10.1046/j.1365-2125.1998.00676.x).
13. Gutenkunst RN, Waterfall JJ, Casey FP, et al. Universally sloppy parameter sensitivities in systems biology models. *PLoS Comput Biol*. 2007;3(10):e189. [10.1371/journal.pcbi.0030189](https://doi.org/10.1371/journal.pcbi.0030189).
14. Raue A, Kreutz C, Maiwald T, et al. Structural and practical identifiability analysis of partially observed dynamical models by exploiting the profile likelihood. *Bioinformatics*. 2009;25(15):1923–1929. [10.1093/bioinformatics/btp358](https://doi.org/10.1093/bioinformatics/btp358).
15. Kreutz C, Raue A, Timmer J. Likelihood based observability analysis and confidence intervals for predictions of dynamic models. *BMC Syst Biol*. 2012;6:120. [10.1186/1752-0509-6-120](https://doi.org/10.1186/1752-0509-6-120).
16. ICH. [M15 General principles for model-informed drug development, Step 4](https://database.ich.org/sites/default/files/ICH_M15_Step4_Final_Guideline_2026_0129.pdf)（2026年1月29日）.
17. U.S. FDA. [M15 General Principles for Model-Informed Drug Development, final guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m15-general-principles-model-informed-drug-development)（2026年6月3日）.
18. U.S. FDA. [Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making for Drug and Biological Products, draft guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological)（2025年1月）.
19. EMA, U.S. FDA. [Guiding principles of good AI practice in drug development](https://www.ema.europa.eu/en/documents/other/guiding-principles-good-ai-practice-drug-development_en.pdf)（2026年1月）. [EMAの発表](https://www.ema.europa.eu/en/news/ema-fda-set-common-principles-ai-medicine-development-0).
