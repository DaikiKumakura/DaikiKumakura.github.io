## 定義

**クリアランス（CL）**は、単位時間に薬物が完全に除かれる血漿の体積で、L/hやL/dayなどの単位で表す。消失速度と濃度の比例定数である。

## 何を決めるか

線形のPKでは、静注の後のAUCは用量をCLで割った値になり、定常状態の平均濃度は投与速度をCLで割った値になる。体重が大きいなど、CLを大きくするものは、固定用量での曝露を下げる。

## 抗体の場合

モノクローナル抗体は、主に異化で消失し、クリアランスには標的を介した消失（[標的介在性薬物動態](target-mediated-drug-disposition-ja.html)）も含まれうる。治療中にクリアランスが時間とともに下がる抗体もある。

## このサイトでは

再実装したpembrolizumabのモデルは、典型値が0.22 L/day、体重の指数が0.595で、nivolumabのモデルは、クリアランスが時間とともに最大で約26%下がる（[抗PD-1抗体の解析](../writing/fixed-vs-weight-dosing.html)）。[mosunetuzumabの再実装](../writing/mosunetuzumab-public-pk.html)は、時間変化するクリアランスを経験的な記述として使っている。[共変量としての体重](allometric-scaling-covariates-ja.html)も参照。
