# Clip_21 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `f2ff586941d6423886aad0ecac430d70820da6b74cf51940b58f6900ca48154c`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 68.318 s, audio 68.318 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1638 (manifest 1638)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1638, "expected_frames": 1638, "video_duration_s": 68.31825, "audio_duration_s": 68.318, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 230, "asr_words": 225, "matched": 204, "match_ratio": 0.887, "matched_words_inside_their_caption": 0.946, "caption_onset_vs_first_word_s": {"n": 22, "median": -0.238, "max_abs": 0.608}}

## Critic rounds
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json 1080x1920, SAR 1:1, video 68.318 s, audio 68.318 s, frames 1638 = manifest 1638, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits empty; only profanity "s**t" (L006 at 38.96-41.31) is masked; JP rows and Expl rows not masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - sheet_1.jpg and extra/e_35/e_43/e_51.png show white bold Yu Gothic, black outline+shadow, centred, EN above JP, max 2 EN + 2 JP lines, same size and position as reference, no clipping, readable on bright background.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
 - Text matches glossary_draft_s1.json for L002, L003, L004, L006, L007, L008, L009 verbatim (only line breaks differ; L008's two terms are on separate lines).
 - Timing: L002 8.80-16.04 (starts with "Quincy Jones" caption, 7.2 s); L003 17.24-21.94 (4.7 s); L004 21.96-28.03 (6.1 s); L006 31.45-41.31 (9.9 s); L007 41.33-48.22 (6.9 s); L008 49.85-57.87 (8.0 s); L009 59.04-end (9.3 s). Each starts with the caption that carries the term, all over 2 s.
 - Layout: Expl at y=1188..1284 (L007 shifted up to 1138/1186 because JP is 1 line); checked frames at 35, 43, 51 and 60.89 s show a clear gap below the JP row, no overlap. Lowest line (L008 third line, y~1284+40) is well inside the sharp band (438..1480).
 - Style: same Yu Gothic Bold, white fill, black outline and shadow, size 40. No word or name is split by the line breaks (Quincy Jones, Irina Shayk, Mos Def・Common, 『The New Workout Plan』 all intact).

Non-blocking notes
- Expl row is noticeably thinner/smaller than EN/JP; still legible on all checked frames.

