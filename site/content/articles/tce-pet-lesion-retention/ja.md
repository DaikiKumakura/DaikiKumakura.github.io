[English](tce-pet-lesion-retention-en.html)

投与直後の画像で腫瘍への取り込みが見えても、その後まで同じ動きが続くとは限らない。CEA×CD3 T-cell engagerのAMG 211を使ったヒトPET研究の公開表から、早い2時点の信号で翌日の病変信号を予測できるかを調べた。

3時間から6時間の対数変化率を24時間まで延長する式は、6時間値をそのまま使う方法より大きく外れた。他の患者から残留係数を推定しても、6時間値を使う基準法を対数誤差で上回らなかった。対象は完全な3時点がそろう16病変・4患者であり、16人の検証ではない。

## 37病変から16病変への絞り込み

原研究では、⁸⁹Zr標識AMG 211の体内分布をPETで測定している。研究全体の対象は9患者だが、今回使用した公開Supplementary Table S3には、定量可能な37病変・6患者のSUVmaxが載っている。全体の人数と、今回の予測評価に使える人数を分ける必要がある（[Moek et al., 2019](https://pubmed.ncbi.nlm.nih.gov/30745297/)、[Supplementary Table S3](https://aacr.figshare.com/articles/journal_contribution/22470416)）。

| 表中の患者ID | 記載病変数 | 3時点がそろう病変数 | 除外理由 |
| --- | ---: | ---: | --- |
| 1 | 13 | 0 | 3時間の撮像なし（ND） |
| 2 | 4 | 4 | なし |
| 3 | 4 | 4 | なし |
| 5 | 7 | 7 | なし |
| 7 | 8 | 0 | 6時間の技術的不成立（NE） |
| 8 | 1 | 1 | なし |
| 合計 | 37 | 16 | 完全例は4患者 |

NDとNEはゼロに置き換えていない。単位は病変で、同じ患者の病変を別の患者として学習と評価に分けることもしない。解析用の表は公開DOCXのXMLから直接読み込んだ。図の曲線からの数値化ではない。

問いは、表で3・6・24時間とされた同じ病変のSUVmaxについて、24時間値を使わずに予測できるか、である。用途は研究段階での撮像時点の省略可能性を検討するベンチマークに限る。SUVmaxは病変内の放射能信号で、活性型TCEの濃度ではない。

![Figure 1. 同じ病変の3時点のSUVmax](shared/tce-pet-lesion-retention/figures/lesion-trajectories.svg)

原表の撮像時点を3・6・24時間として計算した。患者別の正確な撮像開始時刻はこの表にないため、個別の実測経過時間を再構成していない。補足方法には、放射性標識体単独と非標識AMG 211を加えた投与条件が記されている。ここでは患者別投与条件による補正モデルを推定していない（[Supplementary methods](https://aacr.figshare.com/articles/journal_contribution/22470416)）。

## 早期の変化率を延長する式

病変のSUVmaxを\(S_t\)とする。比較したのは次の三つである。

**6時間値をそのまま使う基準法**

\[
\widehat S_{24}=S_6.
\]

**3–6時間の対数変化率をそのまま延長する方法**

\[
k_{3\to6}=\frac{\log(S_6/S_3)}{6-3},\qquad
\widehat S_{24}=S_6\exp\{k_{3\to6}(24-6)\}
=S_6\left(\frac{S_6}{S_3}\right)^6.
\]

これは信号が一定の対数変化率を保つという仮定である。薬剤の消失速度や放射性核種の物理的半減期を推定した式ではない。

**他の患者から残留係数を推定する方法**

\[
\log r_{-p}=\frac1{P-1}\sum_{q\ne p}\frac1{n_q}
\sum_{j=1}^{n_q}\log\frac{S_{24,qj}}{S_{6,qj}},\qquad
\widehat S_{24,pj}=S_{6,pj}r_{-p}.
\]

患者\(p\)を丸ごと外し、残り3患者から係数を推定する。患者内の病変を平均してから患者間で平均するため、病変数が多い患者だけで係数が決まらない。予測対象の患者の24時間値は、その係数の推定に一つも入らない。

## 一定の対数変化率は続かなかった

![Figure 2. 三つの方法による24時間SUVmaxの予測](shared/tce-pet-lesion-retention/figures/prediction-scatter.svg)

比較のため3パネルの縦軸をそろえた。極端に大きい予測も切り捨てていない。破線は予測と観測が等しい線である。

各患者の平均二乗対数誤差を計算し、4患者を等しい重みで平均した平方根を主指標とした。補助的に、患者ごとのSUV絶対誤差の平均も示す。

| 方法 | 患者を等重みとした対数RMSE | 患者を等重みとしたSUVのMAE |
| --- | ---: | ---: |
| 6時間値を使用 | 0.653 | 1.577 |
| 早期対数変化率を延長 | 3.604 | 7,770.357 |
| 他患者の残留係数 | 0.689 | 1.413 |

出力は`outputs/tables/overall-scores.csv`。残留係数はMAEをやや小さくしたが、対数RMSEは改善しなかった。指標の選択によって見え方が異なるため、全体として予測を改善したとは結論しない。

大きな誤差の例は患者3の病変4である。表のSUVmaxは2.4→11.3→3.3だった。早期の上昇を延長すると、24時間の予測は約123,107になった。元表の11.3を誤記と決めつけて修正したり、予測を任意の上限で切ったりしていない。この例は、早期の取り込み速度を長時間の一定速度と見なす仮定が破綻することを示す。

![Figure 3. 患者を丸ごと外したときの予測誤差](shared/tce-pet-lesion-retention/figures/patient-error.svg)

## 一病変だけの問題ではない

最大の早期上昇を示した患者3の病変4を除く、事後的な影響確認も計算した。主解析は除外前の16病変のままである。残る15病変では、対数RMSEは6時間値で0.586、早期傾きの延長で2.515、他患者の残留係数で0.646だった。極端な一病変を除いても、早期傾きの延長は基準法より悪かった（`outputs/tables/influence-exclusion.csv`）。

表の小数第1位の表示を踏まえ、各SUVに独立な±0.05を加えた500回のシナリオでは、対数RMSEの範囲は順に0.629–0.676、3.538–3.663、0.662–0.716だった。これは入力数値の丸めに対する感度で、4患者を超える集団の信頼区間ではない（`outputs/tables/rounding-sensitivity.csv`）。

完全例だけを対象にしていることも制約になる。撮像欠損の21病変について同じ予測性能が得られるかは分からず、他の薬剤・標的や投与条件への移植も検証していない。病変ごとの測定誤差、SUVmaxのノイズ、血流や結合・内在化などの寄与を、この3時点から分けることもできない。

今回の4患者では、3–6時間の傾きを24時間まで伸ばす根拠は得られなかった。PETで見える早期の取り込みと翌日の残留は、同じ一定速度の過程として扱えない。6時間値からの簡単な予測にも誤差が残り、このデータは24時間の撮像を置き換えられることを支持していない。

## 再実行資料

[解析コード・抽出表・出力表](shared/tce-pet-lesion-retention/tce-pet-lesion-retention-analysis.zip)。`analysis/download_sources.py`で公開補足表を取得し、`analysis/run.py`で抽出・予測・図表作成を再実行する。`python -m unittest discover -s tests`で患者単位の除外と係数推定を検査する。原DOCXは配布物に含めず、取得URL・ライセンス・SHA-256を記録した。

## References

Moek KL, Waaijer SJH, Kok IC, et al. 89Zr-labeled Bispecific T-cell Engager AMG 211 PET Shows AMG 211 Accumulation in CD3-rich Tissues and Clear, Heterogeneous Tumor Uptake. *Clinical Cancer Research*. 2019;25(12):3517–3527. [doi:10.1158/1078-0432.CCR-18-2918](https://doi.org/10.1158/1078-0432.CCR-18-2918).

Moek KL, et al. Supplementary Data_clean. Supplementary methods and Table S3. [Publisher-linked public supplement](https://aacr.figshare.com/articles/journal_contribution/22470416). CC BY 4.0.

## Cite this article

Kumakura D. Can early PET predict next-day lesion retention of a T-cell engager? 2026. Independent reanalysis of published lesion-level SUVmax data.
