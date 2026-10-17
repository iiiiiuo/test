# Clip_12 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `9fa1c9bcb5f083457d7aacde209d9d7777036ad1b70d966d260605c013551a4c`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 65.524 s, audio 65.524 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1571 (manifest 1571)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1571, "expected_frames": 1571, "video_duration_s": 65.523791, "audio_duration_s": 65.524, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 176, "asr_words": 181, "matched": 165, "match_ratio": 0.938, "matched_words_inside_their_caption": 0.97, "caption_onset_vs_first_word_s": {"n": 20, "median": 0.066, "max_abs": 1.374}}

## Critic rounds
- round latest: FAIL — end cut inside "away" → end moved to 1093.07 (frame 26207)

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json 1080x1920, SAR 1:1, video 65.524 s / audio 65.524 s, 1571 frames = expected, no decode errors.
3. Transcript: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES none)
5. Masking: PASS - ASS shows ni**as, f**k, b**ch, f**king; auto.json unmasked_hits empty; Japanese not mechanically masked.
6. Timing: NOT IN SCOPE
7. Typography/visuals: PASS - frames f_0002.89, f_0013.30, f_0064.52 vs ref_20: white bold Yu Gothic, black outline+shadow, EN above JP, centred, same position/size as reference, no clipping, 2 EN + 2 JP lines max.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
- L002 Roscoe's (ASS 1.37-8.17, 6.8 s): text verbatim; frame f_0002.89 inside span: single line, ink ~725 px wide, clear of JP row (JP bottom ~1145, Expl top 1188), within sharp band.
- L003 Usher (10.46-16.53, 6.1 s): text verbatim; frame f_0013.30 inside span: breaks after "は", "2001年のヒット曲" on line 2; no split of name/title; clear of JP rows.
- L012 40エーカー (61.80-65.52, 3.7 s, ends at clip end): text verbatim; frame f_0064.52 inside span: breaks after "に" (no word split); 4-row block ends ~1145, Expl 1188-1284, inside band (<=1480).
- All three start with the first caption showing the term and last >= 3.7 s; no overlap between explanations; same font, white fill, black outline and shadow as EN/JP, 40 px size.

Non-blocking notes: none.

