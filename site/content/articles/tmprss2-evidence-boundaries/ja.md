計算で有望な候補が見つかったという報告と、動物や患者で効いたという報告の間には距離がある。この距離を指摘するだけなら簡単だ。難しいのは、個々の論文がその途中のどこまで進んだのかを、ひとまとめにせず読むことだ。

2026年10月にXで話題になった膜貫通型セリンプロテアーゼ2（transmembrane serine protease 2、TMPRSS2）の阻害剤研究は、その区別を考える具体例になる。酵素・細胞での実験結果がある一方、著者が報告する約29倍という改善は計算費用の比較である。「計算だけ」と片づけても、「29倍よく効く」と受け取っても、研究の評価を外す。

## 対象と確認範囲

発端は、計算による新薬候補の報告と、in vitro・in vivoでの薬効の間に隔たりがあるという[投稿](https://x.com/osYZtdWoeHsph6C/status/2115036216316055875)だった。その引用先は、分子動力学（molecular dynamics、MD）とマルコフモデルによる代表構造の選択を紹介する[投稿](https://x.com/shizuku50312776/status/2114882150172660120)で、BaraPhaSilicoの解説へリンクしている ([1](#ref-1), [2](#ref-2))。

解説が扱う原著はElezらの2025年の論文である。2026年の新しい実験報告ではない。原著本文、[原著のTable 1](https://www.nature.com/articles/s41467-025-62139-5#Tab1)、[原著のFigure 4](https://www.nature.com/articles/s41467-025-62139-5#Fig4)、解説本文を照合した。MDや実験の再実行、化合物の追加評価は行っていない ([3](#ref-3), [4](#ref-4))。

## 約29倍の分母は計算費用

原著の約29倍は、既知の阻害剤を探索する計算で、能動学習による候補選択と無作為な選択を比較した値である。酵素阻害の強さ、細胞での薬効、動物の生存期間の比ではない。資源使用時間を積算するcore hoursも、手元の時計で測る経過時間とは異なる。並列化の程度が違えば、資源量が同じでも待ち時間は変わる ([3](#ref-3))。

費用の計上範囲にも留保がある。[原著のTable 1](https://www.nature.com/articles/s41467-025-62139-5#Tab1)の表注は、印を付けた時間に受容体構造群を作る約8,000 hを含むとする。しかし、その印が付いた行に3,403.0 hなど8,000 hより小さい値がある。表示された時間と表注だけでは、準備計算をどう計上したかを整合的に読み取れない。ここでは約29倍を著者の報告値として扱い、準備費用まで監査済みの総費用比とはしない ([3](#ref-3))。

その留保を置いても、比較しようとしている対象は、指定された探索の終点へ到達する費用だ。探索を速くすることには価値がある。ただし、計算上の終点と治療上の終点は別である。候補の優先順位を効率よく決められたという結果に、患者の転帰を改善したという意味を足すことはできない。

MDの役割も一つではない。原著は複数の受容体構造を用意する処理と、候補の配置を動かして採点する処理を分けて評価している。DrugBankの既知阻害剤を探す比較では、後者の追加利益は限られ、費用が増えた。だからといって、受容体構造の集合を使う利益まで否定されたわけではない ([3](#ref-3))。

BaraPhaSilicoの解説も、29倍の比較対象と動的採点の追加費用を区別している。本件は、解説の誇張を発見したという話ではない。原著と解説の双方が書いている条件を、短いSNSの議論でも落とさず読む問題である ([4](#ref-4))。

## 細胞の結果があることと動物で効くこと

原著はBMS-262084について酵素阻害と細胞での作用を報告している。[原著のFigure 4](https://www.nature.com/articles/s41467-025-62139-5#Fig4)はその実験結果であり、ドッキング得点の図ではない。一方、この論文に動物での有効性やヒトの治療効果の評価はない ([3](#ref-3))。

この確認範囲から書けるのは、「この研究は細胞までの実験的裏付けを持つ」である。「動物では効かない」ではない。動物の結果を報告していない論文を失敗例として数えると、未評価と陰性を混ぜてしまう。逆に、細胞で作用したことを動物や患者での成功へ繰り上げてもいけない。

酵素を阻害する濃度と、生体内の作用部位で保たれる濃度は異なる量である。後者には吸収、分布、代謝、排泄が関わる。さらに、標的への作用が病態の改善へつながるかも別の問題になる。酵素・細胞での結果が正しくても、その候補が治療薬になるとは限らない。

## 同じ標的の臨床試験をどう置くか

TMPRSS2を標的とする薬剤の文脈では、カモスタットの無作為化試験が重要な比較材料になる。ACTIV-2の第II相試験では、治療を開始した216人についてカモスタット109人とプラセボ107人を比較し、症状改善までの中央値は両群とも9日だった。論文は、この条件でウイルスの消失や症状改善を速めなかったと報告している ([5](#ref-5))。

これはBMS-262084の臨床試験ではない。異なる分子、曝露、患者集団の結果から、BMS-262084も失敗すると推定することはできない。使えるのは、細胞での抗ウイルス作用と患者での利益が別々に検証されるという実例としてである。カモスタットの試験を無視すれば臨床への隔たりを過小評価し、別化合物の結果をそのまま移せば過大評価する。

ここではカモスタット試験の書誌情報と要旨の主要結果を確認した。試験間メタ解析、曝露の比較、治療効果の再推定は行っていない。

## 「なかなか効かない」の割合は分からない

元投稿への返信には、陰性結果が表に出にくいことを踏まえ、細胞で作用した候補のうち動物でも作用した割合を調べてはどうかという指摘がある。この返信自体に、その割合を計算できる候補一覧や追跡結果はない ([6](#ref-6))。

その割合を求めるには、少なくとも細胞で陽性だった候補の集合と、各候補の動物評価の実施・未実施・結果を区別した記録が必要になる。公表された成功報告だけを集めても、その集合は復元できない。未評価を陰性として分母へ入れる方法も、動物評価済みの候補だけを取り出す方法も、元の候補全体の移行率とは異なる量を数える。

したがって、今回確認した論文一本とSNSの印象から、「計算創薬は従来法より動物へ進みにくい」とは言えない。この比較には、従来法側でも同じ選択・追跡の定義が必要である。研究の個別評価と、方法全体の成功率の評価を混ぜないことが肝心になる。

同時期のRedditの開発者投稿にも、ドッキング得点は実験親和性ではなく、探索のアニメーションはMDではないという区別が明記されていた。これは道具の表示と検証された量を分ける説明の一例であり、TMPRSS2論文の独立追試や、掲示板全体の合意を意味しない ([7](#ref-7))。

## 結論

このTMPRSS2研究は、計算の順位付けから酵素・細胞での実験へ進んだ研究として評価できる。約29倍という報告も計算費用に関するもので、準備費用の計上には未解決の点がある。動物や患者での利益は、この結果からはまだ判断できない。

「細胞まで示した」と「治療薬になった」の間を埋める必要は残る。ただし、まだ埋まっていないことを、すでに失敗したことへ書き換えない。その区別を保った方が、計算の成果も限界も正確に見える。

## 参照

1. <a id="ref-1"></a> osYZtdWoeHsph6C. Comment on the gap between computational drug discovery and in vitro/in vivo efficacy [X post; Japanese]. 2026 Oct 27 [cited 2026 Nov 1]. [Original post](https://x.com/osYZtdWoeHsph6C/status/2115036216316055875). Description in English by the author.
2. <a id="ref-2"></a> shizuku50312776. Comment on representative structures from molecular dynamics and Markov models [X post; Japanese]. 2026 Oct 27 [cited 2026 Nov 1]. [Original post](https://x.com/shizuku50312776/status/2114882150172660120). Description in English by the author.
3. <a id="ref-3"></a> Elez K, Hempel T, Shrimp JH, Moor N, Raich L, Rocha C, et al. Simulations and active learning enable efficient identification of an experimentally-validated broad coronavirus inhibitor. Nature Communications. 2025;16:6949. [doi:10.1038/s41467-025-62139-5](https://doi.org/10.1038/s41467-025-62139-5).
4. <a id="ref-4"></a> BaraPhaSilico. Narrowing inhibitor candidates with computation and active learning [blog; Japanese; title translated by the author]. BaraPhaSilico. 2026 Oct 23 [updated 2026 Oct 24; cited 2026 Nov 1]. [Article](https://baraphasilico.com/articles/tmprss2/).
5. <a id="ref-5"></a> Jilg N, Chew KW, Giganti MJ, Daar ES, Wohl DA, Javan AC, et al. One Week of Oral Camostat Versus Placebo in Nonhospitalized Adults With Mild-to-Moderate Coronavirus Disease 2019: A Randomized Controlled Phase 2 Trial. Clin Infect Dis. 2023;77(7):941–949. [doi:10.1093/cid/ciad342](https://doi.org/10.1093/cid/ciad342).
6. <a id="ref-6"></a> nosuz. Comment on publication bias and the denominator of in vitro-to-in vivo translation [X reply; Japanese]. 2026 Oct 28 [cited 2026 Nov 1]. [Original reply](https://x.com/nosuz/status/2115368877425348689). Description in English by the author.
7. <a id="ref-7"></a> MolDesign. I'm developing a free molecular docking application with AutoDock Vina, reproducible workflows, and 3D visualization [Reddit post]. r/comp_chem. 2026 Oct 23 [cited 2026 Nov 1]. [Discussion](https://www.reddit.com/r/comp_chem/comments/1xd4kvn/im_developing_a_free_molecular_docking/).
