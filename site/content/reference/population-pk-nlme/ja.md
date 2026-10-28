## 定義

**母集団PK（PopPK）モデル**は、患者集団での薬物の典型的な濃度の形と、そのまわりのばらつきを表す。多くの患者のデータを合わせ（1人あたりは疎でもよい）、**非線形混合効果（NLME）モデル**で推定する。濃度がパラメータの非線形関数なので非線形、固定効果と変量効果の両方を持つので混合効果という。

## モデルの構成

- **固定効果：** パラメータの典型値（たとえばCLとV）と、体重などの共変量の効果（[共変量](allometric-scaling-covariates-ja.html)）。
- **変量効果：** パラメータの[個体間変動](inter-individual-variability-iiv-ja.html)。
- **残差誤差：** 観測値と予測値の残りの差。

## ソフトウェア

よく使われるのは、NONMEM、Monolix、nlmixr2（R）である。このサイトでは、[nimotuzumab](../writing/nimotuzumab-poppk.html)と[warfarin](../writing/warfarin-pkpd-ja.html)の解析でnlmixr2とrxode2を使い、[mosunetuzumab](../writing/mosunetuzumab-public-pk.html)のように、[公表モデルを表から再実装](poppk-reimplementation-ja.html)している。
