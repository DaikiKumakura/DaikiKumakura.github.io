無作為化した2用量のどちらを次の試験へ持ち込むか。小規模試験では、高用量の奏効率が少し高くても、差が投与量の増加に見合うか、毒性が許容範囲に収まるかは別の問いになる。FDAのオンコロジー用量最適化ガイダンスは、安全性と抗腫瘍活性を各用量で評価を推奨している ([1](#ref-1))。ROSEは、事前に定めた正選択の確率を用いて無作為化比較の規模を決める設計の一例だ ([2](#ref-2))。ここでは、即決すべきか証拠を待つべきかを数値実験で比べた。

## 保留を選択肢に加える

仮想試験では同じ人数を低用量と高用量に割り付けた。真の母集団奏効率が高用量で8ポイント以上増え、かつ高用量の毒性率が25%以下なら、高用量を正解とした。全条件で低用量の真の毒性率は25%以下だった。母集団率は用量ごとに40万個体を生成して近似した。奏効率と毒性率は一つの評価窓内の二値結果で、閾値は比較のために置いた値である。

同じ試験標本に三つの規則を適用した。群別規則は割付群の観測割合、曝露–反応規則は全患者の対数曝露に対するロジスティック回帰を使う。後者は重症度を回帰に入れず、曝露が用量に比例すると仮定して両用量の割合を計算した。両規則とも、二つの基準を満たさなければ低用量を選ぶ。3択規則では、割付群の奏効率差の下限が8ポイント以上、かつ高用量毒性率の上限が25%以下なら高用量を選ぶ。低用量毒性率の上限が25%以下で、奏効率差の上限が8ポイントを下回るか高用量毒性率の下限が25%を超えれば低用量とする。残りは保留とした。毒性はWilson境界、奏効率差はWilson境界を組み合わせたNewcombe型の境界を使った ([3](#ref-3))。各成分の名目片側水準は90%。試験全体の誤判定率を90%という数値から読み取ることはできない。

## 人数を増やしても交絡は残る

便益が明確、頭打ち、毒性超過の3条件を、重症度によるクリアランス上昇の有無と各群40・100人に組み合わせ、12条件を各2,000回反復した。重症度が高い患者が奏効しにくく、かつ曝露も低くなる設定では、群をプールした曝露–反応の傾きに重症度の影響が混ざる。用量比は2:1で、交絡ありの条件では重症度1 SDあたりCLを1.49倍、奏効のlog-oddsを0.6低下させた。無作為化は投与量の割付に対して行われ、測定された曝露を無作為に割り付けるわけではない。

表1に代表的な4条件を示す。

**表1.** 2用量比較の誤選択率と保留率。

| Scenario | Patients per arm | Arm-rate error | Exposure–response error | Three-way error | Three-way deferral |
| --- | ---: | ---: | ---: | ---: | ---: |
| Clear benefit without confounding | 40 | 18.70% | 12.75% | 1.15% | 75.45% |
| Plateau with confounding | 40 | 27.95% | 74.55% | 1.95% | 79.95% |
| Plateau with confounding | 100 | 25.00% | 87.55% | 1.90% | 65.65% |
| Excess toxicity with confounding | 40 | 13.95% | 11.05% | 0.10% | 73.25% |

交絡のある頭打ち条件では、各群40人で曝露–反応の正選択率が群別規則より46.6ポイント低かった。対応のある差のMonte Carlo 95%区間は−49.0〜−44.2ポイント。各群100人に増やすと差は−62.55ポイントに広がった。この区間は患者での効果の不確実性を表さず、有限回のシミュレーションによる誤差を表す。

3択規則は誤選択を減らしたが、頭打ち・40人では8割近くを保留した。誤選択の損失を1、保留の損失を $c$ とする単純な比較では、推定平均損失は3択で $0.0195+0.7995c$、群別規則で $0.2795$ となる。ここで3択が有利なのは $c$ が約0.325より小さいときだ。たとえば保留の損失を0.5と置けば、その順位は逆になる。どちらの用量を誤って選ぶかで損失が違う試験には、同じ境界を持ち込めない。

シミュレーションに中止、時変曝露、遅発毒性は入れていない。結論は、指定した真値と評価窓に対して、保留の費用を明示すると候補規則の比較が変わる、という範囲に留まる。

## データとコードの公開状況

[再現用ZIP](shared/dose-selection-with-deferral/companion.zip)にRコードと全結果を収録した。

## 参照

1. <a id="ref-1"></a> US Food and Drug Administration. Optimizing the Dosage of Human Prescription Drugs and Biological Products for the Treatment of Oncologic Diseases. Guidance for Industry. 2024. [FDA guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/optimizing-dosage-human-prescription-drugs-and-biological-products-treatment-oncologic-diseases).
2. <a id="ref-2"></a> Wang S, Yuan Y, Liu S. Randomized optimal selection design for dose optimization. Biometrics. 2025;81(4):ujaf124. [doi:10.1093/biomtc/ujaf124](https://doi.org/10.1093/biomtc/ujaf124).
3. <a id="ref-3"></a> Newcombe RG. Interval estimation for the difference between independent proportions: comparison of eleven methods. Stat Med. 1998;17:873–890. [PubMed](https://pubmed.ncbi.nlm.nih.gov/9595617/).
