# Clip_36 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `2f66d056c51411ddd5302c65b1bf797d2564b159f7c23b31ec91d417b47d9bc5`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 78.996 s, audio 78.995 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1894 (manifest 1894)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1894, "expected_frames": 1894, "video_duration_s": 78.995583, "audio_duration_s": 78.995, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 221, "asr_words": 229, "matched": 196, "match_ratio": 0.887, "matched_words_inside_their_caption": 0.974, "caption_onset_vs_first_word_s": {"n": 23, "median": 0.013, "max_abs": 1.157}}

## Critic rounds
- round 1: PASS — non-blocking: caption 10 ~1.2 s early over applause → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 5, 7, 10; item 4 CHANGED_LINES = none)
1. Structure: NOT IN SCOPE
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 78.996 s / audio 78.995 s (60 <= d < 120), 1894 frames = expected 1894, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (no changed lines)
5. Masking: PASS. Only profanity is "f**k" (L016, 67.8 s); auto.json unmasked_hits = []; JP "何とも思ってない" not mechanically masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS. f_25.png, f_73.5.png, sheet_2.jpg: white bold Yu Gothic, black outline + shadow, EN above JP centred (EN y~948-1000, JP below), up to 2 EN + 2 JP lines, inside the sharp band, same look as ref_sheet.jpg.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS.
 - Text verbatim vs glossary_draft_s2.json (L005 Stephen A. Smith, L006 Oprah, L016 Good Morning America, L017 Tucker Carlson): all four match; line breaks only after "アメリカを" and after "。" (no word/name split).
 - Style Expl: Yu Gothic, 40 px, white fill, black outline + shadow (same as Sub). Position y=1188 (+48 second line), ends about y 1280, inside the 438..1480 band. In f_73.5 (4-line caption block ends about y 1145) there is no overlap with EN/JP rows.
 - Durations: Stephen 18.48-22.46 (3.98 s), Oprah 22.48-27.08 (4.60 s), GMA 67.85-71.83 (3.98 s), Tucker 71.85-77.78 (5.93 s). All >= 2 s; none overlap each other.
 - Frames confirmed: Oprah at 25 s, GMA at 68.87/70.74 s, Tucker at 73.5 s.

Non-blocking notes
- Oprah expl starts 22.48 s, about 1.2 s after its caption (21.27 s), and Tucker expl starts 71.85 s, about 1.9 s after its caption (69.92 s). Each waits for the previous term's row to end so rows do not stack. Still readable and the term is spoken in that window. Could be tightened by ending the Stephen / GMA rows sooner (about 3 s).

