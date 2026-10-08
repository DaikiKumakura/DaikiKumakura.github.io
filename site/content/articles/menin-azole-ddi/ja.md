Menin阻害剤のrevumenibとziftomenibは、どちらもCYP3Aによる代謝を受ける。では、新しいMenin阻害剤の開発で、既存薬のazole併用時の曝露倍率をそのまま使えるだろうか。

公開資料を読むだけでも、注意すべき点がある。revumenibのラベルにはazole強阻害剤との併用でAUCとCmaxが約2倍になると書かれている。一方、ziftomenibでは強阻害剤によるAUCの増加は「最大3倍」、Cmaxは「最大2倍」という推定表現である。臨床データに基づくラベル記述と推定上限を、同じ種類の数値として比べることはできない。[REVUFORJラベル §12.3](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6eb3cdbc-0e74-477d-82d6-3bb172d3f63f&version=5)、[KOMZIFTIラベル §12.3](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/220305s000lbl.pdf)

本解析の結論は、**今回の公開資料だけでは、Menin阻害剤に共通するazole併用倍率を正当化できない**、というものになった。理由は単に数字が違うことではない。ラベルのPK表にはモデル由来の値が含まれ、原著の「検証済み」という評価とFDAの用途別評価も同じではなかった。どの情報が独立した検証に使えるのか、AUCへの適合がCmaxまで説明するのかを分けて調べた。

## 問いと使用範囲

QOIは「既存薬のazole併用情報を別薬に移すと、薬剤固有の公開情報との整合性がどこで失われるか」である。COUは公開データによる研究・学習と、次に収集する情報の優先度の検討とした。患者の用量変更や臨床試験の用量決定には使わない。

この解析は個体濃度時系列からのNLME推定でも、Simcypの全身PBPKモデルの再実装でもない。公表された集約PK・PBPK結果を入力とする、情報の監査と縮約モデルの解析である。入手していない患者背景を仮想患者で補って、実測データの検証と呼ぶことはしなかった。

## 同じ表の中にも異なる種類の数値がある

FDA/NIHラベル、両薬のFDA審査資料、2026年のziftomenib PBPK論文を確認した。資料の版、投与条件、初回か定常状態か、観測値かモデル由来かを入力CSVに残した。

| 情報 | 数値の性質 | 比較時の注意 |
| --- | --- | --- |
| Revumenibのazole約2倍 | ラベルのClinical Studies記述 | azole群の要約で、全剤・全条件の共通定数ではない |
| RevumenibのラベルPK表 | 160 mg BID併用と270 mg BID非併用の集約値 | 用量も患者群も異なる |
| ZiftomenibのラベルPK表 | 600 mg QD、C2D1のPopPK由来集約値 | 独立観測の検証データではない |
| ZiftomenibのFDA Table66 | fmを置いた保守的条件の推定 | 患者で検証済みの真値ではない |
| 原著Table2/3 | 校正用群比への感度結果／条件付きPBPK予測 | 初回投与とDay29、校正と予測を分ける |

例えばrevumenibのラベル行のAUC生比は1.74だが、用量を補正すると2.94になる。ziftomenibのラベル行のAUC比は2.39である。いずれも今回の計算結果だが、同一患者・同じ投与条件でazoleの有無だけを変えたDDI比ではない。用量補正は群間の患者背景や投与履歴の違いを消さない。[REVUFORJ Table9](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6eb3cdbc-0e74-477d-82d6-3bb172d3f63f&version=5)、[FDA ziftomenib審査 p133](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2025/220305Orig1s000MultidisciplineR.pdf)

## AUCを合わせてもCmaxが合うとは限らない

Ziftomenibの公表PBPK感度解析には、CYP3A代謝寄与率 $f_m$ を20–80%へ変えた7条件がある。その計算結果と、校正に使った臨床群比との比（S/O）を調べた。本解析では0.80–1.25を整合性スクリーニングとした。これは臨床的許容域や承認基準ではない。

![ZiftomenibのAUCとCmaxの整合性](shared/menin-azole-ddi/figures/joint-endpoint-consistency.png)

図1：公表7条件を線形補間した結果。灰色は今回のスクリーニング範囲。独立検証ではなく、校正に使った群比への整合性である。

AUCでは範囲内へ入る $f_m$ があった。しかしCmaxのS/Oは最大でも0.776で、調べられた範囲に**両方が通過する条件はなかった**。これは全範囲の $f_m$ や別のモデル構造が不可能という意味ではない。少なくとも、この一つのパラメータを動かしてAUCに合わせる操作だけでは、初期のpeakまで説明できていない。[Templeton et al., Table2](https://doi.org/10.1002/psp4.70327)

S/Oと予測倍率から元の参照群比を逆算すると、AUCは約2.25–2.27、Cmaxは約2.00–2.02となった。この幅は印刷丸めによる整合範囲であり、臨床的な信頼区間ではない。未取得の患者値を復元したわけでもない。

ただし、許容幅を広げれば結果は変わる。最初の解析後に追加した感度計算では、公表7条件の共同通過は次のようになった。

| 予測／参照比の許容幅 | AUCとCmaxが共同通過した公表条件数 |
| --- | ---: |
| 0.80–1.25 | 0/7 |
| 1/1.5–1.5 | 3/7 |
| 0.50–2.00 | 7/7 |

原著もモデル性能の文脈で2倍誤差に言及している。「通過なし」は厳しい基準での結果であり、モデルがあらゆる用途で不十分という証明ではない。一方、広い許容幅を通過したことも、別の阻害条件や新薬への外挿を検証したことにはならない。**用途に必要な精度と、独立した検証データを先に定める必要がある。**

## 別薬から2倍を借りると、ずれの向きも同じにならない

次に、revumenibのazole約2倍をziftomenibのitraconazole条件へ移す、単純な情報借用を計算した。主参照はFDA Table66、感度参照は原著Table3とした。以下はFDAが用いた保守的 $f_m=0.7$ の条件との比較である。

| 指標 | 借用値 | Ziftomenibの条件付きベンチマーク | 借用値の不一致 |
| --- | ---: | ---: | ---: |
| AUC倍率 | 2.0 | 2.6 | −23.1% |
| Cmax倍率 | 2.0 | 1.7 | +17.6% |

計算は $100(R_{borrowed}/R_{benchmark}-1)$。Ziftomenib 600 mg QD、itraconazole 200 mg QDの推定条件に対する不一致であり、患者での予測誤差ではない。[FDA ziftomenib Table66、印字p312](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2025/220305Orig1s000MultidisciplineR.pdf)

![薬剤間で倍率を借りたときの不一致](shared/menin-azole-ddi/figures/transfer-benchmark-discrepancy.png)

図2：$f_m=0.6/0.7$、FDAと原著の別々の条件付きベンチマーク。塗りつぶしはFDA、白抜きは原著。灰色は今回のスクリーニング範囲で、薬剤間の同等性を示さない。

$f_m=0.6$ の条件ではAUCの不一致は小さくなり、Cmaxでは大きくなった。単一倍率は「安全側」とも一括には言えない。AUCを小さく、Cmaxを大きく見積もる場合があるからである。ここから安全性や有効性の順位を決めるには、さらに薬剤固有のE–R情報が必要になる。

## AUC倍率だけでは代謝と吸収を分けられない

次の縮約式を使った。

$$
R_{AUC}=\frac{B}{1-f_m+f_mr}
$$

$B$ は経口bioavailabilityの比、$r$ は残存CYP3A活性、$f_m$ は阻害を受ける経路の寄与である。定常状態で線形PK、他の経路や用量が変わらないという限定したモデルである。肝血流、腸管代謝、輸送、自己阻害を含む全身PBPKの代用ではない。

同じAUC倍率でも、$B$ と $r$ の仮定を変えると適合する $f_m$ は変わる。例えば $R=2.6$、完全阻害 $r=0$ の下では、$B=1$ なら $f_m=0.615$、$B=1.5$ なら $f_m=0.423$ で同じ比を再現する。

![静的モデルで同じAUCを作る異なる機序](shared/menin-azole-ddi/figures/structural-nonidentifiability.png)

図3：仮定した $B,r$ と同じAUC倍率を作る $f_m$。各線は確率分布でも推定の信頼区間でもない。縮約モデル内の非識別性を示す。

これは「PBPKを使っても機序を推定できない」という結論ではない。**AUCという一つの数字だけを見て、阻害の強さ・代謝寄与・吸収変化を一意に割り当てることはできない**という、今回のモデル内の結果である。絶対bioavailability、IV clearance、mass balance、吸収・輸送の情報があると、許される組合せを狭められる。

## 「論文で検証済み」と「その用途で十分」は別に読む

Ziftomenibの2026年PBPK論文はモデルを検証済みと説明している。一方、FDA審査のPBPK評価では、疎な採血、小さい群、高い変動、併用薬などのため、患者PKによる $f_m$ の検証は不十分と評価されていた。FDAはin vitro、mass balance、絶対bioavailabilityなども使い、保守的条件を検討している。ラベルの記載を支持したことを、すべてのモデル仮定が検証されたことと同一視しない。[原著](https://doi.org/10.1002/psp4.70327)、[FDA ziftomenib審査 pp304/311–313](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2025/220305Orig1s000MultidisciplineR.pdf)

なお、FDA審査は2025年、原著は2026年の公表であり、FDAが後年の論文を否定したという意味ではない。資料ごとの時点と評価用途を区別して読む。

Revumenibにも、親薬の適合から代謝物M1の予測性能を導けない問題がある。M1はQTcに関係し、FDAはcobicistat以外の阻害条件でのモデル性能に懸念を示している。親薬AUCを合わせたからQTリスクまで再現できるとは言えない。[FDA revumenib審査 pp287–293](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2024/218944Orig1s000MultidisciplineR.pdf)

## 新薬なら、次に何を集めるか

今回の結果から考える情報収集の優先度は次の通りである。統計的に最適化した試験設計ではなく、残った曖昧さを減らすための順序である。

| 優先する情報 | 減らしたい曖昧さ |
| --- | --- |
| 代謝寄与、吸収・輸送、絶対BA／IV PK・mass balance | 同じAUC倍率を作る機序の区別 |
| 併用開始・中止時刻、阻害剤曝露、食事・PPIなどを伴う患者PK | 「強阻害剤併用」という群名だけでは消えない交絡 |
| 校正に使わないmoderate条件でのAUCとCmax | strong条件への適合から別条件へ移せるか |
| 必要に応じて親薬・代謝物とQTなどの対応データ | 曝露の再現を安全性予測と取り違えないこと |

同じ標的の薬は、どの相互作用を早期に調べるかを考える材料になる。倍率の借用を一律に禁じるわけではないが、今回の資料からクラス共通の値は支持できない。借用するなら、薬剤固有の代謝・吸収、実際の併用条件、未使用条件での予測性能を確認する必要がある。

## 再実行と限界

入力CSV、解析関数、図作成コード、実行済Notebookを制作フォルダに保存した。単位換算、式の逆算、数値積分によるpeak上限、丸め幅、境界値の10検査を通した。解析は決定的なグリッド計算で乱数を使わない。

患者の濃度時系列・共変量・azole濃度のjoint dataは未取得で、NLME/IIV/E–Rを再推定していない。原著補足の直接取得は403だった。モデル条件の差を解消する資料も不足しているため、公開結果の違いを薬剤差の因果推定や独立臨床検証に読み替えない。

ラベルの集約半減期から代表1-compartment曲線を作れるかという補助診断はNotebookと補足メモに保存した。本文の主結論はその診断に依存しない。縮約式の非識別性も、既知のモデルの性質を確認する説明用計算であり、新しい薬理学的発見ではない。

## 参考文献

1. Templeton IE, Litou C, Jones HM, et al. A Practical Alternative to Refine the Estimate of fmCYP3A4 and Evaluate Drug–Drug Interaction Potential for Ziftomenib Using PBPK Modeling to Inform Labeling. *CPT Pharmacometrics Syst Pharmacol.* 2026;15:e70327. [doi:10.1002/psp4.70327](https://doi.org/10.1002/psp4.70327).
2. FDA. NDA 220305, KOMZIFTI multidisciplinary review. 2025. [審査資料](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2025/220305Orig1s000MultidisciplineR.pdf).
3. FDA. NDA 218944, REVUFORJ multidisciplinary review. 2024. [審査資料](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2024/218944Orig1s000MultidisciplineR.pdf).
4. NIH DailyMed. REVUFORJ prescribing information, revised February 2026. [ラベル](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6eb3cdbc-0e74-477d-82d6-3bb172d3f63f&version=5).
5. FDA. KOMZIFTI prescribing information. 2025. [ラベル](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/220305s000lbl.pdf).

## 解析関数と検査コード

[解析関数と単体検査のZIP](shared/menin-azole-ddi/menin-azole-ddi-functions.zip)を配布する。原データや解析全体の再実行資料は含まない。検査に使う構成例を、臨床データの検証とは扱わない。
