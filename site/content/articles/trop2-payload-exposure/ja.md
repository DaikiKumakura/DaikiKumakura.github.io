## 要旨 {#article-abstract}

TROP2を標的とする二つのADCについて、公開PK・曝露–反応資料からpayload曝露の共通目標を作れるか検討した。SGの旧版と2026年版ラベルでADC AUCの記載値は2.136倍異なったが、free SN-38のAUC差は−5.0%であり、定義・モデル・集団の変更を区別する必要があった。DARによる派生濃度の変換は非線形で、薬剤間では分析物と積分窓も異なる。今回の集約情報から、移用可能なpayload曝露目標や効力順位は得られなかった。

## 背景と目的 {#article-introduction}

Sacituzumab govitecan（SG）とdatopotamab deruxtecan（Dato-DXd）は、どちらもTROP2を標的とするADCである。新しいTROP2 ADCの開発で、既存薬のpayload曝露を参照したくなる。しかし、単位を揃える前に確認すべきことがある。**「ADCの濃度」が、何を測り、どう計算した値なのか**である。

SGの旧ラベルと2026年版を比べると、初回投与後168時間のADC AUCの記載値は2.136倍になっている。一方、free SN-38のAUCの記載値差は−5.0%だった。患者の曝露が経年的に倍増したという結果ではない。公開審査資料は、ADC濃度の算出とPopPKモデルの変更を説明している。

本記事では、2薬の曝露を数値で順位付けする前に、その比較を採用できる条件を調べた。結論は、**今回の集約PKとE–R情報から、共通のpayload曝露目標や効力順位は作れない**。その理由を「薬が違う」で終わらせず、測定値・派生値・時間窓・転帰の違いまで分解する。

## 対象と確認方法 {#_1}

QOIは「公表PK・E–Rから、TROP2 ADC間で移せるpayload曝露目標や比較順位を作れるか」。COUは公開資料に基づく薬剤間の比較可能性と情報の不足の検討である。患者の治療や臨床試験の用量決定には使わない。

ラベル版履歴、原著、2026年の審査資料を確認し、単位変換と派生濃度の感度を計算した。患者別の濃度データからPopPKを推定した解析ではなく、既存モデルの全面再実装でもない。計画は資料探索後、数値計算前に固定した。

## 資料の比較と計算 {#article-results}

### SG濃度の算出定義 {#sg}

2024年のSG PopPK原著では、total SN-38とfree SN-38をLC–MS/MSで、total antibodyを別の測定法で定量している。SG濃度は、結合SN-38とDAR=8の仮定から算出した。**直接測定したtotal antibodyと、この派生SG濃度は同じ量ではない。** ([1](#ref-1))

2026年のEMA審査では、total antibody、free SN-38、total SN-38を扱う統合モデルへ変更し、時間とともに変わるDARからSG濃度を計算している。審査はDAR導入をAUC・半減期変更の主要な要因として説明する。同時に、派生SG濃度はモデルに依存し、確認データがないことも指摘している。これは測定法そのものが変更されたという説明ではない。([2](#ref-2), printed pp. 18–20, 34)

**表1　SGラベルの版による記載値の差**

| SGのラベル記載値 | 旧版18 | 2026年版20 | 今回計算した記載値差 |
| --- | ---: | ---: | ---: |
| ADC AUC0–168（ng·h/mL） | 5,640,000 | 12,049,500 | 2.136倍 |
| Free SN-38 AUC0–168（ng·h/mL） | 3,696 | 3,510 | −5.0% |
| Free SN-38 Cmax（ng/mL） | 98.0 | 108 | +10.2% |

表1の旧版は単剤投与、現行版は単剤・pembrolizumab併用を含む集団の要約であり、モデルと患者構成も同一ではない ([3](#ref-3), [4](#ref-4))。 **この2.136倍の全量をDARだけの因果効果として分解することはできない。** 同一患者・同一濃度時系列を両定義で再計算した比較ではなく、記載値差には信頼区間を付けなかった。

![SGのラベル記載値の比較](shared/trop2-payload-exposure/figures/label-version-differences.png)

**図1。** 現行／旧版の記載値比。3つの集約指標を比較したもので、患者数3ではない。破線は記載値が同じ場合を示す。臨床的な曝露変化やモデル改善の程度を表す図ではない。

### DARによる非線形な変換 {#dar}

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

**図2。** 固定した結合payloadに対する代数的な $8/DAR$。患者データや推定DAR軌跡を描いていない。

例えば結合payload積分量の半分ずつがDAR=8と2の領域にある仮定では、比は2.5になる。同じ重みで平均DAR=5を固定すると1.6となる。**同じ平均DARから同じAUC換算は得られない。** この計算例は非線形な変換を確認するためのもので、ラベルの2.136倍を再現した患者モデルではない。

### 薬剤間の分析物と積分窓 {#2}

表2の比較では、Dato-DXdの原著においてADCとreleased DXdをplasmaで測定している。SGのserum、派生ADCとの違いを記録した ([1](#ref-1), [5](#ref-5))。 「free payload」は抗体に結合していないという意味であり、血漿蛋白に結合していない薬物濃度とは区別する。

**表2　SGとDato-DXdの分析物と曝露定義**

| 確認項目 | SG | Dato-DXd | 比較に必要な確認 |
| --- | --- | --- | --- |
| Payload | SN-38 | DXd | 異なる分子の効力・細胞内動態 |
| ADC濃度 | 結合SN-38から派生、DAR仮定が変更 | ADCを免疫測定 | 測定・派生定義とmodel version |
| 公表ラベルのpayload AUC | 3,510 ng·h/mL、0–168h | 18 ng·day/mL、初回cycleのAUC | 積分窓と投与履歴 |
| レジメン | Day1・8、21日cycle | 21日ごと | 反復回数と観測期間 |

18 ng·day/mLは432 ng·h/mLへ換算できる。しかし、単位が一致したことは同じ168時間の積分や同じbioactive exposureを意味しない。Dato-DXdラベルの該当表は積分上限を明示していないため、その行から168時間平均や21日平均を作らなかった。原著のcycle 1指標を利用するなら、元の定義と母集団を照合する必要がある ([6](#ref-6))。

SGの0–168h内のfree SN-38平均は20.89 ng/mLと計算できる。これは投与周期全体の平均でも、蛋白非結合SN-38の平均でもない。両薬の質量AUCを割った値から、腫瘍内のpayload量、治療効果、安全性の優劣を導くことはしない。

### 曝露–反応解析の指標 {#er}

SGのmTNBC E–R原著では、SGの治療期間平均濃度がORR/CR、total antibodyの平均濃度がOS/PFSに選ばれている ([7](#ref-7))。 Dato-DXdの2026年HR+/HER2−乳癌原著では、cycle 1のADC AUCがOSに関連したが、PFSの最終モデルではbaseline tumor sizeが選ばれた ([8](#ref-8))。 同年9月のNSCLC原著では、OS、PFS、ORRに異なるADC曝露指標が使われている ([9](#ref-9))。

異なる腫瘍種だけが問題ではない。同じ薬でも、転帰・観測期間・患者背景によって選ばれる横軸が異なる。治療期間平均は、dose interruption/reductionやイベントまでの期間を含む。**曝露との関連を、同じ患者の用量を増やしたときの因果効果と解釈できない。** また、ADCが選ばれたE–Rモデルを、そのまま遊離payloadの共通E–Rへ読み替えることはできない。

## 考察 {#adc}

Total antibody、conjugated payload、unconjugated payloadは異なる測定対象であり、ADC濃度への変換式とDARの扱いで派生曝露が変わる。今回のSGの例では、定義と資料の版をそろえずにAUCを借りると、異なる量を同じ目標としてしまう。

蛋白非結合率だけで、別payloadの細胞内活性や腫瘍内送達まで等しくなるわけでもない。FDAのADC guidanceも、複数構成成分のbioanalysisとE–Rを課題として扱う ([10](#ref-10))。 今回の比較から、別のADCへ移せる共通の曝露目標や推奨用量は得られていない。

### 限界と計算の確認 {#_2}

数値は`analysis/01_audit.py`から生成した`outputs/tables/`に保存している。Notebookは同じ関数を呼び出す。ラベル数値の転記は原本中の数値とのassertionで確認し、原本のSHA256も検証する。患者個票、濃度時系列、モデル間のpaired推定値、腫瘍内bioactive payloadは取得していない。PopPKモデルの性能や薬剤間の同等性を検証したとは呼ばない。

公開原著・審査資料は読み取り監査に利用し、原著の図や表を転載・改変しない。本記事の図は公開数値の算術と明示した代数から独自に作成した。

## 結論 {#article-conclusion}

同じ単位のAUCでも、測定対象と派生定義、時間窓が異なれば同じ曝露目標にはならない。SGの記載値差はDARだけの効果や患者曝露の経年的増加を示すものではなく、二つのADCの集約値を効力換算へ使う根拠にもならない。

## データとコードの公開状況 {#_4}

[解析関数と単体検査のZIP](shared/trop2-payload-exposure/trop2-payload-exposure-functions.zip)を配布する。原データや解析全体の再実行資料は含まない。検査に使う構成例を、臨床データの検証とは扱わない。

## 参照 {#_3}

1. <span id="ref-1"></span>Sathe AG, Singh I, Singh P, Diderichsen PM, Wang X, Chang P, et al. Population Pharmacokinetics of Sacituzumab Govitecan in Patients with Metastatic Triple-Negative Breast Cancer and Other Solid Tumors. Clinical Pharmacokinetics. 2024;63(5):669–681. [doi:10.1007/s40262-024-01366-3](https://doi.org/10.1007/s40262-024-01366-3).
2. <span id="ref-2"></span>European Medicines Agency. Trodelvy: assessment report on variation EMA/VR/0000312649. EMADOC-1700519818-3107530. 2026 May 21. Sections 2.3.2 and 2.3.4. [Public assessment](https://www.ema.europa.eu/en/documents/variation-report/trodelvy-vr-0000312649-epar-assessment-report-variation_en.pdf).
3. <span id="ref-3"></span>DailyMed. TRODELVY (sacituzumab govitecan-hziy): US prescribing information [Internet]. Version 18, Table 9 [cited 2026 Oct 8]. [Archived label](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=57a597d2-03f0-472e-b148-016d7169169d&version=18).
4. <span id="ref-4"></span>DailyMed. TRODELVY (sacituzumab govitecan-hziy): US prescribing information [Internet]. 2026; version 20, Table 13 [cited 2026 Oct 8]. [Archived label](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=57a597d2-03f0-472e-b148-016d7169169d&version=20).
5. <span id="ref-5"></span>Hong Y, Peigné S, Pan Υ, Friberg Hietala S, McLaughlin A, Tajima N, et al. Population Pharmacokinetic Analysis of Datopotamab Deruxtecan (Dato- DXd ), a TROP2 -Directed Antibody-Drug Conjugate, in Patients With Advanced Solid Tumors. CPT: Pharmacometrics & Systems Pharmacology. 2025;14(12):2149–2160. [doi:10.1002/psp4.70118](https://doi.org/10.1002/psp4.70118).
6. <span id="ref-6"></span>DailyMed. DATROWAY (datopotamab deruxtecan-dlnk): US prescribing information [Internet]. Revised 2026 May, Table 10 [cited 2026 Oct 8]. [Label](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=2950227c-6230-4ca4-a135-46e44d9424a0&type=display).
7. <span id="ref-7"></span>Sathe AG, Diderichsen PM, Fauchet F, Phan SC, Girish S, Othman AA. Exposure–Response Analyses of Sacituzumab Govitecan Efficacy and Safety in Patients With Metastatic Triple-Negative Breast Cancer. Clinical Pharmacology & Therapeutics. 2025;117(2):570–578. [doi:10.1002/cpt.3495](https://doi.org/10.1002/cpt.3495).
8. <span id="ref-8"></span>Tang Z, Lim K, Jiang Y, Denduluri N, Rokutanda N, Pan Y, et al. Exposure-Response Analyses of Datopotamab Deruxtecan (Dato-DXd) in Patients with Hormone Receptor (HR) Positive, Human Epidermal Growth Factor Receptor 2 (HER2)-Negative Breast Cancer. The Journal of Clinical Pharmacology. 2026;66(4):e70188. [doi:10.1002/jcph.70188](https://doi.org/10.1002/jcph.70188).
9. <span id="ref-9"></span>Hong Y, Mc Laughlin AM, Pan Y, Hietala SF, Peigné S, Chargualaf M, et al. Exposure-Response Analyses of Datopotamab Deruxtecan (Dato- DXd ), a TROP2 -Directed Antibody-Drug Conjugate, in Advanced Non-small Cell Lung Cancer. Clinical Pharmacology & Therapeutics. 2026 [published online 2026 Sep 13]. [doi:10.1002/cpt.70477](https://doi.org/10.1002/cpt.70477).
10. <span id="ref-10"></span>US Food and Drug Administration. Clinical Pharmacology Considerations for Antibody-Drug Conjugates: Guidance for Industry. 2024 Mar. [Final guidance](https://www.fda.gov/media/155997/download).
