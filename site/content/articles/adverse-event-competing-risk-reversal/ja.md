有害事象が起きる前に死亡した患者を打ち切り扱いにすると、6か月時点で有害事象の多い群が逆転することがある。SAVVY研究は、追跡期間にばらつきがある試験で、競合イベントを含めた有害事象リスクの推定法を比較した ([1](#ref-1))。ここでは、群の順位まで変わる条件を定数ハザードで計算する。

## 初回の有害事象までに死亡が起きる場合

初回の有害事象の原因別ハザードを $a$、それに先行する死亡の原因別ハザードを $d$ とする。6か月の行政的打ち切り以外に追跡脱落はなく、いずれのイベントも起きていない患者のハザードは一定とする。死亡を打ち切ったKaplan–Meier（KM）法の $1-KM$ の極限は $1-e^{-6a}$。死亡を競合イベントとして扱う累積発生率は、時点 $s$ でどちらのイベントもまだ経験していない確率 $e^{-(a+d)s}$ に $a$ を掛けて積分した $a(1-e^{-6(a+d)})/(a+d)$ になる。

**表1. 6か月までの初回有害事象の推定対象**

| Group | Adverse event hazard per month | Death hazard per month | $1-KM$ with deaths censored | Cumulative incidence |
| --- | ---: | ---: | ---: | ---: |
| A | 0.10 | 0.30 | 45.1% | 22.7% |
| B | 0.08 | 0.02 | 38.1% | 36.1% |

表1で、初回の有害事象も死亡も起きていない患者に限れば、毎月の有害事象ハザードはA群で高い。ところがA群は先に死亡する患者が多く、6か月までに有害事象を経験できる時間が短いため、累積発生率は低い。死亡自体の負担を含めた安全性の評価には、死亡の結果も並べて読む必要がある。

例のハザードは仮定値であり、実薬の安全性や、死亡を取り除く介入の効果を推定していない。有害事象の再発や追跡の中断も扱っていない。

## データとコードの公開状況

仮想条件のみを用いた。[再現用Pythonコードと出力](shared/adverse-event-competing-risk-reversal/companion.zip)を公開する。

## 参照

1. <a id="ref-1"></a> [Stegherr R, Schmoor C, Beyersmann J, Rufibach K, Jehl V, Brückner A, et al. Survival analysis for AdVerse events with VarYing follow-up times (SAVVY)-estimation of adverse event risks. Trials. 2021;22:420.](https://doi.org/10.1186/s13063-021-05354-x)
