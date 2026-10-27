# QA report — full_source_translation_20261027_105548

final.mp4 sha256 `18d290d9366cc50a459f3cda21636c42a082fac2fa6bb43e53cd7f40eec8f96f` (byte copy of work/runs/full_source_translation_20261027_105548/render3.mp4, which was checked).
Subtitles: subtitles.ass (52 events from 49 approved lines; 013, 045 and 049 split across two events; no annotation rows). Style = frozen subtitle_style_spec v1 without the explanation row, same font hash (d923a57f…) and renderer (FFmpeg 6.1.1 libass) as runs _030524 / _070832.
Source: iPhone screen recording, HEVC VFR (1/600 timebase), rotation 90 → 2556x1180 with side bars; programme picture x 230–2325.

## Gauntlet
| Round | Change | Verdict | Largest gap |
|---|---|---|---|
| 1 | full render (render2) | FAIL | in the 5 two-shots the crop showed only the listening host and cut out Snoop, who was speaking |
| 2 | two-shot windows moved to the left edge (both faces in frame); 130.85–135.12 too (render3) | PASS | none |

The Fresh Clip Critic ran in an independent context (task, rubric, render, source, subtitles, approved translation, reference and style spec only). Reports: work/runs/full_source_translation_20261027_105548/qa/fresh_critic_r1.md, fresh_critic_r2.md.

## Hard acceptance conditions
```
FINAL VIDEO COUNT = 1
VIDEO SOURCE = SOURCE_VIDEO.mp4 (the attached ScreenRecording_10-26-2026 15-15-33_1.mp4)
AUDIO SOURCE = SOURCE_VIDEO.mp4 (same file)
FULL VIDEO USED = YES            (4903/4903 frames, PTS list identical)
FULL AUDIO USED = YES            (AAC packets md5 identical; decoded samples bit-identical)
UNAUTHORIZED CUTS = NO
UNAUTHORIZED SPEED CHANGES = NO
ORIGINAL SCENE ORDER PRESERVED = YES (band vs source crop mean abs diff 0.38 at offset 0, 0.8+ at ±1 frame)
FINAL DURATION MATCHES SOURCE = YES (video 135.797 s = last PTS + frame duration; audio 135.789 s presentation end, same as source; source container reports 135.812 s from its edit list)
FINAL ASPECT RATIO = 9:16        (1080x1920, SAR 1:1)
ALL RELEVANT ENGLISH SPEECH CHECKED = YES
TRANSLATION COVERAGE = FULL SOURCE
LYRICS ANNOTATIONS CHECKED = N/A (no 1.lyrics.txt)
ANNOTATIONS VISIBLE IN VIDEO = NO
JAPANESE TRANSLATION APPROVED = YES (giub, 2026-10-27 14:27 UTC)
APPROVED TRANSLATION MODIFIED = NO (only caption chunking/line breaks)
ENGLISH SUBTITLES MATCH AUDIO = YES, as approved (critic note: "Sonny" at 67.6 s is clearly spoken (large-v3 p=0.88) but was left out of the approved EN; possible "bro" at 24.2 s is uncertain)
JAPANESE SUBTITLES MATCH APPROVAL = YES (script diff)
SUBTITLE TIMING = PASS
REFERENCE STYLE = PASS
YU GOTHIC BOLD = PASS
OUTLINE / SHADOW = PASS
VERTICAL FRAMING = PASS
AUDIO / VIDEO SYNCHRONIZATION = PASS (source audio edit list: 1033-sample empty edit; copy decodes those as zeros, so every sample keeps its presentation time)
ACTUAL RENDER INSPECTION = PASS
```
Kept from the source: YouTube UI at 0–0.6 s and the iOS Control Center from about 134.9 s (the screen recording being stopped).
Masking (display EN only): s**t ×3. Evidence: work/runs/full_source_translation_20261027_105548/qa/, verify_render1-3.json.
