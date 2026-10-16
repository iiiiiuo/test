# Clip_20 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `76287ebc6e3653827868a4420114a225c3bad07b377d204b5360a2e8fe98d19d`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 74.575 s, audio 74.574 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1788 (manifest 1788)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1788, "expected_frames": 1788, "video_duration_s": 74.5745, "audio_duration_s": 74.574, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 217, "asr_words": 214, "matched": 187, "match_ratio": 0.862, "matched_words_inside_their_caption": 0.92, "caption_onset_vs_first_word_s": {"n": 24, "median": 0.085, "max_abs": 5.605}}

## Critic rounds
- round latest: FAIL — D'Usse/Hennessy JP swapped across chunks → L004/L011 chunk overrides

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

## Items
1. Structure: PASS. Opens on "Like, you at somebody's wedding" (source_context: "it adds to it like you at...", no mid-word start). Runs through the D'Usse / Hennessy argument and the "Go full Ye" chant, then ends on "A nightcap is well recommended, my friend." with laughter. Standalone-readable.
2. Duration/format: PASS. auto.json has 1080x1920, SAR 1:1, video 74.5745 s, audio 74.574 s, 1788 of 1788 frames, no decode errors.
3. Transcript: PASS. 24 of 27 captions match the HEARD lines. The only differences are ASR errors ("Ducé" for D'Usse, "yay" for Ye, "douce"). A spot ASR of 29-38 s heard "I'm asking and call it that every..." then "I'm asking every black person", which matches the captions.
4. Translation: PASS. Each JP line conveys its EN line, with the right rows and the right moments. Dropped_lines is empty. JP uses English-spelled D'Usse/Ye and ヘネシー / ブラックライブスマター per the naming rules.
5. Masking: PASS. EN shows s**t (x2) and f**k. auto.json has unmasked_hits=[]. JP is not mechanically masked.
6. Timing/sync: PASS. Median caption onset vs first heard word is 0.085 s (the 5.6 s max_abs is a single misalignment in the automatic sync check, not a real lag). There is an uncaptioned gap at 31.8-34.4 s. A spot ASR shows only crowd or background "We're with that!" there, with Ye silent and the next caption starting on "I'm asking" at 34.45. The shortest caption is about 1.06 s ("They say some real s**t."), still readable.
7. Typography: PASS. Frames f_0042.27 and the sheets show white bold Yu Gothic, black outline and shadow, EN above JP, centred. The first line sits at y≈957 and EN is 54 / JP 50, as in the style spec and ref_20.png (first line top ≈957). No more than 2 EN + 2 JP lines. Nothing is clipped, and it is readable on the bright yellow background.
8. Framing: PASS. The sharp 1080x1042 band plus blurred fill matches the reference. Faces are in the band in all 12 frames and sheets (Ye, the host, the interviewer). Crop changes fall on shot changes (5 pieces).
9. Source usage: PASS. part_6, single interval [5165,6953) with PTS mapping given, frame count 1788 equals the manifest. No padding or repetition. The repeated "Go full Ye" lines are the speaker's own chant, not duplicated footage.

## Non-blocking notes
- Caption 11 JP breaks mid-katakana ("ブラックライブスマ / ター"), which is slightly awkward. It is approved wording, only the wrap point.
- The first 0.3 s of audio carries low-level speech tail (RMS ≈0.07-0.1 before the jump at ≈0.4 s). It is not noticeably abrupt.
- At about 7 s the cap brim touches the top edge of the sharp band. It is minor.

