## 要旨 {#article-abstract}

用量比較後に不確実性が残っても、それだけでは追加試験を正当化できない。価値は、新しい観測が行動を変え、定めた判断基準のもとで期待損失を減らせるかに依存する。

IDeate-Lung01の無作為化群の公開人数から、8対12 mg/kgを単純なBayes奏効・害モデルで比べた。奏効差は重症有害事象差より明確だった。仮想的な害の重み1では各群50人を追加する情報価値は、**将来の判断対象100人あたり0.074の奏効相当単位**に留まる。重み2と4では**1.62**、**11.02**だった。条件付きの研究計算であり、観測された臨床便益や金銭収益ではない。未公表の結合転帰と追跡の仮定は価値を大きく変えた。

## 背景と目的 {#article-introduction}

追加の無作為化用量比較が、奏効と害の判断をどの条件で変え、検討する価値を持つかを問う。用量選択資料全体の再構築より狭い問いである。

用途は研究の優先順位を考えることに限る。特定の選好では既に決着している交換関係と、追加根拠が役立ちうるものを区別する。治療推奨、別のB7-H3 ADCの用量選択、曝露反応・生存根拠の代替には使わず、判断への影響度は低いものとする。その用途を超えると、重要な便益を犠牲にし、重大な害を見落とす可能性がある。

## 方法 {#article-methods}

### 比較する観測と解析集団 {#observations-and-population}

共通の中間カットオフ**2024年4月25日**における、**Part 1の投与された無作為化群だけ**を使った。後の報告には非無作為化12 mg/kg拡大群もあるが除外した。表1に確認した入力を示す。

**表1　投与されたPart 1無作為化群の入力**

| Endpoint | 8 mg/kg | 12 mg/kg |
| --- | ---: | ---: |
| Treated randomized participants | 46 | 42 |
| Confirmed BICR response | 12 | 23 |
| All-cause Grade ≥3 TEAE | 20 | 21 |
| AE-associated treatment discontinuation | 3 | 7 |
| Adjudicated treatment-related ILD/pneumonitis | 4 | 5 |

同時点の有効性・安全性は公開中間発表から得た ([1](#ref-1))。重症事象と中止人数は、報告された小数1桁の割合と分母に合う一意の整数であり、集約値から再構築した人数である。奏効と間質性肺疾患（ILD）人数は明示されている。独立な反復イベント数ではなく、影響を受けた参加者数である。

主要論文と補足資料も別に確認した ([2](#ref-2))。奏効数は一致するが、後の高用量安全性表は無作為化群と拡大群を統合するため、今回の高用量群へ置き換えられない。投与された無作為化患者という推定対象も、割付全例のintention-to-treat推定対象と自動的には等しくない。

### 効用と事後モデル {#utility-and-posterior}

用量dについて、奏効確率を (p_d)、観測された治療・追跡過程で少なくとも1件の重症治療下発現有害事象（TEAE）を経験する確率を (q_d) とする。

\[
U_d(w)=p_d-wq_d,\qquad
\Delta U(w)=U_{12}(w)-U_8(w).
\]

重み (w) は、重症TEAEを経験する参加者1人の追加に対する仮想的な奏効相当の罰則である。1なら、この単一指標内で奏効1人と重症TEAE1人を同じ重さとする。**患者から聴取した選好、QALYの重み、死亡の価値付けではない**。

各評価項目・群の二項尤度とBeta(1,1)事前分布から、次の事後分布を得る。

\[
p\mid x,n\sim \operatorname{Beta}(x+1,n-x+1).
\]

主計算は4つの周辺パラメータを独立とする。線形効用の期待値は周辺値だけで決まるが、効用の不確実性と将来データの価値は結合モデルに依存する。独立性は公表表から確立した事実ではなく、結果を変える仮定である。

2つの問いを分けた。

1. **期待効用を最大にする行動。** 強制的な2択として (E[Delta U]>0) なら12 mg/kg、そうでなければ8 mg/kgを選ぶ。情報価値はこの規則で定義する。
2. **比較の確からしさ。** 記述規則では確率≥0.80を高用量寄り、≤0.20を低用量寄り、間を不確かとする。0.90/0.10も報告するが、どちらも臨床閾値ではない。

記述上の不確かさは、EVSI計算の第3の行動ではない。正式な判断延期を入れるなら、その費用と後の根拠取得戦略を定義する必要がある。

### 情報価値の計算 {#information-value-method}

完全情報の期待価値（EVPI）は、評価項目の確率を知るoracleに対し、現在の最良行動が負う期待損失である。その確率を学ぶ価値の上限を与える。標本情報の期待価値（EVSI）は、特定した不完全な追加試験を評価する。

\[
\operatorname{EVSI}(n,w)
=E_Y\left[\max_d E\{U_d(w)\mid D,Y\}\right]
-\max_d E\{U_d(w)\mid D\}.
\]

(D) は既存の集約根拠、(Y) は各群 (n) 人を追加した仮想の新人数である。新参加者は既存Part 1集団と交換可能で、転帰の確認過程も同じと仮定する。独立性のもとで4つの予測人数はベータ二項分布になる。共役性から事後平均を直接求め、ノイズを含む内側推定ループなしで離散確率の総和を計算できる。Strongらの意思決定論的定義に基づくが、この小さな共役モデルでは同論文の回帰近似は必要ない ([3](#ref-3))。

## 結果 {#article-results}

### 周辺評価項目と効用の不確実性 {#endpoint-and-utility-results}

図1と表1が示す評価項目について、奏効率差の事後推定は**+27.4パーセントポイント**、95%信用区間**+7.9–+46.0**だった。重症TEAE差は**+6.2ポイント**、区間**−14.0–+26.3**だった。新たに計算したモデル由来推定であり、試験が報告した信頼区間ではない。

![無作為化用量群の評価項目ごとの事後確率](shared/b7h3-adc-dose-information/figures/endpoint-evidence.png)

**図1　確認したPart 1人数からの計算。** 点と四角は事後平均、棒はBeta(1,1)事前分布による95%等裾信用区間。各区間は周辺評価項目のものである。

**表2　仮想重み別の効用比較**

| Hypothetical weight | Mean ΔU | 95% credible interval | P(ΔU > 0) | Descriptive 0.80 rule |
| --- | ---: | --- | ---: | --- |
| 0 | 0.275 | 0.079 to 0.460 | 0.997 | 12 mg/kg leaning |
| 1 | 0.212 | −0.066 to 0.487 | 0.932 | 12 mg/kg leaning |
| 2 | 0.150 | −0.293 to 0.597 | 0.743 | Uncertain |
| 4 | 0.025 | −0.798 to 0.856 | 0.523 | Uncertain |

期待効用の選択は約 (w=4.39) まで12 mg/kgだが、臨床カットオフではない。重み4付近では平均差はゼロに近く、両方向が考えられる。正の平均を確かな優位性として示すことはできない。図2と表2に重みごとの不確実性を示す。

![仮想的な害の重みによる効用不確実性](shared/b7h3-adc-dose-information/figures/tradeoff-uncertainty.png)

**図2　効用差と優位確率。** 上段は優位確率と記述的な確からしさの閾値、下段は平均効用差と信用区間。主要モデルは評価項目パラメータの独立を仮定し、重みは仮想値である。

### 追加比較の情報価値 {#additional-comparison-value}

図3と表3に、追加観測数による価値を示す。

**表3　将来の判断対象100人あたりの条件付き情報価値**

| Weight | EVPI | EVSI: +50/arm | EVSI: +100/arm |
| --- | ---: | ---: | ---: |
| 0 | 0.010 | <0.001 | 0.001 |
| 1 | 0.425 | 0.074 | 0.170 |
| 2 | 3.492 | 1.618 | 2.290 |
| 4 | 15.693 | 11.021 | 12.801 |

**すべて、定めた効用とモデルを条件とする、将来の判断対象100人あたりの奏効相当単位である。** 試験参加者の追加奏効人数ではない。EVPIはMonte Carlo推定、EVSIは離散モデルのもとで浮動小数点演算誤差を除いて厳密に計算した。

重み1では選択は比較的決まっており、4確率を完全に学んでも除ける期待損失は小さい。重み4ではその選好下の判断不確実性が大きいため、追加比較の条件付き価値も大きい。人数増加は情報を増やすが、どの選好が適切かは確立しない。

![追加人数と条件付きの情報価値](shared/b7h3-adc-dose-information/figures/information-value.png)

**図3　追加群人数に対する厳密EVSI。** 破線はMonte CarloのEVPIで、パネルの縦軸は異なる。研究費用、遅延、参加負担、生存便益は含めない。

独立確認として各設計60,000の将来試験をシミュレーションした。重み2で事後予測のoracleと異なる選択は、新データなしで約**25.7%**、各群50人追加で**18.4%**、100人追加で**14.8%**だった。モデル条件付きの低効用行動を選ぶ確率であり、頻度論の第I種過誤、臨床誤り率、実際の将来試験の予測ではない。期待後悔とMonte Carlo標準誤差を配布結果に含めた。

### 結合転帰と追跡仮定への感度 {#sensitivity}

#### 奏効と害の結合 {#joint-outcomes}

公開周辺人数では、奏効者と重症TEAE経験者が同じ人か分からない。各群で、重なり最小、周辺独立に最も近い重なり、重なり最大という3つの両立可能な結合表を作った。各セルにDirichlet事前分布0.5を置くと、周辺事後分布は主計算のBeta(1,1)更新のままなので、結合仮定だけの影響を調べられる。

重み2・各群50人追加のEVSIは、将来100人あたり**2.77**、**1.62**、**0.32**で、対応するMonte Carlo標準誤差は**0.028**、**0.019**、**0.006**だった。各仮定表の内部の計算精度であり、未知の表自体の不確実性ではない。両極端は同定上のストレス条件で、臨床依存の推定ではない。

#### 事前分布と評価項目と時点 {#prior-endpoint-timing}

表4の感度条件はいずれも重み2・各群50人追加を基準とする。

**表4　追加比較の情報価値の感度**

| Change from primary model | EVSI / 100 future subjects | Meaning |
| --- | ---: | --- |
| Primary severe-TEAE model | 1.62 | Marginal independence |
| Jeffreys prior | 1.63 | Prior sensitivity |
| Symmetric Beta(4,4) prior | 1.57 | Stronger regularization |
| AE-associated discontinuation as harm | 2.02 | Different criterion; not the same weight interpretation |
| All-grade adjudicated ILD as harm | 0.23 | Inadequate as a standalone severity valuation |
| 20% independent future evaluability loss | 1.39 | 40 informative participants/arm instead of 50 |
| 40% independent future evaluability loss | 1.09 | 30 informative participants/arm instead of 50 |
| Fixed hypothetical late-harm penalty +5 points at high dose | 4.39 | Additional utility penalty; not fitted incidence |
| Fixed hypothetical late-harm penalty +10 points at high dose | 4.36 | Additional utility penalty; not fitted incidence |

遅発性の害を加える条件は判断境界へ近づき、条件付き情報価値を増やす。10ポイント追加では重み2の現在の期待効用選択が低用量へ変わる。追加罰則は既知・固定とし、将来試験で学ぶのは観測された奏効・重症事象の周辺値であって、欠けた遅発性項ではない。その不確実性を扱うなら別のモデルとデータが必要になる。

同じ暦日のカットオフでも毒性の評価期間は揃わない。中間の追跡中央値は14.6、15.3か月、治療期間中央値は3.5、4.7か月だった。後の低用量重症TEAE人数は増えたが、比較可能な後の高用量無作為化安全性は確認した表で分離されていない。中央値や統合割合から欠けたイベント時間過程は復元できない ([1](#ref-1), [2](#ref-2))。図4と表4に仮定への感度を示す。

![未観測の結合転帰と遅発性の害に対する感度](shared/b7h3-adc-dose-information/figures/assumption-sensitivity.png)

**図4　重み2・各群50人追加での条件付き感度。** 左の誤差棒は95%Monte Carlo精度区間、右は固定した仮想の追加害罰則に対する厳密計算である。どちらも未報告の仮定を推定しない。

別の奏効分類ストレスでは、記載されていない最良総合効果（BOR）の残余人数を片群だけ奏効へ割り当てた。重み2・各群50人追加のEVSIは1.62から、低用量群へ割当で**3.82**、高用量群で**0.94**となった。反実仮想の再分類であり、観測奏効の補完や報告ORRの訂正ではない。

## 考察 {#article-discussion}

重み1のように奏効を重視する選好では、同じ二値データを増やす価値はこの判断基準で小さい。重症事象区間が広いという理由だけでは、大きな反復比較を正当化できない。

奏効と害の患者内の対応、イベント時点、長期の確認は集約値から分からない。それらの情報価値を別々には計算しておらず、大規模無作為化比較に対してどの測定を優先すべきかは順位付けできない。

投資判断へ変換するなら、対象集団の規模 (H) と、研究・遅延・機会費用 (C) を比較可能な単位で定める必要がある。条件式 (H	imesmathrm{EVSI}>C) は、その入力を与えない。最適例数や金銭収益は確立しない。計算で強制した2択から、追加用量比較が倫理的・運用的に妥当とも言えない。

### 限界 {#limitations}

公開集約人数からは、個人PK、曝露反応、生存、反復毒性、脱落機構を推定できない。ORRは持続便益や生存便益ではなく、Grade ≥3 TEAEも異なる重症度をまとめる。致死性と非致死性ILDを臨床的に同等と推定できない。害の定義変更は判断基準の変更であり、互いの検証ではない。新集団や別のB7-H3 ADCへの確率の移植は未検証である。

## 結論 {#article-conclusion}

追加の二値奏効・害観測の価値は、仮想選好と患者内の結合転帰の仮定に強く依存した。不確実性が残ることだけで大きな試験を支持できない。条件付きの情報価値から、最適例数、投資収益、臨床用量は確立しない。

## データとコードの公開状況 {#availability}

確認した人数、出典位置とハッシュ、解析コード、集約出力、自作図、実行済みノートブックを付属資料へ含めた。出版社文書と私的な計画資料は含めない。10の検証で、人数再構築、データ追加ゼロのEVSI、小設計の厳密列挙、予測期待値、単調性、完全情報上限、結合表の実現可能性、独立数値積分と試験シミュレーションとの一致を調べた。再現性が示すのは計算の確認であり、臨床上の限界は除かれない。

[コード・集約結果・実行済みノートブックのダウンロード](shared/b7h3-adc-dose-information/b7h3-adc-dose-information-companion.zip)

## 参照 {#article-references}

1. <span id="ref-1"></span>Rudin CM, Ahn MJ, Johnson M, Hann CL, Girard N, Nishio M, et al. OA04.03 Ifinatamab deruxtecan (I-DXd) in extensive-stage small cell lung cancer (ES-SCLC): interim analysis of IDeate-Lung01 [Conference abstract]. J Thorac Oncol. 2024;19(10):S15–S16. [doi:10.1016/j.jtho.2024.09.033](https://doi.org/10.1016/j.jtho.2024.09.033). Same-cutoff counts were obtained from the [Merck public interim release, 2024 Sep 7](https://www.merck.com/news/ifinatamab-deruxtecan-continues-to-demonstrate-promising-objective-response-rates-in-patients-with-extensive-stage-small-cell-lung-cancer-in-ideate-lung01-phase-2-trial/); the publisher abstract was not downloaded in the original source audit.
2. <span id="ref-2"></span>Rudin CM, Johnson ML, Paz-Ares L, Nishio M, Hann CL, Girard N, et al. Ifinatamab deruxtecan in patients with extensive-stage small cell lung cancer: primary analysis of the phase II IDeate-Lung01 trial. J Clin Oncol. 2026;44(4):261–273. [doi:10.1200/JCO-25-02142](https://doi.org/10.1200/JCO-25-02142). [Open-access record and supplementary appendix](https://pmc.ncbi.nlm.nih.gov/articles/PMC12834294/).
3. <span id="ref-3"></span>Strong M, Oakley JE, Brennan A, Breeze P. Estimating the expected value of sample information using the probabilistic sensitivity analysis sample: a fast, nonparametric regression-based method. Med Decis Making. 2015;35(5):570–583. [doi:10.1177/0272989X15575286](https://doi.org/10.1177/0272989X15575286). [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4471064/).
