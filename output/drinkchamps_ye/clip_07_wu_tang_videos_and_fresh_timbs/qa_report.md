# Clip_07 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `bbd56a60eddd471dc48e5db5c04b636ae68d77e63f76ceeef12798a4d3a6caae`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 63.188 s, audio 63.188 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1515 (manifest 1515)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1515, "expected_frames": 1515, "video_duration_s": 63.188125, "audio_duration_s": 63.188, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 197, "asr_words": 201, "matched": 170, "match_ratio": 0.863, "matched_words_inside_their_caption": 0.994, "caption_onset_vs_first_word_s": {"n": 22, "median": 0.124, "max_abs": 0.454}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Scope: items 2, 5, 7, 10 (item 4: CHANGED_LINES = none). Items 1, 3, 6, 8, 9: NOT IN SCOPE (no blocking problem noticed).

2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 63.188 s, audio 63.188 s (60 <= d < 120), 1515 frames = expected 1515, decode_errors empty.
5. Masking: PASS. auto.json unmasked_hits = []; grep of ASS/SRT finds no unmasked profanity; only hit is "ni**as" at 38.49-41.21 (heard "niggas"); JP "NYの奴らが..." not mechanically masked.
7. Typography/visuals: PASS. Frames f_0004.46, f_0025.59, extra e_14.0 and e_22.0 versus reference: white bold Yu Gothic, black outline and shadow, EN above JP, centred, max 2 EN + 2 JP lines (ASS check: no more), nothing clipped, legible on the white shirt.
10. Term-explanation row: PASS. Three rows, each judged from a render frame inside its span:
 - L001 (0.06-10.03, 9.97 s): frames f_0004.46 (also 0.63, 1.00): text matches the draft verbatim; separate terms start on their own lines; no break inside a word.
 - L005 (10.96-17.68, 6.7 s): extracted extra/e_14.0.png: "Tony Starks：Wu-Tang Clanの / Ghostface Killahの別名" matches the draft; starts with the "Tony Starks" caption (10.96).
 - L008 (19.46-28.81, 9.35 s): f_0025.59 and extra/e_22.0.png: "Don C：... / Wallabees：Clarksの靴。Wu-Tangの / メンバーの愛用で有名" matches the draft. It starts with the Don C caption and stays through the Wallabees caption (22.38-28.81).
 All rows: style Expl 40 px, Yu Gothic bold, white, black outline and shadow. They sit at y 1188-1332 in the ASS. In frames the rows span about y 1190-1370, inside the sharp band 438..1480. The EN/JP block ends at about y 1145 (4 lines at 22.0), so there is no overlap.

Non-blocking notes: the L001 explanation stays up 10 s, across the next caption (fine). The 4-line L008 EN/JP block sits about 45 px above the explanation row; it reads clearly but is tight.

