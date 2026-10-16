# Final series QA

Checked 2026-10-16T01:16:25Z on the exported files.

- Clips: 21; all frozen PASS by an independent Fresh Clip Critic and byte-identical to the frozen render: PASS
- 9:16 1080x1920 and 60.0 <= duration < 120.0 for every final.mp4: PASS (range 61.770–85.919 s)
- Zero shared source frames/audio across the series: PASS (`source_overlap_audit.md`)
- Unmasked curse words in displayed English: PASS (none)
- Repeated sentences (>=6 words) across clips: none
- Subtitle style identical across clips (ASS Style line): PASS
- Font: Yu Gothic|Bold|200
- Translation: every Japanese line is approved rev 3 text (no new Japanese); per-clip notes list display-English corrections, hand chunking and cuts.
- Shared-folder copy (/mnt/project-files/output/drinkchamps_ye): all 21 final.mp4 have identical audio/video packets to the frozen renders (ffmpeg stream MD5); the shared store rewrites the MP4 container header, so file-level sha256 differs there.
