文献・公開資料の確認日：2026年10月14日。本記事は文献に基づく論考であり、新しい解析は含まない。

2026年9月、単一細胞の転写データから代謝の状態を推定する新しい手法MeRNがプレプリントとして公開された ([1](#ref-1))。 代謝ネットワークの構造を事前知識として組み込んだ変分オートエンコーダで、細胞ごとの代謝状態と、反応や経路の活性を表す潜在表現を学ぶ。論文は、マウス小腸の絨毛に沿ったタンパク質の測定と照合して他の手法を上回ったことを示し、scFEAとの比較、葉酸の取り込みに関わるFolr1を欠損させた胚のデータ、抗PD-1療法を受けた肺がん患者の免疫細胞のデータへの適用まで行っている。

細胞ごとの代謝を直接測ることは難しい。単一細胞のメタボロミクスは感度や測れる代謝物の数に限りがある。一方、単一細胞RNA-seqは大量にある。転写データから代謝を推定できれば魅力的であり、CompassやscFEAなど、同じ方向の手法がこれまでにも提案され、それぞれ検証されてきた ([2](#ref-2), [3](#ref-3))。

この種の手法では、最初に確かめるべき問いがある。**推定された「代謝状態」は、何を指していて、何と照らし合わせて確かめられたのか**である。

## 「代謝」と呼ばれるものは少なくとも三つある {#_1}

転写データからの推定が指すものは、手法によって違う。少なくとも三つは区別が必要だ。

1. **代謝物の量**：ある時点で細胞の中にある代謝物の量。メタボロミクスで測る。大規模な細胞株のデータの多くは、絶対濃度ではなく相対量である。
2. **代謝の流れ（フラックス）**：反応が単位時間あたりにどれだけ進んでいるか。直接は測れず、同位体で標識した栄養を与えて代謝物の標識パターンを測り、代謝ネットワークのモデルに当てはめて推定する（13C代謝フラックス解析など）。
3. **代謝の能力**：酵素の遺伝子やタンパク質の量から見た、反応を担える潜在的な力。

転写データが直接表しているのは、三つ目の「能力」に最も近い。酵素の量はmRNAの量と必ずしも比例せず、酵素の活性は翻訳後修飾、基質の濃度、アロステリックな制御で変わる。代謝物の量は、作られる速さと使われる速さの釣り合いで決まる。流れが速くても量が少ないことはあるし、その逆もある。

既存の手法をこの三つに当てはめると、主張と検証の対応が見えてくる。

表1　転写データからの代謝推定と原著での検証対象。

| 手法 | 主に推定するもの | 論文で示された主な検証 |
| --- | --- | --- |
| Compass ([2](#ref-2)) | 流束平衡解析に基づく反応の潜在的な活性（能力・流れ寄り） | 代謝アッセイでの確認、ポリアミン代謝への化学的・遺伝的介入、生体での介入による表現型の変化 |
| scFEA ([3](#ref-3)) | 細胞ごとの代謝の流れ | 酸素条件と遺伝子操作を変えた細胞での、対応するメタボロミクスとの照合 |
| MeRN ([1](#ref-1)) | 反応・経路の活性を表す状態 | 小腸の絨毛に沿ったタンパク質の測定との照合、他手法との比較、欠損胚や治療データへの適用 |

どの手法も、何らかの独立した情報で確かめている。一方で、検証の対象は手法ごとに違う。Compassの介入実験は、予測から導いた仮説の**表現型**を確かめた。scFEAは流れの推定を**代謝物の量の変化**と照らし合わせた。MeRNは推定を**タンパク質**、つまり能力に近い量と照らし合わせた。推定した量そのものを、同じ種類の独立した測定で細胞ごとに確かめた例は、まだ少ない。

## 細胞株の集団データでは代謝物の量の予測に答えが分かれている {#_2}

単一細胞より測りやすい細胞株の集団（バルク）では、遺伝子発現と代謝物の量を同じ細胞株で測ったデータがある。ここで扱うのは三分類の一つ目、代謝物の量である。以下の三つの研究は、いずれもがん細胞株のCCLEのデータを使っている。

Liらは、454のがん細胞株で、代謝物ごとにLASSO回帰で遺伝子発現から量を予測した ([4](#ref-4))。 培養条件や細胞の系統を考慮しても、正確に予測できた代謝物は少なかった。頑健だったのはNNMTの発現と1-メチルニコチンアミドの関係くらいで、それも純度の高いがん試料でしか確かめられなかった。

一方、Cavicchioliらは同じCCLEで代謝物と転写産物の相関ネットワークを作り、別のデータセット（NCI-60）でも代謝物の量や群間の差を予測できると報告した ([5](#ref-5))。

2026年のMetab8Dは、約1,000の細胞株で、転写データ、タンパク質、リン酸化、DNAメチル化など8種類の分子データから代謝物の変動を予測した ([6](#ref-6))。 転写データは上位の予測因子だったが、結びつき方は一様ではなかった。周辺の代謝物は対応する酵素の量で予測できた一方、中心代謝の代謝物は複数の因子の組み合わせを必要とし、対応する経路の発現を反映しないことがあった。

この三つは、どれかが間違っているというより、どの代謝物を、どの予測の基準で評価するかの違いと読める。共通して言えるのは、**経路の酵素の発現から、その経路の代謝物の量がそのまま読めるとは限らない**ことである。ただし、これは代謝物の量についての結果であり、能力や流れを推定する手法を直接否定するものではない。能力や流れの推定値を「代謝物が多い・少ない」と読み替えるときに、注意が必要だということである。

## 照らし合わせる方法とその限界 {#_3}

単一細胞の代謝状態の推定を確かめる方法として、以下の方法では、照合できる対象が異なる。

表2　代謝状態の推定を照合する測定とその限界。

| 照合の方法 | 確かめられること | 限界 |
| --- | --- | --- |
| 同じ試料のバルクのメタボロミクス、同位体標識と代謝フラックス解析 | 細胞集団の平均として、推定が量や流れと合うか | 細胞ごとの違いは確かめられない |
| 空間メタボロミクス（質量分析イメージングなど）と空間トランスクリプトミクス | 組織の場所ごとの代謝物の分布と推定が合うか | 測れる代謝物と解像度に限りがある |
| 細胞を分離してからのメタボロミクス | 細胞の種類ごとの量の違い | 分離の操作そのものが代謝物を変えうる |
| 代謝への介入（栄養の除去、酵素の欠損、阻害剤） | 介入したときに、推定が予想どおりの方向に変わるか | 次の節で述べる |

既知の生物学（腸の場所による代謝の違いなど）を再現することは大切な確認である。ただ、それを強い証拠として読むには、細胞の種類の名前だけを使うような単純な基準と比べて、推定がどれだけ情報を足したかも示されているかが解釈を分ける。

## 介入で確かめるときの落とし穴 {#_4}

[予測と機序の関係を論じた記事](prediction-vs-mechanism.html)で書いたように、観察データでパターンを再現できることは、介入の結果を正しく予測できることを保証しない。代謝状態の推定を、創薬の標的探しや患者の層別に使うなら、介入の結果を予測できるかを確かめる必要がある。ただし、転写データを入力にする推定器を介入で確かめるときには、特有の落とし穴がある。

### 入力から自明に出る変化

 酵素の遺伝子を欠損させれば、その遺伝子の発現は下がり、推定器はその反応の低下を当然のように示す。これは推定器の能力の証拠にならない。確かめたいのは、欠損の影響が離れた反応や経路にどう波及するか、といった自明でない予測である。
### 介入後の時間と適応応答

 阻害剤は酵素の活性を直接下げるが、mRNAはすぐには変わらない。転写データに現れるのは、その後の適応的な応答である。フィードバックで転写が逆向きに動くこともある。例えば、コレステロール合成を阻害すると、その経路の遺伝子の転写はむしろ上がる方向に働く。介入後のどの時点の何を予測するのかを決めておく必要がある。
### 予測対象に対応する独立測定

 介入の結果を細胞の表現型で読むのか、代謝物や流れで読むのかを区別しなければならない。推定器の検証には、転写データとは独立した測定（メタボロミクスや同位体標識）で正解を取ることが望ましい。
### 介入後の当てはめと事前予測

 介入後のデータに手法を当てはめて差を見ることと、介入の結果を事前に予測してから確かめることは違う。後者の方が強い証拠になる。

## 創薬の現場から見た注意 {#_5}

推定が正しくても、その結論がどの環境で成り立つかは別の問題である。同じがんの遺伝子変異を持つ細胞でも、培養皿の上と生体の中では代謝への依存が異なることが報告されている ([7](#ref-7))。 培地の組成を人の血漿に近づけるだけで、細胞の代謝が大きく変わることも示されている ([8](#ref-8))。 腫瘍の中では、がん細胞と免疫細胞が栄養を奪い合い、酸素の濃度も場所によって違う。

代謝を標的とする薬では、前臨床の根拠が臨床での効果につながらなかった例もある。トリプトファン代謝を担うIDO1の阻害薬epacadostatは、抗PD-1抗体との併用で上乗せ効果を示せなかった ([9](#ref-9))。 グルタミナーゼ阻害薬telaglenastatも、腎がんでの併用で無増悪生存期間を改善しなかった ([10](#ref-10))。 これらの失敗は推定器の問題ではないが、代謝の知見を判断に使うことの難しさを示している。

## 量と流れは異なる照合対象である {#_6}

代謝物が多いことと、その代謝物を通る流れが大きいことは同じではない。転写量から得たスコアが代謝物量や表現型と関連しても、フラックスそのものが検証されたことにはならない。

MeRNのような手法による照合や応用も、何を推定し、どの環境のどの測定と一致したかによって意味が変わる。培養条件内の関連を、別の組織や生体内でも成り立つ定量的な代謝流量へ読み替えることはできない。

## 参照 {#article-references}

1. <span id="ref-1"></span>Lewinsohn DP, Dias N, Chau A, Koike Y, Smith ZD, Ioannidis NM, et al. Extracting interpretable single-cell metabolic states with graph-guided representation learning. bioRxiv [preprint]. 2026 Sep 24. [doi:10.64898/2026.09.17.751504](https://doi.org/10.64898/2026.09.17.751504).
2. <span id="ref-2"></span>Wagner A, Wang C, Fessler J, DeTomaso D, Avila-Pacheco J, Kaminski J, et al. Metabolic modeling of single Th17 cells reveals regulators of autoimmunity. Cell. 2021;184(16):4168–4185.e21. [doi:10.1016/j.cell.2021.05.045](https://doi.org/10.1016/j.cell.2021.05.045).
3. <span id="ref-3"></span>Alghamdi N, Chang W, Dang P, Lu X, Wan C, Gampala S, et al. A graph neural network model to estimate cell-wise metabolic flux using single-cell RNA-seq data. Genome Research. 2021;31(10):1867–1884. [doi:10.1101/gr.271205.120](https://doi.org/10.1101/gr.271205.120).
4. <span id="ref-4"></span>Li H, Barbour JA, Zhu X, Wong JWH. Gene expression is a poor predictor of steady‐state metabolite abundance in cancer cells. The FASEB Journal. 2022;36(5):e22296. [doi:10.1096/fj.202101921RR](https://doi.org/10.1096/fj.202101921RR).
5. <span id="ref-5"></span>Cavicchioli MV, Santorsola M, Balboni N, Mercatelli D, Giorgi FM. Prediction of Metabolic Profiles from Transcriptomics Data in Human Cancer Cell Lines. International Journal of Molecular Sciences. 2022;23(7):3867. [doi:10.3390/ijms23073867](https://doi.org/10.3390/ijms23073867).
6. <span id="ref-6"></span>Schildcrout R, Smith K, Bhowmick R, Lu Y, Menon S, Kapadia M, et al. Metab8D: a metabolic regulome network from multiomics and machine learning. Communications Biology. 2026;9(1):1161. [doi:10.1038/s42003-026-10409-3](https://doi.org/10.1038/s42003-026-10409-3).
7. <span id="ref-7"></span>Davidson SM, Papagiannakopoulos T, Olenchock BA, Heyman JE, Keibler MA, Luengo A, et al. Environment Impacts the Metabolic Dependencies of Ras-Driven Non-Small Cell Lung Cancer. Cell Metabolism. 2016;23(3):517–528. [doi:10.1016/j.cmet.2016.01.007](https://doi.org/10.1016/j.cmet.2016.01.007).
8. <span id="ref-8"></span>Cantor JR, Abu-Remaileh M, Kanarek N, Freinkman E, Gao X, Louissaint A, et al. Physiologic Medium Rewires Cellular Metabolism and Reveals Uric Acid as an Endogenous Inhibitor of UMP Synthase. Cell. 2017;169(2):258–272.e17. [doi:10.1016/j.cell.2017.03.023](https://doi.org/10.1016/j.cell.2017.03.023).
9. <span id="ref-9"></span>Long GV, Dummer R, Hamid O, Gajewski TF, Caglevic C, Dalle S, et al. Epacadostat plus pembrolizumab versus placebo plus pembrolizumab in patients with unresectable or metastatic melanoma (ECHO-301/KEYNOTE-252): a phase 3, randomised, double-blind study. The Lancet Oncology. 2019;20(8):1083–1097. [doi:10.1016/S1470-2045(19)30274-8](https://doi.org/10.1016/S1470-2045(19)30274-8).
10. <span id="ref-10"></span>Tannir NM, Agarwal N, Porta C, Lawrence NJ, Motzer R, McGregor B, et al. Efficacy and Safety of Telaglenastat Plus Cabozantinib vs Placebo Plus Cabozantinib in Patients With Advanced Renal Cell Carcinoma. JAMA Oncology. 2022;8(10):1411. [doi:10.1001/jamaoncol.2022.3511](https://doi.org/10.1001/jamaoncol.2022.3511).
