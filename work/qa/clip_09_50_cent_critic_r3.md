# clip_09_50_cent — Fresh Clip Critic, round 3 (scoped re-check)

Artifact: work/clips/clip_09_50_cent/render.mp4 (2265 frames). Scope: items 2,3,6,9 at seg5/seg6 joins and changed captions; item 4 for changed caption; item 10.
Output mapping: seg4 67.167-68.869 | seg5 68.869-70.604 (src 725.758-727.493) | seg6 70.604-72.339 (src 729.295-731.030) | seg7 72.339-75.576.

VERDICT: FAIL

| # | Item | Verdict | Evidence |
|---|------|---------|----------|
| 2 | duration | PASS | ffprobe: video 75.575500 s (2265 frames @30000/1001), audio 75.575011 s; 60.0 <= 75.58 < 120.0 |
| 3 | transcript (changed captions) | FAIL | 68.89 "He too old for the trolling that he does." — render ASR (large-v3, render audio) hears "that he do." (p 0.72 / 0.42 in two passes). Source ASR: 726.40-727.46/727.50 window -> "that he did." (0.71); window extended to 727.58 -> "that he does." (0.99). The final /z/ of "does" lies after the seg5 cut (727.493), so the displayed word is not what the render audio contains. 71.03 "He got me on 25 years." matches render ASR ("He got me on 25 years", 70.80-71.72). |
| 4 | translation (changed caption) | PASS | あの歳であの煽りはないって = "at that age, that trolling is not OK" — faithful to "he too old for the trolling", natural spoken register, dismissive attitude kept. |
| 6 | timing | PASS | Cap 37 onset 68.89 vs speech onset 68.90 (RMS -44 -> -26 dB at 68.88-68.90); ends 71.009, no overlap with cap 38 (71.029). Cap 38 onset 71.03 vs RMS onset 71.00-71.04 (-55 -> -34 dB). Cap 39 onset 72.37 vs speech onset 72.66 (RMS -54 -> -25 dB) = 0.29 s early, inside the 0.3 s tolerance (borderline, unchanged caption). |
| 9 | editing / joins | FAIL | Join 70.604 (seg5 end, src 727.493): render RMS stays at speech level -25..-29 dB through 70.58 then drops to -45/-57 dB at 70.60 — a hard cut inside speech, not at a silence minimum (source floor ~-55 dB; src 727.50 is only a local -29 dB dip between -20 dB neighbours). Truncates the end of "does" (see item 3). Join 68.869 (seg4 end/seg5 start): RMS -23 -> -44 (20 ms) -> -20 dB, no sample discontinuity (max diff 0.0003), ASR "I would not. / He too old..." clean. Join 72.339: seg6 speech ends ~72.32, cut lands at -50 dB, clean. Pauses 70.60-71.00 (0.40 s) and 72.34-72.66 (0.32 s) are not padding. |
| 10 | source usage | PASS | 7 video segments sum 2265 frames = rendered nb_frames; audio sample ranges match each video interval to <0.5 sample and equal duration (<2e-5 s); pieces disjoint and sum 2265; no segment touches the excluded spans listed. |

Carried forward from earlier rounds (not re-checked): items 1,5,7,8 PASS; joins at seg3 start and seg4 PASS.

Note (non-blocking): src 725.20-725.74 "Like you said," is excluded, so "He too old..." is presented as the guest's own statement instead of agreement with the host; the guest does endorse it, so meaning is not distorted.

## Largest gap
Seg5 end cut at src 727.493 truncates "does" (render audio reads "do"/"did") while the caption shows "does"; audio hard-cut at speech level.

## Fix
Move seg5 end_frame_excl from 21803 later, to the real end of "does" (it ends after src 727.50; try 21805-21806 = src 727.56-727.59). Confirm with ASR of the rendered span that it reads "does" and has no "Yeah" fragment, and add a 10-20 ms audio fade-out at the join. If the /z/ cannot be kept without pulling in the next utterance, choose a different boundary or drop seg5. Then re-check items 3, 6, 9 and 10.
