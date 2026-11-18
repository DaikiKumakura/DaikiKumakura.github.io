尿路上皮がんの原発巣と遠隔転移巣を対応づけた137組で、膜性NECTIN-4陰性（H-score 0–14）だったのは原発27、転移54だった。原著の[Figure 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC10102834/#F1)は部位ごとの減少を示す ([1](#ref-1))。保存された原発標本を転移巣の代用にするとき、原発で陽性だった患者のうちどの割合が転移で陰性になりうるかを、公表周辺度数だけから計算した。

## 二つの周辺度数から個別の移り変わりを挟む

両方で陰性だった組数を $a$ とすると、原発陽性・転移陰性は $54-a$、原発陰性・転移陽性は $27-a$ になる。四つのセルが非負であることから $0\leq a\leq27$。原発陽性は110組なので、転移陰性の条件付き割合は27/110〜54/110、すなわち24.5〜49.1%になる。

**表1.** 公表周辺度数と両立する二つの端点。

| Both negative | Primary negative only | Metastasis negative only | Both positive | Discordant |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 27 | 54 | 56 | 81 |
| 27 | 0 | 27 | 83 | 27 |

表1のどの割付でも、原発陽性から転移陰性に分類が変わった数は逆方向より27多い。だが両部位が食い違う組の合計は27〜81と幅がある。これは原著の図や個々の症例の情報を追加する前に、部位別集計から最低限言えることだ。原著の[Figure 1C](https://pmc.ncbi.nlm.nih.gov/articles/PMC10102834/#F1)には両方で陰性の組が少なくとも1組あり、これも使えば上限は53/110（48.2%）になる ([1](#ref-1))。部位ごとの陽性率だけでは標本代替の誤りは測り切れない。

陰性分類は当該研究の膜染色による。同じ患者でも測った病変以外は分からず、病変の選び方や染色の閾値を変えたときの誤差もここでは推定していない。別のエンホルツマブ ベドチン投与コホートの関連と、この137組からの分類差は同じ推定対象ではない ([1](#ref-1))。

## データとコードの公開状況

[再計算用ZIP](shared/nectin4-primary-metastasis-bounds/companion.zip)にPythonコードと出力を収録した。

## 参照

1. <a id="ref-1"></a> [Klümper N, Ralser DJ, Ellinger J, Roghmann F, Albrecht J, Below E, et al. Membranous NECTIN-4 expression frequently decreases during metastatic spread of urothelial carcinoma and is associated with enfortumab vedotin resistance. Clin Cancer Res. 2023;29(8):1496–1505.](https://doi.org/10.1158/1078-0432.CCR-22-1764)
