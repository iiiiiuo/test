VERDICT: PASS
Blocking gaps: none
Largest gap: none (caption 10 "Boy, they did. Don't clap yet." appears at 27.70s but first heard word is ~28.9s, about 1.2s early over applause; non-blocking)
Fix: none required; optional: start caption 10 at ~28.8s

## Items
1. Structure PASS: starts 0.2s after prior speech (source ends 663.71, clip 663.91) on a full question; ends on "That's all they care about." (sync 77.80-78.98) before source continues "At the end of the day". Coherent, standalone.
2. Duration/format PASS: auto.json 1080x1920, SAR 1:1, video 78.9956s / audio 78.995s, 1894 = 1894 frames, no decode errors.
3. Transcript PASS: HEARD matches displayed English except ASR noise. Note: ASR hears "Good money in America" (twice) vs displayed "Good Morning America"; approved wording, plausible, flagged only as uncertain. "Boy, they did" is MEDIUM confidence per CSV note.
4. Translation PASS: all 25 captions have JP matching meaning; no clear errors.
5. Masking PASS: only "f**k" (67.85-69.90), masked with two asterisks; auto.json unmasked_hits empty; JP not mechanically masked.
6. Timing PASS: onset median 0.013s, 97.4% of matched words inside their caption. Shortest caption 1.24s (cap 12, 4 words) readable. Uncaptioned gaps 13.2-15.4, 31.1-34.8 are applause/reaction with no ASR speech (render_asr 30.62-34.82 silent of words). Caption 10 leads speech by ~1.2s (see largest gap).
7. Typography PASS: white bold Yu Gothic with black outline/shadow, EN above JP, centred, same vertical position (~y 975-1140) as reference; max 2 EN + 2 JP lines; no overflow (f_0054.47, f_0068.87). Legible on the bright wide shot.
8. Framing PASS: close crops of Ye/host centred in the sharp band with blurred fill (sheet_1). The wide shot (approx 42-70.6s) is the source's actual wide camera; Ye is off-camera during his lines 58.5-70s (host shown) and the lower half of the fill is near-black because the table is dark. Acceptable, not broken.
9. Source usage PASS: single interval part_6 frames [15917,17811) with consistent pts mapping; no freeze/padding/repetition.

## Non-blocking notes
- Wide shot shows the host while Ye speaks "Good Morning America..." (68.87s); a Ye shot would be nicer but none is chosen in framing.json.
- Dark lower fill in wide shot differs from the brighter reference fills.
