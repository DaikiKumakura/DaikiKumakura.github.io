体重を入れると、pembrolizumabまたはnivolumabの曝露が、投与方式ごとに、臨床試験で確かめられた範囲を外れる割合を調べられます。数値は、[記事で説明している公表モデルのシミュレーション](../writing/fixed-vs-weight-dosing.html)の結果です。このページは数値を引くだけで、再計算はしません。

<div id="exposure-tool" data-lang="ja" data-src="../assets/tools/anti-pd1-exposure-data.json"></div>
<noscript><p class="notice">この機能にはJavaScriptが必要です。同じ数値は<a href="../writing/fixed-vs-weight-dosing.html">記事</a>の表にあります。</p></noscript>
<script src="../assets/tools/anti-pd1-exposure.js" defer></script>

## 見方

- **体重** で7つの帯（50 kg未満、50–60、60–80、80–100、100–120、120–150、150 kg以上）のどれかが選ばれます。表の割合は、その帯の仮想成人のうち、曝露が範囲を外れた人の割合です。
- **下限を下回る割合** は、定常状態のトラフが、体重換算の基準方式（pembrolizumab 2 mg/kg 3週ごと、nivolumab 3 mg/kg 2週ごと）の5パーセンタイルを下回る患者の割合です。**上限を超える割合** は、定常状態の最高濃度が、試験された最高用量（10 mg/kg 2週ごと）での最高濃度の中央値を超える患者の割合です。
- **範囲を保てるか** は、解析の前に決めた規則（下限を下回る割合が10%以下、かつ上限を超える割合が5%以下）を当てはめた判定です。2つの許容割合は変えられるので、判定が許容割合にどれだけ依存するかも確かめられます。
- **条件** で、記事の感度解析に切り替えられます。体重の指数を95%区間の両端に置いた場合、アジア人の体重分布、性を無視した場合、薬剤ごとの別条件（pembrolizumabは表の脚注の値と低アルブミン、nivolumabは時間変化するクリアランスを無視）です。

## 数値について

- 公表された母集団PKモデルを2つ再実装しました。pembrolizumab（Ahamadiら、2017）とnivolumab（Bajajら、2017）です。
- NHANES 2017〜2020年3月（米国の調査）の成人の体重から仮想患者20,000人を作り、52週以降の最初の投与間隔で曝露を計算しました。
- 下限と上限は、試験で使われた曝露の代理です。効果や毒性の閾値ではありません。
- 数値の出どころは、記事の[配布資料](../writing/shared/fixed-vs-weight-dosing/fixed-vs-weight-dosing-companion.zip)（`results/bands.csv`、`thresholds.csv`、`extreme-weights.csv`）です。

## 限界

シミュレーションによる曝露の比較であり、用量を決めるためのツールではありません。どの用量を患者に投与すべきかは示しません。曝露の差が効果の差になることも示していません。NHANESは米国の一般成人で、がん患者ではありません。判断できること・できないことの全体は、[記事](../writing/fixed-vs-weight-dosing.html)にあります。
