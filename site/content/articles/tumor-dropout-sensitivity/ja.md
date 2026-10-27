## 要旨 {#article-abstract}

公開された大腸がん試験の部分集団には、腫瘍計測が終了した理由が記録されていない。最後の計測から短期間で死亡した患者ほど腫瘍が増大する傾向があった。48週の観測平均は、混合効果モデルや死亡とのjoint modelによる推定より大きい縮小を示した。死亡を現在の腫瘍量へ結び付けたときの変化は、観測平均と混合モデルの差より小さかった。24週の群間差は検討したすべての感度条件で支持されたが、48週の差は片群だけに置いた小さなdelta調整で支持を失った。Joint modelは事前に定めた合成データ検査の2基準を満たさず、主な根拠ではなく感度シナリオとして残した。これらは脱落仮定への依存を示す結果であり、真の欠測機構を特定するものではない。

## 背景と目的 {#article-introduction}

固定した週での平均腫瘍変化など、腫瘍増殖抑制（TGI）の要約は、なお計測を受けている患者から求められる。進行がんでは病勢進行、全身状態悪化、死亡などで計測が終わるため、残った患者は無作為な標本とは限らない。**推定する縮小量と治療群間差は、計測されなくなった患者についての仮定にどれだけ依存するか。** これを問う。

利用範囲は、そのTGI要約を額面どおりに読めるか、どの時点・条件で結論が不安定になるかを検討する研究とする。混合効果モデルがここで推定するのは、全員が生存し計測された場合の平均軌跡という、ICH E9(R1)の意味での仮想的な量である ([1](#ref-1))。死亡後の腫瘍サイズは存在しないため、観測されない値の仮定に依存する。どの推定対象が適切かを決める解析ではなく、その依存の強さを調べる。

## 方法 {#article-methods}

### データと確認できる範囲 {#data-scope}

CRANのfrailtypack 3.8.1に含まれる`colorectal`と`colorectalLongi`は、FFCD 2000–05の410人から無作為に選ばれた150人のデータである ([2](#ref-2))。原試験は、逐次化学療法（フルオロウラシル、FOLFOX6、FOLFIRIの順）と、初めからの併用（FOLFOX6、FOLFIRIの順）を比べた無作為化試験だった ([3](#ref-3))。腫瘍の値は病変径和をBox–Cox変換した尺度（λ=0.3）で、負の変化はその尺度での縮小を表す。1人に死亡後の計測があり除外したため、モデル解析は149人、900計測、死亡120人となる。同じ部分集団で、早期腫瘍変化と生存予測、ランドマークでの動的腫瘍モデルを既に検討している ([4](#ref-4), [5](#ref-5))。

**脱落理由の記録はない。** データにあるのは死亡または打切り時刻と新病変の時刻であり、計測終了の理由ではない。初期の集計は前述の除外前の150人を用いた。「その週にも計測が続く人数」は直前4週間に1回以上の計測がある人で、表1の観測平均の標本数とは異なる。集計は次の特徴を示した。

- 最後の計測から死亡までの中央値は12週だった。
- 最後の計測から6か月以内に死亡した人は、最後の区間の腫瘍変化の中央値が変換後尺度で年+1.1であり、それ以外の人は変化ゼロだった。分布は大きく重なる。
- 逐次群の方が早く計測から外れ、24週の直前4週に計測があったのは77人中57人、併用群は73人中65人だった。
- 新病変の後も60人で計測が続き、軌跡は一次治療だけでなく治療戦略全体を含む。

理由が欠けているため、脱落機構は推定できない。モデル推定前に固定した計画では、現在の腫瘍量と死亡リスクを結ぶjoint modelと、delta調整の2つに感度解析を限定した。

### 腫瘍軌跡のモデル {#trajectory-models}

1. **計測が続いた患者の平均。** 脱落を扱わない記述統計である。
2. **MAR混合効果モデル。** 24週で傾きが変わる区分線形時間経過、群別の傾き、相関したランダム切片・傾きを持つ線形混合モデルを`nlme`の最尤法で推定した。脱落が観測された情報だけに依存するmissing at random（MAR）を仮定する。区間は患者単位で1,000回再標本化し、モデルを再推定して求めた ([6](#ref-6))。
3. **Joint model。** 同じ縦断モデルと、治療群、WHO全身状態、切除歴、年齢群を含む死亡のCoxモデルを連結し、ハザードを現在の腫瘍値へ依存させた。`JMbayes2`の3チェーン・12,000反復で、すべてのR̂<1.05だった。現在の傾きも加える別モデルは、収束に24,000反復を要した ([7](#ref-7))。

## 結果 {#article-results}

### 推定された腫瘍軌跡 {#estimated-trajectories}

図1と表1に、観測平均と2つのモデルの推定を示す。表のsequentialは逐次群、combinationは併用群、differenceは併用群から逐次群を引いた差である。数値は変換後の腫瘍尺度を用いる。

![ベースラインからの平均変化と計測が続いた人数](shared/tumor-dropout-sensitivity/figures/01-trajectories.png)

**図1　平均腫瘍変化と計測人数。** モデル軌跡はそれぞれの欠測仮定に依存する。表1の観測平均を求めた人数と、直前4週間の計測有無による集計人数は異なる。

**表1　異なる軌跡モデルによるベースラインからの変化**

| Change from baseline | Still measured (n) | MAR mixed model | Joint model |
| --- | --- | --- | --- |
| 24 weeks, sequential | −0.52 (46) | −0.60 (−0.83, −0.34) | −0.61 (−0.96, −0.26) |
| 24 weeks, combination | −1.34 (48) | −1.39 (−1.87, −1.02) | −1.39 (−1.73, −1.06) |
| 24 weeks, difference | | −0.79 (−1.31, −0.35) | −0.78 (−1.25, −0.32) |
| 48 weeks, sequential | −0.69 (29) | −0.62 (−1.09, −0.36) | −0.50 (−0.88, −0.13) |
| 48 weeks, combination | −1.80 (28) | −1.37 (−1.80, −0.95) | −1.22 (−1.59, −0.83) |
| 48 weeks, difference | | −0.75 (−1.27, −0.04) | −0.72 (−1.24, −0.19) |

Joint modelでは、変換後腫瘍値が1増えると死亡ハザードは1.37倍となった。対数ハザード係数は0.31、95%信用区間0.18–0.46だった。傾きを加えても結果は変わらず、傾きの関連は−0.01、区間−0.23–0.22だった。

観測平均が混合モデルより大きな縮小を示した差は、48週の併用群で−1.80対−1.37だった。混合モデルは、仮定のもとで各脱落者の軌跡を外挿することで、その差の多くを減らした。Joint modelは48週の推定をさらに逐次群で0.12、併用群で0.15、縮小が小さくなる方向へ動かした。死亡の多くは後に生じたため、24週はほぼ変わらなかった。事前計画では、joint modelによる変化が混合モデルの区間幅の半分を超えた場合だけ実質的な変化としたが、どちらの時点でも超えなかった。

### Delta調整による感度解析 {#delta-sensitivity}

Joint modelは腫瘍軌跡と死亡の特定の関係を仮定する。Delta調整では、最後の計測後の未観測軌跡が混合モデルの予測より年δだけ悪いとしたら推定がどう変わるかを調べる。δは死亡前の最終区間傾きを挟むよう、年0、0.5、1、2、3に事前固定した。図2に48週の縮小と群間差を示す。

![48週のdelta調整後の縮小と群間差の転換点](shared/tumor-dropout-sensitivity/figures/02-delta-sensitivity.png)

**図2　Delta感度解析。** δは変換後尺度で、混合モデル予測を超える年間悪化量として仮定した値である。

- **各群の縮小。** 両群に同じδを置くと、逐次群の48週の縮小はδ=2で支持を失った（−0.04、区間−0.54–+0.30）。併用群はδ=3でも縮小を保った（−0.65、−1.14–−0.18）。Joint modelの変化はδ約0.5–1に対応する。
- **24週の群間差。** 併用群だけにδ=3を適用する条件でも差は保たれた（−0.64、−1.18–−0.20）。
- **48週の群間差。** 併用群だけにδ=0.5を置くと支持を失い（−0.63、−1.15–+0.08）、δ=3では点推定がゼロに近づいた。両群または逐次群にδを置く場合は、逐次群の計測終了が早いため、逆に群間差が広がった。

データの選び方を変えた2条件も確認した。最初の新病変後の計測を除き、脱落を病勢進行へ近づける一般的な扱いにすると、48週の混合モデルの群間差の区間はゼロを含んだ（−0.62、−1.32–+0.43）。変換の下限にある34計測を除くと両群の縮小は小さくなったが、結論は変わらなかった。

### 合成データでの検査 {#synthetic-checks}

Joint modelへ依存する前に、真値が既知の合成データで確認した。1条件につき150人の試験を30回生成し、推定したjoint modelに基づく腫瘍軌跡と死亡時刻、実データと同じ81%死亡割合を使った。腫瘍量と死亡の関連はゼロ（MARが正しい条件）、推定値、推定値の2倍とした。事前計画は、関連がある条件でjoint modelが混合モデルを上回り、MARが正しい条件では両者がほぼ不偏（|bias|<0.1）であることを要求した。短いチェーンの初回計算では収束が少なすぎたため延長し、joint modelが収束した反復（R̂<1.1、各条件30回中20–23回）だけを集計した。混合モデルも同じ反復で比較した。図3に48週の偏りを示す。

![合成試験における48週の偏り](shared/tumor-dropout-sensitivity/figures/03-simulation.png)

**図3　合成試験の48週の偏り。** 収束したjoint modelの反復だけを要約し、両モデルを同じ反復上で比較した。

- **群ごとの縮小。** 死亡が腫瘍量に依存すると、混合モデルは48週の縮小を推定値の関連条件で0.25–0.30、関連2倍で約0.5過大に示した。関連を正しく指定したjoint modelは偏りを除いたが、真の関連が当てはめで仮定した関連の2倍の場合は0.2–0.3過補正した。
- **群間差。** 関連のあるどの条件も両モデルの偏りは小さく（|bias|≤0.09）、joint modelは混合モデルを上回らなかった。共通の脱落機構が両群平均を動かすため、差では大きく相殺された。
- **MARが正しい条件。** 48週の併用群と群間差では両モデルとも−0.13–−0.16の偏りがあり、Monte Carlo標準誤差の約2倍だった。30反復では小標本の影響と偶然を区別できない。

Joint modelは事前基準の2つを満たさなかったため、計画どおり主な根拠に用いず、可能な1シナリオとして残した。この検査は実データの傾向を理解する材料にもなる。共通機構は主に各群の縮小を動かし、群固有の機構が群間差を動かす。片群へのdelta調整は後者を調べている。

## 考察 {#article-discussion}

この部分集団では、計測が続く患者の平均を、最初の数か月以降の治療による縮小として読むことはできない。48週の併用群では混合モデルと比べて約3分の1大きな縮小を示した。24週の縮小と群間差は検討したすべての脱落仮定に対して安定し、48週の併用群の縮小自体も大きい悪化仮定まで保たれた。

一方、48週の群間差は不安定だった。併用群の計測終了者がモデル予測より年約0.5悪化すれば支持が失われる。この大きさは死亡前の観測範囲内である。原試験全体の治療関連死亡6例はすべて併用群にあり、計測終了の理由が群間で異なる可能性は軽視できない ([3](#ref-3))。

脱落を無視できることや、joint modelの変化が小さいから脱落の影響も小さいことは示されていない。Joint modelは群間差についての合成データ検査を通過していない。理由が記録されない以上、脱落機構は同定されず、joint modelとdelta調整は異なる仮定として残る。また、機序的TGIモデル、治療ベネフィット、物理的な腫瘍サイズ、他試験の評価も行っていない。原試験の主要評価項目は無増悪生存期間で、群間差を示さなかった ([3](#ref-3))。

計測終了理由がないため、毒性と病勢進行による脱落が単一のδへ混ざる。原尺度の腫瘍サイズと、正式な病勢進行に対応付けて確認した評価履歴も得られない。新病変時点とその後の計測だけでは、計測終了理由は分からず、毒性と進行の機構を分離できない。

## 結論 {#article-conclusion}

24週の群間差は検討した脱落仮定に対して安定していたが、48週の差は最後の計測後の群固有の悪化仮定に依存した。計測終了理由がなく、joint modelも事前基準を満たさないため、joint modelによる小さな変化や観測データへの適合から、脱落を無視できるとは判断できない。

## データとコードの公開状況 {#availability}

付属資料は取得・書出しスクリプト、解析・シミュレーション・検証コード、集約結果表、図コードを含む。参加者単位データは配布しない。`acquire.py`はCRANから出典パッケージを取得してSHA-256を確認し、`export.R`が2データセットを手元で書き出す。

実行順は`python acquire.py`、`Rscript export.R`、`python audit.py`、`Rscript analyze.R`、`Rscript simulate.R 1`（続けて2、3）、`Rscript simulate.R combine`、`Rscript validate.R`、`python figures.py`である。環境はR 4.5.3、nlme 3.1-168、survival 3.8-6、JMbayes2 0.6.0、lme4 2.0-1と、Python 3.12・matplotlibを使った。

混合モデルは独立実装のlme4と照合し、固定効果差は4 × 10⁻⁶以内だった。Joint modelは別のMCMC seedと照合し、事後平均差は0.005以内だった。R 4.5.1・survival 3.8-3と、R 4.5.3・survival 3.8-6で解析出力はバイト単位で一致した。

[コード・集約結果・図スクリプトのダウンロード](shared/tumor-dropout-sensitivity/tumor-dropout-sensitivity-companion.zip)

## 参照 {#article-references}

1. <span id="ref-1"></span>International Council for Harmonisation. Addendum on estimands and sensitivity analysis in clinical trials to the guideline on statistical principles for clinical trials: E9(R1) [Guideline]. 2019 Nov 20. [Final guideline](https://database.ich.org/sites/default/files/E9-R1_Step4_Guideline_2019_1203.pdf).
2. <span id="ref-2"></span>Rondeau V, Gonzalez JR, Mazroui Y, Mauguen A, Diakite A, Laurent A, et al. frailtypack: Shared, Joint (Generalized) Frailty Models; Surrogate Endpoints [Software and datasets]. Version 3.8.1. Datasets colorectal and colorectalLongi. [CRAN record](https://cran.r-project.org/package=frailtypack).
3. <span id="ref-3"></span>Ducreux M, Malka D, Mendiboure J, Etienne PL, Texereau P, Auby D, et al. Sequential versus combination chemotherapy for the treatment of advanced colorectal cancer (FFCD 2000–05): an open-label, randomised, phase 3 trial. Lancet Oncol. 2011;12(11):1032–1044. [doi:10.1016/S1470-2045(11)70199-1](https://doi.org/10.1016/S1470-2045%2811%2970199-1).
4. <span id="ref-4"></span>Kumakura D. Do early tumor measurements improve prediction of subsequent survival? [Internet; technical note]. 2026 Oct 4. [Earlier analysis](https://daikikumakura.github.io/writing/tumor-dynamics-survival.html).
5. <span id="ref-5"></span>Kumakura D. Does a tumor-kinetic model add anything to a single early tumor change? [Internet; technical note]. 2026 Oct 9. [Earlier analysis](https://daikikumakura.github.io/writing/tumor-kinetics-landmark.html).
6. <span id="ref-6"></span>Pinheiro J, Bates D, R Core Team. nlme: Linear and Nonlinear Mixed Effects Models [Software]. Version 3.1-168. [CRAN record](https://cran.r-project.org/package=nlme).
7. <span id="ref-7"></span>Rizopoulos D, Papageorgiou G, Miranda Afonso P. JMbayes2: Extended Joint Models for Longitudinal and Time-to-Event Data [Software]. Version 0.6.0. [CRAN record](https://cran.r-project.org/package=JMbayes2).
