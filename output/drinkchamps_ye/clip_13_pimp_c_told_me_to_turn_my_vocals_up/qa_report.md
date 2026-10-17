# Clip_13 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `33b0f8dea93a118df4d27e8a01b25d4bda1228ed3ccf4cd48cfc27dfe0c4665f`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 78.996 s, audio 78.995 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1894 (manifest 1894)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1894, "expected_frames": 1894, "video_duration_s": 78.995583, "audio_duration_s": 78.995, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 261, "asr_words": 288, "matched": 249, "match_ratio": 0.954, "matched_words_inside_their_caption": 0.98, "caption_onset_vs_first_word_s": {"n": 28, "median": 0.077, "max_abs": 0.727}}

## Critic rounds
- round latest: FAIL — end cut before final "right?" → end moved to 1474.48 (frame 35352)

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 78.9956 s, audio 78.995 s (60 <= d < 120), 1894 frames = expected 1894, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits = []; grep of subtitles.ass finds no curse words in EN or Expl text; JP rows carry no asterisks.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - frames f_0005.69, f_0012.36, f_0063.23, f_0078.00, extra/f_44.0, f_54.0, f_68.0: white bold Yu Gothic, black outline+shadow, EN above JP, centred, max 2 EN + 2 JP lines, same vertical position as the reference (about y 975-1130), no clipping, readable on the bright white shirt and gold backdrop.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
 - Text verbatim vs glossary_draft_s1.json for all 7 Clip_13 keys (L001, L002, L007, L009, L012, L013, L014); only line breaks differ (allowed).
 - Spans (ASS Expl) and render frames inside each span:
   Pimp C 3.48-7.89 (f_0005.69 OK); pink polo 7.91-14.63 (f_0012.36 OK); The Strokes 40.05-48.29 (extra/f_44.0.png OK); All Falls Down 52.64-57.54 (extra/f_54.0.png OK); Tucker Carlson 61.03-65.43 (f_0063.23 OK); Drink Champs 65.45-72.26 (extra/f_68.0.png OK); SNL 75.44-79.00 (f_0078.00 OK).
 - Each starts with the caption whose JP row first shows the term (Pimp Cみたいな, ピンクのポロシャツの, The Strokesの, 『All Falls Down』で, Tucker Carlsonも, 『Drink Champs』, KimがSNLに出た時の) and lasts 3.6-8.2 s (>= 2 s).
 - Layout: Expl rows at y=1188/1236 (fs40, an8), below the last JP row (y=1098, fs50) with a visible gap in every checked frame, so no overlap; bottom of row 2 is about y 1290, inside the sharp band 438..1480; widest line (pink polo, about 680 px wide) is inside the 1080 frame.
 - Style: same Yu Gothic bold, white fill, black outline and shadow as Sub (same outline 3 / shadow 2); no word or name split by breaks (Pimp C / UGKの|メンバー, N.O.R.E.と|DJ EFN, アメリカの|コメディ番組 are all clean).
 - Last Expl end 79.00 vs video 78.9956 (0.004 s over, invisible).

Non-blocking notes
- Pink polo Expl (from 7.91) and The Strokes Expl (from 40.05) start with the first caption that already shows the term in JP, so they appear 2-4 s before the English words are spoken. This matches the stated rule and is acceptable.

