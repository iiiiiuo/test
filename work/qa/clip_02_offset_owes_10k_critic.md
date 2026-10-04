# Fresh Clip Critic: clip_02_offset_owes_10k
Render: work/clips/clip_02_offset_owes_10k/render.mp4 (1080x1920, v 70.6706 s / a 70.670 s)
Evidence frames: scratchpad c2/{a,b,c,d,e}.png; ASR spot-check: scratchpad c2_asr.txt (faster-whisper large-v3, 7 spans)

VERDICT: FAIL

1 structure: PASS. Host setup question (0.0-18.4) -> guest explanation of Offset debt / DMs -> payoff "How much... 10K... kudos to you" (58.4-70.7). Standalone.
2 duration: PASS. video 70.6706 s, audio 70.670 s (60 <= d < 120).
3 transcript: PASS. 7 spans re-transcribed (66.9-74, 79.4-89.5, 90.5-99.6, 103.3-112.4, 112.3-119.49, 122.96-128.4, 128.2-135.27). Matches; AAVE kept ("I be feeling", "you a bum ass", "owe me bread", "wildin'", "broski"). Minor: fillers "like, like, I'm like" (~83 s src) omitted; "Okay," at 79.5 low-confidence (0.09 ASR); "taking people's bread, running off" ASR-disputed (medium). Non-blocking.
4 translation: PASS. Faithful/natural casual register. Note (non-blocking): 27 "I'll get it back in blood" -> 「なぁ、きっちり返すから」 softens the menacing tone implied by "angry texts about getting in blood"; consider 「血で返してやるよ」-type rendering or neutral 「ちゃんと返すって」 consistently with 24.
5 masking: PASS. ni**a (17), ni**as (20); JP not asterisked.
6 timing: PASS. Onsets checked: ev4 5.992 -> src 67.12; ev10 18.372 -> 79.50; ev15 29.592 -> 90.72; ev29 58.462 -> 123.06. No overlaps (20 ms gaps), dwell >= 0.88 s.
7 visuals: PASS. Matches spec/reference r_30 (Yu Gothic Bold white, outline+shadow, EN above JP, y~948); no overflow in sampled frames, max 4 lines/event.
8 framing: FAIL. Output 57.8-58.36 s (src ~118.9-119.49, frames ~3560-3581, piece G crop x=430): source camera pans/zooms out, fixed crop lets guest slide out of the band; at 58.0-58.3 the band shows mostly empty set/bookshelf with the guest's face cut at the right edge (c2/d.png, h_58.0, h_58.3), then hard cut to wide shot. Elsewhere natural (head turns at 46/53 s acceptable).
9 editing: PASS. One internal cut 58.358 s (src 119.486 -> 122.956) joins "I'm like, damn." -> "How much did he owe you?" without distorting meaning; no padding; A/V start 0/0.
10 source usage: PASS. Segments 1749 + 369 = 2118 frames x 1001/30000 = 70.6706 s = probed duration.

Largest gap: item 8 framing at 57.8-58.36 s.
Fix: For source frames ~3555-3581 switch piece to a wide/tracking crop that keeps the guest centered (e.g. split piece G at the camera-move onset and keyframe crop x from 430 toward ~800, or use WG crop x=987 / full-width for that tail); re-render and recheck framing only.
