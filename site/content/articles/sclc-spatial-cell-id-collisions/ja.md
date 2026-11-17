腫瘍の近くにT細胞がいるかを調べるには、座標と細胞型が同じ細胞を指していなければならない。小細胞肺がんのCosMx研究で、Zhangらは原発・リンパ節転移由来の計105標本を調べた ([1](#ref-1))。公開された座標と注釈を使えば別の近傍指標を計算できそうに見える。そこでまず、手元のファイルで何が同じ細胞だと言えるかを数えた。

## 結合できる行は一意とは限らない

著者リポジトリの固定版には、座標RDSが2点と、スライド付き注釈CSVがある ([2](#ref-2))。座標ファイルには `cell_id, x, y`、注釈表には `slide, cell_id, cell_type` がある。座標は426,822行と314,447行。ファイル内で細胞IDは一意だったが、ファイル間では279,603個が共通した。注釈のスライドと細胞IDの組も一意だった。座標側に明示的なスライド列がないため、この二つの一意性だけでは結合を決められない。

候補ごとの照合結果を表1に示す。

**表1.** 注釈IDと座標ファイルの候補一致件数。

| Annotation and candidate ID | Annotation rows | Matched in coordinate file 1 | Matched in coordinate file 2 |
| --- | ---: | ---: | ---: |
| Slide1, unmodified | 360,169 | 360,169 | 234,360 |
| Slide2, unmodified | 244,061 | 0 | 0 |
| Slide2, terminal `_2` replaced by `_1` | 244,061 | 215,386 | 244,061 |

右下の244,061を見れば、末尾を変えたSlide2をファイル2に結べばよさそうに見える。しかしファイル1にも215,386行が一致する。数が多く一致したことは有力な候補を与えるが、末尾変換の意味や座標の由来を証明しない。

## スライド情報を消すとラベルまで混ざる

末尾を同じ表記にそろえたSlide2のIDを、座標を使わずにSlide1の注釈へ照合した。180,027個が一致し、そのうち115,671個で細胞型ラベルが異なった。両方とも `Undefined` 以外だった116,649個に絞っても、57,553個（49.34%）が異なる。実際に研究で誤結合された件数ではない。スライドを捨てた結合を行うと、ここまで多くの別ラベルを結びうるという検算だ。

データ辞書は局所・大域ピクセル座標と視野（FOV）位置のmm表記を区別している ([2](#ref-2))。今回のRDSの短い `x,y` 列にどの変換が対応するかは、調べた資料から確定できなかった。視野内の被覆と患者・標本の対応が揃わなければ、境界で見えなかったT細胞と、実際に近傍にいないT細胞も区別できない。ここで示せる結論は、ファイル識別子とスライドに依存する結合を検証せずに、µm単位の近傍率や患者間の順位を算出すると、解釈の前提が崩れるということだ。著者が報告した近傍効果やDLL3薬効の再評価はしていない。

## データとコードの公開状況

[再現用ZIP](shared/sclc-spatial-cell-id-collisions/companion.zip)には入力の固定版情報と取得先、Rの監査コード、集計表を収録した。元ファイルは取得先から読む。

## 参照

1. <a id="ref-1"></a> Zhang Z, Wu D, Chen Z, Dai M, Yang F, Wang J, et al. Single-cell spatial transcriptomics reveals tumor microenvironment heterogeneity in primary and lymph node-metastatic small cell lung cancer. Cell Rep Med. 2026;7(4):102713. [doi:10.1016/j.xcrm.2026.102713](https://doi.org/10.1016/j.xcrm.2026.102713).
2. <a id="ref-2"></a> Zhang Z, et al. SCLC-LNM-SMI. [Coordinate and annotation repository at commit 1c6ed2c](https://github.com/ZhoulabCPH/SCLC-LNM-SMI/tree/1c6ed2c985a79ee55371865f3ccc9a10f9d64581) · [SMI data file README](https://github.com/ZhoulabCPH/SCLC-LNM-SMI/blob/1c6ed2c985a79ee55371865f3ccc9a10f9d64581/SMI%20Data%20File%20information/SMI%20Data%20File%20ReadMe.pdf).
