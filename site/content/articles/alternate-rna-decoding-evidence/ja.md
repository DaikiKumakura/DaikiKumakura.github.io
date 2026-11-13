予想と違うアミノ酸を含むペプチドが見つかった。そこから、細胞が遺伝暗号の読み方を変えたとまで言えるだろうか。必要なのは、見慣れない配列の数を増やすことだけではない。その配列がどこで生まれ、何のために残ったのかを切り分けることだ。

Nikolai Slavovの連投をたどると、書籍の紹介から、標準的な翻訳予測から外れるペプチドを調べた研究へつながる ([1](#ref-1))。TsourらのNature論文は、1,000以上のヒト試料を含む既存データから、多数のアミノ酸置換を報告している ([2](#ref-2))。本稿では、その主張を補足表の実体から読む。数え直すと、論文に出てくる8,746と1,955は再現できた。ただし、その二つを単純に割って「厳しい検証に残った割合」とすることはできなかった。

## 対象と確認範囲

2026年11月1日に、正式版の検索索引から取得できた方法・確認実験・図説明、著者の公開コードとデータ説明、出版社の公開補足データ2・3・8を確認した。出版社本文の全ページを通読したわけではなく、質量スペクトル、患者別DNA・RNA、生物学的な機能実験を再解析していない。

補足データは著者の表記に合わせて以下Table 2、Table 3、Table 8と呼ぶ。633 MBの公開ZIPから必要な3ファイルだけを取得し、ZIP内のサイズとCRCを照合した。元のExcelファイルは変更せず、著者による列の説明を確認してから集計した ([3](#ref-3))。ここでの独自解析は表の行・配列対・対応関係の監査であり、置換そのものの追試ではない。

## 質量差を配列へ読み替えるまで

この研究でいう置換ペプチドは、substituted amino acid peptide（SAAP）、対応する通常配列はbase peptide（BP）である。出発点は、質量分析（MS）で得られた、通常のペプチドと異なる質量を持つ信号だ。しかし同じ質量差には、アミノ酸置換以外の説明もあり得る。

原著は、既知の翻訳後修飾・化学修飾と整合する質量差を除き、候補配列を追加したデータベースで再探索し、置換位置を支持する断片や保持時間などを検討した。偽発見率（FDR）も通常のペプチドとまとめず、SAAPを対象として管理している。[原著のFigure 1](https://www.nature.com/articles/s41586-026-10678-2#Fig1)は、この検証の流れを示す ([2](#ref-2))。同じ信号から異なる情報を照合する検証であり、別の患者集団で結果を再現したことと同じではない。

それでも、置換位置が一意に決まることと、ペプチドの同定が支持されることは区別される。原著は、位置を高い確信で限定できないものでは、未知の複数修飾という代替説明を完全には排除できないとしている ([2](#ref-2))。検出の成否を一つの白黒判定にすると、この違いが消える。

## 8,746と1,955の数え方

Table 2の1行は、データセット内のSAAP・BP配列対である。同じ対が別のデータセットに現れれば、別の行になる。Table 3とTable 8はさらに細かく、tandem mass tag（TMT）という化学標識を使った測定セット、または健康組織の試料に対応する観測を持つ ([3](#ref-3))。行数を患者数や独立した反復数へ読み替えることはできない。

再集計では、空白を補完したり遺伝子名でまとめたりせず、`SAAP`と`BP`の配列文字列の組を同一性のキーにした。表1はその結果である。

表1. 公開補足表の行数と配列対数の再集計

| Published table | Rows | Distinct sequence pairs within datasets | Distinct sequence pairs across datasets |
| --- | ---: | ---: | ---: |
| Table 2 | 10,086 | 10,086 | 8,746 |
| Table 3 | 19,480 | 10,285 | 8,944 |
| Table 8 | 5,873 | 2,503 | 1,955 |

「配列対」はSAAP・BPの組を指す。位置、タンパク質、遺伝子、患者を新たな同一性キーにはしていない。原著と同じ二つの総数を得ても、その総数が同じ階層の処理前後を表すとは限らない。

実際、Table 2とTable 8で共有される配列対は1,899だった。Table 8にはTable 2にない56対があり、81行の健康組織の観測に対応した。この差がどの生成段階から来るかは、今回の集計では特定していない。論文の誤りを検出したという意味ではない。一方、公開された二表をそのまま使う限り、Table 8をTable 2の単純な部分集合として扱えないことは確認できる。

著者の説明では、Table 8の集計元はTable 3であり、Table 2から直接集計したものではない ([3](#ref-3))。そこで`Dataset`、`SAAP`、`BP`、`TMT/Tissue`、`Digest`の5列で対応を調べると、Table 8の観測キーはすべてTable 3に存在した。この比較なら、行の残存率は5,873/19,480（30.1%）、配列対の残存率は1,955/8,944（21.9%）となる。同じ二表でも、何を一個と数えるかで割合が変わる。

Table 8を再フィルタせず、著者が公開した集合として用いた点にも注意が要る。原著は局在確率>0.9の集合を説明しているが、配布表には確率がちょうど0.900と記載された4行がある。丸め前の値は確認できないため、こちらで閾値の反対側へ移して原著の集合を作り替えてはいない。この表の1,955対は著者の高局在確率集合であり、それ以外を偽陽性と分類する数ではない。

## 配列の違いが生まれた場所

通常の翻訳予測と異なる配列を見つけても、その違いが翻訳時に生まれたとは直ちに決まらない。DNA変異、RNA配列の変化、翻訳の読み違い、修飾、同定上の曖昧さを検討する必要がある。これらは、同じ一枚の表から同時に解ける問題ではない。

著者のパイプラインは、対応するRNA-seqから試料別の配列データベースを作る段階を含む。RNA-seqがない場合も処理はできるが、非ゲノム由来だという確信が低くなるとREADMEは明記する ([4](#ref-4))。原著の一部の患者別DNA・RNAデータには申請アクセスが必要であり、著者が実施した照合を本稿で再検証したわけではない ([2](#ref-2))。

Moranのブログとそのコメント欄でも、何を観測し、転写と翻訳のどちらに由来すると判断したかが議論されている ([5](#ref-5))。ただしコメントには互いに異なる解釈があり、議論の存在を反証として使うことはできない。検証すべきなのは用語への賛否より、代替説明をどの観測が狭めたかである。

## 多く残ることと多く作ること

存在量の解釈にも一段の距離がある。置換を持つ分子が多く残っていることは、その置換が高頻度で合成されたことを意味しない。

置換型と通常型のタンパク質量をそれぞれ\(P_s,P_b\)、合成速度を\(v_s,v_b\)、一次分解速度定数を\(k_s,k_b\)とする。独立した二つのプールが定常状態にあるという仮定なら、\(P=v/k\)なので、

\[
\frac{P_s}{P_b}=\frac{v_s}{v_b}\frac{k_b}{k_s}
\]

となる。比が大きくても、合成の比と分解の比は一つに決まらない。これは単純な収支の式であり、原著データへ当てはめたモデルではない。原著もタンパク質安定性を置換型の存在量に関わる要因として検討している ([2](#ref-2))。

さらにMSでのペプチドの相対信号を、そのまま完全長タンパク質の分子数比に置き換えるには、測定応答やどのタンパク質に由来するかという条件が残る。SAAP・BPの比から、翻訳装置が特定のコドンを読み替えた確率まで逆算することはできない。

## 創薬の候補にするまで

この研究が増やすのは、参照配列だけでは列挙し切れないペプチドを調べる入口である。そこから腫瘍の機能や薬剤の標的へ進むには、別の観測が要る。腫瘍で多いことは腫瘍を増やす原因であることを意味せず、細胞全体で見つかるペプチドは、主要組織適合遺伝子複合体上で提示されてT細胞に認識される抗原と同一ではない。

本稿の再集計は同定された配列の真偽や機能を評価していない。公開表の二つの総数を再現し、それらを一つの通過率として扱えないこと、正しい親表でも観測単位により割合が変わることを確認した。そのうえで残る問いは、配列の同定、置換の由来、存在量、機能をつなぐ証拠である。予想と違う配列を見つけることには価値がある。その価値を翻訳の制御や治療標的の証拠へ変えるときこそ、数えているものを変えてはならない。

## データとコードの公開状況

[公開表の取得コード](shared/alternate-rna-decoding-evidence/fetch_supplement.py)、[集計コード](shared/alternate-rna-decoding-evidence/analysis.py)、[表1のCSV](shared/alternate-rna-decoding-evidence/results/table-counts.csv)、[データセット別集計](shared/alternate-rna-decoding-evidence/results/dataset-counts.csv)、[結果と入力ハッシュ](shared/alternate-rna-decoding-evidence/results/summary.json)、[再実行手順](shared/alternate-rna-decoding-evidence/REPRODUCE.md)を公開する。元のxlsxは再配布せず、出版社の公開ZIPから取得する。Python 3.12.4、openpyxl 3.1.5で実行し、乱数は使っていない。

## 参照

1. <span id="ref-1"></span>Slavov N [@slavov_n]. Thread linking genome metaphors to RNA decoding research [X post; editorial description]. 2026 Oct 18 [cited 2026 Nov 1]. Available from: [https://x.com/slavov_n/status/2111826378257793117](https://x.com/slavov_n/status/2111826378257793117).
2. <span id="ref-2"></span>Tsour S, Machné R, Leduc A, Widmer S, Koo E, Guez J, et al. Alternate RNA decoding results in stable and abundant proteins in mammals. Nature. 2026;656:506–515. [https://doi.org/10.1038/s41586-026-10678-2](https://doi.org/10.1038/s41586-026-10678-2).
3. <span id="ref-3"></span>Slavov Laboratory. Download alternate RNA decoding results: supplementary data descriptions [Internet]. Decode; [cited 2026 Nov 1]. [Author documentation](https://github.com/SlavovLab/decode/blob/main/docs/mass-spec/data.md). [Publisher supplementary data ZIP](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-026-10678-2/MediaObjects/41586_2026_10678_MOESM3_ESM.zip).
4. <span id="ref-4"></span>Slavov Laboratory. Decode: computational pipeline for quantifying amino acid substitutions from alternate RNA decoding [Software and documentation]. [cited 2026 Nov 1]. Available from: [https://github.com/SlavovLab/decode](https://github.com/SlavovLab/decode).
5. <span id="ref-5"></span>Moran L. What is alternate RNA decoding? [Internet]. Sandwalk; 2026 Aug 23 [cited 2026 Nov 1]. Available from: [https://sandwalk.blogspot.com/2026/08/what-is-alternate-rna-decoding.html](https://sandwalk.blogspot.com/2026/08/what-is-alternate-rna-decoding.html).
