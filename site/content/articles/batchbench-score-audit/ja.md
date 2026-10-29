正解率が17.5%から24.4%へ上がった。細胞画像を読むAIで、撮像条件の違いに対応できたらしい。ここだけなら、よいニュースに見える。

けれど、その約6.9ポイントは、どの薬の画像で稼いだのだろう。

2026年10月21日に公開された未査読論文BatchBench ([1](#ref-1))は、異なる施設で撮ったCell Painting画像から、投与された化合物を当てるベンチマークだ。原著の成績表を読み、公開ラベルとメタデータ95,215行を照合した。丸め済みの群別成績から再構成すると、単純な適応手法AdaBNの改善の約94.5%は、8種類の陽性対照薬の画像に由来した。原著も、総合値がこれらの画像に支配されると述べて群別成績を併記している ([1](#ref-1))。ここでの計算はその寄与を数にしたもので、誤りの指摘ではない。総合正解率の改善と、これから調べたい薬を見分ける力の改善は、別々の主張である。

## 未知の施設へ持っていく {#_1}

Cell Paintingでは細胞内の構造を染め、形や染色の変化から薬剤応答を読む ([2](#ref-2))。大量の画像があれば、AIに薬の違いを覚えさせたくなる。ただ、画像には細胞の応答だけでなく、顕微鏡、染色、プレート、実験日の違いも映る。JUMP Cell Paintingは13の施設が異なる顕微鏡と手順で撮像した大規模な公開データで ([1](#ref-1), [3](#ref-3))、施設や装置をまたぐと、このバッチ効果が画像ベースのプロファイルの統合を妨げることが指摘されている ([4](#ref-4))。

BatchBenchは、この厄介さを評価の中心に置いた。JUMP Cell Paintingから頻度の高い2,000化合物を選び、ウェルごとに1視野を採用する。入力は5チャンネルの画像。課題は、その細胞に何の化合物が加えられたかを2,000クラスから選ぶことだ ([1](#ref-1))。

公開側の9施設のうち8施設が訓練、source 2が検証。テストは別の4施設で行い、テスト画像は未知のバッチと未知のプレートにも由来する ([1](#ref-1))。つまり、同じ施設の画像をランダムに分けて測る正解率とは違う。私は公開ラベル・施設情報を再集計し、訓練81,880画像、検証13,335画像、訓練側2,000クラス、検証側1,877クラスを確認した ([5](#ref-5))。検証だけに現れる化合物はなかった。

未知なのはデータを作った施設であり、未知化合物の薬効を予測する課題ではない。化合物名を画像から当てることと、標的、作用機序、患者での有効性を当てることも分けておきたい。

テスト画像を使うこと自体が、すべて禁止されているわけでもない。ラベルを隠した画像を使い、推論時にモデルを適応させるtest-time adaptationは許される。AdaBNは、そのプレートの画像からBatchNormの統計量を計算し直す。正解ラベルを見せずに、画像の分布へ合わせる方法だ ([1](#ref-1), [6](#ref-6))。一方、非公開の4施設を訓練、事前学習、モデル選択に使うことは禁止されている ([1](#ref-1))。ここでは[公式ベースライン実装](https://github.com/ml-jku/batchbench-baselines/tree/df18b76bbf6233a0a8bdb423801c5353e613078f)も確認した ([7](#ref-7))。

## 対象と確認範囲 {#scope}

読んだのはBatchBench v1の全文HTMLで、本文と表1・表2を計算に使った ([1](#ref-1))。群別の成績は、表2に印刷された3桁の平均と標本標準偏差（乱数シード3回）だけであり、シードごとの予測も画像も持っていない。公開メタデータは行数・施設・群・ラベルの集計に使った ([5](#ref-5))。リーダーボード側の掲載値は使っていない。BatchBench以外の文献は、書誌情報と抄録の範囲で背景として引いており、本文の詳細な結果を再検討したものではない。

## 8種類の対照薬がテスト画像の36%を占める {#836}

成績は三つの画像群に分かれる。POSCONは8種類の陽性対照薬で、全プレートに置かれ、通常は固定位置にある。多くの訓練画像があり、強い形態変化を示す。TARGETは標的や作用機序を広く含む参照コレクションに由来する293化合物。RESTはそれ以外の画像で、公開側では1化合物あたり約12画像と少ない ([1](#ref-1))。

[原著のTable 1](https://arxiv.org/html/2610.30104v1)の画像数から比率を計算した。

表1。公開画像と非公開テスト画像の群別構成。

| 画像群 | 公開側の画像数 | 公開側の比率 | 非公開テストの比率 |
| --- | ---: | ---: | ---: |
| POSCON | 48,574 | 51.0% | 36.2% |
| TARGET | 23,455 | 24.6% | 54.9% |
| REST | 23,186 | 24.4% | 8.9% |

非公開テストの画像数は、原著のTable 1の合計で46,150（POSCON 16,691、TARGET 25,352、REST 4,107）になる。RESTは1,864化合物に対して4,107画像、平均2.2画像しかない。公開側と非公開テストで画像群の構成が違うこと（ラベルシフト）は原著が設計として明記しており、共変量シフトとラベルシフトが重なる条件ではTTA手法が劣化し得るとされる ([1](#ref-1))。Zhaoらも、TTAの有効性は分布シフトの種類で大きく変わり、一部のシフトでは既存手法が体系的に苦戦すると報告している ([8](#ref-8))。

総合正解率は、各画像群の正解率を、その画像数で重み付けした平均になる。薬剤一つずつに同じ重みを与えた成績ではない。画像単位で数える平均は多数派のクラスに引かれ、クラスごとの平均（macro平均）とは性質の違う指標である ([9](#ref-9))。POSCONとTARGETでテスト画像の91%を超えるため、総合値はこの二群に支配される。原著もこの点を明記している ([1](#ref-1))。対照薬が8種類でも、画像が多ければ総合値への影響は大きい。

やや紛らわしい点もあった。公開側の化合物数を群ごとに足すと、8＋293＋1,926で2,000を超える。公開メタデータをラベル単位で調べると、227化合物がTARGETとRESTの両方に現れていた。画像行は別々の群に属するが、群をまたいで同じ化合物が現れる。三群を「重複のない三つの化合物集合」と考えると、集計を間違える。

この照合には、200ピクセル版のCSVと500ピクセル版のNPZ・ラベル配列を使った。画像ID、施設、バッチ、プレート、群、ラベルの行順が一致し、画像IDの重複がないことも確認した。画像本体と非公開テストデータは取得していない ([5](#ref-5))。

## AdaBNの改善を分解する {#adabn}

[原著のTable 2](https://arxiv.org/html/2610.30104v1)には、乱数シードを変えた3回の実行の平均と標本標準偏差が載っている。ここでは平均値を使う。単位は正解率の%である。比較する手法は、適応なしのResNet18に加え、deepCORAL ([10](#ref-10))、AdaBN ([6](#ref-6))、TENT ([11](#ref-11))、ARM-BN ([12](#ref-12))などで、いずれもResNet18を土台にしている ([1](#ref-1))。下の表は5手法を示し、DANNとCS-ARM-BNは配布コードのみに収録した。2,000クラスを一様に無作為選択する場合の期待正解率は1/2,000で0.05%である ([1](#ref-1))。

表2。原著が報告した平均正解率（%）。

| 手法 | 総合 | POSCON | TARGET | REST |
| --- | ---: | ---: | ---: | ---: |
| 適応なしのResNet18 | 17.5 | 46.5 | 1.2 | 0.2 |
| deepCORAL | 20.1 | 50.2 | 3.4 | 0.7 |
| AdaBN | 24.4 | 64.6 | 1.9 | 0.2 |
| TENT | 24.9 | 66.1 | 1.7 | 0.2 |
| ARM-BN | 26.0 | 66.5 | 3.5 | 0.4 |

AdaBNは、適応なしに比べてPOSCONを18.1ポイント改善する。一方、TARGETは0.7ポイント、RESTは表示された桁では変わらない。この差にテスト画像の比率を掛けると、総合への寄与はPOSCONが約6.55ポイント、TARGETが約0.38ポイント、RESTが0ポイントになる。再構成した改善の約94.5%がPOSCONだ。これは寄与を会計的に割り振った数であり、POSCONの画像がなぜ改善したかを説明するものではない。

![画像群ごとの成績とAdaBN改善への寄与](shared/batchbench-score-audit/figures/subgroups-and-gain.png)

図1。左は[原著のTable 2](https://arxiv.org/html/2610.30104v1)の平均正解率。配布コードには表の全7手法を収録した。右はAdaBNと適応なしとの差を、非公開テストの画像数比で重み付けしたもの。丸め済みの平均からの記述的な計算であり、改善の有意性を検定した図ではない。

この分解は、モデルを再学習しなくてもできる。各群の成績を重み付けすると、7手法すべてで総合値と0.043ポイント未満の差に収まった。公表表の丸めと整合する範囲だ。

シード間のばらつきも確認した。標本標準偏差と3回という実行数だけを使い、手法間でシードは対応しないものとして、群別の差にWelchの方法 ([13](#ref-13))で粗い95%区間を付けた。POSCONの差18.1ポイントの区間は9.4–26.8ポイントで、適応なしの標準偏差が3.6ポイントと大きいため幅が広い。TARGETの差0.7ポイントは−0.4–1.8ポイントで、0を含む。RESTは差が0.0ポイントだった。総合の差6.9ポイントは3.5–10.4ポイントになる。これらは独立な正規分布の実行結果を仮定した参考計算である。実行数は3回で、標準偏差は丸められ、手法間の対応・共分散も不明である。この区間から、改善がPOSCONに限られるとも、TARGETの改善がないとも結論しない。

同じ分解を他の手法に当てると、改善の出どころが手法で異なる。適応なしからの改善のうちPOSCON由来の割合は、deepCORALで約52%、ARM-BNで約85%、AdaBNで約94.5%、TENTで約96%になる。deepCORALは総合の改善が2.6ポイントと小さいが、その約47%はTARGETの2.2ポイント（区間は約1.0–3.4ポイント）に由来する。TARGETの改善は、ARM-BNでも2.3ポイントあった。一方、TENTとAdaBNでは区間が0を含む。総合値が近い手法でも、改善した画像群は同じではない。

ただし、ここから「AdaBNは役に立たない」と結論するのも早計だ。POSCONの8化合物は強い表現型を示し、訓練画像も多い。バッチ効果のもとでその識別が上がったことは、適応が一定の効果を持つ証拠にはなる。問題は、何を改善した数字なのかを取り違えることだ。弱い応答や少数画像の化合物にも使えるようになった、とまではこの総合値から言えない。また、POSCONは全プレートに置かれ、通常は固定位置にあるため ([1](#ref-1))、POSCON正解率の上昇が形態の読み取りによるのか、プレートや位置に結びついた画像の癖によるのかは、本表からは区別できない。

## 薬の構成が変わると手法の選び方も変わる {#_2}

もう一つ、簡単な感度分析をした。各群の正解率は公表値に固定し、陽性対照画像の重みだけを変える。残りのTARGETとRESTの比は、非公開テストの比率に固定する。

これは、データ構成を変えてAIを実際に動かした実験ではない。重みの置き方で成績の読み方がどれだけ変わるかを見る計算だ。

陽性対照を集計から外すと、TARGETとRESTの画像数で重み付けした正解率は、AdaBNが約1.66%、deepCORALが約3.02%になる。元の総合成績ではAdaBNの方が高かったが、この集計では順序が逆になる。両者が交わる陽性対照画像の比率は、丸め値による計算で約8.6%だった。同じ粗い方法で、この二手法の差1.4ポイントの95%区間を計算すると0.2–2.5ポイントとなり、これは上記の仮定に依存する参考値であり、シード間変動を超えて順位が逆転すると確定したものではない。参考として、公開側の構成比（POSCON 51.0%）を当てた総合値は、適応なしが約24.1%、AdaBNが約33.5%になる。

![集計重みへの感度と公開施設ごとの画像構成](shared/batchbench-score-audit/figures/mixture-and-sources.png)

図2。左は群別正解率を固定した再重み付け。破線は非公開テストの陽性対照比率。右は公開メタデータを集計した施設ごとの画像構成で、source 2が検証施設。施設間の差は、撮像条件の違いだけでなく化合物構成の違いも含む。

8.6%を実運用の閾値として使うつもりはない。画像の構成が変われば、適応時に計算する統計量も変わり、群別正解率自体が動き得る。この計算はそこを固定している。シードごとの予測と共分散も持っていないので、群別成績の標準偏差を完全正相関として合成した。これは固定した周辺分散のもとで重み付き和の分散を最大化するが、手法間の共分散やWelch近似の自由度まで含む区間全体の保守性を保証しない。

この再集計から、原著の結果の読み方について次の三点が言える。第一に、総合正解率の順位は、評価に使う画像群の構成に依存する。順位の違いを手法の優劣として述べるなら、どの構成での優劣かを示す必要がある。第二に、ARM-BNとTENTの総合値の差1.1ポイントは、約86%がTARGET由来で、TARGETでの差1.8ポイント（区間0.7–2.9ポイント）による。POSCONでの差は0.4ポイント（区間−2.1–2.9ポイント）で、この近似区間は0を含む。総合値の小さな差を「同程度に改善した」と読むと、改善した画像群の違いを見落とす。第三に、原著が主要な未解決問題とする、少数画像かつ弱い表現型の化合物（TARGETとREST）の識別は、全手法で偶然水準（0.05%）より高いが、RESTでは最大でも0.7%にとどまる。RESTの0.2%は丸められた3実行の平均であり、4,107画像に掛けると、1実行あたり平均約6–10画像の正解に相当する。各実行で実際に正解した枚数ではない。一様無作為選択の期待値は約2画像だが、クラス頻度を利用する基準法との比較や有意差の検定ではない。陽性対照が多い測定系と、少数画像で弱い応答も比較する測定系では、重視すべき成績が異なる。

## バッチを消せば生物学だけが残るのか {#_3}

私は、バッチ補正を「技術的な差を引けば終わる処理」として置くのに少し抵抗がある。技術差と薬剤構成が結びついていれば、施設を見分けにくくする処理が、欲しい生物学的な差まで薄める可能性があるからだ。逆に、施設由来の情報を残したまま高い成績が出ても、そのまま次の実験へ移せるとは限らない。

BatchBenchは、施設をまたぐ評価、群別成績、ラベルを使わない適応を同じ枠に置くため、評価の枠組みとして使いやすい。同じく未知のバッチへの汎化を測るRxRx1は、遺伝子摂動を対象とし、バッチ補正手法を評価するための分類課題を提供する ([14](#ref-14))。BatchBenchは化合物を対象とし、群別成績と非公開テストを備える点で位置付けが異なる。ただし、両者の結果を直接比べたわけではなく、RxRx1の結果は抄録の範囲でしか確認していない。

BatchBenchの表だけでは、性能低下のうち何割が技術差で、何割が弱い表現型や画像数不足に由来するかを分離できない。陽性対照は訓練画像数、表現型の強さ、プレート上の配置も他の群と異なる。今回の再集計でも、それらの因果効果を切り分けたわけではない。

集約正解率はPOSCON・TARGET・RESTの構成にも依存する。各化合物を同じ重みで数えるmacro accuracyは、今回の表からは計算できない。施設をまたぐ成績の差を、薬剤群に依存しない一つの性能差として扱うことはできなかった。

## 結論 {#conclusion}

AdaBNによる総合正解率17.5%から24.4%への改善のうち、約94.5%は、非公開テスト画像の36.2%を占める8種類の陽性対照薬の画像で説明される。TARGET（293化合物）の改善は0.7ポイントで、仮定付きの近似区間は0を含み、RESTは表示された桁で変化がなかった。総合改善の大半は強い表現型の対照薬での成績に由来する。総合値だけでは、少数画像で弱い応答の化合物にも同程度の改善があったとは言えない。この結論は、丸めた3シード平均と、固定した群別正解率に基づく記述的な計算に依存する。非公開テストでのモデル再評価ではないため、画像群の構成が変わったときの実際の成績は推定していない。

## データとコードの公開状況 {#_4}

[解析コード・入力集計表・結果・図](shared/batchbench-score-audit/batchbench-score-audit.zip)を同梱した。`analysis.py`と`plot.py`で再重み付けと図を再生成できる。`fetch_data.py`と`extract.py`は、リビジョンを固定した公開メタデータを取得し、行対応・施設分割・化合物群の重なりを再確認するためのものだ。元のモデルコードは実行していない。

シード間の粗い区間と、手法別の寄与割合は、[追加計算コード](shared/batchbench-score-audit/extra-score-checks.py)で計算した（`numpy`と`scipy`を使用）。入力は表2の平均と標本標準偏差のみで、`python extra-score-checks.py`で実行できる。元の配布ZIPとは別に提供する。

成績は[原著v1のTable 2](https://arxiv.org/html/2610.30104v1)に固定した。掲載先Spaceの取得時の結果JSONにはexampleのURLを含むサンプル様式の行があり、原著の成績とは対応しなかったため、最新の実測順位として引用していない。ここで示したのは公表値の再集計であり、非公開テストでのモデル再評価ではない。確認日は2026年10月24日。補助計算と原著全文の再確認は2026年10月29日。

## 参照

1. <span id="ref-1"></span> Topf S, Sanchez-Fernandez A, Klambauer G. [BatchBench: Benchmarking AI Robustness to Batch Effects and Domain Shift in Biomedical Images](https://arxiv.org/abs/2610.30104v1). [Preprint]. arXiv; 2026. Version 1, arXiv:2610.30104v1, posted 2026 Oct 21; not peer-reviewed. [cited 2026 Oct 24].
2. <span id="ref-2"></span> Bray MA, Singh S, Han H, Davis CT, Borgeson B, Hartland C, et al. [Cell Painting, a high-content image-based assay for morphological profiling using multiplexed fluorescent dyes](https://doi.org/10.1038/nprot.2016.105). Nat Protoc. 2016;11(9):1757–74.
3. <span id="ref-3"></span> Chandrasekaran SN, Ackerman J, Alix E, Ando DM, Arevalo J, Bennion M, et al. [JUMP Cell Painting dataset: morphological impact of 136,000 chemical and genetic perturbations](https://doi.org/10.1101/2023.03.23.534023) [Preprint]. bioRxiv; 2023. Posted 2023 Mar 24;[bibliographic record checked only].
4. <span id="ref-4"></span> Arevalo J, Su E, Ewald JD, van Dijk R, Carpenter AE, Singh S. [Evaluating batch correction methods for image-based cell profiling](https://doi.org/10.1038/s41467-024-50613-5). Nat Commun. 2024;15(1):6516.
5. <span id="ref-5"></span> AI Lab JKU. [JUMP Cell Painting challenge datasets](https://huggingface.co/datasets/ai-lab-jku/jumpcp-challenge-datasets/tree/a5c2888d320f57e14d1c7d4dd4374397935ab9a4) [dataset]. Revision a5c2888d320f57e14d1c7d4dd4374397935ab9a4 [cited 2026 Oct 24].
6. <span id="ref-6"></span> Li Y, Wang N, Shi J, Hou X, Liu J. [Adaptive batch normalization for practical domain adaptation](https://doi.org/10.1016/j.patcog.2018.03.005). Pattern Recognit. 2018;80:109–17.
7. <span id="ref-7"></span> Machine Learning at JKU. [BatchBench baseline implementation](https://github.com/ml-jku/batchbench-baselines/tree/df18b76bbf6233a0a8bdb423801c5353e613078f) [software]. Commit df18b76bbf6233a0a8bdb423801c5353e613078f [cited 2026 Oct 24].
8. <span id="ref-8"></span> Zhao H, Liu Y, Alahi A, Lin T. [On pitfalls of test-time adaptation](https://proceedings.mlr.press/v202/zhao23d.html). Proc Mach Learn Res. 2023;202:42058–80.
9. <span id="ref-9"></span> Sokolova M, Lapalme G. [A systematic analysis of performance measures for classification tasks](https://doi.org/10.1016/j.ipm.2009.03.002). Inf Process Manag. 2009;45(4):427–37.
10. <span id="ref-10"></span> Sun B, Saenko K. [Deep CORAL: correlation alignment for deep domain adaptation](https://doi.org/10.1007/978-3-319-49409-8_35). In: Hua G, Jégou H, editors. Computer Vision – ECCV 2016 Workshops. Lecture Notes in Computer Science, vol 9915. Cham: Springer; 2016. p. 443–50.
11. <span id="ref-11"></span> Wang D, Shelhamer E, Liu S, Olshausen B, Darrell T. [Tent: fully test-time adaptation by entropy minimization](https://arxiv.org/abs/2006.10726) [Preprint]. arXiv; 2020. arXiv:2006.10726. Published in: International Conference on Learning Representations; 2021. [abstract checked only].
12. <span id="ref-12"></span> Zhang M, Marklund H, Dhawan N, Gupta A, Levine S, Finn C. [Adaptive risk minimization: learning to adapt to domain shift](https://proceedings.neurips.cc/paper/2021/hash/c705112d1ec18b97acac7e2d63973424-Abstract.html). Adv Neural Inf Process Syst. 2021;34:23664–78.
13. <span id="ref-13"></span> Welch BL. [The generalization of "Student's" problem when several different population variances are involved](https://doi.org/10.1093/biomet/34.1-2.28). Biometrika. 1947;34(1–2):28–35.
14. <span id="ref-14"></span> Sypetkowski M, Rezanejad M, Saberian S, Kraus O, Urbanik J, Taylor J, et al. [RxRx1: a dataset for evaluating experimental batch correction methods](https://doi.org/10.1109/CVPRW59228.2023.00451). In: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW). 2023. p. 4285–94.
