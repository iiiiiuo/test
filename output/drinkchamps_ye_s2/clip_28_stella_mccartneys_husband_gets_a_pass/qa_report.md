# Clip_28 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `3f89be9543ea73bd00993b5e3a9ce7385f8ad61026f80910c18689d94d22d972`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 64.648 s, audio 64.648 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1550 (manifest 1550)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1550, "expected_frames": 1550, "video_duration_s": 64.647916, "audio_duration_s": 64.648, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 241, "asr_words": 241, "matched": 226, "match_ratio": 0.938, "matched_words_inside_their_caption": 0.956, "caption_onset_vs_first_word_s": {"n": 27, "median": -0.078, "max_abs": 0.918}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items
1. Structure: PASS. Starts at "No, man, come on" (source ctx: prior words "take a shot" are outside); ends on resolved "You get a pass from the culture, right?" (next source words "but that said" excluded). Standalone coherent.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 64.648 s, audio 64.648 s, 1550/1550 frames, no decode errors.
3. Transcript accuracy: PASS. sync.txt HEARD matches displayed English (95.6% words in their caption); only filler differences ("uh", "yeah").
4. Translation fidelity: PASS. No clear errors; approved wording, names per naming rules.
5. Masking: PASS. auto.json unmasked_hits empty; no profane word in English text ("porn" not on list); Japanese not asterisked.
6. Timing/sync: PASS. Median onset -0.078 s; 28 captions, none under ~0.45 s ("You know what I'm saying?" 0.45 s, short but readable); no uncaptioned foreground sentence.
7. Typography/visuals: PASS. Sheets 1-2 vs ref_sheet: white bold Yu Gothic-style, black outline/shadow, EN above JP, centred, same size/position as reference, max 2 EN + 2 JP lines, no clipping.
8. Framing: PASS. Ye framed in sharp centre band with blurred fill; host shot at ~3.8 s centred; changes only at shot changes.
9. Source usage: PASS. Single interval part_4 frames [24042,25592), audio same range; no padding/repetition/joins.

Non-blocking notes
- Caption 35.30-35.75 is 0.45 s; readable but brief.

