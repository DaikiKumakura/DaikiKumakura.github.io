遺伝子発現から経路の応答を読むとき、刺激群と無処置群が離れるだけでは、どの刺激に反応したかまでは分からない。たとえばIFN-βとIFN-γはともにインターフェロン応答を誘導する。固定したスコアが別の実験へ移せるかを確かめるため、無処置に加えて、応答が似ていても区別したい処置を比較に入れた。

## 重みを固定して別の実験へ移す

各軸の重みは、開発に使った各研究で効果の絶対値を百分位順位へ変換し、元の符号を付けた。2研究で符号が一致した遺伝子について符号付き順位の平均を取り、その絶対値が大きい50個を選んだ。MAPKの開発資料は[GSE312195](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312195)と[GSE87419](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE87419)、IFN-I・IFN-IIは[GSE185200](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE185200)と[GSE236156](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE236156)。評価データの値で遺伝子や重みを選び直していない。各試料で全測定遺伝子の順位を−0.5から0.5へ変換し、測定できた遺伝子の符号付き加重和を絶対重みの総和で割った。同順位は平均順位を使った。

IFNはGSE103363のHeLa細胞で調べた。無刺激、IFN-β、IFN-γは各3生物反復 ([1](#ref-1))。AffymetrixのGPL6244注釈から単一Entrez IDを用い、HGNCの一対一Ensembl IDへ対応させた。同じ遺伝子の複数プローブは中央値で集約し、18,664遺伝子を順位化した ([2](#ref-2), [3](#ref-3))。MAPKにはGSE301146の51T-2D膵がん細胞を用いた。48時間のsotorasib、palbociclib、溶媒対照の各3反復のみを使い、公開正規化行列の26,485遺伝子を順位化した ([4](#ref-4))。Sotorasibは上流のKRAS G12C阻害薬で、palbociclibを比較に入れた結果は、直接のERK活性を測った結果とは区別する。

## 二つの比較で符号は揃ったか

表1に全試料での差と除外感度を示す。

**表1.** 固定スコアの差と、符号が保たれた試料除外の回数。

| Axis | Absolute weight coverage | Target minus control | Target minus other treatment | Both signs under omissions |
| --- | ---: | ---: | ---: | ---: |
| IFN-I (IFN-β) | 100.0% | +0.1799 | +0.0713 | 27/27 |
| IFN-II (IFN-γ) | 94.0% | +0.1102 | +0.1074 | 27/27 |
| MAPK (sotorasib) | 100.0% | −0.1212 | −0.0898 | 27/27 |

IFN-Iでは、無刺激との比較よりもIFN-γとの比較で差が小さくなった。各群から1試料ずつ除く全27通りで再計算しても、両比較で符号は保たれた。IFN-Iの差の最小値は、無刺激比で+0.1720、IFN-γ比で+0.0650だった。この二つの最小値は比較ごとに求めた値であり、同じ除外の組合せから出る必要はない。

同じ9試料を使う27通りは独立な検証ではない。各軸1細胞株であり、薬剤量・時間や生物種を変えた一般化も調べていない。各スコアの数値は測定した遺伝子集合の中での順位に依存するため、異なる実験の絶対値を活性の共通尺度にしない。ここで確かめたのは、開発とは別の2実験で、固定した符号付きスコアが無処置と比較処置の両方に対して所期の方向を示したことまでである。

## データとコードの公開状況

[再現用ZIP](shared/frozen-pathway-perturbation-transfer/companion.zip)に重み、取得元、前処理と計算コード、集計表を収録した。

## 参照

1. <a id="ref-1"></a> Randow F, Wandel MP. Expression data from HeLa cells upon interferon-gamma or interferon-beta treatment. NCBI Gene Expression Omnibus. [GSE103363](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103363).
2. <a id="ref-2"></a> NCBI Gene Expression Omnibus. Affymetrix Human Gene 1.0 ST Array. [GPL6244](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL6244).
3. <a id="ref-3"></a> HUGO Gene Nomenclature Committee. HGNC complete set. [HGNC download archive](https://www.genenames.org/download/archive/).
4. <a id="ref-4"></a> Paulsohn MB, Frahnert KH, Schlösser D, Oschwald J, Kopp W, Fang X, et al. Simultaneous targeting of KRAS and CDK4 synergistically induces durable growth arrest in pancreatic cancer cells. Cell Death Dis. 2026;17:129. [doi:10.1038/s41419-025-08362-w](https://doi.org/10.1038/s41419-025-08362-w) · [Figure 3](https://www.nature.com/articles/s41419-025-08362-w/figures/3) · [GSE301146](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE301146).
