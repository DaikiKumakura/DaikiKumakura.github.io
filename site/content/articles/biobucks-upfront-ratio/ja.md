2026年10月、RocheとHansohが2件目の抗体薬物複合体（antibody-drug conjugate、ADC）提携を発表した。報道の見出しは「総額150億ドル超」である。しかし、Hansohが契約時に受け取るのは4億ドルで、1年後にさらに1.1億ドルを受け取る。残りの約150億ドルは、開発・承認・売上に応じたマイルストーンである ([1](#ref-1))。

製薬の提携では、見出しの総額を前払金とマイルストーンの合計で示すことが多い。条件付きの支払いは、業界の文章で「biobucks」と呼ばれることがある ([2](#ref-2))。契約時に確定するのは前払金であり、総額の大半は条件付きの支払いである。本記事は、公開されている提携18件について、前払金が総額のどれだけを占めるかを数える。

**基準日：** 本記事の事実関係と数値は、2026年10月30日時点の公開情報による。公開時点以降の契約条件の更新は反映していない。引用した資料の書誌情報の確認は2026年10月31日に行った。

## 要旨

**問題：** 前払金は見出しの総額のどれだけを占めるか。AI創薬の提携はそれ以外と異なるか。

**方法：** 2026年9〜10月を中心とする提携18件の前払金と総額を公開情報から手作業で集め、前払金が公表された15件で割合（前払金÷総額）を計算した。18件のうち、発表文書そのものを確認できたのは5件である。

**主要結果：** 前払金は総額の中央値で4.1%（四分位範囲3.3〜7.6%、範囲2.5〜18.8%）だった。15件の合計では、総額65,661百万ドルのうち前払金は3,255百万ドル（5.0%）だった。AI創薬の5件は中央値3.0%、それ以外の10件は6.1%で、これは探索的な比較である。「前払金」の定義が提携ごとに異なり、定義の選び方で割合は最大約2.2倍動いた。総額の大きさと割合の間には、15件では関係を検出できなかった。

**結論：** この標本では、前払金は総額の数%にとどまる。ただし標本は偏っており、一般の提携の基準にはならない。個別の提携の価値や将来の成否を予測するものでもない。

## 背景と目的

提携報道の総額を、契約時に確定する部分と条件付きの部分に分けて読むための参考値を得ることが目的である。標本は偏っているため、得られた割合を一般の提携の基準にはできない。個別の提携の評価や投資の判断には使わない。

## 方法

### データ

提携18件を集めた。2026年9〜10月の提携が11件、2026年1〜5月の提携が5件、2024年1月の提携が2件（Isomorphic Labsの2件）である。このうち前払金と総額の両方が公表された15件で割合を計算した。前払金が公表されていない3件（Lilly–Gate、AI Proteins–Astellas、Roche–Rona）は、割合を計算できないため除いた。提携名、日付、金額、定義、出典のURL、出典の種類は`deals.csv`に記録した（[配布資料](shared/biobucks-upfront-ratio/biobucks-upfront-ratio-companion.zip)に含む）。

AI創薬の提携は、Generate–Zealand、Insilico–Lilly、Insilico–Servier、Isomorphic–Lilly、Isomorphic–Novartisの5件とした。この分類は筆者が付けた。

出典の水準は提携ごとに異なる。2026年10月31日に、次の5件は発表文書そのものを読み、金額が`deals.csv`と合うことを確認した。Merck–SciBrunch ([3](#ref-3))、Novo Nordisk–Hengrui ([4](#ref-4))、Genentech–Alector（Alectorの提出書類 Form 8-K）([5](#ref-5))、Gilead–Vir ([6](#ref-6))、Servier–Insilico ([7](#ref-7))である。Generate–Zealandの発表文 ([8](#ref-8)) は、同日のアクセスがHTTP 403で本文を読めなかった。金額は他の報道の要約と一致することを見たにとどまる。Roche–Hansohは報道 ([1](#ref-1)) を読み、前払金、1年後の支払い、「150億ドル超」の記述を確認した。残る12件は、`deals.csv`に記録した報道やニュースレターに依拠し、原資料までは確認していない。`deals.csv`の`verified_level`列に、確認の水準（read_full、press_read、press_only）を記録した。有料の提携データベースは使っていない。

選び方に偏りがある。前払金と総額の両方が報道された提携を中心に筆者が集めたもので、取りこぼしの範囲を測っていない。小さな提携や条件が非公開の提携は含まれにくい。

### 定義と解析

- **総額：** 報道の見出しの金額で、前払金とマイルストーンの上限の合計とした。ロイヤルティは含まない。出典が前払金とマイルストーンを別々に記している場合は合計を総額にした。Roche–Hansohは前払金400、1年後の110、150億ドル超のマイルストーンから、15,510百万ドルを総額とした。「150億ドル超」のため、これは下限である。
- **前払金の割合：** 前払金÷総額。主な定義の前払金は、出典が「前払金」とする金額とした。
- **別の定義：** 出典によっては、前払金が近い時期の支払いや早期マイルストーンを含むことがある。そのような値が見つかった4件（Generate–Zealand、Gilead–Vir、BMS–Hengrui、Roche–Hansoh）は、別の定義の値も記録した。
- **群の比較：** AI創薬、売り手の国（中国企業）、総額50億ドル以上で、中央値と四分位範囲を求めた。中央値の95%区間はブートストラップ（2,000回、seed 20261030）で求めた。AI創薬群とそれ以外の群の差にはMann–WhitneyのU検定（両側）、総額（対数）と割合の関係にはSpearmanの順位相関を用いた。
- **粗いリスク調整：** マイルストーンの全額に、第1相から承認までの確率7.9%（全領域、2011〜2020年）を掛け、前払金の割合を「前払金÷（前払金＋0.079×マイルストーン）」として計算した。7.9%は、BIO・Informa Pharma Intelligence・QLS Advisorsの報告書にある全適応症の値である ([9](#ref-9), p. 10)。

解析の計画は、計算の前に固定したものではない。指標（前払金÷総額）は集める前に決めたが、AI創薬との比較、前払金の定義を変えた感度分析、承認確率による粗い補正は、データを見た後に加えた（事後）。この範囲は`analysis-plan.md`に記録した。

## 結果

### 前払金は総額の2.5〜19%で中央値は4.1%

図1は、前払金が公表された15件の割合である。

![前払金が公表された15件の、前払金の割合。割合の小さい順に並べ、橙がAI創薬、青がそれ以外。白抜きの丸は別の定義の値、点線は15件の中央値。](shared/biobucks-upfront-ratio/figures/01-upfront-share.png)

図1　前払金の割合（前払金÷総額）。縦軸は提携名（括弧内は総額、百万ドル）、横軸は前払金の割合（%）。塗りの丸は主な定義、白抜きの丸は別の定義（4件）、点線は15件の中央値（4.1%）。橙はAI創薬、青はそれ以外。n = 15。出典は`deals.csv`、作図は`figures.py`による。

表1　前払金の割合の群別の要約。

| Group | n | Median (95% interval) | IQR | Range |
| --- | ---: | ---: | ---: | ---: |
| All deals with a disclosed upfront | 15 | 4.1% (3.6–7.9%) | 3.3–7.6% | 2.5–18.8% |
| AI-discovery deals | 5 | 3.0% (2.5–4.2%) | 2.6–3.6% | 2.5–4.2% |
| Other deals | 10 | 6.1% (4.0–9.7%) | 4.0–8.6% | 2.6–18.8% |
| Chinese seller | 7 | 7.4% (3.9–11.5%) | 4.0–10.2% | 2.6–18.8% |
| Non-Chinese seller | 8 | 3.8% (2.6–4.8%) | 2.9–4.3% | 2.5–7.9% |
| Headline total of $5 billion or more | 4 | 4.0% (2.6–7.4%) | 3.6–4.8% | 2.6–7.4% |
| Headline total below $5 billion | 11 | 4.2% (3.0–8.8%) | 3.3–8.3% | 2.5–18.8% |

注：95%区間は、中央値のブートストラップ区間（2,000回）である。件数が10未満の群では区間が不安定で、5件の群の区間は範囲と一致する。4件の群の区間は参考値にとどまる。出典は`results/upfront-share-summary.csv`。

最も低いのはGenerate–Zealand（2.5%、前払金3,000万ドル、総額約12億ドル）で、Isomorphic–Lilly（2.6%）、Roche–Hansoh（2.6%）が続く。最も高いのはMerck–SciBrunch（18.8%、前払金4億ドル、総額21.3億ドル）で、Novo–Hengrui（11.5%）が続く。

AI創薬の5件は、すべて4.2%以下だった。AI創薬群とそれ以外の10件の差は、Mann–WhitneyのU検定（両側、同順位なし、厳密法）でp = 0.02（0.0193）だった。この比較は事後に決めたもので、多重性の補正はしていない。表1の群分け（AI創薬、売り手の国、総額）も事後に試した区分であり、検定は上記の1件とSpearman相関の1件だけを行った。AI創薬の5件にはプラットフォーム型の提携が含まれ、2024年の提携2件も入る。時期、開発段階、相手企業の違いは分けられていない。

売り手が中国企業の提携は、中央値が7.4%と高い。この群の割合を押し上げているのは、Merck–SciBrunch（18.8%）、Novo–Hengrui（11.5%）、Sanofi–Sino Biopharm（8.8%）である。同じHengruiの提携でも、BMS–Hengruiは3.9%と低い側にある。

総額（対数）と割合のSpearman順位相関は0.14（p = 0.63）で、この15件では関係を検出できなかった。件数が少なく、関係がないことの証拠ではない（検出力が足りない）。

図2は、横軸に総額、縦軸に前払金をとり、どちらも対数軸で表したものである。

![総額と前払金の両対数散布図。総額の2%、5%、10%、20%に当たる破線が引かれ、15件中13件が2%と10%の破線の間に入る。](shared/biobucks-upfront-ratio/figures/02-upfront-vs-total.png)

図2　総額と前払金の関係。横軸は総額（百万ドル、対数）、縦軸は前払金（百万ドル、対数）。破線は前払金が総額の2%、5%、10%、20%となる位置、橙はAI創薬、青はそれ以外。n = 15。15件中13件が2%と10%の線の間に入る。出典は`deals.csv`。

### 前払金の定義で割合は最大2.2倍動く

出典によって、「前払金」に含まれる範囲が異なる。4件で別の定義が見つかった。

表2　前払金の定義による割合の違い。

| Deal | Upfront (main definition) | Alternative definition | Headline total | Share (main → alternative) |
| --- | ---: | ---: | ---: | --- |
| Generate–Zealand | $30 million | $65 million (includes $35 million in early preclinical milestones) | about $1,200 million | 2.5% → 5.4% |
| Gilead–Vir | $90 million ($65 million cash, $25 million equity) | $135 million (includes up to $45 million in near-term preclinical milestones) | $1,870 million | 4.8% → 7.2% |
| BMS–Hengrui | $600 million | $950 million (includes near-term payments) | $15,200 million | 3.9% → 6.3% |
| Roche–Hansoh | $400 million | $510 million (includes the $110 million at the first anniversary) | $15,510 million or more | 2.6% → 3.3% |

注：BMS–Hengruiの950/15,200は6.25%で、四捨五入（0.5を切り上げ）して6.3%と表記した。Gilead–Virの現金・株式の内訳と135百万ドルの内訳は、発表文書 ([6](#ref-6)) による。Roche–Hansohの1年後の支払いは報道 ([1](#ref-1)) による。Generate–Zealandの値は、発表文 ([8](#ref-8)) を読めなかったため、報道の要約に基づく。BMS–Hengruiの950百万ドルは、報道では600百万ドルの前払金に、初年度記念と後年の条件付きの各175百万ドルを加えた額と説明されている。この内訳は原資料まで確認していない。割合は`deals.csv`の値から計算した。

別の定義を使うと、15件全体の中央値は4.1%から5.4%（95%区間3.6〜7.4%）になった。別の定義と主な定義の比の最大は約2.2倍（Generate–Zealandの65/30）だった。

主な定義の側にも、定義の揺れが残る。Insilico–Servierの32百万ドルは、発表文書では「前払金と近い時期のR&D支払いを合わせて最大32百万ドル」と書かれている ([7](#ref-7))。前払金だけの額は公表されていない。この32百万ドルを本記事は主な定義の前払金として扱ったが、他の提携で別の定義に回した「近い時期の支払いを含む」値と同じ性質である。処理が非対称であり、Servierの主な定義の割合（3.6%）は、前払金だけの割合を過大に見積もる。Menarini–Georgiamuneの45百万ドルにも同じ性質がある。報道が引用する会社の表現は「前払金と近い時期の支払いを合わせて45百万ドル」であり、本記事は主な定義の前払金として扱った（割合は4.1%）。この是正は計算に反映していない。前払金だけの額は不明なので、極端な場合として両提携の前払金を0とした臨時の確認を行った。AI創薬群の中央値は3.0%から2.6%に下がり、それ以外の群の中央値は6.1%のままで、AI創薬群が低いという向きは変わらなかった。一方でMann–WhitneyのU検定のp値は0.02から0.057に上がった。この確認は本記事の結果ファイルと配布資料に保存していない。

株式の扱いも提携で異なる。Gilead–Virでは、前払金9,000万ドルの一部（2,500万ドル）が株式である ([6](#ref-6))。現金と株式を分けて書く発表は多くない。総額の定義も出典で異なる。「マイルストーンだけ」「前払金を含む」と書かれ、ロイヤルティを除くと明記しないものもある。本記事は前払金を含む合計に揃えたが、出典の記述が曖昧な提携は残る。Gilead–Virでは、発表文書の条件を足し上げると90＋45＋1,740＝1,875百万ドルになる。本記事は報道の1,870百万ドルを使ったが、割合は小数第1位で変わらない（4.8%と7.2%）。

### マイルストーンの全額が支払われる確率は低い

総額の大半は、開発・承認・売上のマイルストーンである。マイルストーンの全額は、プログラムが承認、または承認後の売上の達成まで進んだときに支払われる。

粗い試算として、マイルストーンの全額に第1相から承認までの確率7.9% ([9](#ref-9), p. 10) を掛けると、前払金は「前払金＋リスクを調整したマイルストーン」の中央値35%（四分位範囲30〜51%）を占める。

この試算は粗い。7.9%は全領域・全薬剤の平均で、提携ごとの開発段階が違う。向きの異なる要因が混ざる。

- 前臨床の提携では、承認までの確率は7.9%より低く、マイルストーンの期待値はさらに小さくなる。前払金の割合は35%より大きくなる。
- 後期（第2相以降）の提携では、確率は7.9%より高く、前払金の割合は35%より小さくなる。
- 早い段階で支払われるマイルストーンは、確率が高い。それを7.9%で割り引くと、期待値を低く見積もり、前払金の割合を大きく見せる。

これらの要因は向きが異なるため、試算が全体として過大か過小かは言えない。35%は個別の提携の価値の推定ではない。総額をそのまま価値として読むと、条件付きの部分（中央値で約96%）を、契約時に確定する前払金と同じ重さで数えることになる、という点を示すにとどまる。

## 考察

この標本では、前払金は総額の数%だった。中央値は4.1%、合計では5.0%で、15件中13件が2〜10%に収まった（図2）。合計で見ると、総額の約95%は契約時に確定しない部分である。「総額150億ドル」という見出しの数字は、条件がすべて満たされた場合の上限を示すものである ([1](#ref-1))。

AI創薬の提携で割合が低かった（5件すべてが4.2%以下）ことは、探索的な観察である。時期、開発段階、相手企業の違いが混ざっており、5件対10件でp = 0.02という結果も、補正のない事後の比較である。AI創薬という性質が割合を下げたとは言えない。

定義の違いは、割合の比較に直接影響した。定義を変えると、15件全体の中央値は4.1%から5.4%に動き、個別の提携では最大約2.2倍動いた（表2）。同じ「前払金」という言葉が、契約時の支払いだけを指す場合と、早期マイルストーンや近い時期の支払いを含む場合がある。割合を比較するには、各提携の前払金の定義を揃える必要がある。本記事の主な定義にも、ServierやMenarini–Georgiamuneのような揺れが残る。

総額の大きさと割合の関係は、15件では検出できなかった。件数が少なく、無関係の証拠ではない。売り手が中国企業の提携で中央値が高い（7.4%）のは、少数の提携が押し上げた結果である。中国企業のライセンス条件に起因すると読む根拠は、このデータにはない。

## 限界

- **標本：** 18件（割合を計算できたのは15件）で、前払金と総額が公表された提携に偏る。提携全体の分布ではない。前払金が非公表の提携が18件中3件あったが、これは標本の中の件数であり、提携全体の率ではない。AI創薬とそれ以外の比較は探索的である。
- **出典：** 発表文書を読めたのは18件中5件で、残りは報道やニュースレター経由である（「方法」のデータ）。報道の間で数値が少し異なる提携もある（例：Lilly–Innovent）。企業の発表した値を、そのまま写している。
- **日付：** `deals.csv`の日付は、報道、提出書類、発表文書の日付で、発表日と1日ほどずれうる。Sanofi–Sino Biopharmは提出書類の日付（3月3日）で、会社の発表は現地時間3月4日とする報道がある。解析は日付を使っていない。
- **総額の意味：** 総額は、すべてのマイルストーンが達成された場合の上限である。個別の提携が実際に支払う金額、成功の確率、価値の推定ではない。
- **リスク調整：** 7.9%は全領域・全薬剤の平均であり、35%は粗い参考値である。
- **検証：** Rによる再計算は、筆者自身による別実装で、第三者の確認ではない。件数、中央値、四分位範囲、群の中央値、合計の割合、リスク調整後の中央値を検証し、差は最大3.0×10⁻⁶だった。ブートストラップ区間、Mann–WhitneyのU検定、Spearman相関のp値はRでは検証していない。本記事の執筆にはAI（Claude）を使い、同じ筆者の指示で3つのAIによる査読を受けた。人間の第三者による確認ではない。

## 結論

創薬提携の見出しの「総額」のうち、前払金は、前払金が公表された15件の標本で中央値4.1%、合計で5.0%だった。15件中13件が2〜10%に収まり、総額の大半は契約時に確定しない条件付きの支払いである。AI創薬の5件はすべて4.2%以下で、探索的に見て割合が低かった。「前払金」の定義は提携で異なり、定義の選び方で割合は最大約2.2倍動いた。総額の大きさと割合の関係は、15件では検出できなかった。標本は偏り、発表文書まで確認できたのは5件にとどまるため、これらの値を一般の提携の基準として読むことはできない。

## データとコードの公開状況

入力（`deals.csv`）、解析計画、解析コード（`analysis.py`、`test_analysis.py`、`figures.py`、`validate.R`）、結果、図は[配布資料](shared/biobucks-upfront-ratio/biobucks-upfront-ratio-companion.zip)に含めた。再実行は`python test_analysis.py && python analysis.py && python figures.py && Rscript validate.R`で行う（Python 3.12、numpy、pandas、scipy、matplotlib；R 4.5.3、jsonlite）。乱数のseedは20261030に固定した。同じseedで再実行すると、結果のファイルが一致する。Mann–WhitneyのU検定はscipyの既定（同順位がないため厳密法）で計算した。結果の「前払金の定義で割合は最大2.2倍動く」に述べた、極端な場合の臨時確認は、結果ファイルと配布資料に含めていない。単体の検査は4件で、中央値の計算、表の整合（前払金が総額より小さいこと、別の定義が主な定義以上であること、出典のURLがあること）、リスク調整後の割合が元より大きいことを確かめる。金額は出典の記載を写したもので、再配布が許可されたデータベースではない。出典の種類（公式発表、SEC提出書類、報道）は`source_type`列に記録した。

## 参照

<span id="ref-1"></span>1. Philippidis A. Roche, Hansoh launch up-to-$15B+ cancer ADC collaboration [Internet]. GEN Genetic Engineering & Biotechnology News; 2026 Oct 20 [cited 2026 Oct 31]. Available from: [https://www.genengnews.com/topics/cancer/roche-hansoh-launch-up-to-15b-cancer-adc-collaboration/](https://www.genengnews.com/topics/cancer/roche-hansoh-launch-up-to-15b-cancer-adc-collaboration/)

<span id="ref-2"></span>2. Booth B. Hitting the milestones: update on earning "biobucks" [Internet]. LifeSci VC; 2016 Dec 8 [cited 2026 Oct 31]. Available from: [https://lifescivc.com/2016/12/hitting-milestones-update-earning-biobucks/](https://lifescivc.com/2016/12/hitting-milestones-update-earning-biobucks/). The author name is taken from the site's author profile; the page text carries no explicit byline.

<span id="ref-3"></span>3. Merck & Co., Inc. Merck enters into exclusive global license agreement with SciBrunch Therapeutics for SPR2015, an investigational oral KRAS G12D (ON) inhibitor [Internet]. Merck; 2026 Sep 28 [cited 2026 Oct 31]. Available from: [https://www.merck.com/news/merck-enters-into-exclusive-global-license-agreement-with-scibrunch-therapeutics-for-spr2015-an-investigational-oral-kras-g12d-on-inhibitor/](https://www.merck.com/news/merck-enters-into-exclusive-global-license-agreement-with-scibrunch-therapeutics-for-spr2015-an-investigational-oral-kras-g12d-on-inhibitor/)

<span id="ref-4"></span>4. Novo Nordisk. Novo and Hengrui Pharma enter exclusive license agreement for once-weekly oral GLP-1/GIP dual receptor agonist HRS-1596 [Internet]. Novo Nordisk; 2026 Sep 29 [cited 2026 Oct 31]. Available from: [https://www.novonordisk.com/news-and-media/news-and-ir-materials/news-details.html?id=917052](https://www.novonordisk.com/news-and-media/news-and-ir-materials/news-details.html?id=917052)

<span id="ref-5"></span>5. Alector, Inc. Form 8-K, current report (event date 2026 Sep 30; signed 2026 Oct 5) [Internet]. U.S. Securities and Exchange Commission [cited 2026 Oct 31]. Available from: [https://www.sec.gov/Archives/edgar/data/0001653087/000119312526413090/alec-20260930.htm](https://www.sec.gov/Archives/edgar/data/0001653087/000119312526413090/alec-20260930.htm)

<span id="ref-6"></span>6. Vir Biotechnology, Inc. Vir Biotechnology enters multi-program collaboration and license agreement with Gilead Sciences to discover and develop novel PRO-XTEN dual-masked T-cell engagers for solid tumors [Internet]. Vir Biotechnology; 2026 Oct 14 [cited 2026 Oct 31]. Available from: [https://s203.q4cdn.com/628578897/files/doc_news/Vir-Biotechnology-Enters-Multi-Program-Collaboration-and-License-Agreement-with-Gilead-Sciences-to-Discover-and-Develop-Novel-PRO-XTE-EY8Z3.pdf](https://s203.q4cdn.com/628578897/files/doc_news/Vir-Biotechnology-Enters-Multi-Program-Collaboration-and-License-Agreement-with-Gilead-Sciences-to-Discover-and-Develop-Novel-PRO-XTE-EY8Z3.pdf)

<span id="ref-7"></span>7. InSilico Medicine Cayman TopCo. Voluntary announcement on multi-year collaboration with Servier for drug discovery and development in oncology [Internet]. Hong Kong Exchanges and Clearing Limited; 2026 Jan 5 [cited 2026 Oct 31]. Available from: [https://www.hkexnews.hk/listedco/listconews/sehk/2026/0105/2026010500029.pdf](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0105/2026010500029.pdf)

<span id="ref-8"></span>8. Generate Biomedicines; Zealand Pharma. Generate Biomedicines and Zealand Pharma enter collaboration and license agreement to develop protein therapeutics engineered with AI for metabolic diseases [Internet]. GlobeNewswire; 2026 Oct 13 [cited 2026 Oct 31]. Available from: [https://www.globenewswire.com/news-release/2026/10/13/3380182/0/en/generate-biomedicines-and-zealand-pharma-enter-collaboration-and-license-agreement-to-develop-protein-therapeutics-engineered-with-ai-for-metabolic-diseases.html](https://www.globenewswire.com/news-release/2026/10/13/3380182/0/en/generate-biomedicines-and-zealand-pharma-enter-collaboration-and-license-agreement-to-develop-protein-therapeutics-engineered-with-ai-for-metabolic-diseases.html). The full text was not read: the page returned HTTP 403 on the cited date.

<span id="ref-9"></span>9. Biotechnology Innovation Organization; Informa Pharma Intelligence; QLS Advisors. Clinical development success rates and contributing factors 2011–2020 [Internet]. Biotechnology Innovation Organization; 2021 Feb [cited 2026 Oct 31]. Available from: [https://www.bio.org/clinical-development-success-rates-and-contributing-factors-2011-2020](https://www.bio.org/clinical-development-success-rates-and-contributing-factors-2011-2020). The 7.9% value (all indications, Phase I to approval) was checked on p. 10 of a PDF copy of the report hosted by CPHI Online.
