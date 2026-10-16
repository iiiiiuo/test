# Clip_30 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `010a3b6d030037c7b236f81e1bcd6ee3ab3bbdc128d26f24775c9e6cd9347f27`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 94.761 s, audio 94.761 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2272 (manifest 2272)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2272, "expected_frames": 2272, "video_duration_s": 94.761333, "audio_duration_s": 94.761, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 247, "asr_words": 257, "matched": 245, "match_ratio": 0.992, "matched_words_inside_their_caption": 0.922, "caption_onset_vs_first_word_s": {"n": 28, "median": -0.334, "max_abs": 1.494}}

## Critic rounds
- round 1: FAIL — opens on uncaptioned tail 'thing is' (0-0.25 s) → start window 51.62-51.78 (frame ~1238)
- round 2: PASS — non-blocking: 0.06 s tail of 'is,' at open → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (non-blocking: clip opens ~0.06 s inside the tail of the previous word "is," before "this is the thing")
Fix: none required; optional: start at source frame 1240 (51.76 s) instead of 1238

## Items
1. Structure: PASS. Opens on "This is the thing" and goes straight into the Tuskegee point. Ends on "...told us not to talk to each other", where audio energy has dropped (RMS ~1300 at 94.7 s) before the source's next "Yeah, like...". Standalone and coherent. Minor: the first ~60 ms is the tail of "is," (source ASR: "is," ends 51.74, "this" starts 51.78, cut at 51.676); see note.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 94.761 s, audio 94.761 s, frames 2272 = expected, decode_errors empty.
3. Transcript accuracy: PASS. sync.txt SUB vs HEARD match on all 28 captions (match ratio 0.992). No meaningful mismatches.
4. Translation fidelity: PASS. Spot-checked all 28 rows against the English and context. Meaning is intact, with no wrong-moment attachment. "Drink Champs" is kept in English per the naming rules.
5. Masking: PASS. auto.json unmasked_hits is empty. No listed words are spoken in this clip. The Japanese has no mechanical asterisks.
6. Timing/sync: PASS. Onsets track first heard words (e.g. caption 24 at 79.18 s vs speech ~79.2 s; caption 1 at 0.04 s). Longest gap with no caption is 75.90-79.18 s. I checked that span with a span-only ASR on the source and found no words, only laughter/crosstalk (loud, non-speech) over Ye smiling. The pause or reaction is meaningful and acceptable. Every caption lasts at least 1.1 s.
7. Typography/visuals: PASS. sheet_1/2 and f_0076.08 show white bold Yu Gothic with black outline and shadow, EN above JP, centred, at the same vertical band and size as ref_sheet. No more than 2 EN and 2 JP lines (max 4). No clipping or overflow, readable over the bright gold backdrop and white shirt.
8. Framing: PASS. Faces sit in the sharp centre band (1080x1042 at y=438) with blurred fill above and below like the reference. Crop changes at 1400/1427/2725/3032/3059 line up with speaker or shot changes. No cut-off heads (checked at 0.05, 6.88, 56.57, 76.08, 93.76 s).
9. Source usage: PASS. One interval, part_5 frames [1238, 3510), half-open, with matching audio segment and no auxiliary footage. No padding, freezes or repetition.

## Non-blocking notes
- The first ~0.06 s of audio (RMS ~8000 at t=0, no ramp) is the tail of the prior word "is,". It is a faint blip and is not likely to read as a mid-word start. Starting at frame 1240 would remove it.
- Caption 23 ("When you were talking right now, like...") stays up to 75.90 s, while the speech ends at ~74 s. This is harmless, since it holds through the trailing pause.

