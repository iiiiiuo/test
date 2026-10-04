# Permanent operating rules

Read this file and `prompt.md` before work: this file owns durable constraints; `prompt.md` owns production objectives and execution. Load existing skills only as needed.

## 1. Authority, autonomy, boundaries

- Precedence: current user requirements → this file → `prompt.md` → compatible skills. Actual references govern visual appearance; measured media/render evidence overrides state and Builder claims. Legacy overlap/120-second permissions are superseded.
- Measure source duration; ignore old guesses. Record material ambiguities and resolutions. Execute routine local inspection, editing, rendering, and QA autonomously; ask only for genuine unresolved blockers.
- Inputs are immutable, including inputs outside `input/`. Never overwrite, rename, delete, or destructively transform source media, references, fonts, or supplied resources. Write generated files only under `work/`, `scripts/`, or `output/`.
- No external uploads, publication, paid services/APIs, new charges, or credential disclosure. Missing local tools/models do not authorize cloud substitutes.
- Never fabricate speech, translation, evidence, measurements, or QA success. Report unavailable evidence as BLOCKED.

## 2. Hard media constraints

- Final videos are 9:16 and satisfy **60.0 <= actual duration < 120.0 seconds**. The upper bound is exclusive; rounded displays and planned durations are not proof.
- Final clips share **zero source frames**. Candidate overlap is allowed only before final selection. Reserve disjoint intervals before rendering and recheck every extension/change.
- Track all used intervals: hooks, questions/setup, reactions, quotes, teasers, flashbacks, source B-roll, intros/outros, and transition handles. Cuts require interval lists, not an enclosing range.
- Use canonical source IDs, decoded frame indices, and original presentation timestamps/timebase. Store intervals as half-open `[start_frame, end_frame_exclusive)`. For the same source, overlap exists when `max(a.start,b.start) < min(a.end,b.end)`. Adjacent intervals sharing only an exclusive endpoint are allowed. For variable frame rate, use decoded frame/PTS mappings; never infer frames from rounded seconds or nominal FPS alone. Track audio source ranges too; no repeated source speech/setup.
- Do not duplicate footage or repeat the same hook/setup within or across exports. Account for repeated source content appearing at different timestamps; disjoint timestamps alone do not prove unique content. Similar subject matter or generic repeated words alone are not duplicate footage/hooks.
- No duration padding: unrelated conversation, meaningless silence, freeze frames, slowdown, repeated speech/footage, or redundant intro/outro. Preserve meaningful pauses and reactions. Never distort meaning through cuts or rearrangement.

## 3. Speech and subtitle integrity

- Keep an accurate, unmasked internal English transcript. Preserve actually spoken AAVE, slang, contractions, reduced pronunciation, informal grammar, regional/internet language, proper nouns, and register. Do not normalize into Standard English or add slang not spoken.
- Mark uncertain speech and confidence. Resolve locally with the relevant audio; cut LOW/UNTRANSLATABLE material where coherent, otherwise reject that candidate. Never guess.
- Japanese: semantic fidelity first, then natural spoken Japanese, reference-style consistency, and concise readability. Preserve humor, sarcasm, confidence, aggression, friendliness, and energy where present. Do not represent AAVE with racial stereotypes or invented Japanese dialects.
- Display English + Japanese. Mask curse words **only in displayed English**, using a consistent reference-derived list, e.g. `ni**a`, `ni**as`, `b*tch`, `f*ck`, `f*cking`, `sh*t`. Translate from the unmasked meaning; do not propagate asterisks mechanically into Japanese. Keep spoken audio uncensored. Ordinary editing must preserve speech and A/V sync.
- Required typography: **Yu Gothic / 游ゴシック Bold; white text; black outline; black shadow**. No silent font substitution. Verify actual font file, glyph coverage, weight, and renderer fallback.

## 4. Reference and evidence

- `REFERENCE_VIDEO` is visual ground truth and the series quality bar for subtitle geometry, localization/register, timing, and editing rhythm. Reference screenshots support it. Explicit constraints above remain binding.
- Judge actual rendered video/audio and extracted render frames against actual reference frames. ASS/SRT settings, command success, and Builder assurances do not prove visual quality.
- Calibrate and freeze one shared subtitle template with reference-derived measurements/tolerances and evidence as specified in `prompt.md`. Require perceptual series consistency, not pixel identity across different content/compression.
- Frame faces, bodies, gaze, and conversational subjects naturally. Use punch-ins, zooms, jump cuts, and reframing only where reference-supported. Do not invent unrelated effects.

## 5. Independent QA and bounded correction

- Normal loop: `Builder → actual render → one Fresh Clip Critic → targeted correction`. Lead may build but cannot be sole final judge. One critic covers structure, transcript, translation, masking, timing, visuals, framing, duration, standalone quality, and source usage.
- Give the critic only task/rubric, relevant source/audio/transcript spans, subtitle files, manifest, actual render, reference evidence, and style spec. Never provide Builder reasoning, parameter rationales, confidence, or self-evaluation. Use an independent context. If that is unavailable, record independent QA as BLOCKED.
- Launch specialist critics (Structure/Translation/Timing/Visual etc.) **only for blocking failures needing specialist diagnosis**. Calibration and series review are shared checks, not per-clip pipelines.
- Persist item-level verdicts and evidence paths against artifact hashes. Compact response:

```text
VERDICT: PASS | FAIL
Blocking gaps: none | item + timestamp/frame + evidence (one line per gap)
Largest gap: none | one gap
Fix: none | concrete correction
```

- Fix the largest meaningful gap first; retain other blockers. Re-render and inspect affected checks only. Two occurrences of the same failure require a different root-cause hypothesis; log the failed approach. Diminishing returns may end cosmetic tuning, never waive a hard constraint or unresolved blocker.
- Freeze PASS work; never re-evaluate it unchanged. Invalidate only affected checks after changes: boundaries → structure/duration/overlap/timing; wording → translation/masking/wrapping/timing; style/font/render → dependent visuals. Carry forward unaffected PASS.
- Final series QA adds cross-clip and final-file checks; reuse valid per-clip verdicts instead of repeating full criticism.

## 6. Compact durable state and reuse

- Canonical state: `work/state.json`. Canonical reservations: `work/source_timeline_ledger.json`. Cache full transcript/alignment and semantic map once under `work/`; keep large media and evidence separate. State stores paths/IDs, not copies of those files.
- State indexes input hashes/metadata, caches/style, candidates/dispositions, reservations/committed `used_source_ranges`, completed clips, artifact hashes, item QA/evidence, uncertainties, best renders, failed approaches, current task/next action/blockers. Link separate per-clip details.
- Update atomically after meaningful transitions. On resume read state, verify dependency hashes, and continue the next incomplete action. Prevent concurrent reservation collisions; release reservations for rejected clips and invalidate the series audit when membership changes.
- Migrate legacy `state/{project_state,gauntlet_state,multi_clip_state,source_timeline_ledger,failed_approaches}.json` facts once into canonical state/ledger and linked records. Preserve originals; avoid competing live copies.
- Whole-source transcription **and semantic analysis** run once by default. Reuse caches for subsequent discovery. Reprocess only defective/changed spans; global reruns or recalibration require documented cache invalidity, changed inputs, or a demonstrated shared defect. A new clip alone is not a reason.
- Hand off paths, relevant timestamps/transcript slices, compact rubric, scope, and next action. Do not paste full transcripts, this file, or `prompt.md` into every agent task. Persist decisions and evidence, not long reasoning logs. Token efficiency never replaces necessary media inspection.
