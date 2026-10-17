VERDICT: PASS
Blocking gaps: none
Largest gap: none (non-blocking: Dave Chappelle explanation starts 13.42 s, 1.26 s after the caption naming him at 12.16 s)
Fix: none

Items
1. Structure: NOT IN SCOPE
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 67.943 s / audio 67.943 s, 1629 frames = expected 1629, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity (CHANGED_LINES = none): NOT IN SCOPE
5. Masking: PASS. auto.json unmasked_hits = []; no listed word appears in the ASS EN text; JP and Expl rows contain no asterisks.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS. f_0007.01, f_0012.18, extra/e_15, extra/e_43.5: Yu Gothic Bold white, black outline and shadow, EN above JP, centred, EN 54 / JP 50, max 2 EN + 2 JP lines, nothing clipped, readable on the bright background; matches the style spec.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS.
 - Text matches glossary_draft_s1.json verbatim for L001, L002, L003 and L007 (ASS rows are the same strings; line breaks differ only).
 - Timing: L001 3.92-9.40 (5.5 s, starts on the caption showing Larry Hoover); L002 9.42-13.40 (4.0 s, starts on "concert together"); L003 13.42-16.80 (3.4 s); L007 42.40-48.47 (6.1 s, starts with the caption that says the address).
 - No overlap with EN/JP rows: Expl y 1120-1263, in the sharp band (438-1480). EN/JP block ends at about 1148 on 4-line captions, and the Expl row was moved to 1170 for those. Frames at 7.01, 12.18, 15, 43.5 show a clear gap.
 - Same font, white fill, outline and shadow (Expl style). Widest line spans x 150-930 inside the frame. No break splits a word or name (L001 breaks after "シカゴの", which is acceptable).

Non-blocking notes
- The L003 explanation (Dave Chappelle) starts at 13.42, while its caption starts at 12.16 and the name is spoken there. L002's row stays up until 13.40 and the two cannot share the space. It is still on screen for 3.4 s.
- At 9.42-12.14 and 12.16-13.40 the Expl row sits at y 1170 or 1218, lower than the 1120 used for L001; this is consistent with 4-line captions and does not collide.
