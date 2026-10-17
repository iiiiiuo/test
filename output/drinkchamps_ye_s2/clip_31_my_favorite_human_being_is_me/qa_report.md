# Clip_31 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `e8257cd5454b4856b512e44891609f3440a71bcc45ab6daec2e605bd1c4adfb1`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 70.529 s, audio 70.529 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1691 (manifest 1691)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1691, "expected_frames": 1691, "video_duration_s": 70.528791, "audio_duration_s": 70.529, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 198, "asr_words": 195, "matched": 181, "match_ratio": 0.914, "matched_words_inside_their_caption": 0.945, "caption_onset_vs_first_word_s": {"n": 23, "median": -0.145, "max_abs": 2.125}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items
1. Structure: NOT IN SCOPE (no blocking problem noticed).
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 70.529 s, audio 70.529 s (60 <= d < 120), 1691 frames = expected 1691, decode_errors empty.
3. Transcript: NOT IN SCOPE.
4. Translation: NOT IN SCOPE (CHANGED_LINES = none).
5. Masking: PASS. auto.json unmasked_hits empty; srt grep finds no unmasked listed words; frame f_0009.06 shows "ni**a's"; Japanese not mechanically masked.
6. Timing: NOT IN SCOPE.
7. Typography/visuals: PASS. f_0002.70 and f_0009.06 vs ref_20: white bold Yu Gothic, black outline + shadow, EN above JP, centred, same vertical position/size as reference, max 2 EN + 2 JP lines, no clipping, readable on the white shirt.
8. Framing: NOT IN SCOPE.
9. Source usage: NOT IN SCOPE.
10. Term-explanation row: PASS. Single term for Clip_31_L001; ASS text "Common：シカゴ出身のラッパー・俳優。" / "本名はLonnie Rashid Lynn" matches the glossary draft verbatim, split at the sentence stop (no word broken). On screen 0.00-7.70 s (7.7 s), starting with the caption that shows "Common" (EN caption 1 at 0.00-5.40, continuing through the Denny's captions). Style Expl, Yu Gothic bold, white fill, black outline, shadow; rows at y 1188 and 1236 (about 1170-1265 rendered), clear of the JP row ending about 1145 and inside the sharp band 438..1480 (f_0002.70).

Non-blocking notes
- Expl row stays up through the following Denny's captions to 7.70 s, which is acceptable.

