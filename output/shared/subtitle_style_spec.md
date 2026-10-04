# Global subtitle style spec (frozen v1)

Status: FROZEN after independent calibration critic PASS (`work/qa/calibration_critic.md`).

## Font
- File: `work/fonts/YuGothB.ttc` (byte copy of supplied `YuGothB.ttc`), sha256 `d923a57f781f06198167da4f58287be7ac64a954a47aff4295e078a42b4b68b2`
- Face index 0: family "Yu Gothic", subfamily "Bold", full name "Yu Gothic Bold", usWeightClass 700. Glyph coverage checked for all kana/kanji/Latin/punctuation used (fontTools cmap); missing = none.
- Renderer: FFmpeg 6.1.1 `subtitles` filter (libass) with `fontsdir=work/fonts` — the only font file available to libass in that dir; glyph shapes verified against reference crops (`work/calib/cmp_zoom.png`).

## Canvas and layout (1080x1920, 9:16, SAR 1:1; reference 720x1280 normalized x1.5)
- Sharp foreground band: y 438..1480 (1080x1042), reference measured 292..987 @720p (x1.5 = 438..1481).
- Background: same crop window scaled to 2000x1932, center-cropped 1080x1920, boxblur 28:3.
- Framing per shot class (auto-detected cuts + dissolves, `work/cache/shots.json`): guest close-up crop x0=430; DJ Envy x0=610; Jess x0=700 (1119x1080 windows); wide shots 1.2x punch (933x900, y0=150) on the guest (x0=987) or the left-seated speaker (x0=0) by speaker.

## Text
- ASS PlayRes 1080x1920, WrapStyle 2 (manual wrapping), one event per line, `\an8\pos(540,y)`.
- English: Yu Gothic Bold 54 (libass size), Japanese: Yu Gothic Bold 50. White fill `&H00FFFFFF`, black outline 3 px, black shadow 2 px (`&H80000000`), BorderStyle 1.
- Stack: English line(s) first, then Japanese line(s). First line box top y=948; line pitch 50 px.
- Wrap: max line width 760 px (measured with PIL on the same font); English greedy with single-word-orphan rebalancing, max 2 lines; Japanese manually broken, max 2 lines.

## Measurements vs reference (scaled x1.5)
| item | reference | test | tolerance |
|---|---|---|---|
| EN line ink width, same text | 754 px | 754 px | ±8% |
| JP line ink width, same text | 376 px | 379 px | ±8% |
| first line ink top | 956–959 | 957–959 | ±29 px |
| line pitch | 48–51 | 47–50 | ±8% |
| EN glyph height | 39–40 | 39–40 | ±8% |
| horizontal center | 539–545 | 537–540 | ±10 px |

Evidence: `work/calib/cmp50.png`, `work/calib/cmp_zoom.png`, `work/calib/side.png`, test render `work/clips/calib/render.mp4`, critic `work/qa/calibration_critic.md`.

## Timing
Phrase-level captions starting at the first word onset; held up to 0.5 s after the last word, never overlapping the next caption; minimum 0.8 s.

## English masking (reference-derived, two asterisks as in the reference "s**t", "f**king")
shit→s**t, fuck→f**k, fucking→f**king, fucked→f**ked, bitch→b**ch, nigga→ni**a, niggas→ni**as. Displayed English only; Japanese translated from unmasked meaning; audio uncensored.
