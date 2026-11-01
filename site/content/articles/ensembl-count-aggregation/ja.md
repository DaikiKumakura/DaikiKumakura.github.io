遺伝子名をEnsembl IDへそろえたところ、別々だった2行が同じIDになった。ではカウントを足せばよいのか。RNA-seqのアトラス統合について、まさにこの相談がRedditに出ていた。相談にはscVIへ入れる前の長さ補正という別の問題も含まれていた ([1](#ref-1))。

答えを決めるのは、変換先の文字列だけではない。2行が**別々の分子を数えたものか、同じ分子を二度載せたものか**である。IDの統一とカウントの統合を一つの操作にしてしまうと、この違いが消える。

## 対象と確認範囲

2026年11月1日に、IDTrack 0.0.5の公式API、EnsemblのID説明、scvi-toolsの公式FAQとTabula Murisチュートリアルを確認した。掲示板の特定の遺伝子名が本当に同一の遺伝子へ対応するかは検証していない。以下では実在の遺伝子名を使わず、決定論的な小例で加算が成立する条件を調べる。アトラスやscVIモデルを再解析した記事ではない。

## IDが同じでも数えた対象は同じとは限らない

Ensembl IDは遺伝子、転写産物などの対象を区別し、モデルの版も持つ。ヒトのgene IDとtranscript IDを、接頭辞を省いた同じ種類の番号として扱うことはできない ([2](#ref-2))。さらに遺伝子は転写産物をまとめた単位である。転写産物の行と遺伝子の行を混ぜて足すと、親と子を足すことになりうる ([3](#ref-3))。

IDTrackの`build_graph`は参照するEnsembl releaseを固定でき、変換結果も未対応・一対一・一対多などに分類する。外部mapperには版の接尾辞を落とす設定もある ([4](#ref-4))。このため、「ID変換をした」という記録だけでは再現に足りない。元ID、変換先、release、assembly、対象の種類と、曖昧な対応をどう扱ったかが必要になる。

ただし、こうした注釈の記録をそろえても、元の計数で同じ分子を重複して数えたかは別問題である。ID変換ツールは遺伝子の履歴を調べる道具であり、カウント行列から失われた分子の対応を復元する道具ではない。

## 加算できる条件を集合で書く

1細胞の中で、ある2行に数えられた分子の集合を\(A\)と\(B\)とする。同じ遺伝子へまとめた後に欲しいのが異なる分子の数なら、

\[
|A\cup B|=|A|+|B|-|A\cap B|
\]

となる。ここでの分子IDは、誤り補正・重複除去を終えた分子の識別子を仮定している。UMI（unique molecular identifier）の文字列だけが一致したら同一分子とする、という意味ではない。

表1に、この式をPythonで確かめた3例を示す。入力はすべて人工的な整数集合であり、実測データではない。

**表1. 2行の加算と異なる分子数の違い**

| 条件 | 行Aの数 | 行Bの数 | 単純な和 | 共有する分子数 | 異なる分子数 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 別々の分子 | 8 | 5 | 13 | 0 | 13 |
| 一部が重複 | 8 | 5 | 13 | 4 | 9 |
| 同じ行の複製 | 8 | 8 | 16 | 8 | 8 |

最初の2例は、カウント行列ではどちらも8と5である。それでも求める値は13と9に分かれる。集計値と変換先IDしか残っていなければ、どちらが正しいかは決まらない。

逆に、同じ遺伝子を排他的な区画として数えていたことが元の定量法から分かり、各分子がいずれか一行へ一度だけ割り当てられているなら、和は妥当である。同じ情報を別名で複製した行なら、加算ではなく重複を除く処理になる。単なる数値の一致から複製と判断することもできない。独立した2行が偶然同じ値になる場合があるためだ。

転写産物の推定カウントはさらに別である。曖昧に対応するリードの配分や有効長を含む定量値を、実測UMIの集合と同じものとして扱えない。表1は、そのような定量法を置き換える集約アルゴリズムではない。

## 正規化しても二重計数は消えない

元の計数が誤っていても、後で総カウントをそろえれば消えるだろうか。これも小例で調べた。2細胞の本当の標的分子数をどちらも10、他の分子数をどちらも90とする。片方の細胞だけ、標的の10分子が行の複製により二重に載っていると仮定する。

そのまままとめると標的は10対20、全体は100対110になる。1万カウント当たりへ換算すると、標的は1000対1818.2で、差のない標的に1.82倍の差が生じる。逆に背景の合計は9000対8181.8へ下がる。これは2細胞だけの算術例であり、差次的発現検定やバッチ効果の実測ではない。

加算前後で総カウントが保存されていることも、重複がない証拠にはならない。すでに複製された入力行を足した場合、誤った総数はきれいに保存される。行列が壊れていないことと、観測単位が正しいことは違う。

## scVIの入力は計数法から決まる

scVIは遺伝子発現カウントをモデル化する。公式FAQは、scVIのようにraw countsを期待するモデルへ、正規化・変換済みの値を誤って渡さないよう説明している ([5](#ref-5))。通常のUMIデータに対し、遺伝子長で割ることや細胞ごとの総数補正・対数変換を、機械的な前処理として足す理由にはならない。

一方、公式のTabula Murisチュートリアルは、UMIのないSmart-seq2のread countsに遺伝子長補正を施している。UMIとfull-lengthでは、長さが観測数へ及ぼす影響を分けている ([6](#ref-6))。「scVIでは常に長さ補正を禁止する」と一般化するのも正しくない。使用するモデルと計数法を特定して、対応する実装を確認する必要がある。

長さ補正と行の統合は、順番まで含めて同じ計算とは限らない。人工例としてカウントが8と5、長さが1 kbと2 kbなら、先に割って足す値は\(8/1+5/2=10.5\)である。先に13へ足し、便宜的な1.5 kbで割れば8.67となる。後者の長さは説明用に置いただけで、正しいgene lengthの定義ではない。名称を一つにそろえても、補正に必要な測定モデルは自動では決まらない。

## 残せる根拠と残らない根拠

この問題で役立つのは、変換表だけでなく元の計数の来歴である。表2は今回の反例から整理した監査項目であり、IDTrackやscVIの公式な合格基準ではない。

**表2. ID統合と計数統合を分けるための記録**

| 記録 | 判断に使う内容 |
| --- | --- |
| 元のfeature IDと名称 | 表示名の変更か別featureか |
| 生物種・assembly・注釈release・ID version | 同じ参照系で比較しているか |
| gene・transcriptなどの対象 | 集計単位を混ぜていないか |
| quantifierと割当・重複除去の設定 | 2行が同じ分子を含む可能性があるか |
| 変換の一対多・未対応と採用規則 | 曖昧な対応を黙って一行へ潰していないか |
| 統合前後の細胞別総数と採用feature | 実装上の脱落・増殖を検出できるか |

原データから同じ注釈・計数法で定量し直せるなら、少なくとも比較する観測単位をそろえられる。集計行列しかない場合、表1の共有部分は推定不能なまま残る。疑わしいfeatureを除く解析と残す解析の比較は、その不確かさへの感度を調べることはできても、正しい分子数の回復にはならない。

同じEnsembl IDへ写ることは、注釈上の対応をそろえる根拠にはなる。しかし足すべきかどうかは、元の行が何を数えたかで決まる。加算の前に必要なのは、もっと賢い正規化より、失われると戻せない計数の定義である。

## データとコードの公開状況

人工集合、二重計数、長さ補正の例を再実行する[Pythonコード](shared/ensembl-count-aggregation/analysis.py)、[結果JSON](shared/ensembl-count-aggregation/results/results.json)、[再実行説明](shared/ensembl-count-aggregation/REPRODUCE.md)を公開する。Python 3.12.4で実行し、標準ライブラリだけを使用した。乱数は使用していない。実在の遺伝子マッピング、分子レベルデータ、scVI学習は含まない。

## 参照

<a id="ref-1"></a>
1. Reddit user. Handling many-to-one gene name mappings [Reddit discussion; editorially shortened title]. r/bioinformatics. [cited 2026 Nov 1]. Available from: [Discussion permalink](https://www.reddit.com/r/bioinformatics/comments/1xjdmkb/handling_manytoone_gene_name_mappings_eg/).

<a id="ref-2"></a>
2. Ensembl. I have an Ensembl ID, what can I tell about it from the ID? Ensembl release 116 documentation [Internet]. [cited 2026 Nov 1]. Available from: [Ensembl FAQ](https://jun2026.archive.ensembl.org/Help/Faq?id=488).

<a id="ref-3"></a>
3. Ensembl. Ensembl Core API Tutorial: Genes, Transcripts, and Exons [Internet]. [cited 2026 Nov 1]. Available from: [Core API tutorial](https://asia.ensembl.org/info/docs/api/core/core_tutorial.html).

<a id="ref-4"></a>
4. IDTrack developers. Reference; External Mappers. IDTrack 0.0.5 documentation [Internet]. [cited 2026 Nov 1]. Available from: [Reference](https://idtrack.readthedocs.io/en/latest/reference.html); [External Mappers](https://idtrack.readthedocs.io/en/latest/reference/external_mappers.html).

<a id="ref-5"></a>
5. scvi-tools developers. Frequently asked questions. scvi-tools documentation [Internet]. [cited 2026 Nov 1]. Available from: [Frequently asked questions](https://docs.scvi-tools.org/en/stable/faq.html).

<a id="ref-6"></a>
6. scvi-tools developers. Integration and label transfer with Tabula Muris. scvi-tools documentation [Internet]. [cited 2026 Nov 1]. Available from: [Tabula Muris tutorial](https://docs.scvi-tools.org/en/stable/tutorials/notebooks/scrna/tabula_muris.html).
