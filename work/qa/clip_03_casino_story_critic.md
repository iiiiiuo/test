# Fresh Clip Critic: clip_03_casino_story

Artifacts judged (sha256):
- render.mp4 `0ed6b5bba854f360e838e2008910abd4544011c7f8536db4978689af6bdfba98`
- subtitles.ass `7ff00c37779d045abb013061edcac1580d22e3ecf4fdcd3f7c9c3f4e37d327e8`
- subtitles.srt `fd70df3c602af1e7d5e34dae84a5b4eef1f3b03cb80701a504ba26b917b01ad4`
- source_manifest.json `3a2e27ba899f70936a18a0c0263efbdbd5c526eab8d7b4aa1293492fc4f85a3e`

Output to source mapping: seg1 out 0.000-16.817 = src 143.143-159.960; seg2 16.817-18.986 = 162.396-164.564; seg3 18.986-61.695 = 169.236-211.945; seg4 61.695-69.536 = 214.247-222.089; seg5 69.536-72.039 = 224.858-227.360.

Evidence: the ASR runs were faster-whisper large-v3 (plus medium) on the source spans and on the render audio. Their output is in `scratchpad/spans.out` and the session log. The frame grids came from the render at 1, 3, 9, 15, 17.5, 20, 37, 45, 52, 58, 62, 63.5, 66, 70 and 71.5 s, plus sequences at 61.7-63.3 s and 69.5-72.0 s. I also compared the render against the reference frame r_30.png.

## VERDICT: FAIL

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | structure | PASS (weak) | The clip opens on the host's question about the casino and moves through the guest asking strangers for money, chasing the repayment, getting dodged, then seeing the strip-club "made it rain" payoff. It ends on the host verdict "it ain't about the money, it's about the respect". It is coherent and resolved. Weakness: the clip never says outright that the guest lent the money. It is implied only by "y'all really want my money" at 38.2 s and "somebody owe you money" at 64.8 s. |
| 2 | duration | PASS | ffprobe: video 72.038633 s, audio 72.038005 s, format 72.038633 s. The manifest has 2159 frames x 1001/30000 = 72.0386 s. |
| 3 | transcript accuracy | FAIL | Caption 29 (61.77-63.33 s, src 214.25-215.9) shows "It's the image. It's the image." Three independent decodes of src 213.9-216.0 hear "It's the Emmys. It's the Emmys!" (p 0.88-1.00). Two decodes of the render span hear no "image" at all. Only the machine slice has "image". On screen, DJ Envy is laughing as he says it. That fits a joke that the story is an Emmy-worthy performance, and Charlamagne's next line is "if that story is true". Minor issues: in caption 33 (69.54 s), "And" is not audible in the render because the join starts at 224.858 and the render ASR begins at "at that point". Caption 19 (41.25 s) drops the spoken slang "fake" ("I fake probably", heard by 2 decodes). In caption 10 (19.09 s), "I probably hit him back" is contested: 2 decodes hear "I'm trying to hit him back". Confirmed correct: caption 1, "axing" (AAVE, 147.86/149.18), the "f**king lady" in caption 4, caption 6, "fake tweaking, gang" in caption 9, caption 17 "y'all really want my money" (confirmed on recheck), "spun off ... ten times", captions 24-25, and captions 31-32. |
| 4 | translation | FAIL (dependent on #3) | Caption 29 JP "イメージだよ、イメージ" translates the misheard "image". If the line is "It's the Emmys", it should read something like 「エミー賞もんだな」 / 「アカデミー賞級だろ」. All other Japanese is faithful and natural, and keeps the register: 「お前ちょっとイカれてんぞ」, 「ナメられてんぞ」, 「はぐらかされてさ」, 「金ばら撒いてた」, 「リスペクトの問題なんだよ」. None of it uses a stereotyped dialect. |
| 5 | masking | PASS | The English shows f**king (cap 4), s**t (cap 25) and f**ked (cap 31), all with a consistent two-asterisk mask. The Japanese has no asterisks, and the audio is uncensored. |
| 6 | timing | PASS | The SRT is sequential with 20 ms gaps and no overlaps. Sampled onsets: cap1 0.157 against word 0.10; cap4 5.717 against 5.74; cap5 8.377 against 8.38; cap9 16.90 against 16.84; cap16 36.69 against speech after silence ending 36.81; cap24 51.09 against 51.01. All are within 0.3 s. The uncaptioned "Thank you, bro" at about 52.2 s is off-mic crosstalk, so leaving it out is acceptable. Dwell is tight on cap 20 (1.02 s) and cap 21 (1.14 s) but matches the fast speech. |
| 7 | visuals | PASS | Yu Gothic Bold in white with black outline and shadow, English above Japanese, centred. The glyph shape, size and line pitch match reference r_30 (side-by-side crop). No clipping or overflow in any sampled frame. |
| 8 | framing | PASS | Speakers are framed within the sharp band with faces intact (1, 3, 9, 20, 52, 58, 62, 66, 70 s). The three framing changes in the last 2.5 s (69.54/70.0/70.9 s) follow source camera cuts. They are busy but not broken. |
| 9 | editing | PASS (minor) | No dead air: every silence is under 0.6 s. No repeated content. The joins at 16.82, 18.99 and 61.70 are clean and coherent. The 69.54 s join clips the leading "And" (see #3). The excluded spans are crosstalk or filler and leaving them out does not distort meaning. |
| 10 | source usage | PASS | Video frames 504+65+1280+235+75 = 2159 = edited_duration_frames = 72.0386 s, matching the probe. The audio sample ranges match the video intervals (6312606/44100 = 143.143 s, and so on). The intervals are disjoint and ascending. |

Blocking gaps:
- #3/#4: caption 29, 61.77-63.33 s (src 214.25-215.9). "It's the image. It's the image." / 「イメージだよ、イメージ」 is most likely "It's the Emmys" (3/3 targeted decodes). The English and Japanese are both wrong.

Fix:
1. Check src 213.9-216.0 locally. If it is "Emmys", change caption 29 to "It's the Emmys. It's the Emmys!" / 「エミー賞もんだな、エミー賞！」. If it cannot be resolved, mark it unclear and cut it or show "...".
2. Cleanups that are cheap and do not block: drop the inaudible "And" from caption 33 (or start seg5 a few frames earlier if "And" is really there), and restore "fake" in caption 19 ("I fake probably, like, got spun off...").
