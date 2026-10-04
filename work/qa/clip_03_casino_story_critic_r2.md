# clip_03_casino_story - Fresh Clip Critic, round 2 (scoped re-check)

Artifacts judged: render.mp4 sha256 63beff63a32ec7383f3dc6ef0e362aaa0274c9d4f74473554287da624da8009a; subtitles.ass 7ff00c37...e8; subtitles.srt fd70df3c...d4
Probe: video 72.0386 s, audio 72.0380 s, 1080x1920.
Output->source map (manifest): seg3 out 18.986 = src 169.236; seg4 out 61.695 = src 214.247; seg5 out 69.536 = src 224.858.

VERDICT: FAIL - none of the three claimed subtitle edits are present in the render or in subtitles.ass/.srt.

## Item 3 transcript accuracy - FAIL
- src 214.2-215.8 (out ~61.77-63.33): render frame at out 62.4 burns "It's the image. It's the image." / "イメージだよ、イメージ" (also SRT cue 29, ASS). An independent local transcription of src 214.2-216.0 gives "It's(0.55) the(0.94) Emmys.(0.77)". The claimed "It's the Emmys!" caption is not in the render. Evidence: scratchpad c3r2/f_62.4.png.
- src 224.96 (out 69.64-72.04): render frame at out 70.0 still shows "And at that point, it ain't about the money. It's about the respect." (SRT cue 33). The leading "And" was not removed. The local transcription of src 224.86-227.36 gives "It(0.16) ain't about the money, it's about the respect." The opening ("At that point"/"It") is low confidence; "And" is not supported.
- src 191.50-195.46 (out 41.25-45.51): still ONE caption, "No, no, no. I probably, like, got spun off, like, ten times, blah, blah, blah." Not split, and "fake" was not restored. Evidence: f_42.5.png, f_44.8.png, SRT cue 19. Note: the local transcription hears "I think(0.94) probably", so if "fake" is restored, confirm that word against the audio first.
- Root cause: work/clips/clip_03_casino_story/captions.py (mtime 19:42:24) contains all three edits. subtitles.ass/.srt (19:42:30) and render.mp4 (19:45:04) do not, so the subtitle files were generated from a stale caption list (possibly a stale __pycache__ import or an old module) and burned in.
## Item 4 translation - FAIL (for the src 214.8 caption)
- The render shows イメージだよ、イメージ ("it's the image") for speech that the transcription renders as "It's the Emmys". The intended エミー賞もんだな！ (in captions.py) is not rendered. For the other two edited captions, the JP text is unchanged and still fits the meaning.
## Item 6 timing - FAIL (not verifiable as edited)
- The rendered cue timings are the old ones: cue 29 61.768-63.328 instead of src 214.80-215.80 = out ~62.25-63.25; cue 19 is one cue, 41.25-45.51, with no split at src 193.86/193.92; cue 33 starts at 69.638 (src 224.96). The edited timings do not exist in the artifact, so they cannot be checked.
## Item 7 visuals (split captions) - FAIL / not evaluable
- The split captions are not rendered. The existing unsplit cue 19 renders cleanly (2 EN + 2 JP lines, white with black outline, no clipping). There was no other style change.
## Regression diff (SRT vs transcript slice, other cues)
- Apart from the three edits, cues 1-28 and 30-32 match the earlier wording and the slice (axing, fake, gonna, and the masking are as before). No new regressions were seen, but the whole artifact is the pre-edit version.
## Items 1,2,5,8,10
- Carried forward as PASS from the prior round. Footage is unchanged, and the duration was re-probed at 72.04 s.
