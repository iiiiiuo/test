# Clip_09 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `8ea513c487762b436b73b58c9d438f2d7273b36a656994bf66584c9b5f4e81b1`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 64.815 s, audio 64.815 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1554 (manifest 1554)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1554, "expected_frames": 1554, "video_duration_s": 64.81475, "audio_duration_s": 64.815, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 175, "asr_words": 188, "matched": 162, "match_ratio": 0.926, "matched_words_inside_their_caption": 0.951, "caption_onset_vs_first_word_s": {"n": 19, "median": -0.043, "max_abs": 1.623}}

## Critic rounds
- round 1: FAIL — ended on dangling "But it's funny," → end moved to after "...thousand back." (247.125 s); JP tail segment 笑えるよな dropped (approved segments only)
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items
1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 64.81475 s / audio 64.815 s (60.0 <= d < 120.0), 1554 frames = manifest 4371..5925, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits empty; no profane words in subtitles.ass/srt or in sync.txt HEARD lines (grep for shit/fuck/bitch/nigg/pussy: none); JP has no asterisks.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - f_0004.24.png and f_0053.84.png vs ref_20.png: white bold Yu Gothic, black outline+shadow, EN above JP, centred, same size and vertical position (EN first line y~975, as in reference), max 2 EN + 2 JP lines, no clipping, inside sharp band, blurred fill above/below. ASS styles Sub/Expl use Yu Gothic bold, white, black outline/shadow.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS (no rows) - glossary_draft_s1.json has no Clip_09_* keys (0 matches), and subtitles.ass has no Expl events (0 matches), so no explanation row is expected or present. No frames needed; nothing missing, nothing overlapping.

Non-blocking notes
- Style Expl is defined in the ASS but unused for this clip, which is consistent with the glossary.

