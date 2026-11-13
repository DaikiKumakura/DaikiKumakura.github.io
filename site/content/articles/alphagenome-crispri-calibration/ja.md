AlphaGenomeが実験結果と相関するとき、その出力を「RNAが何％下がるか」と読んでよいのか。この二つは、私には別の問いに見える。大きく下がる組を上に並べられても、40％の低下を10％と予測するなら、効果量を前提にした判断は変わってしまう。

そこで、公開されたCRISPR interference（CRISPRi）ベンチマークの予測CSVを再解析した。Gasperiniデータの共通352組では、AlphaGenomeのPearson相関は0.46だった。一方、未校正の効果量の二乗平均平方根誤差（root mean squared error; RMSE）は24.75ポイントで、評価対象の遺伝子を除いた平均値だけを返す基準の17.33ポイントより大きかった。相関があることと、出力をそのまま効果量として使えることは一致しなかった。

ただし、ここで「使えない」と切るのも早い。実験値から学習する一次式の校正を加え、校正の学習に使わなかった遺伝子で評価すると、RMSEは15.40ポイントになった。この記事では、その改善が何を意味し、どこから先を保証しないのかまで確かめる。

## 再解析する対象を絞る

出発点は、MurphyとKooによる技術記事と公開コードである。2026年11月4日更新の比較では、FulcoとGasperiniのK562細胞のCRISPRiデータを使い、AlphaGenome、Borzoi、Enformer、NTv3の予測を調べている。これは著者らの技術ブログ上の比較であり、査読済みの比較論文とは区別する [(1)](#ref-1)。本稿は公開された予測値の統計的な再解析で、ゲノムモデルの推論や細胞実験を独立に再実行したものではない [(2)](#ref-2)。

元の実験は、エンハンサーをCRISPRiで抑えたときの遺伝子発現を測っている [(3)](#ref-3) [(4)](#ref-4)。ただし、今回のCSVは候補全体ではない。Fulco側は検証済みで発現低下のある組、Gasperini側は有意かつ高信頼とされた組に選別されている。実際、使った観測値はすべて正の低下だった。したがって「モデルが選んだ候補は何割当たるか」は、このデータから答えられない。

解析単位はエンハンサーと遺伝子の組とした。4モデルに予測値がある組をgene_idとenh_locの二つのキーで一対一に結合し、観測値と距離の対応も確認した。表1に共通部分の規模を示す。

表1。モデル間で対応が確認できた組。

| Dataset | AlphaGenome published pairs | Common pairs | Common genes | Common enhancers |
| --- | ---: | ---: | ---: | ---: |
| Fulco | 63 | 62 | 20 | 51 |
| Gasperini | 438 | 352 | 256 | 340 |

共通部分にそろえると、モデルごとの評価対象の違いは減らせる。読み出す測定系やモデルの実装まで同じになるわけではない。Enformerは転写開始点近傍の発現を測るcap analysis of gene expression（CAGE）、ほかの選択ファイルはRNA-seqを使い、集約範囲も異なる。Borzoiは4モデルのアンサンブル、AlphaGenomeはコミュニティ実装の全fold蒸留チェックポイント、NTv3は新しい1 Mb版の公開予測である。今回は推論時に入力を変換して平均するtest-time augmentation（TTA）版を混ぜていない [(1)](#ref-1) [(2)](#ref-2)。

## 相関のある予測にも尺度のずれがある

観測する低下率を次のように置く。

$$
y_i=1-\frac{RNA_{\mathrm{perturbed},i}}{RNA_{\mathrm{control},i}}.
$$

公開CSVのy_deltaは、すでにこの向きの低下率になっている。再び1から引く処理はしない。モデル側の予測pは、元配列とエンハンサー部分をシャッフルした配列の予測差を、元配列の予測で割った値である。RNAの絶対量そのものではない。

誤差はRMSEで測った。

$$
\mathrm{RMSE}=\sqrt{\frac{1}{n}\sum_i(\hat y_i-y_i)^2}.
$$

RMSEは組ごとの誤差に同じ重みを付けるため、対応するエンハンサーの多い遺伝子ほど全体への寄与が大きい。以下では100倍して「ポイント」で示す。30％の低下を10％と予測したときの差は20ポイントであり、相対誤差20％ではない。

![Published AlphaGenome predictions and observed RNA decreases](shared/alphagenome-crispri-calibration/raw-calibration.png)

図1。公開CSVから作成した散布図。破線は予測と実測が等しい位置を表す。負の予測も除かずに描いた。色はエンハンサーと転写開始点（transcription start site; TSS）の距離である。元の比較の散布図は[技術記事のFigure 2](https://genomicsxai.github.io/blogs/2026-007/#results)を参照できる。本図はその転載ではなく、共通組から描き直した。

AlphaGenomeの平均予測と平均観測の差は、Fulcoで−12.63ポイント、Gasperiniで−12.58ポイントだった。もっとも、平均のずれだけでは全体は説明できない。Gasperiniでは、大きさのばらつきの対応も完全ではない。

Pearson相関は、予測に定数を足したり、正の定数を掛けたりしても変わらない。そのため「並び方をある程度捉えた」という結果は、原点や尺度まで合っている証拠にはならない。平均値だけの予測と効果量の誤差を比べるのは、この違いを見るためである。

## 校正を学習する遺伝子と評価する遺伝子を分ける

校正には、各データセットで次の一次式を使った。

$$
\hat y_i=a+b p_i.
$$

一つの遺伝子に複数のエンハンサーが対応するため、組をランダムに分割すると、同じ遺伝子の実験値が学習側と評価側に入る。今回は一つの遺伝子に属する組をまとめて外し、残りの遺伝子だけでaとbを最小二乗推定して、外した遺伝子を予測した。これを全遺伝子について繰り返した。評価に使ったのは、このleave-one-gene-out予測である。0から1への切り詰めはしていない。

比較する平均値も、外した遺伝子を含めずに求めた。距離だけで予測する基準にはlog10距離の一次式を同じ分割で使った。この校正は実験値を必要とする教師ありの補正であり、元モデルのzero-shot性能向上とは呼ばない。また、外したのは補正式の学習からであって、AlphaGenome本体の事前学習で未見の遺伝子だと確認したわけではない。

表2。未校正と校正後の誤差。ppはpercentage pointsを表す。

| Dataset | Pearson r, raw AlphaGenome | Raw RMSE (pp) | Calibrated RMSE (pp) | Held-out mean RMSE (pp) | Distance-only RMSE (pp) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Fulco | 0.67 | 18.54 | 14.89 | 18.77 | 17.88 |
| Gasperini | 0.46 | 24.75 | 15.40 | 17.33 | 17.38 |

表2のGasperiniでは、未校正の予測より平均値のほうが誤差は小さい。それでも、校正後の予測は平均値を上回った。ここには、単なる全体平均では回収できない予測情報が残っていたと読める。

不確実性は、遺伝子を単位に2,000回再標本化し、そのたびに校正も学び直して評価した。同じ再標本を各手法に使い、RMSEの差を対応させた。95％区間には再標本分布の2.5％点と97.5％点を使った。校正後から平均基準を引いた差は、Gasperiniで−1.93ポイント、95％区間は−2.83から−1.09ポイントだった。Fulcoは−3.88ポイントでも、区間は−9.40から+1.51ポイントと0をまたいだ。Fulcoは62組あっても遺伝子は20しかない。点推定だけで、こちらでも改善が確かだとは言わない。

![Uncalibrated and gene-held-out calibrated errors](shared/alphagenome-crispri-calibration/heldout-calibration.png)

図2。共通組における未校正と遺伝子を外した校正後のRMSE。縦線は遺伝子クラスターブートストラップの95％区間、破線は同じ分割の平均基準。棒の区間の重なりだけで手法差を判定せず、本文の対応差の区間を使う。

ほかのモデルも校正後には誤差が下がった。Fulcoの校正後RMSEはBorzoi14.56、Enformer15.39、NTv3 17.65ポイント、Gasperiniはそれぞれ16.33、16.61、16.50ポイントだった。校正前の相関だけでモデルを比較すると、こうした補正可能な尺度のずれを見落とす。ただし、実装、出力、アンサンブル、学習条件が異なる比較から、差の原因をアーキテクチャだけに帰すことはできない。

## 補正式を候補探索へ持ち出せない理由

何を直したのかを見るため、全データで一次式を当てはめると、Fulcoは概ねa=0.138、b=0.848、Gasperiniはa=0.254、b=0.351となった。これは説明用の全データ係数で、上の評価値は遺伝子ごとに学び直した式から計算している。

この係数は、予測を一律に大きくする補正ではない。正の切片を足し、予測の変動幅は縮めている。Gasperiniの説明用の式では、元の予測が0でも約25％の低下を返す。陽性と確認された組だけを見ていれば、それで平均的な誤差は減りうる。しかし、無関係なエンハンサーまで含む候補集合に持ち込んだらどうなるかは、ここでは測れていない。

この点は、実験設計で重要だと思う。「予測0.2の候補なら20％下がる」と読むためには、候補集合に合う校正データと、候補を選ぶ前の評価が要る。今回の結果は、その成功率を与えていない。効果のある組の中で量の対応を調べる問題と、効果のある組を発見する問題を分けておきたい。

## 変わらなかった結果と残る限界

同じエンハンサーが複数遺伝子に対応する場合もある。遺伝子とエンハンサーを結ぶグラフの連結成分を一つずつ評価用に除き、同じエンハンサーが校正と評価の両方に入らないようにした場合も、AlphaGenomeの校正後RMSEはFulco14.86、Gasperini15.40ポイントで、主解析に近かった。元のAlphaGenomeの全組を使った感度解析では、それぞれ14.78、15.55ポイントだった。評価対象を変えても結論の方向は保たれたが、共通組以外を含む数字を、ほかのモデルとの直接比較には使わない。

予測対象と実験介入の違いも残る。公開ベンチマークは2 kbの配列を二塩基頻度を保ってシャッフルする。一方、CRISPRiはdCas9-KRABなどで抑制を誘導し、DNA配列をそのように置換しない。この差を含めて誤差を見ているので、ずれの全量をゲノムモデルの失敗と断定できない [(1)](#ref-1) [(2)](#ref-2)。

さらに、両実験ともK562であり、別の細胞や患者への汎化は検証していない。集約済みの実験効果量を観測値として扱い、実験の反復測定誤差と真の効果を分離していない。遺伝子単位の区間はこの測定誤差を完全に表すものではない。また、遺伝子間を独立とみなす再標本化なので、共有エンハンサーや実験全体の依存も完全には扱わない。連結成分を外す感度解析は、この区間自体を修正するものではない。今回の校正法と比較は探索的に選んだもので、事前登録した検証ではない。

Gasperiniの相関には、効果量の推定にも利用できる情報が残っていた。実験値を使った校正後には平均基準より誤差が小さかった。その一方で、未校正の出力を効果量そのものと読むと、相関0.46という印象から受け取るより誤差が大きい。実験候補を並べる用途と、低下率を計算へ代入する用途では、求める検証が違う。

## データとコードの公開状況

元の予測CSVは[固定コミットの公開リポジトリ](https://github.com/Al-Murphy/seq2func_crispri_eval/tree/b4917f5b1a5ccdac8800d00ed31f65cfcb483093)から取得した。コードと取得マニフェストはSHA256で入力を照合する。乱数seedはFulcoが20261110、Gasperiniが20261111、再標本化は各2,000回である。[再解析コード](shared/alphagenome-crispri-calibration/analysis.py)、[集計結果](shared/alphagenome-crispri-calibration/results.json)、[再現手順](shared/alphagenome-crispri-calibration/analysis-readme.md)を公開する。

[コード・結果・図のZIP](shared/alphagenome-crispri-calibration/alphagenome-crispri-calibration.zip)

## 参照

<a id="ref-1"></a>
1. Murphy A, Koo PK. Benchmarking seq2func models on distal enhancer effects with CRISPRi screens. Genomics x AI. Published June 25, 2026; updated November 4, 2026. [Article](https://genomicsxai.github.io/blogs/2026-007/).

<a id="ref-2"></a>
2. Murphy A. seq2func_crispri_eval. GitHub repository. Snapshot b4917f5b1a5ccdac8800d00ed31f65cfcb483093. [Code and prediction tables](https://github.com/Al-Murphy/seq2func_crispri_eval/tree/b4917f5b1a5ccdac8800d00ed31f65cfcb483093).

<a id="ref-3"></a>
3. Fulco CP, Nasser J, Jones TR, Munson G, Bergman DT, Subramanian V, et al. Activity-by-contact model of enhancer–promoter regulation from thousands of CRISPR perturbations. Nature Genetics. 2019;51:1664–1669. [doi:10.1038/s41588-019-0538-0](https://doi.org/10.1038/s41588-019-0538-0).

<a id="ref-4"></a>
4. Gasperini M, Hill AJ, McFaline-Figueroa JL, Martin B, Kim S, Zhang MD, et al. A Genome-wide Framework for Mapping Gene Regulation via Cellular Genetic Screens. Cell. 2019;176(1–2):377–390.e19. [doi:10.1016/j.cell.2018.11.029](https://doi.org/10.1016/j.cell.2018.11.029).
