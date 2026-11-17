DeLLphi-304の延長追跡では、tarlatamab群と化学療法群の全生存期間（OS）中央値は13.6か月と8.4か月だった。中央値の差は5.2か月である。24か月までの平均生存時間の差を知りたいとき、この数字とAnnals of Oncologyの抄録にある二つの生存割合で、どこまで答えが決まるだろうか。対象は白金製剤による化学療法中または治療後に進行した小細胞肺がんで、tarlatamab群254人、化学療法群255人の無作為化比較である。データカットオフは2026年2月18日だった ([1](#ref-1))。

## 抄録の数字から生存曲線の面積を挟む

24か月までの制限平均生存時間（RMST）は、無作為化から24か月までの生存曲線の面積である ([2](#ref-2))。原著で報告された12か月と24か月の生存割合はtarlatamabが55.9%と30.3%、化学療法が39.0%と14.9%だった ([1](#ref-1))。以下では報告値を固定し、曲線は1から始まり単調に下がるとする。生存割合が初めて0.5以下に達する時点を中央値とし、その時点で0.5を飛び越えて低下する場合も許した。

中央値と報告されたランドマークで時間を区切る。各区間の下限は、右側にある既知の生存割合の最大値である。中央値より前の区間では0.5も下限候補に含める。上限は左側にある既知の生存割合の最小値で、中央値以降なら高くても0.5とする。各上限・下限に区間幅を掛けて足す。例えばtarlatamab群の下限は $12(0.559)+1.6(0.5)+10.4(0.303)=10.6592$ か月になる。

**表1.** 抄録の報告値を順に加えた場合の24か月RMSTの上下限。群間差はtarlatamabから化学療法を引いた値。

| Information used | Tarlatamab (months) | Chemotherapy (months) | Difference (months) |
| --- | ---: | ---: | ---: |
| Median only | 6.80 to 18.80 | 4.20 to 16.20 | −9.40 to 14.60 |
| Median and 12-month OS | 7.51 to 18.09 | 5.60 to 14.88 | −7.37 to 12.49 |
| Median and 12- and 24-month OS | 10.66 to 18.09 | 7.39 to 14.88 | −4.22 to 10.70 |

表1では、12・24か月の生存割合を加えると群間差の幅は24.0か月から14.9か月に狭まる。それでも0をまたぐ。差の下限はtarlatamabの面積の下限から化学療法の上限を引いた値で、上限はその逆の組合せで求めた。区間の端に近いところで段差を作る曲線は、これらの境界に近づける。中央値より前に下限が0.5になる区間では、0.5をわずかに上回る値で近づける。追加のランドマークや曲線の情報なしには、範囲をさらに狭められない。

これは群間差の信頼区間ではない。丸められた報告値を固定して、曲線を省略した要約に何が残るかを測っている。ゼロを含むことは要約値の制約を示しており、試験で報告されたOS結果とは異なる問いである。[原著のFigure 1A](https://pmc.ncbi.nlm.nih.gov/articles/PMC13718749/#F1)には、計算に使っていないKaplan–Meier曲線もある ([1](#ref-1))。求めたい量が24か月でのRMST差なら、中央値の差5.2か月を代用するより、曲線の面積または試験データから求めた推定値とその不確実性を参照する必要がある。

## データとコードの公開状況

入力は原著の中央値とランドマーク生存割合で、個人データは用いていない。[再現用ZIP](shared/survival-landmark-rmst-bounds/companion.zip)にPythonコードと出力を収録した。

## 参照

1. <a id="ref-1"></a> Rudin CM, Ahn MJ, Schuler M, Blackhall FH, Mountzios G, Yoshida T, et al. Extended follow-up of tarlatamab in patients with small-cell lung cancer after platinum-based chemotherapy in the randomized phase III DeLLphi-304 study. Ann Oncol. 2026. [doi:10.1016/j.annonc.2026.10.095](https://doi.org/10.1016/j.annonc.2026.10.095).
2. <a id="ref-2"></a> Zhao L, Claggett B, Tian L, Uno H, Pfeffer MA, Solomon SD, et al. On the restricted mean survival time curve in survival analysis. Biometrics. 2016;72(1):215–221. [doi:10.1111/biom.12384](https://doi.org/10.1111/biom.12384).
