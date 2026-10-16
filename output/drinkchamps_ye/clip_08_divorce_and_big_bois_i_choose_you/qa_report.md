# Clip_08 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `8a184afc1ec4cea197bb40e7a2132776a247a3bd5faaaa2c4c8f3317c2ee44b4`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 80.706 s, audio 80.705 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1935 (manifest 1935)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1935, "expected_frames": 1935, "video_duration_s": 80.705625, "audio_duration_s": 80.705, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 252, "asr_words": 247, "matched": 223, "match_ratio": 0.885, "matched_words_inside_their_caption": 0.964, "caption_onset_vs_first_word_s": {"n": 24, "median": 0.062, "max_abs": 0.938}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: PASS - starts on "Anybody that's ever been through a divorce" (source ctx 1752.33, prior speech ends 1751.63); ends on "get back together" (ASR 80.5-80.70) as a resolved thought.
2. Duration/format: PASS - auto.json 1080x1920, SAR 1:1, video 80.705625 s, audio 80.705 s, 1935/1935 frames, no decode errors.
3. Transcript: PASS - sync.txt HEARD matches displayed English; only ASR slips ("don the two", "outcast", "boy").
4. Translation: PASS - no clear errors; JP matches each EN line and moment (e.g. L15 "I Choose You", L19 "Ms. Jackson").
5. Masking: PASS - "s**t" at 24.06; auto.json unmasked_hits empty; JP not masked.
6. Timing/sync: PASS - median onset offset 0.06 s; 96% matched words inside their caption; gaps 38.76-39.84 and 74.69-75.87 are hesitation/pause ("um", silence), no uncaptioned sentences; min caption 0.74-0.75 s (L20 "Yeah, yeah, yeah." 55.27-56.01) readable.
7. Typography: PASS - f_0022.01 / f_0079.71 show white bold Yu Gothic, black outline/shadow, EN over JP, centred at y~950-1140, similar to ref; up to 2 EN + 2 JP lines, no overflow.
8. Framing: PASS - Ye and N.O.R.E. faces/caps fully in sharp band (f_0022.01, f_0079.71), blurred fill above/below; changes only at shot changes.
9. Source usage: PASS - single interval part_2_2 frames [42012,43947) half-open, continuous, no padding/freezes/repetition.

Non-blocking notes
- Final caption ends at 80.69 s, 0.015 s before video end; last word "together" ends ~80.70, so the cut is tight.
- At 79.71 the cap top touches the sharp band top edge (not cropped).

