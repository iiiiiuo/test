# Clip_25 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `a61b701dba128792a37cc2b46543365f02187df904e24f9fcfad62314e5da07b`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 76.076 s, audio 76.076 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1824 (manifest 1824)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1824, "expected_frames": 1824, "video_duration_s": 76.076, "audio_duration_s": 76.076, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 227, "asr_words": 217, "matched": 206, "match_ratio": 0.907, "matched_words_inside_their_caption": 0.956, "caption_onset_vs_first_word_s": {"n": 27, "median": 0.059, "max_abs": 1.739}}

## Critic rounds
- round 1: PASS — note: opening trims ~0.2 s of 'And I' → interval 1 start moved to 1108.40-1108.46 window
- round 2: PASS — non-blocking: low-level tail of 'and' in first 0.35 s → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (non-blocking: clip opens on the clipped tail of "and" before "I want to change", about 0.35 s of low-level audio)
Fix: none

## Items
1. Structure: PASS. Opens "I want to change something I said", closes on "that squirrel can jet-ski!", and stands alone. The join at 56.64 s cuts Ye's "Took out leaders, took out structure" to "Nothing f**ks with a Drink Champs interview", which reads as a natural jump (source_context.txt: the skipped span is only small talk).
2. Duration/format: PASS. auto.json shows 1080x1920, SAR 1:1, video and audio 76.076 s, 1824 of 1824 frames, no decode errors, and a/v start both 0.
3. Transcript accuracy: PASS. Render ASR is weaker than large-v3 in three places; I re-ran large-v3 on the source spans and it supports the captions.
   - 34.8-39.5 s: large-v3 gives "you're removing the leaders and that was something and that fucked up the world". The render ASR's "that's what happened in Chicago" is wrong.
   - 59.4-60.2 s "No, no, no.": large-v3 on the tight window 1174.3-1175.3 s hears "No, no, no" (word probabilities 0.99-1.0).
   - 60.2-64.6 s "it's not the same": the approved CSV carries this as an uncertainty (turbo "so same", large-v3 "the same"). Low risk.
4. Translation fidelity: PASS. Japanese matches the approved rows and the moment each line appears. The "その" / "一人の" emphasis on the leader/a leader contrast is carried. No dropped lines (dropped_lines is empty).
5. Masking: PASS. auto.json reports unmasked_hits as empty. EN shows f**ked at 35.96 s and f**ks at 56.64 s. Japanese is not mechanically masked.
6. Timing/sync: PASS. Median caption onset vs first word is 0.06 s over 27 captions, and 95.6% of matched words fall inside their caption. The shortest caption is 0.76 s ("No, no, no." at 59.40-60.16 s), a 3-word interjection, so readable. No long uncaptioned speech.
   - Caption 15 ("and that f**ked up the world", from 35.96 s) leads the spoken "that fucked" (about 36.5-36.7 s) by roughly 0.5 s. Not blocking.
   - The 1.7 s "max_abs" in auto.json is ASR noise around 34.8-37 s, not a real lag.
7. Typography/visuals: PASS. Frames f_0016.89 and f_0035.41 and sheets 1-2 show white bold Yu Gothic with black outline and shadow, EN above JP, centred, at the same vertical band as the reference. Maximum is 2 EN + 2 JP lines. No clipping and readable on the bright gold background.
8. Framing: PASS. The sharp centre band (1080x1042 at y 438) with blurred fill above and below matches the reference. Faces are centred with headroom in every frame checked, for Ye, the host and the N.O.R.E./other shots. Crop changes fall at shot changes (manifest pieces).
9. Source usage: PASS. Two half-open intervals from part_3, [26569,27927) and [28091,28557), with no overlap. There is no padding, freeze or repetition. The join distorts nothing.

## Non-blocking notes
- Start (0 s): the first 0.35 s is low-level audio (rms about 0.1, then 0.4 at "I"). Source cut 1108.149 s lands inside the spoken "and" (large-v3 puts it at 1107.96-1108.5 s). Starting about 0.4 s later, at roughly frame 26579, would open cleanly on "I want".
- End (76.06 s): the cut comes right after "jet-ski"; the sentence is complete.

