# clip_09_50_cent — Fresh Clip Critic round 4 (scoped re-check)

Artifacts: render.mp4 (2213 frames), subtitles.ass/.srt, source_manifest.json (6 segments).
Scope: items 1, 2, 3/6/9 at the seg4->seg5 join (render 68.869 s; src 723.957 -> 729.295), 10. Items 4,5,7,8 and the joins at src 682.58 / 722.26 carried forward PASS from earlier rounds (unchanged).

| # | Item | Verdict | Evidence |
|---|------|---------|----------|
| 1 | structure | PASS | Dropped src 725.20-728.64 = host question "Now you saying he too old for the trolling that he does?" + guest "Yeah. You feel me?" (check_span 723.9-729.5). Without it the guest's run reads "For me, a lot of s**t he do, I would not... / He got me on 25 years. / I feel like he didn't even come down to this level and troll me right now." The age gap still comes from the guest himself, the logic still holds, and the meaning is not distorted. The ending still resolves on the troll line. |
| 2 | duration | PASS | ffprobe: video 73.840433 s (2213 frames @30000/1001), audio 73.840000 s, format 73.840433 s. Within [60,120). |
| 3 | transcript (join) | PASS | Render ASR 65.5-73.84: "...be doing. You know what I'm trying to say? For me, a lot of shit he do, I would not. He got me in 25 years. I feel like he didn't even come down to this level and troll me right now." Source check_span 729.0-731.2: "got me on 25 years" (on 0.82), so the caption "on" is accepted. Seg4 source ASR 722.25-723.85 ends "I would not." The following "do" (src 724.02) is excluded, and the caption's "would not..." shows the trail-off honestly. Captions 35-38 match. Nothing is invented and the AAVE ("he do") is kept. |
| 6 | timing (join) | PASS | Render RMS: seg4 speech ends 68.84, then near-silence (34-38 dB) 68.87-69.26. "He" onset is about 69.27-69.30, against caption 37 at 69.29 (within 0.03 s). Caption 36 runs 67.27-69.27 (speech 67.28-68.84). Caption 38 starts at 70.64, the same as speech at 70.64. Every caption has a 0.02 s gap, so there are no overlaps, and no speech is left uncaptioned. |
| 9 | editing (join) | PASS | The src cut at 723.96 falls in an inter-word dip (57 dB, against about 70 dB speech) between "not" and "do". The render falls smoothly from 65 to 46 to 34 dB at 68.86-68.88, with no click or fragment of "do" audible to ASR. The silent gap before "He" is about 0.4 s, which is a natural beat and not padding. Frames at 68.80 (host-reaction H piece), 68.92 and 69.50 (guest G) show a clean cut with A/V in sync (mouth open on "He got me" at 69.5). |
| 10 | source usage | PASS | Segment frames 790+124+1099+51+52+97 = 2213, which equals the render nb_frames and edited_duration_frames. Audio segs 4/5: 75045 and 76516 samples @44.1k = 1.7017 s and 1.7351 s, matching 51 and 52 frames. Intervals are half-open and disjoint, and 725.74-727.50 is no longer used. |
| 4,5,7,8 | carried | PASS (prior rounds) | Caption 36/37 wording is unchanged from what was previously reviewed; the masking in "s**t" is consistent and the Japanese is unasterisked. |

VERDICT: PASS
