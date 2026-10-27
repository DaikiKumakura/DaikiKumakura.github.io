## 要旨 {#article-abstract}

公開された治療前後のRNAを対応付けた43人では、固定した細胞傷害関連の発現要約は多くの場合に上昇した。一方、その変化が、治療前発現を超えて記録された最良奏効に加える情報は不確かだった。患者内の薬力学的変化を予測バイオマーカーとして使うには、別途の評価が必要である。

## 背景と目的 {#article-introduction}

少数の固定した免疫発現指標が患者内で変わるか、その変化が記録された最良総合効果に条件付きの情報を加えるかを問う。用途は薬力学的モニタリング仮説の検討順位を考えることに限る。臨床バイオマーカー検査、治療選択規則、生存の代替指標、前向き予測研究ではない。

原研究は投与前1–7日の生検と、投与後23–29日の生検を予定した。取得したGEOメタデータには個々の正確な採取日がない。奏効はRECIST 1.1による最良総合効果である ([1](#ref-1))。

治療後の発現を、治療前に分かっていた情報として使うことはできない。また、研究全体の予定時点を各患者の実採取日・イベント日の代わりにはできない。それらがないため、このファイルから生存のランドマーク解析やimmortal-time biasの補正を妥当と判断できない。

## 方法 {#article-methods}

### 対応する検体とデータの確認 {#pair-audit}

公式GSE91061のSOFTメタデータ、FPKM、raw countを取得し、ハッシュを保存した。検体タイトルの患者・訪問識別子を使い、訪問ラベルをメタデータの特性項目と照合した。発現列とメタデータの検体は厳密に一致し、患者内の奏効ラベルも一致した ([2](#ref-2))。表1に集計を示す。

**表1　データと検体の対応確認**

| Data audit | Count |
| --- | ---: |
| RNA samples / participants | 109 / 65 |
| Pretreatment / on-treatment samples | 51 / 58 |
| Participants with exactly one sample at each visit | 43 |
| Participants excluded as unpaired | 22 |
| Duplicate participant–visit rows | 2, belonging to one unpaired participant |
| Paired PRCR / SD / PD / unknown response | 9 / 15 / 18 / 1 |
| Response-known paired analysis | 42 participants, 9 responders |
| Genes in each expression matrix | 22,187 |

重複した治療後検体を奏効や発現によって選別していない。その患者には適格な治療前の対がなく、対応解析へ入らなかった。奏効不明例は変化量の記述には残し、奏効関連モデルからだけ除いた。観測された採取構造を保持し、完全な集団を作り出す補完はしていない。

### 固定スコアと測定法の違い {#fixed-scores}

主要な細胞傷害関連スコアは、**GZMAとPRF1**のlog2(FPKM+1)の平均とした。遺伝子の選択はRooneyらの生物学的要約に基づくが、既報CYT指標はTPMを使っていた。今回の変換・正規化・擬似カウントを含む指標は、原法の再現ではなく変更した要約である ([3](#ref-3))。

副次的な記述用IFN関連スコアは、IFNG、STAT1、IDO1、CXCL9、CXCL10、HLA-DRAのlog2(FPKM+1)平均とした。文献はパネルの選択を動機付けるが、NanoStringを用いた計算や臨床閾値をRNA-seqへ移植していない ([4](#ref-4))。

この集団の奏効ラベルで遺伝子や閾値を選択していない。変化量は治療後から治療前を引いた値とした。正規化の感度条件として、各raw-countライブラリーの総量から求めたlog2(CPM+1)でも主要スコアを計算した。CPMは遺伝子長を正規化せず、FPKMやTPMとの同等性を示すものではない。

### 奏効関連モデルの評価 {#response-models}

Ridgeロジスティックモデルを2つ固定した。治療前主要スコアだけのモデルと、治療前スコアに変化量を加えたモデルである。PRCR（部分・完全奏効）をSD/PD（安定・増悪）と比較し、安定を奏効へ再分類しなかった。奏効は9例のみで、追加の臨床交互作用、非線形項、転帰で選んだカットオフは加えていない。

患者単位で層別化した3分割を20回反復した。中心化、尺度、係数は学習fold内だけで推定し、同じ患者の2時点は一緒に保持した。傾きへの罰則は1に固定し、結果が最大になるよう選んでいない。各患者の反復検証予測を平均した。

## 結果 {#article-results}

### 対応する患者内の変化 {#paired-changes}

図1と表2に患者内の変化を示す。

![患者内の発現変化と各訪問の中央値](shared/on-treatment-immune-change/figures/paired-expression.png)

**図1　対応する発現変化。** 太線は各訪問時点の中央値を結ぶ。その縦方向の差は個人変化量の中央値ではない。

**表2　患者内のスコア変化**

| Score | Pairs | Median change | Participant-bootstrap 95% interval | Positive changes |
| --- | ---: | ---: | ---: | ---: |
| Cytolytic-inspired, FPKM | 43 | +0.346 | +0.154 to +1.108 | 33 / 43 |
| IFN-related, FPKM | 43 | +0.454 | +0.242 to +0.803 | 34 / 43 |
| Cytolytic-inspired, CPM sensitivity | 43 | +0.419 | +0.184 to +1.138 | 34 / 43 |

区間は患者を2,000回再標本化して求めた、対応差の中央値の95%区間である。図の訪問別中央値の差と、個人変化の中央値を混同できない。

主要変化のFPKMとCPMの順位は強く相関し、Spearman rhoは**0.996**だった。この正規化変更に対する順位パターンの安定性を支持するが、絶対スコア単位、組織の比較可能性、免疫細胞数としての解釈を検証するものではない。

バルクRNAの変化は、細胞組成、腫瘍含有量、採取、細胞内発現の変化を反映しうる。無治療の縦断対照がなく、観測された変化はニボルマブがスコアへ与える因果効果の無作為化推定ではない。患者内対応は固定的な個人差を除くが、時間とともに変わるすべての説明を除くわけではない。

### 記録された奏効への条件付き情報 {#conditional-response-information}

図2–3と表3に、奏効関連の記述と検証指標を示す。

![選択された対応集団における奏効群別の変化](shared/on-treatment-immune-change/figures/change-by-response.png)

**図2　奏効群別の変化。** 記録された最良効果による記述的な関連であり、治療前予測ではない。

![条件付き奏効関連についての検証用予測の診断](shared/on-treatment-immune-change/figures/association-validation.png)

**図3　奏効関連モデルの検証診断。** 同一患者の両時点を一緒に保った反復交差検証の予測を集約した。

**表3　検証用予測の指標**

| Held-out measure | Baseline | Baseline + change |
| --- | ---: | ---: |
| AUC | 0.599 | 0.673 |
| Brier score, lower is better | 0.1650 | 0.1635 |
| Log loss, lower is better | 0.5198 | 0.5042 |

AUC差は**+0.074**、層別化した条件付きbootstrap区間は**−0.084–+0.269**だった。Brier差は**−0.0015**（−0.0251–+0.0232）、log-loss差は**−0.0157**（−0.0946–+0.0610）だった。いずれも改善なしを含む。推定済み検証予測を条件とし、観測された奏効数を保つ区間で、再推定による不確実性は含まない。

拡張モデルの検証予測の校正傾きは**0.648**、罰則なしの校正回帰切片は**−0.417**だった。奏効9例では不精密な診断であり、個人確率の妥当性を保証しない。CPM感度解析の拡張モデルはAUC 0.677、Brier 0.1630で、小さな点推定の改善は保ったが臨床有用性は確立しない。

これらは**対が取得できた患者での条件付き関連診断**であり、治療前予測ではない。最良効果の時点と個々の生検日をファイルから順序付けられない。患者単位の交差検証はモデル当てはめの情報混入を抑えるが、2回目生検への選択や、臨床評価項目の情報時点の問題を修復できない。

### 観測できる選択の差 {#selection-effects}

表4は、治療前検体を持つ患者について治療後の適格な対の有無を比較したものである。

**表4　対応検体の有無と観測された特徴**

| Pretreatment samples | Participants | Known responses | PRCR | Median baseline primary score |
| --- | ---: | ---: | ---: | ---: |
| Also have an eligible on-treatment pair | 43 | 42 | 9 | 2.692 |
| No eligible on-treatment pair | 8 | 7 | 1 | 2.298 |

小規模な観測差の記録であり、治療後生検がない理由や欠測の無作為性を説明しない。他には治療後検体だけの患者もいて、この治療前比較へ含められない。既治療、正確な病変組成、個人の採取時点を調整していない。

## 考察 {#article-discussion}

観測された対の中では患者内の免疫発現変化が支持された。一方、主要変化量が有用な奏効情報を加えるという根拠は弱い。固定した情報時点での解釈には、採取時点、生検の失敗、病変の同一性、奏効確認の限界がある。

PKや曝露と対応した応答は測っておらず、用量調整の根拠にはならない。新しい免疫生物学の発見でもなく、既存縦断集団の範囲を限った再解析である。対応付けの確認、固定した低次元スコア、正規化感度は付属資料へ記録した。

## 結論 {#article-conclusion}

免疫発現スコアは観測された患者内で上昇したが、変化量による追加の奏効情報は不確かだった。対応集団への選択と個別時点の不明があるため、治療前予測や検証済みモニタリング規則として解釈できない。

## データとコードの公開状況 {#availability}

付属資料は取得・解析コード、集約結果、図、実行済みノートブックを含む。患者メタデータ、発現行列、個人スコア、予測行は配布物へ含めない。[README](shared/on-treatment-immune-change/README.md)に手順を記載した。出典台帳には公式URLとSHA-256を保存している。

[コード・集約結果・実行済みノートブックのダウンロード](shared/on-treatment-immune-change/on-treatment-immune-change-companion.zip)

## 参照 {#article-references}

1. <span id="ref-1"></span>Riaz N, Havel JJ, Makarov V, Desrichard A, Urba WJ, Sims JS, et al. Tumor and microenvironment evolution during immunotherapy with nivolumab. Cell. 2017;171(4):934–949.e16. [doi:10.1016/j.cell.2017.09.028](https://doi.org/10.1016/j.cell.2017.09.028).
2. <span id="ref-2"></span>National Center for Biotechnology Information. Gene Expression Omnibus: GSE91061 [Dataset]. [Official series record](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE91061). Official sample metadata and processed expression files; acquisition URLs and SHA-256 hashes are retained in the companion.
3. <span id="ref-3"></span>Rooney MS, Shukla SA, Wu CJ, Getz G, Hacohen N. Molecular and genetic properties of tumors associated with local immune cytolytic activity. Cell. 2015;160(1–2):48–61. [doi:10.1016/j.cell.2014.12.033](https://doi.org/10.1016/j.cell.2014.12.033).
4. <span id="ref-4"></span>Ayers M, Lunceford J, Nebozhyn M, Murphy E, Loboda A, Kaufman DR, et al. IFN-γ–related mRNA profile predicts clinical response to PD-1 blockade. J Clin Invest. 2017;127(8):2930–2940. [doi:10.1172/JCI91190](https://doi.org/10.1172/JCI91190). The gene panel motivated the secondary summary; the original assay and cutoff were not reused.
