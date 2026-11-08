中央演算処理装置（CPU）で3時間、画像処理装置（GPU）で3.2時間。2026年11月8日（日本時間）にRedditで確認した、全ゲノムシーケンス（WGS）の処理を比較する投稿にあった数字である。bwa-mem3の高速モードとParabricksについての報告だった [(1)](#ref-1)。

GPUだから必ず速いとは限らないという話は目を引く。だが、この二つの値からCPUへ移る判断をするには、何を同じ条件にした比較かを確かめる必要がある。処理範囲が違う場合と、出力が違う場合では、速度差の読み方が変わる。

## 対象と確認範囲

Redditの投稿と表示されたコメント、投稿に結び付いた公開ワークフロー、bwa-mem3とParabricksの公式説明を確認した。独立したWGSの実行、アラインメントの比較、変異検出の精度評価は行っていない。したがって、本記事はCPUとGPUの実測優劣を決定するベンチマークではなく、公開比較が支持する範囲の検討である。

ワークフローはコマンドと処理の対応を追う入口になる [(2)](#ref-2)。ただし、実行手順が公開されていることと、その全出力が品質検証されたことは同じではない。

## 高速モードは同じ出力の約束ではない

bwa-mem3の公式説明は、`--fast` が既定モードと同じアラインメントを生成する設定ではないと明記している [(3)](#ref-3)。したがって、同じアラインメントを実装だけの違いで速く計算した比較とは言えない。

アラインメントが違うこと自体は、変異検出が悪いことを意味しない。同じくらい妥当な位置へ読み替わる場合も、下流のフィルターで使われないリードの位置が変わる場合もある。一方、全体ではわずかな差でも、特定の反復領域や変異の近くへ集中すれば、関心のある結果を変えうる。

したがって、「何件のリードが同じ位置か」と「何件の真の変異が検出できたか」は分ける必要がある。出力が違うことを失敗と決めつけず、違いがどこにあり、下流の何へ伝わるかを評価する問題になる。

## ストップウォッチの始点と終点

WGSの処理はアラインメントだけで終わらない。ソート、重複の処理、塩基品質の再較正、ファイルの読書きなどが加わる。NVIDIAの公式文書でも、`fq2bam` はアラインメント以外の処理を含み、再較正は指定する入力・出力オプションに依存する [(4)](#ref-4)。

このため、一方のコマンド終了時と、他方で後処理を追加した後を比較すると、異なる到達点を測ることになる。逆に、コマンドの名前が同じでも、オプションが違えば終点の内容が変わる。速さは実行時間だけでなく、実行時間を定義する仕様と一緒に記録される必要がある。

全体時間を概念的に \(T=T_{\mathrm{map}}+T_{\mathrm{sort}}+T_{\mathrm{dup}}+T_{\mathrm{other}}\) と分けると、一つの工程が大きく高速化しても、他の工程が支配的なら全体はあまり短くならない。この式は直列工程の説明用であり、実際に重なって動く処理を正確に計時した分解ではない。単一工程の性能と全体の所要時間を混同しないために置いている。

## 速いと安いは別の比較

仮に投稿された3.0時間と3.2時間が同じ到達点を測り、再実行しても保たれるとする。CPU環境とGPU環境の一式の時間料金を \(p_C,p_G\) とすれば、計算費用はそれぞれ \(3.0p_C\) と \(3.2p_G\) である。GPU側が安い条件は

\[
\frac{p_G}{p_C}<\frac{3.0}{3.2}=0.9375
\]

となる。ここでの時間料金はGPU単体ではなく、CPU、メモリなどを含む比較環境全体の料金である。保存・転送費用や待ち時間は含めていない。実際のクラウド価格を調べた計算ではない。

同じGPU環境で試料を並列処理できれば、単一試料の所要時間と、多数試料の単位時間当たり処理数も違う。所有済みのCPUと新規のGPUを比べる場合には、既存設備の扱いも変わる。この一組の時間だけから、費用や処理能力を一般化することはできない。

## 品質の比較には正解と対象領域が要る

二つの出力が一致しない場合、どちらが良いかは一致率だけでは決まらない。双方が同じ誤りをしていれば一致率は高い。独立に定めた正解付きの試料と評価領域が必要になる。Genome in a Bottleは、そのような公開ベンチマークの取得先を提供している [(5)](#ref-5)。

ただし、正解が評価可能とされる領域だけで得た成績を、ゲノム全体へそのまま広げることもできない。単一塩基変異と挿入・欠失、容易な領域と難しい領域では結果が違いうる。変異検出器、参照配列、正解セットの版を変えると、アラインメント以外の差も入る。

投稿に対する疑問の核心は、速さの報告を否定することではない。実務で置き換える対象がアラインメントなのか、変異検出を含む一連の解析なのかを定めることである。前者の良い比較が、そのまま後者の置換根拠になるとは限らない。

## 結論

公開された比較は、特定条件でCPU処理がGPU処理に近い時間へ達しうるという報告である。CPUが一般に速い、GPUが不要だという結論までは支持しない。

とくに高速モードを使う場合、時間の比較には出力の比較が伴う。処理の終点と変異精度を保ったまま短くできたのか。それを分けて読めば、3時間という数字は有用な問いの入口になるが、導入判断の代わりにはならない。

## データとコードの公開状況

費用の境界条件の計算は[スクリプト](shared/wgs-cpu-gpu/reproduce.py)と[出力](shared/wgs-cpu-gpu/illustration.json)の `WGS` にある。入力時間は投稿者の報告値であり、独立測定ではない。参照ワークフローはコミット `ba6c6203fc91643d9018f2432bfab12173ca5174` を確認した [(2)](#ref-2)。本記事からWGSの品質評価結果は提供していない。

[計算コードと結果のZIP](shared/wgs-cpu-gpu/wgs-cpu-gpu.zip)。

## 参照

1. <a id="ref-1"></a> Comparison of bwa-mem, minibwa, bwa-mem3 and Parabricks [Reddit post; editorial description]. r/bioinformatics [cited 2026 Nov 8, JST; exact posting timestamp not independently verified]. [Discussion](https://www.reddit.com/r/bioinformatics/comments/1xqcr6u/i_compared_bwamem_minibwa_bwamem3_and_parabricks/).

2. <a id="ref-2"></a> bio-pype. bwas_comparison [Workflow documentation]. Codeberg; 2026. Commit ba6c6203fc91643d9018f2432bfab12173ca5174 [cited 2026 Nov 8]. [Versioned workflow](https://codeberg.org/bio-pype/test_workflows/src/commit/ba6c6203fc91643d9018f2432bfab12173ca5174/bwas_comparison).

3. <a id="ref-3"></a> fg-labs. bwa-mem3: Three ways to run it [Software documentation]. GitHub [cited 2026 Nov 8]. [Repository](https://github.com/fg-labs/bwa-mem3#three-ways-to-run-it--plain---compat---fast).

4. <a id="ref-4"></a> NVIDIA. fq2bam (BWA-MEM + GATK) [Software documentation]. Parabricks v4.8.0 [cited 2026 Nov 8]. [Official documentation](https://docs.nvidia.com/clara/parabricks/tool-reference/tools/fq2bam).

5. <a id="ref-5"></a> Genome in a Bottle. giab_latest_release [Dataset documentation]. GitHub [cited 2026 Nov 8]. [Benchmark release directory](https://github.com/genome-in-a-bottle/giab_latest_release).
