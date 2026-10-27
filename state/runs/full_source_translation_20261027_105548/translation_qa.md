# Translation QA — full_source_translation_20261027_105548

Critic: an independent Translation Critic in a fresh context. It got the audio, the EN/JP draft (no builder notes or confidence marks) and the rubric only. It re-ran large-v3 on the whole audio and medium.en on doubtful spans (a later large-v3 span pass was cut off by a timeout). Full report: work/runs/<RUN>/critic_report.md

## Round 1: PASS (no blocking gaps)
- Coverage 0.00–135.81 complete. Only host backchannels ("yeah") and silent gaps are unsubtitled.
- EN matches ASR elsewhere (ain't, finna, holla, we was, whoop, Rasslin', Bonanza, Beverly, Snoopy, G). JP faithful, casual, no added aggression, proper nouns in English.

## Suggestions and dispositions
- 014 "or none" → "and none": APPLIED.
- 006 "I say" → "I said": APPLIED (both span passes).
- 034 make speaker change to Mom clear: APPLIED 「そしたらおふくろが『…』」.
- 035 「電話の後ろで俺は」 too literal: APPLIED 「後ろで俺が『…』」.
- 008 "and thought" vs "oh wow": NOT applied; the builder's large-v3 span pass gave "and thought" (0.95). Left as MED and put to the user in translation_review.md §D.
- 025 "Sonny" (low confidence 0.07–0.77, other passes heard different words): NOT applied; stays out of the subtitle, reported in §D.
- 003 leading "So/Oh", 024 "went in there": NOT applied (low-confidence filler / minor).
