# Clip_16 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `75d808253713a846834903e032bb0c6c4dfb44886bf37fb8f1e4f6c0a4848f63`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 64.564 s, audio 64.564 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1548 (manifest 1548)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1548, "expected_frames": 1548, "video_duration_s": 64.5645, "audio_duration_s": 64.564, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 207, "asr_words": 198, "matched": 184, "match_ratio": 0.889, "matched_words_inside_their_caption": 0.984, "caption_onset_vs_first_word_s": {"n": 18, "median": 0.06, "max_abs": 1.64}}

## Critic rounds
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Scope: items 2, 5, 7, 10 (item 4: no CHANGED_LINES). Items 1, 3, 6, 8, 9 NOT IN SCOPE; no blocking problem noticed.

1. NOT IN SCOPE
2. PASS - auto.json: 1080x1920, SAR 1:1, video 64.5645 s, audio 64.564 s, frames 1548 = expected 1548, no decode errors.
3. NOT IN SCOPE
4. NOT IN SCOPE (no changed lines)
5. PASS - auto.json unmasked_hits empty; displayed EN shows "s**t" (29.03) and "ni**a's" (58.04); no unmasked profanity in ASS/SRT; no asterisks in Japanese text.
6. NOT IN SCOPE
7. PASS - f_0017.63.png: white bold Yu Gothic with black outline/shadow, EN above JP, centred, 4 lines max (2 EN + 2 JP), inside frame, same vertical zone as ref_20.png, readable on bright background.
8. NOT IN SCOPE
9. NOT IN SCOPE
10. PASS - single Expl event 15.91-21.59 (5.68 s): "Waldorf：ビバリーヒルズの高級ホテルWaldorf Astoria" matches glossary_draft_s1.json Clip_16_L006 verbatim. It starts with the L006 caption (15.91) and stays while it is spoken. At y=1188 (about 1170-1225 in f_0017.63.png) it is below the last JP line (ends about 1145) with no overlap and inside the sharp band (438..1480). Same font, white fill, black outline and shadow, smaller size (40). Single line, x 148..932, no split word.

Non-blocking notes
- The Expl row is a single line of about 785 px; fine at this width.

