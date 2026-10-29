[English](dellphi305-time-benefit-en.html)

「死亡のハザード比0.42」と聞いても、治療を始めてからどのくらいの時間差が積み上がったのかは分からない。DeLLphi-305の公開生存曲線を12か月で区切って積分すると、OSの制限平均生存時間の群間差は約1.91か月、PFSでは約3.80か月になった。

これは公表された中央値の差でも、新たに推定した平均余命でもない。同じ12か月の窓で、生存または無増悪で過ごす時間を比較した値である。

## 維持療法開始からの12か月をそろえる

DeLLphi-305は、初期の化学免疫療法後に進行していない進展型小細胞肺がんで、tarlatamab＋durvalumabとdurvalumab単独を比較した無作為化試験である。2026年10月24日の報告ではOS中央値21.1対12.7か月、OSハザード比0.42が示された（[Pérol et al., 2026](https://doi.org/10.1056/NEJMoa2609482)）。

今回の数値データは、公開発表資料17頁のOS曲線と19頁のPFS曲線を使用した。両頁には曲線と3か月ごとのリスク集合がある。原著本文を取得できたものとして扱わず、計算の直接の出典をこの発表資料に限定した（[October 24 public presentation, pp.17,19](https://investors.amgen.com/static-files/b4ad55cd-2ca8-4082-9485-2141bd493d3d)）。

問い（QOI）は、維持療法への無作為化から共通の期間までに、二群の生存時間差がどれだけ積み上がったかである。用途（COU）は、公表臨床結果の絶対的な大きさと時間軸を読むための再解析に限る。開始を遅らせる、早める、途中で中止するといったレジメンの比較ではない。

| 指標 | 併用群 | 単独群 |
| --- | ---: | ---: |
| 無作為化人数 | 282 | 281 |
| 12か月時点のOSリスク集合 | 222 | 146 |
| 12か月時点のPFSリスク集合 | 86 | 18 |

リスク集合は、その時点でイベントなく追跡中の人数である。生存確率に割付人数を掛けた人数とは一致しない。打切りを含むため、この表だけからイベント時刻を再構成することもできない。

12か月は曲線の観測範囲内であり、両群にリスク集合が残る共通の制限時点として選んだ。ただしPFS単独群は18人まで減っており、終盤の推定が少人数に支えられる点は残る。この12か月は今回の記述的再解析で定めたもので、試験の事前規定された主要解析ではない。

## 曲線の下の面積を計算する

群\(g\)の公表Kaplan–Meier曲線を\(\widehat S_g(t)\)、制限時点を\(\tau\)とすると、制限平均生存時間（RMST）は

\[
\widehat{\mathrm{RMST}}_g(\tau)=\int_0^\tau\widehat S_g(t)\,dt
\]

となる。比較したのは

\[
\Delta(\tau)=\widehat{\mathrm{RMST}}_{\mathrm{combo}}(\tau)-\widehat{\mathrm{RMST}}_{\mathrm{control}}(\tau)
\]

である。OSなら制限期間内に生存して過ごす時間、PFSなら進行または死亡なく過ごす時間の群平均の推定差に対応する。

PDFの曲線を画像上で手描きせず、色と単調性で識別したベクトルの頂点を読み取った。曲線の水平区間は左側の生存確率を保って積分し、垂直区間には幅がないため面積を加えない。患者別の疑似データを作ったり、曲線の先を外挿したりしていない。頂点は`outputs/tables/curve-vertices.csv`、リスク集合の転記は`risk-sets.csv`に保存した。

![12か月までの公開生存曲線の再描画](shared/dellphi305-time-benefit/figures/survival-common-window.svg)

原図では打切り記号や注記が曲線と重なる。抽出では曲線本体の色付きパスを選び、時刻が戻らず、生存確率が増加しないことを検査した。線や軸をPDFとして描く際の丸めは残るため、以下の値は原個票による再推定と同一ではない。

## 利益の積み上がりは評価期間で変わる

`analysis/run.py`の出力は次のとおりだった。単位はすべて月である（`outputs/tables/rmst.csv`）。

| 制限時点 | OS併用群RMST | OS単独群RMST | OS差 | PFS併用群RMST | PFS単独群RMST | PFS差 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 3か月 | 2.98 | 2.89 | 0.08 | 2.78 | 2.17 | 0.61 |
| 6か月 | 5.81 | 5.31 | 0.50 | 4.79 | 2.92 | 1.86 |
| 9か月 | 8.48 | 7.32 | 1.16 | 6.28 | 3.37 | 2.91 |
| 12か月 | 10.97 | 9.06 | 1.91 | 7.51 | 3.71 | 3.80 |

12か月までのOS差1.91か月は、中央値の差8.4か月より小さい。しかし、この違いは結果の不整合ではない。中央値は生存曲線が50%を通る時刻の比較であり、12か月RMSTは0–12か月の面積である。観測する量が違う。

また「ハザードが58%低い」を、12か月の死亡確率が58 percentage points小さいという意味にはできない。抽出曲線の12か月OSは約79.4%対53.4%だった。これもハザード比とは異なる量である。

![制限期間を伸ばしたときのRMST差](shared/dellphi305-time-benefit/figures/accumulated-absolute-benefit.svg)

PFS差はOS差より早く積み上がった。これは図示された二つのエンドポイントの時間経過の記述であって、PFSを改善したことがOS差を生じさせたという媒介機序の証明ではない。

## 区間別の形と読取感度

3か月ごとの曲線変化を

\[
\bar\lambda_g(a,b)=-\frac{\log\{\widehat S_g(b)/\widehat S_g(a)\}}{b-a}
\]

で記述した。これは区間内の平均的な対数生存率低下を表す記述量である。OSの併用群/単独群の比は0–3、3–6、6–9、9–12か月で順に0.213、0.363、0.235、0.654だった。PFSでは0.225、0.512、0.670、0.472となった（`outputs/tables/interval-rates.csv`）。

公表の層別Coxハザード比を再現した値ではない。これらの変動だけで比例ハザード仮定の成立や不成立を検定していない。後半のリスク集合の減少や曲線の読み取りも含むため、「効き目が何月から弱まる」と解釈することもできない。

軸・線の読み取りに対して、各群の曲線全体を時間方向に±0.05か月、生存確率方向に±0.005ずらす2,000通りの固定シード計算を行った。単調性を保ち、生存確率を0–1に収めた。12か月RMST差のシナリオ範囲はOSで1.78–2.04か月、PFSで3.65–3.95か月だった（`outputs/tables/reading-sensitivity.csv`）。

これは読取条件を変えた幅であり、患者の標本抽出に対する95%信頼区間ではない。個々のイベント・打切り時刻や曲線間の共分散を使っていないため、新しい統計的有意性は主張しない。

## 投与開始時期の答えにはならない

今回の差は、初期治療後に進行せず、維持療法の無作為化に入れた集団の比較である。初期治療を始めたすべての患者へ、そのまま同じ差を割り当てることはできない。

さらに、併用群と単独群の比較から、二薬の相乗作用、個別の寄与、tarlatamabを3か月遅らせたときの効果は分からない。一定期間で中止しても利益が残るかも、二つの曲線の積分では判断できない。治療の割付、実際に継続できた期間、薬物曝露の違いを同じものとして扱わない。

公開曲線から再現可能だったのは、共通の12か月内の絶対的な時間差である。OSでは約1.91か月、PFSでは約3.80か月の面積差が積み上がっていた。ハザード比や中央値と並べて読むことで、何を「利益」と数えるかが具体的になる。

## 解析資料

[コード・抽出座標・集計表](shared/dellphi305-time-benefit/dellphi305-time-benefit-analysis.zip)。`analysis/download_sources.py`で公開PDFのハッシュを確認し、`analysis/run.py`で図表を再生成する。元のPDFや原図は配布物へ含めない。独自に描いた図と数値積分の結果を収録した。

## References

Pérol M, Yoshida T, Ahn MJ, et al. Tarlatamab–Durvalumab Maintenance for Extensive-Stage Small-Cell Lung Cancer. *New England Journal of Medicine*. Published October 24, 2026. [doi:10.1056/NEJMoa2609482](https://doi.org/10.1056/NEJMoa2609482).

Amgen. ESMO 2026 Update. October 24, 2026. Pages 17 and 19, public plotted OS and PFS data used for this independent numerical integration. [Public presentation](https://investors.amgen.com/static-files/b4ad55cd-2ca8-4082-9485-2141bd493d3d).

## Cite this article

Kumakura D. When does the survival benefit of tarlatamab maintenance accumulate? An independent integration of public DeLLphi-305 survival curves. 2026.
