## 定義

**Emaxモデル**は、E = E0 + Emax × C / (EC50 + C)で、Cは濃度、E0はベースラインの効果、**Emax**は最大効果、**EC50**はEmaxの半分を与える濃度である。抑える効果では、E = E0 × (1 − Imax × C / (IC50 + C))の形になる。

## Hill指数

**シグモイドEmax（Hill）モデル**は、指数γを加える。E = E0 + Emax × C^γ / (EC50^γ + C^γ)。γが大きいほど、EC50のまわりで曲線が急になる。γ = 1が単純なEmaxモデルである。

## 使い方

これらの関数は、[間接反応モデル](indirect-response-model-ja.html)や直接効果モデルで、濃度–効果の関係の形を与える。疎なデータからは、EC50やγをうまく推定できないことが多い（[実用的識別可能性](practical-identifiability-ja.html)）。

## このサイトでは

[warfarinのPK/PD解析](../writing/warfarin-pkpd-ja.html)では、最大の抑制を1に固定し、Hill指数は、個体間変動のない典型値のパラメータである。[RAS阻害薬の解析](../writing/ras-inhibitor-target-coverage-ja.html)は、薬物濃度を標的の占有の反応と結びつけている。
