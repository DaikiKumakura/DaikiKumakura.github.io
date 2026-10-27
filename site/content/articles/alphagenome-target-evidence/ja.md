DNAの一文字を変えると、遺伝子の働きはどう変わるか。AlphaGenome Atlasは、その分子レベルの影響を調べる入口を大きく広げた。2026年9月に公開されたAtlasには、約90億の一塩基変異の予測が収められている。[Official announcement](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/)

では、影響が大きいと予測された変異から、その遺伝子を薬で抑えればよいと判断できるだろうか。私は、まず「変異を選ぶ」「分子の変化を説明する」「治療の介入を選ぶ」を分けたい。Atlasの具体例を読むと、最初の二つを進める力と、三つ目までに必要な証拠が見えてくる。

本記事では、[Original Atlas report](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/alphagenome-atlas.pdf)のDNM1スプライシング実験を再集計し、PCSK9の研究と対照して考える。Atlas報告は確認時点でプレプリントである。私はAlphaGenomeやAtlas APIを実行していない。スコアと実験値は著者の報告、図と集計は本記事の計算である。確認日：2026年10月12日。

## AVIの24.7は何の数字か {#avi247}

AlphaGenomeはDNA配列から、発現、スプライシング、クロマチンなどの分子データを予測する。スプライシングとは、RNAから不要な部分を除き、残る部分をつなぐ過程である。[AlphaGenome Original paper](https://www.nature.com/articles/s41586-025-10014-0)

AtlasのAlphaGenome Variant Impact（AVI）は、その予測をまとめて変異を順位付けするスコアである。原報告によると、分子測定の種類ごとに組織をまたぐ最大の予測効果を取り、AlphaMissense、タンパク質終端に関する注釈、保存性などと合わせた18特徴を使う。

学習ラベルは、ヒト集団で観測された変異のfiltering allele frequencyが0.1%より高いか低いかを用いた代理ラベルである。この頻度指標は、集団での頻度推定の不確実性を考慮した下限を使い、遺伝的祖先集団間で最大の値を取る。これは全変異について「疾患を起こす」「治療で改善する」を直接測って学習したものではない。疾患関連変異を選別できるかは、その後の別のベンチマークで検証されている。

表示されるPHREDスコアは、全SNV（一塩基変異）の参照分布での順位を対数に変換したものだ。上位側の割合を\(u\)とすると、

\[
Q=-10\log_{10}u,\qquad u=10^{-Q/10}.
\]

| AVI PHRED | 参照分布の上位側割合 |
| ---: | ---: |
| 10 | 10% |
| 20 | 1% |
| 24.7 | 約0.339% |
| 30 | 0.1% |

24.7は「病原性の確率が99.661%」という意味ではない。同じ上位割合でも、疾患、候補の絞り方、遺伝形式、対象組織によって、注目すべき変異は変わる。

![AVI PHREDと参照分布の上位割合の関係](shared/alphagenome-target-evidence/figures/02-phred-rank.png)

**図1。** 原報告の順位尺度から計算した関係。点はDNM1の変異について著者が報告した24.7。疾患の確率や薬効への変換ではない。

また、AVIの特徴寄与はrawスコア（PHREDへの順位変換前の値）に対する加算的な説明である。PHREDへ変換した数字を、発現の寄与とスプライシングの寄与にそのまま足し分けることはできない。特徴寄与の符号も、遺伝子を増やすべきか減らすべきかという治療方向を表していない。

## DNM1ではスコアの後に組織と転写産物を読む {#dnm1}

原報告は、てんかん性脳症の症例で、DNM1のイントロン内変異`chr9:128225994:G>A`を優先した例を示す。座標はGRCh38。著者の報告したAVI PHREDは24.7で、スプライシング特徴が強く寄与していた。

総合スコアと併せて、転写産物ごとの予測を読む。予測は、脳に特有の転写産物で、新しいスプライス受容部位が使われ、13アミノ酸の延長が生じることを示した。参照・変異配列の予測を比べると、どのRNAのつなぎ方が変わるかまで調べられる。血液では該当するエクソンの発現が乏しく、血液RNAだけでは確かめにくい例でもあった。([Original report Fig. 3](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/alphagenome-atlas.pdf))

ここで、最大効果を一つにまとめるAVIと、組織別の予測を読む作業の役割が分かれる。総合順位で候補を絞り、次に「どの組織の、どの転写産物が、どう変わるか」を調べる。この二段階を省くと、高スコアの理由を標的遺伝子の一般的な機能低下と取り違えかねない。

著者らは近傍の変異を調べ、minigene reporterを用いてスプライシングを測定した。これは対象の配列部分を組み込んでRNAのつなぎ方を測る実験であり、患者の脳や症状そのものを測る実験ではない。既存の症例報告も合わせて、著者らはこの変異をLikely Pathogenicへ分類することを推奨している。

## 実験で見た12変異を同じ「機能異常」にまとめない {#12}

[Atlas report, Table S4](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/alphagenome-atlas.pdf)には、読み枠を保ったエクソン延長を生じる12変異が示されている。以前の報告に対応するものが3、Prospectiveと記されたものが9である。この選ばれた12行をCSVへ転記し、延長の長さと代替スプライス部位の選択率を再集計した。

12変異の延長は2〜45アミノ酸、選択率は0.16〜0.94だった。13アミノ酸延長の変異は0.76である。長さが分かっても、同じ異常転写産物がどの程度作られるかまで一律には決まらない。

![DNM1のエクソン延長と代替スプライス部位選択率](shared/alphagenome-target-evidence/figures/01-dnm1-assay.png)

**図2。** Table S4の12行から作成。橙は以前報告された3変異、青はProspectiveの9変異。選択率はreporter実験の集計値で、患者の発症確率ではない。反復測定の生データを取得していないため、誤差棒や信頼区間は付けていない。

方法には、代替スプライシング率を反復内で求め、反復と品質基準を満たした5つの細胞株・プロモーターの組み合わせで平均する手順が記載されている。したがって、表の一つの割合をすべての細胞や組織で共通の割合と扱わない。

この12行は全スクリーニングの分母ではない。12件すべてに延長があるからといって、モデルの成功率を100%とは計算できない。本記事では、予測精度や新しい病原性分類を推定していない。実験を通じて、総合スコアから具体的なRNAの変化へ進んだことを確認する集計である。

タンパク質への影響は、さらに別の段階になる。原報告は、延長によって正常なDNM1の働きも妨げるdominant-negative作用の可能性を、既存研究との関係から論じている。異常タンパク質が正常なものを妨げる場合と、タンパク質が単に少なくなる場合では、必要な介入は変わりうる。reporterのスプライシング結果だけで、その作用や治療法まで確定したわけではない。

## 創薬標的には変化の大きさに加えて方向が要る {#_1}

この区別を具体的に見せるのがPCSK9である。PCSK9では機能が強くなる変異と、機能が弱くなる変異が調べられてきた。機能獲得変異の研究ではLDL受容体への作用が評価され、機能喪失変異の研究ではタンパク質の分泌低下などが実験で確認された。[Gain-of-function variants paper](https://pubmed.ncbi.nlm.nih.gov/22683120/)、[Loss-of-function variants paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC1559532/)

PCSK9はLDL受容体の分解を促すため、阻害すると受容体が保たれ、血中LDLの取り込みが増える方向に働く。さらに、機能低下に関連する遺伝的変異と低いLDL・冠動脈疾患リスクとの関係が集団で調べられ、PCSK9を阻害する薬剤の臨床効果は無作為化試験で検証された。[Cohen et al. population study](https://pubmed.ncbi.nlm.nih.gov/16554528/)、[FOURIER trial](https://pubmed.ncbi.nlm.nih.gov/28304224/)

これはAlphaGenomeがPCSK9を新たに発見した例ではない。本記事でもPCSK9のAVIを取得していない。対照として示したいのは、**変異に影響があることに加え、作用の方向、疾患との関係、薬による介入を別々の証拠で確認している**点である。生涯にわたる遺伝的な作用と、成人から薬を投与する作用も同じではない。

| 判断 | DNM1のAtlas例で得られた情報 | 創薬のために追加して問うこと |
| --- | --- | --- |
| どの変異を調べるか | 総合順位とスプライシング寄与 | 対象疾患・遺伝形式に合う候補か |
| どこで何が変わるか | 脳特異的転写産物、スプライス部位、延長 | 関連する細胞・組織で再現するか |
| タンパク質がどう働くか | 既存研究に基づく作用機序の仮説 | 機能低下、機能獲得、正常機能の妨害を区別できるか |
| 何を介入するか | この報告だけでは治療方向は決まらない | 正常機能を保ちつつ、異常な作用を変えられるか |
| 患者に便益があるか | reporter実験では評価していない | 曝露、対象組織、時期、安全性、臨床効果を検証できるか |

高スコア変異を持つ遺伝子を並べることと、薬で介入する標的を並べることは、同じ順位付けではない。疾患に関連する変化が強くても、その遺伝子全体を抑えることが望ましいとは限らない。

## AVIは疾患別の標的スコアではない {#atlas}

AVIは分子への影響を要約するが、特定疾患との関連を入力した疾患別の標的スコアではない。近くの遺伝子や高AVIの変異を選ぶだけでは、連鎖した候補のどれが疾患に関与するか、どの組織でどちら向きに介入すればよいかは決まらない。

DNM1の例は、血液で確認できなかった候補を脳特有のスプライシングという仮説へつないだ。その分子予測と、遺伝的な疾患の証拠、介入による機能変化は異なる証拠である。総合順位が高いことだけでは、最後の二つを代用できない。

## 再計算の範囲と資料 {#_2}

[再計算コード・入力CSV・図・結果](shared/alphagenome-target-evidence/alphagenome-target-evidence.zip)を配布する。`python analysis.py`でTable S4の集計とPHREDの順位尺度を再計算できる。標準ライブラリだけで集計でき、図の再作成にはmatplotlibを使う。これは著者の実験集計値の読み直しであり、モデル推論、API照会、全スクリーニングの再解析ではない。

主な資料は[Atlas Original report](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/alphagenome-atlas.pdf)、[AlphaGenome Original paper](https://www.nature.com/articles/s41586-025-10014-0)、上記PCSK9原著である。[Atlas portal](https://alphagenome.google/atlas)と[Official SDK](https://github.com/google-deepmind/alphagenome)も公開されている。原報告は、研究用途であり医療判断のための診断用途ではないこと、データの種類と取得経路で利用条件が異なることを記載している。本記事の配布物には、原論文の図、個人のゲノム、モデル重み、公式コードを含めていない。
