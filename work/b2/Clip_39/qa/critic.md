VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 5, 7, 10; item 4 none changed)
1. NOT IN SCOPE
2. PASS - auto.json: 1080x1920, SAR 1:1, video 77.619 s / audio 77.619 s (60<=d<120), 1861 frames = expected, no decode errors.
3. NOT IN SCOPE
4. NOT IN SCOPE (CHANGED_LINES = none)
5. PASS - auto.json unmasked_hits empty; no curse words in displayed EN (captions.json read in full); JP not masked.
6. NOT IN SCOPE
7. PASS - frames at 13.5 s and 60.5 s (qa/extra/x_*.png): white bold Yu Gothic, black outline/shadow, EN above JP, centred, max 2 EN + 2 JP lines, inside frame, same layout as the reference.
8. NOT IN SCOPE
9. NOT IN SCOPE
10. PASS
 - L003 text and L009 text in ASS match glossary_draft_s2.json verbatim. Terms are on separate lines, with no mid-word breaks.
 - L003 row: 8.96-17.89 s (8.9 s); starts with the caption "Quincy Jones beneath...". L009 row: 56.67-65.18 s (8.5 s); matches the line's caption span.
 - Rows are at y 1188-1284 (fs40, style Expl, Yu Gothic bold, white, black outline/shadow). The last EN/JP line is at y 1098, so there is a visible gap and no overlap. Rows are inside the sharp band (438..1480). The widest line (L009 row 2) spans x~165-915, within 1080.

Non-blocking notes
- The L003 row stays up to 17.89 s, about 1.6 s into the L004 caption (the L003 speech ends ~15.9 s). Harmless, and it leaves reading time.
