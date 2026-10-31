がん、遺伝子編集、肥満、AI創薬、異種移植などを並べた「バイオ・ブーム」型の一覧には、数値の定義が省かれた見出しが載りやすい。本記事は、そのような10の見出しを取り上げ、数値が何を測った量か、承認または開発のどの段階かを、論文の抄録、企業の発表、FDAのページ、試験登録で確かめる。問いは二つある。10項目のうち、薬・ワクチン・治療法にあたる8項目で承認されたものはいくつか。見出しの数値は公開資料の記載と合うか。承認状況は2026年10月30日時点（10月31日再確認）で記述する。全文を読めた論文は一つもなく、数値の多くは抄録、企業発表、要約ツールの抽出に基づく。

## 対象と確認範囲

10項目は、SNSで広く読まれたと伝えられる一覧の見出しを伝聞で要約したものである。その投稿自体は見つけられておらず、元の文言は不明である。「87%が発作なし」と読める書き方が投稿にあったかどうかも分からない。以下では、見出しに近い数値を公開資料がどう定義しているかだけを示す。承認状況は2026年10月30日時点で、FDAのページと試験登録は10月31日に取得して確認した。その他の項目は同日に検索で承認の報道を探し、追加の承認は見つからなかった。

確認の水準は次の5段階に分けて記録した。第1は雑誌論文の抄録で、PubMedのAPIから取得したXMLを読んだ。論文の全文は一つも読んでいない。第2は試験登録で、ClinicalTrials.govのAPIが返したレコードを読んだ。第3は企業発表の全文で、Merck・Modernaの発表はPDFから文字を抽出し、結果の節を読んだ。第4はウェブページの抽出で、FDA・企業・報道のページを、ページ取得ツールが要約して返した結果で読んだ。原文との逐語照合はしていない。第5は検索結果の抜粋で、ページ本体が取得できなかったものである。表1に項目ごとに確認できた資料の種類を示す。各数値の出所と水準は配布資料の `source-notes.md` に一覧した。

表1　10項目の確認水準と状況（2026年10月30日時点）。

| # | 見出しの要約 | 確認できた資料の種類 | 状況 |
| --- | --- | --- | --- |
| 1 | daraxonrasib、膵がん、全生存期間13.2対6.6か月 | 論文抄録 ([1](#ref-1))。FDAページの抽出 ([2](#ref-2)) | FDA承認済み（2026年8月26日） |
| 2 | 遺伝子編集、遺伝性血管性浮腫、87%と62% | 論文抄録 ([3](#ref-3))（87%）。企業発表の抽出 ([4](#ref-4))（62%） | 未承認。BLA受理・優先審査（2026年9月8日） ([5](#ref-5)) |
| 3 | 遺伝子編集でLDLコレステロール −62% | 論文抄録 ([6](#ref-6)) | 未承認（第1相） |
| 4 | 個別化mRNAワクチン、1,137例、42% | 企業発表の全文 ([7](#ref-7))。報道の抽出 ([8](#ref-8)) | 未承認。論文はNEJM掲載受理と企業が記載、未出版 |
| 5 | retatrutide、約28%の体重減少 | 企業の医療情報ページの抽出 ([9](#ref-9))。企業発表の抽出 ([10](#ref-10)) | 未承認。BLA提出は2027年第1四半期の予定 |
| 6 | rentosertib、第3相 | 試験登録 ([11](#ref-11))。第2a相の論文抄録 ([12](#ref-12)) | 未承認 |
| 7 | 発毛の飲み薬、第3相 | 企業発表の検索結果抜粋のみ（数値は未照合） ([13](#ref-13)) | 未承認 |
| 8 | dostarlimab、直腸がん、FDA承認 | FDAページの抽出 ([14](#ref-14))。試験登録 ([15](#ref-15))。論文抄録 ([16](#ref-16)) | 加速承認（2026年10月19日） |
| 9 | ブタの腎臓、271日 | 論文抄録 ([17](#ref-17))。企業発表の抽出 ([18](#ref-18)) | 未承認。拡大アクセス継続中でRESTORE試験は未開始 |
| 10 | 染色体サイズのDNAの細胞間移動 | 論文抄録 ([19](#ref-19), [20](#ref-20)) | 承認の対象ではない基礎研究 |

本文中の差や比は、特に断らない限り原資料の報告値であり、筆者が引き算をした値には「筆者計算」と付ける。

## 承認された2項目

### daraxonrasibの全生存期間

FDAは2026年8月26日、daraxonrasib（製品名Rasonque）を、少なくとも1回の全身療法を受けた、または多剤の全身療法の対象にならない成人の転移性膵腺がんに対して承認した ([2](#ref-2), [21](#ref-21))。見出しの数値は第3相RASolute 302に由来する。500例が無作為化され（daraxonrasib群248例、化学療法群252例）、91.8%がRAS G12変異を持っていた。主要評価項目は、RAS G12変異集団での全生存期間と無増悪生存期間である ([1](#ref-1))。

RAS G12変異集団の全生存期間の中央値は13.2か月対6.6か月、全体集団では13.2か月対6.7か月で、ハザード比はどちらも0.40であった ([1](#ref-1))。「6.6」と「6.7」の違いは集団の違いであり、資料間の矛盾ではない。FDAのページでは、全体集団の中央値は13.2か月（95%信頼区間 10.0から推定不能）対6.7か月（5.8から8.0）、ハザード比は0.40（0.30から0.53）である ([2](#ref-2))。1年生存率53.3%対18.7%は、報道に記載されたG12集団の値であり、抄録には載っていない ([22](#ref-22))。対照は医師選択の化学療法で、試験はオープンラベルである ([1](#ref-1))。FDAのページは、通常承認か加速承認かを記載していない ([2](#ref-2))。

### dostarlimabの臨床的完全奏効

FDAは2026年10月19日、dostarlimab（Jemperli）に、FDA認可の検査でMSI-HまたはdMMRと判定されたII期・III期の局所進行直腸がんの成人を対象とする加速承認を与えた ([14](#ref-14))。根拠はAZUR-1である。単群・オープンラベルで、前治療のない154例が治療を受けた。試験登録の区分は第2相である ([15](#ref-15))。主要評価項目は、治療終了後12か月持続する臨床的完全奏効（cCR12）である。FDAのページは、独立中央判定で47%（評価可能116例）、試験医師の判定で68%（144例）を示す ([14](#ref-14))。

二つの値は、判定者だけでなく評価可能例の範囲も異なる。独立中央判定で臨床的完全奏効に達しながら追跡が12か月に満たない例が38例（33%）あった ([14](#ref-14))。学会誌の抄録も、独立判定のcCR12は最初の奏効が確認された時点が遅く、試験医師の判定より成熟していないと記す ([16](#ref-16))。47%と68%は別々の評価であり、どちらかが誤りという関係ではない。

FDAのページには、別の試験（研究者主導の単群、50例）のcCR12 93%と奏効率100%も記載されている。これらはAZUR-1の値ではない ([14](#ref-14))。加速承認は、制度上、臨床的有用性を確かめる追加試験の実施が求められる ([23](#ref-23))。dostarlimabのページから抽出した範囲には、確認試験の記述は含まれなかった ([14](#ref-14))。追跡期間の中央値は26.3か月で、cCR12、cCR、ほぼ完全奏効に達した例に進行はなかったとFDAは記す ([14](#ref-14))。単群試験であり、標準治療との直接比較はない。

## 数値の定義が見出しの読みと異なる4項目

### 遺伝性血管性浮腫の87%と62%

第3相HAELOでは、16歳以上のC1インヒビター欠乏性遺伝性血管性浮腫の80例が、lonvo-z 50 mgの1回投与（52例）またはプラセボ（28例）に割り付けられた。追跡期間の中央値は7.5か月（範囲4.9から12.8）である。投与後5週から28週の月あたり発作回数（最小二乗平均）は0.26（95%信頼区間 0.15から0.45）対2.10（1.55から2.86）で、相対差は−87%（−93から−78）であった ([3](#ref-3))。87%は発作回数の減少率であり、発作がなかった患者の割合ではない。

発作がなく、かつ長期予防療法もなかった患者は、6か月の評価期間でlonvo-z群62%、プラセボ群11%と企業の発表は記す ([4](#ref-4))。この値は論文の抄録には含まれず、論文の全文は読めていないため、企業発表の抽出に基づく値として扱う。抄録は、lonvo-z群で重篤な有害事象とグレード3以上の有害事象がなかったことを記す ([3](#ref-3))。FDAはBLAを2026年9月8日に受理し、優先審査としてPDUFA目標日を2027年3月10日とした。諮問委員会の開催は現時点で予定されていない ([5](#ref-5))。追跡が中央値7.5か月の1回投与療法であり、効果の持続は今回の資料から判断できない。

### LDLコレステロール −62%

VERVE-102の第1相は非盲検の単回投与漸増試験で、ヘテロ接合性家族性高コレステロール血症または早発冠動脈疾患の成人に、0.3から1.0 mg/kgの6用量で1回投与した。解析対象は35例である。LDLコレステロールの平均低下率は、0.3 mg/kgで9%、1.0 mg/kgで62%（絶対値で78 mg/dL）であった。PCSK9は51%から88%低下し、低下は追跡中保たれた。追跡が1年以上の参加者は15例である ([6](#ref-6))。

「62%」は最高用量群の平均であり、対照群のない用量漸増試験の値である。最高用量群の例数は抄録に記載がなく、確認できていない。抄録は、一過性のALT上昇と、1例の誤嚥性肺炎を報告している ([6](#ref-6))。「遺伝子編集でLDLが62%下がる」は、この集団・この用量に限られた記述になる。

### 個別化mRNAワクチンの42%

第3相INTerpath-001は、完全切除後のIIB期からIV期の黒色腫1,137例を、intismeran autogeneとpembrolizumabの併用、またはプラセボとpembrolizumabに2:1で割り付けた。主要評価項目は、研究者判定の無再発生存期間である。主要な事前規定のintention-to-treat解析で、追跡期間の中央値24.6か月、再発または死亡のハザード比は0.58（95%信頼区間 0.45から0.75）であった。企業はこれを「再発または死亡のリスクを42%低下」と表現する ([7](#ref-7))。0.58は発生速度の比であり、1−0.58=0.42はハザードの減少を意味する。42%の人が再発しなかったという意味ではない。

2年無再発生存率は82.2%（79.3%から84.8%）対70.0%（65.0%から74.5%）で、差は12.2ポイントである（筆者計算）。2年の遠隔転移なし生存率は88.5%対80.2%、遠隔転移または死亡のハザード比は0.62（0.45から0.85）である ([7](#ref-7))。ハザード比は時期により異なる。最初の6か月は0.99（0.66から1.49）で差がなく、6か月以降の事前規定の感度分析では0.42（0.30から0.58）であった。投与を受けなかった例を除いた解析では0.51（0.39から0.67）である ([7](#ref-7))。全生存期間は未成熟で、企業の発表にハザード比はない ([7](#ref-7))。報道は0.77（0.45から1.31）を伝えるが、事前規定の有意水準に達していない ([8](#ref-8))。結果は論文として受理されたと企業は述べ、筆者のPubMed検索では見つからなかった ([7](#ref-7))。

### retatrutideの28%

TRIUMPH-1は、糖尿病のない肥満または過体重の成人2,339例を80週追跡した。企業の医療情報ページによると、12 mgの平均体重変化は、治療中断などの事象の前の効果を表す推定対象（efficacy estimand）で−28.3%（プラセボ−2.2%）、服薬の遵守にかかわらない治療レジメンの推定対象（treatment-regimen estimand）で−25.0%（プラセボ−3.9%）である。4 mgは−19.0%と−17.6%、9 mgは−25.9%と−23.7%である ([9](#ref-9))。プラセボとの差は、前者で26.1ポイント、後者で21.1ポイントになる（筆者計算）。見出しの約28%は前者の最高用量の値である。2型糖尿病を合併する集団（TRIUMPH-2）では、同じ12 mg、80週で最大20.8%である ([10](#ref-10))。LillyはBLAを2027年第1四半期に提出する予定と述べ、現時点では世界のいずれの規制当局からも承認されていない ([10](#ref-10))。

## 開発の途中にある2項目

### rentosertibの第3相

ClinicalTrials.govの登録によると、rentosertibの第3相は特発性肺線維症を対象とする無作為化・二重盲検・プラセボ対照試験で、1日1回、52週投与する。予定登録数は320例、開始は2026年9月9日、主要評価項目は52週間の努力性肺活量の年間低下率、主要評価項目の完了予定は2029年10月30日である ([11](#ref-11))。第3相の開始は、効果を示した結果ではない。有効性に関する公表データは第2a相のみである。第2a相は71例を12週間、30 mg 1日1回・30 mg 1日2回・60 mg 1日1回・プラセボに割り付け、主要評価項目は有害事象の発現割合であった。努力性肺活量の変化は副次評価項目で、60 mg 1日1回群が+98.4 mL（95%信頼区間 10.9から185.9）、プラセボ群が−20.3 mL（−116.1から75.6）であり、区間は重なる ([12](#ref-12))。

### 発毛の飲み薬の第3相（数値は未照合）

見出しの薬は特定できていない。候補は、Veradermicsの徐放性経口ミノキシジルVDPHL01である。同社の2026年10月19日の発表を検索結果の抜粋で見た範囲では、第3相Study 304は男性型脱毛症の男性536例を、8.5 mgの1日1回、1日2回、プラセボに割り付け、6か月時点の非軟毛の本数が+28.6本/cm²、+36.4本/cm²、プラセボ+6.6本/cm²であった。差は22.0と29.8本/cm²である（筆者計算）。ページ本体は取得できず、試験登録も読めていないため、これらの数値は原文と照合していない ([13](#ref-13))。企業の発表であり、査読論文ではない。見出しの薬がこれかどうかは確認できず、他の候補を排除していない。

## 1例の報告と基礎研究

### ブタの腎臓の271日

Lancetの報告は、FDAの拡大アクセスのもとで計画された3例の研究の最初の1例である。遺伝子改変ブタ腎臓EGEN-2784（糖鎖抗原の欠失、ブタ内在性レトロウイルスの不活化、ヒト導入遺伝子7個）を2025年1月25日に移植し、271日間透析から離脱した。移植後14日にT細胞性拒絶があり、治療で改善した。免疫抑制を減らした後に微小血管の炎症が進み、血栓性微小血管症で移植腎が機能を失った。摘出の82日後にヒトの腎臓を移植し、231日の追跡で感作は認められなかった ([17](#ref-17))。1例の経過であり、一般化はできない。

「記録」という表現にも留保がある。eGenesisの2026年9月3日の発表は、拡大アクセスで5例が移植を受け、別の1例が9か月を超えて透析なしで試験を継続しており、世界記録を更新したと述べる ([18](#ref-18))。同社は、FDAが承認した第1/2/3相のRESTORE試験（50歳から70歳の33例）を2027年第1四半期に始める予定とする ([18](#ref-18))。271日が最長とは、同社自身の発表からは言えない。

### 染色体サイズのDNAの細胞間移動

2026年のCell論文は、微小核や断片化した染色体に由来する細胞質DNAが、接触依存性のナノチューブを通って隣接するヒト細胞へ移ることを示した。移った断片は受容細胞で安定に受け継がれる。対象はヒト培養細胞である ([19](#ref-19))。2025年のScience論文は、ヒト染色体をヒト細胞からマウス胚性幹細胞へ移し、再びヒト細胞へ戻して内在染色体を除く方法を報告した ([20](#ref-20))。見出しがどちらを指すかは確認できず、「染色体サイズ」が抄録で確認できるのは後者の方法論である。どちらも培養細胞の基礎研究であり、承認の対象ではない。

## 限界

- 元の投稿を確認できていない。見出しの正確な文言が不明なため、投稿が数値を誤って伝えたとは言えない。
- 論文の全文は一つも読んでいない。87%、62%、42%などの数値のうち、抄録に載らないもの（発作なし62%、1年生存率、全生存期間のハザード比）は、企業発表や報道の抽出に基づく。
- FDA・企業・報道のページは、要約して返すツールの抽出で読んだ。原文の画面や文書との逐語照合はしていない。Veradermicsの発表は検索結果の抜粋のみで、数値は未照合である。
- 承認状況は2026年10月30日時点の記述であり、公開までに変わりうる。
- dostarlimabの独立判定47%の信頼区間は、原文を直接確認できなかったため扱わない。
- 本記事の執筆にはAI（Claude）を使い、同じ筆者の指示で3つのAIによる査読を受けた。人間の第三者による確認ではない。

## 結論

2026年10月30日時点（10月31日再確認）で、確認できた範囲では、10項目のうち薬・ワクチン・治療法にあたる8項目で承認済みは2項目である。daraxonrasibの膵がんはFDAに承認され、dostarlimabの直腸がんは加速承認された。lonvo-zはBLAが受理され審査中であり、他の5項目は申請前または開発の途中である。ブタの腎臓とDNAの移動は承認の対象ではない。

見出しの数値は、確認できた資料の記載と矛盾しなかった。ただし、数値が指す量には条件がつく。遺伝性血管性浮腫の87%は発作回数の減少率で、発作なしは62%である。LDLの62%は最高用量群の平均で、ワクチンの42%はハザードの減少であり、最初の6か月のハザード比は差がなかった。retatrutideの約28%は、治療中断などの事象を除いた推定対象の値で、遵守にかかわらない推定対象では約25%である。dostarlimabの47%と68%は判定者と評価可能例が異なる別の評価である。元の投稿が確認できないため、これらの条件が投稿でどう書かれていたかは判断できない。

## 参照

<span id="ref-1"></span>1. O'Reilly EM, Wainberg ZA, Hendifar AE, Borad MJ, Pietrantonio F, Pant S, et al. Daraxonrasib or chemotherapy in previously treated metastatic pancreatic cancer. N Engl J Med. 2026;395(4):325–337. [doi:10.1056/NEJMoa2605555](https://doi.org/10.1056/NEJMoa2605555).

<span id="ref-2"></span>2. U.S. Food and Drug Administration. FDA approves daraxonrasib for metastatic pancreatic adenocarcinoma [Internet]. Silver Spring (MD): FDA; 2026 Aug 26 [cited 2026 Oct 31]. Available from: [https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-daraxonrasib-metastatic-pancreatic-adenocarcinoma](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-daraxonrasib-metastatic-pancreatic-adenocarcinoma).

<span id="ref-3"></span>3. Cohn DM, Gurugama P, Longhurst HJ, Aygören-Pürsün E, Craig TJ, Farkas H, et al. Lonvoguran ziclumeran: in vivo CRISPR gene editing in hereditary angioedema. N Engl J Med. 2026;395(15):1471–1482. [doi:10.1056/NEJMoa2600931](https://doi.org/10.1056/NEJMoa2600931).

<span id="ref-4"></span>4. Intellia Therapeutics. Intellia Therapeutics reports positive phase 3 results in hereditary angioedema, marking a global first for in vivo gene editing [press release]. Cambridge (MA): Intellia Therapeutics; 2026 Apr 27 [cited 2026 Oct 31]. Available from: [https://www.biospace.com/press-releases/intellia-therapeutics-reports-positive-phase-3-results-in-hereditary-angioedema-marking-a-global-first-for-in-vivo-gene-editing](https://www.biospace.com/press-releases/intellia-therapeutics-reports-positive-phase-3-results-in-hereditary-angioedema-marking-a-global-first-for-in-vivo-gene-editing) (reprint of the company release).

<span id="ref-5"></span>5. Intellia Therapeutics. Intellia Therapeutics announces FDA acceptance of Biologics License Application with priority review for lonvoguran ziclumeran (lonvo-z) for hereditary angioedema (HAE) (Exhibit 99.1 to Form 8-K) [press release]. U.S. Securities and Exchange Commission; 2026 Sep 8 [cited 2026 Oct 31]. Available from: [https://www.sec.gov/Archives/edgar/data/0001652130/000119312526385194/ntla-ex99_1.htm](https://www.sec.gov/Archives/edgar/data/0001652130/000119312526385194/ntla-ex99_1.htm).

<span id="ref-6"></span>6. Vafai SB, Täubel J, Ashdown T, Patel RS, Diamondali S, Cegla J, et al. In vivo base editing of PCSK9 with VERVE-102 for hypercholesterolemia. N Engl J Med. 2026;395(7):648–659. [doi:10.1056/NEJMoa2601283](https://doi.org/10.1056/NEJMoa2601283).

<span id="ref-7"></span>7. Merck, Moderna. Merck and Moderna will present results from landmark phase 3 INTerpath-001 trial for intismeran autogene plus KEYTRUDA (pembrolizumab) at ESMO 2026 Presidential Symposium [press release]. Rahway (NJ), Cambridge (MA): Merck; 2026 Oct 22 [cited 2026 Oct 31]. Available from: [https://s2.q4cdn.com/584635680/files/doc_news/Merck-and-Moderna-Will-Present-Results-From-Landmark-Phase-3-INTerpath-001-Trial-for-Intismeran-Autogene-Plus-KEYTRUDA-pembrolizumab--RDG7J.pdf](https://s2.q4cdn.com/584635680/files/doc_news/Merck-and-Moderna-Will-Present-Results-From-Landmark-Phase-3-INTerpath-001-Trial-for-Intismeran-Autogene-Plus-KEYTRUDA-pembrolizumab--RDG7J.pdf).

<span id="ref-8"></span>8. CancerNetwork. INTerpath-001 data detail survival, subgroup, and safety findings in melanoma [Internet]. CancerNetwork; 2026 Oct 24 [cited 2026 Oct 31]. Available from: [https://www.cancernetwork.com/view/interpath-001-data-detail-survival-subgroup-and-safety-findings-in-melanoma](https://www.cancernetwork.com/view/interpath-001-data-detail-survival-subgroup-and-safety-findings-in-melanoma).

<span id="ref-9"></span>9. Eli Lilly and Company. What are the results of retatrutide from TRIUMPH-1 in participants with obesity or overweight without type 2 diabetes? [Internet]. Lilly Medical Information; date of last review 2026 Aug 26 [cited 2026 Oct 31]. Available from: [https://medical.lilly.com/us/products/answers/what-are-the-preliminary-results-of-retatrutide-from-triumph-1-in-participants-with-obesity-or-overweight-without-type-2-diabetes-386151](https://medical.lilly.com/us/products/answers/what-are-the-preliminary-results-of-retatrutide-from-triumph-1-in-participants-with-obesity-or-overweight-without-type-2-diabetes-386151).

<span id="ref-10"></span>10. Eli Lilly and Company. Lilly's triple agonist, retatrutide, successful in two additional phase 3 obesity trials, delivering significant improvements in weight and A1C [press release]. Indianapolis (IN): Eli Lilly and Company; 2026 Jul 23 [cited 2026 Oct 31]. Available from: [https://www.biospace.com/press-releases/lillys-triple-agonist-retatrutide-successful-in-two-additional-phase-3-obesity-trials-delivering-significant-improvements-in-weight-and-a1c](https://www.biospace.com/press-releases/lillys-triple-agonist-retatrutide-successful-in-two-additional-phase-3-obesity-trials-delivering-significant-improvements-in-weight-and-a1c) (reprint of the company release).

<span id="ref-11"></span>11. InSilico Medicine Hong Kong Limited. Study evaluation rentosertib (INS018_055) administered orally in patients with idiopathic pulmonary fibrosis (IPF); ClinicalTrials.gov identifier NCT07687459 [Internet]. National Library of Medicine (US); last update posted 2026 Oct 13 [cited 2026 Oct 31]. Available from: [https://clinicaltrials.gov/study/NCT07687459](https://clinicaltrials.gov/study/NCT07687459).

<span id="ref-12"></span>12. Xu Z, Ren F, Wang P, Cao J, Tan C, Ma D, et al. A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial. Nat Med. 2025;31(8):2602–2610. [doi:10.1038/s41591-025-03743-2](https://doi.org/10.1038/s41591-025-03743-2).

<span id="ref-13"></span>13. Veradermics. Veradermics' oral VDPHL01 achieved early, consistent, and robust hair growth in positive phase 3 '304' clinical trial in male pattern hair loss [press release]. Business Wire; 2026 Oct 19 [cited 2026 Oct 31]. Available from: [https://www.businesswire.com/news/home/20261019684103/en/Veradermics-Oral-VDPHL01-Achieved-Early-Consistent-and-Robust-Hair-Growth-in-Positive-Phase-3-304-Clinical-Trial-in-Male-Pattern-Hair-Loss](https://www.businesswire.com/news/home/20261019684103/en/Veradermics-Oral-VDPHL01-Achieved-Early-Consistent-and-Robust-Hair-Growth-in-Positive-Phase-3-304-Clinical-Trial-in-Male-Pattern-Hair-Loss) (page not retrievable; content seen only as search-result excerpts).

<span id="ref-14"></span>14. U.S. Food and Drug Administration. FDA grants accelerated approval to dostarlimab for locally advanced rectal cancer [Internet]. Silver Spring (MD): FDA; 2026 Oct 19 [cited 2026 Oct 31]. Available from: [https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-dostarlimab-locally-advanced-rectal-cancer](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-dostarlimab-locally-advanced-rectal-cancer).

<span id="ref-15"></span>15. GlaxoSmithKline. A study of dostarlimab in untreated dMMR/MSI-H locally advanced rectal cancer (AZUR-1); ClinicalTrials.gov identifier NCT05723562 [Internet]. National Library of Medicine (US); last update posted 2026 May 26 [cited 2026 Oct 31]. Available from: [https://clinicaltrials.gov/study/NCT05723562](https://clinicaltrials.gov/study/NCT05723562).

<span id="ref-16"></span>16. Cercek A, Bachet JB, Folprecht G, Bando H, Seligmann J, Starling N, et al. Clinical complete response with dostarlimab monotherapy in dMMR/MSI-H locally advanced rectal cancer: first results from the global AZUR-1 trial. Ann Oncol. 2026 Oct 25:S0923-7534(26)08070-1 [Epub ahead of print]. [doi:10.1016/j.annonc.2026.10.1280](https://doi.org/10.1016/j.annonc.2026.10.1280).

<span id="ref-17"></span>17. Riella LV, Borges TJ, Rosales IA, Avillach CT, Palsson R, Hullekes F, et al. Porcine kidney xenotransplantation as a bridge to allotransplantation: a first-in-human study. Lancet. 2026;408(10559):1029–1040. [doi:10.1016/S0140-6736(26)01295-X](https://doi.org/10.1016/S0140-6736(26)01295-X).

<span id="ref-18"></span>18. eGenesis. eGenesis announces clinical update in ongoing expanded access study of EGEN-2784 in patients with kidney failure [press release]. Cambridge (MA): eGenesis; 2026 Sep 3 [cited 2026 Oct 31]. Available from: [https://egenesisbio.com/news-media/press-releases/egenesis-announces-clinical-update-in-ongoing-expanded-access-study-of-egen-2784-in-patients-with-kidney-failure](https://egenesisbio.com/news-media/press-releases/egenesis-announces-clinical-update-in-ongoing-expanded-access-study-of-egen-2784-in-patients-with-kidney-failure).

<span id="ref-19"></span>19. Maurais EG, Mazzagatti A, Lin YF, Narozna M, Hu Q, Dahiya R, et al. Genome instability triggers intercellular DNA transfer between human cells. Cell. 2026;189(15):4548–4561.e14. [doi:10.1016/j.cell.2026.04.041](https://doi.org/10.1016/j.cell.2026.04.041).

<span id="ref-20"></span>20. Petris G, Grazioli S, van Bijsterveldt L, Murat P, Liu KC, Birnbaum J, et al. High-fidelity human chromosome transfer and elimination. Science. 2025;390(6777):1038–1043. [doi:10.1126/science.adv9797](https://doi.org/10.1126/science.adv9797).

<span id="ref-21"></span>21. U.S. Food and Drug Administration. FDA approves first in class targeted therapy for metastatic pancreatic cancer [Internet]. Silver Spring (MD): FDA; 2026 Aug 26 [cited 2026 Oct 31]. Available from: [https://www.fda.gov/news-events/press-announcements/fda-approves-first-class-targeted-therapy-metastatic-pancreatic-cancer](https://www.fda.gov/news-events/press-announcements/fda-approves-first-class-targeted-therapy-metastatic-pancreatic-cancer).

<span id="ref-22"></span>22. The ASCO Post. Daraxonrasib nearly doubles survival in previously treated metastatic pancreatic cancer [Internet]. The ASCO Post; 2026 Jun 10 [cited 2026 Oct 31]. Available from: [https://ascopost.com/news/june-2026/daraxonrasib-nearly-doubles-survival-in-previously-treated-metastatic-pancreatic-cancer/](https://ascopost.com/news/june-2026/daraxonrasib-nearly-doubles-survival-in-previously-treated-metastatic-pancreatic-cancer/).

<span id="ref-23"></span>23. U.S. Food and Drug Administration. Accelerated approval program [Internet]. Silver Spring (MD): FDA; content current as of 2026 Aug 25 [cited 2026 Oct 31]. Available from: [https://www.fda.gov/drugs/nda-and-bla-approvals/accelerated-approval-program](https://www.fda.gov/drugs/nda-and-bla-approvals/accelerated-approval-program).
