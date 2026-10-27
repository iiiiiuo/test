# SOURCE_VIDEO 全編和訳レビュー（v1）

RUN_ID: `full_source_translation_20261027_105548`

## A. SOURCE INFORMATION

```
Source:
ScreenRecording_10-26-2026 15-15-33_1.mp4（2026-10-27 10:54 添付, sha256 48ce9840…fecfe）
※ 今回の依頼文の SOURCE_VIDEO.mp4 = この添付ファイルとして扱っています（プロジェクト直下の SOURCE_VIDEO.mp4 = Breakfast Club とは別物）

Source Duration:
135.812 s（コンテナ）/ 映像 135.788 s, 4903フレーム, HEVC, 可変フレームレート（60fps基準, 平均36.1fps）, 回転90°で表示 2556x1180 / 音声 AAC 44.1kHz stereo 135.788 s（開始 0.023 s）

Translation Coverage:
00:00.000 – 02:15.812

Translation Status:
PENDING HUMAN APPROVAL
```

内容: iPhoneの画面録画。ポッドキャスト（マイクに「GIVING」のロゴ）に出演した Snoop Dogg が、孫への接し方、自分の祖父と母の話をする。最後は女性ホストの質問の途中で終わる。BGMなし。

- 横長の番組映像の左右に黒帯があり、ほぼ全編 Snoop のアップ。最後の約5秒だけホストと2人の画になる。
- `1.lyrics.txt` はリポジトリ・input/・プロジェクトフォルダのどこにもなく、歌詞もない会話動画なので N/A。
- タイムスタンプはASRの単語タイミング（秒）。フレーム単位の調整はPHASE 2で行います。
- 信頼度: HIGH = 複数モデルが一致 / MED = 細部が不一致（意味は同じ）/ LOW = 聞き取りが確定できない。
- 下の EN は字幕に表示する形（伏せ字適用済み, s**t）。伏せ字なしの原文は transcription.json にあります。
- 固有名詞は英語表記（Snoop, Beverly, Snoopy, Bonanza）。動画内に解説行は出しません。
- 006〜010, 025〜037 は Snoop が孫・祖父・母・子供の頃の自分の声色をまねて再現している部分です。セリフは「」で区別しています。
- 字幕にしない音: ホストの相づち「yeah」（約33.5, 39.1, 42.3, 103.0秒）と、無音の間（59.9–61.1, 64.1–66.5, 95.1–97.0, 129.3–130.3秒）。

## B. COMPLETE ENGLISH / JAPANESE TRANSLATION

### [001]

Timestamp: 00:00.000 – 00:02.400  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: ...trust you more than they trust their mother and father,  
JP: …自分の親より こっちを信用してんだよ

> 動画は文の途中から始まる。主語 they は前後から孫たち。you は一般的な「祖父母（俺）」

### [002]

Timestamp: 00:02.780 – 00:05.700  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: because they know their mother and father can't beat you.  
JP: 親じゃ勝てねえって わかってるからな

> 2つ目の their は they とも聞こえる（MED）が意味は同じ

### [003]

Timestamp: 00:06.760 – 00:10.300  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: I tell my grandkids, I tell my granddaughters all the time,  
JP: 孫たちに 孫娘たちに いつも言ってんだ

> 冒頭の "Oh/So" はフィラーとして字幕にしない

### [004]

Timestamp: 00:10.540 – 00:11.500  
Speaker: Snoop Dogg  
Confidence: MED

EN: You scared of your daddy?  
JP: 「パパが怖いのか？

> 直前に "you see" と聞こえるモデルあり（低確率）

### [005]

Timestamp: 00:12.400 – 00:14.400  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: I will beat your daddy. Your daddy ain't nothing.  
JP: 俺がパパをぶっ倒してやる パパなんて屁でもねえ」

### [006]

Timestamp: 00:15.740 – 00:17.200  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: I said, how much money you think your daddy got?  
JP: 「パパがいくら持ってると思う？」って聞くと

> 区間再確認で said

### [007]

Timestamp: 00:17.380 – 00:18.950  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: "He got a lot of money, Grandpa."  
JP: 「いっぱい持ってるよ おじいちゃん」

> 孫娘のセリフをSnoopが再現

### [008]

Timestamp: 00:19.360 – 00:21.400  
Speaker: Snoop Dogg  
Confidence: MED

EN: I pulled out like $10,000 and thought,  
JP: で 1万ドルくらい出して見せたら

> "and thought"（large-v3 区間・medium.en）/ "oh wow"（large-v3 全体・small.en）で割れた → §D。訳は「見せたら」で両方に対応

### [009]

Timestamp: 00:21.500 – 00:24.400  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: "Wow, you have way more money than him."  
JP: 「すごい パパよりずっとお金持ってる」

> 末尾の "bro" は medium.en のみが聞いたため字幕にしない

### [010]

Timestamp: 00:24.740 – 00:26.950  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: Yeah, you come holla at Grandpa when you need something.  
JP: だろ？ 何か欲しい時は じいちゃんに言いに来な

> holla at = 声をかける・頼みに来る

### [011]

Timestamp: 00:27.280 – 00:28.150  
Speaker: Host (woman, on camera at the end)  
Confidence: HIGH

EN: I know that's right.  
JP: ほんとそれ

> 相手に強く同意する口語表現

### [012]

Timestamp: 00:28.220 – 00:30.400  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: I laid the law down with my grandbabies  
JP: 孫たちには ビシッと教えといたんだ

> lay down the law = 決まりをはっきり言い渡す

### [013]

Timestamp: 00:30.460 – 00:33.200  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: and let them know, because they need to know who their grandfather is.  
JP: 自分のじいちゃんが何者か 知っとかなきゃいけねえからな

### [014]

Timestamp: 00:34.540 – 00:36.100  
Speaker: Snoop Dogg  
Confidence: MED

EN: Not celebrity and none of that other stuff,  
JP: セレブとか そういうのじゃなくて

> and（large-v3）/ or（medium.en）。Critic の確認で and を採用

### [015]

Timestamp: 00:36.160 – 00:38.950  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: but who he is up close and personal, with being a part of their life.  
JP: 孫の人生にちゃんと関わってる 素のじいちゃんをな

### [016]

Timestamp: 00:39.480 – 00:42.950  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: My grandfather was my best friend my first 12 years on this earth.  
JP: 俺のじいちゃんは 生まれてから12年間 俺の親友だった

> ここから自分の祖父の話

### [017]

Timestamp: 00:43.360 – 00:45.000  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: My mother could never whoop me.  
JP: おふくろは俺をシバけなかった

> whoop = 子供を叩いてしつける

### [018]

Timestamp: 00:45.220 – 00:46.800  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: She could never do none of that to me,  
JP: そういうことは 一切できなかった

### [019]

Timestamp: 00:47.280 – 00:48.750  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: but when he wasn't around, I got beat.  
JP: でも じいちゃんがいない時は シバかれた

### [020]

Timestamp: 00:49.560 – 00:50.600  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: But when he was ever around...  
JP: でも じいちゃんがいる時は…

> 言いかけて次のエピソードへ移る

### [021]

Timestamp: 00:51.760 – 00:54.600  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: I got suspended from school and I knew I was gonna get beat.  
JP: 学校で停学くらって 絶対シバかれるって わかってた

> gonna / going to はモデル差。口語の gonna を採用

### [022]

Timestamp: 00:55.180 – 00:57.600  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: He lived right here, and my mama house was right here.  
JP: じいちゃんちがここで おふくろの家がここ

> 手で位置を示しながら。mama house は所有の 's を落としたAAVEの形のまま

### [023]

Timestamp: 00:57.780 – 00:59.850  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: I had to pass his house before I went home.  
JP: 家に帰る前に じいちゃんちを通るんだよ

### [024]

Timestamp: 01:01.080 – 01:04.100  
Speaker: Snoop Dogg  
Confidence: MED

EN: I went there, sat down with him, watched Rasslin' and Bonanza.  
JP: そこに寄って じいちゃんと座って プロレスとBonanzaを見てた

> Rasslin' = wrestling の南部・黒人口語の発音（medium.en 2回 / large-v3 1回）。Bonanza は60〜70年代の西部劇ドラマ（固有名詞なので英語のまま）

### [025]

Timestamp: 01:06.520 – 01:09.850  
Speaker: Snoop Dogg  
Confidence: MED

EN: He said, "Why you here so early?"  
JP: じいちゃんが「なんでこんな早えんだ？」

> "He said," と "why" の間の呼びかけ（Sonny?）が聞き取れず。不確実なので字幕から外した → §D

### [026]

Timestamp: 01:10.040 – 01:11.950  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: I said, "Papa, I got suspended.  
JP: 俺は「じいちゃん 停学くらった

> ここの Papa は祖父のこと。日本語の「パパ」だと父親と誤解されるので「じいちゃん」

### [027]

Timestamp: 01:12.180 – 01:13.050  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: My mom gonna beat me."  
JP: ママにシバかれる」

> 子供の頃の自分のセリフなので「ママ」

### [028]

Timestamp: 01:13.680 – 01:15.100  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: "Your mom ain't gonna do s**t to you.  
JP: 「母ちゃんなんか 何もできやしねえよ

> 祖父のセリフ（Snoopが声色を変えて再現）。large-v3 全体パスは shit を落としたが区間再確認で確定

### [029]

Timestamp: 01:15.840 – 01:16.950  
Speaker: Snoop Dogg  
Confidence: MED

EN: I'm finna tell her right now."  
JP: 今すぐ言ってやる」

> finna（large-v3, 0.97）/ gonna（medium.en）。どちらでも意味は同じ

### [030]

Timestamp: 01:17.240 – 01:18.400  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: "Don't tell her, Papa. Please."  
JP: 「言わないで じいちゃん お願い」

### [031]

Timestamp: 01:18.780 – 01:20.150  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: "No, hell no. I'm telling her right now."  
JP: 「ダメだ 冗談じゃねえ 今すぐ言う」

### [032]

Timestamp: 01:21.040 – 01:24.050  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: "Beverly, Snoopy got suspended, and you ain't doing s**t.  
JP: 「Beverly Snoopyが停学になったが お前は何もすんじゃねえぞ

> 祖父から母への電話。Beverly はSnoopの母の名前、Snoopy は祖父が呼ぶ愛称。you ain't doing shit = 手出しするな

### [033]

Timestamp: 01:24.260 – 01:26.000  
Speaker: Snoop Dogg  
Confidence: MED

EN: He's here with me watching Rasslin' and Bonanza."  
JP: 今 俺とプロレスとBonanza見てるからな」

> Rasslin' は024と同じ

### [034]

Timestamp: 01:27.100 – 01:28.600  
Speaker: Snoop Dogg  
Confidence: MED

EN: "I'm beating his ass when he get out here!"  
JP: そしたらおふくろが「帰ってきたら ケツひっぱたいてやる！」

> 母のセリフ。"get out here" の out は低確率（3モデルとも同じ語順）。意味は「ここ（家）に来たら」

### [035]

Timestamp: 01:28.760 – 01:31.100  
Speaker: Snoop Dogg  
Confidence: MED

EN: On the back of the phone: "Please, mama, I ain't gonna do it, please!"  
JP: 後ろで俺が「ママ お願い もうしないから お願い！」

> on the back of the phone = 電話口の後ろで（子供のSnoopが叫んでいる）。medium.en 全体パスの "I hear her" は他のパスに無いため不採用

### [036]

Timestamp: 01:32.420 – 01:33.250  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: "She ain't gonna do s**t.  
JP: 「母ちゃんは何もしやしねえ

> 祖父がSnoopに

### [037]

Timestamp: 01:34.120 – 01:35.100  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: He's spending the night with me."  
JP: こいつは今夜うちに泊まる」

### [038]

Timestamp: 01:37.040 – 01:38.950  
Speaker: Snoop Dogg  
Confidence: MED

EN: And so my grandpa was a G, you know what I'm saying?  
JP: だから じいちゃんはマジでGだったんだよ わかるだろ？

> a G / G はモデル差。G = gangster から来た「筋が通った強い男・本物」という褒め言葉。日本のHIP-HOPリスナー向けに G のまま

### [039]

Timestamp: 01:39.300 – 01:40.700  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: Mom couldn't break that, you know what I'm saying?  
JP: おふくろも そこは崩せなかった わかるだろ？

> break that = じいちゃんの守りを崩す

### [040]

Timestamp: 01:40.940 – 01:42.750  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: Like, that protector.  
JP: 守ってくれる存在っつうかさ

### [041]

Timestamp: 01:43.780 – 01:46.900  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: But despite mama being, you know, disciplinary,  
JP: でも おふくろは まあ 厳しかったけど

### [042]

Timestamp: 01:47.520 – 01:48.750  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: she was an amazing protector.  
JP: 最高に俺らを守ってくれた

### [043]

Timestamp: 01:49.380 – 01:51.600  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: Because when you were a single mother raising men  
JP: シングルマザーで 男の子を育ててたんだぜ

> raising men = 息子たち（Snoopと兄弟）を育てる

### [044]

Timestamp: 01:52.540 – 01:53.850  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: in the '70s and the '80s,  
JP: 70年代 80年代にさ

### [045]

Timestamp: 01:53.900 – 01:58.800  
Speaker: Snoop Dogg  
Confidence: MED

EN: and from what we was encountering and the things we was seeing when we was outside of our home,  
JP: 俺らが家の外で 出くわしてたことや 見てたもんを考えたら

> 2つ目の we was / we were、outside of / at はモデル差。AAVEの we was を維持

### [046]

Timestamp: 01:59.140 – 02:00.200  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: she did an amazing job.  
JP: おふくろは 本当によくやってくれたよ

### [047]

Timestamp: 02:00.960 – 02:04.000  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: And I understand now, as a father and a grandfather,  
JP: 今 父親として じいちゃんとして わかるんだ

> large-v3 は "as a, as a" と言い直しを聞いている。言い直しは字幕にしない

### [048]

Timestamp: 02:04.320 – 02:09.300  
Speaker: Snoop Dogg  
Confidence: HIGH

EN: how hard it is to raise a kid, or kids, when it's you by yourself.  
JP: 1人で子供を 子供たちを育てるのが どれだけ大変か

### [049]

Timestamp: 02:10.280 – 02:15.810  
Speaker: Host (woman, on camera at the end)  
Confidence: HIGH

EN: Do you feel like there's really a big difference between children that grow up with both their parents...  
JP: 両親そろって育った子と… 本当に大きな違いってあると思う？

> 質問の途中で動画が終わる（比較の相手「片親の子」は言われていない）。日本語も「…」で途切れを示す

## C. IMPORTANT TRANSLATION DECISIONS

**1. Papa（026, 030）**  
Original: "Papa, I got suspended." / "Don't tell her, Papa."  
Literal meaning: パパ  
Contextual meaning: 話の流れ（"My grandfather…", "my grandpa was a G"）から、ここの Papa は祖父への呼びかけ。  
Proposed Japanese: じいちゃん  
Reason: 「パパ」と訳すと父親と誤解される。004〜009 の your daddy（孫たちの父親）は「パパ」のまま。

**2. beat（002, 005, 019, 021, 027）**  
Original: "can't beat you" / "I will beat your daddy" / "I got beat"  
Literal meaning: 打ち負かす / 叩く  
Contextual meaning: 002・005 は孫に向けた冗談まじりの「勝てない・ぶっ倒す」。019・021・027 は母親のお仕置き（叩かれる）。  
Proposed Japanese: 勝てねえ / ぶっ倒す / シバかれる  
Reason: 同じ beat でも、孫の話（張り合い）と子供時代の話（体罰）で意味が違うため訳し分けた。

**3. holla at（010）**  
Original: "you come holla at Grandpa when you need something"  
Literal meaning: じいちゃんに声をかけに来い  
Proposed Japanese: 何か欲しい時は じいちゃんに言いに来な  
Reason: holla at = 連絡する・頼みに来る、のスラング。自慢げで温かい口調を残した。

**4. laid the law down（012）**  
Original: "I laid the law down with my grandbabies"  
Literal meaning: 孫に法律を敷いた  
Contextual meaning: 決まり・立場をはっきり言い渡した（半分冗談の自慢）。  
Proposed Japanese: 孫たちには ビシッと教えといたんだ

**5. whoop / Rasslin'（017, 024, 033）**  
whoop = 子供を叩いてしつけること →「シバく」。Rasslin' = wrestling の口語発音。昔のテレビのプロレス中継 →「プロレス」。Bonanza は60〜70年代のアメリカの西部劇ドラマで、固有名詞なので英語のまま。

**6. a G（038）**  
Original: "my grandpa was a G"  
Literal meaning: gangster  
Contextual meaning: 犯罪者という意味ではなく、筋の通った強い男・本物という褒め言葉。  
Proposed Japanese: じいちゃんはマジでGだったんだよ  
Reason: 日本のHIP-HOPリスナーには「G」で通じ、Snoopらしさも残る。「最強の男」「本物の漢」にする案もある。

**7. you ain't doing shit（032）/ ain't gonna do shit（028, 036）**  
Literal meaning: お前はクソも何もしない  
Contextual meaning: 祖父が母に「（この子に）手出しはさせない」と言っている。  
Proposed Japanese: お前は何もすんじゃねえぞ / 母ちゃんなんか何もできやしねえよ  
Reason: 罵倒ではなく「守る」意味の強調。英語字幕では s**t と伏せ字、音声はそのまま。

**8. 話者の切り替わり（034）/ on the back of the phone（035）**
034 から母のセリフになるので、日本語に「そしたらおふくろが」を補った。  
Original: "On the back of the phone: 'Please, mama…'"  
Contextual meaning: 祖父が母に電話している後ろで、子供のSnoopが母に向かって叫んでいる。  
Proposed Japanese: 後ろで俺が「ママ お願い もうしないから お願い！」

**9. 動画の終わり（049）**  
ホストの質問「両親そろって育った子どもと（片親の子で）本当に大きな違いがあると思う？」の途中で録画が終わる。比較の相手は言われていないので、日本語も「両親そろって育った子と…」で途切れを残した。

## D. UNCERTAIN EXPRESSIONS

| 行 | 時刻 | 内容 | 対応 |
|---|---|---|---|
| 025 | 66.9–68.8 s | "He said, ___, why you here so early?" の呼びかけ部分。モデルによって "Sonny"（低確率）/ "He's a funny" / "Son of a bitch" とばらばらで確定できない | 字幕から外し、"He said, "Why you here so early?"" とした。音声はそのまま残る |
| 008–009 | 20.9–21.5 s | "and thought, wow"（large-v3 区間・medium.en）/ "oh wow"（large-v3 全体・small.en）。Critic は、wow 以降は孫のセリフなので "oh wow" の方が自然と指摘 | "and thought," のまま。"I pulled out like $10,000," + "Oh wow, you have…" に変える案もあり。日本語はどちらでも同じ |
| 009 | 24.2 s | 末尾 "bro" は medium.en だけが聞いた | 字幕にしない |
| 029 | 76.0 s | "finna"（large-v3 0.97）/ "gonna"（medium.en） | finna を採用。意味は同じ |
| 034 | 88.4 s | "get out here" の "out" が低確率（3モデルで同じ語順） | そのまま採用。「帰ってきたら」は "get on (home)" でも成り立つ |
| 045 | 117.1 / 118.3 s | we was / we were, outside of / at | we was, outside of を採用。意味は同じ |

## E. TRANSLATION COVERAGE CHECK

```
SOURCE BEGINNING COVERED = YES（00:00.000, 文の途中から始まる）
SOURCE ENDING COVERED = YES（02:15.81, 質問の途中で終わる）
ALL RELEVANT SPEECH INCLUDED = YES（相づちの "yeah" のみ字幕なし）
ENGLISH TRANSCRIPTION CHECKED = YES（medium.en + large-v3 全編, 不一致区間を large-v3 / medium.en / small.en で再確認）
JAPANESE TRANSLATION COMPLETE = YES（49行）
LYRICS ANNOTATIONS CHECKED = N/A（1.lyrics.txt なし, 歌詞なし）
UNCERTAINTIES REPORTED = YES（§D）
TRANSLATION CRITIC = PASS（独立Critic, 1回目, 修正提案のうち4件を反映）（translation_qa.md）
```
