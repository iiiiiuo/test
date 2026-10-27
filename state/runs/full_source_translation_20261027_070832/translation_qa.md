# Translation QA — full_source_translation_20261027_070832

Critic: an independent Translation Critic in a fresh context. It got the audio, the EN/JP draft and the rubric only (no builder notes or confidence marks) and re-ran large-v3, medium.en and small.en on the audio itself.

## Round 1: FAIL
- 019 (34.94–36.18): "bodyguards" is not supported by the audio. Every model hears "booty"; the last word varies (goals 0.13 / goons 0.52 with a prompt / groups / wounds / gloves). **Blocking.**
- 021 (41.00–43.38): "67% of the [Bobcats / bypass]" is unresolved, and 022–028 depend on it. **Blocking.** The critic proposed cutting 021–028. The user's full-source rule forbids cuts, so that fix was not applied.
- Non-blocking: 001 keep the agent "He" → applied; 007 more defiant → applied 「で、何か文句ある？」; 018 more punch → applied 「とっとと失せろ」; display EN must be masked → applied in the review file.
- Coverage: complete. 21.0–22.5 and 29.7–30.8 are silence or hallucination, 36.2–39.2 is laughter, and 50.6–51.0 is the tail of the last word. 001–018 match large-v3. 'Cause (008) and gonna (017) were confirmed.

## Resolution
019, 021 and 025 are marked LOW and put to the user in translation_review.md §D. Round 2 waits for the user's answer on those lines.
