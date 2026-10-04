# clip_08_safe_alone — Fresh Critic r3 (scoped re-check: items 3,4,6 for captions 1-4; items 2,10)
VERDICT: PASS
- 2 duration PASS: ffprobe video 75.5755 s, audio 75.5750 s (60<=d<120).
- 10 source usage PASS: manifest single segment frames [17194,19459) = 2265 frames * 1001/30000 = 75.5755 s = render duration.
- 3 transcript PASS: local large-v3 re-transcription of 573.7-582.2 and isolated windows. Cap1 "You just said that you spent a lot of time alone." matches; machine-slice "right?" not supported (575.5-576.5 window gives only "...time alone."; 576.15-576.5 near-silent). Cap2 "Yeah. And sometimes you got to do that": isolated burst 576.78-577.16 -> "Yeah." (p=0.76), 576.78-578.4 -> "Yeah, and sometimes you got to do that"; supported. Cap3 "even with the people you come from." 578.34-580.60 matches. Cap4 "Because I feel safe alone." 580.64-581.68 matches.
- 4 translation PASS: cap1-4 JP faithful, natural spoken register; "do that ... even with the people you come from" rendered as 時には地元の仲間とでも/距離を置かなきゃいけないこともある (meaning-faithful; JP word order spans cap2-3 acceptably).
- 6 timing PASS: speech onset after silence 576.45-576.82 is at ~576.85 (RMS); cap2 onset 576.81 (out 3.104). Cap1 573.88 vs speech ~573.75; cap2 end 578.32 vs "that" 578.34; cap3 578.34-580.64 vs speech 578.34-580.60; cap4 580.66-582.02 vs 580.64-581.68. No overlaps (gaps 0.02-0.19 s); dwell >=1.36 s.
Other items carried forward from prior PASS.
