AIが単一細胞解析に正解した。その一文で、どこまで任せられると考えてよいのだろうか。Kenny Workmanは、コードと同じく実行・確認を繰り返せるデータ解析が、生物学のエージェントの入口になると論じている。同時に、科学的な正解の定義と実験からのフィードバックは、ソフトウェアほど単純ではないとも書いている ([1](#ref-1))。

この議論を、公開されたscBenchの採点条件で確かめた。差次的発現の課題では、遺伝子の数が合格範囲に入ることと、どの遺伝子を見つけたかが一致することは別だった。品質管理の課題でも、同じ集計値に到達した理由までは、数値の採点から決まらない。

## 対象と確認範囲

2026年11月1日に、scBenchの公開リポジトリと3件の公開課題を読み、そのうち差次的発現と品質管理の2件を小検証の対象にした。確認したREADMEは195課題・6カテゴリーを説明している ([2](#ref-2))。一方、2026年2月のプレプリントは394課題・7カテゴリーであり、版と対象が違う。両者の正答率や分母を混ぜて評価しない ([3](#ref-3))。

原データを使って解析を再実行したわけでも、AIモデルを評価し直したわけでもない。公開された数値採点器を実行し、その条件を独立に書いたコードと照合した。生物学的な入力を必要としない9ケースで判定が一致した。採点器の原ソースは再配布せず、配布コードには独自の数値条件の実装だけを含める。

## 遺伝子数を採点する課題

`DE01_pseudobulk_de`は、複数ドナーの単一細胞RNAシーケンシング（scRNA-seq）から、IFN-beta刺激に応答するCD14単球の差次的発現を調べる課題である。ドナーと条件ごとの細胞数、遺伝子の総カウント、調整済みp値と変化量の閾値が指定されている。解答として要求するのは、差次的発現遺伝子（DEG）の数を表す`n_degs`一つである ([4](#ref-4))。

公開設定の参照値は1150、絶対許容差は350だった。参照値を \(c\)、提出値を \(x\)、許容差を \(\delta\) とすれば、判定は

\[
|x-c|\leq\delta
\]

である。実装は設定された数値フィールドを読み、この条件を確認する。遺伝子集合や解析方法を、この数値フィールドから復元して調べる処理ではない ([5](#ref-5))。

表1に、公開設定を使った境界の実行結果を示す。整数の提出値だけを調べた。

**表1. DEG数の採点条件の境界**

| 提出したDEG数 | 数値条件の判定 |
| ---: | --- |
| 799 | 不合格 |
| 800 | 合格 |
| 1150 | 合格 |
| 1500 | 合格 |
| 1501 | 不合格 |

独自コードと、取得した公開採点器の両方で同じ判定になった。これはモデルの正答率ではなく、設定が受け付ける範囲を確かめた結果である。

許容幅には理由がある。課題の説明は、ドナーごとに集計するpseudobulkの方法や、細胞数の採用条件でDEG数が変わることを挙げている。数値を一点に固定すれば、妥当な方法の違いまで落としてしまう。幅を持たせること自体が誤りなのではない ([4](#ref-4))。

## 数が合っても遺伝子は同じとは限らない

ここで、人工的な遺伝子集合AとBを作った。両方とも1150個を持つが、一つも重ならないようにした。実在の遺伝子名やscBenchの原データは使っていない。

集合の一致をJaccard係数

\[
J(A,B)=\frac{|A\cap B|}{|A\cup B|}
\]

で測ると、この例では \(0/2300=0\) である。一方、数値採点器へ渡す解答は、どちらも`n_degs=1150`なので合格する。

ここで採点器に遺伝子集合を渡したわけではない。**遺伝子集合を要求していない採点から、その一致を結論できない**ことを、二つの人工集合で示した。実際のエージェントが無関係な遺伝子を報告した証拠ではなく、偽合格の頻度を測ったものでもない。

薬剤の応答遺伝子を追試へ回す場面なら、この違いは大きい。候補の件数が揃っていても、次に実験する遺伝子が違えば、判断は揃っていない。逆に、処理の取り違えでDEGが極端に増減する失敗を検出する目的なら、数の採点は役立つ。評価の意味は、何を合格の対象にしたかで決まる。

## 同じ集計値に違う理由が付く

品質管理（QC）の公開例`bd_rhapsody_tnbc_panel_aware_qc`は、全トランスクリプトーム用の足切りを、小さな標的遺伝子パネルへ持ち込む失敗を扱う。採点するのは、残した末梢血単核球（PBMC）の数、検出遺伝子数の中央値、古典的単球の数の3項目である ([6](#ref-6))。

この例で興味深いのは、作者が許容する範囲を明記していることだ。パネルにミトコンドリア遺伝子がないため、ミトコンドリア比率によるフィルタは無操作になる。誤った理由でそのフィルタを選んでも、残る集計値が同じなら数値上は合格する。作者はこれを記載し、生物学的な結果が変わらない例として扱っている。隠れた欠陥をこちらが発見したわけではない。

検証では、公開設定の参照集計値を二つの解答へ同じように入れた。一方に「パネルを考慮した処理」、もう一方に「無操作フィルタ」という説明上のラベルを付けたが、ラベルは採点器へ渡していない。両方とも合格した。これは、数値採点の入力に含まれない理由を、同じ数値から区別できないことの確認である。

結果が変わらない無操作を落とさない設計には合理性がある。ただ、その合格を「測定法を理解した」と言い換えると、採点した範囲より主張が広くなる。いまのデータで同じ答えになったことと、異なるパネルにも適切に対応できることは、別の確認である。

## 合格の範囲を広げずに読む

局所的な採点は、手順の誤りを切り分け、改善を追いやすくする。その利点は残る。Workman自身の論考も、局所的な検証から科学全体の正解へ一気に飛べるとは述べていない ([1](#ref-1))。

また、scBench-Longは、複数段階の解析から科学的な結論へ進む別の評価を提案している。21課題を扱う2026年6月のプレプリントを確認したが、本稿ではその原データや全採点規則を再検証していない。今回読んだ局所課題だけを、生物学のエージェント評価全体として扱うこともできない ([7](#ref-7))。

本検証の対象は公開課題のうち2件の数値条件に限る。未公開の課題、軌跡の評価、他の採点方式が同じ弱点を持つとは主張しない。文字列の解答抽出、異常値の扱い、実行環境全体を独自コードで再現したわけでもない。

この範囲で言えることは明確だ。DEG数の合格は遺伝子集合の一致を保証せず、QC集計の合格は分析者が選んだ理由を特定しない。AI解析の正答率を読むときには、数値の後ろに、その評価が実際に観測した対象を残しておく必要がある。

## データとコードの公開状況

[独自の計算コード](shared/scbench-grading-identifiability/analysis.py)、[境界のCSV](shared/scbench-grading-identifiability/results/de-boundaries.csv)、[結果JSON](shared/scbench-grading-identifiability/results/results.json)、[再実行手順](shared/scbench-grading-identifiability/REPRODUCE.md)を公開する。Python 3.12.4の標準ライブラリだけで実行し、乱数は使っていない。公開採点器との9ケースの照合結果も[検証記録](shared/scbench-grading-identifiability/upstream-verification.json)へ収めた。原データ・第三者の採点器原ソース・モデル出力は含まない。

## 参照

1. <span id="ref-1"></span>Workman K. [Agentic biology is shaped like software](https://blog.latch.bio/p/agentic-biology-is-shaped-like-software) [Internet]. LatchBio; 2026 Apr 30 [cited 2026 Nov 1].
2. <span id="ref-2"></span>LatchBio. [scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis](https://github.com/latchbio/scbench) [Software and documentation]. GitHub; [cited 2026 Nov 1]. README version accessed describes 195 evaluations.
3. <span id="ref-3"></span>Workman K, Yang Z, Muralidharan H, Abdulali A, Le H. scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis [Preprint]. arXiv; 2026. Version 1, 2026 Feb 9. [doi:10.48550/arXiv.2602.09063](https://doi.org/10.48550/arXiv.2602.09063).
4. <span id="ref-4"></span>LatchBio. [DE01_pseudobulk_de.json](https://github.com/latchbio/scbench/blob/main/evals/differential_expression/DE01_pseudobulk_de.json) [Evaluation specification]. GitHub; [cited 2026 Nov 1]. Git blob SHA: 473eaaf2eb8da8e92e722fab20da15492357362e.
5. <span id="ref-5"></span>LatchBio. [NumericToleranceGrader](https://github.com/latchbio/latch-eval-tools/blob/main/src/latch_eval_tools/graders/numeric.py) [Software source]. GitHub; [cited 2026 Nov 1]. Git blob SHA: 4fe0a812d3abc52f0efcfc69fd204eefa713f930.
6. <span id="ref-6"></span>LatchBio. [bd_rhapsody_tnbc_panel_aware_qc.json](https://github.com/latchbio/scbench/blob/main/evals/qc/bd_rhapsody_tnbc_panel_aware_qc.json) [Evaluation specification]. GitHub; [cited 2026 Nov 1]. Git blob SHA: 5540b13fe58289b313dfaad515de9d0d4ef235e7.
7. <span id="ref-7"></span>Diks I, Yang Z, Banerjee A, Proctor T, Workman K. scBench-Long: Verifiable Benchmarking of Long-Horizon Single-Cell Biology [Preprint]. arXiv; 2026. Version 1, 2026 Jun 25. [doi:10.48550/arXiv.2606.26563](https://doi.org/10.48550/arXiv.2606.26563). Abstract consulted; full benchmark not re-evaluated.
