Daraxonrasib投与後の変異を探した研究では、治療前と進行時の血中循環腫瘍DNA（ctDNA）を比較した44人中16人に、獲得性の変異型KRAS増幅が検出された。単群第I/II相の対象はRAS変異陽性の転移性膵管がんで、解析対象者は二次治療以降として160–300 mg/日の単剤を受け、無増悪生存期間が3か月を超えてから進行した。原著の[Figure 1](https://www.nature.com/articles/s41591-026-04537-w/figures/1)は、この条件で解析できた患者の結果である ([1](#ref-1))。追加採血を計画するなら、36%をどの集団へ持ち出せるかが問題になる。

## 同じ36%から異なる母集団が成り立つ

同じ治療経過をたどった進行例で、全員を共通の測定条件で評価できたときのKRAS増幅陽性率を $p$ とする。陽性例と陰性例でペア検体が評価に入る確率を $s_1,s_0$ とすると、評価例の陽性率は $q=ps_1/[ps_1+(1-p)s_0]$。比 $r=s_1/s_0$ を仮定すると $p=q/[q+r(1-q)]$ になる。$q=16/44$ を固定して感度を計算した。

**表1.** 評価に入る確率の比を変えたときの陽性率。

| Inclusion probability ratio | Target positive fraction |
| ---: | ---: |
| 0.5 | 53.3% |
| 1.0 | 36.4% |
| 2.0 | 22.2% |

表1の22.2〜53.3%は信頼区間ではなく、選択条件を変えたときの値である。ctDNAの放出量、採血時期、進行時の追跡、検体品質は評価可否と関連しうるが、この資料は $r$ を推定するためのものではない。さらにこの計算は早期進行例への外挿も、検出感度や組織間の不一致の補正もしていない。次の採血設計で必要なのは、検体が揃った患者の一覧に加えて、適格だったが解析に入らなかった患者のフローである。

## データとコードの公開状況

[再計算用ZIP](shared/daraxonrasib-resistance-sampling/companion.zip)にPythonコードと出力を収録した。

## 参照

1. <a id="ref-1"></a> [Aronchik I, Kar S, Zhuang Y, Ahler E, Lai LP, Seshadri V, et al. Acquired resistance to the RAS(ON) multi-selective inhibitor daraxonrasib guides rational combination therapy strategies in pancreatic cancer. Nat Med. 2026;32:2865–2877.](https://doi.org/10.1038/s41591-026-04537-w)
