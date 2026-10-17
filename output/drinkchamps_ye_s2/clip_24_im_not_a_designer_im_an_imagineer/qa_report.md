# Clip_24 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `c6fc16ac755a2381b082167c742091da0aff643d822afe84a496702a4e81e7eb`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 65.482 s, audio 65.482 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1570 (manifest 1570)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1570, "expected_frames": 1570, "video_duration_s": 65.482083, "audio_duration_s": 65.482, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 195, "asr_words": 197, "matched": 187, "match_ratio": 0.959, "matched_words_inside_their_caption": 0.973, "caption_onset_vs_first_word_s": {"n": 23, "median": -0.034, "max_abs": 1.694}}

## Critic rounds
- round 1: FAIL — L002 shown 1.1 s early over uncaptioned 'I ain't gonna lie, I've been' → interval 2 start moved to 'since' (frame 35657)
- round 2: FAIL — L012 JP order inverted vs EN (46.43-50.77) → chunks override Clip_24_L012
- round 3: PASS — non-blocking: 44.03 fragment EN-only → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

## Items
1. Structure: NOT IN SCOPE
2. Duration/format: PASS. qa/auto.json format.PASS true; 1080x1920, SAR 1:1, video 65.482083 s, audio 65.482 s (60 <= d < 120), 1570 frames = expected 1570, no decode errors; ffprobe confirms.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS. Only masked form in ASS/SRT is "s**t" (0:50.79); grep finds 0 unmasked shit/fuck/bitch/nigg/pussy/motherf hits; auto.json unmasked_hits empty; the only asterisks are in the EN row, none in Japanese rows.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS. Frames f_0021.66, f_0037.24, f_0064.48 vs ref_20.png: white bold Yu Gothic, black outline plus shadow, EN above JP, centred, same vertical band as the reference (EN starts y~948), max 2 EN + 2 JP lines, nothing clipped, readable on the bright white shirt and yellow backdrop.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS. Three Expl events, one per approved key; text verbatim vs glossary_draft_s2.json:
   - L006 "スティーブ・ジョブズ：Appleの共同創業者": 18.35-22.21 s (3.86 s), starts with the Steve Jobs caption; frame f_0021.66 (inside span): one line at y~1208, below JP block, centred, inside band.
   - L009 "イマジニア：imagine（想像）とengineer（技術者）を／合わせた造語。Disneyの用語": 32.57-39.81 s (7.2 s), starts with the "imagineer" caption; frame f_0037.24 (inside span, 4-row EN+JP above): two lines at y~1207/1255, clear gap to JP (bottom ~1150), break falls between を / 合わせた (no split word); text width within frame.
   - L016 "トラウマ経済：人々の苦しみを消費して利益を生む／構造を指すYeの言葉": 63.17-65.48 s (2.31 s, >= 2 s), starts with the "trauma economy" caption; frame f_0064.48 (inside span): two lines at y~1158/1205 below the 3-row EN+JP block; break between 生む / 構造 (no word split).
   All Expl rows: style Expl, Yu Gothic 40, white fill, black outline, shadow, y 1138..1284 max, inside sharp band 438..1480; no overlap with EN/JP rows in any frame. No extra frames needed (supplied frames fall inside all three spans).

## Non-blocking notes
- Clip_24_L012 first caption (44.03-46.41 s, "So even if, say, say, say, we wanted to, like,") has no JP row; the sentence continues and the JP appears on the next caption (46.43 s). Outside this round's scope and unchanged from the previous render; flagging only.
- L016 explanation ends with the clip (2.31 s), acceptable at the minimum readable length.

