基準日：本記事の事実関係は2026年11月5日時点の公開情報による。

English version: [Is there a body-weight threshold for flat dosing?](https://daikikumakura.github.io/writing/flat-dose-weight-threshold-en.html)

## 要旨

固定用量（体重によらず全員に同じ量を投与する方式）で曝露が基準から外れる体重を、母集団薬物動態（PK）モデルが報告したクリアランス（CL）の体重指数 \(b\) から計算した。体重の閾値は臨床上の境界ではなく、基準体重の患者の曝露に対する比が \(1\pm\delta\)（\(\delta\) は許容する相対差で、0.1・0.2・0.3を計算した）になる体重と定義した。原資料の本文または表で指数と基準体重を確認できた9種類の抗体（pembrolizumab・nivolumab・atezolizumab・durvalumab・avelumab・tislelizumab・cemiplimab・dostarlimab・ipilimumab）を対象にした。\(b\) は0.324–0.694だった。

曝露が基準の ±20%（比0.8–1.2）に収まる体重帯は、固定用量で下限側が40–62 kg、上限側が96–141 kgだった。mg/kg用量では下限側が39–51 kg、上限側が93–145 kgだった。±20% の限界はすべて、体重範囲を取得できた7種類の原資料の最小値と最大値の内側にあったが、3種類は体重範囲を取得できず、データの密度は確認できていない。曝露（AUCまたは平均濃度）の対数の分散は、体重だけに由来する分では、固定用量で \(b^2\sigma^2\)、mg/kg用量で \((1-b)^2\sigma^2\) となり、\(b=0.5\) で等しい。点推定が0.5を下回ったのは4種類で、標準誤差だけに基づく \(b<0.5\) の確率は、avelumab 1.00、durvalumab 0.99、dostarlimab 0.85、cemiplimab 0.66だった。閾値の95%区間は \(b\) の標準誤差だけで、固定用量の上限側で幅が最大のavelumabが126–168 kg、最小のipilimumabが107–114 kgだった。トラフ（投与直前濃度）は、1コンパートメントの近似では、9種類すべてで上限側の限界がAUC基準より2–13 kg（原資料の投与間隔）軽い体重に移った。結果は、べき乗モデル、報告された指数、想定した体重分布に条件付きであり、曝露の差は効果の差を意味しない。

## 背景と目的

抗体医薬の用量を体重に比例させる（mg/kg）か、全員に同じ量にする（フラット）かは、母集団PKモデルのCLの体重指数で説明されることが多い。tislelizumabの母集団PK解析は、指数が0.5未満または約0.5であれば、固定用量とmg/kg用量の曝露が同程度になると述べ、dostarlimabの解析は、指数が0.5未満であれば固定用量でAUCのばらつきが小さくなると述べている ([1](#ref-1), [2](#ref-2))。一方、「体重が何kgを超えると固定用量は不利になるか」という問いには、指数とは別に、閾値の定義が必要になる。

本サイトには、pembrolizumabとnivolumabの公表モデルを一般成人の体重分布に当てはめた記事 ([3](#ref-3)) と用語ページ ([4](#ref-4)) がある。そこでは、基準方式のトラフの5パーセンタイルを下限として、下限を下回る患者の割合が10%を超える体重帯を調べた。本記事は同じ公表モデルの考え方を使いながら、次の4点を加える。

1. 指数 \(b\) から閉じた式で体重の閾値を定義し、計算する。
2. 9種類の抗体を、同じ定義で比較する。
3. 指数の標準誤差から閾値の不確実性を求める。
4. 分散が固定用量とmg/kg用量で等しくなる \(b=0.5\) の境界を導き、数値で確かめる。

目的は、上の定義に基づいて、指数と閾値の関係を調べることである。閾値は曝露の差の定義であり、効果や安全性の境界ではない。用量の推奨はしない。

## 仮定と定義

### 記号

体重を \(\mathrm{BW}\)（kg）、基準体重を \(\mathrm{BW}_\mathrm{ref}\)（kg）とし、相対体重を \(x=\mathrm{BW}/\mathrm{BW}_\mathrm{ref}\)（無次元）とする。CLのべき乗モデルは次の式である。

\[ \mathrm{CL}=\mathrm{CL}_\mathrm{ref}\,x^{b} \tag{1} \]

\(\mathrm{CL}_\mathrm{ref}\)（L/日）は基準体重の患者のCL、\(b\)（無次元）はCLの体重指数である。分布容積 \(V\)（L）には \(V=V_\mathrm{ref}\,x^{c}\) を置く（\(V_\mathrm{ref}\) は基準体重の患者の \(V\)、\(c\) は無次元の体重指数）。線形PKでは、定常状態のAUC（濃度時間曲線下面積、1投与間隔）と平均濃度 \(C_\mathrm{avg}\) は、用量をCLで割った値に比例する。曝露比 \(R\)（無次元）を、基準体重の患者がmg/kg用量で受ける曝露に対する比とすると、固定用量とmg/kg用量の曝露比は次の式になる。

\[ R_\mathrm{flat}(x)=s\,x^{-b},\qquad R_\mathrm{mg/kg}(x)=x^{1-b} \tag{2} \]

\(s=D/(d\,\mathrm{BW}_\mathrm{ref})\)（無次元）は、固定用量 \(D\)（mg）を、mg/kg用量 \(d\)（mg/kg）と基準体重の積で割った値である。\(s=1\) は、固定用量が基準体重の患者のmg/kg用量に等しいことを意味する。本文の主な結果は \(s=1\) で示す。この場合、\(R_\mathrm{flat}\) は、基準体重の患者自身が同じ固定用量で受ける曝露に対する比であり、結果は「基準体重の患者のまわりでの曝露のばらつき」を表す。mg/kg用量で定義した曝露からの隔たりではない。実際の承認用量では \(s\) が1から離れることがあり、その場合の結果は別に示す（表6）。

![相対体重に対する相対クリアランスと、固定用量とmg/kg用量の曝露比を示す2枚組の図。右は0.8から1.2の帯と、固定用量の帯の両端を示す。](shared/flat-dose-weight-threshold/figures/fig1_power_model_schematic.png)

図1．べき乗モデルの模式図。(a) \(b\) の違いによる相対CL（CL：クリアランス）。(b) \(b=0.6\)（例示）での固定用量（実線）とmg/kg用量（破線）の曝露比。灰色は曝露比0.8–1.2の帯、点線は固定用量の帯の両端を示す。

### 体重の閾値の定義

閾値は、曝露比が \(r=1\pm\delta\) になる相対体重である。\(r\)（無次元）は曝露比の目標値、\(\delta\)（無次元）は許容する曝露の相対差で、0.1・0.2・0.3を計算した。式 (2) を \(x\) について解くと次の式になる。

\[ x_\mathrm{flat}(r)=(s/r)^{1/b},\qquad x_\mathrm{mg/kg}(r)=r^{1/(1-b)} \tag{3} \]

曝露が \(1\pm\delta\) に収まる体重帯は、固定用量で \(r=1+\delta\) と \(r=1-\delta\) に対応する2つの体重の間、mg/kg用量も同様である。帯は曝露比の線形の幅 \(1\pm\delta\) で定義した。対数で対称な帯 \(\exp(\pm\delta)\) では限界が少し変わる（結果で示す）。\(s=1\) のとき、帯の上限と下限の比は、固定用量で \(((1+\delta)/(1-\delta))^{1/b}\)、mg/kg用量で \(((1+\delta)/(1-\delta))^{1/(1-b)}\) になる。固定用量の帯が広いのは \(1/b>1/(1-b)\)、つまり \(b<0.5\) のときである。

2つの方式で曝露が等しくなる体重（等曝露体重）は、式 (2) から \(R_\mathrm{flat}/R_\mathrm{mg/kg}=s/x\) となり、\(x=s\) のとき（\(s=1\) なら基準体重）で、\(b\) に依らない。

### 分散の交差

体重が対数正規分布 \(\ln\mathrm{BW}\sim N(\mu,\sigma^2)\)（\(\mu\) は \(\ln\mathrm{BW}\) の平均、\(\sigma\) は標準偏差で、ともに無次元）に従うとき、体重だけに由来する対数曝露の分散は次の式である。

\[ \mathrm{Var}[\ln R_\mathrm{flat}]=b^{2}\sigma^{2},\qquad \mathrm{Var}[\ln R_\mathrm{mg/kg}]=(1-b)^{2}\sigma^{2} \tag{4} \]

\(b^2=(1-b)^2\) は \(b=0.5\) で成り立ち、\(b<0.5\) で固定用量の分散が小さい。この関係は、用量をCLで割った曝露（AUCと平均濃度）の対数の分散に当てはまり、トラフには当てはまらない。曝露の変動係数（CV）は \(\sqrt{\exp(\mathrm{Var})-1}\) である。

### 指数の不確実性と解釈上の条件

\(b\) の標準誤差を \(\mathrm{SE}(b)\) とすると、閾値の対数のデルタ法の標準誤差は、固定用量で式 (5)、mg/kg用量で式 (6) になる。

\[ \mathrm{SE}(\ln x_\mathrm{flat})=\frac{|\ln(s/r)|}{b^{2}}\,\mathrm{SE}(b) \tag{5} \]

\[ \mathrm{SE}(\ln x_\mathrm{mg/kg})=\frac{|\ln r|}{(1-b)^{2}}\,\mathrm{SE}(b) \tag{6} \]

各モデルの \(b\) は、そのモデルに含まれる他の共変量（性別・アルブミン・腫瘍量など）で調整した条件付きの効果であり、体重の周辺的な効果ではない。

### トラフ（近似）

トラフ \(C_\mathrm{trough}\) は \(\mathrm{CL}\) と \(V\)、および投与間隔 \(\tau\)（日）に依存する。繰り返し静脈内（IV）ボーラス投与の1コンパートメントモデルの定常状態では、次の式になる。

\[ C_\mathrm{trough}=\frac{D}{V}\,\frac{e^{-k\tau}}{1-e^{-k\tau}},\qquad k=\frac{\mathrm{CL}}{V} \tag{7} \]

これは近似である。実際の抗体は2コンパートメント以上で、点滴で投与される。本記事は、\(V\) を中心コンパートメントの容積 \(V_\mathrm{c}\) と末梢コンパートメントの容積 \(V_\mathrm{p}\)（ともにL）の和、すなわち \(V_\mathrm{ss}=V_\mathrm{c}x^{c_\mathrm{c}}+V_\mathrm{p}x^{c_\mathrm{p}}\) とした（\(c_\mathrm{c}\)・\(c_\mathrm{p}\) はそれぞれ \(V_\mathrm{c}\)・\(V_\mathrm{p}\) の体重指数）。2コンパートメント以上のモデルでの感度解析は結果に示す。

## 方法

### 入力データ

原資料の本文または表で、CLの体重指数、基準体重、べき乗の形を確認できた抗体だけを使った。pembrolizumab ([5](#ref-5), [Ahamadiらの原著Table 3](https://doi.org/10.1002/psp4.12139))、nivolumab ([6](#ref-6), [Bajajらの原著Table 1](https://doi.org/10.1002/psp4.12143))、atezolizumab（米国食品医薬品局（FDA）の臨床薬理審査 ([7](#ref-7), [審査資料のTable 8](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/761041Orig1s000ClinPharmR.pdf))）、durvalumab ([8](#ref-8), [Baverelらの原著Table 2](https://doi.org/10.1002/cpt.982))、avelumab ([9](#ref-9), [Wilkinsらの原著Table 2](https://doi.org/10.1002/psp4.12406))、tislelizumab ([1](#ref-1), [Budhaらの原著Table 3](https://doi.org/10.1002/psp4.12880)と[原著のEquation 5・6](https://doi.org/10.1002/psp4.12880))、cemiplimab ([10](#ref-10), [Yangらの原著Table 3](https://doi.org/10.1007/s10928-021-09739-y))、dostarlimab ([2](#ref-2), [Melhemらの原著Table 3](https://doi.org/10.1111/bcp.15339))、ipilimumab ([11](#ref-11), [Sanghaviらの原著Table 2](https://doi.org/10.1002/psp4.12477)) である。ipilimumabは、より古い時間不変モデル ([12](#ref-12), [Fengらの原著Table 2](https://doi.org/10.1111/bcp.12323)) の指数0.642（95%区間0.423–0.819）も感度解析に使った。pembrolizumabは、原著の表脚注の式に別の指数0.578があり ([5](#ref-5))、表の0.595を主解析、0.578を感度解析にした。

表1に、解析に使った指数を示す。標準誤差は、報告された相対標準誤差（RSE）に推定値を掛けて求めた。RSEがなく区間だけの場合は、区間の幅を \(2\times1.96\) で割った。これは対称な正規近似である。atezolizumabのRSEは審査資料で整数に丸められた5%である。基準体重は、原資料の式、表の脚注、または共変量の効果の基準患者に書かれた値である。avelumabは中央値を基準とする式（[Wilkinsらの原著のEquation 3](https://doi.org/10.1002/psp4.12406)）で、[Wilkinsらの原著のTable 1](https://doi.org/10.1002/psp4.12406)の全体の中央値71 kgを使った（中心化の定数の記載はない）。tislelizumabは原著のEquation 5・6が本文にあり、基準体重65 kgのべき乗である。dostarlimabは本文に式そのものがなく、基準患者の体重（70 kg）と「アロメトリー」という記述から、べき乗の形と判断した。この点は図2で「部分的」とした。cemiplimabのCLの体重指数は、CLとコンパートメント間クリアランスに共通で、\(V_\mathrm{c}\)・\(V_\mathrm{p}\) には体重と体格指数（BMI）が入る（式は \(V\propto \mathrm{WGT}^{0.970}\,\mathrm{BMI}^{-0.560}\)）。

表1．解析に使ったCLの体重指数と原資料の集団の体重範囲。SE：標準誤差。CI：95%区間（ブートストラップまたは原資料の報告）。BWref：基準体重。「not reported」は区間がなくRSEだけが報告されていることを示す。体重範囲は原資料が報告した最小値と最大値で、5パーセンタイルと95パーセンタイルはすべてNOT AVAILABLE（原資料の本文に記載なし）だった。

| Drug | b | SE (derived) | 95% CI (reported) | BWref (kg) | Source weight min–max (kg) |
| --- | --- | --- | --- | --- | --- |
| pembrolizumab | 0.595 | 0.047 | 0.506–0.686 | 76.8 | NOT AVAILABLE |
| nivolumab | 0.566 | 0.046 | 0.479–0.658 | 80 | NOT AVAILABLE |
| atezolizumab | 0.666 | 0.033 | not reported | 77 | NOT AVAILABLE |
| durvalumab | 0.389 | 0.045 | 0.299–0.477 | 69.8 | 34.0–149.1 |
| avelumab | 0.324 | 0.033 | 0.260–0.388 | 71 | 30.4–204 |
| tislelizumab | 0.565 | 0.034 | 0.491–0.631 | 65 | 31.9–130 |
| cemiplimab | 0.477 | 0.058 | not reported | 76.2 | 30.9–172 |
| dostarlimab | 0.470 | 0.029 | 0.414–0.527 | 70 | 34.0–182.0 |
| ipilimumab | 0.694 | 0.032 | 0.630–0.750 | 80 | 36.8–181 |

出所：`inputs/parameter_table.csv`、`inputs/source_weight_ranges.csv`、および各原資料の表（上記）。nivolumabは平均79.1 kg（SD 19.3）だけが報告されている。

確認できなかった抗体は、camrelizumab・adebrelimab・panitumumab・cetuximab・trastuzumab・bevacizumab・rituximabである。camrelizumabの母集団PKの要旨は、体重が影響したのは線形CLではなくコンパートメント間クリアランスだったと述べている ([13](#ref-13))。panitumumabの母集団PKの要旨は、体重がCL・最大非線形消失速度・中心容積に影響したと述べるが、指数は確認できなかった ([14](#ref-14), [15](#ref-15))。trastuzumabの母集団PKの表には、線形CLへの体重の影響0.967（RSE 7.19%）があるが、共変量の式と基準体重が本文になく、本文が述べる46 kgで27%低下・98 kgで43%上昇（66 kgを基準）は、べき乗なら指数0.87と0.90に相当する。報告値0.967をべき乗に当てはめると約29%低下・46%上昇になり、数値は近いが一致せず、形を確認できなかった ([16](#ref-16))。bevacizumabは小児の解析だけで ([17](#ref-17))、rituximabの解析は体表面積を共変量にしていた ([18](#ref-18))。adebrelimabとcetuximabは、確認できる一次資料を見つけられなかった。各抗体の状態と理由は `inputs/not_verified.csv` に記録した。図2は、使った抗体と使えなかった抗体の確認状況を示す。

![データの確認状況の表。使った9種類は指数・不確実性・基準体重・式・分布容積の指数がそろい、dostarlimabだけ式が部分的である。使わなかった7種類は一部または全部がない。](shared/flat-dose-weight-threshold/figures/fig2_data_provenance_matrix.png)

図2．データの確認状況。CL：クリアランス。V：分布容積。Yes：確認できた。Partial：式の記載が本文に明示されていない。RSE：相対標準誤差だけで区間がない。CI：区間あり。No：確認できなかった、または使わなかった。

### 計算

すべての閾値は式 (3) で閉じた形で計算した。不確実性は3通りで求めた。デルタ法（式 (5)・(6)）、\(b\sim N(b,\mathrm{SE}^2)\) からの200,000回の乱数による2.5–97.5パーセンタイル、原資料の区間の両端を式 (3) へ代入した値（区間がある7種類）である。乱数のシードは20261105とした。

体重の分布は、対数正規分布の4つの仮定のシナリオ（S1：中央値75 kg・CV 20%、S2：70 kg・25%、S3：80 kg・30%、S4：65 kg・25%）で置いた。これらは仮定であり、特定の集団の実測ではない。シナリオごとに、曝露比が0.8–1.2の外に出る患者の割合を、正規分布の累積分布関数で厳密に求め、400,000回の乱数でも確かめた。中央値のずれと広がりの効果を分けるため、中央値を基準体重に合わせてCVだけを変えた計算（20・25・30%）と、CV 25%で中央値だけを変えた計算（65・70・75・80 kg）も行った。分散の確認はS1（\(\sigma=0.198\)）で行った。体重だけの分散に、CLの個体間変動を表す対数標準偏差（SD）0.30（仮定）を加えた総SDも比較した。

閉じた式は、1コンパートメントの繰り返しボーラス投与の微分方程式（LSODA、相対許容誤差 \(10^{-11}\)）を解いた結果と照合した。9種類・5つの相対体重・2つの投与方式で、トラフとAUCを比べた。この照合は実装の確認であり、1コンパートメント・ボーラスという近似が実際の抗体に妥当かどうかは確認しない。トラフの近似は、報告された典型値のCL・\(V_\mathrm{c}\)・\(V_\mathrm{p}\) と体重指数を使い、共通の21日と14日、および各原資料が検討した投与方式の間隔で求めた（pembrolizumab・atezolizumab・tislelizumab・cemiplimab・dostarlimab・ipilimumabは21日（Q3W、3週に1回）、nivolumab・durvalumab・avelumabは14日（Q2W、2週に1回））。cemiplimabの \(V\) には、BMIが身長一定のとき体重に比例するとして、体重指数に \(-0.560\) を加えた正味の指数0.41を使い、体重だけの指数0.970の結果は感度解析とした。2コンパートメント（tislelizumabは3コンパートメント）のボーラスモデルでの上限側の限界は、報告されたコンパートメント間クリアランスを使い、体重に対して一定とした場合と \(x^{b}\) で変化するとした場合で、行列指数関数により求めた。

### 検証

テスト15件を実行した（閉じた式と微分方程式の一致、多コンパートメントの行列解と微分方程式の一致、固定用量とmg/kg用量の比 \(1/x\)、\(b=0.5\) での分散の一致、単調性、デルタ法と乱数の一致、厳密な割合と乱数の一致、シードによる再現性、入力表の完全性など）。解析全体と図を2回実行し、結果ファイルのハッシュが一致することを確かめた。

## 結果

### 指数の範囲

9種類の指数は0.324（avelumab）から0.694（ipilimumab）で、4種類が0.5未満、5種類が0.5以上だった。

### 閾値の体重

図3は、式 (2) による曝露比の曲線を抗体ごとに示す。表2に、\(\delta=0.1,0.2,0.3\) の固定用量の体重帯と、\(\delta=0.2\) のmg/kg用量の体重帯を示す。\(s=1\) では、固定用量とmg/kg用量の曝露は基準体重で等しい。

![3×3の小さな図で、各抗体の固定用量とmg/kg用量の曝露比を体重40から160 kgで示す。灰色の帯が0.8から1.2。](shared/flat-dose-weight-threshold/figures/fig3_relative_exposure_by_drug.png)

図3．抗体ごとの相対曝露。実線が固定用量、破線がmg/kg用量、灰色の帯が曝露比0.8–1.2、点線が基準体重。縦軸は対数目盛。b：CLの体重指数、BWref：基準体重。

表2．曝露が基準から \(\pm\delta\) 以内に収まる体重帯（kg、\(s=1\)）。

| Drug | Flat, ±10% | Flat, ±20% | Flat, ±30% | mg/kg, ±20% |
| --- | --- | --- | --- | --- |
| pembrolizumab | 65–92 | 57–112 | 49–140 | 44–120 |
| nivolumab | 68–96 | 58–119 | 50–150 | 48–122 |
| atezolizumab | 67–90 | 59–108 | 52–132 | 39–133 |
| durvalumab | 55–92 | 44–124 | 36–175 | 48–94 |
| avelumab | 53–98 | 40–141 | 32–213 | 51–93 |
| tislelizumab | 55–78 | 47–96 | 41–122 | 39–99 |
| cemiplimab | 62–95 | 52–122 | 44–161 | 50–108 |
| dostarlimab | 57–88 | 47–113 | 40–150 | 46–99 |
| ipilimumab | 70–93 | 62–110 | 55–134 | 39–145 |

出所：`analysis.py`、`results/thresholds.csv`。

\(\pm20\%\) では、固定用量の下限側は40–62 kg、上限側は96–141 kgで、mg/kg用量の下限側は39–51 kg、上限側は93–145 kgだった。上限側の相対体重 \(0.8^{-1/b}\) は \(b\) が小さいほど大きく、avelumab（\(b=0.324\)）で1.99、tislelizumab（0.565）で1.48、ipilimumab（0.694）で1.38だった。kg単位の限界は、これに基準体重を掛けた値で、基準体重が65–80 kgと異なるため、\(b\) の順序と一致しないことがある（tislelizumab 96 kg、ipilimumab 110 kg）。固定用量の帯がmg/kg用量の帯より広いのは、durvalumab・avelumab・cemiplimab・dostarlimabの4種類で、\(b<0.5\) の4種類と一致した。

帯を対数で対称な \(\exp(\pm0.2)\) で定義すると、固定用量の限界は、avelumabで38–132 kg（線形の定義では40–141 kg）、pembrolizumabで55–107 kg（57–112 kg）になった（`results/thresholds_log_symmetric.csv`）。別の指数を使った感度解析では、pembrolizumabの表脚注の指数0.578で固定用量の ±20% 帯が56–113 kg（主解析は57–112 kg）、ipilimumabの古いモデルの指数0.642で60–113 kg（主解析は62–110 kg）となり、主解析との差は3 kg以内だった。

限界体重を、原資料の集団の体重範囲（表1）と比べた。\(\pm20\%\) の24限界（体重範囲を取得できた7種類、2方式、下限側と上限側）はすべて、原資料の最小値と最大値の内側にあった。\(\pm30\%\) では5限界が範囲を外れた（durvalumabの固定用量の上限側175 kgは最大149.1 kg、avelumabの上限側213 kgは最大204 kg、tislelizumabのmg/kg用量の下限側29 kgは最小31.9 kg、ipilimumabのmg/kg用量の下限側25 kgと上限側189 kgは範囲36.8–181 kg）。これらは外挿である。pembrolizumab・nivolumab・atezolizumabは体重範囲が取得できず（NOT AVAILABLE）、12限界の判定はできなかった。範囲の内側でも、原資料の患者数の分布（5パーセンタイルと95パーセンタイルはNOT AVAILABLE）は確認できておらず、端の体重の患者は少ないと考えられる。

### 不確実性

表3に、\(\delta=0.2\) の閾値と、\(b\) の標準誤差だけから求めた乱数による95%区間を示す。図4はこの区間を示す。

表3．±20% の限界体重とその95%区間（kg、\(b\) の不確実性のみ、乱数）。

| Drug | Flat, light side | Flat, heavy side | mg/kg, heavy side |
| --- | --- | --- | --- |
| pembrolizumab | 57 (53–59) | 112 (106–120) | 120 (111–138) |
| nivolumab | 58 (55–61) | 119 (112–128) | 122 (113–136) |
| atezolizumab | 59 (57–60) | 108 (104–112) | 133 (122–152) |
| durvalumab | 44 (38–48) | 124 (111–147) | 94 (91–99) |
| avelumab | 40 (35–44) | 141 (126–168) | 93 (91–96) |
| tislelizumab | 47 (45–49) | 96 (93–102) | 99 (94–107) |
| cemiplimab | 52 (46–56) | 122 (111–141) | 108 (101–119) |
| dostarlimab | 47 (45–50) | 113 (107–120) | 99 (96–103) |
| ipilimumab | 62 (60–63) | 110 (107–114) | 145 (131–169) |

出所：`results/thresholds_uncertainty.csv`。

![各抗体の下限側と上限側の限界体重とその95%区間を、固定用量とmg/kg用量の2枚で示す。](shared/flat-dose-weight-threshold/figures/fig4_threshold_weights_forest.png)

図4．±20% の限界体重（kg）。三角が下限側、四角が上限側の限界（乱数の中央値）、横線が \(b\) の不確実性だけによる95%区間、黒い菱形が基準体重。抗体は \(b\) の昇順（下から上）で、ラベルの b は CL の体重指数。

デルタ法の区間と乱数の区間は近かったが、乱数の区間は上限側へ非対称になった。デルタ法と乱数の区間幅の相対差は最大11%だった。原資料の区間がある7種類では、区間の両端を式 (3) へ代入した値も乱数の区間と近かった（pembrolizumabの固定用量の上限側は106–119 kg）。固定用量の上限側で区間が最も広かったのはavelumab（126–168 kg）、最も狭かったのはipilimumab（107–114 kg）で、下限側で最も狭かったのもipilimumab（60–63 kg）である。

### 分散の交差と \(b=0.5\)

体重の対数SD \(\sigma=0.198\)（S1、中央値75 kg・CV 20%）で、体重だけに由来する対数曝露のSDを式 (4) から求めると、乱数400,000回の値との差は最大0.0003（対数単位）だった。表4に、\(b\)、\(b<0.5\) の確率、曝露のCV、点推定で分散が小さい方式を示す。図5は、\(b\) に対するSDの比と、各抗体の \(b\) の位置を示す。

表4．体重だけに由来するAUC（または平均濃度）のばらつき（\(\sigma=0.198\)）。\(P(b<0.5)\) は、報告された標準誤差だけに基づく正規近似の確率で、モデル構造や試験間の違いによる不確実性は含まない。「Lower variance (point estimate)」は \(b\) の点推定による判定である。

| Drug | b | P(b<0.5) | CV flat (%) | CV mg/kg (%) | Lower variance (point estimate) |
| --- | --- | --- | --- | --- | --- |
| pembrolizumab | 0.595 | 0.022 | 11.8 | 8.0 | mg/kg |
| nivolumab | 0.566 | 0.074 | 11.2 | 8.6 | mg/kg |
| atezolizumab | 0.666 | 0.000 | 13.2 | 6.6 | mg/kg |
| durvalumab | 0.389 | 0.993 | 7.7 | 12.1 | flat |
| avelumab | 0.324 | 1.000 | 6.4 | 13.4 | flat |
| tislelizumab | 0.565 | 0.027 | 11.2 | 8.6 | mg/kg |
| cemiplimab | 0.477 | 0.655 | 9.5 | 10.4 | flat |
| dostarlimab | 0.470 | 0.852 | 9.3 | 10.5 | flat |
| ipilimumab | 0.694 | 0.000 | 13.8 | 6.1 | mg/kg |

出所：`results/variance_crossover.csv`。

![上段はbに対する対数曝露のSDの比で、固定用量とmg/kg用量の2直線がb = 0.5で交差する。下段は各抗体のbと95%区間。](shared/flat-dose-weight-threshold/figures/fig5_variance_crossover.png)

図5．\(b\) と分散の交差。上段：体重の対数SDに対する対数曝露のSDの比（固定用量は \(|b|\)、mg/kg用量は \(|1-b|\)）。下段：各抗体の \(b\)（点）と推定値 ± 1.96 SE（横線）。点線は \(b=0.5\)。

cemiplimabとdostarlimabは、点推定が0.5に近く、\(b<0.5\) の確率が0.66と0.85にとどまる。\(P(b<0.5)\) は報告された標準誤差だけに基づくため、モデル構造の違いは含まない。実際に、同じ抗体のモデル間の指数の差は、pembrolizumabの表と脚注で0.017、ipilimumabの2つのモデルで0.052、durvalumabの時間不変モデルで0.011と、主推定値の標準誤差の0.2–1.7倍あった。CLの個体間変動を表す対数SD 0.30（仮定）を加えた総SDは、固定用量とmg/kg用量で最大0.024しか違わなかった（ipilimumab 0.330と0.306）。体重以外のCLの個体間変動が大きいと、方式の差は小さくなる。

### 体重分布への感度

表の割合は、曝露比が0.8–1.2の外に出る患者の割合である。S1では、固定用量で0.2%（avelumab）から18.4%（ipilimumab）、mg/kg用量で0.1%（ipilimumab）から16.5%（avelumab）だった。図6は、4つのシナリオ（S1–S4）の結果を示す。シナリオ間では、固定用量で0.2–42.7%、mg/kg用量で0.1–36.7%まで動いた。割合の小さい方式が \(b<0.5\) の規則と一致したのは、S2とS4でcemiplimabを除く8種類、S1とS3で9種類全部だった。

![各抗体について、4つの体重分布シナリオで、曝露比が0.8から1.2の外に出る割合を、固定用量とmg/kg用量の2枚で示す。](shared/flat-dose-weight-threshold/figures/fig6_weight_distribution_sensitivity.png)

図6．体重分布のシナリオによる、曝露比0.8–1.2の外に出る割合。S1–S4はシナリオ1–4で、仮定した対数正規分布（中央値と変動係数CV）であり、実測の集団ではない。体重だけに由来する変動で、CLの個体間変動は含まない。b：CLの体重指数。

中央値のずれと広がりの効果は分けて見られる（`results/distribution_shift_spread.csv`）。中央値を基準体重に合わせてCVだけを20%から30%へ増やすと、固定用量で割合が0.2–14.5%から3.7–32.2%へ、mg/kg用量で0.1–13.4%から2.8–31.0%へ増えた。CV 25%で中央値だけを65 kgから80 kgへ動かすと、pembrolizumab（基準体重76.8 kg）の固定用量は29.9%から16.7%へ減り、tislelizumab（基準体重65 kg）の固定用量は14.9%から23.9%へ増えた。割合には、広がりと、中央値と基準体重のずれが、\(b\) と同程度に効いた。

### トラフとの違い

表5に、1コンパートメント近似で、固定用量のトラフが基準から20%低下する上限側の体重を、AUCの限界と並べて示す。投与間隔は、各原資料が検討した投与方式の間隔である。

表5．固定用量の上限側の限界体重（曝露比0.8、kg）。\(c_\mathrm{eff}\)：\(V\) の実効的な体重指数（\(V_\mathrm{ss}(2\,\mathrm{BW}_\mathrm{ref})/V_\mathrm{ss}(\mathrm{BW}_\mathrm{ref})\) の底2の対数）。\(t_{1/2}\)：近似での半減期。Shift：AUCの限界からトラフの限界を引いた値。Shift (2-comp)：2コンパートメント（tislelizumabは3）のボーラスモデルでの同じ差で、コンパートメント間クリアランスが体重に対して一定の場合 / \(x^{b}\) で変化する場合。cemiplimabの \(c_\mathrm{eff}\) はBMIを含めた正味の値。

| Drug | b | c_eff | t1/2 (day) | Interval (day) | AUC limit | Trough limit | Shift | Shift (2-comp) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pembrolizumab | 0.595 | 0.49 | 23.8 | 21 | 112 | 109 | 2.4 | 4.7 / 2.2 |
| nivolumab | 0.566 | 0.37 | 19.7 | 14 | 119 | 114 | 4.3 | 3.9 / 2.2 |
| atezolizumab | 0.666 | 0.27 | 24.2 | 21 | 108 | 101 | 6.3 | 6.6 / 4.3 |
| durvalumab | 0.389 | 0.22 | 20.8 | 14 | 124 | 117 | 7.3 | 6.2 / 1.5 |
| avelumab | 0.324 | 0.29 | 4.1 | 14 | 141 | 128 | 13.1 | 13.6 / 14.3 |
| tislelizumab | 0.565 | 0.20 | 29.1 | 21 | 96 | 91 | 5.9 | 6.4 / 5.3 |
| cemiplimab | 0.477 | 0.41 | 11.9 | 21 | 122 | 116 | 5.3 | 6.4 / 5.0 |
| dostarlimab | 0.470 | 0.42 | 19.7 | 21 | 113 | 110 | 2.3 | 4.5 / 2.2 |
| ipilimumab | 0.694 | 0.36 | 14.6 | 21 | 110 | 102 | 8.0 | 7.7 / 6.3 |

出所：`results/trough_approximation.csv`、`results/trough_two_compartment.csv`。

9種類すべてで \(b>c_\mathrm{eff}\) となり、体重が増えると消失速度定数 \(k=\mathrm{CL}/V\) が大きくなって、トラフはAUCより下がりやすい。上限側のトラフの限界は、AUC基準より2.3–13.1 kg（原資料の投与間隔）軽い体重で現れた。すべての抗体に共通の21日の間隔で計算すると、差は2.3–19.5 kgで、最大はavelumab（\(k\tau=3.6\)）だった。avelumabの原資料の投与方式は14日である。AUC基準の限界体重でのトラフは、基準の0.75–0.79倍だった。2コンパートメントのモデルでは、上限側のトラフの限界が1コンパートメントの値より、約 \(-5\) から \(+6\) kg動き、AUCとの差は1.5–14.3 kgだった。符号と大きさはモデル構造に依存する。

cemiplimabの \(V\) の体重指数は、\(V_\mathrm{ss}\) に対して報告された0.970だけでなく、BMIの指数 \(-0.560\) が加わる ([10](#ref-10))。BMIが身長一定のとき体重に比例すると、正味の指数は0.41になり、上限側のトラフの限界は116 kg（21日）、AUCの限界122 kgより約5 kg軽かった。体重の指数0.970だけを \(V\) に使うと、限界は225 kg（21日）、164 kg（14日）になるが、この値は \(V\) の指数に強く依存し（指数0.82で178 kg、1.12では体重8倍までに到達しない）、\(b\) の標準誤差の範囲でも大きく動く（`results/cemiplimab_trough_sensitivity.csv`）。したがって、本記事はこの値を結果として採用せず、180 kg前後以上という強く不確かな値と位置づける。

微分方程式との照合は、実装の確認であり、トラフとAUCの相対差は最大 \(3.9\times10^{-11}\) だった（9種類・5つの相対体重・2つの投与方式、計90件）。多コンパートメントの行列解も、微分方程式との相対差は最大 \(1\times10^{-11}\) だった。

### 基準体重と投与量の対応づけ

固定用量を基準体重のmg/kg用量に対応づける \(s\) を変えた感度解析（`results/dose_matching_sensitivity.csv`）では、\(s=1.25\) でpembrolizumabの固定用量の ±20% 帯は82–163 kgになり、\(s=0.8\) では39–77 kgになった。承認用量や原資料の検討用量での \(s\) を、投与間隔の違いを含めて計算した結果を表6に示す。

表6．原資料または既存記事に記載された用量での \(s\) と固定用量の曝露帯。\(s=(D/\tau_\mathrm{flat})/(d\,\mathrm{BW}_\mathrm{ref}/\tau_\mathrm{mg/kg})\)（\(\tau\) は投与間隔）。durvalumabの括弧内は、投与間隔の違いを無視した1回あたりの比。

| Drug | Flat dose | mg/kg comparator | s | Flat ±20% band (kg) | Flat +10% heavy limit (kg) |
| --- | --- | --- | --- | --- | --- |
| pembrolizumab | 200 mg Q3W | 2 mg/kg Q3W | 1.30 | 88–174 | 143 |
| nivolumab | 240 mg Q2W | 3 mg/kg Q2W | 1.00 | 58–119 | 96 |
| atezolizumab | 1200 mg Q3W | 15 mg/kg Q3W | 1.04 | 62–114 | 96 |
| durvalumab | 1500 mg Q4W | 10 mg/kg Q2W | 1.07 (2.15) | 53–149 | 110 |
| avelumab | 800 mg Q2W | 10 mg/kg Q2W | 1.13 | 58–204 | 142 |
| tislelizumab | 200 mg Q3W | 3 mg/kg Q3W | 1.03 | 49–101 | 82 |

出所：`results/label_dose_matching.csv`。pembrolizumabとnivolumabの用量は既存記事 ([3](#ref-3)) の対応づけ、他は原資料の用量による。

既存記事は、下限を下回る患者が10%を超える体重帯を約150 kg以上（pembrolizumab）と約100–120 kg以上（nivolumab）と報告している ([3](#ref-3))。本記事の曝露比の定義では、pembrolizumabの200 mgを100 kgに対応づけた \(s=1.30\) の ±10% の上限側が143 kg、\(s=1\) では92 kgで、nivolumabの \(s=1\) では96 kgだった。pembrolizumabがnivolumabより重い側まで許容するという順序は、\(s=1.30\) のときだけに現れ、\(s=1\) では逆になる。つまり、既存記事との順序の一致は \(b\) ではなく用量の対応づけ \(s\) から生じる。定義（曝露比の帯と、基準方式のトラフの5パーセンタイルを下限とした割合）と対象（原資料の集団と一般成人）も異なり、2つの数値は直接比べられない。

## 考察

指数 \(b\) が決める量は、体重帯の幅と分散の大小の2つである。曝露が基準の ±20% に収まる体重の上限と下限の比は、固定用量で \((1.5)^{1/b}\) となり、\(b\) が0.324から0.694に増えると約3.5から約1.8になる。この比は基準体重に依らない。一方、帯のkg単位の位置は基準体重に依存し、限界は基準体重に比例する（基準体重1 kgの違いは限界の1.3–1.5%）。基準体重は65–80 kgの母集団の中央値で、母集団と共変量の定義が資料ごとに異なる。avelumabの中心化の定数は明記されていない。したがって、表2の体重を抗体間で比べるときは、指数の差だけでなく基準体重の差も含む。

\(s=1\) の結果は、基準体重の患者のまわりでの曝露のばらつきに答える。承認用量では \(s\) が1.00–1.30（durvalumabは投与間隔を考慮して1.07）で、帯の位置が重い側へ動く（表6）。固定用量が実際にどの体重の患者のmg/kg用量に相当するかで、同じ \(b\) でも限界は大きく動く。

\(b=0.5\) の交差は、式 (4) の2乗の関係から導かれ、数値でも確かめられた。しかし、点推定が0.5を下回った4種類のうち、確率が0.99以上だったのはavelumabとdurvalumabだけで、dostarlimabは0.85、cemiplimabは0.66である。tislelizumab・nivolumab・pembrolizumabは0.5を上回る確率が0.93–0.98だが、点推定は0.565–0.595と0.5に近い。この確率は報告された標準誤差だけに基づき、モデル間の指数の差（標準誤差の0.2–1.7倍）を含まない。「\(b<0.5\) なら固定用量」という二分は、境界付近の抗体では確定できない。この関係はAUCと平均濃度の分散に限られ、トラフでは別の計算が必要になる。

panitumumabは、指数を確認できなかったが、公表された解析が参考になる。Liaoらは、シミュレーションしたAUCの患者間変動が、6 mg/kgで29%、フラット480 mgで34%だったと報告した ([15](#ref-15))。この方向は \(b>0.5\) と整合する。ただし、panitumumabは非線形PKを持ち、本記事のべき乗モデルの対象外であり、指数の値は確認していない。本記事の指数の範囲0.32–0.69は、PD-1・PD-L1・CTLA-4を標的とする抗体の範囲であり、抗体一般の範囲ではない（trastuzumabは0.967が報告されている）。

トラフでは、体重の影響が \(V\) の指数にも依存した。9種類すべてで、トラフの上限側の限界は、AUCの限界より原資料の投与間隔で2.3–13.1 kg、共通の21日では2.3–19.5 kg軽い体重に移った。この差は、1コンパートメント・ボーラスの近似と投与間隔、\(V\) の指数、コンパートメント間クリアランスの扱いに依存し、2コンパートメントでは符号と大きさが変わった。cemiplimabでは、BMIを含めない体重の指数を \(V\) に使うと、限界が180 kg前後以上に動いた。\(V\) への体重の入り方が、トラフの閾値を左右する。

既存記事 ([3](#ref-3)) との対応では、pembrolizumabとnivolumabの指数と基準体重は一次資料で確認でき、同じ値だった（0.595と76.8 kg、0.566と80 kg）。数値は、定義と用量の対応づけ \(s\) の違いで大きく動き、直接比べられない。

## 限界

結果は、べき乗モデル（式 (1)）、報告された指数、仮定した体重分布に条件付きである。各指数は、各試験の患者集団で、体重と相関する性別・アルブミン・腫瘍量などの共変量と同時に推定された条件付きの値で、体重の影響が他の共変量の影響を含む可能性がある。体重と他のCLの決定因子の相関は、対数SD 0.30（仮定）を加えた総SDの計算（独立を仮定）に含まれない。報告された標準誤差はモデルが正しいという条件での値である。tislelizumabの患者の76.7%はアジア人で ([1](#ref-1))、他の資料と集団が異なる。

体重の指数は総体重に対するべき乗で、除脂肪体重と肥満（高BMIでは総体重のべき乗がCLを過大にする）、悪液質、べき乗以外の形、体重の両端での非線形性は含まれない。限界体重は、原資料の体重範囲の端か外側で外挿になり（\(\pm30\%\) の5限界は範囲外）、pembrolizumab・nivolumab・atezolizumabは体重範囲を取得できなかった。5パーセンタイルと95パーセンタイルはどの資料でも取得できなかった。

標準誤差は、報告されたRSEまたは区間から求めた対称な正規近似である。durvalumabのブートストラップの成功は1,000回中694回で ([8](#ref-8))、atezolizumabとcemiplimabは区間が報告されていない。atezolizumabの値はFDA審査担当者が申請者のモデルを再推定した結果で ([7](#ref-7))、RSEは整数に丸められており、原著論文の値ではない。avelumabの基準体重は中央値71 kgで、中心化の定数は明記されていない。dostarlimabは式が本文にない。基準体重は推定されたパラメータではなく、その不確実性は含まれない。nivolumab・avelumab・cemiplimab・dostarlimab・ipilimumab・durvalumabのCLは時間とともに変化するモデルで、指数は基準時点（ベースライン）のCLに対するものである。時間変化の因子が体重と独立であれば、定常状態の比は保たれるが、この因子は病勢や悪液質と関連し、体重と相関する可能性がある。durvalumabの非線形（Michaelis–Menten）消失は表で体重によって調整されておらず、軽い体重の患者と低用量の比較に関係する。べき乗の比が当てはまるのは、線形または基準時点の成分である。

体重分布は、4つの対数正規分布のシナリオで、特定の集団の主張ではない。実際の体重分布は、対数正規分布より右の裾が重い。体重以外のCLの個体間変動、共変量間の相関は含めていない。トラフの計算は、1コンパートメント・ボーラスの近似と、2・3コンパートメントでの感度解析で、2つのコンパートメント間クリアランスの扱いだけを試した。最高濃度は解析していない。

曝露の差は効果や安全性の差ではない。曝露と応答の関係が平坦かどうかは、本記事が扱わない。閾値は曝露比の定義であり、臨床上のカットオフではなく、用量の推奨ではない。確認できなかった抗体（図2）の結果は含まれず、9種類は薬剤の代表標本ではない。


## 結論

固定用量に、体重の閾値という一つの値はない。曝露比が基準の ±20% に収まる体重帯として閾値を定義すると、9種類の抗体で、固定用量の下限側は40–62 kg、上限側は96–141 kgだった。この範囲は、指数 \(b\)（0.324–0.694）、基準体重（65–80 kg）、固定用量とmg/kg用量の対応づけ \(s\) で決まり、\(b\) の標準誤差だけでも、上限側の限界が最大で約40 kg幅の区間（avelumab、126–168 kg）を持った。端の体重は原資料の患者が少ない外挿を含みうる。AUC（または平均濃度）の対数の分散は、体重だけに由来する分では、\(b=0.5\) で両方式が等しく、点推定が下回ったのは4種類だが、確率が0.99以上だったのはavelumabとdurvalumabだけだった。トラフで定義すると、上限側の限界は、9種類で、原資料の投与間隔ではAUCの限界より2–13 kg軽い体重に移った。これらは、べき乗モデル、報告された指数、仮定した体重分布の下での曝露の計算であり、効果の差を示すものではなく、用量の推奨でもない。

## データとコードの公開状況

入力は、公表された表から転記した指数と典型値（`inputs/parameter_table.csv`、各行に出典のDOI・表の位置・基準体重の根拠を記載）、原資料の集団の体重範囲（`inputs/source_weight_ranges.csv`）、確認できなかった抗体の記録（`inputs/not_verified.csv`）である。計算コード（`powermodel.py`・`odecheck.py`・`analysis.py`・`figures.py`）、テスト（`test_analysis.py`、15件）、再現性の確認（`check_reproducibility.py`）、`requirements.txt`、結果のCSV/JSON、図を配布ZIPに含める。乱数シードは20261105、Python 3.12・NumPy 2.2・SciPy 1.14・pandas 2.2・matplotlib 3.9・pytest 9で実行した。再実行は、`python -X utf8 analysis.py`、`python -X utf8 figures.py`、`python -X utf8 -m pytest test_analysis.py -q`、`python -X utf8 check_reproducibility.py` の順で、全体で2分程度である。2回の実行で結果ファイルのハッシュが一致することを、`check_reproducibility.py` で確認した。

入力表は、原資料から転記した数値と表の位置だけを含み、原資料の表・図・本文は再掲していない。原資料は、それぞれのライセンスで公開されている。cemiplimab ([10](#ref-10)) とtrastuzumab ([16](#ref-16)) はCC BY、tislelizumab ([1](#ref-1))・dostarlimab ([2](#ref-2))・nivolumab ([6](#ref-6))・durvalumab ([8](#ref-8))・panitumumabのLiaoらの解析 ([15](#ref-15)) はCC BY-NC、pembrolizumab ([5](#ref-5))・avelumab ([9](#ref-9))・ipilimumab ([11](#ref-11), [12](#ref-12))・bevacizumab ([17](#ref-17))・rituximab ([18](#ref-18)) はCC BY-NC-NDである。camrelizumab ([13](#ref-13)) とMaらのpanitumumab解析 ([14](#ref-14)) は出版社の条件によるもので、FDAの審査資料 ([7](#ref-7)) は米国政府の文書である。これらのライセンスは原資料に適用され、本記事が編集した入力表には及ばない。図はすべて本記事の計算による。コードはMIT License、結果のCSV/JSONと図はCC BY 4.0とし、`LICENSE` に記載した。

[解析コード・結果・図をダウンロード](shared/flat-dose-weight-threshold/flat-dose-weight-threshold-companion.zip)

再実行用の資料一式は[配布資料](shared/flat-dose-weight-threshold/flat-dose-weight-threshold-companion.zip)に置いた。


## 参照

<span id="ref-1"></span>1. Budha N, Wu CY, Tang Z, Yu T, Liu L, Xu F, et al. Model-based population pharmacokinetic analysis of tislelizumab in patients with advanced tumors. CPT Pharmacometrics Syst Pharmacol. 2023;12(1):95–109. [https://doi.org/10.1002/psp4.12880](https://doi.org/10.1002/psp4.12880)
<span id="ref-2"></span>2. Melhem M, Hanze E, Lu S, Alskär O, Visser S, Gandhi Y. Population pharmacokinetics and exposure-response of anti-programmed cell death protein-1 monoclonal antibody dostarlimab in advanced solid tumours. Br J Clin Pharmacol. 2022;88(9):4142–4154. [https://doi.org/10.1111/bcp.15339](https://doi.org/10.1111/bcp.15339)
<span id="ref-3"></span>3. Kumakura D. Do fixed doses of anti-PD-1 antibodies keep exposure in range at extreme body weights? [Internet]. DaikiKumakura.github.io; 2026 Oct 20 [cited 2026 Nov 5]. Available from: [https://daikikumakura.github.io/writing/fixed-vs-weight-dosing.html](https://daikikumakura.github.io/writing/fixed-vs-weight-dosing.html)
<span id="ref-4"></span>4. Kumakura D. Fixed (flat) dosing versus weight-based dosing [Internet]. DaikiKumakura.github.io; updated 2026 Oct 28 [cited 2026 Nov 5]. Available from: [https://daikikumakura.github.io/glossary/fixed-vs-weight-based-dosing-ja.html](https://daikikumakura.github.io/glossary/fixed-vs-weight-based-dosing-ja.html)
<span id="ref-5"></span>5. Ahamadi M, Freshwater T, Prohn M, Li CH, de Alwis DP, de Greef R, et al. Model-based characterization of the pharmacokinetics of pembrolizumab: a humanized anti-PD-1 monoclonal antibody in advanced solid tumors. CPT Pharmacometrics Syst Pharmacol. 2017;6(1):49–57. [https://doi.org/10.1002/psp4.12139](https://doi.org/10.1002/psp4.12139)
<span id="ref-6"></span>6. Bajaj G, Wang X, Agrawal S, Gupta M, Roy A, Feng Y. Model-based population pharmacokinetic analysis of nivolumab in patients with solid tumors. CPT Pharmacometrics Syst Pharmacol. 2017;6(1):58–66. [https://doi.org/10.1002/psp4.12143](https://doi.org/10.1002/psp4.12143)
<span id="ref-7"></span>7. U.S. Food and Drug Administration, Center for Drug Evaluation and Research. Clinical pharmacology and biopharmaceutics review(s), application number 761041Orig1s000 (atezolizumab), Reference ID 3992046 [Internet]. FDA; [date unknown; URL path 2016] [cited 2026 Nov 5]. Available from: [https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/761041Orig1s000ClinPharmR.pdf](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/761041Orig1s000ClinPharmR.pdf)
<span id="ref-8"></span>8. Baverel PG, Dubois VFS, Jin CY, Zheng Y, Song X, Jin X, et al. Population pharmacokinetics of durvalumab in cancer patients and association with longitudinal biomarkers of disease status. Clin Pharmacol Ther. 2018;103(4):631–642. [https://doi.org/10.1002/cpt.982](https://doi.org/10.1002/cpt.982)
<span id="ref-9"></span>9. Wilkins JJ, Brockhaus B, Dai H, Vugmeyster Y, White JT, Brar S, et al. Time-varying clearance and impact of disease state on the pharmacokinetics of avelumab in Merkel cell carcinoma and urothelial carcinoma. CPT Pharmacometrics Syst Pharmacol. 2019;8(6):415–427. [https://doi.org/10.1002/psp4.12406](https://doi.org/10.1002/psp4.12406)
<span id="ref-10"></span>10. Yang F, Paccaly AJ, Rippley RK, Davis JD, DiCioccio AT. Population pharmacokinetic characteristics of cemiplimab in patients with advanced malignancies. J Pharmacokinet Pharmacodyn. 2021;48(4):479–494. [https://doi.org/10.1007/s10928-021-09739-y](https://doi.org/10.1007/s10928-021-09739-y)
<span id="ref-11"></span>11. Sanghavi K, Zhang J, Zhao X, Feng Y, Statkevich P, Sheng J, et al. Population pharmacokinetics of ipilimumab in combination with nivolumab in patients with advanced solid tumors. CPT Pharmacometrics Syst Pharmacol. 2020;9(1):29–39. [https://doi.org/10.1002/psp4.12477](https://doi.org/10.1002/psp4.12477)
<span id="ref-12"></span>12. Feng Y, Masson E, Dai D, Parker SM, Berman D, Roy A. Model-based clinical pharmacology profiling of ipilimumab in patients with advanced melanoma. Br J Clin Pharmacol. 2014;78(1):106–117. [https://doi.org/10.1111/bcp.12323](https://doi.org/10.1111/bcp.12323)
<span id="ref-13"></span>13. Wang CY, Sheng CC, Ma GL, Xu D, Liu XQ, Wang YY, et al. Population pharmacokinetics of the anti-PD-1 antibody camrelizumab in patients with multiple tumor types and model-informed dosing strategy. Acta Pharmacol Sin. 2021;42(8):1368–1375. [https://doi.org/10.1038/s41401-020-00550-y](https://doi.org/10.1038/s41401-020-00550-y). Abstract and a truncated publisher page were read.
<span id="ref-14"></span>14. Ma P, Yang BB, Wang YM, Peterson M, Narayanan A, Sutjandra L, et al. Population pharmacokinetic analysis of panitumumab in patients with advanced solid tumors. J Clin Pharmacol. 2009;49(10):1142–1156. [https://doi.org/10.1177/0091270009344989](https://doi.org/10.1177/0091270009344989). Abstract only was read.
<span id="ref-15"></span>15. Liao MZ, Berkhout M, Prenen H, Dutta S, Upreti VV. Dose regimen rationale for panitumumab in cancer patients: to be based on body weight or not. Clin Pharmacol. 2020;12:109–114. [https://doi.org/10.2147/CPAA.S262949](https://doi.org/10.2147/CPAA.S262949)
<span id="ref-16"></span>16. Quartino AL, Li H, Kirschbrown WP, Mangat R, Wada DR, Garg A, et al. Population pharmacokinetic and covariate analyses of intravenous trastuzumab (Herceptin), a HER2-targeted monoclonal antibody, in patients with a variety of solid tumors. Cancer Chemother Pharmacol. 2019;83(2):329–340. [https://doi.org/10.1007/s00280-018-3728-z](https://doi.org/10.1007/s00280-018-3728-z)
<span id="ref-17"></span>17. Han K, Peyret T, Quartino A, Gosselin NH, Gururangan S, Casanova M, et al. Bevacizumab dosing strategy in paediatric cancer patients based on population pharmacokinetic analysis with external validation. Br J Clin Pharmacol. 2016;81(1):148–160. [https://doi.org/10.1111/bcp.12778](https://doi.org/10.1111/bcp.12778)
<span id="ref-18"></span>18. Gibiansky E, Gibiansky L, Chavanne C, Frey N, Jamois C. Population pharmacokinetic and exposure-response analyses of intravenous and subcutaneous rituximab in patients with chronic lymphocytic leukemia. CPT Pharmacometrics Syst Pharmacol. 2021;10(8):914–927. [https://doi.org/10.1002/psp4.12665](https://doi.org/10.1002/psp4.12665)
