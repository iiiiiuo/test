# Clip_04 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `56e92fc98f06dfaee4d2c44b3755a4807e742c393b136ddd9c1e2504c824d1d5`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 75.117 s, audio 75.117 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1801 (manifest 1801)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1801, "expected_frames": 1801, "video_duration_s": 75.116708, "audio_duration_s": 75.117, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 248, "asr_words": 250, "matched": 222, "match_ratio": 0.895, "matched_words_inside_their_caption": 0.986, "caption_onset_vs_first_word_s": {"n": 30, "median": 0.07, "max_abs": 1.084}}

## Critic rounds
- round 1: FAIL — false face (backdrop crest) framing 43-52 s; LOW lines L015-L017 captioned as a guess → crest saturation filter + cluster consistency in framing; jump cut removing L015-L017
- round 1: FAIL — "Stadium. Bad Bunny..." one 5.9 s caption ~3 s early → same pause-break rule (split "Stadium." / "Bad Bunny...")
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (cosmetic: caption 22 "I'm sorry." / 悪いね is shown only 0.42 s, 50.03-50.45)
Fix: none

## Items
1. Structure: PASS. Opens on Ye's "like right now when me, James Blake..." (source 30.53 is a quiet gap before onset at ~30.70, no mid-word start); middle is coherent (stadium question, Bad Bunny wall, reggaeton claim, "everything we look at"); ends on "That's how I look at everything." (render 74.0-75.03, tail level drops to near silence at 75.05). Jump cut at render 50.467 (after "I'm sorry." to "So the thing is...") skips only crosstalk/"let's make some noise"; reads as a natural pivot.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 75.1167 s, audio 75.117 s, 1801 frames = expected, decode_errors empty.
3. Transcript accuracy: PASS. sync.txt: 98.6% of matched words fall inside their caption; differences are ASR errors ("broke reggae tone" vs source-context "brought Reggaeton"). Minor omission: spoken "You know what I'm saying?" (0.6-0.88) not shown in caption 1 (non-meaningful).
4. Translation fidelity: PASS. JP matches approved rev3 rows (L001-L014, L018-L024); dropped L015-L017 are absent as intended. See note on caption 28/29 line attachment.
5. Masking: PASS. auto.json unmasked_hits = []; no maskable word occurs in the English; JP not mechanically masked.
6. Timing/sync: PASS. Onset vs first heard word median 0.07 s (n=30, max 1.08 s on caption 1 which starts on "Okay" ahead of the main phrase). No uncaptioned foreground sentence; uncaptioned single "Stadium." at render 27.19 is a brief host word. No overlaps; all captions inside video length (max_end 75.10).
7. Typography/visuals: PASS. sheet_1/sheet_2 vs ref_sheet: white bold Yu Gothic, black outline/shadow, EN above JP, centred, same vertical position as reference (first line ~y948), max 2 EN + 2 JP lines (max_lines 4), no clipping; readable on white shirt and bright background.
8. Framing: PASS. Ye, host and N.O.R.E. shots are centred in the sharp band with blurred fill above/below as in the reference; heads not cut off; framing changes coincide with shot changes (sheet frames at 18.23/19.44/38.16/41.58/43.33).
9. Source usage: PASS. Manifest: part_2_2, frames [731,1941) and [2079,2670), half-open, same source, disjoint; no padding or freeze; the join drops only the unrelated crosstalk.

## Non-blocking notes
- Caption 22 ("I'm sorry." / 悪いね, 50.03-50.45) is below the 0.8 s spec minimum; could linger to ~50.57 (silence before "So the thing is" at 50.59) to give ~0.55 s.
- Captions 28/29: JP of caption 28 already says スタジアムも見るし while the English "we're looking at stadiums" appears in caption 29, whose JP shows only Bad Bunnyも見る (about 1-2 s early); approved wording, so not failed.
- Caption 1 holds "when me, James Blake," up to 3.1 s while the phrase continues; fine.

