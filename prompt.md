# Production objective and execution

Execute this local video project to completion under `CLAUDE.md`. Produce as many **clear, coherent, standalone-enough, postable** non-overlapping vertical clips as the source supports. For 20–40 minute material, actively seek multiple clips across the entire source; completing Clip 01 never ends discovery.

Strongly prefer **61–75 seconds**, close to one minute when natural. The hard duration gate is defined in `CLAUDE.md`; 60–61 seconds is valid, 75–90 is acceptable, and 90–<120 needs a brief content-based reason. Do not sacrifice meaning for a preferred duration or demand an exceptional viral moment from every candidate.

## 1. Inspect and initialize

1. Read `CLAUDE.md`, this file, necessary existing `.claude/skills/`, input inventory, and existing `work/state.json`. Migrate legacy state if needed. Do not create unnecessary agent/skill scaffolding.
2. Identify actual paths for SOURCE_INTERVIEW/SOURCE_VIDEO, REFERENCE_VIDEO, supporting images, and font resources. Check local media probing, transcription/alignment, subtitle rendering, encoding, and image/audio inspection capabilities (e.g. FFmpeg/ffprobe, Python/OpenCV, locally available Whisper tools).
3. Record measured duration, resolution, FPS, timebase/PTS, frame count, audio, rotation, input hashes, and tools. Map aliases/transcodes to canonical source/frame provenance. Missing essentials block the affected stage; continue independent work.

## 2. Analyze globally once

4. Reuse a valid full-source transcript or extract audio and transcribe/align the complete source once, including speakers and uncertainty flags. Save `work/transcript.json` with timestamps and `work/semantic_map.json` for questions/answers, topics, stories, opinions, exchanges, setup, reactions, and endpoints.
5. Cover the entire measured timeline, including non-speech/unusable sections; repair uncertainty locally. Global analysis/planning must precede Clip 01.

## 3. Discover broadly and select a disjoint set

6. Generate all credible candidates from the semantic map, not fixed time slices. Candidate ranges may overlap or initially fall outside final duration limits. Keep `work/clip_candidates.json` and export a compact `output/shared/clip_candidate_map.md` table:

```text
ID | source intervals | estimated edited duration | topic
opening/setup + ending | standalone/dependency | confidence risk
quality HIGH/MEDIUM/LOW | edit/framing issue | overlap conflicts
status proposed/reserved/frozen/rejected | brief decision reason
```

7. Adjust boundaries naturally: extend short candidates (e.g. 45–59 seconds) with available same-topic context; split >=120-second topics only into independently coherent semantic units. Trim filler without distorting meaning; reject invalid constructions with a brief reason.
8. Require a natural opening, coherent middle, and resolved ending understandable to ordinary viewers. Include necessary question/setup; inferable pronouns and missing nonessential background are not automatic failures.
9. Select globally among candidates meeting the quality floor and hard constraints. Prefer more usable independent clips, then stronger content and natural preferred durations. Compare conflicting alternatives: a long candidate should not consume material for two good short clips without a substantive reason. Do not use an arbitrary clip cap or a score that can trade away hard constraints.
10. Resolve all overlaps and reserve the selected set in the ledger. Use exact source-frame lists/intervals for edits and handles; validate pairwise disjointness programmatically before final renders and after every reservation change. Do not silently steal a frozen clip's material.

## 4. Calibrate the global style once

11. Inspect representative reference frames and short reference audio/video passages. Choose a 10–20 second source test covering short/long EN+JP captions, kanji/kana, wrapping, and slang/masking where available. Preview material may reuse a candidate interval during testing; previews are not final clips.
12. Render the test and compare actual frames with reference evidence. Measure glyph height/bounding boxes, font identity/weight, colors, outline thickness, shadow X/Y/blur/opacity, EN/JP center/baselines, spacing, bottom margin, alignment, width/wrapping, line spacing, caption duration/segmentation, and onset/offset behavior. Compare normalized geometry if resolutions differ.
13. Obtain fresh calibration PASS and save `output/shared/subtitle_style_spec.md`: font path/hash, renderer, canvas, measurements/tolerances, reference/test frames, and QA evidence. Diagnose wrong variants, fallback, scaling, DPI, renderer/libass, and resize pipeline before compensating for wrong glyphs with font-size changes. Freeze the template.

## 5. Build, render, critique, freeze

14. For each reservation, verify boundaries against source audio/transcript; resolve uncertainty; write accurate English, natural Japanese, and terse translation notes only for consequential choices. Apply reference-derived English masking. Author synchronized phrase-level EN/JP captions with readable dwell, natural breaks, and reference-consistent timing.
15. Create 9:16 framing and reference-supported edits. Keep a `source_manifest.json` mapping every output segment/layer to canonical source frame/PTS intervals, including audio, transitions, hooks/setup, and any auxiliary footage. No hidden reused source segments.
16. Render in `work/`. Check the actual video, audio, subtitles, and decode result. Inspect normal playback for timing/coherence and actual frames at openings/endings, longest captions, wraps, bright/dark backgrounds, and framing changes. Confirm glyph rendering and no clipping, occlusion, missing captions, or A/V drift.
17. Give one Fresh Clip Critic the compact evidence package described in `CLAUDE.md`. Store item-level verdicts in the QA report; follow the compact verdict format. A missing evidence item cannot receive PASS.
18. Apply `CLAUDE.md` correction/escalation rules: largest gap first, affected checks only, changed hypothesis for repeated failure. Unresolved blockers remain BLOCKED/rejected.
19. On PASS, freeze the artifact/hash, subtitle/style version, manifest, and QA evidence. Commit its intervals to `used_source_ranges`; continue the queue.
20. After freezing each clip, inspect remaining unreserved/unused semantic units and unresolved candidate conflicts using cached analysis. Add credible disjoint candidates; do not re-transcribe the source. Release rejected reservations and reconsider newly available units. End discovery only when every semantic unit has a disposition and no viable unused candidate remains. If the source supports fewer than two clips, document the limiting source evidence and remaining-range dispositions; never pad to meet a quota.

## 6. Final series QA and export

21. After freezing clips and exhausting discovery, run one fresh cross-clip review. Reuse hash-matched per-clip PASS evidence; inspect final renders together for style/register consistency and redundancy.
22. Run reproducible checks on the **actual final encoded files** and their manifests:

| Gate | Required evidence |
|---|---|
| Duration and format | Probe exact packet/frame timestamps and stream ends, accounting for start offsets; verify video duration and effective presented A/V runtime each satisfy the hard bounds. Check 9:16 display geometry including SAR/rotation and successful full decode. Do not round to pass. |
| Zero overlap | Compare every used canonical source interval across all accepted clips; include handles/layers and report zero intersecting source frames plus no reused audio ranges. Use actual frame/PTS mappings. |
| No duplicate footage | Check source provenance plus cross-clip frame/sequence fingerprints to flag repeated source content at different timestamps or via aliases. Verify flagged sequences visually/audio-wise; static interview backgrounds alone are not duplicates. |
| No repeated hook/setup | Compare manifest spans, opening/setup transcript passages, and flagged audio/visual sequences; review semantic near-duplicates. Record evidence-based disposition of flags. |
| Subtitles and series style | Check font/style hashes, subtitle event bounds, paired EN/JP timing, missing text, and unmasked target-word scans. Compare representative actual final frames for typography, scale, placement, EN/JP relationship, wrapping, and framing consistency. |
| Meaning and readiness | Reuse valid per-clip independent QA; series reviewer checks localization/masking register consistency and redundancy. Confirm natural starts/ends, standalone usability, and no padding from recorded evidence and any newly flagged passages. |
| Exhausted discovery | Full semantic coverage and reasons for unused/rejected units; no viable pending/unreserved candidates. Record reasons for natural durations outside the preference band. |

Automation proves measurable properties; meaning and perceptual similarity require evidence review, not config/fingerprint scores alone.

23. Any series failure blocks completion. Correct only responsible clips/items, invalidate affected evidence, and rerun affected series checks. Unchanged frozen clips retain their PASS. After verification, copy approved artifacts without re-encoding to `output/`, verify hashes, and record destination paths. If an export is re-encoded, treat it as a changed artifact and validate affected checks again.

## 7. Deliverables and completion

```text
output/
  clip_01_<topic>/                 # repeat for each accepted clip
    final.mp4
    subtitles.ass                 # rendered bilingual subtitle styling
    subtitles.srt                 # bilingual timed text; no ASS styling claim
    transcript.txt                # accurate unmasked speech, source timestamps
    translation_notes.md          # concise decisions/uncertainties, or none
    source_manifest.json
    qa_report.md                  # hashes, item verdicts, evidence paths
  shared/
    subtitle_style_spec.md
    clip_candidate_map.md
    source_overlap_audit.md       # zero-frame result, algorithm/script, inputs
    gauntlet_state.json           # final snapshot/index, not another live state
    gauntlet_report.md            # compact meaningful-round table
    final_series_qa.md
```

Retain helpers in `scripts/`, evidence/caches in `work/`; reports link existing files. Gauntlet rows: target, factual change, evidence, verdict, largest gap, fix/strategy, result. Series report: clips, exact durations, manifests, hashes, verdicts, coverage, limitations.

Declare COMPLETE only when the full source has been searched; no usable unused candidates remain; all accepted clips are rendered and independently PASS; hard duration/format/zero-overlap/uniqueness/no-padding gates pass; the approved template and localization style are consistent; final series QA is PASS; and deliverables/state are saved. Multiple clips are the production objective whenever supported. If only one is feasible, disclose that evidence-backed exception prominently. If a required gate is blocked, save progress and report BLOCKED, not COMPLETE. Finish with a concise output index, clip count/durations, QA result, and material limitations.
