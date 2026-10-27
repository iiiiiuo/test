# QA report — full_source_translation_20261027_030524

final.mp4 sha256 `251215934a6e3d912add3153dc7a3d9ae169eec3ea92f0a7aa96eab63f277a07` (stream MD5 v `03dc4760…`, a `fcf1edfc…`; matches the QA'd render in work/).
Subtitles: subtitles.ass (50 events, 0 annotation rows), style = frozen subtitle_style_spec v1 (output/shared/subtitle_style_spec.md) minus the explanation row; same font file hash (d923a57f…) and renderer (FFmpeg 6.1.1 libass).

## Gauntlet
| Round | Target | Change | Verdict | Largest gap |
|---|---|---|---|---|
| 0 (self-check) | framing | 2 shots re-centred (71.6–73.6 s Travis at right edge; 124.4–127.4 s Travis at left) | — | — |
| 1 | full render | — | FAIL (item 4 only) | 6 captions 0.35–0.5 s early (011, 019, 020, 024, 038, 039): large-v3 onsets absorbed leading music |
| 2 | 6 caption starts moved to measured voice onset | re-render; text unchanged | PASS | none |

Fresh Clip Critic (independent context; given task, rubric, render, source, subtitles, approved translation, reference, style spec only).

## Hard acceptance conditions
```
FINAL VIDEO COUNT = 1
VIDEO SOURCE = SOURCE_VIDEO.mp4
AUDIO SOURCE = SOURCE_VIDEO.mp4
FULL VIDEO USED = YES            (3917/3917 frames, PTS identical to source)
FULL AUDIO USED = YES            (130.714 s, xcorr lag 0 at 8+ points, corr ≥0.9994)
UNAUTHORIZED CUTS = NO
UNAUTHORIZED SPEED CHANGES = NO
ORIGINAL SCENE ORDER PRESERVED = YES (band vs source crop mean abs diff 0.2–0.6 at offset 0)
FINAL DURATION MATCHES SOURCE = YES (video 130.697233 s, audio/format 130.714 s — identical to source)
FINAL ASPECT RATIO = 9:16        (1080x1920, SAR 1:1)
ALL RELEVANT ENGLISH SPEECH CHECKED = YES
TRANSLATION COVERAGE = FULL SOURCE
LYRICS ANNOTATIONS CHECKED = N/A (no 1.lyrics.txt)
ANNOTATIONS VISIBLE IN VIDEO = NO
JAPANESE TRANSLATION APPROVED = YES (giub, 2026-10-27 04:53 UTC)
APPROVED TRANSLATION MODIFIED = NO (only re-chunking/line breaks; 018 not shown as approved)
ENGLISH SUBTITLES MATCH AUDIO = YES (approved EN; 026/039 are giub's confirmed wording)
JAPANESE SUBTITLES MATCH APPROVAL = YES (script diff: identical)
SUBTITLE TIMING = PASS           (19+ captions measured; all within ~0.25 s, none late)
REFERENCE STYLE = PASS
YU GOTHIC BOLD = PASS            (incl. ♪ glyph, no fallback)
OUTLINE / SHADOW = PASS
VERTICAL FRAMING = PASS
AUDIO / VIDEO SYNCHRONIZATION = PASS
ACTUAL RENDER INSPECTION = PASS
```

## Notes
- Audio was re-encoded from Opus to AAC 256 kb/s (MP4 compatibility); no filters, gain or edits. The residual vs the source is at the codec-noise level (SNR ≈30 dB).
- English masking: no word on the mask list occurs in this source.
- Evidence: work/runs/full_source_translation_20261027_030524/qa/ (contact.png, style_cmp.png, framing_cmp.png, spec_zoom.png, new_36.80.png, new_99.90.png), verify_render2.json.
