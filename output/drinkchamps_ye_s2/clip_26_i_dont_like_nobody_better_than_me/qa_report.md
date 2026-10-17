# Clip_26 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `a004f75aa1756ada7976dd6cb5d50f97c716f97a79e9c76d4c895309be79f772`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 82.165 s, audio 82.165 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1970 (manifest 1970)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1970, "expected_frames": 1970, "video_duration_s": 82.165416, "audio_duration_s": 82.165, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 177, "asr_words": 184, "matched": 160, "match_ratio": 0.904, "matched_words_inside_their_caption": 0.95, "caption_onset_vs_first_word_s": {"n": 24, "median": -0.061, "max_abs": 2.581}}

## Critic rounds
- round 1: PASS — non-blocking: 'Right.' caption lags ~0.9 s at 60.01 → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 82.165 s / audio 82.165 s, 1970 frames = expected, no decode errors.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits empty; srt/ass contain no profane words (none spoken-displayed in this clip); JP not mechanically masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - f_0073.60.png and f_0036.08.png vs ref_20.png: white bold Yu Gothic, black outline+shadow, centred, EN above JP, same vertical area (y~950-1100), max 2 EN + 2 JP lines, no clipping.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS - L014 Expl text "『Watch the Throne』：2011年の / Jay-ZとYeの共作アルバム" matches glossary draft verbatim (break only after の); on screen 70.35-76.55 s (6.2 s), starting at the caption showing "Watch the Throne" and covering L015 which repeats it; Expl at y 1188/1236 (fs40, style Expl: Yu Gothic bold, white, black outline, shadow) sits below the JP row (ends ~1160 in f_0073.60.png) with no overlap, inside band 438..1480; no name split.

Non-blocking notes: none.

