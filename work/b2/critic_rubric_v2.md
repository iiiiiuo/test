# Fresh Clip Critic: task and rubric

You are an independent reviewer of one finished vertical short clip. Judge only the evidence files listed for your clip. Do not modify any file except your own report. Do not assume quality you cannot see in the evidence; an item with missing evidence cannot PASS (mark it BLOCKED).

Series context: Japanese-subtitled 9:16 shorts cut from a Drink Champs interview with Ye. Display is English (top) + Japanese (below), plus an approved Japanese term-explanation row under them for some lines (item 10). The Japanese wording was approved by a human reviewer; do not FAIL a clip because you would phrase the Japanese differently. Flag a Japanese line only if it is clearly wrong against what is heard, attached to the wrong moment, missing, or unreadable.

Approved naming rules for the Japanese (do not flag these): most proper nouns are in English spelling (Drake, Ye, Kim, Puff Daddy, Quavo, Adidas, D'Usse …). These names are in katakana or a fixed form on purpose: スティーブ・ジョブズ, ジェフ・ベゾス, イーロン, ヘネシー, ティンバーランド, シャキールオニール, モーゼ, ブラックライブスマター, リュック系ラッパー, トランプ, ウォーレンバフェット, デニーズ, ウクライナ, アメリカ, ファレルウィリアムズ, Ralph Lauren, Black Mafia Family, トランプ支持者の赤の帽子 (the red MAGA hat).

English masking in the displayed English only (two asterisks, from the reference): s**t, f**k, f**king, f**ked, b**ch, ni**a, ni**as, motherf**ker(s), p**sy. The audio is uncensored on purpose.

## Items (give each PASS / FAIL / BLOCKED with one line of evidence)
1. Structure: natural opening (no mid-word or mid-thought start), coherent middle, resolved ending (not cut mid-sentence); understandable standalone. Use `qa/source_context.txt` (what was said just before/after) and `qa/sync.txt`.
2. Duration/format: `qa/auto.json` → format (1080x1920, SAR 1:1, 60.0 <= video and audio duration < 120.0, frame count = manifest, clean decode).
3. Transcript accuracy: displayed English vs what is actually heard in the render (`qa/sync.txt`, HEARD lines = an automatic transcript of the rendered audio, which can itself be slightly wrong). Flag meaningful mismatches, not filler words.
4. Translation fidelity: Japanese conveys the meaning of the English at that moment (approved wording; only clear errors).
5. Masking: displayed English masks the listed words; no unmasked hits; Japanese not mechanically masked.
6. Timing/sync: captions appear with their speech (onset close to first heard word, not lagging into the next sentence); no caption flashing too briefly to read; no long speech with no caption. Brief uncaptioned reactions (a laugh, "yeah", a single word, background crosstalk under a captioned speaker) are acceptable; an uncaptioned full sentence of foreground speech is a FAIL.
7. Typography/visuals vs reference: compare `qa/sheet_*.jpg` (and full-res `qa/f_*.png` if needed) with reference `work/b2/ref_sheet.jpg` / `work/b2/ref_*.png` and the style spec: white bold Yu Gothic, black outline+shadow, EN above JP, centred, similar size and vertical position, max 2 EN + 2 JP lines (the explanation row is judged in item 10), no clipping/overflow outside frame, readable on bright backgrounds.
8. Framing: speakers' faces/bodies naturally framed in the sharp centre band (not cut off at the head, not empty frame), blurred fill above/below like the reference; framing changes only at shot changes.
9. Source usage: `source_manifest.json` intervals are frame-exact half-open ranges from one source; no padding (silence, freeze, repetition); interval joins (if more than one interval) do not distort meaning.

10. Term-explanation row (added after reviewer approval): a third row of smaller white text (ASS style `Expl`) under the EN+JP block. Check that its text is the approved draft verbatim (`review/glossary/glossary_draft_s2.json`, key = line id; '／' separates terms and each term starts on its own line; spaces and line breaks may differ); that it is on screen while that line is spoken (it starts at the caption that shows the term) and long enough to read (about 2 s or more); that it never overlaps the EN/JP rows and stays inside the sharp band (y 438..1480); that it uses the same font, white fill, black outline and shadow; and that no line break splits a word or name awkwardly. Do not judge whether an explanation is needed or how it is worded: the reviewer approved the wording.

## Output
Write your report to `work/b2/<CLIP>/qa/critic.md` with this exact head, then the item list:

```text
VERDICT: PASS | FAIL
Blocking gaps: none | item + timestamp/frame + evidence (one line per gap)
Largest gap: none | one gap
Fix: none | concrete correction
```

FAIL only for blocking problems a viewer would notice or that break a hard rule (duration, format, unmasked word, wrong/missing subtitle, badly cut start/end, broken framing). Cosmetic suggestions go under a final "Non-blocking notes" heading. Your final message must repeat the four-line head.
