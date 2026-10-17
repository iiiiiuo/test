VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 5, 7, 10; item 4 CHANGED_LINES=none; 1,3,4,6,8,9 NOT IN SCOPE, no blocking problem noticed)
2. PASS - auto.json: 1080x1920, SAR 1:1, video 65.5238 s / audio 65.524 s, frames 1571 = expected, decode_errors empty.
5. PASS - ASS/SRT contain only f**k, b**ch, ni**as, f**king; no unmasked hits (auto.json unmasked_hits empty); JP rows not masked.
7. PASS - frames f_0002.89, f_0013.30, f_0063.65: white bold Yu Gothic, black outline+shadow, EN above JP, centred, max 2 EN + 2 JP lines, inside sharp band, matches ref_20.png layout.
10. PASS - three rows, text matches glossary_draft_s1.json verbatim (L002 Roscoe's, L003 Usher, L012 40エーカー). Spans: Roscoe's 1.37-8.17 s (frame 2.89 inspected), Usher 10.46-16.53 s (frame 13.30 inspected; also f_15.01), 40エーカー 61.80-65.52 s (frame 63.65 inspected; also 64.52, 65.44). Each starts with the caption showing the term, 3.7-6.8 s long. Expl rows at y 1188/1236 (ink ~1190-1265), below the EN/JP block (ends ~1150), inside y 438..1480. Same font, white, black outline, shadow. Line breaks fall after 、/』 so no word or name is split.

Non-blocking notes
- Usher row second line begins with the particle は (break after 』); acceptable.
