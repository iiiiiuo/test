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
TRANSLATION CRITIC = {CRITIC}（translation_qa.md）
```
