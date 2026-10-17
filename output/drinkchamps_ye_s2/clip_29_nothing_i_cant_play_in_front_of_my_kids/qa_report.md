# Clip_29 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `f10f5c2b6be44ae620db47dadf46fa735f63ff8fcf61eed7f2688dcb0f6ede62`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 73.991 s, audio 73.990 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1774 (manifest 1774)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1774, "expected_frames": 1774, "video_duration_s": 73.990583, "audio_duration_s": 73.99, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 248, "asr_words": 258, "matched": 242, "match_ratio": 0.976, "matched_words_inside_their_caption": 0.967, "caption_onset_vs_first_word_s": {"n": 25, "median": 0.036, "max_abs": 0.614}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 73.990583 s, audio 73.99 s, 1774 frames = expected, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits empty; grep of subtitles.srt for s/f/b/n/p/motherf* words finds none; no profanity in EN lines; JP not mechanically masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - f_0004.60.png and f_0011.22.png: white bold Yu Gothic, black outline+shadow, EN above JP, centred, 2 EN + 1-2 JP lines, same layout as reference, inside frame, no clipping.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
 - Text verbatim vs glossary_draft_s2.json: L001 two terms (True Love / Kim), each on its own line, at ASS 0:00.00-0:08.67 (8.67 s, covers captions 1-2 that show the terms); L003 "Chicago：YeとKimの娘の名前" at 10.14-13.61 (3.47 s), starts with the Chicago caption.
 - Style Expl: Yu Gothic bold, white fill, black outline, shadow, 40 pt; confirmed in frames at 4.60 s and 11.22 s.
 - Position y 1188/1236 (row bottom about 1260), below the last JP row (pos 1098/1048, bottom about 1150), no overlap with EN/JP; inside sharp band 438..1480.
 - No word/name split across lines; widest line (L001 term 1) fits within 1080 with margin.

Non-blocking notes: none.

