# Clip_23 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `57889998498f9668b10fcd5eb059fd9dfc0f968eb20a93a4fd5d9ab5c428b46a`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 86.253 s, audio 86.253 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2068 (manifest 2068)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2068, "expected_frames": 2068, "video_duration_s": 86.252833, "audio_duration_s": 86.253, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 243, "asr_words": 262, "matched": 227, "match_ratio": 0.934, "matched_words_inside_their_caption": 0.956, "caption_onset_vs_first_word_s": {"n": 28, "median": -0.071, "max_abs": 1.003}}

## Critic rounds
- round 1: FAIL — final word 'about' cut ~0.25 s early; 'fit in' clipped at join → hand end windows 1143.08-1143.14 and 1197.24-1197.30 (frames 27408, 28706)
- round 2: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Scope: items 2, 5, 7, 10 (item 4 CHANGED_LINES = none, not judged). Items 1, 3, 6, 8, 9 NOT IN SCOPE; no blocking problem noticed.

1. NOT IN SCOPE
2. PASS - auto.json: 1080x1920, SAR 1:1, video 86.253 s, audio 86.253 s (60 <= d < 120), 2068 frames = expected 2068, decode_errors empty.
3. NOT IN SCOPE
4. NOT IN SCOPE (CHANGED_LINES none)
5. PASS - EN shows f**k (0:00.32) and ni**as (0:58.42); srt/ass grep finds 0 unmasked fuck/shit/bitch/nigg/pussy; auto.json unmasked_hits empty; Japanese has no asterisks.
6. NOT IN SCOPE
7. PASS - frames f_0001.00, f_0040.87, f_0042.50, f_0080.96 and extra/f_8.0, extra/f_33.0: white bold Yu Gothic, black outline+shadow, EN above JP, centred at the reference position (about y 950-1150), max 2 EN + 2 JP lines, no clipping, blurred fill above/below like ref_20.
8. NOT IN SCOPE
9. NOT IN SCOPE
10. PASS
- Text verbatim vs glossary_draft_s2.json for Clip_23_L002, L007, L010, L018 (line breaks only differ).
- Timing: L002 5.98-16.73 (10.7 s, starts with the Cassius/Ali caption); L007 29.72-36.83 (7.1 s, starts with the Drake caption); L010 41.63-45.36 (3.7 s, starts with the dyslexic caption); L018 74.32-83.66 (9.3 s, starts with the Fortune 500 caption).
- Position: rows at y 1188/1236/1284 (fs40), below the last JP row (max about y 1150) with a gap, no overlap, inside the sharp band (438..1480). Frames confirm.
- Style: same font, white fill, black outline and shadow; width at most about 740 px.
- Line breaks do not split words or names (Kanye West, Larry Hoover's, Muhammad Ali kept whole).

Non-blocking notes
- The explanation row is only about 3.7 s for dyslexia, which is readable but short.

