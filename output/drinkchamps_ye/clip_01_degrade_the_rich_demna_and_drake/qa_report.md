# Clip_01 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `331bd1c36ab32ac11387d5c8906924bf9d22040f17755f888d2e64c73582ab36`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 64.106 s, audio 64.106 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1537 (manifest 1537)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1537, "expected_frames": 1537, "video_duration_s": 64.105708, "audio_duration_s": 64.106, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 162, "asr_words": 162, "matched": 153, "match_ratio": 0.944, "matched_words_inside_their_caption": 0.987, "caption_onset_vs_first_word_s": {"n": 20, "median": 0.103, "max_abs": 1.383}}

## Critic rounds
- round 1: FAIL — clip ended ~0.1 s before last word "ever" while caption showed it → systematic boundary audit of all 42 boundaries (scripts/boundary_check.py) -> 15 clips moved to quietest point between last included and first excluded word (scripts/refine_bounds.py, work/b/boundary_changes.json); Clip_01 host aside (LOW, untranslated) removed by jump cut
- round 2: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

## Items
1. Structure: PASS. Opens on "Because as a person that" right after the host's "let me ask you something"; ends on "Drake is the greatest rapper ever." with the next speech (1270.79 "And you said in war") excluded (audio rms 1.3k after 1270.3). Standalone and coherent.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 64.106 s / audio 64.106 s, 1537 frames = expected, decode_errors empty.
3. Transcript accuracy: PASS. Displayed English matches HEARD lines in sync.txt; only ASR noise ("yay" for Ye, "this is closed" for "the clothes is").
4. Translation fidelity: PASS. All 22 captions carry approved rev3 JP, no dropped lines, each attached to its own moment.
5. Masking: PASS. "motherf**kers" is the only listed word, masked in EN; auto.json unmasked_hits is empty; JP is not masked.
6. Timing/sync: PASS. Caption onset vs first word: median 0.10 s, 98.7 % of matched words fall inside their caption. Only uncaptioned span is 30.44-31.03 (host laugh/jump-cut gap). "You know" caption at 31.03 lags the "you" by about 0.2 s, acceptable. No caption flashes: the shortest is caption 4 at 0.62 s, a short phrase.
7. Typography/visuals: PASS. sheet_1/sheet_2 match the reference: white bold text with outline, EN above JP, centred, same vertical position, max 2 EN + 2 JP lines, no overflow or clipping, legible on the bright gold background.
8. Framing: PASS. Faces sit in the sharp centre band with blurred fill above and below. Crops change only at shot changes (host to Ye to host to Ye). Ye is tightly cropped at the left edge during 36-43 s but the face stays in frame.
9. Source usage: PASS. One source (part_1), two half-open intervals [28860,29598) and [29659,30458), no overlap. The jump removes only the host's "That was a good one" (1234.48-1237.03) after "hop over...". The join lands at a low-energy gap (rms 2.3k at 1237.02) and reads naturally; no padding, freeze or repetition.

## Non-blocking notes
- First ~80 ms of render audio has energy (rms 6-8k) before a dip at ~0.1 s. It may be a faint tail of the host's "something" (ASR places its end at 1203.73, the clip starts 1203.70). Could trim 2-3 frames at the start if wanted.
- Caption 13 "Because we'll hop over..." ends at 30.44 while the join is at 30.78. This is harmless because the gap shows the host laughing.

