[English](zw209-repeated-challenge-en.html)

1回目と2回目の実験でほぼ同じ殺細胞活性を示したT-cell engager（TCE）が、3回目にも同じように働くとは限らない。DLL3×CD3×CD28抗体ZW209の公開ポスターでは、最初の2回には重なって見える三つの曲線が、3回目に分かれていた。

初回の強さと、その後も活性を保つことを分けて調べるため、最初の2点だけから後の点を予測した。ZW209では3回目の予測誤差が小さかった一方、CD28機能を除いた対照とAMG 757類似体では約92、86 percentage points（pp）の過大予測になった。この差は原著がすでに示した現象であり、新たな生物学的発見ではない。今回追加したのは、初期の測定だけでその分岐を予測できるかという、固定した外挿式の検証である。

## 反復刺激の測定単位

2026年10月23日、ZW209の初期臨床開発に関する契約が発表された。ただし、本解析のデータは臨床試験の結果ではなく、2025年AACR公開ポスターのFigure 2Bである（[開発発表](https://ir.zymeworks.com/news-releases/news-release-details/zymeworks-enters-exclusive-global-license-and-collaboration/)、[Lau et al., 2025, Figure 2](https://www.zymeworks.com/wp-content/uploads/2025/04/ZYME-AACR-2025-ZW209_final.pdf)）。

この実験は、DLL3陽性NCI-H82細胞とT細胞を使い、各刺激の後にT細胞を回収・計数し、新しい腫瘍細胞と抗体を加える。したがって、薬物濃度が体内で減る過程をそのまま観察した試験ではない。

比較対象はZW209、ZW209 CD28null、ポスターでAMG 757†と示された類似体である。最後の分子を市販製剤や臨床試験で使用した原薬と同一とはみなさない。Figure 2BにはZW209が5点、対照2分子がそれぞれ3点ある。ドナー数、独立実験数、分散はこのパネルに明示されていない。11点を11人の独立観測として扱うことはできない。

| 項目 | 今回の定義 |
| --- | --- |
| 問い（QOI） | 1・2回目の殺細胞活性から3回目をどの程度予測できるか |
| 用途（COU） | この培養実験内の反復刺激の外挿を評価する |
| 共通の検証対象 | 3分子の3回目の測定値 |
| 追加の観測 | ZW209だけの4・5回目。対照の未報告値は補わない |
| 対象外 | ヒトの投与量・投与間隔・臨床効果の推定 |

## 重なった点をPDFの描画情報から読む

最初の2回ではマーカーが重なるため、画像の見た目だけで別々の値を読み取るのは難しい。元PDFには各色のマーカーがベクトル図形として残っていた。`analysis/run.py`はFigure 2B内の位置と色を使ってマーカーを抽出し、図形の外接矩形の中心を観測位置とした。縦軸の0%と100%に対応するPDF座標から線形変換する。

抽出結果は`data/processed/vector-observations.csv`に、PDF内の座標とともに保存した。元画像を生成し直して観測を増やしたわけではない。図形の座標は元のドナー別測定値でもなく、公表図の描画位置である。

| 分子 | 1回目 | 2回目 | 3回目 |
| --- | ---: | ---: | ---: |
| ZW209 | 98.2% | 97.8% | 97.5% |
| ZW209 CD28null | 97.7% | 97.1% | 4.5% |
| AMG 757類似体 | 97.7% | 97.0% | 10.1% |

3回目を「反応なし」と表現する原ポスターの記述と、図上で0%を少し上回る値があることを区別した。今回の数値計算では抽出値を0に置き換えていない。

## 最初の2回から保持率を推定する

各刺激の後の殺細胞活性を\(A_n\)とし、刺激ごとに同じ割合\(r\)だけ活性が保たれると仮定した。

\[
A_n=A_1r^{n-1},\qquad
\widehat r=\frac{A_2}{A_1}.
\]

この2点による推定は数値最適化を必要としない。3回目の予測は\(\widehat A_3=A_2^2/A_1\)になる。推定には3回目以降の値を使わず、保持率の上限や下限を結果に合わせて変更しなかった。

\(n\)は刺激回数であり日数ではない。図の採取日は4・7・11・14・18日だが、日数間隔は一定ではないため、時間当たりの減衰率や半減期として解釈しない。また、殺細胞活性は生きたエフェクター数そのものではなく、\(r\)もT細胞の生存率ではない。

基準法は2回目の値をそのまま使う\(\widehat A_n=A_2\)とした。複雑な式が単純な据え置きより役立つかを確かめるためである。両方法の比較は全3分子で測定されている3回目にそろえた。

## 初期の保持率は3分子を区別しなかった

推定された\(r\)はZW209で0.9963、CD28nullで0.9944、AMG 757類似体で0.9937だった。いずれも初期2点がほぼ一定であることを表している。しかし3回目の結果は大きく異なった。

| 分子 | 保持率モデルの予測 | 公表図の観測 | 予測−観測 |
| --- | ---: | ---: | ---: |
| ZW209 | 97.5% | 97.5% | −0.1 pp |
| ZW209 CD28null | 96.6% | 4.5% | +92.0 pp |
| AMG 757類似体 | 96.4% | 10.1% | +86.4 pp |

![初期2点で校正した反復刺激後の予測](shared/zw209-repeated-challenge/figures/repeat-forecast.svg)

ZW209についても、3回目への近い予測だけでその後の全刺激を予測できたとはしない。4・5回目はZW209だけに報告されており、その線上の観測を図に残した。対照について実施されていない、または掲載されていない後続点を0%として補っていない。

| 方法 | 共通の3回目におけるRMSE | 平均絶対誤差 |
| --- | ---: | ---: |
| 一定保持率 | 72.9 pp | 59.5 pp |
| 2回目を据え置き | 73.3 pp | 59.9 pp |

出力は`outputs/tables/common-round-scores.csv`である。このRMSEは3分子の図上の要約値を平均した記述量であり、患者集団に対する予測誤差ではない。保持率モデルの小さな改善より、両方法が対照2分子の急な変化を捉えなかったことが重要である。

![3回目の外挿誤差](shared/zw209-repeated-challenge/figures/third-round-error.svg)

## 座標の微小な違いでは説明できない

3点それぞれの縦座標に独立な±0.5 PDF pointの変化を与え、固定シードで2,000通りを計算した。これは図形位置の取り方に対する感度分析であり、ドナー間変動や測定誤差の信頼区間ではない。

| 分子 | 3回目の予測誤差の範囲 |
| --- | ---: |
| ZW209 | −1.50〜+1.45 pp |
| ZW209 CD28null | +90.61〜+93.51 pp |
| AMG 757類似体 | +84.93〜+87.79 pp |

対照での過大予測はこの範囲でも残った。反面、ZW209の誤差が−0.1 ppという細かい値を強調する根拠はない。描画位置の取り方だけでも符号が変わる程度の差だからである。

## この実験から機序をどこまで言えるか

CD28nullとの比較はCD28機能の寄与を考える手掛かりになる。ただし、この図だけでは、細胞数、細胞状態、回収率、再播種条件などのどの違いが活性の持続を説明したかを定量的に分離できない。回収後に計数していることは示されるが、全刺激での投入生細胞数やE:T比の詳細はパネルから再構成できない。単純な保持率の失敗を、特定の疲弊機序を証明した結果とはしない。

また、2点への完全な当てはまりは予測能力を保証しない。このデータでは、初期活性が高いという情報だけでは3回目の差を識別できなかった。これは臨床効果の優劣ではなく、培養系での分子選択に使う測定期間の違いである。初期の濃度反応と反復刺激後の反応は、同じ情報として置き換えられない。

## 再実行資料

[コード・抽出表・結果表](shared/zw209-repeated-challenge/zw209-repeated-challenge-analysis.zip)。`analysis/download_sources.py`で公開PDFを取得し、`analysis/run.py`でベクトル抽出・予測・感度計算・新しい図表を作成する。元PDFと元図は配布しない。11個のマーカーの座標、抽出条件、元ファイルのSHA-256を記録した。

## References

Lau D, Repenning P, Canals Hernaez D, et al. ZW209, a DLL3 targeted trispecific T cell engager with integrated CD28 co-stimulation, demonstrates safety and potent preclinical efficacy in models of small cell lung cancer. AACR Annual Meeting 2025. Abstract 7318, Figure 2. [Public poster](https://www.zymeworks.com/wp-content/uploads/2025/04/ZYME-AACR-2025-ZW209_final.pdf). New analyses and figures were generated from displayed marker coordinates; the source poster is not redistributed.

Zymeworks. Zymeworks Enters into an Exclusive Global License and Collaboration Agreement with Roche for ZW209, a Trispecific T cell Engager Targeting DLL3. October 23, 2026. [Development announcement](https://ir.zymeworks.com/news-releases/news-release-details/zymeworks-enters-exclusive-global-license-and-collaboration/).

## Cite this article

Kumakura D. Can initial ZW209 cytotoxicity predict activity after repeated stimulation? Independent analysis of public figure coordinates. 2026. [Japanese](zw209-repeated-challenge.html); [English](zw209-repeated-challenge-en.html).
