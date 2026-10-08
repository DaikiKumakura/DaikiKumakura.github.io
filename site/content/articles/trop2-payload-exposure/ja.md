Sacituzumab govitecan（SG）とdatopotamab deruxtecan（Dato-DXd）は、どちらもTROP2を標的とするADCである。新しいTROP2 ADCの開発で、既存薬のpayload曝露を参照したくなる。しかし、単位を揃える前に確認すべきことがある。**「ADCの濃度」が、何を測り、どう計算した値なのか**である。

SGの旧ラベルと2026年版を比べると、初回投与後168時間のADC AUCの記載値は2.136倍になっている。一方、free SN-38のAUCの記載値差は−5.0%だった。患者の曝露が経年的に倍増したという結果ではない。公開審査資料は、ADC濃度の算出とPopPKモデルの変更を説明している。

本記事では、2薬の曝露を数値で順位付けする前に、その比較を採用できる条件を調べた。結論は、**今回の集約PKとE–R情報から、共通のpayload曝露目標や効力順位は作れない**。その理由を「薬が違う」で終わらせず、測定値・派生値・時間窓・転帰の違いまで分解する。

## 問いと使用範囲

QOIは「公表PK・E–Rから、TROP2 ADC間で移せるpayload曝露目標や比較順位を作れるか」。COUは公開資料による研究と、次に収集する情報の優先度の検討である。患者の治療や臨床試験の用量決定には使わない。

ラベル版履歴、原著、2026年の審査資料を確認し、単位変換と派生濃度の感度を計算した。患者別の濃度データからPopPKを推定した解析ではなく、既存モデルの全面再実装でもない。計画は資料探索後、数値計算前に固定した。

## 同じ「SG濃度」でも算出方法が違う

2024年のSG PopPK原著では、total SN-38とfree SN-38をLC–MS/MSで、total antibodyを別の測定法で定量している。SG濃度は、結合SN-38とDAR=8の仮定から算出した。**直接測定したtotal antibodyと、この派生SG濃度は同じ量ではない。** [1]

2026年のEMA審査では、total antibody、free SN-38、total SN-38を扱う統合モデルへ変更し、時間とともに変わるDARからSG濃度を計算している。審査はDAR導入をAUC・半減期変更の主要な要因として説明する。同時に、派生SG濃度はモデルに依存し、確認データがないことも指摘している。これは測定法そのものが変更されたという説明ではない。[2, 印字p18–20、34]

| SGのラベル記載値 | 旧版18 | 2026年版20 | 今回計算した記載値差 |
| --- | ---: | ---: | ---: |
| ADC AUC0–168（ng·h/mL） | 5,640,000 | 12,049,500 | 2.136倍 |
| Free SN-38 AUC0–168（ng·h/mL） | 3,696 | 3,510 | −5.0% |
| Free SN-38 Cmax（ng/mL） | 98.0 | 108 | +10.2% |

旧版は単剤投与、現行版は単剤・pembrolizumab併用を含む集団の要約であり、モデルと患者構成も同一ではない。[3, 4] **この2.136倍の全量をDARだけの因果効果として分解することはできない。** 同一患者・同一濃度時系列を両定義で再計算した比較ではなく、記載値差には信頼区間を付けなかった。

![SGのラベル記載値の比較](shared/trop2-payload-exposure/figures/label-version-differences.png)

図1：現行／旧版の記載値比。3つの集約指標を比較したもので、患者数3ではない。破線は記載値が同じ場合を示す。臨床的な曝露変化やモデル改善の程度を表す図ではない。

## DARは単純なスケール補正ではない

結合payloadのモル濃度を $P(t)$ とすると、定義の違いは次のように表せる。

$$
C_{old}(t)=\frac{P(t)}{8},\qquad
C_{new}(t)=\frac{P(t)}{DAR(t)}.
$$

同じ $P(t)$ を使う場合、瞬間的な濃度比は $8/DAR(t)$ である。積分比は、単なる時間平均DARの逆数ではない。

$$
\frac{AUC_{new}}{AUC_{old}}
=8\frac{\int P(t)/DAR(t)\,dt}{\int P(t)\,dt}.
$$

これはモル濃度の恒等式で、薬剤間の効力換算ではない。質量濃度に移す際は、分子量や分析物の定義も確認する必要がある。

![DARによる派生濃度の変化](shared/trop2-payload-exposure/figures/dar-definition-sensitivity.png)

図2：固定した結合payloadに対する代数的な $8/DAR$。患者データや推定DAR軌跡を描いていない。

例えば結合payload積分量の半分ずつがDAR=8と2の領域にある仮定では、比は2.5になる。同じ重みで平均DAR=5を固定すると1.6となる。**同じ平均DARから同じAUC換算は得られない。** この計算例は非線形な変換を確認するためのもので、ラベルの2.136倍を再現した患者モデルではない。

## 2薬で揃う単位と、揃わない量

Dato-DXdの原著ではADCとreleased DXdをplasmaで測定している。SGのserum、派生ADCとの違いを記録した。[1, 5] 「free payload」は抗体に結合していないという意味であり、血漿蛋白に結合していない薬物濃度とは区別する。

| 確認項目 | SG | Dato-DXd | 比較に必要な確認 |
| --- | --- | --- | --- |
| Payload | SN-38 | DXd | 異なる分子の効力・細胞内動態 |
| ADC濃度 | 結合SN-38から派生、DAR仮定が変更 | ADCを免疫測定 | 測定・派生定義とmodel version |
| 公表ラベルのpayload AUC | 3,510 ng·h/mL、0–168h | 18 ng·day/mL、初回cycleのAUC | 積分窓と投与履歴 |
| レジメン | Day1・8、21日cycle | 21日ごと | 反復回数と観測期間 |

18 ng·day/mLは432 ng·h/mLへ換算できる。しかし、単位が一致したことは同じ168時間の積分や同じbioactive exposureを意味しない。Dato-DXdラベルの該当表は積分上限を明示していないため、その行から168時間平均や21日平均を作らなかった。原著のcycle 1指標を利用するなら、元の定義と母集団を照合する必要がある。[6]

SGの0–168h内のfree SN-38平均は20.89 ng/mLと計算できる。これは投与周期全体の平均でも、蛋白非結合SN-38の平均でもない。両薬の質量AUCを割った値から、腫瘍内のpayload量、治療効果、安全性の優劣を導くことはしない。

## E–Rも同じ横軸ではない

SGのmTNBC E–R原著では、SGの治療期間平均濃度がORR/CR、total antibodyの平均濃度がOS/PFSに選ばれている。[7] Dato-DXdの2026年HR+/HER2−乳癌原著では、cycle 1のADC AUCがOSに関連したが、PFSの最終モデルではbaseline tumor sizeが選ばれた。[8] 同年9月のNSCLC原著では、OS、PFS、ORRに異なるADC曝露指標が使われている。[9]

異なる腫瘍種だけが問題ではない。同じ薬でも、転帰・観測期間・患者背景によって選ばれる横軸が異なる。治療期間平均は、dose interruption/reductionやイベントまでの期間を含む。**曝露との関連を、同じ患者の用量を増やしたときの因果効果と解釈できない。** また、ADCが選ばれたE–Rモデルを、そのまま遊離payloadの共通E–Rへ読み替えることはできない。

## 新しいADCで優先して残す情報

今回の結果が支持するのは、既存薬のAUCを目標値として借りる前の確認事項である。

1. Total antibody、conjugated payload、unconjugated payloadの測定結果と、ADC濃度への変換式を別々に残す。
2. DARの時間変化を扱うなら、固定DARと動的DARで派生曝露がどう変わるかを確認し、その検証に使った観測を明示する。
3. E–Rに使う曝露の積分窓・投与履歴・イベント時点を揃え、初回曝露と治療期間平均を分ける。
4. 他payloadへ情報を移す際には、蛋白非結合率だけでなく、細胞内活性・腫瘍内deliveryなど、使用目的に必要なbridgeを実測で確かめる。

これらは新薬の推奨用量を決める結果ではない。FDAのADC guidanceも、複数の構成成分を扱うbioanalysisとE–Rの設計を重要な課題として扱う。[10] 今回のSGの例は、**比較前に定義と版を確認するだけで、誤った曝露目標の借用を避けられる**ことを具体的に示している。

## 再実行と限界

数値は`analysis/01_audit.py`から生成した`outputs/tables/`に保存している。Notebookは同じ関数を呼び出す。ラベル数値の転記は原本中の数値とのassertionで確認し、原本のSHA256も検証する。患者個票、濃度時系列、モデル間のpaired推定値、腫瘍内bioactive payloadは取得していない。PopPKモデルの性能や薬剤間の同等性を検証したとは呼ばない。

公開原著・審査資料は読み取り監査に利用し、原著の図や表を転載・改変しない。本記事の図は公開数値の算術と明示した代数から独自に作成した。

## 出典

1. [Sathe et al. SG PopPK, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11106201/).
2. [EMA Trodelvy variation assessment, 2026](https://www.ema.europa.eu/en/documents/variation-report/trodelvy-vr-0000312649-epar-assessment-report-variation_en.pdf), §2.3.2、§2.3.4.
3. [TRODELVY US label, version 18](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=57a597d2-03f0-472e-b148-016d7169169d&version=18), Table9.
4. [TRODELVY US label, version 20](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=57a597d2-03f0-472e-b148-016d7169169d&version=20), Table13.
5. [Dato-DXd PopPK, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12706414/).
6. [DATROWAY US label, May2026](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=2950227c-6230-4ca4-a135-46e44d9424a0&type=display), Table10.
7. [Sathe et al. SG E–R](https://pmc.ncbi.nlm.nih.gov/articles/PMC11739744/), DOI10.1002/cpt.3495.
8. [Tang et al. Dato-DXd breast cancer E–R, 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13084299/), DOI10.1002/jcph.70188.
9. [Hong et al. Dato-DXd NSCLC E–R, 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13572793/), DOI10.1002/cpt.70477.
10. [FDA, Clinical Pharmacology Considerations for ADCs, March2024](https://www.fda.gov/media/155997/download).

## 解析関数と検査コード

[解析関数と単体検査のZIP](shared/trop2-payload-exposure/trop2-payload-exposure-functions.zip)を配布する。原データや解析全体の再実行資料は含まない。検査に使う構成例を、臨床データの検証とは扱わない。
