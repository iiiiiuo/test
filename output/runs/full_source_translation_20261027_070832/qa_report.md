# QA report — full_source_translation_20261027_070832

final.mp4 sha256 `f94944f80aaabf2763d6fcb08de0635e09251e3f023f7d5dd56639d71496b9b6` (byte copy of work/runs/full_source_translation_20261027_070832/render.mp4, which was checked).
Subtitles: subtitles.ass (28 events, no annotation rows). Style is the frozen subtitle_style_spec v1 without the explanation row, with the same font hash (d923a57f…) and renderer (FFmpeg 6.1.1 libass) as run full_source_translation_20261027_030524.
Source note: the MP4 hides 139 pre-roll video frames with an edit list. FFmpeg 6.1 with libdav1d still outputs them, so the render drops them (select n>=139). The presented 1528 frames keep their original PTS.

## Gauntlet
| Round | Change | Verdict | Largest gap |
|---|---|---|---|
| 1 | full render | FAIL (timing only) | 006/008/009/011/012 captions 0.32–0.39 s before the voice |
| 2 | those 5 starts moved to the measured onsets (8.96/12.58/15.84/18.72/22.84) | PASS | none (note: 008 first half was only 0.62 s) |
| 3 | 008 merged into one 12.58–15.52 caption with the same approved wording | self-check | frames at 12.55 and 14.0 s show no early caption and correct text; verify_render3.json unchanged otherwise |

The Fresh Clip Critic ran in an independent context. It was given the task, rubric, render, source, subtitles, approved translation, reference and style spec only.

## Hard acceptance conditions
```
FINAL VIDEO COUNT = 1
VIDEO SOURCE = SOURCE_VIDEO.mp4
AUDIO SOURCE = SOURCE_VIDEO.mp4
FULL VIDEO USED = YES            (1528/1528 presented frames, PTS identical)
FULL AUDIO USED = YES            (51.014 s; xcorr lag 0 at every 6 s window; residual SNR 38.1 dB = AAC codec noise)
UNAUTHORIZED CUTS = NO
UNAUTHORIZED SPEED CHANGES = NO
ORIGINAL SCENE ORDER PRESERVED = YES (band vs source crop mean abs diff 0.39 at offset 0, 5.3+ at ±1 frame)
FINAL DURATION MATCHES SOURCE = YES (video 50.984 s, audio/format 51.014 s; identical to source presented timeline)
FINAL ASPECT RATIO = 9:16        (1080x1920, SAR 1:1)
ALL RELEVANT ENGLISH SPEECH CHECKED = YES
TRANSLATION COVERAGE = FULL SOURCE
LYRICS ANNOTATIONS CHECKED = N/A (no 1.lyrics.txt)
ANNOTATIONS VISIBLE IN VIDEO = NO
JAPANESE TRANSLATION APPROVED = YES (giub, 2026-10-27 10:01 UTC; option 2 for 019/021)
APPROVED TRANSLATION MODIFIED = NO (only caption chunking/line breaks)
ENGLISH SUBTITLES MATCH AUDIO = YES (approved EN; ASR also hears "We embracing" at 006, "You asked" at 017, and the last word of 019 is unclear — wording as approved)
JAPANESE SUBTITLES MATCH APPROVAL = YES (script diff: identical)
SUBTITLE TIMING = PASS
REFERENCE STYLE = PASS
YU GOTHIC BOLD = PASS
OUTLINE / SHADOW = PASS
VERTICAL FRAMING = PASS          (note: DJ Envy half out of frame during the source's own whip pan 39.4–40.2 s)
AUDIO / VIDEO SYNCHRONIZATION = PASS
ACTUAL RENDER INSPECTION = PASS
```
Masking (display EN only): motherf**ker, ni**a, F**k, S**t (series two-asterisk form).
Evidence: work/runs/full_source_translation_20261027_070832/qa/ (contact.png, r3_008.png), verify_render1-3.json.
