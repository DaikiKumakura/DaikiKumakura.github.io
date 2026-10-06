抗PD-1抗体のpembrolizumabとnivolumabは、体重換算の用量（2 mg/kg、3 mg/kg）から固定用量（200 mg、240 mg）へ移行し、さらに投与間隔の長い方式（400 mg Q6W、480 mg Q4W）が加わった。体重の中央付近の患者では、どの方式でも曝露はほぼ同じになる。気になるのは分布の両端、つまり非常に軽い患者と非常に重い患者である。

本記事では、公表された母集団PKモデルを再実装し、米国の公開調査（NHANES）の成人の体重分布に当てはめた。そのうえで、体重帯ごとに曝露が「臨床試験で確かめられた範囲」から外れる割合を比べた。

先に結論を述べる。

- **重い側：** 固定用量では、pembrolizumab 200 mgで約150 kg以上、nivolumab 240 mgで約100〜120 kg以上の帯で、トラフ濃度が範囲の下限を下回る患者が10%を超えた。
- **軽い側：** 体重換算の方が、初回投与間隔のトラフが低くなりやすかった。
- **間隔の長い方式：** 評価が、トラフと平均濃度のどちらを基準にするかで正反対になった。

いずれも曝露の比較であり、効果の差を示したものではない。

## 先行研究との関係

固定用量への移行は、どちらの薬でも母集団PKモデルによる曝露の比較を根拠に行われた。

- **pembrolizumab 200 mg：** 体重が重い患者（90 kg超）で曝露が最も低くなるが、2 mg/kgで近最大の有効性が示された曝露の範囲には入る、と報告された［Freshwater 2017］。
- **pembrolizumab 400 mg Q6W：** 200 mg Q3Wと平均濃度がほぼ同じで、Q3W方式で観測されたトラフより低くなる患者は1%未満だった［Lala 2020］。
- **nivolumab 240 mg：** 3 mg/kgの80 kg相当として選ばれ、曝露の中央値と分布は3 mg/kgと同様だった［Zhao 2017］。
- **nivolumab 480 mg Q4W：** 3 mg/kgと比べて、平均濃度は同様、トラフは約16%低く、最高濃度は約45%高かった［Long 2018］。

これらはいずれも、試験の患者集団全体での比較である。本記事が加えるのは次の3点である。

1. 体重分布の端（50 kg未満の下位約3%、150 kg以上の上位約1.4%）に絞って見る。
2. 試験集団とは別の、一般成人の体重分布（NHANES）を使う。
3. 「範囲を保てる」を、計算の前に数値の規則として決めておく。

## 問いと使いみち

**問い（QOI）：** 固定用量は、体重換算用量と比べて、極端な体重の患者でも曝露を臨床試験で確かめられた範囲に保てるか。

**使いみち（COU）：** 固定用量への切り替えや、新しい抗体の投与方式を検討するとき、どの体重帯で追加の確認（低体重での曝露確認、高体重での安全性・曝露確認）が必要かを絞る。用量の推奨や臨床便益の評価には使わない。

**範囲の定義：** 計算する前に、次のように固定した。

- **下限：** 体重換算の基準方式（pembrolizumab 2 mg/kg Q3W、nivolumab 3 mg/kg Q2W）を同じ集団に投与したときの、定常状態トラフ（Cmin,ss）の5パーセンタイル。
- **上限：** 試験された最高用量（10 mg/kg Q2W）での、定常状態の最高濃度（Cmax,ss）の中央値。

ある体重帯で、下限を下回る患者が10%以下、かつ上限を超える患者が5%以下なら「範囲を保てる」とした。この下限・上限は、試験で使われた曝露の代理であり、効果や毒性の閾値ではない。

## モデルとデータ

**Pembrolizumab** は Ahamadi ら（2017）の最終モデル（Table 3）を使った。

- 2-compartment、線形、時間不変のCL（典型値0.22 L/day）。
- 体重の指数：CL・Qに0.595、Vc・Vpに0.489（基準76.8 kg）。
- 女性はCLが15%、Vcが13%低い。
- 個体差（IIV）：CLが38%CV、Vが21%CV。

論文の表の脚注には、CL 0.202、体重指数0.578という別の値の式もあった。体重指数0.578は、固定用量を評価した Freshwaterら（2017）が報告した値と同じで、同じモデルの別の版の値と考えられる。表の値を主解析に、脚注の値を感度解析に使った。

**Nivolumab** は Bajaj ら（2017）の最終モデル（Table 1）を使った。

- 2-compartment、線形で、CLが時間とともに下がる（最大約26%、sigmoid Emax、T50 1,410時間）。
- 体重の指数：CLに0.566、VCに0.597（基準80 kg）。
- 男性はCLが18%高い。
- CLとVCの個体差は相関している。

**仮想患者：** NHANES 2017〜2020年3月の成人8,811人を、調査重みで復元抽出して20,000人とした。体重と性は実データを使い、それ以外の共変量は各モデルの基準値に置いた。体重の中央値は80.7 kg、1〜99パーセンタイルは45.8〜156.3 kgである。

**計算：**
- rxode2で30分点滴を反復投与し、投与開始から52週以降の最初の投与間隔で曝露を求めた。
- 両剤とも線形PKなので、1 mgあたりの濃度を一度計算し、各方式の投与量を掛けた。
- 実装は10件の検査で確かめた（定常状態の平均濃度が dose/(CL·τ) と一致すること、論文の典型値の再現など）。

## 結果：重い側では固定用量の下限割れが増える

![体重帯別の定常状態トラフ濃度](shared/fixed-vs-weight-dosing/figures/01-trough-by-weight.png)

![体重帯別に下限を下回る割合](shared/fixed-vs-weight-dosing/figures/02-below-floor-by-weight.png)

下限を下回る割合（%）：

| 体重 | 2 mg/kg Q3W | 200 mg Q3W | 400 mg Q6W | 3 mg/kg Q2W | 240 mg Q2W | 480 mg Q4W |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| <50 kg | 6.9 | 0.2 | 3.5 | 7.4 | 0.7 | 3.5 |
| 50–60 kg | 6.1 | 0.6 | 6.0 | 6.9 | 1.7 | 6.8 |
| 60–80 kg | 5.4 | 1.9 | 10.4 | 5.5 | 3.9 | 10.6 |
| 80–100 kg | 5.0 | 3.7 | 15.5 | 4.5 | 6.3 | 16.6 |
| 100–120 kg | 4.2 | 5.9 | 21.3 | 4.2 | 10.7 | 23.2 |
| 120–150 kg | 2.6 | 7.0 | 25.8 | 2.9 | 14.2 | 26.8 |
| ≥150 kg | 3.0 | 13.3 | 31.0 | 2.6 | 18.5 | 31.0 |

固定用量では、体重が増えるほどトラフが下がる。
- **体重換算の方式：** すべての帯で判定を満たした。
- **pembrolizumab 200 mg：** 150 kg以上の帯だけが範囲外だった。
- **nivolumab 240 mg：** 100 kg以上で範囲外だった。体重の指数はnivolumab（0.566）の方がpembrolizumab（0.595）よりわずかに小さく、差の原因は指数ではない。240 mgは3 mg/kgの80 kg相当で、80 kgより重い患者は体重換算より少ない量を受ける。一方、200 mgは2 mg/kgの100 kg相当で、100 kgまでの患者は体重換算と同じかそれより多い量を受ける。固定用量をどの体重に合わせたかが、重い側の余裕を決めている。

**上限側：** ほぼ問題にならなかった。例外は480 mg Q4Wで、50 kg未満の帯で6.4%、体重40 kgの仮想患者で7.9%が、10 mg/kg Q2Wの最高濃度の中央値を超えた。

**軽い側：** 様子が逆になる。体重40 kgの仮想患者では、体重換算の方式で下限割れが12%前後に増えた。初回の投与間隔のトラフに限ると、26%（pembrolizumab）、31%（nivolumab）が、基準方式の初回トラフの5パーセンタイルを下回った。固定用量では、軽い患者の曝露はむしろ高くなる。

## 間隔の長い方式は、何を基準にするかで評価が変わる

400 mg Q6Wと480 mg Q4Wは、60〜80 kgの帯から下限割れが10%を超えた。ただしこれは体重のせいではない。投与間隔が2倍になれば、同じ平均濃度でもトラフは下がる。この下限は、Q3W・Q2Wの基準方式のトラフから定めたものである。

これは先行研究と矛盾しない。下限の置き方が違うからである。Lalaら（2020）は、Q3W方式で観測されたトラフ（の最低値の付近）を基準にし、それを下回る患者は1%未満とした。本記事で同じ基準（Q3W方式の仮想患者のトラフの最小値）を使うと、400 mg Q6Wで下回る患者は0.06%だった。本記事の下限は5パーセンタイルと厳しめにとっている。「範囲」を最低値で定義するか5パーセンタイルで定義するかで、間隔の長い方式の評価は大きく変わる。

解析計画にはない事後の確認として、平均濃度（Cavg,ss）で同じ判定をした。
- **間隔の長い方式：** 同じ投与速度の200 mg Q3W・240 mg Q2Wと、平均濃度の分布は同一になった。
- **重い側（150 kg以上）：** 固定用量の下限割れは、平均濃度で見ても13.7%（pembrolizumab）、22.5%（nivolumab）だった。

つまり、重い側の結論はトラフでも平均濃度でも変わらない。一方、間隔の長い方式の評価は、トラフを重視するか平均濃度を重視するかという、曝露指標の選択そのものに依存する。どちらを採るべきかは曝露反応の関係で決まり、このモデルだけでは決まらない。

## 感度解析

![重い帯（150 kg以上）での判定の安定性](shared/fixed-vs-weight-dosing/figures/03-sensitivity-heavy.png)

| 条件 | pembrolizumab 200 mg、≥150 kg | nivolumab 240 mg、≥150 kg |
| --- | ---: | ---: |
| 主解析 | 13.3% | 18.5% |
| 脚注の値（CL 0.202、指数0.578） | 12.9% | — |
| 体重の指数を95% CIの下端 | 9.2% | 13.3% |
| 体重の指数を95% CIの上端 | 14.4% | 24.4% |
| アジア人の体重分布 | 20.6% | 20.6% |
| 性を無視 | 10.7% | 18.8% |
| 低アルブミン（pembrolizumab） | 12.5% | — |
| 時間変化CLを無視（nivolumab） | — | 24.7% |

- **重い側の判定：** pembrolizumabは、体重の指数をCIの下端に置いた条件だけで10%を下回った。nivolumabは、すべての条件で10%を超えた。
- **体重換算の方式：** すべての条件・帯で判定を満たした。
- **アルブミン（体重以外の共変量）：** 30 g/Lにすると、pembrolizumabのCLは1.29倍になる。これは体重100 kgと150 kgの差（1.27倍）と同程度で、体重だけが曝露の両端を作るわけではない。

## 実装の確かめ

- **独立の再計算：** 計算の中心であるrxode2による曝露を、別の実装で計算し直した。各薬の仮想患者30人 × 4方式 × 4指標、計960の値で、相対差は最大1.1×10⁻⁵だった。別の実装とは、Pythonで投与ごとに微分方程式を直接積分し、1 mgあたりの濃度を掛ける近道を使わない計算である。
- **集計の再計算：** 下限・上限と体重帯ごとの割合も、曝露のファイルから計算し直し、一致した。
- **公表値との比較：** nivolumab 480 mg Q4W／3 mg/kgの比は、平均濃度0.98、トラフ0.79、最高濃度1.34で、Longら（2018）の「同様、約16%低い、約45%高い」と近かった。pembrolizumab 400 mg Q6W／200 mg Q3Wの平均濃度の比は1.00（Lalaら：約1%高い）、400 mg Q6Wの最高濃度は10 mg/kg Q2Wの31%（Lalaら：約65%低い）だった。
- **再現性：** 乱数のseedを固定しており、同じ結果ファイルが再生成される。

## 判断できること・できないこと

**判断できること：**
- 公表モデルと一般成人の体重分布のもとでは、固定用量は体重の上側の端でトラフ曝露が試験の範囲を下回りやすい。
- 体重換算は、下側の端の初回間隔で、曝露が範囲を下回りやすい。
- 追加の確認が必要な帯は、pembrolizumab 200 mgでは約150 kg以上、nivolumab 240 mgでは約100〜120 kg以上である。体重換算の方式では、40〜50 kgの初回間隔である。

**判断できないこと：**
- **効果の差：** これらの曝露差が効果の差になるかは、判断できない。抗PD-1抗体では曝露反応が平坦と報告されており、範囲の下限を少し下回ることが臨床的に問題になるかは、この解析の外にある。
- **集団の違い：** NHANESは米国の一般成人で、がん患者や日本人の体重分布ではない。アジア人の体重分布では、固定用量の重い側の帯の結果はむしろ悪くなった。ただし該当する人数は少ない。
- **共変量の相関：** 体重とアルブミンなど、共変量の間の相関は公開データから同定できないため、入れていない。

**次に必要なデータ：**
- 体重150 kg以上の患者で実測したトラフ濃度。
- 体重の両端での曝露と反応の関係。

固定用量か体重換算かの議論は、平均的な患者ではなく分布の端で決着させるべきである。そのためには、どの曝露指標を「守るべき範囲」とするかを先に決めておく必要がある。

## 出典

- Ahamadi M, et al. Model-based characterization of the pharmacokinetics of pembrolizumab: a humanized anti-PD-1 monoclonal antibody in advanced solid tumors. *CPT Pharmacometrics Syst Pharmacol*. 2017;6:49–57. [doi:10.1002/psp4.12139](https://doi.org/10.1002/psp4.12139)
- Bajaj G, et al. Model-based population pharmacokinetic analysis of nivolumab in patients with solid tumors. *CPT Pharmacometrics Syst Pharmacol*. 2017;6:58–66. [doi:10.1002/psp4.12143](https://doi.org/10.1002/psp4.12143)
- Freshwater T, et al. Evaluation of dosing strategy for pembrolizumab for oncology indications. *J Immunother Cancer*. 2017;5:43. [doi:10.1186/s40425-017-0242-5](https://doi.org/10.1186/s40425-017-0242-5)
- Lala M, et al. A six-weekly dosing schedule for pembrolizumab in patients with cancer based on evaluation using modelling and simulation. *Eur J Cancer*. 2020;131:68–75. [doi:10.1016/j.ejca.2020.02.016](https://doi.org/10.1016/j.ejca.2020.02.016)
- Zhao X, et al. Assessment of nivolumab benefit–risk profile of a 240-mg flat dose relative to a 3-mg/kg dosing regimen in patients with advanced tumors. *Ann Oncol*. 2017;28:2002–2008. [doi:10.1093/annonc/mdx235](https://doi.org/10.1093/annonc/mdx235)
- Long GV, et al. Assessment of nivolumab exposure and clinical safety of 480 mg every 4 weeks flat-dosing schedule in patients with cancer. *Ann Oncol*. 2018;29:2208–2213. [doi:10.1093/annonc/mdy408](https://doi.org/10.1093/annonc/mdy408)
- Centers for Disease Control and Prevention, National Center for Health Statistics. National Health and Nutrition Examination Survey 2017–March 2020 Pre-Pandemic: Body Measures (P_BMX), Demographic Variables (P_DEMO). <https://wwwn.cdc.gov/nchs/nhanes/>

再実行：`Rscript test_analysis.R && Rscript analysis.R && Rscript figures.R && Rscript export_params.R && python validate.py`（R 4.5.3、rxode2 5.1.8、ggplot2 4.0.2；Python 3.12、scipy、pandas）。

解析計画・コード・集計結果・検証結果は配布資料に含めた（[配布資料](shared/fixed-vs-weight-dosing/fixed-vs-weight-dosing-companion.zip)）
