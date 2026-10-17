VERDICT: FAIL
Blocking gaps: item 10 | 60.23 s (ASS line 83-84) | the "40エーカー" explanation appears at 60.23 s during the earlier caption "God has a place for us in a promised land..." (57.19-61.78 s). The caption that shows "40 acres" starts at 61.80 s (qa/sync.txt line 41), so the explanation is up about 1.6 s before the term is on screen.
Largest gap: Item 10: the 40エーカー explanation starts 1.57 s before the caption that shows the term.
Fix: Start both Expl events for Clip_12_L012 at 0:01:01.80 and end them at 1:05.52. That leaves 3.7 s on screen. Roscoe's (1.37) and Usher (10.46) already start with their captions.

Items
1. NOT IN SCOPE
2. PASS: auto.json 1080x1920, SAR 1:1, video 65.5238 s, audio 65.524 s, frames 1571 = expected 1571, decode_errors empty.
3. NOT IN SCOPE
4. NOT IN SCOPE (CHANGED_LINES = none)
5. PASS: auto.json unmasked_hits is empty. The ASS shows ni**as, f**k, b**ch and f**king, and no unmasked profanity. The Japanese lines are not masked mechanically.
6. NOT IN SCOPE
7. PASS: frames f_0013.30 and f_0059.49 and sheet_2 show white bold Yu Gothic with black outline and shadow. EN is above JP, centred, with at most 2 EN + 2 JP lines. Nothing is clipped, and the style matches the earlier render.
8. NOT IN SCOPE
9. NOT IN SCOPE
10. FAIL, on timing only.
 - Text: all three rows match glossary_draft_s1.json (L002 Roscoe's, L003 Usher, L012 40エーカー). Line breaks are only after the "：" or between words, so no word or name is split.
 - Style and position: the Expl style is Yu Gothic, size 40, white, black outline and shadow. It sits at y=1188 and 1236, below the 4-line EN/JP block (ends about y 1150), with no overlap and inside the sharp band (438..1480). Seen in f_0013.30 and sheet_2.
 - Timing: Roscoe's 1.37-8.17 s and Usher 10.46-16.53 s start with the caption that shows the term and are long enough to read. 40エーカー runs 60.23-65.52 s (5.3 s, long enough to read) but starts early, as described under Blocking gaps.

Non-blocking notes
- The 40エーカー start looks like it was pulled earlier to keep a minimum on-screen time at the end of the clip. 3.7 s from 61.80 s is still enough to read.
- The ASR heard "400 acres" at 61.8 s. This is not in scope for this round.
