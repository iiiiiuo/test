# Clip_32 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `26e3c8f321b6adbff1e9d989afb9934aaa704e8a0cdd63228bc1447109c7a11d`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 95.637 s, audio 95.637 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2293 (manifest 2293)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2293, "expected_frames": 2293, "video_duration_s": 95.637208, "audio_duration_s": 95.637, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 263, "asr_words": 266, "matched": 247, "match_ratio": 0.939, "matched_words_inside_their_caption": 0.947, "caption_onset_vs_first_word_s": {"n": 32, "median": -0.127, "max_abs": 1.367}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items
1. NOT IN SCOPE
2. PASS - auto.json: 1080x1920, SAR 1:1, video 95.637 s / audio 95.637 s, frames 2293 = expected, decode_errors empty.
3. NOT IN SCOPE
4. PASS (no changed lines listed; nothing to check).
5. PASS - no unmasked hits in srt/captions.json/ASS (auto.json unmasked_hits empty; grep of srt and sync.txt finds none). No curse words occur in the clip; Japanese not mechanically masked.
6. NOT IN SCOPE
7. PASS - sheet_1.jpg and f_0088.66.png vs ref_sheet.jpg: white bold Yu Gothic, black outline+shadow, EN above JP, centred, similar size and position, max 2 EN + 2 JP lines, inside sharp band, no clipping.
8. NOT IN SCOPE
9. NOT IN SCOPE
10. PASS (N/A) - glossary_draft_s2.json has no Clip_32 keys; captions.json explanations = []; ASS has no Expl events (only the style definition). No explanation row expected, none rendered.

Non-blocking notes: none.

