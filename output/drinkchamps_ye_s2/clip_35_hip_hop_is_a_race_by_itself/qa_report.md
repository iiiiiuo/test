# Clip_35 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `15974f7c95b188607b19be24967ed07940c8c87a6a043c1a34fe92c465552fd8`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 64.106 s, audio 64.106 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1537 (manifest 1537)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1537, "expected_frames": 1537, "video_duration_s": 64.105708, "audio_duration_s": 64.106, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 204, "asr_words": 211, "matched": 187, "match_ratio": 0.917, "matched_words_inside_their_caption": 0.963, "caption_onset_vs_first_word_s": {"n": 20, "median": -0.063, "max_abs": 1.14}}

## Critic rounds
- round 1: FAIL — 1.8 s uncaptioned repeated sentence at 41.93-43.75; next caption early → jump cut 638.43-641.52 + display EN 'the whole time' (L009)
- round 2: PASS — non-blocking: abrupt audio drop at join 41.70 → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

## Items
1. Structure: PASS. Opens on "But every single Black artist need to be on Tidal" (complete thought, source_context shows it follows "...that's better"). It ends on "we're doing it right now" (661.99-663.71 in source), which resolves the point. The single jump cut at 41.71s skips about 3s of repeated "this is a race / I've been trying to tell you" and reads naturally. A 0.35s breath follows the join before "hip-hop has no color".
2. Duration/format: PASS. auto.json gives 1080x1920, SAR 1:1, video 64.106s, audio 64.106s, 1537 of 1537 frames, no decode errors, A/V start 0.
3. Transcript accuracy: PASS. HEARD matches the captions apart from ASR noise (title/Tidal, "racist" at 39-40s, "Dream Champs", "block" vs the spelled "bloc"). 96% of matched words fall inside their own caption.
4. Translation fidelity: PASS. No clear errors against the heard speech. Cedric/Balenciaga switch lines, "tribe"/"race"/"people" (部族/人種/民), and the closing lines all match the meaning. "Tremendous" and Claude Anderson follow the approved naming rules.
5. Masking: PASS. auto.json reports unmasked_hits [] and no curse words appear in the English. The Japanese is not mechanically masked.
6. Timing/sync: PASS. Median onset error is -0.06s. Caption 1 starts 0.31s after the first heard word (0.02s), which is negligible. There are no uncaptioned sentences. The shortest caption, "Hip-hop is a race." (0.87s, 39.16-40.03), is brief but short enough to read.
7. Typography/visuals: PASS. White bold Yu Gothic-style text with black outline and shadow, EN above JP, centred, at the same vertical position and similar size as the reference (sheet tile y approx. 0.50-0.58). All captions wrap to at most 2 EN + 2 JP lines. No clipping (checked f_0041.79 and f_0064.03) and it stays readable on the bright gold background.
8. Framing: PASS. Faces sit in the sharp centre band with blurred fill above and below, as in the reference. Framing changes only at shot changes (Ye to interviewer and back). The Ye shot at 63.69 sits slightly low but is fully framed.
9. Source usage: PASS. Both intervals are from part_6: [14306,15306) and [15380,15917), half-open, with a gap of 74 frames. There is no padding, freeze or repetition, and the join does not distort meaning.

## Non-blocking notes
- The join at 41.70s drops audio from about 8600 to about 1000 RMS within 50ms, so "time" ends slightly abruptly. It is acceptable at speech pace.
- At 63.1-64.0 the speaker of "I feel like we're doing it right now" is ambiguous. The frame shows the interviewer at 63.11 and Ye at 63.69, so the line is attributed to Ye on screen. It follows the source cut.

