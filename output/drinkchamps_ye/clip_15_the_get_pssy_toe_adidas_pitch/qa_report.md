# Clip_15 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `7f53fe2205ca1c0ea086f72815e8a67089fa31c3813b018874f9b41f420cde10`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 76.827 s, audio 76.827 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1842 (manifest 1842)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1842, "expected_frames": 1842, "video_duration_s": 76.82675, "audio_duration_s": 76.827, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 222, "asr_words": 229, "matched": 207, "match_ratio": 0.932, "matched_words_inside_their_caption": 0.986, "caption_onset_vs_first_word_s": {"n": 28, "median": 0.1, "max_abs": 0.63}}

## Critic rounds
- round latest: FAIL — two uncaptioned host sentences; duplicate JP on "Yeah." → jump cuts 1171.355-1173.385 and 1184.17-1187.235; L005 chunk override

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: PASS. Opens at "So I went to Adidas meeting" (HEARD matches, no clipped word). Ends on "...no one's getting p**sy in Adidas, bro." (source 1224.90, answers the "who came up with that" question). Cuts at 1171.34 (after "Yeah."), 1173.38 and 1184.18 (after "Or still on") fall in pauses. Removed lines ("You guys are not getting p...", "Still on / No, they might not take them off") do not break the sense.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 76.827 s, audio 76.827 s, 1842 frames = expected, decode_errors empty.
3. Transcript: PASS. HEARD matches the displayed English. Differences are ASR noise or acceptable (pulled/put out, "350s" vs three stitches, "Stout" vs "Stoute"). Match ratio 0.93, 98.6% of matched words fall inside their caption.
4. Translation: PASS. No clear errors. JP lines 9/10 ("それがマーケティングの / プレゼンだったわけ？") are split across two captions in the right order. "ヤってる場面" and "モテる" are approved wording.
5. Masking: PASS. auto.json unmasked_hits is empty. Every p**sy and get-p**sy toe is masked in the English. The Japanese is not mechanically masked.
6. Timing/sync: PASS. Onset median offset 0.10 s, max 0.63 s. No caption under 0.48 s except the one-word "Yeah." (24.43-24.91), which is a single word and acceptable. The uncaptioned stretch 39.2-41.8 s is Ye laughing (frames 40.5/41.5), a reaction. The 19.8-24.4 s gap is a pause before "Yeah". No uncaptioned foreground full sentence.
7. Typography/visuals: PASS. White bold Yu Gothic with black outline/shadow, EN above JP, centred, same vertical position and size as the reference sheet. Max 2 EN + 2 JP lines, no overflow. Readable over the white shirt (f_0000.05, f_0050.07).
8. Framing: PASS. Faces sit in the sharp centre band with blurred fill above and below, as in the reference. Crop changes coincide with speaker/shot changes. The face is slightly off-centre at about 40.5 s (laughing, head turned), not cut off.
9. Source usage: PASS. Three half-open intervals from part_4 (27407-28084, 28133-28392, 28465-29371), disjoint, with audio the same as video. No padding, freeze or repetition. The joins read naturally.

Non-blocking notes
- Caption 7 "nobody's getting p**sy in Adidas." starts at 15.40 s after a 0.6 s gap following "look,". This matches the speech pause.
- The JP for "Let's get p**sy, guys" uses 「」 quotes, consistent with the surrounding quoted pitch.

