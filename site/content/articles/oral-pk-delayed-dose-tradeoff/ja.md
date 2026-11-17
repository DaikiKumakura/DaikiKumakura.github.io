12時間間隔の経口薬を9時間遅れて服用すると、次の予定までは3時間しかない。初回の遅れを埋めても、次の予定を元の時刻に置くかどうかで、その後の濃度の山が変わる。ClarkとLawleyは不規則な服用を薬物動態モデルで検討した ([1](#ref-1))。ここでは二つの時間窓を分け、低濃度と高濃度をそれぞれ計算する。

## 次の予定を固定した場合と移した場合

定常状態から始める。1コンパートメントモデルで吸収速度定数を毎時1、消失半減期を8時間、1回量を見かけの分布容積で割った値を濃度の1単位とした。投与から $t$ 時間後の寄与は $k_a(e^{-kt}-e^{-k_at})/(k_a-k)$ で、投与前はゼロ。$k=log(2)/8$ とし、過去の定期投与の寄与を等比級数で求め、予定と異なる投与分を加減した。0.001時間刻みで、0時間の予定を起点とする二つの窓の極値を求めた。

**表1. 0.001時間刻みで求めた濃度の極値**

| Change to the schedule at hours 0, 12 and 24 | Minimum from hour 0 to just before hour 12 | Maximum from hour 12 through hour 24 |
| --- | ---: | ---: |
| No change | 0.599 | 1.278 |
| Skip the dose at hour 0 | 0.212 | 0.962 |
| Move the dose to hour 9 and keep hours 12 and 24 | 0.275 | 1.653 |
| Move the dose to hour 9 and continue every 12 hours | 0.275 | 1.184 |

表1の後ろ2行は0〜12時間の経過が同じだが、次を12時間に置くと後半の最大濃度は1.653で、予定どおりの約1.29倍になる。次を21時間に置くと後半の最大は1.184に下がる。一方で投与時刻は元の周期からずれる。同じ最低濃度を通る二案でも、その後のピークと予定時刻は一致しない。

この例では吸収・消失を線形とし、薬効や毒性の閾値を置いていない。各案の長期の濃度や実薬での服用判断は、この24時間の計算からは決まらない。

## データとコードの公開状況

仮想条件のみを用いた。[再現用Pythonコードと出力](shared/oral-pk-delayed-dose-tradeoff/companion.zip)を公開する。

## 参照

1. <a id="ref-1"></a> [Clark ED, Lawley SD. Should patients skip late doses of medication? A pharmacokinetic perspective. J Pharmacokinet Pharmacodyn. 2022;49(4):429–444.](https://doi.org/10.1007/s10928-022-09812-0)
