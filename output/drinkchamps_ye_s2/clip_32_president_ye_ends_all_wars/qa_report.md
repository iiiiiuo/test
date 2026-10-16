# Clip_32 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `26e3c8f321b6adbff1e9d989afb9934aaa704e8a0cdd63228bc1447109c7a11d`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 95.637 s, audio 95.637 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2293 (manifest 2293)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2293, "expected_frames": 2293, "video_duration_s": 95.637208, "audio_duration_s": 95.637, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 263, "asr_words": 266, "matched": 247, "match_ratio": 0.939, "matched_words_inside_their_caption": 0.947, "caption_onset_vs_first_word_s": {"n": 32, "median": -0.127, "max_abs": 1.367}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: PASS - starts at "Let me ask a presidential question." (speech onset 0.88s, prior source speech ended ~598.9s); ends on "God runs the world." (source 696.52s, clip ends 697.07s). Coherent Q&A about ending wars.
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 95.637s / audio 95.637s, 2293 frames = manifest, no decode errors.
3. Transcript accuracy: PASS - sync.txt HEARD lines match displayed English (ASR noise only, e.g. "first a president yay", "I'm in it all wars"). Match ratio 0.939.
4. Translation fidelity: PASS - JP rows match approved CSV and the heard meaning; no wrong-moment attachments.
5. Masking: PASS - no unmasked hits in auto.json; no masked words needed in this clip; Japanese unmasked.
6. Timing/sync: PASS - median onset -0.13s; L6 (17.03-25.83) holds through a ~2s host pause (~19.8-21.6) but starts with first words and is not mismatched; no uncaptioned full sentences; short captions ("How?" 0.56s) are one word and readable enough.
7. Typography/visuals: PASS - sheets show white bold Yu Gothic, outline+shadow, EN above JP, centred, same size/position as reference; max 2 EN + 2 JP lines; no clipping.
8. Framing: PASS - faces in sharp centre band with blurred fill; crop changes align with speaker shot changes.
9. Source usage: PASS - single interval part_5 frames [14419,16712), no padding or repetition.

Non-blocking notes
- L6 caption is on screen 8.8s including a pause mid-sentence; splitting at the pause (~19.8s) would be tighter but is not required.
- L19 JP "でもどうやって？" omits "Don't just say that. Give me..."; the next caption covers it (approved wording).

