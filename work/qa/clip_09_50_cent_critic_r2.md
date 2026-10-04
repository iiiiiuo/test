# clip_09_50_cent — Fresh Clip Critic, round 2 (scoped re-check)

Artifact hashes (sha256):
- render.mp4 86de8d7d97c8ad8b90bc4dae7b82f9fb8a379bcf7d4dbee6124afd54a0830bdb
- subtitles.ass e0865630f622349a29f0fff4618843f6346d6b56d5788ceb40142b3ca96b4596
- subtitles.srt c9171dc0eb4af4184a6dda5279c51864ef30b2c4037a4ef867a3a5dde39f68d3
- source_manifest.json b7a6c05ceba30a1aa185e28365ac8b0212c521eb100435ff868a90f4617df4e1

Scope: items 2, 3, 6, 9, 10 at the changed joins/captions. Items 1, 4, 5, 7, 8 carried forward from round 1 (PASS), not re-evaluated.

Method: render audio decoded to 16 kHz mono; faster-whisper large-v3 on isolated render spans; source spans via scripts/check_span.py (large-v3 and medium.en); RMS envelopes (20-40 ms windows) at each join.
Output->source map: seg1 0-26.360; seg2 26.360-30.497; seg3 30.497-67.170 (src 682.582+); seg4 67.170-68.872 (src 722.255+); seg5 68.872-71.875 (src 725.124+); seg6 71.875-74.144 (src 728.761+); seg7 74.144-77.377.

## 2 duration — PASS
ffprobe: video 77.377300 s (2319 frames @30000/1001), audio 77.377007 s, format 77.377300 s. 60 <= 77.377 < 120.

## 10 source usage — PASS
Manifest segment frame counts 790+124+1099+51+90+68+97 = 2319 = edited_duration_frames = probed nb_frames; 2319*1001/30000 = 77.3773 s. Segments are disjoint, half-open, and ascending. Pieces tile each segment exactly. Audio sample ranges agree with the video segments to within about 20 samples (44.1 kHz).

## 3 transcript accuracy — FAIL
- 30.497 (seg3 start, src 682.58): the isolated render span 30.497-31.6 reads "But in reality." (0.70/0.91/1.00) with no clipped earlier word. Caption 17 is correct. OK.
- 67.17-68.87 (seg4, caption 36): render reads "For me, a lot of shit he do, I would not." The isolated 68.2-68.872 span ends on "not." and has no "do". Source context (720.5-724.3) confirms "For me," not a "You feel me" tail. "For me, a lot of s**t he do, I would not..." is accurate. OK.
- 71.404 (caption 38 "Yeah."): "Yeah" is heard at 71.30-71.6. BUT a word fragment is still audible after it. See item 9: an isolated 71.6-72.3 span is transcribed as "Hey." and 71.875-74.0 begins with "It@71.88". The source has "Yeah, for me" at 727.40-728.64 and "Hey, Femi" at 728.0-729.0, so part of the dropped unresolvable words is still in the render around the join. "Yeah." does not cover them. FAIL (blocking).
- 68.944 (caption 37 "Like you said, he too old for the trolling that he does."): the first words are disputed. The machine transcript has "Like" (low-confidence). Render large-v3 hears "Now you say" (0.29/0.78/0.36). Source large-v3 (725.0-727.0) hears "Now you say" (0.45/0.78/0.73), and medium.en hears "Now(0.13) you say". No model hears "said". The displayed "Like you said" is unresolved uncertain speech, and the JP 言ってた通り depends on it. FAIL (blocking).
- 72.49 (caption 39 "He got me in 25 years."): models hear "on" (0.69, 0.75, 0.76) more often than "in" (0.58 once). The machine transcript has "on" (low-confidence). Minor: prefer "on" (idiomatic "got 25 years on me"). Non-blocking, but cheap to fix.
- 74.14-77.38 (caption 40): matches "I feel like he didn't (even) come down to this level and troll me right now". OK.
- 0-5, 13.5-19, 25.5-30.5 spot-checks: consistent with captions 1-3, 8-10, 14-16. OK.

## 6 timing — FAIL (minor)
- No overlaps; all dwells >= 0.8 s.
- Caption 17 onset 30.497 vs speech 30.50: OK. Caption 36 onset 67.272 vs speech about 67.26: OK. Caption 38 onset 71.404 vs "Yeah" about 71.30-71.40: OK.
- Caption 39 onset 72.490, but render audio is silent (-53 to -57 dBFS) from 72.10 to 72.79. Speech starts at about 72.80 (-48 -> -38 dB at 72.79-72.82). The caption is 0.31 s early, over the 0.3 s limit. Fix: start it at about 72.78.

## 9 editing — FAIL
- Join 67.170 (seg3->seg4): the cut falls in a -56 dB gap. Clean.
- Join 68.872 (seg4->seg5): "not." ends, the level falls to -47 dB at 68.86, then about 0.3 s of near-silence. No word is heard by isolated transcription. Acceptable.
- Join 30.497 (seg2->seg3): voiced on both sides (-15 dB at 30.48 | -19 at 30.50), but it reads as a natural flow into "But in reality". Acceptable.
- Join 71.875 (seg5->seg6): BLOCKING. Voiced energy is continuous across the cut: -18 to -14 dB at 71.72-71.84, then -20 to -18 dB at 71.88-72.00, decaying to -39 dB only at 72.10. That is a truncated syllable on each side of the splice: about 0.15 s from src 727.97-728.127 and about 0.2 s from src 728.761-728.96. Isolated transcription hears "Hey."/"It". Unresolvable speech is left in, and the join is audibly chopped.

## Carried forward (round 1 PASS, unchanged scope)
1 structure, 4 translation, 5 masking, 7 visuals, 8 framing: PASS (not re-evaluated). Item 4 depends on the caption 37 wording: if caption 37 changes, re-check its JP.

## Verdict
VERDICT: FAIL
Blocking gaps:
- 9/3 join 71.875 (src 727.97-728.13 | 728.76-728.96): speech fragments remain on both sides of the cut (RMS -14..-20 dB continuous; isolated ASR "Hey."/"It"), not covered by "Yeah."
- 3 caption 37 @68.944: "Like you said" is unresolved. ASR on render and source gives "Now you say" (3 runs). No model hears "said".
- 6 caption 39 @72.490: speech onset about 72.80 (silence -54 dB until 72.79), so the caption is 0.31 s early.
Largest gap: the 71.875 splice leaves truncated unresolvable syllables.
Fix: End seg5 at about frame 21817 (src 727.97, right after "Yeah") and start seg6 at about frame 21848 (src 728.99, after the fragment decays). Confirm both edges are at <= -40 dB. For caption 37, start seg5 at "he" (about src 725.63, frame about 21747) and change the caption to "He too old for the trolling that he does." with JP あの歳であの煽りはないって, or resolve the first words by local listening. Retime caption 39 to start at the real speech onset (output about src 729.69), and change "in" to "on". Then re-render and re-check items 2, 3, 4 (caption 37), 6, 9 and 10.
