# Clip_37 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `f9adf91f6f827726dba7a7ec91f47f9b4d5e96af8754f43932101698b4c502c8`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 67.150 s, audio 67.150 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1610 (manifest 1610)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1610, "expected_frames": 1610, "video_duration_s": 67.150416, "audio_duration_s": 67.15, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 208, "asr_words": 207, "matched": 184, "match_ratio": 0.885, "matched_words_inside_their_caption": 0.978, "caption_onset_vs_first_word_s": {"n": 23, "median": 0.06, "max_abs": 1.86}}

## Critic rounds
- round 1: PASS — cosmetic: caption 4 onset ~1.9 s before words (host stutter) → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 5, 7, 10; item 4 CHANGED_LINES = none)
1. Structure: NOT IN SCOPE
2. Duration/format: PASS. auto.json 1080x1920, SAR 1:1, video 67.150 s, audio 67.15 s, 1610 frames = expected, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (no changed lines)
5. Masking: PASS. auto.json unmasked_hits = []; displayed English in all 25 captions contains no listed word; JP not mechanically masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS. Frames f_0012.64, f_0065.66 and extra/x_24,31,36,40 show white bold Yu Gothic, black outline and shadow, EN above JP, centred, same size and y as ref_20; max 2 EN + 2 JP lines; nothing clipped; readable on bright background.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS. Text matches glossary_draft_s2.json verbatim for all 6 rows (L004, L007 two terms, L008, L009, L010, L016); '／' split into separate lines. Checked in a render frame inside each span:
 - L004 11.02-18.39 (f_0012.64): "Tremaine..." 2 lines, break after "Supremeの".
 - L007 20.32-28.34 (extra/x_24, t=24): Pete Davidson and Skete each on own line, 3 lines.
 - L008 29.42-33.98 (extra/x_31, t=31): one line.
 - L009 34.00-37.98 (extra/x_36, t=36): 2 lines, break after "を".
 - L010 38.00-41.08 (extra/x_40, t=40): one line.
 - L016 64.18-67.15 (f_0065.66): 2 lines, break after "創業者。".
 All durations are 2.97 s or more. Rows sit at y about 1188-1300, below the JP rows (bottom about 1150) with no overlap, and inside the sharp band 438..1480. Same font, white fill, black outline and shadow, smaller size.

Non-blocking notes
- L010 row starts at 38.00, 0.9 s after the "Ian Connor" caption begins (37.09). It is held back by the L009 row, which ends at 37.98. It still shows 3.08 s and the name remains on screen through L011. Optionally shorten the L009 row to end near 37.07 and start L010 at 37.09.

