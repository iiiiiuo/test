VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json 1080x1920, SAR 1:1, video 95.554 s / audio 95.554 s (60 <= d < 120), 2291 frames = expected, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits = []; no curse words in the displayed English (SRT read in full); Japanese not mechanically masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - frames at 5, 9.9, 10.5, 80.39, 93.84 s: white bold Yu Gothic, black outline and shadow, EN above JP, centred, max 2 EN + 2 JP lines (4 lines), same size and position as the series reference, no clipping, readable on the bright yellow background.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
 - Text matches glossary_draft_s2.json verbatim: L001 Sway, L019 Bernard Arnault / ベゾス (two lines), L021 D'Usse (two lines); no word split by the line breaks.
 - Timing: Sway 1.61-10.28 s (8.7 s, starts with the caption that says "Sway"); Bernard Arnault 77.05-83.77 s (6.7 s, starts with the caption that says "Bernard Arnault"); D'Usse 89.74-95.53 s (5.8 s, starts with the caption that says "D'Usse"). All are 2 s or longer.
 - Layout: rows at y=1188 and y=1236, fs40. They sit below the EN/JP block (which ends at about y=1145) with no overlap, inside the sharp band (y 438..1480). Verified in frames 5, 9.9, 80.39 and 93.84 s.
 - Style: ASS Expl is Yu Gothic bold, white fill, black outline 3, shadow 2, the same as Sub. The render shows the same look as the EN/JP rows. It is correctly absent at 10.5 s, after the row ends.

Non-blocking notes
- The Sway row stays up about 4.9 s after its caption (which ends at 5.4 s) gives way to other lines. This is acceptable and was not flagged.
