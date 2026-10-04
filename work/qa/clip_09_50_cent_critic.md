# Fresh Clip Critic — clip_09_50_cent

Artifacts (sha256):
- render.mp4 0dbcdd2a5aa660a060d5d4d30f58f6e23d1b873b1a5c1b296f2bbec6bbab11cc
- subtitles.ass ffd04441c5da04f66316ad56199dfd00493668d18e3543700ac5aef58dbf2f74
- subtitles.srt b5a9f8a3c03b0b411a6f097aee4e0b2eea81965805dcc1f34c37a6e7d7bd76e5
- source_manifest.json 4fa18e9e8d4b339cc1dfd666c2f44253b2a5dd334f6a42debbc7e10d3198fe71

Output-time joins (from manifest): 26.360, 30.497, 67.434, 69.135, 75.036 s.

## 1 structure — PASS
DJ Envy's question (shot, 50 moving militant, "how would those conversations have happened") sets up; guest answers he and 50 are different, Many Men remix anecdote, gangster-image/role-model, "at his age I would not be doing", too old for trolling, 25 years older, ends on "he didn't even come down to this level and troll me". Standalone and coherent. Remix anecdote reads fine with "Niggas gassed me" excluded.

## 2 duration — PASS
ffprobe: video 78.278200 s, audio 78.278005 s, format 78.278200 s; 1080x1920, 30000/1001. Manifest 2346 frames x 1001/30000 = 78.2782 s.

## 3 transcript accuracy — FAIL
Spot checks (faster-whisper large-v3 on source via check_span.py, plus render-audio passes):
- 649.30-654.66 (out 0.0-4.6): matches captions 1-4. PASS.
- 682.20-690.16 (out 30.5-38.8): "but in reality I do feel like we different ... it's just my shoes" matches 17-20 (AAVE "we different" preserved). PASS.
- 676.48-680.42 (out 26.4-30.5): "I just went high as fuck, I press(ed) upload, niggas like what the fuck" matches 14-16. PASS.
- 725.12-727.58 (out 69.1-71.6): "Like you said, he too old for the trolling that he does" matches 37. PASS.
- 732.57-735.49 (out 75.0-78.3): "...didn't even come down to this level and troll me right now" matches 40. PASS.
- 729.28-730.82 (out 73.4-74.9): "He got me in/on 25 years" (in 0.59 / on 0.40-0.67) — meaning unaffected. PASS.
- **GAP A** caption 38 (out 71.67-73.15, src 728.16-728.64) "Yeah, you feel me?": the words after "Yeah" are unresolvable. large-v3 x2: "for me" (0.48/0.57); small.en: "for me"; large-v2: "For me" (0.12); distil-large-v3: "family" (0.53); medium: "Family!" (0.11); render-audio large-v3: "it"(0.05). Displayed "you feel me?" is a guess.
- **GAP B** caption 36 (out 67.44-69.19, src 722.25-723.96) "For me, a lot of the s**t he do, I would not do.": the final "do" (src ~723.9-724.04) is cut by the segment end 723.957; render audio transcribes "...I would not" twice (render 67.3-69.135 and 65.5-70.0). "the" also unconfirmed (absent in 2 of 3 passes, 0.56 in the third).

## 4 translation — PASS
JP faithful and natural: 「結局は俺の立場の問題」 for "it's just my shoes", 「俺より25も上だぜ」 for "he got me in 25 years", 「あの歳であの煽りはないって」, 「俺も50は好きだしさ」 for "I f**k with 50 too". Casual male register, no dialect stereotype. (Caption 38 JP 「そう、わかる？」 inherits Gap A.)

## 5 masking — PASS
f**k (14, 16), ni**as (16), f**k with (30), s**t (33, 36) consistent; JP unasterisked (16 「なんだこれ？」, 30 「好き」).

## 6 timing — FAIL (minor, linked to join)
No overlaps (SRT sequential, 20 ms gaps), min dwell ≥0.8 s, onsets within 0.3 s at checks (e.g. "I just" render 26.32-26.48 vs cap 26.50; "Yeah" 71.94 vs 71.67).
- **GAP C** out 30.26-30.50: audible "Nigga" (render-audio large-v3 0.59-0.77; src word 682.22-682.54) at the start of segment 3 is uncaptioned (caption 16 still shows "What the f**k is that?", 17 starts 30.72) and the word is clipped mid-word by the segment start 682.315.

## 7 visuals — PASS
Frame 68.0 s vs reference r_30 (scaled 1.5x): same Yu Gothic Bold look, white fill, black outline + shadow, EN above JP, centered, first line top ~948. ASS: Yu Gothic, EN 54 / JP 50, outline 3, shadow 2. No clipping/overflow in 17 sampled frames (0.5-77.5 s).

## 8 framing — PASS
17 sampled frames: guest close-ups (x0=430) face centered in sharp band, Envy (x0=610) and Jess (x0=700, 71 s) natural; wide punch-ins on guest fine. Camera reaction cuts are source-native.

## 9 editing — FAIL
No padding/repeats; joins do not distort meaning. But joins at 30.497 (Gap C, mid-word "Nigga" fragment) and 69.135 (Gap B, "do" truncated; RMS -19 dB speech then -55 dB) are not clean.

## 10 source usage — PASS
Six half-open intervals sum to 790+124+1107+51+177+97 = 2346 frames = render length; excluded spans respected; audio sample ranges match video segments.

## VERDICT: FAIL
Largest gap: A (caption 38 guessed words).
Fixes:
- A: split segment 5 to drop src ~728.10-728.70 (keep "Yeah" ending ~728.0, resume before "He got me" at ~729.28; e.g. frames [21732,21822) + [21841,21909)), caption 38 → "Yeah." / 「そう」.
- B: end segment 4 after "do" tail (~724.06, frame 21700) if 723.96-724.06 holds only that word tail, else caption "I would not." and drop "the" ("a lot of s**t he do").
- C: start segment 3 at ~682.55 (frame 20457) after the clipped "Nigga", or include the whole word and caption it "Ni**a." / JP 「なあ」-free equivalent.
