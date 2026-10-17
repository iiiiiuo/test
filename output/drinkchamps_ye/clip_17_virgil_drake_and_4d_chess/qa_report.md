# Clip_17 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `4d18a3bd88eb15ed8bb84b0ec48db0b2966ec2f00179dbfc854501a8ca55936e`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 72.823 s, audio 72.823 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1746 (manifest 1746)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1746, "expected_frames": 1746, "video_duration_s": 72.82275, "audio_duration_s": 72.823, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 251, "asr_words": 253, "matched": 242, "match_ratio": 0.964, "matched_words_inside_their_caption": 0.988, "caption_onset_vs_first_word_s": {"n": 29, "median": 0.075, "max_abs": 0.435}}

## Critic rounds
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 72.823 s / audio 72.823 s, frames 1746 = manifest, decode_errors empty.
3. Transcript: NOT IN SCOPE
4. Translation: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS. Displayed English across all 34 SRT cues has no unmasked listed words (auto.json unmasked_hits empty); no asterisks in the Japanese.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS. f_0006.97 and f_0043.13 vs ref_sheet: white bold Yu Gothic, black outline+shadow, EN above JP, centred, same position as reference, max 2 EN + 2 JP lines, no clipping, readable.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS.
 - Text verbatim vs glossary (L002 Virgil, L004 White Lives Matter, L008 Patek, L011 4次元チェス); breaks fall after "Louis Vuittonの" and "Yeが", no word split.
 - Timing: 4.78-12.91 s (8.1 s), 12.93-20.17 s (7.2 s), 40.66-45.82 s (5.2 s), 54.21-58.20 s (4.0 s), starting with the caption that shows each term; all well over 2 s.
 - Position: lines at y 1188/1236, style Expl, 40 px, inside the sharp band (438..1480). The EN/JP block ends near y 1145, so no overlap (f_0006.97, f_0043.13).
 - Style: same Yu Gothic bold, white fill, black outline and shadow as Sub.

Non-blocking notes: none.

