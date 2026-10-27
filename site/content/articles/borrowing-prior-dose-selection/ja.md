## 要旨 {#article-abstract}

公開されたsotorasibとifinatamab deruxtecanの群別用量比較を、仮想新薬の2用量選択へ頑健な混合事前分布として借用し、借用の強さと選択の正しさをシミュレーションした。新薬が既存薬と同等なら正選択率は6〜10ポイント改善したが、期待後悔の改善は約1ポイントだった。逆方向の用量が有利な条件では、全量借用で正選択率が28〜42%へ下がった。1群40例では事後混合重みの調整だけでこの誤りを防げなかった。定めた効用と許容損失のもとで、主条件は借用重み0.5まで、全感度条件では0.25が許容された。これは仮想条件内の結果で、一般的な借用基準や新薬の推奨用量ではない。

<span id="_1"></span>

## 背景と目的 {#revision-015-section-1}

解析の問い（question of interest、QoI）は、 新薬の用量選択試験で、同じクラスの既存薬の用量比較を事前分布として借りると、用量選択はどれだけ正しくなり、新薬が違うときにどれだけ誤るか。

利用範囲（context of use、CoU）は、 新薬の用量最適化試験を計画するとき、既存薬の情報をどの程度借りてよいかと、新薬固有に必要なデータを議論する材料。既存薬の効果を新薬の予測値にはしない。特定の新薬の用量は推奨しない。

頑健な混合事前分布は、既存情報を表す成分と弱い情報の成分を混ぜ、データとの不一致に応じて成分の事後重みが変わるという考え方を使う ([1](#ref-1))。本解析は1つの先行薬の群別事後分布を成分としたもので、複数研究のメタ解析そのものではない。

<span id="_2"></span>

## 方法 {#revision-015-section-2}

### 公開データと効用 {#data-and-utility}

Sotorasibの集計は申請者の公開資料、ifinatamab deruxtecanの集計はIDeate-Lung01の中間解析と同じ時点の企業公表資料から取得した ([2](#ref-2), [3](#ref-3), [4](#ref-4))。表1に入力値を示す。

**表1　既存薬の群別集計**

| 既存薬 | 低用量：奏効 / 重い有害事象 | 高用量：奏効 / 重い有害事象 | 観測が有利とする用量 |
| --- | --- | --- | --- |
| sotorasib 240 / 960 mg | 26/105、20/104 | 34/104、37/104 | 低用量 |
| ifinatamab deruxtecan 8 / 12 mg/kg | 12/46、20/46 | 23/42、21/42 | 高用量 |

重い有害事象は、sotorasibではGrade≥3の治療関連有害事象、ifinatamab deruxtecanではGrade≥3の有害事象。よい用量は、効用 U = 奏効率 − 重い有害事象の率が大きい方とした（奏効1件と重い有害事象1件を同じ重さで見る。sotorasibの用量比較の記事 ([5](#ref-5))の主解析と同じ）。

### 新薬の仮想試験と事前分布 {#trial-and-prior}

 低・高の2用量に、1群40例を無作為に割り付ける。
- 各群の奏効率と有害事象の率に、次の混合事前分布を置いた。
  ω × Beta(a_H, b_H) + (1 − ω) × Beta(1, 1)。既存薬の各群・各評価項目の件数x_H、総数n_Hからa_H=x_H+1、b_H=n_H−x_H+1とした。
- ω は借用の重みで、0（借りない）から1（全量）まで。
- 混合事前分布は、データが既存薬と食い違うと、既存薬の成分の事後重みを下げうる（頑健な事前分布）。
- 効用の事後平均が大きい用量を選ぶ。各条件5,000試験。

### 真値のシナリオ {#truth-scenarios}
- **S0：** 既存薬と同等（既存薬の事後分布から引く）。
- **S1：** 高用量で奏効が増えない。
- **S2：** 既存薬の事後分布から引いた高用量の奏効率に0.15を加える。
- **S3：** 高用量で有害事象が増えない。
- **S4：** 同様に引いた高用量の有害事象率に0.15を加える。

S2・S4は確率を0〜0.99へ制限した。

**15ポイントにした理由：** 既存薬で観測された低・高用量の差と同じ桁にした。
- sotorasibの差：奏効 +7.9ポイント、重い有害事象 +16.3ポイント。
- ifinatamab deruxtecanの差：奏効 +28.7ポイント、重い有害事象 +6.5ポイント。

同じクラスの新薬でも用量効果がこの程度異なると仮定したもので、その差の頻度を実薬から推定したわけではない。S1とS3は、差がなくなる極端な場合として置いた。

<span id="_3"></span>

## 結果 {#revision-015-section-3}

![借用の重みと期待後悔の変化](shared/borrowing-prior-dose-selection/figures/01-regret-change.png)

**図1　**借用なしを基準とする期待後悔の変化。仮想シナリオごとに5,000試験を生成した。

図1は期待後悔（真の最良用量と選んだ用量の効用の差）の、借用しない場合からの変化を示す。図2と表2は正選択率を示す。

- **新薬が同等（S0）：** 全量借りても改善は約1ポイントだった。
- **新薬が既存薬と逆の用量を有利にする場合：** 全量の借用で3.5〜4.3ポイント悪化した。sotorasibではS2・S3、ifinatamab deruxtecanではS1が該当する。
- **既存薬と同じ向きのシナリオ：** 借用すると改善した。

![借用の重みと正選択率](shared/borrowing-prior-dose-selection/figures/02-correct-selection.png)

**図2　**仮想真値のもとで効用が最大となる用量を選んだ割合。臨床試験で検証された正選択率ではない。

**表2　正選択率の比較**

| | 借用なし | 全量借用 |
| --- | ---: | ---: |
| sotorasibを借用、新薬が同等 | 73% | 83% |
| sotorasibを借用、新薬で高用量の害が増えない（S3） | 71% | 28% |
| ifinatamab deruxtecanを借用、新薬が同等 | 87% | 93% |
| ifinatamab deruxtecanを借用、新薬で高用量の奏効が増えない（S1） | 72% | 42% |

### 事後混合重みと不一致 {#posterior-mixture-weight}

 頑健な混合事前分布なら、新薬のデータが既存薬と違えば既存薬の成分の重みが下がるはずである。しかし ω = 0.5 のとき、既存薬の成分の事後重みは次のとおりだった。
- 同等のシナリオ：0.70〜0.74。
- 逆向きのシナリオ：0.58〜0.67。

検討した1群40例の条件では、15ポイント程度の不一致に対する重みの調整は十分でなかった。「混合事前分布にしておけば、違ったときに自動で守られる」とは言えない。

<span id="_4"></span>

### 許容損失による借用範囲 {#revision-015-section-4}

表3では、事前に決めた規則（同等のときに改善し、どのシナリオでも悪化が1ポイント以下）で、許容できる ω を調べた。

**表3　各感度条件で許容された最大借用重み**

| 条件 | sotorasibを借用 | ifinatamab deruxtecanを借用 |
| --- | --- | --- |
| 主解析（1群40例） | 0.5まで | 0.5まで |
| 1群25例 | 0.5まで | 0.5まで |
| 1群60例 | 0.5まで | 0.75まで |
| 既存薬の有効標本数を50に縮める | 0.75まで | 0.5まで |
| 害の重みを2倍 | 0.25まで | 0.5まで |

全量の借用（ω = 1）は、どの条件でも許容できなかった。すべての条件で許容できたのは ω = 0.25 だけだった。

<span id="_6"></span>

### 実装の検証 {#implementation-checks}

- **独立の再実装：** 混合事前分布の更新とシミュレーションを、別の言語（R）と別の乱数で書き直した。既存薬2つ × シナリオ2つ（同等、最も悪化するシナリオ）× 借用の重み3つ（0、0.5、1）で、正選択率と期待後悔が差をMonte Carlo標準誤差で標準化した検査値は|z| < 4だった。
- **事後重みの確かめ：** 混合事前分布の事後重みは、ベータ二項分布の式と一致することを、単体の検査で確かめた。
- **再現性：** 同じseedで再実行すると、結果ファイルがバイト単位で一致する。


<span id="_5"></span>

## 考察 {#revision-015-section-5}

本解析で定めた効用と悪化許容幅では、新薬自身の1群40例の比較を確保した主条件で借用重み0.5まで、全感度条件で0.25が許容された。これらは仮想シナリオ内の結果であり、一般的な借用重みや必要例数の基準ではない。そのうえで、既存薬で用量の結論を決めた評価項目について、新薬でも同じ向きになる根拠（曝露反応、標的の飽和、非臨床）を別に示す必要がある。その評価項目は、sotorasibでは害、ifinatamab deruxtecanでは奏効である。借用は、その根拠の代わりにはならない。

### 仮定と限界 {#assumptions-and-limits}
- 新薬のシナリオは仮想である。
- 既存薬と新薬で用量が対応する（同じ用量比で同じ位置にある）ことは仮定である。
- 群内の奏効と有害事象の相関、時間依存の害は扱っていない。
- 既存薬の効果を新薬の予測値にしていない。


## 結論 {#article-conclusion}

借用は新薬が既存薬と同等な場合の選択を改善したが、逆方向の用量効果がある場合には誤選択を増やした。頑健な混合事前分布も、検討した小標本で自動的な保護にはならなかった。許容重みは仮定した真値・効用・損失幅を条件とする。

## データとコードの公開状況 {#availability}

再実行：`python test_analysis.py && python analysis.py && python figures.py && Rscript validate.R`（Python 3.12、numpy、scipy、pandas、matplotlib；R 4.5.3、jsonlite）。

解析計画・コード・入力の群別集計・結果・検証結果は配布資料に含めた（[配布資料](shared/borrowing-prior-dose-selection/borrowing-prior-dose-selection-companion.zip)）

<span id="_7"></span>

## 参照 {#article-references}

1. <span id="ref-1"></span>Schmidli H, Gsteiger S, Roychoudhury S, O'Hagan A, Spiegelhalter D, Neuenschwander B. Robust meta-analytic-predictive priors in clinical trials with historical control information. Biometrics. 2014;70(4):1023–1032. [doi:10.1111/biom.12242](https://doi.org/10.1111/biom.12242).
2. <span id="ref-2"></span>Amgen Inc. Sotorasib: Background Information for the Oncologic Drugs Advisory Committee, 05 October 2023 [Internet; sponsor briefing document]. 2023 Sep 5. [Tables 20 and 29](https://www.fda.gov/media/172698/download).
3. <span id="ref-3"></span>Rudin CM, Ahn MJ, Johnson M, Hann CL, Girard N, Nishio M, et al. OA04.03 Ifinatamab deruxtecan (I-DXd) in extensive-stage small cell lung cancer (ES-SCLC): interim analysis of IDeate-Lung01 [Conference abstract]. J Thorac Oncol. 2024;19(10):S15–S16. [doi:10.1016/j.jtho.2024.09.033](https://doi.org/10.1016/j.jtho.2024.09.033).
4. <span id="ref-4"></span>Merck & Co., Inc. Ifinatamab deruxtecan continues to demonstrate promising objective response rates in patients with extensive-stage small cell lung cancer in IDeate-Lung01 phase 2 trial [Internet; company announcement]. 2024 Sep 7 [cited 2026 Oct 28]. [Interim results](https://www.merck.com/news/ifinatamab-deruxtecan-continues-to-demonstrate-promising-objective-response-rates-in-patients-with-extensive-stage-small-cell-lung-cancer-in-ideate-lung01-phase-2-trial/). The arm-level counts used here correspond to the 2024 Apr 25 data cutoff.
5. <span id="ref-5"></span>Kumakura D. How far does a dose-comparison trial support dose selection? Arm-level data for sotorasib 960 mg and 240 mg [Internet; technical note]. 2026 Oct 14. [Earlier benefit–risk analysis](https://daikikumakura.github.io/writing/sotorasib-dose-comparison-en.html).
