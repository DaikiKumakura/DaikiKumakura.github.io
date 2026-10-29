[English](amplify7p-response-denominator-en.html)

KRASワクチンで「99%に免疫応答」と聞いたとき、その99%は患者の腫瘍に存在するKRAS変異への応答を表しているだろうか。AMPLIFY-7Pの公開資料では、何らかのワクチンペプチドへの応答と、自分の腫瘍変異に対応するペプチドへの応答を分けて報告している。

前者は89/90、後者は応答者89人中78人だった。同じ90人を分母に置くと98.9%と86.7%になる。数字の誤りを見つけたのではなく、異なる問いに答えている数字を同じものとして読まないための再集計である。

## 評価対象をそろえる

Camupepimut（ELI-002 7P）は7種類の変異KRASペプチドを含む。2026年10月23日に公表された無作為化第2相試験では、ワクチン群96人、観察群48人が比較された。主要DFS評価項目は未達だった。一方、免疫応答評価可能なワクチン群90人のうち89人に、いずれかのペプチドに対する応答が報告されている（[George et al., 2026](https://doi.org/10.1038/s41591-026-04734-7)）。

ここでの問い（QOI）は、免疫応答の対象と分母をそろえると、公表応答率がどう変わるかである。用途（COU）は、公開免疫学データの解釈とバイオマーカーの定義を点検することに限る。治療の有効性を再判定する解析や、患者選択モデルではない。

使用したのは原著のFigure 5 Source Dataである。Figure 5bはワクチン抗原に対する患者別最大fold change、Figure 5iは腫瘍変異に対応した応答の最大fold changeを収録する。ただし前者に数値があるのは89人、後者は78人だった。図の行数91から「90人全員の応答強度がそろう」と判断すると、空欄を誤って埋めることになる。

| 項目 | 確認できた件数 | 解釈 |
| --- | ---: | --- |
| ワクチン群に無作為化 | 96 | 試験の割付集団 |
| 免疫応答評価可能 | 90 | 今回の応答率の主な分母 |
| Figure 5bの正の最大応答 | 89 | 何らかのワクチン抗原への応答者 |
| Figure 5iの正の最大応答 | 78 | 腫瘍変異に対応する応答者 |
| 両パネルの数値をIDで対応できる例 | 78 | 両方で正の要約値がある選択集団 |

78人のIDはすべて89人の集合に含まれ、パネル内のID重複はなかった。欠けた12人について、腫瘍変異へのfold changeをゼロとしたり、1としたりしていない。以下の再集計は`analysis/run.py`、行数・粒度の監査は`outputs/data-quality-audit.json`から再現できる。

## 89人を分母にする場合と90人を分母にする場合

(A)をいずれかのワクチン抗原への記録された応答、(T)を患者の腫瘍変異に対応したペプチドへの記録された応答とする。公表集計では(T)の応答者は(A)の応答者の部分集合である。

\[
\widehat P(A\mid E)=\frac{89}{90},\qquad
\widehat P(T\mid A,E)=\frac{78}{89},\qquad
\widehat P(T\mid E)=\frac{78}{90},
\]

ここで(E)は免疫応答の評価が可能だったことを表す。生物学的な潜在応答の確率ではなく、報告された応答分類の割合として記述している。

| 応答の定義 | 分子/分母 | 再集計率 | Wilson 95%区間 |
| --- | ---: | ---: | ---: |
| いずれかのワクチン抗原への応答 / 評価可能者 | 89/90 | 98.9% | 94.0–99.8% |
| 腫瘍変異への応答 / 何らかの抗原への応答者 | 78/89 | 87.6% | 79.2–93.0% |
| 腫瘍変異への応答 / 評価可能者 | 78/90 | 86.7% | 78.1–92.2% |

同じ90人で比べた差は12.2 percentage pointsだった（`outputs/tables/response-denominators.csv`）。これは異なる二つの治療群の差ではない。単一のワクチン群で、応答の定義を狭めたときの差である。独立した二標本の検定は行っていない。

![応答の定義と分母を変えた再集計](shared/amplify7p-response-denominator/figures/response-denominators.svg)

区間は各分母に条件づけた二項割合のWilson区間であり、欠測・検査誤差・観察時点の選択を含む総合的な不確実性ではない。また三つの推定値は互いに独立ではなく、区間の重なりから差の有意性を判定するものでもない。

## 最大応答の強さも同じではない

両パネルで正の数値が得られる78人だけをIDで対応させた。ワクチン抗原全体の最大応答の中央値は52.58倍、腫瘍変異への最大応答は11.445倍だった。患者内の「腫瘍変異への最大応答 / 全抗原での最大応答」の比の中央値は0.374、四分位範囲は0.133–0.787となった（`outputs/tables/paired-positive-summary.csv`）。

![両パネルに正の要約値がある78人の比較](shared/amplify7p-response-denominator/figures/paired-positive-folds.svg)

これは78人を選んだ後の記述統計である。90人全体の腫瘍変異への応答分布ではない。また、複数の抗原や測定機会から取った最大値と、特定の抗原に限定した最大値を比較している。前者が大きくなりやすいこと自体に、選択操作の影響が含まれる。

測定はex vivo Fluorospotまたはintracellular cytokine staining（ICS）による。原著ではfold changeだけでなく、ベースラインからの増加とアッセイの絶対閾値を組み合わせて応答を判定している。今回のスクリプトで「fold changeが2以上」という条件だけから新しい応答者を発見したわけではない。公表済みの正の要約値の件数を照合した。

これらは採血時点をそろえた同時比較でもない。腫瘍細胞への実際の認識、腫瘍へのT細胞移行、殺細胞活性の大きさを、この比から推定することはできない。

## 評価できなかった6人を含めるとどうなるか

96人の割付集団と90人の免疫評価集団には6人の差がある。ここではその6人に仮想の応答を割り当てず、全員が記録上の応答に該当しない場合と、全員が該当する場合の算術的な幅を計算した。

\[
\frac{k}{96}\le p_{\mathrm{all}}\le\frac{k+6}{96}.
\]

既に評価された90人の公表応答分類を固定した場合の範囲である。脱落の原因を説明するモデルや、未評価者の真の応答率を推定するモデルではない。

| 定義 | 96人を分母にした範囲 |
| --- | ---: |
| いずれかのワクチン抗原への応答 | 92.7–99.0% |
| 腫瘍変異に対応した応答 | 81.3–87.5% |

![未評価6人の分類を変えた場合の算術的な幅](shared/amplify7p-response-denominator/figures/ascertainment-bounds.svg)

この幅は信頼区間ではない。割付後に評価できた人だけを分母にする割合と、割付集団全体での割合が異なることを示している。原著の「評価可能者の98.9%」を否定する計算ではない（`outputs/tables/ascertainment-bounds.csv`）。

## 免疫応答と治療効果の距離

最大免疫応答による生存曲線の群分けは、ベースラインで無作為化された比較ではない。免疫応答の評価まで追跡できることや、その間の病状・採血機会も関係する。今回の集計から「応答を強くすればDFSが改善する」という因果関係は求められない。

2025年の免疫原性資料には540/630の抗原単位応答が載る一方、2026年原著には免疫応答者89人に限定した543/623が載る。分母だけでなく集計対象・報告時点も異なるため、この二つを同一の固定データのように混ぜていない。患者ごとの7抗原を独立した630人として扱うこともしていない（[2025年公開資料](https://elicio.com/wp-content/uploads/2025/09/Immunogenicity-Data-9-4-25.pdf)、[2026年原著](https://doi.org/10.1038/s41591-026-04734-7)）。

本解析では、99%という数値は「評価できた患者のいずれかのワクチン抗原への応答」を表し、腫瘍変異に対応する応答を同じ分母で数えると86.7%になった。どちらも臨床効果そのものではない。今回の公開要約値で確認できたのは、応答の対象・評価集団・最大値の選び方によって、同じ試験の数値が異なるということである。

## 解析資料

[再実行コードと集計表](shared/amplify7p-response-denominator/amplify7p-response-denominator-analysis.zip)。公開Source Dataをハッシュ確認して取得し、集計・図表を再生成する。元のワークブック、原図、患者別の派生表は配布しない。数値は`outputs/results.json`に保存した。

## References

George B, Singh H, Devoe CE, et al. Lymph node-targeted, mKRAS-specific amphiphile vaccine in pancreatic cancer: the randomized phase 2 AMPLIFY-7P trial. *Nature Medicine*. Published October 23, 2026. [doi:10.1038/s41591-026-04734-7](https://doi.org/10.1038/s41591-026-04734-7). Figure 5 Source Data, CC BY-NC-ND 4.0. This article reports independent calculations and newly drawn figures; original figures and participant records are not redistributed.

Elicio Therapeutics. AMPLIFY-7P Phase 2 immunogenicity data. September 2025. [Public presentation](https://elicio.com/wp-content/uploads/2025/09/Immunogenicity-Data-9-4-25.pdf).

## Cite this article

Kumakura D. What does a 99% immune-response rate count in a KRAS vaccine trial? Independent reanalysis of published AMPLIFY-7P response summaries. 2026.
