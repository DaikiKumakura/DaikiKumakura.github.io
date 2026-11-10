少ない実験値から分子の活性を予測できれば、創薬で試す化合物を絞りやすくなる。CheMeleonを紹介した2026年11月6日のMIT Newsも、少量データでの予測を前面に出していた [(1)](#ref-1)。ただ、「少ないデータで強い」という言葉だけでは、古典的な手法を置き換えるほどの差なのかは分からない。

そこで、著者が公開したMoleculeACEの30タスクを再集計した。CheMeleonの誤差は公開ランダムフォレスト（random forest; RF）より平均的に5.0%小さかった。一方、訓練プールが1,000化合物以下の15タスクでは改善は1.9%で、95%区間は改善なしを含んだ。活動崖での改善も、非活動崖より小さかった。

この結果はCheMeleonを否定するものではない。比較相手と対象を変えると、改善の大きさと読み方が変わるという話である。

## 対象と確認範囲

CheMeleonは、計算で得られる分子記述子を予測する事前学習から分子表現を作り、目的の実験値へ微調整するモデルである。正式論文は2026年のJournal of Chemical Information and Modelingに掲載された [(2)](#ref-2)。今回は正式版の書誌を確認したが、出版社の全文にはアクセスできなかった。方法の検討は2026年2月9日のarXiv v2と、固定コミットの公開コード・結果に基づく。正式版と全く同じ方法だと確認したわけではない [(3)](#ref-3) [(4)](#ref-4)。

原著の「勝率」には注意が要る。arXiv v2では、最良の平均成績を持つモデルに加え、Tukeyの多重比較でその最良との差が検出されなかったモデルにも勝ちを与えている。Polarisの75%は21/28、MoleculeACEの約97%は29/30という、この定義の勝率である。単独1位の割合でも、RFを上回る確率でもない。差を検出しなかったことは、同等性を確かめたこととも違う [(3)](#ref-3)。

今回の問いは、この勝率の再現ではない。同じタスクでRFと比べたとき、予測誤差がどれだけ違うかを、活動崖と訓練プールの規模に分けて調べる。Polarisは測定量と評価指標が混在するため、30タスクすべてが活性予測の回帰問題であるMoleculeACEを主解析に選んだ。

## 方法

### 固定テスト集合の5反復を読む

入力は公開されたCheMeleon.md、RF.md、Chemprop.mdの結果と、活動崖別のCSVである。各タスクにseed 42、117、709、1701、9001の5反復があり、3モデルで計450回分を使った。キーをモデル・タスク・seedとして、欠測や重複がないことを確認した。モデルの学習や分子ごとの推論は再実行していない [(4)](#ref-4)。

公開コードではテスト集合が固定されている。seedが変えるのは、学習時の乱数や早期停止用の分割などであり、未知化合物集合を5回独立に取り直した実験ではない。したがって、150個の独立したタスクとしては数えない。原著図説明のfive-foldという表現よりも、実際に読んだ固定分割と結果ファイルを解析の定義に使った。

活動崖は、小さな構造差に対して活性が大きく変わる領域を指す。本稿ではMoleculeACEの固定CSVにあるcliff_molラベルとtrain/test列をそのまま用いた。活動崖ラベルを再作成したり、新しい分割を作ったりしていない [(5)](#ref-5)。表1の訓練数は、微調整時に学習用と早期停止用へ分ける前の訓練プールの規模である。

表1。解析対象。反復数をタスク数へ加算しない。

| Item | Scope |
| --- | --- |
| Tasks | 30 MoleculeACE endpoints |
| Seed runs per task and model | 5 |
| Primary models | CheMeleon, published RF, Chemprop |
| Training-pool compounds | 489–2,924 |
| Tasks with at most 1,000 training-pool compounds | 15 |
| Test split | Fixed published split |

公開リポジトリにはRF以外にRF_MorganやRF_Mordredという別の結果もある。論文に書かれた特徴セットと、各RFファイルの実行履歴の完全な対応は確定できなかった。そのため、主比較を「公開RFラベルの結果」と限定し、別RFの結果は感度解析とした。最適に調整したすべてのランダムフォレストに勝った、とは主張しない。

### 誤差を統合する順序

指標は二乗平均平方根誤差（root mean squared error; RMSE）である。活性は公開CSVの対数尺度を使う。活動崖と非活動崖のRMSEから全体を戻す際には、RMSEをそのまま平均してはいけない。各群の化合物数をn、RMSEをRとすると、各反復の全体値は次になる。

$$
R_{\mathrm{total}}=\sqrt{\frac{n_{\mathrm{cliff}}R_{\mathrm{cliff}}^2+n_{\mathrm{noncliff}}R_{\mathrm{noncliff}}^2}{n_{\mathrm{cliff}}+n_{\mathrm{noncliff}}}}.
$$

この値は、公開Markdownに載った全体RMSEと表示丸めの範囲で一致した。活動崖別の値も、公開の図用CSVと照合した。

次に、タスクt・モデルmの5反復のRMSEを平均して\(\bar R_{m,t}\)と置き、CheMeleonとRFの比を取った。全タスクの代表値Gは、その比の幾何平均である。

$$
G=\exp\left[\frac{1}{30}\sum_{t=1}^{30}\log\left(\frac{\bar R_{\mathrm{CheMeleon},t}}{\bar R_{\mathrm{RF},t}}\right)\right].
$$

Gが1より小さければCheMeleonの誤差が小さい。各タスクを等重みにし、化合物数の多いタスクだけで代表値が決まらないようにした。改善率は100(1−G)%で表す。これは個々の化合物の誤差をまとめた改善率でも、実験成功率でもない。

区間はタスク単位で10,000回再標本化し、2.5%点と97.5%点を取った。同じタスクのモデル・群・反復をまとめて扱い、同じ抽選を対応比較に使った。公開ベンチマーク内のタスク間のばらつきを見る探索的な解析であり、将来の創薬課題を無作為抽出した検証ではない。

## 結果

### RFとの差はChempropとの差より小さい

表2に、RFに対する誤差比を示す。

表2。タスク等重みの誤差比と、CheMeleonの平均RMSEが小さかったタスク数。

| Evaluation subset | Geometric RMSE ratio | 95% task-bootstrap interval | Relative reduction | Lower mean RMSE tasks |
| --- | ---: | ---: | ---: | ---: |
| Total | 0.950 | 0.927–0.972 | 5.0% | 23/30 |
| Cliff | 0.969 | 0.943–0.995 | 3.1% | 19/30 |
| Noncliff | 0.933 | 0.905–0.961 | 6.7% | 24/30 |

全体では23/30タスクでCheMeleonの平均誤差が小さいが、7タスクでは逆転した。原著の29/30という勝ち数と矛盾するわけではない。比べている定義が違う。表2の数は、平均値の厳密な大小であって、タスクごとの有意差の判定数でもない。

![Task-level RMSE ratios against the published RF baseline](shared/chemeleon-low-data/task-ratios.png)

図1。公開結果から作成したタスク別の誤差比。RMSEは二乗平均平方根誤差、RFは公開RFラベルを指す。1より左がCheMeleon優位で、点は5反復平均の比である。タスク名のCHEMBL接頭辞は省略した。原著の活動崖比較は[arXiv v2のFigure 3](https://arxiv.org/html/2506.15792v2#S1.F3)を参照できる。本図は転載ではなく、別の指標による再集計である [(3)](#ref-3) [(4)](#ref-4)。

公開Chempropとの全体の比は0.800、95%区間は0.779–0.822で、30/30タスクで平均誤差が小さかった。未事前学習モデルからの改善は大きい。しかし、その数字を古典的なRFとの差として読むと、改善を大きく見積もる。比較相手が変われば「どれほど強いか」も変わる。

別RFへの感度解析では、全体の比はRF_Morganに対して0.961、RF_Mordredに対して0.908だった。主比較の方向は保たれたが、活動崖だけのRF_Morgan比較は0.975、95%区間0.942–1.009となった。活動崖での小さな改善は、比較するRFの選択にも敏感である。

### 活動崖の改善は非活動崖より小さい

活動崖でRFより良いことと、活動崖の難しさが消えることは別である。CheMeleonの活動崖RMSEは、30タスク中29で非活動崖より大きかった。群間の差のタスク平均は0.151対数活性単位、95%区間は0.112–0.192だった。

RFに対する相対改善も、活動崖で特に大きいわけではない。同じタスク内で、活動崖の誤差比を非活動崖の誤差比で割った値を幾何平均すると1.038、95%区間は1.007–1.071だった。1を上回るので、今回の固定データではRFに対する相対的な改善は、むしろ活動崖で小さかった。これは活動崖で誤差が増えたという意味ではない。RFに対する改善幅が、非活動崖ほど大きくないという意味である。

### 1,000件以下を切り出すと差が縮む

![Aggregate error ratios and training-pool sizes](shared/chemeleon-low-data/aggregate-size.png)

図2。左は表2の誤差比と95%タスク再標本化区間。右は訓練プールの規模と全体誤差比で、各点は異なるタスクを表す。右図は同じタスクで訓練数を増減した学習曲線ではない。

図2右の1,000件以下の15タスクでは、全体の比は0.981、95%区間は0.955–1.008だった。1,000件を超える15タスクでは0.919、区間は0.889–0.949となった。少なくとも、この30タスクのうち最もデータの少ない側で、RFに対する優位が一様に大きくなる様子は見えなかった。

ただし、ここから「データが増えるほどCheMeleonが有利になる」と因果的には言えない。タスクの標的、活性分布、化合物系列、難しさも同時に変わる。1,000件という区切りも、低データを調べる探索的な層別である。数十例しかない課題への汎化や、必要な実験数を何割減らせるかは、この比較では測っていない。

## 考察と限界

全体のRF比較は、タスクを一つずつ外しても比が0.946–0.956に収まった。同じCHEMBL番号の二つのendpointをまとめて29グループに等重みを付け直しても、比は0.949だった。少数の結果だけで全体の方向が決まったわけではない。

それでも、タスク間は完全には独立でない。化合物や標的の共有、測定法の近さは、この名前によるグループ化だけでは処理できない。区間は新規標的、新規骨格、将来の時系列分割への性能保証ではない。個々の化合物の予測値や誤差分布も入力にないため、測定誤差の分離、校正、実験候補を上位から選んだときの成功率は検証していない。

また、比較は著者が公開した学習条件の範囲に限る。計算費用をそろえた再学習、RFの再調整、モデルサイズと事前学習の寄与の分離は行っていない。原著の有意差に基づく勝ち数を、ここで新たに認定したわけでもない。

CheMeleonには、公開Chempropからの大きな改善と、公開RFからのより小さな平均的改善があった。だが、訓練プールの小さい側と活動崖では、その優位は弱まった。少量データという言葉を採用理由にする前に、比較相手をRFまで戻し、目的の化合物群で差を見る必要がある。今回の再解析が支持するのは、条件付きの予測改善であって、実験の省略率や活動崖の解決ではない。

## データとコードの公開状況

[著者の固定コミット](https://github.com/JacksonBurns/chemeleon/tree/b5e5bd88a7070c3f278e7e65e85b792617bf125c)と[MoleculeACEの固定CSV](https://github.com/molML/MoleculeACE/tree/7e6de0bd2968c56589c580f2a397f01c531ede26/MoleculeACE/Data/benchmark_data)を入力とした。[解析コード](shared/chemeleon-low-data/analysis.py)、[集計結果](shared/chemeleon-low-data/results.json)、[再現手順](shared/chemeleon-low-data/analysis-readme.md)を公開する。入力はSHA256で照合し、乱数seedは20261110、再標本化は10,000回である。元の分子データと第三者コードは配布ZIPに含めず、固定URLから取得する。

[コード・結果・図のZIP](shared/chemeleon-low-data/chemeleon-low-data.zip)

## 参照

<a id="ref-1"></a>
1. Chandler DL. How to predict the behavior of molecules from scant data [Internet]. MIT News; 2026 Nov 6 [cited 2026 Nov 11]. [Article](https://news.mit.edu/2026/how-to-predict-molecule-behavior-with-scant-data-1106).

<a id="ref-2"></a>
2. Burns JW, Zalte AS, Abreu CRA, Sieg J, Feldmann C, Mathea M, et al. Deep Learning Foundation Models for Low-Data Regimes from Classical Molecular Descriptors. Journal of Chemical Information and Modeling. 2026;66(17):10692–10701. [doi:10.1021/acs.jcim.6c01546](https://doi.org/10.1021/acs.jcim.6c01546).

<a id="ref-3"></a>
3. Burns JW, Zalte AS, Abreu CRA, Sieg J, Feldmann C, Mathea M, et al. Deep Learning Foundation Models from Classical Molecular Descriptors [Preprint]. arXiv; 2026. Version 2, February 9, 2026. [arXiv:2506.15792v2](https://arxiv.org/html/2506.15792v2).

<a id="ref-4"></a>
4. CheMeleon contributors. CheMeleon [Software and benchmark results]. GitHub. Snapshot b5e5bd88a7070c3f278e7e65e85b792617bf125c [cited 2026 Nov 11]. [Repository](https://github.com/JacksonBurns/chemeleon/tree/b5e5bd88a7070c3f278e7e65e85b792617bf125c).

<a id="ref-5"></a>
5. MoleculeACE contributors. MoleculeACE benchmark data [Dataset]. GitHub. Snapshot 7e6de0bd2968c56589c580f2a397f01c531ede26 [cited 2026 Nov 11]. [Benchmark tables](https://github.com/molML/MoleculeACE/tree/7e6de0bd2968c56589c580f2a397f01c531ede26/MoleculeACE/Data/benchmark_data).
