[English](mrna-vaccine-rfs-comparison-en.html)

mRNAがんワクチンで「再発リスク42%減」。この数字は、100人を治療すれば42人の再発を防げるという意味ではない。死亡だけが42%減ったという意味でもない。

INTerpath-001で報告された42%は、再発または死亡までの時間に関するハザード比0.58を、`1 − 0.58`で表したものだ。同じ報告にある2年無再発生存率は82.2%と70.0%だった ([1](#ref-1))。それなら差は12.2ポイントである。42%と12.2ポイントのどちらかが誤りなのではなく、計算している対象が違う。

もう一つ気になるのは、術前に免疫療法を行った別の試験にも0.58というハザード比があることだ。同じ数字なら、ワクチンを加えることと治療を手術前へ移すことは同じ効果なのだろうか。この比較では、薬の名前より先に、時計を動かし始めた時点を確かめる必要がある。

## 対象と確認範囲

INTerpath-001の2026年10月22日付の公表資料、SWOG S1801とNADINAの原著抄録、S1801の評価項目を扱った方法論論文の抄録を確認した。INTerpath-001は切除後のステージIIB–IV黒色腫を対象とし、個別化mRNA製剤intismeran autogeneをペムブロリズマブへ追加する無作為化比較である ([1](#ref-1))。

本記事の計算は、公表された2年推定値の引き算と比、そして時間の違いを示す仮想例に限る。個人別データの再解析、Kaplan–Meier曲線の読取り、試験間の間接比較推定は行っていない。原著の全文や付録を確認できたときと同じ範囲を主張しない。

## 42%と12.2ポイントを分ける

無再発生存、recurrence-free survival（RFS）のイベントには再発と死亡が含まれる。全生存、overall survival（OS）とは異なる。INTerpath-001の公表時点ではOSのデータは未成熟とされている ([1](#ref-1))。

2年RFSを、ワクチン併用群で \(S_1(2)=0.822\)、対照群で \(S_0(2)=0.700\) と置く。公表された丸め値から、2年までのイベント確率をそれぞれ \(1-S(2)\) と計算すると、17.8%と30.0%になる。

\[
\Delta(2)=S_1(2)-S_0(2)=0.122,
\]

\[
\mathrm{RR}(2)=\frac{1-S_1(2)}{1-S_0(2)}
=\frac{0.178}{0.300}=0.593.
\]

この時点に限った相対リスク減少は約40.7%。見出しの42%に近いが、同じ計算ではない。ハザードは、その時点までイベントを経験していない人の中で、直後にイベントが起こる速さを表す。固定した2年までの累積確率とは区別する。

| 計算対象 | 公表値からの計算 | 意味 |
| --- | ---: | --- |
| 2年RFSの差 | 12.2ポイント | 2年時点での無再発生存確率の群間差 |
| 2年イベント確率の比 | 0.593 | 17.8%を30.0%で割った値 |
| その相対減少 | 40.7% | 固定した2年までのイベント確率の相対差 |
| 差の逆数 | 8.20 | 2年の絶対差に対応するNNTの点推定 |

表1　報告された2年RFSの丸め値から筆者が計算した。NNTはnumber needed to treat。患者数から直接割った観測割合ではなく、打切りを考慮した時点別推定値を入力にしている。

NNTを整数へ切り上げれば約9人となるが、「9人治療すれば必ず1人が助かる」とは言えない。対応する転帰は2年までの再発または死亡であり、生涯の死亡回避ではない。また、群ごとの信頼区間の端点を機械的に引いても、差の正式な95%信頼区間にはならない。ここでは差とNNTの区間を推定しておらず、点推定だけを示した。

## 効果が現れる時期は一つの数字に収まらない

公表資料の事前規定の感度分析では、RFSのハザード比は最初の6か月で0.99、その後で0.42だった。それぞれの95%信頼区間は0.66–1.49と0.30–0.58である ([1](#ref-1))。前半の区間が1を含むことを、効果が完全にゼロである証明とは読まない。一方、全期間の0.58を「初日から終始42%低い」と置き換えることもできない。

この違いを確かめるため、2年時点の値だけが分かる状況で、二つの時間経過を作った。以下はINTerpath-001の曲線の再現ではない。

対照群のハザードを一定と仮定し、2年RFSが0.700になるように \(\lambda_0=-\log(0.700)/2\) と置く。併用群には、最初から一定の比でハザードを下げるモデルAと、最初の0.5年は対照と同じで、その後にだけ下げるモデルBを用意する。時間 \(t\) の単位は年とし、両モデルの2年RFSを0.822へ合わせる。

\[
S_A(t)=\exp(-r_A\lambda_0 t),\qquad
r_A=\frac{-\log(0.822)}{-\log(0.700)}=0.550,
\]

\[
S_B(t)=\exp\left\{-\lambda_0\min(t,0.5)
-r_B\lambda_0\max(t-0.5,0)\right\},
\]

\[
r_B=\frac{-\log(0.822)-0.5\lambda_0}{1.5\lambda_0}=0.399.
\]

![同じ2年RFSへ到達する一定効果と遅延効果の仮想曲線。実際の試験曲線ではない。](shared/mrna-vaccine-rfs-comparison/figures/same-endpoint-different-timing.png)

図1　筆者の仮想計算。青は一定効果、橙の破線は最初の6か月に効果を置かない例、灰は仮想対照である。2年RFSは両モデルとも82.2%だが、6か月では95.2%と91.5%になる。信頼区間や試験の観測値を表す図ではない。

2年値が同じでも、初期にイベントを回避する量は違う。反対に、2年値だけから効果の発現時期を復元することもできない。ここで得た0.550と0.399は仮定した曲線の係数であり、原試験のCoxモデルのハザード比を再推定した値ではない。

前半と後半の差を、mRNAによる免疫応答の形成だけで説明することもまだできない。時間が経つとイベント未発生の集団の構成も変わる。後半のハザード比は、各群でその時点までイベントを経験していない人を比べており、無作為化時点の全員に対する固定の効力係数ではない。6か月以降の数字を取り出して、治療開始を6か月遅らせてもよいという判断にはつながらない。

## 同じ0.58でも比べている治療戦略が違う

SWOG S1801は、ペムブロリズマブを手術前後へ分ける戦略と、すべて手術後に投与する戦略を比較した。対象は臨床的に検出できる切除可能なステージIIIB–IVC黒色腫である。原著抄録では2年の無イベント生存率は72%と49%で、評価項目には手術へ進めないことや術後治療を開始できないことも含まれる ([2](#ref-2))。0.58というハザード比は[SWOGの公表スライド](https://www.swog.org/sites/default/files/docs/2023-04/ScientificImpact_Spr23.pdf#page=1)でも確認できる ([3](#ref-3))。

| 比較 | INTerpath-001 | SWOG S1801 |
| --- | --- | --- |
| 無作為化時点 | 完全切除後 | 手術前 |
| 主な問い | 術後ペムブロリズマブへワクチンを追加する効果 | ペムブロリズマブの一部を術前へ移す効果 |
| 主な対象 | 切除後ステージIIB–IV | 臨床的に検出可能な切除可能IIIB–IVC |
| 評価する転帰 | RFS | 無イベント生存（EFS） |
| 手術へ進めないイベント | 無作為化前に切除済み | 評価項目に含まれる |

表2　試験の評価対象の比較。INTerpath-001は公表資料、S1801は原著抄録による ([1](#ref-1), [2](#ref-2))。両試験の治療成績を同一集団へ標準化した表ではない。

INTerpath-001では無作為化へ入るために手術を終えている。S1801では、手術までに起きる不利益も比較へ入れる。両者の対照群を「ペムブロリズマブ単剤」という名前だけで同じものと見なすと、この選択と時間の違いが落ちる。

S1801の研究者らも、術前・術後戦略を比較するときは、無作為化からのEFSと、群間で異なるイベント測定時期を考慮すべきだと論じている ([4](#ref-4))。評価の時計は細かな集計手順ではなく、治療戦略の何を利益・不利益として数えるかを決めている。

NADINAでも、術前ニボルマブ・イピリムマブと病理応答に応じた術後治療を組み合わせた戦略が、術後ニボルマブと比較された。対象は切除可能な肉眼的ステージIIIであり、術前群の全員が同じ術後治療を受ける設計ではない ([5](#ref-5))。「術前免疫療法」を単一の処置としてまとめると、薬剤の組合せと応答に応じた治療の違いまで消えてしまう。

同じハザード比を二つ並べても、ワクチン追加と術前投与が同等だとは言えない。異なる試験のハザード比を割るだけでは、対象集団、イベントの定義、無作為化時点を揃えた直接比較にはならない。

## 利益と害を同じ分母で読む

INTerpath-001の発表にあるグレード3–5の治療関連有害事象は14.2%と13.4%である ([1](#ref-1))。ここで「治療関連」を外した全有害事象の割合へ置き換えない。治療との因果関係を問う分類と、起きたことを広く拾う分類は違う。

この割合の単純差が小さいことだけで、安全性が同等と証明されたわけではない。同等性の許容幅を置いた解析ではなく、有害事象の種類・重症度・観察期間も一つの割合では表せない。効果のNNTと有害事象の逆数を並べる場合も、RFSの推定集団と安全性の評価集団を同一視しない。

## 42%が支持すること

この結果が支持するのは、切除後の対象集団において、ペムブロリズマブへintismeranを追加する戦略が、再発または死亡という複合転帰を改善したという比較である。死亡だけへの42%低下でも、術前免疫療法との同等性でもない。

同じ公表値を、全期間のハザード比、2年の絶対差、効果が現れる時期へ分けて読むと、治療の意味が具体的になる。ワクチンか術前治療かを決めるためには、この試験が答えた追加効果の問いと、まだ直接比べていない治療戦略の問いを分けておく必要がある。

## データとコードの公開状況

公表値の計算と図1を作る[Pythonスクリプト](shared/mrna-vaccine-rfs-comparison/analysis.py)、[計算結果](shared/mrna-vaccine-rfs-comparison/results/calculations.json)、[仮想曲線CSV](shared/mrna-vaccine-rfs-comparison/results/illustrative-curves.csv)を公開する。Python 3.12.4、Matplotlib 3.9.1で実行した。乱数は使わない。試験の患者データや原著図は再配布していない。

## 参照

1. <span id="ref-1"></span>Merck & Co., Inc., Moderna, Inc. Merck and Moderna Will Present Results From Landmark Phase 3 INTerpath-001 Trial for Intismeran Autogene Plus KEYTRUDA (pembrolizumab) at ESMO 2026 Presidential Symposium [Internet]. Merck; 2026 Oct 22 [cited 2026 Oct 30]. [Official announcement](https://www.merck.com/news/merck-and-moderna-will-present-results-from-landmark-phase-3-interpath-001-trial-for-intismeran-autogene-plus-keytruda-pembrolizumab-at-esmo-2026-presidential-symposium/).
2. <span id="ref-2"></span>Patel SP, Othus M, Chen Y, Wright GP Jr, Yost KJ, Hyngstrom JR, et al. Neoadjuvant-Adjuvant or Adjuvant-Only Pembrolizumab in Advanced Melanoma. N Engl J Med. 2023;388(9):813–823. [doi:10.1056/NEJMoa2211437](https://doi.org/10.1056/NEJMoa2211437). [Abstract consulted](https://pubmed.ncbi.nlm.nih.gov/36856617/).
3. <span id="ref-3"></span>LeBlanc M. Scientific Impact of the CRA [Presentation]. SWOG Cancer Research Network; 2023 Apr 26. Slide 2 (PDF p. 1). [Presentation PDF](https://www.swog.org/sites/default/files/docs/2023-04/ScientificImpact_Spr23.pdf#page=1).
4. <span id="ref-4"></span>Othus M, Sharon E, Wu MC, Sondak VK, Ribas A, Patel SP. Design considerations for randomized comparisons of neoadjuvant-adjuvant versus adjuvant-only cancer immunotherapy when tumor measurement schedules do not align (SWOG S1801). Clin Trials. 2025;22(5):571–577. [doi:10.1177/17407745251321371](https://doi.org/10.1177/17407745251321371). [Abstract consulted](https://pubmed.ncbi.nlm.nih.gov/40099861/).
5. <span id="ref-5"></span>Blank CU, Lucas MW, Scolyer RA, van de Wiel BA, Menzies AM, Lopez-Yurda M, et al. Neoadjuvant Nivolumab and Ipilimumab in Resectable Stage III Melanoma. N Engl J Med. 2024;391(18):1696–1708. [doi:10.1056/NEJMoa2402604](https://doi.org/10.1056/NEJMoa2402604). [Abstract consulted](https://pubmed.ncbi.nlm.nih.gov/38828984/).
