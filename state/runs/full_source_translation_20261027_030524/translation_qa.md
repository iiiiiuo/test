# Translation QA — full_source_translation_20261027_030524

Critic: independent Translation Critic (fresh context; given audio, EN/JP draft and rubric only, no builder notes). It re-ran large-v3 and medium.en on the audio itself.

## Round 1: FAIL
- 032 (89.16–91.62): 「このカメラ放り出して」 = throwing the camera away; the source means leaving the interview camera. **Blocking.**
- 030 (82.40–84.20): 「実物は全然よかった」 lost the "way better in person" comparison. **Blocking.**
- Non-blocking: 019 wording, 040 「喜んでくれた」, 020 keep "bro" tone, 039 "Let's do it!" vs "It's lit!", 025 is a song lyric from the music bed.
- Missed speech: none. Gaps 27.8–36.3, 39.7–51.9, 61.4–64.3, 100.3–107.6, 126.7–130.7 are music only; "Thank you for watching", "We'll be right back" and "Ooh!" runs are hallucinations.

## Fixes
- 032 → 「もう今すぐカメラの前から / 飛び出したいくらいだよ」
- 030 → 「実物のほうが断然よかった」
- 019 → 「Travis、マジな話 / この内装見たら全部しっくりくるんだ」; 040 → 「…喜んでくれたよ」; 020 → 「これは…これはヤバいって、マジで」
- 039: windows 96.5–101.5 and 97.5–100.8 on both models give "Let's do it!"; only windows that start at 99.0 give "It's lit!" (onset cut off). Kept "Let's do it!" at MED.
- 025: presented to the user as a song lyric, with the choice to leave it unsubtitled.

## Round 2 (changed items only): PASS
```
VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none
```
