[English version](/writing/savolitinib-parent-metabolite-ddi-en.html)

薬物相互作用で親薬物のAUCが増えたとき、用量を下げれば元の曝露に近づけられる。しかし、活性代謝物も同じように戻るとは限らない。Savolitinibとfluvoxamineの公開試験は、この違いを計算する材料になる。

以下のAUCは投与直後から無限時間までのAUC（AUCinf）を指す。最終観測時点までのAUClastとは区別する。同じ300 mgで比較したAUCinf比は、親薬物が3.25、活性代謝物M2が0.37だった。本稿では、この二つの比から曝露をそろえる条件を調べる。**親薬物のAUCを厳密に合わせる線形計算では、M2のAUCは基準の11.4%になる。** これは薬効が11.4%になるという意味ではない。

## 問いと使用範囲

QOIは「親薬物のAUCを合わせる用量変更で、M2の曝露も保てるか」とする。COUは、公開集計PKに基づいてDDI時に追跡する曝露指標を検討する研究目的の計算である。患者の処方変更、併用可否、抗腫瘍効果の予測には使用しない。

新しいPopPK推定や仮想患者の生成は行わない。16人の集計値から、同一人の親薬物とM2の相関やDDI効果の分布は再構成できないためである。ここで必要なのは集団を増やすことではなく、AUCを合わせる操作が何を保ち、何を変えるかを明確にすることだ。

## 公開試験が観測したもの

2026年の第I相試験では、健康成人男性16人にsavolitinib 300 mgを単回投与し、別期間にfluvoxamine 50 mg BID投与下で同じ300 mgを投与している。比較は固定順序の個人内比較であり、がん患者の反復投与試験ではない。M2は活性代謝物、M3は非活性代謝物として記載されている（[Miah et al., 2026](https://doi.org/10.1002/prp2.70321)）。

| 指標 | 親薬物 | M2 | M3 |
| --- | ---: | ---: | ---: |
| 同用量でのAUCinf比 | 3.25 | 0.37 | 3.27 |
| AUCinf比の90% CI | 2.87–3.68 | 0.33–0.41 | 2.85–3.74 |
| 同用量でのCmax比 | 1.95 | 0.12 | 1.58 |

数値は原著[Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC13598373/)の幾何最小二乗平均比である。以下の計算にもこの比を使う。表に併記された幾何平均値を割り直した比とは、丸めや解析方法によりわずかに異なる。

## AUCを合わせる式

線形PKの範囲で、投与量の変更倍率を \(d\)、同用量での親薬物AUC比を \(R_P\)、M2のAUC比を \(R_M\) とする。併用時の曝露を非併用時に対して表すと、

\[
E_P(d)=dR_P,\qquad E_M(d)=dR_M.
\]

ここでの厳密な一致は集計された親薬物AUC比についての条件であり、全参加者の曝露を個別に一致させることではない。親薬物を合わせる条件は \(dR_P=1\) なので、

\[
d=\frac{1}{R_P},\qquad E_M=\frac{R_M}{R_P}.
\]

この計算では、用量変更によってDDI比そのものが変わらず、用量とAUCが比例すると仮定する。原著が用量比例性に言及する範囲は100–800 mg QDと300–600 mg BIDであり、計算上の92.3 mgはその下限を下回る。300 mgより低い用量でこの仮定を当該DDI試験が直接検証したわけではない。定常状態への適用も、この単回投与試験では検証されていない。

## 親薬物を合わせた後に残る違い

`analysis/run.py`が出力した結果を示す。

| 計算項目 | 結果 |
| --- | ---: |
| 親薬物AUCを合わせる用量倍率 | 0.3077 |
| 300 mgに倍率を掛けた算術上の量 | 92.3 mg |
| 調整後の親薬物AUC比 | 1.000 |
| 調整後のM2 AUC比 | 0.1138 |
| 調整後のM3 AUC比 | 1.0062 |

![Observed exposure ratios and arithmetic parent-matched ratios](shared/savolitinib-parent-metabolite-ddi/figures/exposure-matching.svg)

図の青は公開試験の同用量AUCinf比、橙は用量比例を仮定した計算値である。青のエラーバーは原著の周辺90% CIであり、橙へ伝播させた区間ではない。橙は観測値ではない。92.3 mgは市販製剤や推奨レジメンを表さない。

親薬物とM2を同時に基準値へ戻すには、\(dR_P=dR_M=1\) が必要になる。従って、単一の用量倍率で両方を完全に合わせられるのは \(R_P=R_M\) の場合だけである。今回は逆方向の変化なので、この条件を満たさない。

M2の90% CI下端を親薬物の上端で割る場合と、その逆の組合せも計算した。結果は0.0897–0.1429だった。ただし、これは**周辺CIの端を組み合わせた感度範囲**であり、調整後M2比の90% CIではない。比の正式なCIには、推定された対数治療コントラスト間の共分散 Cov(log R_M, log R_P) が必要だが、公表されていない。また、個人別予測区間には個体レベルの親薬物・M2の同時分布が別途必要になる。

## 親薬物とM2を足す前に必要な情報

M2は活性を持つが、ng·h/mLのAUCをそのまま親薬物へ加えると、分子量、非結合率、相対効力、作用部位の違いが抜け落ちる。原著はM2の相対的に低い効力に言及しているが、それだけではヒトでの作用寄与率は決まらない。

そこで、基準状態の重み付き曝露に占めるM2の寄与を未知の \(f\) と置く。これは推定値でも患者の割合でもない。I(f)は幾何平均の集計比から構成する例示的な指標であり、個人ごとの親薬物とM2の合計の平均や患者別予測ではない。親薬物AUCを合わせた後の正規化指標は、

\[
I(f)=(1-f)+f\frac{R_M}{R_P}.
\]

![Sensitivity of a normalized exposure index to an assumed M2 contribution](shared/savolitinib-parent-metabolite-ddi/figures/weight-sensitivity.svg)

例えば \(f=0.10\) なら指標は0.911、\(f=0.25\) なら0.778となる。横軸全体は仮定の感度分析であり、M2が実際に25%寄与するという主張ではない。M2の寄与が小さければ影響は小さく、大きければ親薬物だけを合わせる操作と総寄与を合わせる操作の差が広がる。この式から奏効率や毒性発現率は計算できない。

## CLとFを分けて推定しない理由

経口投与では、

\[
\mathrm{AUC}=\frac{FD}{CL},\qquad
R_P=\frac{F_1/F_0}{CL_1/CL_0}.
\]

AUC比3.25を説明する組合せは一つではない。例えばFが変わらずCLが0.3077倍になる場合と、Fが2倍でCLが0.6154倍になる場合は、同じAUC比を与える。後者も基準Fを十分低く置けば数学的に成立する。これは実際のFを推定した結果ではない。

実際、原著の親薬物の終末半減期は8.9 hから8.0 hであり、AUCの約3倍という変化と平行には動いていない。CL/Fは54.0から16.6 L/h、Vz/Fは693.1から191.6 Lと記載されている（[Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC13598373/)）。CL/Fの変化を全身クリアランスCLだけの変化としてモデルへ入れると、この区別が失われる。

同じ理由で、親薬物と代謝物の少数の集計指標に形成・消失速度を無理に当てはめなかった。今回の代数モデルは機序を同定しない代わりに、機序を一意に決めなくても計算できる曝露の関係に限定している。

## この計算から言えること

親薬物のAUCを合わせる操作は、M2のAUCを合わせる操作と等価ではない。この差は公開されたDDI比だけでも定量化できる。一方、それが臨床的に重要な差かを判断するには、M2の非結合曝露と作用寄与、患者での反復投与PK、曝露と薬効・有害事象の関係が必要になる。

原著は添付文書に基づく用量低減にも言及している。本稿の算術計算はその推奨を置き換えず、妥当性を検証したものでもない。独立した研究上の結果は、用量低減の是非ではなく、**親薬物の曝露をそろえた比較でも代謝物の曝露差が残る**という点にある。

## 再実行

Python 3.12、NumPy、pandas、Matplotlibを使用した。`python analysis/run.py`で図2点、表3点と`outputs/results.json`を生成する。`python -m unittest discover -s tests -v`で4件の検査を実行できる。入力は引用した集計比であり、元論文全文や個人データを配布物へ含めない。

[再実行コード・図表・集計値](shared/savolitinib-parent-metabolite-ddi/savolitinib-parent-metabolite-ddi-analysis.zip)をダウンロードできる。

## References

Miah K, Reddy J, Sharma P, et al. Evaluating the Impact of CYP1A2 Inhibition on the Pharmacokinetics of Savolitinib: A Phase 1 Open-Label Study. *Pharmacology Research & Perspectives*. 2026;14(5):e70321. [doi:10.1002/prp2.70321](https://doi.org/10.1002/prp2.70321). Table 2 and study methods; accessed October 30, 2026.

## Cite this article

Kumakura D. Matching savolitinib AUC does not restore metabolite exposure. Personal research article. 2026. [Canonical article](https://daikikumakura.github.io/writing/savolitinib-parent-metabolite-ddi.html). Calculations and limitations are independent of the source study.
