VERDICT: FAIL
Blocking gaps: Item 4/6 caption 6 at 19.15-20.09s ("Yeah.") shows JP "俺はあんたが好きだ" (the translation of "I f**k with you", said at 21.58s), then the same JP repeats on caption 7 at 21.58-23.63s; JP is attached to the wrong moment (subtitles.srt cue 6 vs 7; approved row L004 "Yeah. So, I fuck with you. I love you." split without separating its JP).
Blocking gaps: Item 6 65.95-68.15s: about 2.2s of loud foreground speech ("on a, you know, on a ...") has no caption (render_asr segment 58.98-70.02 continuous; volumedetect -11 to -15 dB at 66-68s); caption 21 (JP 黒人の第一号なんだよ) ends at 65.95 and caption 22 starts at 68.15.
Largest gap: Caption 6 "Yeah." carries the JP of the later line "I f**k with you" and duplicates it on the next caption.
Fix: Give caption 6 ("Yeah.") its own JP (e.g. そう) or merge it into caption 7 so the JP appears once at 21.58s; extend caption 21 (or the start of 22) to cover 65.95-68.15s so the speech is captioned.

## Items
1. Structure: PASS. Opens "this real shit..." at a thought start (source 1651.44 host speech, cut 1652.11); ends "We love you. We're ruling the world right now." resolved, source_context shows next line outside the clip; standalone understandable.
2. Duration/format: PASS. auto.json 1080x1920, SAR 1:1, video 85.127s, audio 85.127s, frames 2041 = expected, no decode errors.
3. Transcript accuracy: PASS. HEARD vs displayed matches except trivial words (HEARD "who" vs "what was your plight" at 10.5s; "I can see you" vs "I consider you" at 26.5s; ASR error, source context heard differently and approved text stands).
4. Translation fidelity: FAIL. See caption 6 above. Otherwise JP matches English; JP of captions 19-21 runs ahead of the EN split (e.g. "HaroとかGTのBMXに乗る" shown with "dude wearing a Harley-Davidson hat") but the sentence is conveyed overall.
5. Masking: PASS. auto.json unmasked_hits empty; s**t, f**k, ni**a masked in EN only; JP unmasked.
6. Timing/sync: FAIL. See 65.95-68.15s gap. Otherwise onset median -0.012s, 95.8% matched words inside their caption. Caption 4/5/6 (17.03-20.09) are short (caption 6 ~0.94s, "Yeah." short word, acceptable).
7. Typography/visuals: PASS. sheet_1/2: white bold Yu Gothic-style, black outline/shadow, EN above JP, centred, max 2 EN + 2 JP lines, same size/position as ref_sheet, no overflow. Lines at 4 total lines is allowed.
8. Framing: PASS. Faces centred in the sharp band with blurred fill; Ye (1:00-1:25) and host framing natural; changes occur at shot changes.
9. Source usage: PASS. Single interval part_5 frames [39610,41651) half-open, 2041 frames = render frame count; no padding or repetition (the repeated "Pharrell" is real spoken repetition).

## Non-blocking notes
- Captions 4 to 6 are back-to-back (20ms gaps), reading fast at 17.0-20.1s.
- JP in captions 19-21 is split ahead of the EN wording; consider re-splitting so JP phrases align with their EN.
