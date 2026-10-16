# Clip_06 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `6e80dff45b4f09f0e5f48622a291d6e4ecfa528395b92094eb06ae107a499a15`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 75.158 s, audio 75.158 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1802 (manifest 1802)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1802, "expected_frames": 1802, "video_duration_s": 75.158416, "audio_duration_s": 75.158, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 149, "asr_words": 158, "matched": 136, "match_ratio": 0.913, "matched_words_inside_their_caption": 0.978, "caption_onset_vs_first_word_s": {"n": 21, "median": 0.128, "max_abs": 2.018}}

## Critic rounds
- round 1: FAIL — "I like both." 2.4 s early (Whisper glued onset of "I" to previous word); "I forgive" 1.6 s early → build_subs: onset moved to just before next heard word when gap >0.8 s; non-final chunk no longer held over long pause; pre-onset only after previous line
- round 2: PASS — none (round 2) → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (non-blocking: caption 16 (41.56-49.82s) appears ~1.0s before first heard word and shows "I forgive Big Sean" ~6s before it is spoken at 47.9s)
Fix: none (optional: start caption 16 at ~42.4s or split "Big Sean. May they all be forgiven." / "I forgive Big Sean")

## Items
1. Structure: PASS. Question, "I like both", "Take a shot" (0-6.0s), jump cut, then Ye's "God said not to compare..." through the forgiveness list to "I forgive the left party." Join reads as a natural pivot; ending is a complete sentence, next source sentence (1216.75s onward) not included. Audio at 1147.60s is just past a syllable onset (RMS dip at 1147.50-1147.55), so a possible 50 ms clip of "So," that ASR did not hear; not noticeable.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, 1802/1802 frames, video 75.158s, audio 75.158s, no decode errors.
3. Transcript accuracy: PASS. HEARD matches captions throughout (sync.txt). Only differences: "Who else is you again?" vs render ASR "Who loves you again?" (approved csv marks LOW, read as "who else?"; 62.5s, host reaction line, not blocking); "Take a shot." (5.05s) not picked up by ASR but present in source ASR at 1111.32-1111.80.
4. Translation fidelity: PASS. All 25 captions have JP matching approved rev3 rows; no clearly wrong/misplaced JP.
5. Masking: PASS. auto.json unmasked_hits = []; "bum-ass" is not on the mask list; no mechanical asterisks in JP.
6. Timing/sync: PASS. Median onset offset 0.13s, 97.8% of matched words inside their caption. Non-blocking early onsets: caption 16 about 1.0s early (41.56 vs first word 42.52s) and long hold, caption "Um, I forgive, uh..." 0.75s early (55.34 vs 56.09s). No uncaptioned foreground sentence; 58.5-62.5s and 39-41.5s are meaningful silent pauses.
7. Typography/visuals: PASS. f_0045.69.png and sheets: white bold Yu Gothic, black outline/shadow, centred at y~950-1140, EN above JP, max 2 EN + 2 JP lines, within frame and readable on the bright yellow background; consistent with ref_sheet.jpg size/position.
8. Framing: PASS. Faces in the sharp band 438-1480 with blurred fill above/below; Envy shot 0-6s, Ye close-ups, host cutaway at 16-17.5s; framing changes only at shot cuts (manifest pieces). Ye looks down at 45s but head stays fully in frame.
9. Source usage: PASS. Manifest part_2_2, two half-open intervals [26512,26656) and [27514,29172), 144+1658=1802 frames, no overlap, no padding or repetition; the jump drops Jay Electronica chatter and does not distort meaning.

## Non-blocking notes
- Caption 16 and caption 13 (22.98-29.62s) are long phrase holds that preview words before they are spoken; splitting would match the reference rhythm better.

