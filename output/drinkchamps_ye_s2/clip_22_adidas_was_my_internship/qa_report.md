# Clip_22 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `0d8b4ae002abed9e4cd91b4ee79c8508e6ecdff9ec182390511b1fd6971d30f3`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 95.554 s, audio 95.554 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2291 (manifest 2291)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2291, "expected_frames": 2291, "video_duration_s": 95.553791, "audio_duration_s": 95.554, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 276, "asr_words": 284, "matched": 266, "match_ratio": 0.964, "matched_words_inside_their_caption": 0.996, "caption_onset_vs_first_word_s": {"n": 34, "median": 0.0, "max_abs": 0.855}}

## Critic rounds
- round 1: PASS — none (note: JP names 3 s early at 73.81-77.03) → chunks override Clip_22_L019
- round 2: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: PASS. Starts at "I want to start because, you know," (source false start at 154.3-155.35 excluded; start audio RMS dip, not mid-word). Ends on "those infrastructures, right?" at 250.96; audio decays to a low before the next "yeah". Standalone and coherent.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 95.554 s / audio 95.554 s, 2291 frames = expected, no decode errors.
3. Transcript: PASS. sync.txt HEARD lines match displayed EN (match ratio 0.964); only ASR errors ("easy", "Duce", "once" vs "one time").
4. Translation: PASS. No clear errors against heard meaning; names follow approved rules.
5. Masking: PASS. unmasked_hits empty; no masked-word candidates in text; JP not mechanically masked.
6. Timing/sync: PASS. Median onset 0.0 s, 99.6% of matched words inside their caption; no flash captions (shortest ~1.0 s); no uncaptioned foreground sentence.
7. Typography: PASS. Yu Gothic bold, white with black outline/shadow, EN above JP, centred, 2 EN + 2 JP lines max, position in lower sharp band like reference, no clipping (f_0067.60, f_0095.47).
8. Framing: PASS. Faces centred in sharp band with blurred fill; changes occur at shot changes (Nore/Ye/Sway cuts).
9. Source usage: PASS. Single interval part_1 frames [3726,6017), 2291 frames; no padding/freeze/repetition.

Non-blocking notes
- Last 3.4 s shows Sway as a cutaway while the line is his interjection; reads naturally.

