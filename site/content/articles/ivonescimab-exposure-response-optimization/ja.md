基準日：本記事の事実関係は2026年11月5日時点の公開情報による。

## 要旨

PD-1（programmed cell death-1）とVEGF-A（vascular endothelial growth factor A）に結合する二重特異性抗体イボネスチマブ（AK112）の公開論文には、用量群ごとの薬物動態（PK）の要約、PD-1占有率、VEGFの変化率、レジメン別の奏効率（ORR）と治療関連有害事象（TRAE）の件数が散在する。本記事は、これらの集計値だけで用量と投与間隔の比較がどこまで定量的に支えられるかを、再実行できる解析で確認した。個体データと図の読み取りは使っていない。

第I相の群要約（3–30 mg/kg）は線形の2コンパートメントモデルで説明され、用量比例性の勾配は1に近かった（無限大時間までの濃度時間曲線下面積AUC0-∞で1.04、90%区間0.95–1.12）。2コンパートメントの利得は初回投与後の谷濃度7点に由来し、見かけの半減期（t1/2）の窓の仮定に左右された。週あたりの用量強度が同じ20 mg/kg Q2W（2週ごと）と30 mg/kg Q3W（3週ごと）は、平均定常状態濃度が構造上等しく、30 mg/kg Q3Wの最高濃度は約1.34倍（パラメータ不確実性の95%信用区間1.32–1.36）、最低濃度は0.58倍（1コンパートメント）から0.78倍（2コンパートメント、0.63–0.85）と予測された。PD-1占有率は3 mg/kgでDay 2とDay 8に約93–98%に達し、測定前の基準値が23.6–56.2%と動いたため、用量間の差を判別できなかった。化学療法併用の第II相（10対20 mg/kg Q3W）では、奏効率の2倍あたり対数オッズ比が−0.17（95%信用区間−0.99から0.64、オッズ比0.37–1.9）で、向きも大きさも決まらなかった。20 mg/kg Q3Wの第III相は薬剤の比較であり、用量の比較ではない。用量と間隔の最適化は公開データからは決められない。

## 背景と目的

イボネスチマブは、PD-1とVEGF-Aの両方に結合する四価の二重特異性抗体である。組換えタンパク質を使った試験管内の実験では、VEGFが存在するとPD-1への結合が18倍以上に高まると報告されている ([1](#ref-1))。協調条件下の親和性の具体値は原著の図にだけあり、本記事は推定していない。

ヒトでは、中国の第I相（AK112-102）が3–30 mg/kgのQ2Wと10・20 mg/kgのQ3Wを評価し ([2](#ref-2))、オーストラリアの第Ia相（AK112-101）が0.3–30 mg/kgのQ2Wを評価した ([3](#ref-3))。第Ib/II相（AK112-202、HARMONi-5の名称で報告）は、免疫療法未治療の非小細胞肺がん（NSCLC）で10 mg/kg Q3W、20 mg/kg Q2W、20 mg/kg Q3W、30 mg/kg Q3Wを非ランダム化で比べた ([4](#ref-4))。化学療法併用の第II相（AK112-201）は10と20 mg/kg Q3Wを逐次割付した ([5](#ref-5))。第III相のHARMONi-2は20 mg/kg Q3W単剤とペムブロリズマブを比較した ([6](#ref-6))。HARMONi-6は扁平上皮がんで、イボネスチマブ20 mg/kg Q3Wとパクリタキセル・カルボプラチンの併用を、チスレリズマブの同併用と比較した。無増悪生存期間は2025年に ([7](#ref-7))、全生存期間は2026年に報告された ([8](#ref-8), [9](#ref-9))。

2026年11月5日時点の規制状況は、会社の一次資料によると次のとおりである。Akesoの製品ページは中国での承認を2024年5月（EGFR［上皮成長因子受容体］変異陽性の非扁平上皮がん、EGFRチロシンキナーゼ阻害薬［TKI］後の化学療法併用）と2025年4月（PD-L1［programmed death-ligand 1］陽性の一次治療単剤）と記載し ([10](#ref-10))、扁平上皮がんの一次治療（化学療法併用）の承認を2026年8月12日に発表した ([11](#ref-11))。HARMONi-6の無増悪生存期間が欧州臨床腫瘍学会（ESMO）2025で発表されたことは、Akesoの発表に記載されている ([11](#ref-11))。全生存期間は米国臨床腫瘍学会（ASCO）2026で報告された ([9](#ref-9))。米国ではSummit Therapeuticsが、HARMONi（EGFR変異・第三世代TKI後・非扁平上皮がん）の生物学的製剤承認申請（BLA）が2026年1月に受理され、審査目標日（PDUFA日）が2026年11月14日で、2026年11月5日時点で承認はないと述べている ([12](#ref-12))。この審査目標日は本記事の公開予定日より前で、公開時点では決定がなされている可能性がある。中国の国家薬品監督管理局（NMPA）のデータベースと米国食品医薬品局（FDA）の文書は確認しておらず、会社の記述である。

承認された用量は主に20 mg/kg Q3Wである。問いは、公開された集計値が、検討されたレジメン間の用量と投与間隔の定量的な比較をどこまで支えるか、である。次の5つの下位の問いを立てた。Q1：PD-1占有率は用量の飽和を判別できるか。Q2：VEGFの変化は投与間隔に依存するか。Q3：奏効の用量反応はレジメン別に同定できるか。Q4：曝露と毒性の関係は同定できるか。Q5：20 mg/kg Q3Wについて、支持される点・支持されない点・決められない点は何か。用量の推奨は目的としない。

## 対象と確認範囲

表1に、資料と、取り出した内容・得られなかった内容を示す。いずれの資料にも個体データは公開されていない。15 mg/kg Q3Wは試験されておらず、探索的な仮想レジメンである。

表1：資料と抽出範囲

| ID | Source | Extracted | Not available |
| --- | --- | --- | --- |
| A | Phase I, AK112-102 ([2](#ref-2)); Cancer Med 2025; CC BY | [Table 3](https://doi.org/10.1002/cam4.70653) NCA mean (SD) by dose group; mean trough by day (supplementary Table S7); Table 5 PD-1 occupancy and VEGF % change; Table 2 Grade 3+ TRAE counts | Concentration-time points (original Figure 2 is an image); subject-level data; n per time point; absolute VEGF; efficacy |
| B | Phase Ia, AK112-101 ([3](#ref-3)); JITC 2024 | Supplementary Tables S2 and S3 mean (SD) PK for 0.3 to 30 mg/kg Q2W; Table 2 Grade 3+ TRAE counts | Occupancy and free VEGF values (original Figure 4 only); any Q3W cohort |
| C | Phase Ib/II, AK112-202 ([4](#ref-4)); JTO 2024; abstract only | ORR percentages in the abstract for four regimens (PD-L1+, first line, n = 67 in total) | Full text; n, events, intervals and Grade 3+ TRAE by regimen |
| D | Phase II, AK112-201 + chemotherapy ([5](#ref-5)); eClinicalMedicine 2023 | Table 2 ORR n and events by cohort and dose (10 vs 20 mg/kg Q3W); Table 3 Grade 3+ TRAE by dose (cohorts pooled) | Cohort-by-dose adverse events; randomisation |
| E | HARMONi-2 and HARMONi-6 ([6](#ref-6)-[9](#ref-9)), conference slides ([13](#ref-13)), company release ([14](#ref-14)), news summaries ([15](#ref-15), [16](#ref-16)) | Arm sizes, Grade 3+ TRAE counts, hazard ratios, cut-off dates | Peer-reviewed full text for the 2026 HARMONi-2 overall-survival update |
| G | Non-clinical binding ([1](#ref-1)); iScience 2025 | KD of PD-1 and VEGF; ELISA EC50 | KD values under cooperative conditions (original Figures 3B and 4B are images) |

略語：NCA、非コンパートメント解析。SD、標準偏差。KD、解離定数。EC50、半数効果濃度。Grade 3+、Grade 3以上。ELISA、酵素結合免疫吸着法。

Aの定常状態の例数は、原著のTable 3で全群5と記載され、登録人数（6–12）と整合しない。本記事はこの表記の群サイズを標準誤差の算出に使い、不整合は解消していない（30 mg/kg Q2Wの一部の値はn = 4）。Table 3の値は同じ被験者から導かれたNCAの要約である。第Ia相（B）と用量が重なるのは3・10・20・30 mg/kg Q2Wだが、Bの3 mg/kgは2例で、Bに5 mg/kg群とQ3W群はなく、2つの試験は対象集団と採血の設計が異なる。

## 方法

用量はmg/kg、体積は体重あたり（L/kg）、クリアランス（CL）はL/day/kgで表した。1コンパートメント（1c）と2コンパートメント（2c）の線形モデルを、1.5時間の点滴入力で比べた（報告は60–120分で、1.0と2.0時間も確認した）。

\[ V_1\frac{dC_1}{dt}=R(t)-CL\,C_1-Q\,(C_1-C_2),\qquad V_2\frac{dC_2}{dt}=Q\,(C_1-C_2) \]

\(R(t)\) は点滴速度（mg/kg/day）、\(C_1\)・\(C_2\) は中心と末梢の濃度（µg/mL）、\(V_1\)・\(V_2\) は中心と末梢の容積、\(Q\) はコンパートメント間クリアランスである。1cは \(Q=0\) の場合にあたる。閉じた式の解を、常微分方程式の数値解と固定刻みのRK4法で検証した（図1）。

![図1：モデルの構造と、集計値との対応](shared/ivonescimab-exposure-response-optimization/figures/fig1_model_structure.png)

図1：機序の文脈（A）、線形PKモデル（B）、モデルに結びつけた公開集計値（C）。

校正には、単回投与後の最高濃度（Cmax）、無限大時間までの濃度時間曲線下面積（AUC0-∞）、見かけの終末半減期（t1/2）、初回投与間隔の終わりの谷濃度（Table S7のDay 15またはDay 22の投与前値）を同時に尤度へ入れた。これらは同じ被験者に由来して相関し、1cではt1/2がCLとV1から決まるため二重計上になる。この過信を弱めるため、群 \(g\) の要約 \(m\) を

\[ \log y_{gm}=\log f_m(\theta;d_g,\tau_g)+\eta_{gm}+\varepsilon_{gm},\quad \varepsilon_{gm}\sim N(0,\mathrm{se}_{gm}^2),\ \eta_{gm}\sim N(0,\sigma_m^2) \]

とした。\(\theta\) はモデルのパラメータ、\(d_g\) は用量、\(\tau_g\) は投与間隔、\(f_m\) はモデルの予測である。seは報告されたSDから変動係数／√nで求め、\(\sigma_m\) は用量群間の異質性（集団、採血、測定の違い）で、個体間変動ではない。モデルのt1/2は3–14日の濃度から求めた。CL・Vz（NCAの分布容積）・平均濃度・蓄積比（Rac）は他の要約から導かれるため校正に使わない。周辺尤度を最大化し、弱情報の事前分布の下で適応的Metropolis法（1本のチェーン、70,000反復、焼き捨て15,000、間引き20）により事後分布を得た。プロファイル尤度で2cの識別性を確かめ、AICと小標本補正のAICc（観測28点）を比べた。定常状態の要約（Cmax,ss、最低濃度Cmin,ss、AUC0-τ,ss、Rac）、Table S7の谷濃度の時間経過、第Ia相は校正に使わず、予測との比較にだけ用いた。

レジメンは10・20・30 mg/kg Q3W、20 mg/kg Q2Wと、仮想の15 mg/kg Q3Wとした。週あたりの平均用量強度は3.33・6.67・10.00・10.00・5.00 mg/kg/weekである。42日（Q2Wの3間隔、Q3Wの2間隔）を共通の窓にして、同じ窓での平均濃度を比べた。個体間変動は、報告されたCLの変動係数（15.4–27.0%）を含む範囲を条件付きのシナリオ入力とし（CLの変動係数15・25・35%）、CLと中心容積に対数正規の変動を与えた（相関0または0.5）。共分散は推定していない。

PD-1占有率（RO）は、群・時点の平均値を、モデルの典型例の濃度に対して比べた。測定前（Day 1投与前）の値 \(a_g\)（%）を測定のオフセット、\(b\) を占有率の上限（%）として、

\[ \mathrm{RO}_{gt}=a_g+(b-a_g)\,\frac{C_{gt}}{C_{gt}+EC_{50}} \]

を、標準誤差の下限を1・3・5パーセントポイント（pp、百分率の差）として重み付き最小二乗で当てはめ、\(EC_{50}\) のプロファイルを調べた。試験管内KDは分子量150–200 kDaを仮定して µg/mL に換算した（文脈のみ）。

奏効率と有害事象は、事前分布Beta(2, 2)のBeta-二項モデルで事後分布を求め、事前分布の感度（Jeffreys、一様、有益、懐疑）を確かめた。第II相の用量勾配は、コホートごとの切片を数値積分で消した層別ロジスティックモデルで、用量の2倍あたりの対数オッズ比として求めた。第I相の有害事象は、log2用量に対するロジスティック回帰の勾配を格子上の事後分布で求めた。第Ib/II相（C）はレジメン別の例数がなく、抄録に記載された割合を示すだけで、件数・区間・勾配は計算していない。全ての数値は `analysis.py` の出力（`results/`）に由来し、乱数シードは20261105である。

## 結果

### 薬物動態

Q2Wの3–30 mg/kgの群平均から求めた用量比例性の勾配は、Cmaxが0.99（90%区間0.87–1.11）、AUC0-∞が1.04（0.95–1.12）で、原著の個体レベルの勾配（0.96と1.04）([2](#ref-2), [Table 4](https://doi.org/10.1002/cam4.70653))と矛盾しなかった（`pk_dose_proportionality.csv`）。用量で規格化した値は群平均に対して約−15%から＋30%散らばり（図2）、この異質性を \(\sigma_m\)（0.07–0.13）で取り込んだ。

![図2：用量群のPK要約とモデル](shared/ivonescimab-exposure-response-optimization/figures/fig2_pk_dose_groups.png)

図2：単回投与のCmaxとAUC0-∞を用量で割った値（上と中央）と、初回投与間隔の終わりの谷濃度（下）。点は群平均、誤差線は±1.96 SE（標準誤差）。線は1cと2cの当てはめ。

2cは1cより当てはまりがよく（AICの差−8.7、AICcの差−5.1、AICcの重み0.93）、中心のCLは0.0065 L/day/kg（95%信用区間0.0057–0.0071）、\(V_1\) は0.051 L/kg（0.046–0.055）、\(Q\) は0.0058 L/day/kg（0.0023–0.0096）、\(V_2\) は0.039 L/kg（0.010–0.072）だった。\(Q\) と \(V_2\) のプロファイル尤度の95%区間も有限だった。2cの終末半減期は12.8日で、3–14日の見かけの半減期は6.3日であり、報告されたNCAのt1/2（5.0–7.3日）([2](#ref-2), Table 3)と矛盾しない。

この利得は脆い。第一に、利得は初回間隔の谷濃度7点が担い、谷濃度を外すと消え（AICの差＋1.1）、\(Q\) の上限が定まらなかった。第二に、t1/2を外すと \(Q\) は約4倍の0.024になり、t1/2の窓を3–21日にすると \(Q\) は0.0027、AICcの差は＋0.6で、2cの優位は消えた。第三に、低濃度での早い消失（標的を介した消失や抗薬物抗体）も、末梢コンパートメントと同様に谷濃度を説明し得る。第四に、2cは後述の定常状態の確認で一部を外した。以上から、2cは谷濃度7点を最もよく説明する構造として主要モデルに採るが、1cを構造の代替案として併記し、レジメン間の比は両者の範囲で示す。MCMCの診断は、2cで分割R-hatが1.000–1.005、有効標本数が376–1,261（2,750本中）だった。下流の解析は全チェーンから等間隔に取った400–500本を使った。事前分布の標準偏差を0.5倍・2倍にしても、\(Q\) の信用区間下限は0.0031–0.0020、最低濃度比の下限は0.69–0.62で結論は変わらなかった。

校正に使ったAUC0-∞はNCAの外挿を含み、真値とは限らない。2cの終末半減期（12.8日）がNCAのt1/2（5–7日）より長いと、Q2WのAUC0-∞は過小になり、校正のCLが約10%高く出る可能性がある。AUC0-∞の観測値を10%増やすとCLは0.0060（約7%減）、AUC0-∞を外すと2cのCLは0.0049になった。

定常状態の予測と報告値（Table 3）の比は、2cでCmax,ssが幾何平均1.06（範囲0.87–1.37）、Cmin,ssが0.88（0.61–1.33）、AUC0-τ,ssが1.10（0.92–1.43）で、大きな乖離は見られなかった（図3上）。ただし、この確認は検出力が低い（異質性とSEを合わせた区間が広い）。報告されたAUC0-τ,ssは単回のAUC0-∞の1.14倍（1.02–1.27）、CLssはCLの0.87倍（0.77–0.97）で、線形・時間不変のモデルが予測する1.0より外れた。説明として、時間に依存するCLの低下、疾患や抗薬物抗体の影響、NCAの外挿の偏りが同程度にあり得る。外挿が不足してt1/2が過小になれば、AUC0-∞が過小になり、比は1より大きくなる（偏りの大きさは採血設計に依存し、本記事では推定していない）。Table S7の谷濃度の時間経過は、2cで群全体の平均比が約1.0だったが、20 mg/kg Q2Wの後期（Day 197）の値は予測の2.1倍に達した（図3中央）。時点ごとの例数が不明で、脱落による選択は評価できない。

![図3：蓄積の予測と第Ia相との比較](shared/ivonescimab-exposure-response-optimization/figures/fig3_accumulation_external.png)

図3：定常状態NCAの報告値と予測の比（上）、20 mg/kgの谷濃度の時間経過（中央）、第Ia相との比較（下）。比が1に近いほど一致する。

第Ia相（[JITC 2024の補足表](https://doi.org/10.1136/jitc-2023-008037)；[3](#ref-3)）の10・20・30 mg/kg Q2Wの値は、校正に使わず、単回のCmaxとAUC0-∞が予測の1.01–1.30倍、定常状態の3つの要約が0.95–1.45倍だった（2c、幾何平均1.15と1.29）。重なる用量でのCmaxとAUC0-∞は第I相より幾何平均1.22倍（範囲1.00–1.39）高かった（`pk_B_over_A.csv`）。2つの試験は対象、採血、測定法、NCAの規約が異なるため、これは独立したモデルの検証ではなく、曝露水準の試験間差の評価である。

### レジメンの定常状態曝露

線形PKでは、同じ平均用量強度なら平均定常状態濃度は等しい。20 mg/kg Q2Wと30 mg/kg Q3Wは、42日の窓の平均濃度が両モデルで一致した（2cで221 µg/mL）。これはモデル構造の帰結であり、発見ではない。違いは濃度の形に現れる（表2、図4）。

表2：定常状態の濃度（典型例、2コンパートメント、µg/mL）

| Regimen | Dose intensity (mg/kg/week) | Cmax,ss (95% CrI) | Cmin,ss (95% CrI) | Cavg,ss |
| --- | --- | --- | --- | --- |
| 10 mg/kg Q3W | 3.33 | 225 (207–243) | 29.6 (18.8–37.8) | 73.8 |
| 15 mg/kg Q3W (hypothetical) | 5.00 | 338 (310–365) | 44.3 (28.2–56.6) | 110.7 |
| 20 mg/kg Q3W | 6.67 | 451 (414–487) | 59.1 (37.6–75.5) | 147.6 |
| 20 mg/kg Q2W | 10.00 | 504 (465–544) | 112.4 (88.1–134.4) | 221.4 |
| 30 mg/kg Q3W | 10.00 | 676 (621–730) | 88.7 (56.4–113.3) | 221.4 |

略語：CrI、信用区間。Cmax,ss、Cmin,ss、Cavg,ss、定常状態の最高・最低・平均濃度。区間は典型例の予測に対するパラメータ不確実性のみで、個体間変動、点滴の長さ、モデル構造の不確実性を含まない。第Ia相の曝露水準は第I相より約1.2倍高く（幾何平均1.22）、この差は区間より大きいため、絶対濃度の不確実性は表の区間より大きい。この水準の差は推定ではなく仮定として扱い、レジメン間の比には影響しないとした。30 mg/kg Q3Wの定常状態を観測した群はなく、線形性による外挿である。

対にした比（30 mg/kg Q3W／20 mg/kg Q2W）は、パラメータ不確実性のみの95%信用区間で、Cmax,ssが2cで1.34（1.32–1.36）、1cで1.33（1.31–1.34）、Cmin,ssが2cで0.78（0.63–0.85）、1cで0.58（0.55–0.61）だった。最低濃度の比は構造に依存するため、0.58–0.78の範囲で示す。個体間変動のシナリオ（CLとV1のみに変動を与え、\(Q\) と \(V_2\) は典型値）では、Cmax,ssの比の2.5–97.5%範囲が1.20–1.45、Cmin,ssの比が2cで0.69–0.87、1cで0.31–0.77だった。\(Q\)（変動係数50%）と \(V_2\)（30%）にも変動を与えたシナリオでは、2cのCmin,ss比が0.79（0.66–0.87）だった。線形モデルでは、30 mg/kg Q3Wの最高濃度が高く最低濃度が低いことは構成上の恒等であり、所見ではない。

![図4：等しい用量強度の定常状態の濃度](shared/ivonescimab-exposure-response-optimization/figures/fig4_regimen_profiles.png)

図4：20 mg/kg Q2Wと30 mg/kg Q3Wの42日の窓の濃度（上）と、同じ仮想被験者の対の比（中央、下）。帯と分布は条件付きのシナリオ入力（CL 25%、V1 20%）に基づく。

### PD-1占有率とVEGF

測定前（Day 1投与前）の占有率は、群平均で23.6–56.2%（群内SDの平均27.6pp）あり、用量順位と強く相関した（スピアマンの順位相関0.93、7群）。投与後は、Day 8で93.1–99.8%、投与前値の時点平均で92.1–95.6%、群内SDの平均は6.1ppだった（図5、[Table 5](https://doi.org/10.1002/cam4.70653)の群平均から本記事が計算；[2](#ref-2)）。3 mg/kgのDay 2とDay 8は97.5%と93.1%だが、以後の投与前値の平均は88.3–100%に散らばる。Day 8の用量勾配は、Q2Wの5群で10倍あたり5.5pp（95%区間1.2–9.8）と小さく、0を含まない。基準値とDay 8の相関（0.76）が高いため、用量の効果と測定の基準値の差を分けられない。最低のモデル濃度（13.2 µg/mL）は、試験管内KDの換算値（0.037–0.049 µg/mL）の270–360倍にあたり、1対1結合を仮定した占有率は99.6%を超える。つまり占有率は、3 mg/kg以上でほぼ頭打ち（90%超）で、小さな用量傾向は除けない。測定法の上限が100%に届かない可能性もある。

![図5：PD-1占有率](shared/ivonescimab-exposure-response-optimization/figures/fig5_pd1_occupancy.png)

図5：群ごとの基準値と投与後の占有率（上）、占有率とモデル濃度（中央）、\(EC_{50}\) のプロファイル（下）。RO、PD-1占有率。

占有率の \(EC_{50}\) の95%区間の上限は、標準誤差の下限を1・3・5ppにすると0.40・1.26・1.58 µg/mLと4倍動いた。当てはめのカイ二乗／自由度は251/58・81/58・35/58で、下限が1・3ppでは当てはまりが悪い。下限は、3ppのときだけ0.10 µg/mLに定まった。\(EC_{50}\) の上限は、双曲線モデル、\(b\) の上限、群ごとのオフセット、同じ患者の反復測定を独立な点として扱う仮定に条件付きで、区間は楽観的である。0.3・1 mg/kgの占有率は第Ia相の図にだけあり、数値表はない。

VEGFの変化率（[Table 5](https://doi.org/10.1002/cam4.70653)）は、投与終了時の群平均が−88.6から−55.4%、投与前の群平均が−55.8から−19.6%で、回復が見られた（図6）。投与前の変化率と予測される投与前濃度の関係は、勾配が10倍あたり3.6pp（群についてのブートストラップ95%区間−44から34、47点・7群）で、濃度依存性は検出されなかった。この区間の幅は観測された変化の幅（約36pp）に匹敵し、情報量は乏しい（7群のブートストラップは被覆が不足し得る）。同じ用量でのQ3WとQ2Wの差（投与前の平均）は、10 mg/kgで31pp（−12から81）、20 mg/kgで16pp（−20から53）で、いずれも0を含む。この区間は反復する時点を独立とみなしており、Q3Wの投与前採血が投与後21日、Q2Wが14日であるという設計の違いと交絡する。10 mg/kg Q3Wの初回投与後の＋162%は、原著が基準値が定量下限未満の1例によると説明している。測定が遊離VEGFか総VEGFかは本文に明記されておらず、絶対濃度もない。投与後の低下の符号は遊離VEGF（または抗体の干渉を受けたアッセイ）と整合するが、決められない。基準値が定量下限（15.6 pg/mL）に近い群の平均変化率は、少数の被験者に支配される。組織中VEGFの抑制や協調結合の程度は推定できない。

![図6：VEGFの変化率](shared/ivonescimab-exposure-response-optimization/figures/fig6_vegf_change.png)

図6：投与終了時と投与前のVEGFの変化率（上）と、投与前の変化率と予測濃度（下）。

濃度の閾値を仮に置くと、閾値を上回る時間割合の順位は閾値に依存する。42日の窓で、20 mg/kg Q2Wは閾値256 µg/mL以下の範囲で30 mg/kg Q3Wより長く閾値を上回り（差は最大で間隔の18%）、291 µg/mL以上では30 mg/kg Q3Wのほうが長い（最大6.5%）。この閾値は仮のもので、占有率やVEGFの効果に対応する値は同定されていない。レジメンの順位（表3）は、曝露指標を平均濃度・最高濃度・最低濃度のどれにするかで入れ替わり、モデル構造やパラメータの不確実性ではほぼ変わらなかった（図7）。

表3：曝露指標ごとの順位（2コンパートメント、同順位あり）

| Regimen | Rank by Cavg,ss | Rank by Cmax,ss | Rank by Cmin,ss |
| --- | --- | --- | --- |
| 10 mg/kg Q3W | 5 | 5 | 5 |
| 15 mg/kg Q3W (hypothetical) | 4 | 4 | 4 |
| 20 mg/kg Q3W | 3 | 3 | 3 |
| 20 mg/kg Q2W | 1 | 2 | 1 |
| 30 mg/kg Q3W | 1 | 1 | 2 |

![図7：レジメンの順位の感度](shared/ivonescimab-exposure-response-optimization/figures/fig7_sensitivity_ordering.png)

図7：曝露指標（色）とモデル構造（記号）に対するレジメンの順位（上）と、30 mg/kg Q3W対20 mg/kg Q2Wの比（下）。

### 奏効率と有害事象

化学療法併用の第II相（D）([5](#ref-5), [Table 2](https://doi.org/10.1016/j.eclinm.2023.102106))の奏効は、10と20 mg/kg Q3Wで、コホート1が10/19と13/24、コホート2が8/10と5/9、コホート3が4/10と4/10だった（分母は評価可能集団、FAS）。20対10 mg/kgの差（事後平均、95%信用区間）は、コホート1で＋1.4pp（−25.6から＋28.3）、コホート2で−17.5pp（−51.2から＋17.7）、コホート3で0pp（−35.3から＋35.2）だった（図8）。コホートを層とした共通の勾配は、2倍あたりの対数オッズ比が−0.17（−0.99から0.64）で、オッズ比0.84（0.37–1.91）は、オッズの半減も2倍近い増加も除けない。事前分布の標準偏差は1、事後は0.42で、データが標準偏差を58%減らしたが、区間はなお両方向を含む。コホート間の不均一性は、Cochran Qが0.97（自由度2、p = 0.61）、I²が0%で検出されなかったが、3コホートでは検出力が低く、コホートごとの差（＋1.4、−17.5、0pp）は交互作用を否定しない。変量効果の合併値は−0.18（−1.04から0.68）だった。奏効率50%を基準にすると、20 mg/kgの差は−4.2pp（−22.9から15.6）で、差が10pp未満である確率は0.63だった。20から30 mg/kgへの仮の外挿は−2.5pp（−14.1から＋9.3）だが、30 mg/kg Q3WはDにない。割付はコホート内で逐次かつ非ランダムで、用量と登録時期が交絡している。

![図8：奏効率の区間](shared/ivonescimab-exposure-response-optimization/figures/fig8_orr_intervals.png)

図8：Dの奏効率の事後平均と95%信用区間（上）、20対10 mg/kgの差（中央）、HARMONi-5の抄録に記載された割合（下、例数なし）。

Cの奏効率（[JTO 2024の抄録](https://doi.org/10.1016/j.jtho.2023.10.014)；[4](#ref-4)）は、10 mg/kg Q3Wが33.3%、20 mg/kg Q2Wが52.6%、20 mg/kg Q3Wが60.0%、30 mg/kg Q3Wが75.0%（PD-L1陽性・一次治療の67例）である。レジメン別の例数は得られないため、件数・区間・用量反応の勾配は計算せず、単アームの試験内の非ランダム化の用量コホートの比較であって、ランダム化された用量比較ではない。

Grade 3以上のTRAEは、第I相（A、単剤）([2](#ref-2), [Table 2](https://doi.org/10.1002/cam4.70653))で10・10・9・12・6・6・6例中、3・1・2・3・2・1・2例（3・5・10・20・30 mg/kg Q2W、10・20 mg/kg Q3Wの順）だった。Q2Wの5群のlog2用量に対する勾配は、2倍あたりのオッズ比が1.09（0.63–1.94、勾配が正の確率0.63）で、第Ia相の10・20・30 mg/kg（6/19、5/18、2/7）([3](#ref-3))では0.89（0.34–2.31）だった。Dの化学療法併用（安全性解析対象、コホート統合）([5](#ref-5), [Table 3](https://doi.org/10.1016/j.eclinm.2023.102106))では、9/40（22.5%）と13/43（30.2%）で、差は＋6.9pp（−11.6から＋25.1、正の確率0.77）だった。ORRの分母（FAS）とTRAEの分母（安全性解析対象）は異なる。事前分布を5種類に変えると、少数の群は動いた（3 mg/kgの3/10は、Beta(2, 2)で0.14–0.61、懐疑的なBeta(1, 4)で0.08–0.51）。Beta(2, 2)は50%を中心とし、10–30%の毒性率には高めで、少数群を上へ引く。結論（区間が広い）は変わらなかった。Aの7群で、用量・平均濃度・最高濃度・最低濃度のどれを共変量にしても、帰無モデルよりAICが約1.7悪く（対数尤度の改善は0.12–0.14、AIC 68.4対66.7）、群レベルの曝露は用量と強く相関する（相関0.93–1.0）ため、用量またはいずれの曝露指標とも、Grade 3以上のTRAEとの検出可能な関係はなかった（図9、`er_A_trae_covariate_comparison.csv`）。治療期間と観察期間は群で異なるため、割合は曝露時間あたりの率ではない。

![図9：Grade 3以上のTRAE](shared/ivonescimab-exposure-response-optimization/figures/fig9_trae_intervals.png)

図9：Grade 3以上のTRAEの割合。Aは単剤の第I相、Dは化学療法併用、下は比較試験の文脈（用量比較ではない）。

第III相の文脈として、HARMONi-2（20 mg/kg Q3W単剤対ペムブロリズマブ）のGrade 3以上のTRAEは58/197（29%）と31/199（16%）([6](#ref-6))、HARMONi-6（化学療法併用対チスレリズマブ併用）は全生存期間の解析時点で184/266（69%）と156/265（59%）だった ([8](#ref-8))。件数は抄録の値で、差＋13.6pp（5.5–21.7）と＋10.2pp（2.1–18.2）はBeta(2, 2)の事後分布から本記事が計算した値である。追跡と曝露の期間が異なる累積割合である。これらは薬剤の比較であり、化学療法併用の毒性を単剤へ移さない。HARMONi-2の全生存期間は、2026年9月の発表で、ハザード比0.73（0.57–0.95）、中央値30.8対22.6か月とされた ([14](#ref-14))。カットオフが2026年8月20日であることは報道の要約によるもので、会社の発表文には日付がなく ([15](#ref-15), [16](#ref-16))、査読済みの論文は見つからなかった。更新時点のGrade 3以上のTRAEは見つかっていない。無増悪生存期間の解析（カットオフ2024年1月29日、追跡中央値8.67か月）は、2024年の世界肺癌学会（WCLC）の発表スライドに基づく ([13](#ref-13))。

### 識別性のまとめ

図10に、識別性の3つの要点を示す。2cの \(Q\)・\(V_2\) は有限の区間をもつが、初回間隔の谷濃度だけに依存する。奏効率とTRAEの用量勾配は、事後分布がなお0の両側に広がる。占有率の \(EC_{50}\) は標準誤差の下限の仮定で下限が動く。

![図10：識別性](shared/ivonescimab-exposure-response-optimization/figures/fig10_identifiability.png)

図10：2cの \(Q\) と \(V_2\) のプロファイル（上）、用量勾配の事後分布（中央）、占有率の \(EC_{50}\) のプロファイル（下）。

## 考察

Q1（占有率）：3 mg/kg以上でほぼ頭打ち（90%超）で、用量を判別できなかった。判別に必要な0.3・1 mg/kgの数値表は公開されていない。Day 8の小さな傾向は基準値のオフセットと分離できない。Q2（VEGF）：投与間隔による差は検出できず、遊離型か総量かも不明である。Q3（奏効の用量反応）：化学療法併用の2用量でもオッズ比0.37–1.9で向きも大きさも決まらず、単剤はレジメン別の例数がない。Q4（曝露と毒性）：検出可能な関係はなく、曝露指標は共線性のため区別できない。

Q5（20 mg/kg Q3W）：支持されるのは、この用量の谷濃度でも占有率が頭打ちの範囲にあること、HARMONi-2とHARMONi-6でこの用量が薬剤の比較として評価されていることである。線形性から導かれる帰結として、定常状態のCavgは10 mg/kg Q3Wの2倍、15 mg/kg Q3Wの約1.3倍である。支持されないのは、20 mg/kg Q3Wが他の用量・間隔より有効または安全だという用量の比較で、公開データにその比較はない。決められないのは、より高い用量（30 mg/kg Q3Wなど）や、同じ強度で間隔を変えた場合（20 mg/kg Q2W）の有効性と安全性の差である。後者の曝露の形の違い（最高濃度が約1.34倍、最低濃度が0.58–0.78倍）は予測できるが、臨床の差になるかは推定できない。最低濃度の比は、末梢コンパートメントの有無という構造に依存し、順位は動かさないが大きさを動かす。

## 限界

公開された値は用量群の平均（SD）と件数だけで、個体間の共分散も個体レベルの曝露と応答の組も作れない。\(\sigma_m\) は4–7点から推定した最尤値で、群内の相関を無視した尤度の過信は緩和にとどまる。用量比例性は5群の平均（自由度3）からの推定である。Table S7の標準誤差は、時点ごとの例数が不明なため下限である。変動シナリオは仮定である。第I相のCL×体重と原著のCLの比は0.75–1.23（幾何平均0.91）で、単位の誤りはないが、平均と中央値の違いやNCAの偏りによる±25%の差が残る。Dは非ランダム化の逐次割付で、有害事象はコホートを横断して統合されている。第III相の一部は抄録・学会スライド・会社発表に基づき、HARMONi-2の全生存期間の更新は査読済みの論文を確認していない。第I相の対象は多腫瘍型で、NSCLCは1例（A）と2例（B）である。規制の記述は会社の一次資料によるもので、NMPAのデータベースは確認していない。図11に、得られなかったデータをまとめる。

![図11：データの欠落](shared/ivonescimab-exposure-response-optimization/figures/fig11_data_gaps.png)

図11：資料ごとの利用可能性。yes：表で得られた、part：一部、no：得られなかった。

本記事は、筆者が使うAIによる査読（3回）を受けたが、人間の第三者による確認ではない。

## 結論

公開された集計値は、等しい用量強度のレジメン（20 mg/kg Q2Wと30 mg/kg Q3W）について、線形PKの構造から、平均濃度が等しく、最高濃度が約1.3倍、最低濃度が0.6–0.8倍になるという条件付きの予測を支えた。PD-1占有率とVEGFの変化は用量と間隔を区別せず、奏効率と毒性の用量反応は広い範囲でしか同定できなかった。20 mg/kg Q3Wの第III相は他の用量や間隔との比較を含まず、用量と間隔の最適化は公開データからは決められない。

## データとコードの公開状況

入力は原著の表から転記した集計値である。第I相（A）のCancer Medicineの論文はCC BYで、転記表を配布物に含む（転記と整形をしており、改変版である）。第Ia相（B）はCC BY-NC、化学療法併用の第II相（D）と非臨床の結合（G）はCC BY-NC-ND、抄録・学会資料・会社発表（CとE）は各権利者の著作物であるため、これらの転記表は配布しない。Bの外部比較、B・C・D・第III相の事後分布など、これらの数値から導いた結果表（`pk_external_B.csv`、`pk_B_over_A.csv`、`rates_B_*`、`rates_C_*`、`rates_D_*`、`rates_phase3_*`）も配布物から除き、入力を再抽出してコードを実行すると再生成される。再抽出の手順は `README-public.md` に記載した。解析（`analysis.py`、`stages_*.py`、`pkmodel.py`、`pkfit.py`、`rates.py`）、図（`figures.py`）、テスト（`test_analysis.py`、20関数・21ケース）、その他の結果のCSV/JSON、図を提供する。乱数シードは20261105で、Python 3.12、NumPy 2.2、SciPy 1.14、pandas 2.2、matplotlib 3.9を使った。B・C・D・E・Gを再抽出したうえで全体を再実行すると約4–5分かかり、結果はバイト単位で再現した。配布した入力（A）だけでは、これらの入力を読む段階（第Ia相との外部比較、占有率の当てはめ［G］、奏効・有害事象、データの欠落表）は実行できない。

再実行用の資料一式は[配布資料](shared/ivonescimab-exposure-response-optimization/ivonescimab-exposure-response-optimization-companion.zip)に置いた。


## 参照

<span id="ref-1"></span>1. Zhong T, Zhang L, Huang Z, Pang X, Jin C, Liu W, et al. Design of a fragment crystallizable-engineered tetravalent bispecific antibody targeting programmed cell death-1 and vascular endothelial growth factor with cooperative biological effects. iScience. 2025;28(3):111722. [https://doi.org/10.1016/j.isci.2024.111722](https://doi.org/10.1016/j.isci.2024.111722)
<span id="ref-2"></span>2. Wang F, Wei X, Zheng Y, Wang J, Ying J, Chen X, et al. Safety, pharmacokinetics, and pharmacodynamics evaluation of ivonescimab, a novel bispecific antibody targeting PD-1 and VEGF, in Chinese patients with advanced solid tumors. Cancer Med. 2025;14(6):e70653. [https://doi.org/10.1002/cam4.70653](https://doi.org/10.1002/cam4.70653)
<span id="ref-3"></span>3. Frentzas S, Austria Mislang AR, Lemech C, Nagrial A, Underhill C, Wang W, et al. Phase 1a dose escalation study of ivonescimab (AK112/SMT112), an anti-PD-1/VEGF-A bispecific antibody, in patients with advanced solid tumors. J Immunother Cancer. 2024;12(4):e008037. [https://doi.org/10.1136/jitc-2023-008037](https://doi.org/10.1136/jitc-2023-008037)
<span id="ref-4"></span>4. Wang L, Luo Y, Ren S, Zhang Z, Xiong A, Su C, et al. A phase 1b study of ivonescimab, a programmed cell death protein-1 and vascular endothelial growth factor bispecific antibody, as first- or second-line therapy for advanced or metastatic immunotherapy-naive NSCLC. J Thorac Oncol. 2024;19(3):465–475 [abstract only accessed]. [https://doi.org/10.1016/j.jtho.2023.10.014](https://doi.org/10.1016/j.jtho.2023.10.014)
<span id="ref-5"></span>5. Zhao Y, Chen G, Chen J, Zhuang L, Du Y, Yu Q, et al. AK112, a novel PD-1/VEGF bispecific antibody, in combination with chemotherapy in patients with advanced non-small cell lung cancer (NSCLC): an open-label, multicenter, phase II trial. EClinicalMedicine. 2023;62:102106. [https://doi.org/10.1016/j.eclinm.2023.102106](https://doi.org/10.1016/j.eclinm.2023.102106)
<span id="ref-6"></span>6. Xiong A, Wang L, Chen J, Wu L, Liu B, Yao J, et al. Ivonescimab versus pembrolizumab for PD-L1-positive non-small cell lung cancer (HARMONi-2): a randomised, double-blind, phase 3 study in China. Lancet. 2025;405(10481):839–849 [abstract only accessed]. [https://doi.org/10.1016/S0140-6736(24)02722-3](https://doi.org/10.1016/S0140-6736(24)02722-3)
<span id="ref-7"></span>7. Chen Z, Yang F, Jiang Z, Sun L, Wu L, Han Z, et al. Ivonescimab plus chemotherapy versus tislelizumab plus chemotherapy as first-line treatment for advanced squamous non-small-cell lung cancer (HARMONi-6): a randomised, double-blind, phase 3 trial. Lancet. 2025;406(10515):2078–2088 [abstract only accessed]. [https://doi.org/10.1016/S0140-6736(25)01848-3](https://doi.org/10.1016/S0140-6736(25)01848-3)
<span id="ref-8"></span>8. Lu S, Liu B, Luo Y, Sun L, Wu L, Han Z, et al. Ivonescimab plus chemotherapy versus tislelizumab plus chemotherapy in advanced squamous non-small-cell lung cancer (HARMONi-6): interim overall survival analysis of a randomised, double-blind, phase 3 trial in China. Lancet. 2026;407(10548):2620–2629 [abstract only accessed]. [https://doi.org/10.1016/S0140-6736(26)00966-9](https://doi.org/10.1016/S0140-6736(26)00966-9)
<span id="ref-9"></span>9. Chen Z, Yang F, Luo Y, Sun L, Wu L, Han Z, et al. Ivonescimab plus chemotherapy versus tislelizumab plus chemotherapy in previously untreated advanced squamous non-small cell lung cancer: overall survival results of the phase 3 HARMONi-6 trial. J Clin Oncol. 2026;44(17_suppl):LBA4 [conference abstract; abstract only accessed]. [https://doi.org/10.1200/JCO.2026.44.17_suppl.LBA4](https://doi.org/10.1200/JCO.2026.44.17_suppl.LBA4)
<span id="ref-10"></span>10. Akeso, Inc. PD-1/VEGF bispecific, Ivonescimab injection [Product page] [Internet]. Akeso; [date unknown] [cited 2026 Nov 5]. Available from: [https://www.akesobio.com/en/rd-and-science/products-center/ivonescimab/](https://www.akesobio.com/en/rd-and-science/products-center/ivonescimab/)
<span id="ref-11"></span>11. Akeso, Inc. Ivonescimab plus chemotherapy approved for first-line squamous NSCLC; HARMONi-6 establishes new gold standard in lung cancer treatment [Press release] [Internet]. Akeso; 2026 Aug 12 [cited 2026 Nov 5]. Available from: [https://www.akesobio.com/en/media/akeso-news/260812/](https://www.akesobio.com/en/media/akeso-news/260812/)
<span id="ref-12"></span>12. Summit Therapeutics Inc. Ivonescimab monotherapy demonstrates statistically significant overall survival benefit compared to pembrolizumab monotherapy in PD-L1-positive advanced NSCLC in HARMONi-2 study conducted by Akeso in China [Press release] [Internet]. Summit Therapeutics; 2026 Sep 2 [cited 2026 Nov 5]. Available from: [https://s206.q4cdn.com/652410165/files/doc_news/Ivonescimab-Monotherapy-Demonstrates-Statistically-Significant-Overall-Survival-Benefit-Compared-to-Pembrolizumab-Monotherapy-in-PD-L-S4V73.pdf](https://s206.q4cdn.com/652410165/files/doc_news/Ivonescimab-Monotherapy-Demonstrates-Statistically-Significant-Overall-Survival-Benefit-Compared-to-Pembrolizumab-Monotherapy-in-PD-L-S4V73.pdf)
<span id="ref-13"></span>13. Summit Therapeutics Inc. HARMONi-2 presentation at the WCLC 2024 Presidential Symposium [Conference slides; exhibit to Form 8-K; title assigned by the editor] [Internet]. U.S. Securities and Exchange Commission; 2024 Sep [cited 2026 Nov 5]. Available from: [https://www.sec.gov/Archives/edgar/data/1599298/000159929824000128/wclc-2024xpresentationxh.htm](https://www.sec.gov/Archives/edgar/data/1599298/000159929824000128/wclc-2024xpresentationxh.htm)
<span id="ref-14"></span>14. Summit Therapeutics Inc. Ivonescimab monotherapy demonstrates a statistically significant & clinically meaningful benefit compared to pembrolizumab monotherapy in PD-L1-positive advanced NSCLC in Akeso's HARMONi-2 study conducted in China [Press release] [Internet]. Summit Therapeutics; 2026 Sep 13 [cited 2026 Nov 5]. Available from: [https://s206.q4cdn.com/652410165/files/doc_news/Ivonescimab-Monotherapy-Demonstrates-a-Statistically-Significant--Clinically-Meaningful-Benefit-Compared-to-Pembrolizumab-Monotherapy-O38XG.pdf](https://s206.q4cdn.com/652410165/files/doc_news/Ivonescimab-Monotherapy-Demonstrates-a-Statistically-Significant--Clinically-Meaningful-Benefit-Compared-to-Pembrolizumab-Monotherapy-O38XG.pdf)
<span id="ref-15"></span>15. The ASCO Post. Ivonescimab significantly improves overall survival vs pembrolizumab in PD-L1-positive advanced NSCLC [News article; title taken from the URL; page content read through a summarising tool] [Internet]. The ASCO Post; 2026 Sep 15 [cited 2026 Nov 5]. Available from: [https://ascopost.com/news/september-2026/ivonescimab-significantly-improves-overall-survival-vs-pembrolizumab-in-pd-l1-positive-advanced-nsclc/](https://ascopost.com/news/september-2026/ivonescimab-significantly-improves-overall-survival-vs-pembrolizumab-in-pd-l1-positive-advanced-nsclc/)
<span id="ref-16"></span>16. ecancer. WCLC 2026: analysis shows ivonescimab significantly improves overall survival versus pembrolizumab in PD-L1-positive advanced NSCLC [News article; title taken from the URL; page content read through a summarising tool] [Internet]. ecancer; [date not recorded] [cited 2026 Nov 5]. Available from: [https://ecancer.org/en/news/28884-wclc-2026-analysis-shows-ivonescimab-significantly-improves-overall-survival-versus-pembrolizumab-in-pd-l1-positive-advanced-nsclc](https://ecancer.org/en/news/28884-wclc-2026-analysis-shows-ivonescimab-significantly-improves-overall-survival-versus-pembrolizumab-in-pd-l1-positive-advanced-nsclc)

## この記事の引用

Kumakura D. How far can public aggregate data support a comparison of ivonescimab dose and dosing interval? [Internet]. DaikiKumakura.github.io; 2026 Dec 12 [Japanese version]. Available from: https://daikikumakura.github.io/writing/ivonescimab-exposure-response-optimization.html (English version: https://daikikumakura.github.io/writing/ivonescimab-exposure-response-optimization-en.html)
