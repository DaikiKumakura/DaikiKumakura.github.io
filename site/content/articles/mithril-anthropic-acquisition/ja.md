> **利益相反の開示：** 本記事の執筆にはAI（Claude）を使った。ClaudeはAnthropic社のモデルで、同社は買収した側である。本記事は、買収を発表したAnthropic社自身の記事と、同社が公開した技術報告書に書かれていることだけを報告する。第三者による検証や取引の内部事情には踏み込まない。同じ筆者の指示で3つのAIによる査読を受けたが、人間の第三者による確認ではない。

2026年10月27日、Anthropicは従業員1名の創薬会社Mithril Medicineを買収したと発表した ([1](#ref-1))。発表は、同社が筋ジストロフィーの1病型について、アイデアから「マウスでの有望な結果」まで18か月未満で進んだと述べる ([1](#ref-1))。この期間が何を指し、何を指さないのか。発表に付属する技術報告書は、その期間とマウスの結果をどこまで裏づけているのか。この2点を、公開された二つの資料で確かめる。

## 対象と確認範囲

対象は二つの資料である。一つはAnthropicが2026年10月27日に公開した記事で、買収の発表を含む ([1](#ref-1))。もう一つは、Mithril Medicineの抗体研究をまとめた2026年10月26日付の技術報告書である。この報告書は、各ページの上部に「Not peer reviewed」と表示された査読前の文書で、査読済み論文としては扱わない ([2](#ref-2))。どちらも買収した側が作成した資料である。

2026年11月2日に発表記事の全文を再確認した。一方、技術報告書は今回の確認環境では取得できず、以前の作業記録に対応するPDFや抽出本文も保存されていなかった。このため、以下の報告書由来の数値・ページ位置・実験条件は過去の読解記録に基づく暫定的な記載であり、今回原資料に再照合できた結果ではない。特に表2の効果量と信頼区間、実験群の内訳、Claudeの処理件数は未再確認であり、確定した数値として引用しないでほしい。報告書の個票データや補足表の個別値についても検証していない。

本記事は統計の再解析を行っていない。行ったのは、報告書のP値の下限についての算術確認（2/35）だけである。計算を伴う配布物はないため、データとコードの公開状況の節は設けない。取引条件や、二次報道にだけある取引時期・出資者の情報は、一次資料で確認できなかったため使わない。

## 発表で確認できること

表1に発表記事の記載と、過去の読解記録に残る報告書の位置づけを示す。

表1　発表記事の記載と報告書の位置づけ。報告書由来の項目は今回未再確認。

| Item | What the sources state |
| --- | --- |
| Announcement date | 27 October 2026 ([1](#ref-1)) |
| Company | Mithril Medicine, a company with one employee. Its founder, Cody Tranbarger, is at Anthropic as of the announcement ([1](#ref-1), [2](#ref-2)) |
| Disease targets | Two rare forms of muscular dystrophy ([1](#ref-1)). The report addresses LAMA2-related congenital muscular dystrophy (LAMA2-CMD) and lists α-dystroglycanopathy among the programs to be continued ([2](#ref-2)) |
| Type of drug | A bispecific "bridging" antibody designed to link laminin-α4 to α-dystroglycan and thereby reconnect muscle fibers to the basement membrane ([2](#ref-2)) |
| Stage | The announcement says the research as a whole is mostly preclinical and has not yet reached testing in humans ([1](#ref-1)) |
| Transaction terms | Not stated in either document |
| Technical report | Dated 26 October 2026; not peer reviewed ([2](#ref-2)) |

## 「18か月未満」が指す期間

発表は、創業者がClaudeを使い、契約、物流、11の外部研究機関との実験を整理したと述べる。運営の他の多くの部分もClaudeに任せたという。その結果、筋ジストロフィー1病型の治療候補が、アイデアから「マウスでの有望な結果」まで18か月未満で進んだとする ([1](#ref-1))。

この期間には二つの特徴がある。第一に、期間の終点はマウスの結果である。発表は、ヒトでの臨床試験を始められる状態になる時期を、候補が持ちこたえた場合に早ければ2028年後半と予想する ([1](#ref-1))。これは条件つきの見通しで、18か月とは別の話である。第二に、18か月という数字は発表の記事にだけ現れる。過去の読解記録では報告書の本文に18か月に当たる記述を見いだせず、起点（アイデア）の定義も読み取れなかった。パイロット試験の日程を示す図10Cの時系列は、期間の検討には使っていない ([2](#ref-2))。

終点に近い部分では、報告書自身が実験の位置づけを述べている。実験は探索的で、GLP（優良試験所基準）の下では行われていない。特に断らない限り、無作為化も盲検化もされておらず、例数は検出力の計算で決めておらず、主要評価項目も事前に定めていない ([2](#ref-2), PDF p. 25)。過去の読解記録ではIND（治験開始のための申請）、毒性試験、費用の記述を見いだせなかったが、今回その不在を原資料に再確認できていない。

試験された分子についても確認が必要である。報告書は、公開されている可変領域をもとに作った「ツール分子」2つで仮説を試したと述べる。新規の構築体（抗体の設計ごとの個別の分子）の評価と最適化には、これより大きなスクリーニングが要るとし、113の構築体のパネルを製造した ([2](#ref-2))。したがって、18か月の終点にある結果は、公開配列にもとづくツール分子での試験であり、新規構築体を絞り込む前の段階のものと読める（筆者の読み）。

18か月の長短は評価しない。比較には、他の事例で起点と終点がどこに置かれたかが必要になる。両資料に比較対象はなく、外部の数値は原典を確認できなかったため、並べていない。

## マウスの結果が支える範囲

報告書は、ラミニン-α2を欠くdyWマウスで予備的な試験を行った ([2](#ref-2))。薬剤を6週間投与し、無処置のvehicle群と野生型のマウスと比べた。分子は、2価の1+1 CrossMabと、4価の2+2 IgG-scFvである。評価したのは、神経刺激で誘発した上腕三頭筋の力の最大値（peak force）と、前肢の握力である。

[原報告のFigure 11B](https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf#page=18)によれば、2+2群のpeak forceは、vehicle群の平均に対して1.95倍（95%信頼区間 1.51〜2.51、2+2群7匹 対 vehicle群4匹）だった。マウスを単位にしたWelchのt検定ではP = 0.0001（多重性の調整なし）である。一方、1匹の母親が産んだ仔の群（litter）を単位にし、litterごとの平均で行った正確順位検定ではP = 0.057である（2+2群4 litter 対 vehicle群3 litter）。1+1 CrossMabは、vehicle群と区別できる差を示さなかった（1.08倍、0.67〜1.76）。同じ名目モル用量での2分子の対比では、2+2群は1.80倍（1.12〜2.91）と報告された ([2](#ref-2), PDF p. 18)。

P = 0.057について、報告書は「7 litterで取りうる最小の値」と説明する ([2](#ref-2), [原報告の限界の記述](https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf#page=21))。筆者の算術確認では、4 litter 対 3 litterの順位の並べ方は7個から3個を選ぶ35通りで、両側の最小のPは2/35 = 0.057となり、報告書の記載と一致する。

報告書は結果の限界を次のように挙げる ([2](#ref-2), [原報告の限界の記述](https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf#page=21))。

- 群は順次登録され、vehicle群は別の投与計画に従った。
- 各litterには1種類の処置だけが与えられ、無作為化されていない。
- 6週目までの脱落（dyWマウス58匹のうち26匹）の後、処置群は4〜7匹になった。
- 処置群6つ、評価項目11以上を調べたため、偶然の所見の可能性がある。
- 2+2の筋肉内の濃度は測られていない。筋肉内の濃度は1+1 CrossMabでだけ測定された。

解析の選び方で結論が動くことも、報告書は感度解析で示している。主文の5群（野生型を含む）を一元配置分散分析（Tukeyの多重比較）で比べると、生の値ではP = 0.43、対数変換した値ではP = 0.023だった ([2](#ref-2), PDF p. 29)。

報告書自身の言い方も確かめておく。効果は「関連していた（associated with）」と書かれ、力の部分的な回復を「示唆する」とされる。「概念実証」と位置づける一方、この解釈には「同時に行う盲検の再現」が必要だとも述べる ([2](#ref-2))。

**解釈（筆者の読み）：** 報告書自身も、統計的な裏づけはマウスとlitterのどちらを単位にするかに依存すると書く ([2](#ref-2), PDF p. 21)。同じlitterの仔は遺伝的背景と飼育条件を共有し、各litterは1種類の処置しか受けていない。処置の違いとlitterの違いが重なっているため、litterを単位にした検定のほうが、この設計に合った問いに答える。そのP値は、この例数では0.057より小さくなり得ない。つまり、報告書が示したのは「効果がない」という証拠ではなく、この設計では慣例の水準で判別できないという検出力の限界である。マウスを単位にしたP = 0.0001は、同じlitterの仔を独立とみなしているため、小さく出すぎている可能性がある。

結果が支えるのは、予備試験で2+2群の力が高い傾向があったという範囲である。ヒトでの有効性、効果の持続、作用の機序は、この試験からは言えない。

## 1週間の事例に見るAIと人間の分担

報告書には「Working with Claude」の節があり、製造委託先から届いたデータの検討を含む1週間の作業を記述している ([2](#ref-2), [原報告のFigure 12](https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf#page=19))。この節は、Claudeが自分のスレッドとメモから編集したもので、偏りの危険があると報告書自身が述べる。報告書の本文も、Claudeが文献を調べ、再解析を行い、図を作り、原稿を起案したと記す ([2](#ref-2), PDF p. 30)。

表2に、その1週間の数値を示す。

表2　報告書が1週間の事例として記す数値。CRO（contract research organization）は受託研究機関を指す。

| Item | What the report states |
| --- | --- |
| Data | A 341-page report arrived from the production contractor on day 4. Claude took 2 min 40 s to give a first answer and 7 min 53 s to produce a visual synthesis of all 113 constructs |
| Triage | Claude marked 82 constructs for screening as is, seven for additional polishing, and 24 (constructs with three laminin-binding arms) to be held back |
| Human ruling | Claude recommended binding kinetics for all 113 constructs; the team overruled this and set the three arms aside on production criteria. About four minutes later Claude had revised the memo, schedule and drafts from 113 to 89 constructs |
| Emails | Claude drafted 17 emails and the team sent 12, each of which had been edited. Claude listed 41 points for which it had found no written statement, for confirmation before sending |
| Errors | Of six errors examined in detail, Claude found five (one after a question from a CRO and two before the affected email was sent). At least three reached a CRO in emails the team had edited and sent. One of these (a request for less material per tube than the assay CRO had asked for) was corrected within a day, before any tube was filled. Two others, both statements in Claude's review of the production data, went unnoticed for more than 4 days, and one remains unsettled |
| Pace | All 89 constructs were shipped for the two cell-based assays within a week of the ruling. Claude's median response times were 96 s for a first answer and 10 min for a full answer; the median first reply of a CRO took 8.5 h |

これらの数値は、報告書の著者が自らの作業を記述したものである。報告書は、作業の速さがCROの返信と人間の判断で決まったと解釈し、Claudeが担ったのは、読み取り、計算、起案、および一つの判断が影響する後続の全工程をたどる作業であり、判断は人間に残ったと述べる ([2](#ref-2))。同時に報告書は、これらの事例から、人間の編集はメールに含まれる判断を検査するほうが、メールが運ぶ細部や前提を検査するより確実だったとみられると述べる ([2](#ref-2))。

**解釈（筆者の読み）：** 表2の誤り6件は、詳しく調べた件数であり、全体の誤り率ではない。分母（Claudeの起案や主張の総数）は報告書に示されていないので、誤りの頻度は、この記述だけからは評価できない。1週間の事例は、報告書の著者が選んで記述したもので、作業全体を代表するかどうかは資料から分からない。分かるのは、人間が編集して送った後でも、誤りが外部に届いた例がある点と、同じ週にClaudeが5件を自分で見つけた点の両方である。

## 限界

- 二つの資料はいずれも買収した側が作成した。報告書は、Claudeが関与して起案されている。第三者による検証はない。
- 報告書は査読前の文書である。マウスの試験は予備的な1回の試験で、独立した再現は報告されていない。
- 本記事は、マウスのデータそのものを再解析していない。報告書の数値は原資料に再照合できておらず暫定的な記載である。補足表の個別の数値も検証していない。
- 18か月の速さを他の事例と比べていない。IND、毒性試験、費用は確認できた情報がないため扱っていない。
- 発表記事の確認は2026年11月2日時点であり、その後のAnthropic社の記事・報告書の更新や取引条件の公表は反映していない。

## 結論

「アイデアから有望なマウス結果まで18か月未満」は、Anthropicの発表記事が示した期間であり、終点は予備的なマウス試験の結果である。報告書における期間や起点の定義、IND、毒性試験、費用は今回原資料に再確認できなかった。発表記事が示す終点は臨床試験の準備完了ではない。ヒトでの試験を始められる状態になる見込みは、候補が持ちこたえた場合に、発表から見て早ければ2028年後半という、条件つきの予測である。

マウスの結果は、2+2群の力が高い傾向を示す予備試験にとどまる。litterを単位にした検定のP = 0.057は、7 litterでは最小の値であり、無作為化や盲検化のない設計の限界を含む。報告書もこれを概念実証と位置づけ、同時対照と盲検での再現を求めている。したがって報告書は、18か月という期間そのものも、AIの寄与の大きさも直接には裏づけない。裏づけるのは、予備的なマウス試験の範囲と、1週間の作業記述である。後者には、Claudeが自分で見つけた誤り5件と、人間が編集して送った後でも外部に届いた誤りの両方が含まれる。

## 参照

<span id="ref-1"></span>1. Anthropic. Early progress on accelerating drug development with Claude [Internet]. Anthropic; 2026 Oct 27 [cited 2026 Oct 31]. Available from: [https://www.anthropic.com/research/early-progress-drug-development](https://www.anthropic.com/research/early-progress-drug-development).

<span id="ref-2"></span>2. Tranbarger C, Mithril Medicine. Preclinical characterization of a bispecific bridging antibody for the treatment of LAMA2-related congenital muscular dystrophy [Technical report; not peer reviewed] [Internet]. Anthropic; 2026 Oct 26 [cited 2026 Oct 31]. 38 p. Available from: [https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf](https://www-cdn.anthropic.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf).
