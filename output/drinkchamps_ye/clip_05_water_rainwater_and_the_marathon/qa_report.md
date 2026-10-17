# Clip_05 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `d61c42ef4429a0b0427e640f422444eeb1b3739435653eeb728d3355c4c5233d`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 65.566 s, audio 65.565 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1572 (manifest 1572)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1572, "expected_frames": 1572, "video_duration_s": 65.5655, "audio_duration_s": 65.565, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 165, "asr_words": 167, "matched": 160, "match_ratio": 0.97, "matched_words_inside_their_caption": 0.938, "caption_onset_vs_first_word_s": {"n": 18, "median": -0.15, "max_abs": 2.39}}

## Critic rounds
- round 1: FAIL — caption 9 2.5 s early over pause → build_subs: glued short-word onset fix + forced chunk break at >1 s pauses (snapped to punctuation)
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json 1080x1920, SAR 1:1, video 65.5655 s / audio 65.565 s, 1572 = 1572 frames, no decode errors.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - only "f**k" (18.49 s) is masked; auto.json unmasked_hits = []; JP rows have no asterisks.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - f_0001.64 and f_0023.42 show white bold Yu Gothic with black outline/shadow, EN above JP, centred, same position as ref_20; max 2 EN + 2 JP lines; no clipping.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
 - L001 row (0.08-6.48 s, 6.4 s): text matches the glossary verbatim ("雨水の収集：実際にはアメリカの大半の州で合法。／一部の州に制限がある" wrapped at the sentence break). Frame f_0001.64 (inside the span) shows it at y~1190-1260, below the JP row (ends ~1140), inside the sharp band.
 - L006 row (18.49-27.55 s, 9.06 s): Tシャツ / "White Lives Matter"Tシャツ / ビーフ lines match the glossary, with each term on its own line. Frame f_0023.42 (inside the span) shows it at y~1190-1320, no overlap with EN/JP, inside the band (y<1480). "beef" is spoken in the caption starting at 21.16 s, and the row is already on screen.
 - Same font, white fill, black outline and shadow (style Expl, 40 px). No word or name is split across lines.
 - Both glossary keys for Clip_05 (L001, L006) are covered; no extra rows.

Non-blocking notes: none

