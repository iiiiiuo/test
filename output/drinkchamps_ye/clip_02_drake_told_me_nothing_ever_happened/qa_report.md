# Clip_02 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `ffcec172bbbc1b2d1885e018555938fdab628189fe75effa21e9b13fc5956f51`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 74.116 s, audio 74.116 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1777 (manifest 1777)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1777, "expected_frames": 1777, "video_duration_s": 74.115708, "audio_duration_s": 74.116, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 197, "asr_words": 195, "matched": 187, "match_ratio": 0.949, "matched_words_inside_their_caption": 0.979, "caption_onset_vs_first_word_s": {"n": 21, "median": 0.094, "max_abs": 1.816}}

## Critic rounds
- round 1: FAIL — final shot framed on backdrop crest; opening edge → framing fix; start moved to quiet point before Yeah (large-v3 span re-check confirms Yeah)
- round 1: FAIL — L014 caption 3.8 s early over laughter → same timing rules (caption now 70.81)
- round latest: FAIL — final shot crop put laughing Ye at left edge (3/10 detections) → manual crop x=420 for frames 40930-41110 (framing_overrides.json)

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 4 for Clip_02_L006, 5, 7, 10)
1. NOT IN SCOPE
2. PASS - auto.json: 1080x1920, SAR 1:1, video 74.116 s / audio 74.116 s (60 <= d < 120), 1777 frames = expected 1777, decode_errors empty.
3. NOT IN SCOPE
4. PASS (L006 only) - "So when I went to the White House, I saw Jared." -> "で、ホワイトハウスに行った時 / Jaredに会ったんだよ" = approved ja_final in rev4; shown at 29.81-31.65 and 32.04-33.39, matches HEARD in sync.txt.
5. PASS - auto.json unmasked_hits empty; EN shows "f**k" (7, 21.73-24.84); no other listed words in SRT; Japanese not mechanically masked (ヤった).
6. NOT IN SCOPE
7. PASS - f_0019.10.png and f_0053.38.png: white bold Yu Gothic, black outline/shadow, EN above JP, centred, 2 EN + 2 JP lines max, inside frame, readable; ASS PlayRes 1080x1920, style Sub Yu Gothic bold.
8. NOT IN SCOPE
9. NOT IN SCOPE
10. PASS
 - Text verbatim vs glossary: Clip_02_L004 "Jared Kushner：トランプ元大統領の娘婿／Steve Stoute：音楽・広告業界の実業家" (two terms, each on own line); Clip_02_L010 "「何もなかった」：DrakeとYeの元妻Kimの間に、という意味" (wrapped after "Yeの", no word/name split).
 - Timing: L004 row 16.50-24.84 (8.3 s) starts with the caption showing both names; L010 row 51.83-56.99 (5.2 s) starts with the caption "nothing ever happened" (SRT 20/21).
 - Geometry: Expl rows at y=1188 and 1236 (fs40), below the lowest EN/JP row (4-line block ends ~1150 in f_0053.38.png); inside sharp band y 438..1480; no overlap seen in frames.
 - Style: Expl uses Yu Gothic bold, white fill, black outline 3, shadow 2 (same as Sub), smaller size; visible in both frames.

Non-blocking notes
- Explanation rows sit close under the 4-line caption block (about 40 px gap); acceptable.

