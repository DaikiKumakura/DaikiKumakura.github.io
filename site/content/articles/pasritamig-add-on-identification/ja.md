パスリタミグとJNJ-9401の第I相試験では、推奨レジメンの15人中11人で前立腺特異抗原（PSA）が50%以上低下した（PSA50） ([1](#ref-1))。JNJ-9401は前立腺特異的膜抗原（PSMA）とCD28を結ぶ共刺激薬である。ここで知りたいのは、併用で何人が反応したかに加えて、パスリタミグを同じ条件で単独投与した場合から何ポイント変わるかだ。

## 単群の率には比較対象が入っていない

共通の評価期間と評価規則を固定した対象集団で、併用のPSA50率を $p_1$、単剤の率を $p_0$ とする。求める差は $p_1-p_0$。11/15を $p_1$ の点推定値として扱うと、単剤情報がない場合の差は−26.7〜+73.3ポイントまで取り得る。これは点推定値に条件付けた計算。二項のWilson 95%信頼区間は併用率につき48.0〜89.1%であり、追加薬の効果を決める単剤率の情報は含まない。

**表1.** 単剤のPSA50率を仮定したときの併用との差。

| Assumed monotherapy PSA50 | Combination minus monotherapy |
| ---: | ---: |
| 40.0% | +33.3 pp |
| 60.0% | +13.3 pp |
| 80.0% | −6.7 pp |

表1のように単剤率を60%と仮定すると13.3ポイント増だが、80%なら6.7ポイント減る。別の単剤コホートを足す場合も、治療歴、PSA確認の時期、測定できなくなった患者の扱いが揃わなければ、この差に選択や測定の影響が混ざる。

第III相KLK2-comPASの第2部は、パスリタミグ単剤、JNJ-9401併用、プラセボの3群に無作為割付する ([2](#ref-2))。この設計には追加薬を比べる同時対照がある。主要評価項目は全生存期間であり、PSA50への寄与を判断するには、共通の評価規則による単剤群と併用群の結果が要る。

## データとコードの公開状況

[再計算用ZIP](shared/pasritamig-add-on-identification/companion.zip)にPythonコードと出力を収録した。

## 参照

1. <a id="ref-1"></a> [Johnson & Johnson. Johnson & Johnson reports 73% PSA response rate with investigational pasritamig-based immunotherapy combination in advanced prostate cancer [press release]. 2026 Nov 9.](https://www.jnj.com/media-center/press-releases/johnson-johnson-reports-73-psa-response-rate-with-investigational-pasritamig-based-immunotherapy-combination-in-advanced-prostate-cancer)
2. <a id="ref-2"></a> [Johnson & Johnson. KLK2-comPAS phase 3 trial design [conference poster]. ESMO 2026. Abstract 2388eTiP. Figure 2.](https://www.jnjmedicalconnect.com/media/attestation/congresses/oncology/2026/esmo/klk2compas-a-phase-3-randomized-doubleblind-placebocontrolled-study-of-a-p.pdf)
