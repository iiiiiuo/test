# Clip_25 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `52d8896bab9921cfcf5ac55e0795eaefd246d1345603808dd4b57c462a57d1cf`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 76.076 s, audio 76.076 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1824 (manifest 1824)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1824, "expected_frames": 1824, "video_duration_s": 76.076, "audio_duration_s": 76.076, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 227, "asr_words": 217, "matched": 206, "match_ratio": 0.907, "matched_words_inside_their_caption": 0.956, "caption_onset_vs_first_word_s": {"n": 27, "median": 0.059, "max_abs": 1.739}}

## Critic rounds
- round 1: PASS — note: opening trims ~0.2 s of 'And I' → interval 1 start moved to 1108.40-1108.46 window
- round 2: PASS — non-blocking: low-level tail of 'and' in first 0.35 s → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 4 [no changed lines], 5, 7, 10; others NOT IN SCOPE, no blocking problem noticed)
1. NOT IN SCOPE
2. PASS - auto.json: 1080x1920, SAR 1:1, video 76.076 s = audio 76.076 s, 1824/1824 frames, no decode errors.
3. NOT IN SCOPE
4. PASS / nothing to check - CHANGED_LINES = none.
5. PASS - auto.json unmasked_hits empty; displayed "f**ked" (~35 s) and "f**ks" (56.64 s); sync.txt HEARD has the uncensored words; Japanese not mechanically masked.
6. NOT IN SCOPE
7. PASS - frames/sheet_2 and extra/m.png: white bold Yu Gothic, black outline and shadow, EN above JP, centred, max 2 EN + 2 JP lines, no clipping, readable on the bright white shirt and gold background.
8. NOT IN SCOPE
9. NOT IN SCOPE
10. PASS - four rows in the ASS, all verbatim against glossary_draft_s2.json (L010 Gangster Disciples, L012 Larry Hoover, L014 Drink Champs, L016 Tucker Carlson); each splits into 2 lines at a natural break, none inside a word or name. Style Expl (Yu Gothic, 40 px, white, black outline, shadow). Positions y=1188/1236, below the JP rows (last at y=1098 plus about 50) and inside the sharp band 438..1480; no overlap in frames at 45, 51, 58, 62 s. Durations 4.08, 6.48, 3.98, 6.98 s.

Non-blocking notes
- L016 Tucker Carlson: the term appears in the caption at 60.18 s but the explanation starts at 60.64 s (0.46 s late). Gangster Disciples (44.34), Larry Hoover (48.44) and Drink Champs (56.64) start with their captions. Still readable for 6.98 s.

