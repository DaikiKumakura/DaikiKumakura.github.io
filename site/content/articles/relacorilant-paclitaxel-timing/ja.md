承認されたrelacorilantとnab-paclitaxelの間欠レジメンでは、経口薬を毎日飲み続けない。Relacorilantを点滴の前日・当日・翌日に投与し、nab-paclitaxelを28日周期のDay 1・8・15に投与する。この組み合わせは2026年3月、米国でプラチナ抵抗性卵巣癌などに承認された。[1]

Relacorilantはグルココルチコイド受容体（GR）の拮抗薬である。GR作用を介したタキサン反応への影響と、薬物相互作用によるpaclitaxel曝露の変化は、区別して検討する必要がある。[4]

この間欠投与を考える際には、二つのPKを区別する必要がある。併用によってpaclitaxelの曝露がどれだけ変わるか。そして、relacorilant自身の曝露を点滴の前後へどう配置するかである。前者の観測値があっても、後者の投与時刻を変更したときの相互作用まで予測できるとは限らない。

公開された第II相試験の集計PKを再解析し、FDA審査資料のrelacorilant PopPK係数を使って、この区別を数値で確かめた。**用量補正したpaclitaxelのAUC₀–₆は間欠併用群で単独群の1.66倍だった。一方、relacorilantの同じ９回投与を24時間ずらすと、周期全体のAUCは変わらなくても、点滴時点の親薬物濃度は変わった。**

文献・資料確認日は2026年10月22日。ここで示す投与時刻の変更は、公開情報を用いた研究上の比較であり、治療上の投与変更案ではない。

## 問いと使う範囲 {#_1}

**QOI**は、観測されたpaclitaxelの早期曝露増加と、relacorilantの親薬物曝露の時間配置を分けて評価できるか、である。さらに、投与条件の比較に必要な測定を絞り込めるかを考える。

**COU**は、公開資料に基づくPK比較と、追加のPK測定を計画するための条件整理とした。最適な投与開始日、GR阻害の持続時間、骨髄抑制の発生率、臨床的な有効性維持は予測しない。

臨床的な位置づけはROSELLA試験と承認資料で確認できる。[1,2] ただし、試験の組み合わせ全体の効果を、GRの薬理作用とpaclitaxelの曝露増加へ分解する解析は行っていない。

## 第II相試験で実際に観測されたPK {#iipk}

第II相試験には、relacorilantの間欠投与群、連日投与群、nab-paclitaxel単独群がある。[3] 補足資料Table S3から、paclitaxelの幾何平均、幾何CV、評価人数を転記した。

| 群 | Relacorilant | Nab-paclitaxel | Paclitaxel Cmax：幾何平均（幾何CV）、n | Paclitaxel AUC₀–₆：幾何平均（幾何CV）、n |
| --- | --- | --- | --- | --- |
| 単独 | なし | 100 mg/m² | 1,038 ng/mL（96.3%）、49 | 1,964 ng·h/mL（83.4%）、43 |
| 間欠併用 | 150 mg、点滴前日・当日・翌日 | 80 mg/m² | 1,574 ng/mL（88.8%）、50 | 2,606 ng·h/mL（70.4%）、33 |
| 連日併用 | 100 mg、毎日 | 80 mg/m² | 1,639 ng/mL（88.1%）、40 | 2,689 ng·h/mL（66.4%）、28 |

Nab-paclitaxelはいずれもDay 1・8・15、28日周期。表の濃度・AUCはpaclitaxelの値であり、後述するrelacorilantの計算値とは別である。CmaxとAUCのnが異なるため、同じ人の二つの測定値として扱っていない。

集中採血はCycle 1 Day 15の投与前、投与後1・2・4・6時間に行われた。解析対象は測定可能なPKを持つ投与例であり、無作為化された全例ではない。[3, 補足Methods pp5,8] 集計表だけでは評価可能例の代表性や群間の欠測差を確認できず、個人別の共変量調整もできない。後述の近似区間はこれらの選択や欠測を補正せず、測定されたCmaxが真のピークを捉えたことも保証しない。後半の周期定常モデルとは投与履歴・対象薬物が異なり、両者を同一条件の検証として扱わない。

ここでは、用量で割った幾何平均の比を推定した。群 \(g\) の幾何平均を \(G_g\)、nab-paclitaxel用量を \(D_g\) とすると、

\[
\widehat R_g=\frac{G_g/D_g}{G_0/D_0}.
\]

幾何CVを小数で \(v_g\) と表し、独立した群の対数正規近似から、

\[
SE(\log \widehat R_g)=\sqrt{\frac{\log(1+v_g^2)}{n_g}+\frac{\log(1+v_0^2)}{n_0}}
\]

を計算した。95%区間は \(\exp\{\log\widehat R_g\pm1.96SE\}\)。これは集計値から復元した近似区間であり、元の個票から推定した調整済みの区間ではない。比較は探索的で、多重比較補正はしていない。

| 単独群に対する用量補正比 | Cmax（近似95%区間） | AUC₀–₆（近似95%区間） |
| --- | --- | --- |
| 間欠併用 | 1.90（1.39–2.58） | 1.66（1.22–2.25） |
| 連日併用 | 1.97（1.42–2.74） | 1.71（1.25–2.34） |

![Paclitaxelの用量補正幾何平均比と近似95%区間。第II相試験の評価項目別集計値から計算。](shared/relacorilant-paclitaxel-timing/figures/paclitaxel-contrasts.png)

この結果は、現行ラベルに記載された用量補正Cmax約２倍、AUC約1.7倍と整合する。[4] ただし同じ試験に由来する情報であり、独立した検証ではない。また、用量で割る操作は記述的な比較であって、80から100 mg/m²への用量比例性を証明してはいない。

**AUC₀–₆は部分AUCであり、AUC∞ではない。** この比の逆数をそのままクリアランス比とすると、分布や採血窓の影響を消失の変化と取り違える。２つの集計PK指標だけで、relacorilant濃度からCYP阻害、さらにpaclitaxel濃度へ至る時間依存モデルを同定することもできない。

## Relacorilantの時間配置を計算する {#relacorilant}

FDA審査資料には、relacorilantの２コンパートメントPopPKモデルと最終係数が掲載されている。[5] 吸収は、一定時間のゼロ次入力と、その後の一次吸収を組み合わせる。

投与時刻を \(t_k\)、量を \(D_k\)、入力持続時間を \(D_1\) として、消化管への入力を

\[
R_g(t)=\sum_k\frac{F_{\rm rel}D_k}{D_1}\mathbf{1}(t_k\le t<t_k+D_1)
\]

と書く。量の状態変数を \(A_g,A_c,A_p\) とすると、

\[
\begin{aligned}
\frac{dA_g}{dt}&=R_g(t)-k_aA_g,\\
\frac{dA_c}{dt}&=k_aA_g-\frac{CL+Q}{V_c}A_c+\frac{Q}{V_p}A_p,\\
\frac{dA_p}{dt}&=\frac{Q}{V_c}A_c-\frac{Q}{V_p}A_p,\\
C(t)&=1000\frac{A_c(t)}{V_c}\quad[\mathrm{ng/mL}].
\end{aligned}
\]

量はmg、容積はL、時間はh。\(CL,V_c,Q,V_p\) は、空腹時を基準にした見かけの係数である。\(F_{\rm rel}\) はその基準に対する相対バイオアベイラビリティとして入力側に一度だけ掛ける。

| 係数 | 食後条件の入力値 | 扱い |
| --- | --- | --- |
| CL/F | 46.7 L/h | 公表最終値 |
| Vc/F | 220 L | 公表最終値 |
| Q/F | 45.0 L/h | 公表最終値 |
| Vp/F | 850 L | 公表最終値 |
| ka | 0.775 h⁻¹ | 食後の公表値 |
| D₁ | 1.66 h | 食後の公表値 |
| Frel | 2.13 | 空腹時に対する食後の相対値。絶対Fではない |

元の共変量式の中心化と相関構造を確認できなかったため、BMI・年齢の乗数を１に固定した条件付きの再構成とした。「平均的な患者」の同定や元のPopPK解析の完全再現ではない。現行の食後投与に合わせ、空腹時への切替比較は行わない。

数値実装には線形系の固有値分解による畳み込みを使い、過去周期からの蓄積も加えた。独立したODE積分との比較、長い反復投与による計算との比較、投与量と周期AUCの関係で検証した。

### どこまで公表濃度に近づくか {#_2}

初回投与前の薬物をゼロとし、食後150 mgを24時間ごとに３回投与すると、条件固定モデルの３回目Cmaxは**767 ng/mL**、ピークはその投与から**2.72時間後**だった。ラベルの３回目投与後Cmaxは720 ng/mL、中央値Tmaxは2.5時間である。[4]

Cmaxの差は+6.5%だった。ただし条件固定モデルの値とラベルの集団要約値を比べており、個人別データによる外部検証ではない。ラベルのAUC 5,686 ng·h/mLは、この確認で積分区間を特定できなかったため、今回の48–72時間AUC 6,194 ng·h/mLと同じ指標として誤差判定しなかった。値を合わせるための再調整も行っていない。

第II相試験のTable S3にはrelacorilant自身の間欠群PKもあり、C1D15のCmaxは668 ng/mL、AUC₀–₂₄は3,668 ng·h/mLだった。[3] 初回周期の投与履歴をモデルへ入れ、同じ点滴日の24時間窓を計算すると、それぞれ744 ng/mL、5,742 ng·h/mLとなり、公表幾何平均より11.3%、56.5%高い。条件固定値と集団幾何平均の比較ではあるが、AUC差は小さくない。共変量・食事・個票を揃えられず原因は特定できていないため、**この再構成を絶対曝露の検証が済んだモデルとは扱わない。** 以下の比もモデル内の感度であり、投与時刻を変えた患者の曝露を検証済みの精度で予測するものではない。

## 同じ９回投与を24時間ずらす {#924}

Nab-paclitaxelの点滴を時刻0、168、336 hに置き、28日周期が反復した状態を比較した。点滴開始と当日の内服を同時刻に置くのは今回の標準化条件であり、ラベルが内服時刻を時単位で指定しているという意味ではない。

| 計算条件 | 各点滴から見たRelacorilantの内服時刻 | 28日あたりの量 |
| --- | --- | --- |
| Intermittent（基準） | −24、0、+24 hに150 mg | 1,350 mg |
| Early（仮定） | −48、−24、0 hに150 mg | 1,350 mg |
| Late（仮定） | 0、+24、+48 hに150 mg | 1,350 mg |
| Continuous（公表連日条件） | 100 mgを24時間ごと | 2,800 mg |

EarlyとLateは３回の窓全体をずらした仮想条件であり、飲み忘れ時の対処を表さない。

![条件固定のRelacorilant親薬物濃度。上は28日周期、下は最初の点滴周辺。灰色は点滴開始後６時間。縦線は点滴時刻。](shared/relacorilant-paclitaxel-timing/figures/parent-timecourse.png)

比較指標は、親薬物の周期AUC、３回の点滴それぞれの開始後0–6 h AUCの合計、点滴時点濃度の３回平均とした。６時間窓はpaclitaxelの公開部分AUCに合わせた観測計画上の窓であり、GR作用やCYP阻害がこの窓だけで決まるという仮定ではない。

| 条件固定モデル | 周期AUC（ng·h/mL） | 点滴後0–6 h AUCの合計（ng·h/mL） | 点滴時点濃度の平均（ng/mL） |
| --- | --- | --- | --- |
| Intermittent | 61,574 | 9,229 | 58.6 |
| Early | 61,574 | 9,706 | 87.1 |
| Late | 61,574 | 8,354 | 6.1 |
| Continuous | 127,709 | 6,852 | 80.9 |

線形・時不変モデルの周期定常状態では、

\[
AUC_{\rm cycle}=\frac{1000F_{\rm rel}\sum_kD_k}{CL}
\]

となる。したがって３つの間欠条件の周期AUCが等しいのは、モデル構造から必然的に得られる結果である。新たな臨床知見ではない。同じ総曝露でも、点滴時点と点滴後の曝露は異なる。

Earlyでは基準より点滴時点の濃度が高い。しかし点滴後６時間のAUC増加は約５%にとどまる。Lateでは点滴時点濃度は大幅に低いものの、その後に当日分が吸収されるため、点滴後６時間AUCの低下は約10%である。**点滴直前の１点だけでは、同じ時間帯のAUCを代用できない。**

連日条件は総投与量が多く、周期AUCは基準の2.07倍になる。一方、点滴後６時間の親薬物AUCは基準より低い。これは100 mgと150 mgの当日量の違いと、投与の配置による。この計算だけで連日条件の薬効や安全性を順位付けすることはできない。

## 4,096人の条件付きシミュレーション {#4096}

公表IIVのうち、CL 54%、Vc 40%、Vp 30%、食後ka 62%、D₁ 59%、食後相対F 31%を使用した。[5] これらをCVとして \(\omega^2=\log(1+CV^2)\) に変換し、独立した正規乱数 \(\eta\) から \(\theta_i=\theta\exp(\eta_i)\) を作った。

元の完全なΩ行列や共変量の同時分布を復元してはいない。したがって、実際の患者集団を代表する仮想患者群ではなく、公表ばらつきを使った条件付き感度解析である。残差誤差は加えず、同じ乱数を４条件に使った。固定効果の推定誤差もこの乱数には含めていない。以下の区間は個人間の5–95パーセンタイルであり、推定値の信頼区間ではない。

| 基準に対する同一個体内比：中央値［5–95%点］ | Early | Late | Continuous |
| --- | --- | --- | --- |
| 周期AUC | 1.00［1.00–1.00］ | 1.00［1.00–1.00］ | 2.07［2.07–2.07］ |
| 点滴後0–6 h AUC合計 | 1.05［1.02–1.13］ | 0.90［0.79–0.96］ | 0.75［0.69–0.95］ |
| 点滴時点濃度の平均 | 1.47［1.33–1.51］ | 0.11［0.01–0.37］ | 1.39［1.01–1.83］ |

![同じ条件付き個体で比較した親薬物曝露比。点は中央値、線は個人間5–95%点。](shared/relacorilant-paclitaxel-timing/figures/paired-window-ratios.png)

周期AUC比にばらつきがないのは、共通のCLと相対Fが比で消えるためである。実際の個人についてこれほど精密に予測できるという意味ではない。

構造的な感度分析として、D₁を0.5–3 h、kaを0.4–1.2 h⁻¹、CLとVpをそれぞれ公表中心値の0.75–1.25倍に一つずつ変えた。これらは信頼区間ではなく、影響を見るための条件である。点滴後６時間AUCの比はEarlyで1.04–1.07、Lateで0.88–0.92となり、この範囲では方向は変わらなかった。相関を含む集団全体の不確実性を包絡する結果ではない。

## 親薬物の半減期は相互作用の回復半減期ではない {#_3}

今回計算したrelacorilantの濃度を、paclitaxelの観測値へ直接つなぐことはしなかった。親薬物濃度が高い時刻と、CYP阻害やGR作用が強い時刻は一致するとは限らず、活性代謝物CORT125295もこのモデルには含まれない。[4]

Late条件では、点滴時点の濃度とその後６時間AUCが同じ方向へ動かなかった。点滴前の1点だけで、投与時刻変更の効果全体を代表させることはできない。

阻害の発現・回復を推定した解析ではないため、親薬物の終末半減期をCYP阻害の回復半減期として扱う根拠もない。ここで得たのは親薬物の時間配置の違いであり、相互作用やGR作用の改善予測ではない。

## 結論の範囲 {#_4}

公開集計値から、間欠併用群のpaclitaxel早期曝露が用量補正後にも高いことを確認できた。ただし、部分AUCから全身クリアランスの変化を推定したわけではない。

Relacorilantの公表PopPK係数を使うと、同じ総量の間欠投与でも、点滴時点濃度と点滴後の曝露を別々に変えられることが分かる。周期AUC、点滴前濃度、点滴後AUCは、それぞれ異なる問いに答える指標である。

この解析が支持するのは、比較すべきPK指標と採血条件の整理までである。Earlyが優れる、Lateでも薬効が維持される、連日投与を避けるべきだという結論は出していない。

## 再実行と出典 {#_5}

`analysis/run_analysis.py` が集計値の比、条件付き4,096人、感度分析、６つのCSV、３つの図と`results.json`を生成する。`analysis/test_model.py`でODE、周期定常、AUC収支、集計比を検査する。新たな個人別NLME推定は行っていない。公開集計値からの対数平均差の推定と、公表係数を用いたシミュレーションである。

元論文・補足資料・審査資料の図や患者データは配布物に含めず、入力係数、計算コード、独自図表、出典とファイルハッシュを収録する。

1. FDA. [Relacorilant with nab-paclitaxel approval, 25 March 2026](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-relacorilant-nab-paclitaxel-platinum-resistant-epithelial-ovarian-fallopian-tube-or). Used to check the current regimen and indication.
2. ROSELLA investigators. [Relacorilant plus nab-paclitaxel versus nab-paclitaxel in platinum-resistant ovarian cancer](https://pubmed.ncbi.nlm.nih.gov/40473448/). *Lancet*. 2025. [doi:10.1016/S0140-6736(25)01040-2](https://doi.org/10.1016/S0140-6736(25)01040-2). [Final OS analysis](https://pubmed.ncbi.nlm.nih.gov/41974149/), 2026. Cited for clinical context, not used for PD coefficients in this analysis.
3. Colombo N, et al. [Relacorilant + Nab-Paclitaxel: randomized three-arm phase II study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10602497/). *J Clin Oncol*. 2023. [doi:10.1200/JCO.22.02624](https://doi.org/10.1200/JCO.22.02624). [Supplementary materials PDF](https://scientiasalut.gencat.cat/bitstream/handle/11351/10535/relacorilant_nab_paclitaxel_patients_recurrent_platinum_resistant_ovarian_cancer_a_three_arm_randomized_controlled_oen_label_phase_ii_study_2023_material_suplementari.pdf?isAllowed=y&sequence=2), Table S3, p18. Source of aggregate PK values.
4. DailyMed. [LIFYORLI prescribing information](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6fcebfb5-19d6-4f63-b852-999d68a13729), March 2026, §§2,12.3. Fed administration, parent/metabolite PK and interactions.
5. FDA. [NDA 220641 multidisciplinary review](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2026/220641Orig1s000MultidisciplineR.pdf), PDF pp280–285, especially 283–284 (printed pp. 282–283). Tumor-population PopPK structure, final estimates and IIV.


[解析コード・入力値・集計表・再実行手順](shared/relacorilant-paclitaxel-timing/relacorilant-analysis.zip)
