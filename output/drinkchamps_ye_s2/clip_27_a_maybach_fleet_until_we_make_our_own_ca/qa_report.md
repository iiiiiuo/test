# Clip_27 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `f0342ff00defe43190bad0c24e440a2c413a5075ca9b46ea411c83d5c41c7063`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 66.858 s, audio 66.858 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1603 (manifest 1603)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1603, "expected_frames": 1603, "video_duration_s": 66.858458, "audio_duration_s": 66.858, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 230, "asr_words": 229, "matched": 189, "match_ratio": 0.822, "matched_words_inside_their_caption": 0.894, "caption_onset_vs_first_word_s": {"n": 16, "median": -0.098, "max_abs": 2.898}}

## Critic rounds
- round 1: FAIL — 0.40 s flash caption 'But it's like,' at 55.57 → chunks override Clip_27_L012 (one caption)
- round 2: FAIL — opens inside 'Because'; ends while 'manner' sounding → hand windows start 657.98-658.06, end 724.86-724.94
- round 3: PASS — non-blocking: framing shows host 0.6-4.4 s → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json 1080x1920, SAR 1:1, video 66.858 s / audio 66.858 s, 1603 frames = expected, no decode errors.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits empty; ASS shows only "s**t" (x2, 43.49 and 50.29); no other listed words; Japanese not masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - f_0016.41 and f_0061.80 vs ref_20: white bold Yu Gothic, black outline+shadow, EN above JP, centred, same vertical start (~y 950), max 2 EN + 2 JP lines, nothing clipped, readable.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
 - Text verbatim vs glossary Clip_27_L004 (ウォーレンバフェット：アメリカの著名な投資家) and Clip_27_L013 (Black Mafia Family：1990〜2000年代にデトロイトで生まれた麻薬組織。ドラマ『BMF』の題材); L013 only line-broken after "デトロイトで", no word split.
 - Timing: Buffett 15.46-20.08 (4.6 s), starts with the JP caption naming him; BMF 59.97-66.86 (6.9 s), starts with caption showing "legal BMF / Black Mafia Family".
 - Placement: Expl y 1188 and 1236 (fs40), visible gap below the JP row (ends ~y 1145) in both frames, no overlap; within sharp band (<=~1290, limit 1480).
 - Style Expl: Yu Gothic bold, white, black outline 3 + shadow 2, same as Sub.

Non-blocking notes: none.

