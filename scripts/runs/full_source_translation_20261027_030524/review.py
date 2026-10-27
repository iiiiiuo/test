import json,sys
S=sys.argv[1]; d=json.load(open(S+'/transcription.json'))
def ts(x): m=int(x//60); return f"{m:02d}:{x-60*m:06.3f}"
o=[]
o.append("# SOURCE_VIDEO.mp4 全編和訳レビュー（v1）\n")
o.append("""## A. SOURCE INFORMATION

```
Source:
SOURCE_VIDEO.mp4（2026-10-27添付, sha256 6a4e1cf5…a996）

Source Duration:
130.714 s（映像 130.697 s / 3917フレーム @29.97fps, 音声 Opus 48kHz 130.714 s）

Translation Coverage:
00:00.000 – 02:10.714

Translation Status:
PENDING HUMAN APPROVAL
```

内容: Velocity「Inside West Coast Customs」の一場面。West Coast CustomsオーナーのRyan Friedlinghausが、Travis Scottにブラウンの Lamborghini Aventador をお披露目する。途中にTravisのインタビュー、最後にRyanのカメラ向けコメント。全編にBGMあり。

- `1.lyrics.txt` はリポジトリ・input/・プロジェクトフォルダのどこにもないため N/A（会話中心の動画で、歌詞は025の1行のみ）。
- 以前の `/mnt/project-files/SOURCE_VIDEO.mp4`（747.8秒のBreakfast Clubインタビュー）とは別の動画です。今回は添付ファイルだけを使います。
- タイムスタンプはASRによる推定値（秒）。フレーム単位の調整はPHASE 2で行います。
- 信頼度: HIGH = 3回の認識が一致 / MED = 細部が不一致 / LOW = 要判断。
- 英語字幕で伏せ字が必要な語はありません（"Damn" はマスク対象外）。
- 固有名詞は英語表記（Travis, Lambo, SV）。

## B. COMPLETE ENGLISH / JAPANESE TRANSLATION
""")
for l in d['lines']:
    jp=l['jp'].replace("\n"," / ")
    o.append(f"### [{l['id']}]\n\nTimestamp: {ts(l['start'])} – {ts(l['end'])}  \nSpeaker: {l['speaker']}  \nConfidence: {l['confidence']}\n\nEN: {l['en']}  \nJP: {jp}\n"+(f"\n> {l['note']}\n" if l['note'] else ""))
o.append("### 発話のない区間（字幕なし）\n")
for n in d['non_speech']:
    o.append(f"- {ts(n['start'])} – {ts(n['end'])}: {n['disposition']}")
o.append("""
（JP欄の「 / 」は字幕の改行位置の案です）

## C. IMPORTANT TRANSLATION DECISIONS

**011 "We won't talk about nothing."**
- Literal meaning: 「何でもないことについて話さない」
- Contextual meaning: 口語・AAVEの二重否定で「何ひとつ話さない」。
- Proposed Japanese translation: 一切ナシだ
- Reason: 二重否定を強調として訳した。英語字幕は話した通りに残す。

**015〜016 "Kind of bringing it back to the old days. / We covered it…"**
- Contextual meaning: 昔のWest Coast Customsのように、布をかぶせて見せる演出に戻したということ。
- Proposed Japanese translation: 昔ながらのやり方でいくよ / チラ見されたくなかったから カバーかけといた

**019 "it all comes together when you see this interior"**
- Literal meaning: 内装を見るとすべてがひとつになる
- Contextual meaning: 外装の色と内装（茶色のスエード）がそろって、コンセプトが完成する。
- Proposed Japanese translation: この内装見たら全部しっくりくるんだ

**022 "the factory SV"**
- Contextual meaning: 純正の Aventador SV（SuperVeloce）のシートのステッチ模様を、そのまま再現したということ。
- Proposed Japanese translation: 純正とまったく同じパターンにしたから ちゃんと純正のSVに見えるんだ
- Reason: SVは型式名なので英語のまま。

**023 / 035 / 036 / 034 などのスラング**
- fire = 最高・イケてる → 「最高」
- dope = 最高 → 「最高」
- crazy は驚きと称賛の意味 → 「ヤバい」
- mad = 「すごく・めっちゃ」（mad colors, mad thankful）→ 「めっちゃ」「マジで」

**031 "ready to run off this camera right now"**
- Literal meaning: このカメラから走り去る準備ができている
- Contextual meaning: インタビューを抜け出して、今すぐ車に乗りに行きたい。
- Proposed Japanese translation: もう今すぐカメラの前から 飛び出したいくらいだよ
- Reason: 「カメラを放り出す」とすると意味が変わるため、QAの指摘で修正済み。

**025 "for this life I cannot change"（歌詞）**
- Literal meaning: この人生は変えられない
- Contextual meaning: Travis Scottの曲の歌詞（「Butterfly Effect」冒頭の一節と一致）。「これが俺の生き方」という意味。
- Proposed Japanese translation: この生き方は変えられねえ
- Reason: 会話ではなくBGMの歌（またはTravisの口ずさみ）。字幕にするかどうかを決めてください（D-1）。

## D. UNCERTAIN EXPRESSIONS（ご判断ください）

1. **025（01:08.2–01:10.8）歌詞**: 「♪」付きで字幕にするか、字幕なしにするか。提案は**字幕にする**（意味が取れて、映像のテンションにも合うため）。
2. **026（01:12.2–01:13.7）**: 聞き取り不能。認識結果が "It didn't heal" / "It in here" / "It ain't him" / "It is here" とばらばら。続きの歌詞 "Hidden Hills" の可能性はありますが確認できないので、**字幕なし**にします。
3. **017（00:27.2–00:27.8）"Ooh!"**: 弱い歓声で、認識の信頼度が低いです（p=0.12〜0.44）。提案は**字幕なし**（入れる場合は「おお！」）。
4. **016 "Pull it off."**: 1つのモデルは "Let's pull it off." と認識。"Let's" が確認できないため、"Pull it off." としています。
5. **024 "Look crazy."**: "You look crazy" / "They're crazy" / "Crazy" の可能性あり。主語は不確定です。訳「見た目ヤバすぎ」はどれでも成り立ちます。
6. **038〜039 "Let's do it." ×2**: 話者不明。間にもう1回短い "Let's do it" が重なっている可能性があります。広めの区間で再認識しても "Let's do it!" で一致しました。
7. **005 "Yeah."**: 1回だけ "Man" と認識されました。
8. **話者**: 001・003・005・007・013・015・017 の短い返事は、映像から見てTravisの可能性が高いですが、確定ではありません。字幕には話者名を出さないので、表示には影響しません。

## E. TRANSLATION COVERAGE CHECK

```
SOURCE BEGINNING COVERED = YES   （00:00–00:02.8 は発話なしのロゴ演出）
SOURCE ENDING COVERED = YES      （最後の発話 02:06.7、以降は発話なし）

ALL RELEVANT SPEECH INCLUDED = YES
ENGLISH TRANSCRIPTION CHECKED = YES  （large-v3 ×2設定 + medium.en、独立Criticが再認識）
JAPANESE TRANSLATION COMPLETE = YES  （026のみ聞き取り不能のため字幕なし案）

LYRICS ANNOTATIONS CHECKED = N/A     （1.lyrics.txt なし）
UNCERTAINTIES REPORTED = YES

TRANSLATION CRITIC = PASS          （初回FAIL 2件 → 修正 → 再検査PASS。詳細は translation_qa.md）
```
""")
open(S+'/translation_review.md','w').write("\n".join(o))
