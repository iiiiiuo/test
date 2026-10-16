VERDICT: FAIL
Blocking gaps: Item 1 (opening) t=0.00-0.25s / source frames 1233-~1238: render opens on the clipped tail of the previous sentence ("thing is", ASR words thing 0.0-0.10, is 0.10-0.26, loud audio rms ~10000 from sample 0, no caption) before the real start "this is the thing" at 0.26; bad mid-word/mid-thought start.
Largest gap: Clip starts mid-word on prior speech ("...thing is" uncaptioned) about 0.25s before the first captioned sentence.
Fix: Move the start forward to ~0.24s into the current clip (source ~51.71s, about frame 1238/1239, in the gap between "is" and "this"; verify on part_5.wav), shift all captions/pieces by that amount, re-render; frame count/duration stay well inside 60-120s.

## Items
1. Structure: FAIL. Opening clipped as above (render_asr.json words, render audio rms at 0-0.4s). Middle coherent; ending "told us not to talk to each other." resolved, audio tail decays to ~2000 rms after 94.55 and ends 94.95 (source 146.437), natural.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, 2277 frames = expected, video 94.970s, audio 94.97s, no decode errors.
3. Transcript accuracy: PASS. sync.txt match ratio 0.988; displayed English matches HEARD; the one omission ("who you know, I'm saying" at ~79.9-81.3s) is a filler span.
4. Translation fidelity: PASS. Approved rows correctly attached by moment; no clear errors seen (e.g. 0:00:57.5 "Right. Hold on" -> そうだな/待て待て; slave-ship line OK).
5. Masking: PASS. auto.json unmasked_hits empty; no listed words in the English; JP not mechanically masked.
6. Timing/sync: PASS. 28 captions, median onset -0.35s vs ASR (ASR drifts late in the clip, e.g. 76-84s); caption at 79.39 coincides with the resumed speech (energy returns ~79.3); 76.11-79.39 is a meaningful pause on the host/N.O.R.E. shot, not padding. No full sentence uncaptioned except the clipped opening fragment (item 1). Shortest caption 1.2s (0.25-1.45 "This is the thing.") readable.
7. Typography/visuals: PASS. f_0008.22.png / f_0094.89.png: white bold Yu Gothic, black outline+shadow, EN above JP, centred, 2 EN + up to 2 JP lines, inside frame, same size/position as ref_sheet.jpg, readable on bright gold/dark backgrounds.
8. Framing: PASS. sheet_1/2: faces centred in the sharp band 438-1480 with blurred fill; crop changes in manifest pieces coincide with shot changes (Ye, N.O.R.E., host).
9. Source usage: PASS. Single interval part_5 frames [1233,3510), half-open, no repetition/freeze/padding (fix above would move start to ~1238 and stay single-interval).

## Non-blocking notes
- Caption "Right. Hold on. Hold on." is shown over the Ye shot while the ASR hears "right hold up no"; matches approved row, no action.
