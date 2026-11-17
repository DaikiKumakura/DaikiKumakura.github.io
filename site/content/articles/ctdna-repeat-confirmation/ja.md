術後の血液検査で循環腫瘍DNA（ctDNA）を追うとき、1回の陽性で判定する場合と、2回続けて陽性になるまで待つ場合では、誰が治療試験の候補になるかが変わる。筋層浸潤性膀胱がんのIMvigor011では、膀胱全摘後にctDNAを繰り返し測定し、陽性となって適格基準を満たした患者をアテゾリズマブ群かプラセボ群に無作為に割り付けた ([1](#ref-1))。以下の計算では、この試験とは別に二つの仮想的な判定規則を比べる。

## 1回あたりの特異度をそろえる

分子残存病変（MRD）の有無は初回から最終採血まで変わらないとした。MRDがある患者の1回あたりの陽性率は70%で、結果は採血間で独立とした。MRDがない患者のうち、毎回陽性となる割合を `f` とし、0%、0.5%、1%を比べた。残りの患者の結果は採血間で独立とした。この群の1回あたりの陽性率を `q = (0.01 − f) / (1 − f)` とすると、MRDがない患者全体では、どの採血回でも偽陽性率が1%になる。

FDAのガイダンスは、早期固形がんでctDNAを患者選択に使う場合の考慮事項に、アッセイの性能と採血時期を挙げている ([2](#ref-2))。転移がん患者などを対象に血漿と白血球を同時に解析した研究では、血漿で検出された変異の一部がクローン性造血に由来した ([3](#ref-3))。ここで置いた0.5%と1%は、同じ患者で偽陽性が続く場合を検討するための仮定であり、術後アッセイの偽陽性率を推定した値ではない。

採血をまたぐ判定と、1検体内の陽性基準は分けて考える。FDAの審査資料によれば、Signatera CDxでは1検体で16の標的変異のうち2つ以上を検出すると陽性と判定する。全血の配列情報も使い、クローン性造血などに由来しうる候補変異を除く ([4](#ref-4))。以下の「2回連続陽性」は、別々に採った2検体が続けて陽性になる規則を指す。

## 8回調べたときの判定

陽性の連続回数を記録し、所定の回数に達した時点で陽性と判定した。判定がつく前に陰性が出れば連続回数をゼロに戻す。各回で初めて条件を満たす確率を合計すると、最終採血までに陽性と判定される確率が得られる。MRDがない患者の判定率は、必ず判定される群の割合 `f` に、残りの群の割合 `1 − f` とその群の判定確率の積を足して求めた。表1は真のMRDがある患者を5%と仮定した結果である。

**表1　8回採血したときの偽陽性患者数と陽性的中率**

| Always positive among patients without MRD | False-positive patients per 1,000 (one positive) | False-positive patients per 1,000 (two consecutive positives) | Positive predictive value (one positive) | Positive predictive value (two consecutive positives) |
| --- | ---: | ---: | ---: | ---: |
| 0% | 73.4 | 0.7 | 40.5% | 98.7% |
| 0.5% | 42.1 | 4.9 | 54.3% | 90.8% |
| 1% | 9.5 | 9.5 | 84.0% | 83.5% |

偽陽性患者数は検査対象1,000人あたりの期待値。陽性的中率は、陽性と判定された患者に占める真のMRD陽性者の割合。

MRDがある患者の判定率は、1回陽性で99.99%、連続陽性で96.48%だった。それぞれの規則で8回以内に判定された患者に限ると、判定までの採血回数は平均1.43回と3.20回だった。予定採血が2回なら、連続陽性での判定率は49%まで下がる。平均を計算する患者の集まりは規則ごとに異なるため、この差を同じ患者の待ち時間の差や治療開始の遅れとしては扱えない。

偽陽性が採血ごとに独立に起きるなら、採血が増えるほど、一度は偽陽性になる患者が増える。偽陽性がすべて同じ患者に集中する1%の条件では、2回陽性を待っても偽陽性患者数は1,000人あたり9.5人のままだった。その一方で、判定される真のMRD陽性者は50.0人から48.2人に減った。単回の特異度が同じ検査でも、同じ患者で偽陽性がどのくらい続くかによって、確認のためにもう一度採血する価値は変わる。

このモデルは、MRDが採血期間中に発生する過程、検査間の治療、臨床的再発による観測打ち切りを表さない。MRDがある患者についても採血間の誤差を独立とした。実際の試験で何人が治療候補になるかや、判定を待つことによる治療効果への影響は、この計算からは求められない。

## データとコードの公開状況

患者データは使用していない。[再現用ZIP](shared/ctdna-repeat-confirmation/ctdna-repeat-confirmation-companion.zip)にコードと36条件の結果を収録した。Python 3.12.4の標準ライブラリで `python analysis.py > results.csv` を実行すると同じ表を再生成できる。乱数は使用していない。

## 参照

1. <a id="ref-1"></a> Powles T, Kann AG, Castellano D, Gross-Goupil M, Nishiyama H, Bracarda S, et al. ctDNA-guided adjuvant atezolizumab in muscle-invasive bladder cancer. N Engl J Med. 2025;393(24):2395–2408. [doi:10.1056/NEJMoa2511885](https://doi.org/10.1056/NEJMoa2511885).
2. <a id="ref-2"></a> US Food and Drug Administration. Use of circulating tumor DNA for curative-intent solid tumor drug development: guidance for industry. 2024. [FDA guidance](https://www.fda.gov/media/183874/download).
3. <a id="ref-3"></a> Razavi P, Li BT, Brown DN, Jung B, Hubbell E, Shen R, et al. High-intensity sequencing reveals the sources of plasma circulating cell-free DNA variants. Nat Med. 2019;25(12):1928–1937. [doi:10.1038/s41591-019-0652-7](https://doi.org/10.1038/s41591-019-0652-7).
4. <a id="ref-4"></a> US Food and Drug Administration. Signatera CDx: Summary of Safety and Effectiveness Data. P260004. 2026. [FDA review, Section V](https://www.accessdata.fda.gov/cdrh_docs/pdf26/P260004B.pdf#page=3).
