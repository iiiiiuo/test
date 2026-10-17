# Clip_35 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `96832f8417390a12b6cf89a4830206ed54ad899bd8632d5f9184983a5246093e`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 64.106 s, audio 64.106 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1537 (manifest 1537)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1537, "expected_frames": 1537, "video_duration_s": 64.105708, "audio_duration_s": 64.106, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 204, "asr_words": 211, "matched": 187, "match_ratio": 0.917, "matched_words_inside_their_caption": 0.963, "caption_onset_vs_first_word_s": {"n": 20, "median": -0.063, "max_abs": 1.14}}

## Critic rounds
- round 1: FAIL — 1.8 s uncaptioned repeated sentence at 41.93-43.75; next caption early → jump cut 638.43-641.52 + display EN 'the whole time' (L009)
- round 2: PASS — non-blocking: abrupt audio drop at join 41.70 → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 64.106 s, audio 64.106 s, frames 1537 = expected, decode_errors empty.
4. Translation (CHANGED_LINES = none): NOT IN SCOPE.
5. Masking: PASS. No curse words in the EN text of subtitles.ass or srt; auto.json unmasked_hits is empty. JP has no asterisks.
7. Typography/visuals: PASS. f_0001.00, f_0009.38 and extra/f_23.png show EN above JP, centred, white bold with black outline and shadow, at the same size and position as the reference, within the frame. The reference shows the same layout.
10. Term-explanation row: PASS.
 - Text verbatim against glossary_draft_s2.json (L001 Tidal, L003 Cedric, L005 Claude Anderson). The Claude Anderson text is split at a natural point after を, so no word or name is split.
 - Timing: Tidal 0.31-5.21 s (4.9 s), Cedric 6.58-15.22 s (8.6 s), Claude Anderson 20.09-25.90 s (5.8 s). Each starts with the caption that shows the term.
 - Position: y 1188 (second line 1236), well below the JP row (last line ends about 1160), inside the sharp band 438..1480, no overlap.
 - Style: Expl uses Yu Gothic bold at 40 pt, white with black outline and shadow, same as Sub. Widths fit within the frame.
1, 3, 6, 8, 9: NOT IN SCOPE (nothing blocking noticed).

Non-blocking notes: none.

