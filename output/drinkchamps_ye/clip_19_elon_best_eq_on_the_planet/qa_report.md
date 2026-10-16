# Clip_19 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `767cd9f9d57a3fdb511deae0ac9b132f9f04ce85273071f52766f774935bcd0c`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 75.993 s, audio 75.992 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1822 (manifest 1822)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1822, "expected_frames": 1822, "video_duration_s": 75.992583, "audio_duration_s": 75.992, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 246, "asr_words": 245, "matched": 229, "match_ratio": 0.931, "matched_words_inside_their_caption": 0.965, "caption_onset_vs_first_word_s": {"n": 26, "median": 0.025, "max_abs": 0.545}}

## Critic rounds
- round latest: FAIL — IQ/EQ JP on wrong EN chunks → L010 chunk override

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (cosmetic: captions 15-16 (39.4-43.4s) show English with no Japanese; JP for that sentence appears only at 43.4s)
Fix: none required

1. Structure: PASS. Starts at "In a way, they got a guy..." (source ctx: prior line is the host's, clip begins ~0.2s before first word); ends on "I ain't gonna lie, yeah." which resolves the host's compliment. Coherent Ye-on-Elon/EQ story.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 75.9926s, audio 75.992s, frames 1822 = manifest, no decode errors.
3. Transcript: PASS. EN matches HEARD/source ctx (match_ratio 0.93; differences are ASR noise: "Relaxation guy" interjection rendered as "— Yeah", approved as LOW).
4. Translation: PASS. JP matches the approved CSV and meaning at each moment. L010 JP deliberately omits the LOW interjection (approved note). No clear errors.
5. Masking: PASS. "s**t" at 53.7s masked; auto.json unmasked_hits empty; JP not mechanically masked.
6. Timing/sync: PASS. Median caption onset vs first heard word 0.025s; no flashing; all foreground speech has English captions (gap only 0.0-0.5s before first word).
7. Typography: PASS. sheet_1.jpg vs ref_sheet.jpg: white bold Yu Gothic, black outline/shadow, EN above JP, centred, same size/vertical position, max 2 EN + 2 JP lines (max_lines 4), no clipping, readable on the white shirt.
8. Framing: PASS. Ye framed in the sharp band throughout with blurred fill above/below, hat/head not cut off (frames 0.05-75.91); single fixed crop, no mid-shot changes.
9. Source usage: PASS. One half-open interval [41692,43514) of part_5, matches 1822 frames; no padding or repeats.

Non-blocking notes
- Captions 15-16 (39.37-43.38s, "This is a person... — Yeah." / "This is a person that a lot of people") have no JP; the JP for that sentence arrives at 43.4s. Approved design, but a JP-reading viewer sees a ~3.8s gap.
- Caption 26 (70.4-72.26s) JP is only "あんたには", with the continuation at 72.28s; reads slightly staccato.
- Final "yeah" at 74.78-75.97 is clipped at the clip end rather than the source's trailing "yeah, yeah"; acceptable.

