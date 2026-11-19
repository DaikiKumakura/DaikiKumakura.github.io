## 要旨 {#article-abstract}

国際医薬品規制調和会議（ICH）のM15ガイドライン（モデルを用いた医薬品開発）は、モデル影響度と誤判断の帰結を評価し、そこからモデルリスクを導くことを開発者に求め、モデルの評価はそのリスクに見合うべきだとしている ([1](#ref-1))。本稿では、これらの評価要素を、真値が分かる3つの用量選択の数値解析に当てはめた。重症度がクリアランスを左右するときに2用量のうち1つを選ぶプールした曝露反応モデル、Gompertz型の腫瘍に指数増殖を当てはめた腫瘍増殖抑制モデル、疎な採血にRのnlmeパッケージで当てはめた母集団薬物動態（PK）モデルである。それぞれで、どの確認が失敗を捉えたかを調べた。重症度がクリアランスを左右するとき、プールしたモデルは、ほぼ平坦な反応の2,000試験のうち、1群40例で正しい用量を選んだのは25.4%にとどまった。曝露の傾きが有意だった割合は、1,000試験のうち55.2%だったが、モデルによる増分を無作為化した群間の差と比べる確認が警告したのは10.5%だった。腫瘍増殖では、指数モデルとGompertzモデルを赤池情報量規準（AIC）で比べると、9設定のうち8設定で約96%以上の試験がGompertzモデルを選んだが、ほぼ指数的な場合の14日試験では46.0%だった。40例の疎な母集団PKモデルでは、2点採血で典型的な吸収速度定数が29.4%過小に推定され、収束警告のない当てはめでも同じ偏りが残った。これらの数値実験では、評価が確認の感度を決めたわけではなく、私が作り込んだ失敗を警告したのは、モデルを独立した情報やより豊かな構造と比べる確認で（10.5%〜100%の試験）、収束、標本内の有意性、窓内の当てはめは警告しなかった。この感度は、各ケースで設定した単一の失敗の型と効果の大きさに条件付きであり、評価は結果が分かった後に付けた私自身のもので、規制上の評価ではない。

## 背景と目的 {#article-introduction}

ICH M15ガイドラインは、2026年1月29日にStep 4で採択され、米国食品医薬品局は2026年6月3日に最終版のガイダンスとして告知した ([1](#ref-1), [2](#ref-2))。モデルを用いた医薬品開発（MIDD）の根拠を評価する枠組みを定め、問い・使用目的・モデル影響度・誤判断の帰結を記述し、後の2つを低・中・高で評価して根拠を示し、そこからモデルリスクを導く ([1](#ref-1), Section 2.1)。ガイドラインは、モデルの評価が、現在受け入れられている標準を満たし、モデルリスクに見合うべきだと述べる ([1](#ref-1), Sections 2.1.5 and 3)。ある評価の結果が評価の内容に何を意味するかは、解析者と審査者に委ねられている。

本稿は、評価要素の評価を出発点とし、そのような評価が含みうる確認が何を見つけるかを調べる。**真値が分かる3つの用量選択の解析について、M15の評価要素はモデルリスクをどう示し、シミュレーションが明らかにした失敗は、どの評価の段階で捉えられるか。** 数値実験は別の問いのために実行し、別の記事で説明している ([3](#ref-3)–[5](#ref-5))。ここでは、真値が利用できるケースとして再利用し、確認を、問題を警告した頻度で採点する。

## 対象と確認範囲 {#article-scope}

M15の最終版 ([1](#ref-1)) を読み、特にSection 2.1（重要な評価要素）、Section 2.2（技術的基準と適切性）、Section 3（モデルの評価）、Section 4.1（モデル解析計画）を参照し、米国の告知の書誌はFederal Registerから取った ([2](#ref-2))。ガイドラインが作成中としているICHの補足の研修資料（[1](#ref-1), footnote 5）は読んでおらず、規制当局がこれらのケースをどう評価するかは分からない。表1の評価は私のもので、仮定した結果を持つ数値実験の設定に対するものであり、数値実験を実行して結果が分かった後に付けたため、事後の評価である。モデル影響（Section 2.1.6）は、開発計画に対するモデルの効果に関するもので、模擬した解析では生じないため、本稿では評価しない。

3つのケースは、私自身の数値実験である ([3](#ref-3)–[5](#ref-5))。数値は、それらの解析の結果ファイルから取り、データとコードの公開状況に示した。それらの解析が記録していなかった2つの確認を、本稿のために計算した。ケース1では、曝露反応モデルの標本内の確認と群間の差との比較（1セルあたり1,000試験、シード20261124）、ケース3では、完全なランダム効果モデルと簡略モデルの尤度比較（1セルあたり200試験、シード20261125）である。各数値実験は、パラメータが既知の患者集団または動物試験なので、確認は、問題を警告した試験の割合で採点する。

## 4つの問いの評価 {#article-ratings}

M15は、問いごとに別の評価表を用いることを勧める ([1](#ref-1), Section 2.1.1)。ケース2には、効力の順位づけと、試験期間を超える予測という2つの問いがあるため、4行になる（表1）。モデル影響度は、他の根拠に対するモデルの結果の重みで評価され ([1](#ref-1), Section 2.1.3)、モデルが決定の唯一の根拠のとき、一般に高い。誤判断の帰結は、負の影響の重大さと起こりやすさを考慮する ([1](#ref-1), Section 2.1.4)。モデルリスクは、その2つから導かれ、2つが異なるときは、より影響の大きい方に従いうる ([1](#ref-1), Section 2.1.5)。

**表1.** 本稿での評価要素の評価（評価は著者のもので、模擬した設定に対するもの）。

| Case | Question of interest | Context of use | Model influence | Consequence of wrong decision | Model risk |
| --- | --- | --- | --- | --- | --- |
| 1. Exposure–response | Which of two doses (relative 1 and 2) to take forward after a randomized trial with 20 to 100 patients per arm | Pooled logistic exposure–response model predicts response and toxicity at each dose; the arm contrasts of the same trial are also available | High (the model-based rule decides; the arm contrasts of the same trial are available, so medium to high would also be defensible) | High (in the near-plateau setting the high dose adds about 0.03 response and raises toxicity from 0.10 to 0.16, with the likelihood of the wrong choice shown below) | High |
| 2a. Tumour growth, potency | Which concentration gives half of the maximal kill rate | Growth inhibition model fitted to a 14- to 28-day xenograft study; used to rank compounds | Medium (other assay evidence is expected) | Low (a ranking, revisited with later data) | Low |
| 2b. Tumour growth, projection | What treated-to-vehicle volume ratio a concentration inside the tested range gives at day 28 | Same model, used to project beyond the study window | High (the study does not observe day 28 when it lasts 14 or 21 days) | Medium (a compound may be advanced or dropped on the projection) | High (follows the model influence, which is the more influential element) |
| 3. Population PK | Do typical CL, V and ka and their variability, from 20 to 80 subjects with 2 to 6 samples each, support dosing simulation | nlme fit with random effects on CL, V and ka (or CL and V) | Medium (later studies or dense data would normally be available) | Medium (an exposure miss that a later dose adjustment can correct) | Medium |

CL、クリアランス。V、分布容積。ka、吸収速度定数。PK、薬物動態。

## ケース1 プールした曝露反応モデルと無作為化した群間の差 {#article-case1}

ほぼ平坦な設定では、高用量の真の反応の増分は約0.03で、境界の0.08を下回るため、正しい用量は低用量である。交絡がないとき、プールした曝露反応モデルが正しい用量を選んだのは、2,000試験のうち1群40例で73.8%、100例で83.8%で、群ごとの反応率を使う規則では71.5%と74.7%だった。重症度がクリアランスを左右するとき（重症度1SDあたりクリアランスが49%高い、仮定）、モデルが正しい用量を選んだのは25.4%と11.9%で、群の規則は73.0%と77.0%だった ([3](#ref-3))。当てはめた曝露の傾きは平均0.87（真値0.2）で、真の重症度を加えると0.23になった ([3](#ref-3))。

どの確認がこれを見たか。標本内の確認はモデルを支持した。曝露の傾きの尤度比検定は、交絡があるとき、1群40例の55.2%、100例の89.9%の試験で有意で、交絡がないときは6.9%と10.8%だった（表2）。データは、用量の判断に関する限り、大部分が重症度である曝露反応関係を支持するように見えた。群ごとの当てはめた反応率と観測した反応率の一致は、全群で最大の差が0.02以内だった割合が、交絡のある試験で23.3%（1群40例）と13.5%（100例）、交絡のない試験で42.4%と61.9%だった。100例では、この確認は2つの設定を区別したが、偽の警告が多く（交絡のない試験の38.1%が0.02を超え、交絡のある試験では86.5%）、閾値0.02は恣意的である。傾きの検定と群間差との比較は、別の問いに答える。前者は曝露が反応を予測するかを、後者はモデルによる増分が無作為化した群間差と一致するかを問う。

区別できた確認は、モデルによる増分を、モデルが傾きに使わない情報である無作為化した群間の差と比べるものである。差が群間差の標準誤差の1.96倍を超えたのは、交絡のある試験の10.5%（1群40例）と26.5%（100例）、交絡のないときは0.2%と0.5%だった。偽の警告はほとんど出さず、問題を検出できたのは少数の試験だった。群間差の標準誤差は、モデルによる増分と群間差が同じデータ由来であることを無視するため、この規則は保守的で、感度は下限である。モデルと群の規則が反応の増分が0.08に達するかで食い違ったのは（ここでは用量選択の解析の毒性上限を課していない）、交絡のある試験の49.1%と65.1%で、正式な警告より食い違いははるかに多かったが、交絡のない試験でも17.8%と16.8%で同じ食い違いが起きたため、どちらが誤りかは特定できない。

**表2.** ほぼ平坦な設定（真の反応の増分約0.03）。2つの規則の正しい用量の割合は用量選択の解析 ([3](#ref-3)) から（1行あたり2,000試験）、曝露反応モデルの確認は本稿から（1行あたり1,000試験）。

| Condition | Patients per arm | Correct dose, arm rule | Correct dose, E–R model | E–R slope significant | Model gain differs from arm contrast by more than 1.96 SE | Model and arm rule differ on a gain of at least 0.08 |
| --- | --- | --- | --- | --- | --- | --- |
| No confounding | 40 | 71.5% | 73.8% | 6.9% | 0.2% | 17.8% |
| No confounding | 100 | 74.7% | 83.8% | 10.8% | 0.5% | 16.8% |
| Severity drives clearance | 40 | 73.0% | 25.4% | 55.2% | 10.5% | 49.1% |
| Severity drives clearance | 100 | 77.0% | 11.9% | 89.9% | 26.5% | 65.1% |

E–R、曝露反応。SE、標準誤差。最後の列は、反応の増分の基準だけを適用し、毒性上限は適用していない。

M15は、主要な仮定を特定して根拠を示し、代替を検討し、頑健性を評価することを求め、独立したデータでの外部検証が場合により不可欠になりうると述べる ([1](#ref-1), Section 3)。ここで重要な代替は、重症度の指標を含むモデルであり、誤差のある重症度指標を加えた版は、1群40例で、正しい用量の割合を25.4%から52.2%に上げたが、群の規則を下回った ([3](#ref-3))。モデル影響度が高く誤判断の帰結も高い（表1）場合、私は独立した情報との確認を求める。無作為化した群間の差は、同じ試験の情報であり外部検証ではなく、試験内で使える最も感度の高い確認だったが、これらのサンプルサイズでは検出力の低いものだった。

## ケース2 投影する期間とともに不一致が広がる増殖モデル {#article-case2}

溶媒対照の腫瘍がGompertz型に増殖するとき、指数増殖モデルは半数最大濃度を回収し（すべての設定で中央値2.99〜3.01）、最大殺傷率を過小に推定した（Gompertz速度0.05で、14・21・28日の順に0.153、0.135、0.121/日、真値0.20）([4](#ref-4))。検討範囲内の濃度での処理群と溶媒群の体積比の予測は、28日目で、これらの期間の順に真の比の0.459、0.619、0.784倍で、最終観測日では0.930、0.863、0.784倍だった ([4](#ref-4))。

問いによって、どれが重要かが決まる。効力の順位づけ（表1の2a）では、指数モデルが半数最大濃度を回収したことが重要で、低いモデルリスクは結果と整合する。予測（2b）では、評価は期間を覆う必要がある。14日後の最終観測日での指数モデルの窓内の誤差は中程度だったが（真の比の0.930倍）、28日目への予測は半分以上外れた（0.459倍）（表3）。観測した窓内の当てはめでは、データが届かない期間へのモデルの適用可能性を覆えない。M15は、モデルとデータの全体的な比較である妥当性と、それぞれの使用に対するデータとモデルの適切さに関する適用可能性の評価を区別する ([1](#ref-1), Section 3)。

より豊かなモデルとの比較は、ほとんどの設定で感度が高かった。AICは、Gompertz速度0.05で、14日後の98.8%、21日と28日後の100%の試験でGompertzモデルを選び、速度0.10では3つの期間すべてで選んだ ([4](#ref-4))。ほぼ指数的な場合（速度0.02）では、14日後の46.0%、21日後の96.0%の試験だった（表3）。残差平方和の中央値は、速度0.05・14日後でGompertzモデルが6.4%低いだけ（5.43対5.80）、28日後に33.1%低く（9.23対13.79）([4](#ref-4))、窓内の当てはめの観察だけでは、予測の誤差の大きさは示されなかっただろう。速度0.02・14日の試験は、確認が問題を見逃す一方で、28日目の予測が真の比の0.641倍になっている例である。

**表3.** Gompertz型の腫瘍に指数増殖モデルを当てはめた結果。増殖モデルの解析 ([4](#ref-4)) から、1行あたり2,000試験（9設定のうち5設定。Gompertz速度0.10の設定と速度0.02の28日試験は、元の解析にある）。最大殺傷率（真値0.20/日）、検討範囲内の濃度での処理群と溶媒群の体積比の予測値を真の比で割った値、AICがGompertzモデルを選んだ試験の割合。

| Gompertz rate (per day) | Duration (days) | Maximal kill rate | Predicted / true ratio, last observation day | Predicted / true ratio, day 28 | AIC prefers Gompertz |
| --- | --- | --- | --- | --- | --- |
| 0.05 | 14 | 0.153 | 0.930 | 0.459 | 98.8% |
| 0.05 | 21 | 0.135 | 0.863 | 0.619 | 100.0% |
| 0.05 | 28 | 0.121 | 0.784 | 0.784 | 100.0% |
| 0.02 | 14 | 0.179 | 0.965 | 0.641 | 46.0% |
| 0.02 | 21 | 0.170 | 0.921 | 0.750 | 96.0% |

AIC、赤池情報量規準。

## ケース3 省いたランダム効果を重要な場面で見ない尤度比較 {#article-case3}

40例の1コンパートメント経口モデルにnlmeを当てはめたとき、典型的な吸収速度定数は、1人2点で29.4%、6点で6.9%過小に推定され、VのランダムSDがゼロと推定された割合は41.0%と1.8%だった ([5](#ref-5))。推定に関する2つの警告が使えた。nlmeは、2点の97.5%の試験で当てはめを返したが、収束の警告のない当てはめは46.3%だけだった。警告のない当てはめに限っても、偏りは残り（典型的なkaは2点で−29.3%、6点で−7.3%）（表4）、収束の警告は、信頼できない当てはめを示すが、偏りのある当てはめを特定しない。M15は、検証を、コード・式・計算が正しいことの確認と定義する ([1](#ref-1), Section 3)。実装が正しくても、小標本では偏りのある推定量が得られうるが、検証はそれを扱わない。収束の警告と曝露の傾きの有意性は、この意味の検証ではなく、推定と当てはめの診断である。

その解析で調べた構造の誤指定は、データ生成モデルが含んでいたkaのランダム効果を省くことだった。その簡略モデルでは、典型値は悪化せず、残差SDが23.5%〜31.0%、VのランダムSDが18.8%〜29.0%過大に、40例で推定された ([5](#ref-5))。そのため、典型値だけを見る読者は、気づかない。完全モデルと簡略モデルの尤度比較（AIC）が、データ生成の構造を持つ完全モデルを選んだのは、1人2点の200試験の30.6%、3点で82.0%、4点で99.5%、6点で100%だった（表4）。2点では、比較は、正しいモデルより誤ったモデルを選ぶことの方が多く、両方の当てはめが収束警告なしだった試験は26.5%にすぎなかった（その53試験のうち完全モデルを選んだのは30.2%）。1人2点では、3つのランダム効果が1人あたりの観測数を上回り、完全モデルのSDが境界に潰れることが多く、AIC差の中央値は−2.0にとどまったため、そこでの比較は成立していない。省いたことを検出する確認には、1人3〜4点が必要で、典型値の偏りは、3点ですでに大きかった（典型的なka −20.1%）。

**表4.** 40例の母集団PKモデル。2列目から6列目は、nlmeの解析 ([5](#ref-5)) から、1行あたり400試験。7列目と8列目は、本稿から、1行あたり200試験。

| Samples per subject | nlme returned a fit | Fit without a convergence warning | Typical ka, median error | Typical ka, median error, fits without a warning | SD of the random effect on V estimated at zero | AIC prefers the full model | Both fits free of warnings |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 97.5% | 46.3% | −29.4% | −29.3% | 41.0% | 30.6% | 26.5% |
| 3 | 100.0% | 55.7% | −20.1% | −20.3% | 19.2% | 82.0% | 54.0% |
| 4 | 100.0% | 84.5% | −11.7% | −11.5% | 5.5% | 99.5% | 81.0% |
| 6 | 100.0% | 92.2% | −6.9% | −7.3% | 1.8% | 100.0% | 94.5% |

ka、吸収速度定数。SD、標準偏差。AIC、赤池情報量規準。

![独立した情報やより豊かな構造との確認が問題を警告した、模擬した試験の割合](shared/ich-m15-model-risk-dose-analyses/figures/figure-1-checks.png)

**図1.** モデルを独立した情報やより豊かな構造と比べる確認が問題を警告した、模擬した試験の割合：モデルによる増分と無作為化した群間の差の食い違い（パネルA、点あたり1,000試験）、AICがGompertzモデルを選んだ割合（パネルB、点あたり2,000試験）、AICが完全なランダム効果モデルを選んだ割合（パネルC、点あたり200試験）。AIC、赤池情報量規準。

## 評価が定めたことと残したこと {#article-discussion}

3つのケースのすべてで、評価は、M15が期待する評価の深さに関わるもので、確認の感度に関わるものではなかった。M15は、ある評価にどの確認が対応するかを定めていない。私の判断では、リスクの高いケースの評価は、モデルを独立した情報やより豊かな構造と比べる確認を含むべきだった。ケース1の無作為化した群間の差、ケース2のより豊かな増殖モデル、ケース3の完全なランダム効果モデルである。その感度は、図1の設定で10.5%から100%に及び、データの情報量を決める設計の変数、すなわち群あたりの例数、試験期間、1人あたりの採血数に依存した。標本内の確認（収束、曝露の傾きの有意性、窓内の当てはめ）は、推定と当てはめの診断であり、M15の意味の検証（コードと計算が正しいこと）ではなく、失敗を区別できなかった。それらは、絶対的な失敗が最大の場面で最も安心させるものだった。100例の交絡のある試験の89.9%で曝露の傾きは有意で、モデルが正しい用量を選んだのは11.9%だった。この感度は、各ケースで私が作った単一の失敗の型と、選んだ効果の大きさに条件付きである。

M15の2つの特徴が、この結果に直接関わる。第1に、技術的基準とモデルの評価は、モデル解析計画で事前に定められるべきで、「事前に定める」とは、データにアクセスする前、または解析を行う前に文書化することを意味する ([1](#ref-1), Section 4.1 and footnote 10)。「モデルによる増分が群間差と標準誤差の1.96倍以内で一致しなければならない」という基準は、事前にしか設定できず、1群40例では、交絡のある試験の89.5%で満たされたはずで、そこでモデルが正しい用量を選んだのは25.4%だった。第2に、ガイドラインは、モデルリスクを、特定の問いに対するモデルの結果の性質とし、方法に固有のものとは見ない ([1](#ref-1), Section 2.1.5)。腫瘍増殖モデルの2行がそれを示す。同じ当てはめが、効力の順位づけでは低いリスク、予測では高いリスクを持ち、前者に合う評価は、後者を明らかにしない。

ケースは、評価が誤解を招きうる場面も示す。母集団PKモデルの中程度の評価（表1）は、後のデータや用量調整が曝露の外れを補えるという仮定に基づくが、1人2〜3点で得られた典型的なkaの20%〜29%の誤差を、後の用量調整が補うかは検証していない。ケース1の帰結の評価は、仮定した反応率と毒性率から判断したもので、毒性の重さが異なれば変わる。

### 限界

評価と、確認の感度は、模擬した設定と、影響度と帰結に関する私の判断に当てはまる。規制当局や学際チームは異なる評価をしうるし、M15は、2つの評価から3つ目を導く規則を定めていない。ケースは、真値のある数値実験なので、割合は、私が作った誤指定に対する確認の感度であり、実際の誤指定は分からず、規制上の判断は伴わなかった。比べた確認は選んだものであり、他の診断（視覚的予測確認、残差プロット、標準誤差、シュリンケージ）は計算していない。ケース1は、確認に1セルあたり1,000試験、用量選択の結果に2,000試験を使い、割合は別の乱数による（確認はシード20261124）ため、表2の2組の列は対応していない。ケース3の尤度比較は、1セルあたり200試験で、モンテカルロ標準誤差は約0.035である。標本内の群ごとの反応率の一致の確認は閾値0.02を使い、標準誤差の1.96倍の規則は、本稿で選んだ記述用の規則であり、規制上の基準ではなく、保守的である。M15の基準と評価は、実際の使用目的について評価者と事前に合意されるが、模擬したケースにはそれが存在しないため、評価要素を当てはめることは、枠組みを例示するものであり、検証するものではない。私が読んだのはガイドラインと告知だけで、補足の研修資料や規制当局の運用は利用できなかった。

## 結論 {#article-conclusion}

M15の評価要素を、3つの数値実験の用量選択の解析に当てはめると、曝露反応モデルのモデルリスクは高く、母集団PKモデルは中程度、腫瘍増殖モデルのリスクは問いによって異なった（効力では低く、予測では高い）。失敗を警告した確認は、モデルを独立した情報やより豊かな構造と比べるもので、その感度は、群あたりの例数、試験期間、1人あたりの採血数によって、10.5%から100%の試験に及び、収束、標本内の有意性、窓内の当てはめの確認は、最も大きな失敗を警告しなかった。結論は、私が設定した失敗の型と効果の大きさ、および私自身の事後の評価に限られる。

## データとコードの公開状況 {#reproduce}

患者や動物のデータは使っていない。付属の配布物には、本稿のために書いた2つのスクリプト（`check_er_checks.R`と`check_nlme_aic.R`）、図の作成（`figures.R`）、その結果（`results/er-checks.csv`、`results/nlme-aic.csv`、`results/nlme-aic-raw.csv`）、セッション情報を含む。スクリプトは、3つの元の解析の定義と結果を読む。それらの付属配布物は各記事からリンクされている ([3](#ref-3)–[5](#ref-5))。`check_er_checks.R`は用量選択の解析のデータ生成コード（`simulate.R`、シード20261117）、`check_nlme_aic.R`は母集団PKの解析のもの（`simulate.R`、シード20261123）、`figures.R`は増殖モデルの解析の結果を読む。新しい計算のシードは20261124（`Rscript check_er_checks.R 1000`、1分未満）と20261125（`Rscript check_nlme_aic.R 200`、11のワーカープロセスを使うデスクトップPCで約8分）である。表の数値は、4つの解析の結果ファイルで照合できる。

[付属配布物のダウンロード（コードと集計結果）](shared/ich-m15-model-risk-dose-analyses/ich-m15-model-risk-dose-analyses-companion.zip)

## 参照 {#article-references}

1. <span id="ref-1"></span>International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use. M15: general principles for model-informed drug development [Internet]. ICH harmonised guideline, final version, adopted 29 January 2026 [cited 2026 Nov 19]. Available from: [ICH M15 Step 4 guideline](https://database.ich.org/sites/default/files/ICH_M15_Step4_Final_Guideline_2026_0129.pdf)
2. <span id="ref-2"></span>Food and Drug Administration. M15 general principles for model-informed drug development; International Council for Harmonisation; guidance for industry; availability. Fed Regist. 2026 Jun 3;91:33179. Docket No. FDA-2024-D-5580. [Federal Register document 2026-11112](https://www.federalregister.gov/documents/2026/06/03/2026-11112/m15-general-principles-for-model-informed-drug-development-international-council-for-harmonisation)
3. <span id="ref-3"></span>Kumakura D. Does exposure information help a randomized two-dose trial select the better dose? Simulated trials with and without severity-driven clearance [Internet]. Daiki Kumakura; 2026 Dec 16. Available from: [Does exposure information help a randomized two-dose trial select the better dose?](https://daikikumakura.github.io/writing/randomized-dose-selection-exposure-response.html)
4. <span id="ref-4"></span>Kumakura D. Does the growth model for vehicle tumours change what a xenograft study says about potency and efficacy? Simulated studies with Gompertz vehicle growth and an exponential-growth model [Internet]. Daiki Kumakura; 2026 Dec 18. Available from: [Does the growth model for vehicle tumours change what a xenograft study says about potency and efficacy?](https://daikikumakura.github.io/writing/tgi-growth-model-misspecification.html)
5. <span id="ref-5"></span>Kumakura D. What does nlme recover from sparse sampling in a population pharmacokinetic analysis? Simulated studies with 20 to 80 subjects and 2 to 6 samples per subject [Internet]. Daiki Kumakura; 2026 Dec 29. Available from: [What does nlme recover from sparse sampling in a population pharmacokinetic analysis?](https://daikikumakura.github.io/writing/poppk-sparse-nlme-recovery.html)
