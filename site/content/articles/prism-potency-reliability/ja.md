公開スクリーニングのEC50は、薬剤と細胞株を絞る入口になる。しかし、数値が表にあることと、その値の近くを追試すればよいことは別である。濃度反応の中点が測定範囲にあるか、反復が残っているか、別screenでも曲線が保たれるかを確認する必要がある。

本記事ではPRISMの公式19Q4データから、事前に選んだ3薬・肺由来6細胞株を再解析した。30組のうち1組は全欠測、残る29曲線では12曲線のEC50 profileが探索範囲の端まで閉じなかった。**この12曲線では、点推定を精密な感受性の順位や追加濃度の根拠として扱えない。** 一方、erlotinib–HCC827のようにtechnical redoでも遷移が保たれる例もあった。目的はPRISM全体の良し悪しを判定することではなく、次に何を測るべきかを曲線ごとに分けることである。

## 問いと使用範囲

QOIは「公開EC50を次の濃度・再実験の選択に使えるか、その判断を変えるのは何か」とする。COUは非臨床の追試設計に限る。患者のPKを推定した解析ではなく、細胞株の結果から臨床用量や治療選択は決めない。モデルの判断への影響は低い。誤ったEC50の採用は、不適切な濃度に追試を集中させる危険がある。

## データ：未集約でも「生データ」ではない

PRISMは細胞株を混合し、barcodeを通じて薬剤処理後の相対的なviabilityを測るスクリーニングである。[1] 公式19Q4 version 4を利用した。Figshare上のライセンスはCC BY 4.0であり、出典を明示する。[2]

読込前に、肺由来・STR確認済みの細胞株をDepMap ID昇順で6株選び、erlotinib、palbociclib、doxorubicinを固定した。薬剤反応や遺伝子変異で選んでいない。ただし、この小さな便宜的対象はPRISM全体を代表しない。

| 項目 | 今回の実体 |
| --- | --- |
| 対象 | HCC827、NCIH1581、NCIH1693、PC14、NCIH1650、RERFLCMS |
| 濃度 | 約0.00061〜10 µM、8濃度、約4倍希釈 |
| 候補測定値 | 720 |
| 有限な観測値 | 528（192欠測） |
| 評価できた曲線 | 29／予定30組 |
| 同じ薬・株のscreen比較 | 11組 |

入力はreplicate未集約のlog2 fold changeであるが、すでにQC・対照正規化・ComBat補正を受けている。[2, 3] 生の蛍光測定値ではない。検出plateによって残る測定が異なり、最大3plateが残る曲線と1plateしかない曲線を同列の独立反復数として数えない。

erlotinibとpalbociclibにはHTS002とMTS010の両方がある。READMEはMTS010をtechnical redoと記載し、利用可能なら優先するよう勧めている。[2] したがって、両screenの比較を独立した生物学的追試や外部検証とは呼ばない。

## 方法：EC50の値より、どこまで決まるかを見る

相対viabilityを $v=2^{\mathrm{log2FC}}$ とし、クリッピングせずに次を推定した。

$$
v(c)=L+\frac{U-L}{1+(c/EC_{50})^h}+b_{plate}
$$

$L,U$ は高濃度・低濃度側の漸近値、$h$ はHill slopeである。$b_{plate}$ はscreen内の平均が0になるplate offsetとした。少数plateから集団分散を推定する混合効果モデルではない。$0\le L\le U\le2.5$、$L\le1.5$、$0.1\le h\le5$とし、EC50の探索を測定範囲の両側3桁まで延ばした。複数の開始点で残差平方和を最小化した。

**EC50は上下の漸近値の中点であり、viabilityが0.5になるIC50とは異なる。** $L>0.5$なら、EC50が有限でも絶対50%阻害濃度はこのモデル上存在しない。

次にEC50を固定し、残りのパラメータを再推定するprofileを計算した。全域101点に推定値近傍81点を追加し、各点を4開始点で最適化した。残差増加をF分布に基づく95%相当の基準と比べた。これは補正済み技術反復、独立残差、指定曲線を条件とした**近似的な許容範囲**であり、独立した実験の95%信頼区間ではない。境界制約や補正後の相関もあるため、coverageを保証しない。

## 結果

### 遷移を観測している曲線と、数値だけが出る曲線

![反復未集約の観測値と再推定曲線。点は技術測定、線はplate offsetを除いた共通曲線。](shared/prism-potency-reliability/figures/fig1_observed_curves.png)

**図1：** 左のerlotinib–HCC827は両screenで濃度依存的な低下が見える。中央のNCIH1581では反応がばらつき、曲線の遷移を決めにくい。右のpalbociclib–HCC827では、HTS002の遷移に対してMTS010の点が大きく散らばる。凡例のnは有限な技術測定値の数であり、独立実験数ではない。

| 曲線 | EC50点推定（µM） | 条件付きprofileの許容範囲（µM） | 読み方 |
| --- | ---: | --- | --- |
| erlotinib–HCC827、HTS002 | 0.0148 | 0.00768〜0.0241 | 遷移付近を追加測定する根拠になる |
| erlotinib–HCC827、MTS010 | 0.0164 | 0.00879〜0.0362 | technical redoでも近い遷移 |
| erlotinib–NCIH1581、HTS002 | 0.00237 | 探索境界まで開放 | 点推定で濃度を決めない |
| erlotinib–NCIH1581、MTS010 | 11.4 | 探索境界まで開放 | 範囲外のEC50として確定しない |
| palbociclib–HCC827、HTS002 | 0.449 | 0.297〜0.656 | このscreen条件での推定 |
| palbociclib–HCC827、MTS010 | 15.8 | 探索境界まで開放 | 元screenの値を精密な値として移さない |

29曲線で最適化は収束したが、12曲線のprofileが探索境界まで開放し、7曲線の点推定は測定範囲外だった。17曲線では漸近値またはslopeが設定した境界に接し、7曲線は1plateしか残っていない。**収束したことだけでは、EC50がデータから識別されるとは言えない。** また、閉じたprofileでも1plateだけから推定されたものがあり、狭い許容範囲を独立再現性の証拠とはしない。

### 点推定の変化と、推定できないことを分ける

![EC50を固定した残差profile。緑は測定濃度範囲、破線1は条件付き残差の許容基準。](shared/prism-potency-reliability/figures/fig2_ec50_profiles.png)

**図2：** HCC827のerlotinibでは許容されるEC50が限定される。一方、中央の平坦なprofileでは、非常に異なるEC50でも同程度に観測値を説明できる。グラフの縦軸は表示を0〜2に限定しているが、判定は保存した全profile値で行った。

同じ薬・株を比較できた11組のうち10組では、screen間のEC50点推定が4倍を超えて動いた。ただし、未識別のEC50も含むため「感受性が4倍変わった」とは解釈しない。閉じたprofileが両screenにあるのは3組に限られ、その範囲でも条件付き推定の違いと技術的再現性の問題は残る。

公式処理済みパラメータと結合できた27曲線も比較した。今回の制約、plate offset、最適化によって点推定は変わるため、公式EC50をそのまま再現した解析ではない。同じ観測源からの再処理比較であり、独立検証ではない。重要なのは、どちらの表が正しいと宣言することではなく、点推定・profile・反復構造を一緒に保存することである。

## 次に何を測るか

![推定曲線のlog10 EC50に対する局所感度。上下漸近値とHill slopeを固定した条件付き計算。](shared/prism-potency-reliability/figures/fig3_conditional_sensitivity.png)

**図3：** 他のパラメータが既知なら、EC50付近の濃度はその変化に敏感である。しかし、漸近値やslopeも不確かな曲線では、この局所感度の最大点を「最適な次濃度」と呼べない。

今回の結果から、追試を次のように分ける。

- **遷移が両screenで保たれる場合：** erlotinib–HCC827では、約0.01〜0.03 µM付近を含む追加濃度が条件付き候補になる。ただし、上下のplateauを確認する濃度と別実験の反復を残す。
- **profileが開放する場合：** 大きなEC50点推定から自動的に高濃度へ延ばさず、まず元の範囲で独立再実験し、対照・反応の方向・漸近値を確認する。再実験後に、溶解性や非特異的毒性も踏まえて拡張を判断する。
- **1plateしか残らない場合：** 条件付きprofileが狭くても、独立再実験の優先度を下げない。欠測が多いcurveは、精密そうなEC50を濃度選択の根拠にしない。

追加濃度を一つ選ぶだけでなく、「何を先に確認するべきか」を決めるのが、この解析の役割である。

## 限界と結論

対象は3薬・6株であり、PRISM全体の未識別率を推定する標本ではない。補正前のMFIからQC・ComBatを再実装しておらず、plate offsetだけでは処理の不確実性を復元できない。残差の独立性・等分散性、Hill曲線の妥当性も十分ではなく、profileを独立実験CIとして読むことはできない。培地中の遊離濃度、曝露時間差、患者PKへの変換も扱っていない。

公開EC50を追試設計へ使うには、**その曲線でどの濃度範囲が観測され、どの反復が残り、EC50がどこまで識別されるか**を確認する必要がある。安定した遷移の周辺へ濃度を増やす場合と、元の範囲から再測定する場合を分けられたことが、今回の実測データ解析の結論である。

数値は`analysis/02_analyze.py`の`curve_fits.csv`、`profiles.csv`、`audit.json`、`screen_comparison.csv`から取得した。図は`analysis/03_figures.py`で作成し、再実行手順とNotebookを保存した。

## 参考資料

1. Corsello SM et al. Discovering the anticancer potential of non-oncology drugs by systematic viability profiling. *Nature Cancer* 2020;1:235–248. [DOI:10.1038/s43018-019-0018-6](https://doi.org/10.1038/s43018-019-0018-6)。公開資料として[PRISM公式プロジェクトページ](https://depmap.org/repurposing/)を併用。
2. Broad DepMap et al. [PRISM Repurposing 19Q4 Dataset, version 4](https://figshare.com/articles/dataset/9393293/4)。使用ファイルのREADME・注釈・未集約LFC・公式curve parameters、CC BY 4.0。
3. Broad Institute. [PRISM secondary screen processing script](https://github.com/broadinstitute/repurposing/blob/master/secondary_processing_script.R)。処理手順の照合に使用。

## 解析関数と検査コード

[解析関数と単体検査のZIP](shared/prism-potency-reliability/prism-potency-reliability-functions.zip)を配布する。原データや解析全体の再実行資料は含まない。検査に使う構成例を、臨床データの検証とは扱わない。
