VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items
1. NOT IN SCOPE
2. PASS - auto.json: 1080x1920, SAR 1:1, video 67.942875 s / audio 67.943 s (60 <= d < 120), 1629 frames = expected, decode_errors empty.
3. NOT IN SCOPE
4. PASS (no CHANGED_LINES supplied; nothing to judge)
5. PASS - auto.json unmasked_hits = []; SRT/ASS contain no profanity needing masks, no asterisks in JP; spot-checked the HEARD text, no listed curse word spoken.
6. NOT IN SCOPE
7. PASS - frames f_0004.88, f_0007.01, f_0014.32 vs ref_35: white bold Yu Gothic (style Sub, 54/50 px), black outline + shadow, EN above JP, centred, same vertical start (~y 950) as reference, max 2 EN + 2 JP lines, no clipping, readable on bright yellow/white background.
8. NOT IN SCOPE
9. NOT IN SCOPE
10. PASS - Texts match glossary_draft_s1.json verbatim for L001 (Larry Hoover), L002 (一緒にライブ), L003 (Dave Chappelle), L007 (住所をバラした); line breaks only after a term label or at a phrase boundary, no word/name split. Timing (ASS): 3.92-9.40 (5.5 s), 9.42-13.40 (4.0 s), 13.42-16.80 (3.4 s), 42.40-48.47 (6.1 s); each starts at the caption showing the term and is >= 2 s. Placement: Expl rows sit 90 px below the last EN/JP row baseline (y 1138 for 3-line blocks, 1188 for 4-line blocks, second line +48 up to y 1236), no overlap with Sub rows (computed per overlapping event); all within sharp band y 438..1480; widest row ~150..930 px, inside frame. Frames f_0004.88/0007.01/0014.32 confirm: Yu Gothic Bold 40 px, white fill, black outline + shadow, same as Sub.

Non-blocking notes
- Expl row sits fairly far below the 3-line caption block in the 3.92-9.40 span (it does not move when the block grows at 6.86 because 3 lines end at y 1048; fine).
- Frame for the 42.40-48.47 term not among the supplied f_*.png; judged from ASS geometry (same style/positions as the verified rows).

Addendum (render frame extra/f_0045.00.png, 45.00 s)
- Item 10 for the L007 row confirmed from the actual render: text "住所をバラした：確執中にYeがDrakeの住所を / Instagramに載せた騒動" matches the draft; sits at y ~1190-1255 below the 4-line EN+JP block (ends ~1140) with clear gap, no overlap; inside sharp band (438..1480) and frame width (~210..870); smaller white bold Yu Gothic with black outline/shadow as the other rows; no word split. Verdict unchanged: PASS.
