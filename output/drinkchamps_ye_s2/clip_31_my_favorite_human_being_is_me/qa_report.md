# Clip_31 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `8326f691a03fd2e5059ca9d0f3e8c464305a34d73b589d2908d5d395cac78aa7`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 70.529 s, audio 70.529 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1691 (manifest 1691)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1691, "expected_frames": 1691, "video_duration_s": 70.528791, "audio_duration_s": 70.529, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 198, "asr_words": 195, "matched": 181, "match_ratio": 0.914, "matched_words_inside_their_caption": 0.945, "caption_onset_vs_first_word_s": {"n": 23, "median": -0.145, "max_abs": 2.125}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (ending cuts immediately after "in the world", continuous speech follows in source; sentence/quote is complete)
Fix: none

1. Structure: PASS. Opens at 157.36 on "I remember I used to play ball..." (speech onset 157.50; prior line ends 157.32). Join at 215.92/220.80 follows "I'm going to Drink Champs." (ends 215.79) into "And think about this." (starts 220.77); reads naturally. Ends on completed quote "man, most influential in the world."
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 70.529 s, audio 70.529 s, frames 1691 = expected, no decode errors.
3. Transcript: PASS. All 25 captions match HEARD (sync.txt); only ASR misses/filler differences.
4. Translation: PASS. No clear errors; JP lines attached to the correct moments.
5. Masking: PASS. "ni**a's" at 7.72 masked; unmasked_hits empty; JP not mechanically masked.
6. Timing/sync: PASS. Onsets track speech (e.g. 30.01 caption vs "does" ~29.99; 65.17 "He said" vs 65.29). Gaps 12.44-13.12, 28.36-30.01, 38.5-39.1, 41.22-43.84 (no ASR words, crosstalk/reaction), 43.84 onward captioned. Shortest caption ~1.14 s (58.56-59.72, 1.16 s; 59.74-61.14 etc.), readable.
7. Typography/visuals: PASS. White bold Yu Gothic with black outline/shadow, EN above JP, centred, size/position consistent with ref_sheet; max 2 EN + 2 JP lines; no clipping; readable over white shirt.
8. Framing: PASS. Ye, the host-side cutaways (guest at ~13-17 s, host at ~19 s) are centred in the sharp band with blurred fill above/below; changes only at shot changes.
9. Source usage: PASS. Two half-open intervals from part_5 (3772-5176, 5293-5580), non-overlapping; no padding/freeze/repetition; join does not distort meaning.

Non-blocking notes
- Ending is tight: speech continues in the source right after "world" (clip end 70.53 vs last word end ~70.45); a few frames more would soften the cut but the quote is complete.
- Start tail of the previous line ("Got that Denny's?") ends 157.32, 0.04 s before the in-point; no audible bleed observed (RMS at 157.36-157.5 is low).

