このサイトの解析で、再実装した、公開データに当てはめた、または公表された推定値をそのまま使った、文献のモデルの一覧である。解析はすべて公開情報またはシミュレーションだけを使った研究と学習のための解析で、投与の提案ではない。各行に、*論文から再実装した*のか*公開データから推定した*のかを書いてある。この2つは、支える主張が違うからである（[公表された母集団PKモデルの再実装](../glossary/poppk-reimplementation-ja.html)を参照）。

| 薬剤とモデル | 出典 | 構造 | 解析で行ったこと | 記事 |
| --- | --- | --- | --- | --- |
| mosunetuzumabの母集団PK（静注） | [Benderら、2024](https://doi.org/10.1111/cts.13825)。推定値は[Liら、2025](https://doi.org/10.1002/cpt.3445)でも確認 | 2-compartment、時間変化するクリアランス、CD20結合 | Pythonで再実装。ステップアップ投与の曝露を比較。受容体占有率からCRSへの結びつきは探索的に検討 | [公表されたmosunetuzumabモデルの再実装](../writing/mosunetuzumab-public-pk.html) |
| pembrolizumabの母集団PK | [Ahamadiら、2017](https://doi.org/10.1002/psp4.12139)（Table 3） | 2-compartment、線形、時間不変のクリアランス、体重の指数 | R（rxode2）で再実装。固定用量、体重換算、400 mg Q6Wの体重帯別の曝露 | [抗PD-1抗体の固定用量](../writing/fixed-vs-weight-dosing.html)・[エクスプローラー](../tools/anti-pd1-exposure-ja.html) |
| nivolumabの母集団PK | [Bajajら、2017](https://doi.org/10.1002/psp4.12143)（Table 1） | 2-compartment、線形、時間変化するクリアランス、体重の指数 | R（rxode2）で再実装。固定用量、体重換算、480 mg Q4Wの体重帯別の曝露 | [抗PD-1抗体の固定用量](../writing/fixed-vs-weight-dosing.html)・[エクスプローラー](../tools/anti-pd1-exposure-ja.html) |
| tarlatamabの母集団PK | FDAの審査報告書（2024）の公表された固定効果。[Kongら、2025](https://doi.org/10.1007/s40262-025-01499-z) | 線形の2-compartment | 公表された推定値を使い、平均曝露をそろえた投与方式を比較 | [平均曝露をそろえるだけでtarlatamabの投与間隔を決められるか](../writing/tcell-engager-regimen-design.html) |
| tarlatamab（公表されたPKの要約値から） | 公開されたPKの要約値。背景として[Kongら、2025](https://doi.org/10.1007/s40262-025-01499-z) | 線形の2-compartment（6つの要約値に4つのパラメータ） | 再実装ではなく、要約値への当てはめ。値が何を決め、何が仮定に依存するかを検討 | [公開されたPKの要約値で投与間隔の変更をどこまで評価できるか](../writing/tarlatamab-summary-pk.html) |
| nimotuzumabの母集団PK | データ`nimoData`（nlmixr2data）。背景として[Rodríguez-Veraら、2015](https://doi.org/10.1002/jcph.496) | 3候補：線形の1-compartment、線形の2-compartment、非線形消失のある2-compartment | nlmixr2で、公開された濃度データから推定。曝露の比較に必要な構造を検討（元のモデルの再現ではない） | [母集団PKモデルはどこまで複雑である必要があるか](../writing/nimotuzumab-poppk.html) |
| warfarinのPK/PD | データ`warfarin`（nlmixr2data）。PK/PDの考え方は[Wrightら、2011](https://doi.org/10.1111/j.1365-2125.2011.03925.x) | ラグのある経口の1-compartment、ターンオーバー型の反応 | 公開データから推定。個人の情報が予測をいつ改善するかを検討 | [個人の情報はいつPK/PD予測を改善するか](../writing/warfarin-pkpd.html) |
| RMC-6236（RAS阻害薬） | [Jiangら、2024](https://doi.org/10.1158/2159-8290.CD-24-0027)、補足のTable S8 | 経口の1-compartmentの血中PK、腫瘍との交換、間接的なDUSP6の反応 | 補足の点推定値を再利用。標的の占有のシナリオを計算 | [RAS阻害薬の用量：公開されたPK/PDデータから標的の占有のシナリオへ](../writing/ras-inhibitor-target-coverage.html) |

## 注

- 公表値と一致することは、モデルを正しく作り直せたことを示す。別の集団や投与方式を予測するモデルとして妥当かどうかは示さない。
- 出典に不一致（たとえば表の値と脚注の値が違う）があったときは、記事で報告し、両方の版を試している。
- [抗PD-1抗体の解析の配布資料](../writing/shared/fixed-vs-weight-dosing/fixed-vs-weight-dosing-companion.zip)に、コード、結果、独立の再計算が入っている。

関連：[PK/PDモデルの識別可能性](../glossary/structural-identifiability-ja.html)、Rパッケージ[pkident](../software/pkident.html)。
