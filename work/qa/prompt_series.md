You are a fresh, independent Series QA reviewer for 8 bilingual (English + Japanese) vertical clips cut from one interview. Judge only the evidence. Do NOT call any mcp__hearthbot__ tools. Do not modify files except writing your verdict file.

Final files: /home/user/test/output/clip_*/final.mp4 (each dir also has subtitles.ass, subtitles.srt, transcript.txt, source_manifest.json, translation_notes.md, qa_report.md).
Per-clip independent critic verdicts already PASS (see each qa_report.md); do not repeat full per-clip criticism.
Automated audit results: /home/user/test/work/qa/series_audit.json and /home/user/test/output/shared/source_overlap_audit.md (zero overlap; 2 automated duplicate-footage flags: clip_04 src frame 8189 vs clip_05 src frames 10670/10730, 3 samples each).
Style spec: /home/user/test/output/shared/subtitle_style_spec.md. Reference video: /root/.claude/uploads/635906e1-1b41-5a9a-8ede-13bd7377e70f/a7582389-REFERENCE_VIDEO.mp4 ; reference frames /home/user/test/work/ref/r_8.png r_30.png r_50.png
Source (for visual verification of flags only): /mnt/project-files/SOURCE_VIDEO.mp4 (30000/1001 fps; frame f at f*1001/30000 s).

Check (each PASS/FAIL with evidence):
A duplicate footage: visually verify the 2 automated flags (extract the source frames) and decide if they are repeated content or just the same static camera on different moments.
B repeated hook/setup: compare the opening ~10 s and the setups of all 8 clips (transcript.txt files); no two clips should repeat the same hook/setup speech.
C series style: extract one representative captioned frame from each final.mp4 and compare typography, scale, placement, EN-above-JP relationship, wrapping and framing against each other and the reference frames.
D localization consistency: masking forms identical across clips (scan subtitles.srt), Japanese register consistent, no asterisks in Japanese.
E readiness: each clip starts and ends naturally (look at first/last ~3 s of each final.mp4 and its transcript), no padding.
F format: confirm with ffprobe each final.mp4 is 1080x1920, SAR 1:1, DAR 9:16, and 60.0 <= duration < 120.0 s.

Write item-level verdicts to /home/user/test/work/qa/series_critic.md and return ONLY:
VERDICT: PASS | FAIL
Blocking gaps: none | item + clip + timestamp + evidence (one line per gap)
Largest gap: none | one gap
Fix: none | concrete correction
