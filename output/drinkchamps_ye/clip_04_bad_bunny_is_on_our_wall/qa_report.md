# Clip_04 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `32440448fcca5ed46283269f904aa0dfe404bb74a255cd23ac8cb17d8d2dd334`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 75.117 s, audio 75.117 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1801 (manifest 1801)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1801, "expected_frames": 1801, "video_duration_s": 75.116708, "audio_duration_s": 75.117, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 248, "asr_words": 251, "matched": 218, "match_ratio": 0.879, "matched_words_inside_their_caption": 0.995, "caption_onset_vs_first_word_s": {"n": 32, "median": 0.08, "max_abs": 0.48}}

## Critic rounds
- round 1: FAIL — false face (backdrop crest) framing 43-52 s; LOW lines L015-L017 captioned as a guess → crest saturation filter + cluster consistency in framing; jump cut removing L015-L017
- round 1: FAIL — "Stadium. Bad Bunny..." one 5.9 s caption ~3 s early → same pause-break rule (split "Stadium." / "Bad Bunny...")
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 75.117 s / audio 75.117 s, 1801 frames = expected, no decode errors.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits empty; no profanity in displayed EN in subtitles.ass; JP not asterisked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - frames f_0001.65 and f_0074.12 vs ref_20: white bold Yu Gothic, black outline+shadow, EN above JP, centred, same size/position as reference, max 2 EN + 2 JP lines, no clipping.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation rows: PASS
 - Clip_04_L001 (James Blake / Arca / No I.D.): text verbatim vs glossary_draft_s1.json, one term per line; on screen 0.20-9.91 s (9.7 s) from the first caption; judged from actual render frame f_0001.65 (inside span): rows at y 1188/1236/1284 (ink about 1190-1320), clear of the 4-line EN/JP block (ends about 1150), inside band 438..1480, same font/white/outline/shadow, smaller than Sub, no awkward breaks.
 - Clip_04_L024 (Saudi): text verbatim; on screen 71.65-75.12 s (3.47 s) starting with the caption that shows "Saudis"; judged from f_0074.12 (inside span): single row y 1138 (ink about 1140-1175), below the 2-line EN/JP block (ends about 1050), inside band, same styling, no line break.
 - Explanation rows exist only for L001 and L024, the two keys in the glossary for Clip_04; no extras.

Non-blocking notes
- f_0000.05 is before the first caption/explanation (0.20 s), so it was not used for judging.

