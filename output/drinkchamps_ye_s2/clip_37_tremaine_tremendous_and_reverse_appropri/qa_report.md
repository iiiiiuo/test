# Clip_37 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `d1f2c04cdbaac9473196b83583be8aae9cd1cfeb92f07491be795dca0251a8b8`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 67.150 s, audio 67.150 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1610 (manifest 1610)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1610, "expected_frames": 1610, "video_duration_s": 67.150416, "audio_duration_s": 67.15, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 208, "asr_words": 207, "matched": 184, "match_ratio": 0.885, "matched_words_inside_their_caption": 0.978, "caption_onset_vs_first_word_s": {"n": 23, "median": 0.06, "max_abs": 1.86}}

## Critic rounds
- round 1: PASS — cosmetic: caption 4 onset ~1.9 s before words (host stutter) → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (cosmetic only: caption 4 "The Supreme Lives Matter" onsets at 6.98s while the words are heard ~8.9-10.6s, host stuttering "the, um" before it)
Fix: none

1. Structure: PASS. Opens on the host question "Why are you wearing the Trump..." (prev source line is unrelated chatter, clean break), ends after "It's bigger than White Lives Matter." (source speech ends 930.04, clip 930.47). Standalone clear.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 67.150s / audio 67.15s, 1610 frames = manifest, no decode errors.
3. Transcript: PASS. HEARD matches captions through the clip. "It's not Trump" (4.6-6.56) is not in the render ASR, but a local large-v3 check of source 867.5-869.6 hears Ye "It's not true/Trump... No." at 867.88, matching the approved row. Tremaine/Skete/Dov Charney are proper-noun spellings from the approved CSV; ASR variants are ASR errors.
4. Translation: PASS. JP matches the EN at each moment; no clear errors.
5. Masking: PASS. auto.json unmasked_hits empty; no listed profanity in this clip.
6. Timing/sync: PASS. Median onset offset 0.06s, 97.8% of matched words inside their caption. Only lead is caption 4 (see above, stutter). No long uncaptioned speech; shortest caption 0.77s ("excuse me...", short phrase, readable).
7. Typography/visuals: PASS. White bold Yu Gothic with black outline/shadow, EN above JP, centred, up to 2 EN + 2 JP lines, same size/vertical position as reference, inside frame (f_0065.66.png), readable on the bright gold background.
8. Framing: PASS. Sharp centre band with blurred fill above/below as in reference; faces in frame in sheets. Ye's cap brim hides his face in the head-down moment around 11-14s (natural pose, not a framing fault). Cutaways to host/Ye on shot changes only.
9. Source usage: PASS. One interval, part_6 frames [20698, 22308), audio same range; no padding, freeze or repetition.

Non-blocking notes
- Caption 4 could start ~1s later to track "Supreme Lives Matter" more tightly; not worth a re-render.
- Opening 0-4.6s shows Ye (toast) while the host speaks off-screen; acceptable reaction cutaway.

