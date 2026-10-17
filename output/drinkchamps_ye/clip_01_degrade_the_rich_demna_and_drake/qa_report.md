# Clip_01 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `612b4ff8601b035801d0fbfeb5dc53c49d77913d967f05229d5e1a58e8d2f99a`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 64.106 s, audio 64.106 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1537 (manifest 1537)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1537, "expected_frames": 1537, "video_duration_s": 64.105708, "audio_duration_s": 64.106, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 162, "asr_words": 166, "matched": 149, "match_ratio": 0.92, "matched_words_inside_their_caption": 0.973, "caption_onset_vs_first_word_s": {"n": 18, "median": 0.103, "max_abs": 1.343}}

## Critic rounds
- round 1: FAIL — clip ended ~0.1 s before last word "ever" while caption showed it → systematic boundary audit of all 42 boundaries (scripts/boundary_check.py) -> 15 clips moved to quietest point between last included and first excluded word (scripts/refine_bounds.py, work/b/boundary_changes.json); Clip_01 host aside (LOW, untranslated) removed by jump cut
- round 2: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 64.106 s / audio 64.106 s (60<=d<120), 1537 frames = expected, decode_errors empty.
3. Transcript: NOT IN SCOPE
4. Translation (CHANGED_LINES none): NOT IN SCOPE (nothing changed)
5. Masking: PASS - only masked hit "motherf**kers" (srt/ass, frame 4-8 s); auto.json unmasked_hits empty; grep finds no unmasked profanity; JP not mechanically masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - frames f_0022.94, extra/f_38.62, extra/f_49.5: white bold Yu Gothic, black outline+shadow, EN above JP, centred, same position as reference; max 2 EN + 2 JP lines; no clipping; readable on bright shirt/gold background.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
 - L003 (15.36-23.08, 7.7 s), L008 Ray Kurzweil (36.71-43.53, 6.8 s), L009 Demna (47.65-53.07, 5.4 s): text matches glossary_draft_s1.json verbatim (line breaks only differ).
 - Each starts with the caption that shows the term/line; all >2 s.
 - Rows at y=1188 (and 1236 for second line), fs40, Expl style Yu Gothic bold white, outline 3, shadow 2; inside band 438..1480. EN/JP block ends ~y1150 at most (4-line case), so ~40 px clear gap, no overlap (seen at 38.62 and 49.5 s).
 - Line breaks fall at natural points (after に / ディレクター preceded by の); no word or name split.

Non-blocking notes
- Expl row sits over the microphone/shirt at 22.94 s; still readable thanks to outline.

