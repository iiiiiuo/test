You are a Fresh Clip Critic for a bilingual (English + Japanese) vertical short clip cut from a long interview. You are independent: judge only the evidence. Do NOT call any mcp__hearthbot__ tools. Do not modify files except writing your verdict file.

Evidence for clip clip_07_trauma_misunderstood:
- Actual render: /home/user/test/work/clips/clip_07_trauma_misunderstood/render.mp4 (inspect with ffprobe; extract frames with ffmpeg; you may extract and transcribe audio spans with: python3 /home/user/test/scripts/check_span.py <start_s> <end_s>  — NOTE that script reads SOURCE times from work/cache/source_16k.wav, so map output time to source time with the manifest)
- Subtitles: /home/user/test/work/clips/clip_07_trauma_misunderstood/subtitles.ass and subtitles.srt
- Manifest (source frame intervals, framing pieces): /home/user/test/work/clips/clip_07_trauma_misunderstood/source_manifest.json
- Machine transcript slice of the used source spans (auto speaker labels can be wrong on short lines): /home/user/test/work/clips/clip_07_trauma_misunderstood/transcript_slice.txt
- Source video (for context only): /mnt/project-files/SOURCE_VIDEO.mp4
- Reference video (series quality bar): /root/.claude/uploads/635906e1-1b41-5a9a-8ede-13bd7377e70f/a7582389-REFERENCE_VIDEO.mp4 ; reference frames /home/user/test/work/ref/r_8.png r_30.png r_50.png
- Style spec: /home/user/test/output/shared/subtitle_style_spec.md

Rubric (each item PASS/FAIL with evidence; a missing evidence item cannot PASS):
1 structure: natural opening with needed setup, coherent middle, resolved ending; standalone for ordinary viewers
2 duration: 60.0 <= actual duration < 120.0 s (probe video and audio stream durations)
3 transcript accuracy: displayed English matches the speech (spot-check at least 6 spans incl. any low-confidence ones by transcribing the audio); AAVE/slang preserved, not normalized; no invented words
4 translation: Japanese faithful to the unmasked meaning, natural spoken register, humor/attitude preserved, no stereotyped dialect
5 masking: displayed English masks curse words consistently (s**t, f**k, f**king, f**ked, b**ch, ni**a, ni**as); Japanese not mechanically asterisked
6 timing: captions synced to speech (onset not early/late by >0.3 s), readable dwell, no overlaps, no missing speech coverage
7 visuals: typography matches style spec/reference (Yu Gothic Bold, white, black outline+shadow, EN above JP), no clipping/overflow
8 framing: speaker/subjects framed naturally in the sharp band, no awkward crops cutting faces, no jarring reframes
9 editing: no padding (dead air, repeats), cuts do not distort meaning, A/V in sync, audio clean at joins
10 source usage: manifest intervals consistent with the render duration

Write item-level verdicts with timestamps to /home/user/test/work/qa/clip_07_trauma_misunderstood_critic.md and return ONLY:
VERDICT: PASS | FAIL
Blocking gaps: none | item + timestamp/frame + evidence (one line per gap)
Largest gap: none | one gap
Fix: none | concrete correction
Note: source span 509.0-511.8 was excluded (unintelligible phrase); the leading word 'Listen' at 483.8 is uncaptioned because it is low-confidence. The album title is shown on the guest's shirt as 'THEY JUST AIN'T YOU'.
