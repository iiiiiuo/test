# Clip_10 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `6305c6d87669d836770d6151584e7d00a9c2b2af3cc86e4915a12ea6065087d9`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 71.613 s, audio 71.613 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1717 (manifest 1717)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1717, "expected_frames": 1717, "video_duration_s": 71.613208, "audio_duration_s": 71.613, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 178, "asr_words": 187, "matched": 170, "match_ratio": 0.955, "matched_words_inside_their_caption": 0.988, "caption_onset_vs_first_word_s": {"n": 25, "median": 0.09, "max_abs": 0.78}}

## Critic rounds
- round 1: FAIL — wide shot 19252-19331 cut Ye off at right edge; caption "But..." 1.2 s early → manual 1.2x punch crop on Ye for that shot (work/b/framing_overrides.json); timing rules
- round latest: FAIL — JP for Jewish/black people shown 3-6 s early; "He offered it." repeat uncaptioned; "But" early → chunk override for L014 (EN-only lead-in), L004 window extended to 794.95, primary ASR pass chosen by match count

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (non-blocking: ~3.7 s silent mid-sentence pause 43.6-47.2 s, and ending "I know that." hangs without payoff)
Fix: none required

## Items
1. Structure: PASS. Starts at clean low-energy point (audio rms dip at -0.1..0.0 s, "We" onset 0.0-0.2 s in render ASR); source_context shows preceding words ("cardia uzi... we had cravo and um") are before the cut. Ends on complete sentence "I know that." (71.06-71.54 s), next source sentence begins 842.27 s so no cut mid-word. Standalone: question, Ye's answer, "God put me on a timeout", dad advice; understandable. Ending is a hanging acknowledgement (non-blocking).
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 71.613 s, audio 71.613 s, frames 1717 = expected 1717, decode_errors empty, a/v start 0.
3. Transcript accuracy: PASS. sync.txt: 95.5% token match, 98.8% matched words inside their caption; HEARD diffs are ASR errors (Cravo=Quavo, "yay"=Ye, "I agree with God"=that). No meaningful mismatch.
4. Translation fidelity: PASS. All JP rows match approved rev3 (L001-L014); dropped_lines empty. "Real s**t"=マジな話, "technical foul"=テクニカル・ファウル, "timeout"=タイムアウト all consistent with speech. Caption 23 (63.00-68.48 s, "Because I know for a fact, um, you know,") is EN-only because the approved L014 JP starts at "pissing off..."; filler lead-in, not a clear error.
5. Masking: PASS. auto.json unmasked_hits = []; only "Real s**t." masked at 6.39 s. "pissing" is not on the mask list. JP not mechanically masked.
6. Timing/sync: PASS. 25 captions, onset median 0.09 s vs first heard word (max_abs 0.78 s, not visible as lag in checked spans); shortest caption "Yeah." 1.02 s, "Real s**t." 1.14 s, readable. Uncaptioned speech: 18.15-20.27 s "He, uh... / oh no no" (short hesitation/crosstalk, acceptable). No uncaptioned full foreground sentence.
7. Typography/visuals: PASS. f_0000.05, f_0029.46, f_0071.53, sheets vs ref_20.png/ref_sheet.jpg: white bold Yu Gothic, black outline+shadow, EN above JP, centred, same size/vertical position (just under band centre, y~950-1100), max 2 EN + 2 JP lines (max_lines 4), no clipping, readable on bright yellow and dark backgrounds.
8. Framing: PASS. Faces in sharp centre band (1080x1042 @y438) with blurred fill above/below as in reference. Wide shot at ~30.8-34.3 s (f_0032.57.png): Ye at far right edge, hand over face, right shoulder cropped but face fully in frame; this is a source wide shot with a 1.2x punch, acceptable (non-blocking). First 5 frames (0.00-0.21 s) show Ye before cut to host while host's voice speaks (source camera cut, f_0000.05 vs f_0000.33); brief, non-blocking.
9. Source usage: PASS. Single interval part_3 frames [18474, 20191) (1717 frames, pts 18492474..20211191, tb 1/24000), audio same range, no padding/freeze/repetition; no joins. "He said he offered it" repeats are genuine speech in the source.

## Non-blocking notes
- 43.56-47.2 s: ~3.7 s of near-silence (rms ~2000 vs ~6000+ speech) between "I understand," and "but you got to be more sophisticated". It is a thinking pause within one sentence (source-contiguous), but a viewer may feel it drag; could be shortened only with a documented jump cut.
- 34.34-36.08 s and 18.36-20.36 s are also short silent/hesitation gaps; fine.
- Ending "I know that." with the host on screen leaves the point unresolved (source continues with Ye's explanation at 842.27 s, which would overrun/extend); acceptable.
- Speaker of final line (63-71 s) shows host on screen; approved CSV attributes it to Ye. Not a caption error.

