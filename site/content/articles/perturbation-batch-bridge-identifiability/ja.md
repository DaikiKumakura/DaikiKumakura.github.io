単一細胞摂動実験で、対照をバッチ1、摂動群をバッチ2で測ったとする。差が見えたとき、摂動の効果と測定バッチの差をどこまで分けられるか。Songらは、参照パネルやバッチをつなぐ実験配置のもとで、BUSseqモデルで細胞型の差とバッチ効果を識別する条件を示した ([1](#ref-1))。ここでは、共通対照を一つ足したとき、何が分かり何が観測の外に残るかを計算する。

## 対照を足すとバッチ2で処置を比較できる

ある遺伝子スコアの群平均を考える。バッチ1の対照が2、バッチ2の処置が5なら、二つの平均の差3は、加法モデルでのバッチ差と処置差の和である。処置差が2でバッチ差が1でも、処置差が−1でバッチ差が4でも、観測された平均は同じになる。

バッチ2に対照を追加し、平均が3だったとする。このときバッチ2内の処置差は $5-3=2$。処置差が両バッチで共通と仮定すれば、バッチ1の処置平均は $2+2=4$ と予測できる。バッチと処置の交互作用を許すと、バッチ1の処置平均を0と置いても4と置いても、三つの観測値は変わらない。

**表1. 観測した条件と計画行列の階数**

| Observed conditions | Additive model | With interaction |
| --- | ---: | ---: |
| Batch 1 control and batch 2 treated | 2/3 | 2/4 |
| Add a batch 2 control | 3/3 | 3/4 |
| Control and treated in both batches | 3/3 | 4/4 |

表1の各比の分母は係数の数である。平均を記述する最小の線形モデルでの識別可能性を示しており、推定精度は表していない。バッチ1での処置差まで比較したいなら、バッチ1にも処置を置く必要がある。この配置で処置差を測れても、別ドナーへの一般化や細胞組成の変化を評価するには、対応するドナーや実験反復が要る。

## データとコードの公開状況

仮想条件のみを用いた。[再現用Pythonコードと出力](shared/perturbation-batch-bridge-identifiability/companion.zip)を公開する。

## 参照

1. <a id="ref-1"></a> [Song F, Chan GMA, Wei Y. Flexible experimental designs for valid single-cell RNA-sequencing experiments allowing batch effects correction. Nat Commun. 2020;11:3274.](https://doi.org/10.1038/s41467-020-16905-2)
