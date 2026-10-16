# Clip_21 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `946317144c9af0332adf036fc60d9f19651be405cb88d646c2af287741bf5a6f`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 68.318 s, audio 68.318 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1638 (manifest 1638)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1638, "expected_frames": 1638, "video_duration_s": 68.31825, "audio_duration_s": 68.318, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 230, "asr_words": 225, "matched": 204, "match_ratio": 0.887, "matched_words_inside_their_caption": 0.946, "caption_onset_vs_first_word_s": {"n": 21, "median": -0.238, "max_abs": 0.568}}

## Critic rounds
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: PASS. Opens on "Okay, so I'm giving you an analogy" (first word 0.45s, source speech from 1191.46s). The first 0.4s is room crosstalk fading from the previous exchange, not Ye mid-word (source RMS 0.16 -> 0.04 by 1191.4). Middle is one continuous argument (album analogy -> Workout Plan -> Stronger diamond). Ends on "You know what I'm saying?", which resolves; next source line "so we're at the beginning of a new frontier" is excluded. Render audio decays to 0.04 at 68.30s (no hard clip).
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 68.318s / audio 68.318s, 1638 frames = manifest 1638, decode_errors empty.
3. Transcript: PASS. sync.txt HEARD matches displayed EN across all 25 captions. Differences are ASR noise (Mos Def, Irina Shayk, "shit") plus the speaker's repeated "you know what I'm saying". Source says "Our life is an album" and the caption says "the album" (immaterial).
4. Translation: PASS. All JP lines match the approved rev3 rows and sit at the right moments. No dropped lines.
5. Masking: PASS. "s**t" at 38.96s (cap 15). auto.json unmasked_hits empty. JP has no asterisks.
6. Timing/sync: PASS. 21 caption onsets: median -0.24s vs the first heard word, max |0.57s|. 94.6% of matched words fall inside their caption. No caption is shorter than 0.85s (cap 17, 0.85s, a short 2-line caption but readable). No uncaptioned foreground sentence.
7. Typography/visuals: PASS. Sheet frames show white bold Yu Gothic with black outline, EN above JP, centred, same lower-centre position and size as ref_sheet. All captions are at most 2 EN + 2 JP lines. No clipping, and the text is readable over the white shirt and gold backdrop.
8. Framing: PASS. Ye is centred in the sharp band with the whole head and cap visible, with blurred fill above and below as in the reference. One continuous shot, with no framing change.
9. Source usage: PASS. One interval, part_6 frames [28555, 30193), 1638 frames, audio same range. No freeze, padding or repetition (the doubled "You know what I'm saying?" is in the source audio).

Non-blocking notes
- Caption 7 -> 8 splits "J." / "Cole" across two captions (17.24-18.59 / 18.61), and JP caption 1 ends on a dangling "アルバムの". Both are cosmetic and follow the approved wording.
- Caption 25 shows "You know what I'm saying?" twice on two EN lines, matching the doubled phrase in the audio.

