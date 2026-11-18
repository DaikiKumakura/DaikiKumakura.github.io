HARMONiでは、第三世代EGFRチロシンキナーゼ阻害薬後に進行した、EGFR変異陽性の非扁平上皮非小細胞肺がんでイボネスシマブと化学療法の併用を、プラセボと化学療法と比較した。無増悪生存期間（PFS）の中央値は6.8対4.4か月、全生存期間（OS）は16.8対14.0か月だった。OSの主解析のハザード比は0.79（95%信頼区間0.62–1.01）だった ([1](#ref-1))。PFSの改善がOSへどこまで届くかを考えるため、進行後の生存が両群で共通の仮想モデルを作った。

## 進行後の分布を固定する

全例で死亡は進行後に起こると仮定する。進行までの時間と進行後から死亡までの時間は、それぞれ独立な指数分布で、率を $a,b$ とする。OSの生存関数はその和から $[b e^{-at}-a e^{-bt}]/(b-a)$ になる。まず対照群PFSの4.4か月から $a$ を、対照群OSの14.0か月から $b$ を決める。次に $b$ を保ったまま、治療群ではPFSの6.8か月に合わせた。これは群ごとの公表中央値に合わせた計算で、患者個票の適合や検定ではない。

**表1.** 進行後の生存分布を共有するかどうかで比較した中央値（月）。

| Scenario | Control post-progression | Treatment post-progression | Treatment OS |
| --- | ---: | ---: | ---: |
| Shared rate | 7.32 | 7.32 | 17.10 |
| Separate rates calibrated to the two OS medians | 7.32 | 7.08 | 16.80 |

表1の共有モデルで治療群OSの中央値は17.10か月。公表値16.8か月との差は0.30か月だった。単純な条件下では、進行後の率を変えなくても観測されたOS中央値に近づく。各群を別々に合わせた場合の進行後中央値7.32と7.08か月は、中央値の単純な引き算とも一致しない。

実際のPFSでは進行前の死亡もイベントになる。後治療、進行前死亡、非指数型の生存を分けるには、イベント順と対応する時刻が要る。この計算は進行後の治療効果を推定しておらず、公表試験の統計解析も置き換えない。2026年6月カットオフの事後解析では、OSハザード比が0.76（95%信頼区間0.61–0.95）に変わった一方、両群の中央値は同じだった ([2](#ref-2))。中央値を入力とする本稿の計算結果も変わらない。

## データとコードの公開状況

[再計算用ZIP](shared/harmoni-pfs-os-transition/companion.zip)にPythonコードと出力を収録した。

## 参照

1. <a id="ref-1"></a> [Le X, Passaro A, Zhao Y, Huang Y, Laskin J, Rodriguez-Abreu D, et al. Ivonescimab plus chemotherapy versus placebo plus chemotherapy in patients with advanced EGFR-mutated non-small-cell lung cancer after disease progression on EGFR tyrosine kinase inhibitor therapy (HARMONi). Lancet Oncol. 2026;27(9):1094–1109.](https://doi.org/10.1016/S1470-2045(26)00282-2)
2. <a id="ref-2"></a> [Summit Therapeutics Inc. Updated HARMONi data presented at WCLC 2026 [Form 8-K exhibit]. 2026 Sep.](https://www.sec.gov/Archives/edgar/data/1599298/000159929826000081/a2026_prx0915xharmoniltf.htm)
