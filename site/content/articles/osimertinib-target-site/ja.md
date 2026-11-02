## 背景と目的 {#article-introduction}

文献確認日：2026年10月19日。公開PBPKモデルをPythonへ移植し、推定済みパラメータで数値計算した。新しい患者データの推定や、治療用量の提案ではない。

線形PKを仮定すれば、用量を2倍にすると血漿曝露も2倍になる。では、腫瘍内曝露や標的阻害も2倍になるだろうか。

オシメルチニブには、肺腫瘍とEGFR結合を含む全身PBPKモデルが公開されている ([1](#ref-1), [2](#ref-2))。血漿だけを見るモデルから一歩進められるが、出力に「腫瘍」「結合」という名前が付けば、臨床的な作用を直接表すわけではない。今回は80 mgと160 mgの1日1回投与を比べ、どの違いが計算でき、どこで解釈を止めるべきかを調べた。

**原コードの吸収式では、80→160 mgで血漿の後半平均は2.00倍、肺腫瘍のモデル内総濃度は1.80倍、可逆結合状態の割合は85.1%→92.0%だった。** これを有効性の倍率や増量の利点とは解釈しない。

## 問いと使う範囲 {#_1}

**表1．** 比較の問いと解析の使用範囲。

| Item | Definition |
| --- | --- |
| QOI | With the same public parameters, how do plasma, modeled lung-tumor drug amounts, and reversible EGFR binding change from 80 to 160 mg? How do absorption and tumor-partition assumptions affect interpretation? |
| COU | Examine implementation, output meanings, and assumptions requiring further validation when planning target-tissue exposure comparisons. Not intended for patient dose escalation, CNS treatment selection, or optimization of efficacy and safety. |
| Analysis | Conditional numerical calculations with fixed parameters. No new parameter estimation, interpatient-variability estimation, or virtual-population generation. |

80 mg/日は製品情報に記載される通常用量である ([3](#ref-3))。160 mg/日を検討したBLOOM試験は存在するが、対象は髄膜転移を伴う患者であり、今回の**肺腫瘍モデルによる比較を、その試験の再解析やCNSでの増量根拠とはしない** ([4](#ref-4))。薬物相互作用に伴う用量調整も、ここでは再現していない。

## 何を取得し何を取得していないか {#_2}

**表2．** 使用した公開資料と確認できない範囲。

| Material | Obtained and used | Not established here |
| --- | --- | --- |
| 2025 paper ([1](#ref-1)) | Tumor volume, EGFR abundance, binding rates, and state definitions in [original Table 1](https://doi.org/10.1002/psp4.70006) | Re-estimation of original patients' efficacy or toxicity |
| Original Appendices S2–S5 | Tissue volumes, flows and composition, drug properties, partition equations, whole-body ODEs | Empirical validation of unbound tissue concentrations |
| Author-released code ([2](#ref-2)) | Parameters, partition coefficients, and ODE implementation at a fixed commit | Guaranteed agreement with every R/deSolve output |
| Prescribing information and clinical study ([3](#ref-3), [4](#ref-4)) | Distinction between clinical doses and the comparison conditions | Clinical superiority of 80 or 160 mg |

使用コードのコミットは`00c6410c000bcb3b32b7fa54f2cb3a2aed87dcbd`。元ファイルを保存し、SHA256も記録した。原著のPET・臨床PK個票は再取得していない。したがって、以下で確認するのは式・量収支・数値計算の整合であり、患者データによる独立の臨床検証ではない。

## 全身の薬物量とEGFR結合状態を分ける {#egfr}

13組織の非EGFR結合量、10組織のEGFR結合量、消化管内腔、動脈血、静脈血を追う26状態のモデルとした。さらに消失量と未吸収量を積算し、量収支を検査する。時間はmin、量はnmol、容積はLである。濃度nmol/LはnMに等しい。

一般的な組織で、非EGFR結合量を \(A_i\)、EGFR結合量を \(B_i\)、組織容積を \(V_i\)、細胞内水容積を \(V_{iw,i}\)、組織EGFR濃度を \(R_i\) とする。原コードの交換・結合を整理すると、

\[
C_{out,i}=\frac{A_i}{V_i}\frac{bp}{K_{p,i}}
\]

\[
U_i=k_{on,i} A_i\frac{\max(R_iV_i-B_i,0)}{V_{iw,i}}-k_{off,i}B_i
\]

\[
\dot A_i=Q_i(C_{in,i}-C_{out,i})-U_i-E_i,
\qquad \dot B_i=U_i
\]

となる。肝臓は腸管・脾臓と肝動脈から流入し、腎・肝に消失がある。肺・肺腫瘍は静脈から流入する原モデルの構造を保持した。全組織の式は配布コードに含めた。

\(bp\) は血液/血漿比なので、静脈血からの血漿濃度は \(C_{plasma}=A_{ven}/(V_{ven}bp)\) と計算する。組織/血漿係数 \(K_p\) と、組織/血液係数を混ぜない。

**表3．** 代表パラメータと位置付け。

| Parameter | Value | Interpretation |
| --- | ---: | --- |
| Molecular weight | 500 g/mol | Source rounding used for mg-to-nmol conversion |
| Plasma unbound fraction \(f_u\) | 0.0535 | Not the tissue unbound fraction |
| Blood/plasma ratio \(bp\) | 1/1.30 | Conversion to plasma concentration |
| Absorption rate \(k_a\) | 0.24/60 min⁻¹ | Source value |
| Absorption coefficient \(F\) | 0.70 | Its placement in the equations is compared below |
| Calculated tumor Kp | 1.6014 | Calculated with source partition equations |
| Lung-tumor volume | 0.046 L | Fixed source assumption |
| Tumor EGFR concentration | 382.65 nM | Not an individual measurement |
| Tumor \(k_{on},k_{off}\) | 0.18 nM⁻¹min⁻¹, 86.1 min⁻¹ | Source averages WT and L858R/T790M-mutant rates |
| Intrinsic hepatic CL, renal CL | Approximately 3.631, 0.235/60 L/min | Calculated using source expressions |

\(K_p\) は細胞内外水、脂質、酸性リン脂質、lysosomal trappingの項から算出した。式中の`LogP`等も、原コードの数値・使い方を保持し、こちらで別の物性定義へ自動修正していない。これは原実装に沿った条件の検討であり、全ての生理学的仮定が検証済みという意味ではない。

### 「非EGFR結合」と「非結合型」は同じではない {#egfr_1}

今回の腫瘍出力は、次の三つに分けた。

\[
C_{tumor,nonEGFR}=A_{tumor}/V_{tumor}
\]

\[
C_{tumor,total}=(A_{tumor}+B_{tumor})/V_{tumor}
\]

\[
f_{bound}=B_{tumor}/(R_{tumor}V_{tumor})
\]

\(A_{tumor}\) には組織分配・非特異的な保持を反映する量が含まれる。これを「腫瘍内非結合型濃度」とは呼ばない。また、\(f_{bound}\) は**モデル内の可逆結合状態の割合**である。親薬物のみを追い、活性代謝物AZ5104・AZ7550も含めていない。不可逆阻害や標的の合成・分解を直接追うモデルではないため、真のEGFR阻害率や薬効には置き換えない。

原モデルではWT・L858R/T790M変異型の結合速度を平均しており、exon 19 deletionなど他の変異へ一般化しない。異なる二種類の受容体を独立に追った平均とは一般に一致しない。この近似も維持したまま計算している。結合流入には非EGFR結合量と細胞内水容積の比を使う有効的な構造があり、薬理学的な細胞内遊離濃度を直接追ったものではない。

## まず公開コードのまま80 mgと160 mgを比較する {#80-mg160-mg}

0日から1日1回、28日間投与した。比較窓は両条件とも27–28日の同じ24時間である。原コードの臨床PK比較用イベントには、初回後に間隔を空ける設定があるが、今回はそのイベント列の再現ではなく、連日投与の比較へ変更した。

**表4．** 原コードの吸収式による後半24時間の比較。

| Dose | Mean plasma, nM | Mean tumor non-EGFR-bound, nM | Mean tumor total, nM | Mean reversible binding fraction | Predose binding fraction |
| --- | --- | --- | --- | --- | --- |
| 80 mg/day | 742.6 | 1189.2 | 1515.0 | 85.1% | 82.9% |
| 160 mg/day | 1485.2 | 2378.5 | 2730.4 | 92.0% | 90.7% |

全て27–28日の共通区間。患者の実測値・母集団平均・真の標的阻害率ではない。

![原コードの吸収式を使用した、血漿・肺腫瘍のモデル内総濃度・可逆結合状態の経時推移。](shared/osimertinib-target-site/figures/01-exposure.png)

**図1．** 原コードの吸収式を使用した、血漿・肺腫瘍のモデル内総濃度・可逆結合状態の経時推移。

非EGFR結合量はほぼ2倍になったが、総濃度の増加は80.2%だった。丸め前の値から計算した結合状態の平均の差は6.8パーセントポイントであり、「結合が2倍」という結果ではない。

この違いには飽和可能な結合量が関わる。非EGFR結合量は増量にほぼ比例する一方、結合量には \(R_{tumor}V_{tumor}\) という上限がある。したがって、総量の増加率は血漿濃度の増加率より小さくなり得る。ただし、これを「160 mgでは薬効が飽和する」とは解釈できない。

## F=0.70は吸収量を70%にしているか {#f07070}

公開コードでは、消化管内腔と腸管への流入の両方に、同じ \(F\) が掛かっている。

\[
\dot A_{lumen}=-k_aFA_{lumen},\qquad
R_{gut,in}=k_aFA_{lumen}
\]

この構造では、十分な時間が経つと内腔から消えた量は全て腸管区画へ入る。\(F\) はこの箇所では吸収速度を変え、投与量の30%を未吸収として失わせる係数にはなっていない。肝臓での初回通過消失は別に存在するため、これを「全身バイオアベイラビリティが100%」という意味にはしない。

対照として、内腔の減少と腸管への流入を分けた。

\[
\dot A_{lumen}=-k_aA_{lumen},\qquad
R_{gut,in}=Fk_aA_{lumen},\qquad
R_{loss}=(1-F)k_aA_{lumen}
\]

こちらは原実装への**未検証の変更**である。臨床データに再適合しておらず、元のモデルを修正・改善できたとは主張しない。他のパラメータを固定し、\(F\) の置き方だけで解釈がどれだけ動くかを調べる。

**表5．** 未吸収量を分離した対照条件の比較。

| Dose | Mean plasma, nM | Mean tumor non-EGFR-bound, nM | Mean tumor total, nM | Mean reversible binding fraction | Predose binding fraction |
| --- | --- | --- | --- | --- | --- |
| 80 mg/day | 519.8 | 832.5 | 1138.6 | 80.0% | 76.7% |
| 160 mg/day | 1039.7 | 1664.9 | 2005.0 | 88.9% | 86.8% |

上表は吸収量を分離する未検証の変更。同じ他パラメータで計算した対照であり、原著より正しい予測とはしていない。

![吸収式の二つの解釈による、160/80 mg比と絶対的な可逆結合状態の比較。sourceは原コード、fractionは未検証の変更。](shared/osimertinib-target-site/figures/02-absorption.png)

**図2．** 吸収式の二つの解釈による、160/80 mg比と絶対的な可逆結合状態の比較。sourceは原コード、fractionは未検証の変更。

80 mgでは血漿平均が742.6→519.8 nM、結合状態の平均が85.1%→80.0%へ変わった。後者の計算では28日までに総投与量の30.00%を未吸収量として追跡した。

同じ係数を使っていても、式の中で何を制御する係数かによって答えは変わる。特に絶対的な結合状態から閾値達成を議論するなら、この相違を残したまま先へ進めない。

## 血漿が同じでも腫瘍の総量は変わる {#_3}

腫瘍 \(K_p\)、血流、EGFR量を、それぞれ単独で基準の0.5倍・2倍に変更した。これは患者分布でも、公表信頼区間でもない。ここでのKpは非EGFR結合区画の組織量と血漿総濃度の分配を規定する係数であり、その感度を非結合型比Kpuuの変化とは読まない。体重や他の組織は固定し、腫瘍血流を変えるときは肺血流を反対方向へ変えて総心拍出量を保った。

**表6．** 腫瘍の要因を一つずつ変更した感度分析。

| Change | Mean plasma ratio | Mean tumor-total ratio | Mean binding fraction |
| --- | --- | --- | --- |
| Tumor Kp ×0.5 | 1.000000 | 0.580 | 74.1% |
| Tumor Kp ×2.0 | 1.000000 | 1.802 | 92.0% |
| Tumor blood flow ×0.5 | 1.000000 | 1.000 | 85.1% |
| Tumor blood flow ×2.0 | 1.000000 | 1.000 | 85.1% |
| Tumor EGFR abundance ×0.5 | 1.000000 | 0.892 | 85.1% |
| Tumor EGFR abundance ×2.0 | 1.000000 | 1.215 | 85.1% |

80 mg、原コードの吸収式。比は同じ80 mg基準に対する条件付きの変化。1付近の微小差を意味のある個人差として読まない。

![80 mgでの単独変更。左は血漿と腫瘍総濃度の基準比、右は可逆結合状態。丸は0.5倍、三角は2倍。左の横軸は0.95–1.05。血漿平均はどの条件もほぼ1であり、横方向の微小な数値差は表示上区別しない。](shared/osimertinib-target-site/figures/03-sensitivity.png)

**図3．** 80 mgでの単独変更。左は血漿と腫瘍総濃度の基準比、右は可逆結合状態。丸は0.5倍、三角は2倍。左の横軸は0.95–1.05。血漿平均はどの条件もほぼ1であり、横方向の微小な数値差は表示上区別しない。

\(K_p\) の変更は腫瘍濃度と結合状態を動かした。一方、EGFR量を増やすと総濃度は上がるが、結合状態の**割合**はほとんど変わらなかった。「腫瘍に多く薬がある」ことと、「標的の何割が結合状態か」を分ける必要がある。

このモデルで、定常周期の組織量と結合量の1周期変化が0に近く、腫瘍に消失がなければ、

\[
0\simeq Q_{tumor}\{\overline C_{ven,blood}
-\overline C_{tumor,nonEGFR}\,bp/K_{p,tumor}\}
\]

なので、\(\overline C_{tumor,nonEGFR}\simeq K_{p,tumor}\overline C_{plasma}\) となる。血流を変えても後半平均がほぼ変わらなかったことは、この構造で説明できる。**実際の低灌流腫瘍でも血流が重要でない、という結論ではない。** 初期到達過程、膜透過律速、輸送体、壊死、組織内不均一性は別に検討する必要がある。

## 数値計算で確認した範囲 {#_4}

**表7．** 数値計算の検査と結果。

| Check | Result |
| --- | --- |
| Change integrator and tolerances | Maximum relative difference in principal means: 7.9e-08 |
| Final 24 hours at day 28 versus day 56 | Maximum relative difference in principal means: 4.5e-06 |
| Administered dose = body amount + eliminated amount + unabsorbed amount | Maximum relative error: 7.3e-15 |
| Seven unit tests | Mass balance, binding bounds, Jacobian, dose proportionality without binding, absorption loss, and source parameters passed |

1日ごとの投与イベントで積分を区切り、投与直前の量を次の積分へ受け渡した。硬い結合速度を扱うためBDFと解析的Jacobianを使い、より厳しい許容誤差のRadauでも比較した。期間を56日まで延ばした値も確認したが、この数値的な安定性を臨床的妥当性とは呼ばない。

出力の出所は`analysis/run_analysis.py`、表は`outputs/tables/exposure.csv`と`sensitivity.csv`、検証値は`outputs/verification.json`である。ランダム抽出はなく、図の線は患者集団の区間ではない。

## 考察 {#_5}

今回の計算では、血漿と腫瘍総量が同じ倍率では動かなかった。ただし、絶対的な結合状態は吸収式の解釈に依存し、その結合状態自体も不可逆阻害率ではない。

観測されるPETの総シグナル、モデル中の薬物量、標的への不可逆結合は異なる量である。今回、不可逆結合や標的turnoverまで検証したわけではなく、肺腫瘍の結果からCNSへの移行も評価していない。

したがって、公開PBPKモデルの計算結果だけから80 mgと160 mgの臨床的な優劣は決まらない。濃度の増加を占有率や薬効の増加へ読み替える前提が、この比較では満たされていない。


## データとコードの公開状況 {#article-data}

図と派生表は本稿の計算から作成した。出典、変更内容、ライセンスは[計算コード・係数・表・再実行手順](shared/osimertinib-target-site/osimertinib-pbpk.zip)に記録した。原著図や患者データは再配布していない。

## 参照 {#article-references}

1. <span id="ref-1"></span>van der Gaag S, Jordens T, Yaqub M, Grijseels R, van Valkengoed DW, de Langen EN, et al. Physiologically Based Pharmacokinetic Model of Tyrosine Kinase Inhibitors to Predict Target Site Penetration, with PET ‐Guided Verification. CPT: Pharmacometrics & Systems Pharmacology. 2025;14(5):918–928. [doi:10.1002/psp4.70006](https://doi.org/10.1002/psp4.70006).
2. <span id="ref-2"></span>Bartelink I and contributors. Target-Site-PBPK-in-oncology. Source code, commit 00c6410c000bcb3b32b7fa54f2cb3a2aed87dcbd. [Repository](https://github.com/ibartelink/Target-Site-PBPK-in-oncology/tree/00c6410c000bcb3b32b7fa54f2cb3a2aed87dcbd). Apache License 2.0.
3. <span id="ref-3"></span>TAGRISSO (osimertinib): US prescribing information. [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5e81b4a7-b971-45e1-9c31-29cea8c87ce7). Accessed 2026 Oct 19.
4. <span id="ref-4"></span>Yang JCH, Kim SW, Kim DW, Lee JS, Cho BC, Ahn JS, et al. Osimertinib in Patients With Epidermal Growth Factor Receptor Mutation–Positive Non–Small-Cell Lung Cancer and Leptomeningeal Metastases: The BLOOM Study. Journal of Clinical Oncology. 2020;38(6):538–547. [doi:10.1200/JCO.19.00457](https://doi.org/10.1200/JCO.19.00457).

<span id="_6"></span>
