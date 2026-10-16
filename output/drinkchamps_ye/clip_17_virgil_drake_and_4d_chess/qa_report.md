# Clip_17 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `c4d1fbdb4e61ce2342d110f9aaaa2e225bd1f0f2ebff409460352df7e31d1c06`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 72.823 s, audio 72.823 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1746 (manifest 1746)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1746, "expected_frames": 1746, "video_duration_s": 72.82275, "audio_duration_s": 72.823, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 251, "asr_words": 249, "matched": 240, "match_ratio": 0.956, "matched_words_inside_their_caption": 0.992, "caption_onset_vs_first_word_s": {"n": 29, "median": 0.075, "max_abs": 0.455}}

## Critic rounds
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (non-blocking: L006 "took the watch to Drake" vs both ASR passes hearing "from Drake")
Fix: none

## Items
1. Structure: PASS. Starts at Ye's "Puff is my idol, bro" (prior speech ends 1884.99, clip starts 1885.17, first word ~0.46 s in); ends on "That man's a warrior." (ASR end 1957.80, clip end 1958.00, next speech 1958.52); topic resolved, host interjection at 37.8 s reads naturally.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 72.823 s / audio 72.823 s, 1746 frames = manifest, no decode errors.
3. Transcript accuracy: PASS. sync.txt SUB vs HEARD match (match_ratio 0.956); differences are ASR noise ("paddock"=Patek, "when/times", "from/to").
4. Translation fidelity: PASS. All 30 captions have approved JP matching rev3 CSV, attached to the right moments; no dropped lines.
5. Masking: PASS. unmasked_hits empty; no masked-word candidates in the text; JP unmasked.
6. Timing/sync: PASS. Onset vs first word median 0.075 s, max 0.455 s (first caption, 0.585 s vs word at ~0.46 s, fine); 99.2% of matched words inside their caption; shortest caption 0.82 s ("I want to address that."); gaps only 64.97-65.57 and 67.38-67.79 (pauses).
7. Typography/visuals: PASS. sheets/f_0038.08.png vs ref_sheet: white bold Yu Gothic, black outline/shadow, EN above JP, centred, same vertical position (~y 950-1040 at 1080x1920), max 2 EN + 2 JP lines, no clipping; readable on bright backdrop.
8. Framing: PASS. Ye framed in sharp band with face in upper-centre, blurred fill above/below; framing changes only at shot changes (frames 910 and 1031); host shot at 38 s has face centred in band.
9. Source usage: PASS. Single interval part_4 frames [45199,46945) half-open, continuous, no padding/freeze/repetition; no joins.

## Non-blocking notes
- L006 EN shows "Virgil took the watch to Drake" while turbo ASR and render ASR both heard "from Drake" (approved CSV notes this and chose "to"; host then says "from Drake"); JP "Drakeに時計を作ったんだよ" is the approved wording. Audio not re-listened to; left as approved.
- Caption 12 line-wraps "You know what I'm saying? He / knew that..." leaving "He" at line end; cosmetic.

