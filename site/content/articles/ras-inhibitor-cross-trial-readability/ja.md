基準日：本記事の事実関係は2026年11月3日時点の公開情報による。

2026年11月2日に、RAS阻害薬8剤の臨床成績を並べた図「KRASzy Progress」（Chris De Savi作）が、X上で再投稿された ([1](#ref-1))。図には、奏効率（ORR）、無増悪生存期間、全生存期間が、薬剤ごとに並ぶ。並んだ数値は、薬剤の優劣を示すように見える。本記事は、図に印字された数値のうち、公開資料で確認できたものについて、どの比較が区間つきで読め、どの比較が読めないかを、再計算で確かめる。

## 対象と確認範囲

図の画像は転載せず、印字された数値を公開資料と照合した。8剤のうち、次の5剤の成績を確認した（NSCLCは非小細胞肺がん、PDACは膵腺がん、FDAは米国食品医薬品局）。

- ソトラシブのCodeBreaK 200（ドセタキセルとの第3相、KRAS G12C変異のNSCLC）。論文の抄録 ([2](#ref-2)) と、論文を報じた記事 ([3](#ref-3)) を読んだ。奏効率と全生存期間は、後者による。
- ディバラシブのKrascendo 1（ソトラシブまたはアダグラシブとの第3相、KRAS G12C変異のNSCLC）。企業の発表 ([4](#ref-4)) を読んだ。査読論文は読めていない。
- ダラキソンラシブのRASolute 302（化学療法との第3相、転移性PDAC）。FDAの承認情報 ([5](#ref-5)) と、論文の抄録 ([6](#ref-6)) を読んだ。
- エリロンラシブの第1相（KRAS G12C阻害薬の治療後のNSCLC）。学会発表を報じた記事 ([7](#ref-7)) と、ニュース ([8](#ref-8)) を読んだ。
- ゾルドンラシブの第1相（KRAS G12DのNSCLC）。2026年の米国がん研究学会（AACR）の抄録CT021を報じた記事 ([9](#ref-9)) を読んだ。抄録そのものは読めていない。

残りの3剤（オロモラシブ、HRS-4642、セチデグラシブ）は、公開資料を確認できなかったため、表から除いた。ゾルドンラシブの第1次治療の併用と、エリロンラシブの併用の数値も、同じ理由で扱わない。

計算は、報告された奏効率と患者数から奏効例数を復元し（四捨五入）、Clopper–Pearsonの正確な95%信頼区間（CI） ([10](#ref-10)) を求め、報告された区間と比べた。ランダム化した2群の差には、Newcombeの区間 ([11](#ref-11)) を使った。区間は記述的なもので、多重性の調整はしていない。

## 論点ごとの検討

### 試験の対象と設計が違う

並んだ数値は、腫瘍、治療ライン、対照、評価の集団が異なる（表1）。

表1　確認できた試験の設計（ORR：奏効率、NSCLC：非小細胞肺がん）。患者数は、ランダム化した例数（実験群 / 対照群）。

| Trial | Tumor | Comparator | Randomized n | ORR denominator |
| --- | --- | --- | ---: | --- |
| CodeBreaK 200 | KRAS G12C NSCLC, after prior therapy | Docetaxel | 171 / 174 | Randomized |
| Krascendo 1 | KRAS G12C NSCLC, after prior therapy | Sotorasib or adagrasib | 167 / 171 | Response-evaluable (161 / 167) |
| RASolute 302 | Pancreatic adenocarcinoma, after one line | Chemotherapy | 248 / 252 | Overall population |
| Elironrasib phase 1 | KRAS G12C NSCLC, after a G12C inhibitor | None | 24 | Treated |
| Zoldonrasib phase 1 | KRAS G12D NSCLC, after immunotherapy and platinum | None | 27 | Efficacy-evaluable |

Krascendo 1の奏効率は、測定可能な病変がない10例（ディバラシブ群6例、対照群4例）を除いた評価可能集団（161例と167例）の値である ([4](#ref-4))。RASolute 302の例数は、論文の抄録による ([6](#ref-6))。

### 同じ試験の中の比較は区間つきで読める

ランダム化した試験の中では、2群の差を区間つきで読める（表2）。CodeBreaK 200の奏効率は、ソトラシブ28.1%（95%CI 21.5–35.4）、ドセタキセル13.2%（8.6–19.2）で、差は14.9パーセントポイント（6.3–23.2）だった ([3](#ref-3))。RASolute 302の全体集団は、ダラキソンラシブ30%（25–36）、化学療法11%（7–15）だった ([5](#ref-5))。復元した例数から計算した差は18.7パーセントポイント（11.7–25.6）だが、報告値が整数のため、差は小数点以下まで正確ではない（30と11の差は19）。復元した例数から求めた正確な区間は、CodeBreaK 200で報告値と完全に一致し、RASolute 302で0.8ポイント以内の差だった（FDAの区間の計算方法は、読んだ範囲に書かれていない）。

表2　ランダム化した2試験の奏効率の差（復元した例数、Newcombeの95%区間）。

| Trial | Experimental ORR | Control ORR | Difference (percentage points) | 95% interval |
| --- | ---: | ---: | ---: | --- |
| CodeBreaK 200 | 28.1% | 13.2% | 14.9 | 6.3 to 23.2 |
| RASolute 302 (overall) | 30% | 11% | 18.7 | 11.7 to 25.6 |

無増悪生存期間と全生存期間は、各試験でハザード比が区間つきで報告されている。CodeBreaK 200は、無増悪生存期間が0.66（0.51–0.86）、全生存期間が1.01（0.77–1.33） ([2](#ref-2), [3](#ref-3))。Krascendo 1は、無増悪生存期間が0.58（0.44–0.76）、全生存期間が0.56（0.41–0.78） ([4](#ref-4))。RASolute 302の全体集団は、無増悪生存期間が0.49（0.38–0.64）、全生存期間が0.40（0.30–0.53） ([5](#ref-5))。ハザード比は、比例ハザード性を仮定した要約で、対照や後治療（対照群から実験薬への切り替えの有無は、読んだ範囲に書かれていない）が違えば、意味も変わる。

### 試験をまたぐ比較が読めない理由

3つの試験の対照群の奏効率は、13.2%（ドセタキセル）、32%（ソトラシブまたはアダグラシブ）、11%（化学療法）と大きく違う（図1） ([3](#ref-3), [4](#ref-4), [5](#ref-5))。この違いは、対照の治療の違いと、腫瘍や治療ラインの違いの両方を含み、両者は分けられない。どちらにしても、実験群の奏効率やハザード比を、試験をまたいで並べて、薬剤の優劣を読むことはできない。たとえば、ダラキソンラシブの全生存期間のハザード比0.40とソトラシブの1.01は、腫瘍も対照も違う。

![図1　図に印字された群の奏効率（ORR）と、復元した例数から求めた正確な95%区間（青：実験群、灰：対照群、橙：単群）。Krascendo 1の値は、評価可能集団の割合（空の丸）。作図は筆者による（元の図の画像は転載していない）。](shared/ras-inhibitor-cross-trial-readability/figures/01-orr-intervals.png)

試験をまたいで比べてよいかは、共通の薬剤で、ある程度は確かめられる。ソトラシブは、CodeBreaK 200の実験群と、Krascendo 1の対照群（ソトラシブまたはアダグラシブ、内訳は読んだ範囲に書かれていない）の両方にある。奏効率は、28.1%（21.5–35.4）と32%（24.8–39.4）で、差は3.7パーセントポイント（−6.1〜13.3）だった。無増悪生存期間の中央値は、5.6か月（4.3–7.8）と5.7か月だった ([2](#ref-2), [4](#ref-4))。両試験の結果に、差は見えない。ただし、区間が広く、差がないことの証拠にはならない。対照群がアダグラシブを含む点、試験の時期、評価の方法（独立判定と治験医師判定の違いは、読んだ範囲に書かれていない）も違う。この比較から言えるのは、ソトラシブの結果が2つの試験で大きくは食い違わなかった、という限られたことである。

### 単群の第1相は区間が広く順位を付けられない

エリロンラシブ（n = 24）の奏効率は42%（22–63）、ゾルドンラシブ（n = 27）は52%（再計算した区間 32–71）で、区間の幅は約40パーセントポイントある（図1） ([7](#ref-7), [9](#ref-9))。2つの区間は大きく重なり、Krascendo 1のディバラシブの58%（49.7–65.5）の区間とも一部が重なる。区間が重なることは、奏効率が等しいことを意味しない。ただし、この標本の大きさでは、差があるとも順位が付くとも言えない。さらに、エリロンラシブの集団は、全員がKRAS G12C阻害薬の治療後で、92%がそれで進行していた ([8](#ref-8))。ゾルドンラシブは別の標的（KRAS G12D）で、免疫療法と白金製剤の治療後の集団である ([9](#ref-9))。図の無増悪生存期間（エリロンラシブ6.2か月、ゾルドンラシブ11.1か月）は、追跡の期間が揃わず、中央値の区間も示されていないため、同じ扱いで比較しない。

### 図の数値の照合

確認できた数値は、図と公開資料で一致した。RASolute 302の全体集団の奏効率30%は、FDAの値（25–36） ([5](#ref-5)) と一致する。論文（NEJM）の全文と、Krascendo 1の論文は読めておらず、これらの値は確認していない。

## 総合判断

図の数値のうち、同じ試験内の差と、ランダム化した対照との比較は、区間つきで読める。試験をまたぐ薬剤の優劣は、対照群の奏効率が11〜32%と大きく違うことなどから、読めない。共通の薬剤（ソトラシブ）で結果の近さを確かめられたのは、ディバラシブの試験との1組だけで、その近さも、区間の広さから弱い。単群の第1相の奏効率は、約40パーセントポイントの区間の幅から、互いにも、ランダム化した試験の実験群とも、順位を付けられない。

## 限界

確認したのは8剤のうち5剤で、確認した資料には、報道や企業の発表が含まれる。論文の全文を読めたものはない。奏効率の復元は四捨五入した値からで、区間は記述的なものである。本記事は、薬剤の有効性の優劣を判断するものではない。

## 結論

RAS阻害薬の成績を並べた図は、確認できた5剤について、各試験の内部の比較としては読めるが、試験間の薬剤の優劣の比較としては読めない。同じ試験の中の奏効率の差は、区間つきで確かめられた（CodeBreaK 200で14.9パーセントポイント、RASolute 302で約19パーセントポイント）。試験をまたぐ比較は、対照の違いと集団の違いのため成り立たず、単群の第1相の奏効率は、区間の幅が約40パーセントポイントで、順位を付けられない。

## データとコードの公開状況

計算コード（`analysis.py`、`figures.py`）、検査（`test_analysis.py`）、入力の表（`inputs/arms.csv`、出典の区分つき）、結果の表を配布資料に含めた。Python 3（numpy、scipy、pandas、matplotlib）で、`python analysis.py`、`python figures.py`、`python -m pytest test_analysis.py` の順に実行する。入力は公開された報告の値で、患者データは使っていない。筆者が使うAIによる査読（3回）を受けたが、人間の第三者による確認ではない。

再実行用の資料一式は[配布資料](shared/ras-inhibitor-cross-trial-readability/ras-inhibitor-cross-trial-readability-companion.zip)に置いた。


## 参照

<span id="ref-1"></span>1. Scott KA [@Sculpturatus]. credit to chris de savi [X post]. X. 2026 Nov 2 [cited 2026 Nov 3]. The post shows the image "KRASzy Progress" © Chris De Savi. Available from: https://x.com/Sculpturatus/status/2117250509644198100

<span id="ref-2"></span>2. de Langen AJ, Johnson ML, Mazieres J, Dingemans AC, Mountzios G, Pless M, et al. Sotorasib versus docetaxel for previously treated non-small-cell lung cancer with KRAS G12C mutation: a randomised, open-label, phase 3 trial. Lancet. 2023;401(10378):733–746. [doi:10.1016/S0140-6736(23)00221-0](https://doi.org/10.1016/S0140-6736(23)00221-0)

<span id="ref-3"></span>3. The ASCO Post. Sotorasib improves progression-free survival vs docetaxel in previously treated advanced NSCLC with KRAS G12C mutation [Internet]. 2023 Mar 25 [cited 2026 Nov 3]. Available from: https://ascopost.com/issues/march-25-2023/sotorasib-improves-progression-free-survival-vs-docetaxel-in-previously-treated-advanced-nsclc-with-kras-g12c-mutation

<span id="ref-4"></span>4. Roche. Roche's divarasib demonstrated best-in-class efficacy, advancing the standard of care in previously treated KRAS G12C-mutated lung cancer [Press release]. Basel; 2026 Oct 25 [cited 2026 Nov 3]. Available from: https://www.roche.com/media/releases/med-cor-2026-10-25

<span id="ref-5"></span>5. U.S. Food and Drug Administration. FDA approves daraxonrasib for metastatic pancreatic adenocarcinoma [Internet]. FDA; 2026 [cited 2026 Nov 3]. Available from: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-daraxonrasib-metastatic-pancreatic-adenocarcinoma

<span id="ref-6"></span>6. O'Reilly EM, Wainberg ZA, Hendifar AE, Borad MJ, Pietrantonio F, Pant S, et al. Daraxonrasib or chemotherapy in previously treated metastatic pancreatic cancer. N Engl J Med. 2026;395(4):325–337. [doi:10.1056/NEJMoa2605555](https://doi.org/10.1056/NEJMoa2605555)

<span id="ref-7"></span>7. The ASCO Post. Elironrasib active in KRAS G12C–resistant NSCLC [Internet]. 2025 Oct 29 [cited 2026 Nov 3]. Reports the AACR-NCI-EORTC abstract LB-B024. Available from: https://ascopost.com/news/october-2025/elironrasib-active-in-kras-g12c-resistant-nsclc/

<span id="ref-8"></span>8. TheFly. Revolution Medicines: Elironrasib shows "compelling" antitumor activity in trial [Internet]. TipRanks; 2025 Oct 22 [cited 2026 Nov 3]. Available from: https://www.tipranks.com/news/the-fly/revolution-medicines-elironrasib-shows-compelling-antitumor-activity-in-trial-thefly

<span id="ref-9"></span>9. CancerNetwork. Zoldonrasib shows promising activity in KRAS G12D NSCLC [Internet]. 2026 May 12 [cited 2026 Nov 3]. Reports the AACR 2026 abstract CT021. Available from: https://www.cancernetwork.com/view/zoldonrasib-shows-promising-activity-in-kras-g12d-nsclc

<span id="ref-10"></span>10. Clopper CJ, Pearson ES. The use of confidence or fiducial limits illustrated in the case of the binomial. Biometrika. 1934;26(4):404–413. [doi:10.1093/biomet/26.4.404](https://doi.org/10.1093/biomet/26.4.404)

<span id="ref-11"></span>11. Newcombe RG. Interval estimation for the difference between independent proportions: comparison of eleven methods. Stat Med. 1998;17(8):873–890. [doi:10.1002/(SICI)1097-0258(19980430)17:8<873::AID-SIM779>3.0.CO;2-I](https://doi.org/10.1002/%28SICI%291097-0258%2819980430%2917%3A8%3C873%3A%3AAID-SIM779%3E3.0.CO%3B2-I)
