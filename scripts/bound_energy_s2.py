"""Boundary audio-energy check for series 2: dBFS just inside/outside each cut (40 ms windows)."""
import json, wave, numpy as np, sys
d = json.load(open('work/s2/selected_clips.json')); clips = d if isinstance(d, list) else d['clips']
def db(src, t, dur=0.04):
    f = wave.open(f'work/audio/{src}.wav'); sr = f.getframerate(); ch = f.getnchannels()
    f.setpos(max(0, int(t * sr))); x = np.frombuffer(f.readframes(int(sr * dur)), np.int16).astype(float).reshape(-1, ch).mean(1) / 32768
    return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9)
for c in clips:
    if sys.argv[1:] and c['clip_id'] not in sys.argv[1:]: continue
    for i, iv in enumerate(c['intervals']):
        a, b = iv['start_s'], iv['end_s']
        print(c['clip_id'], i, f"start {a:.2f} in {db(c['source_id'],a):.0f} | end {b:.2f} in {db(c['source_id'],b-0.04):.0f} out {db(c['source_id'],b):.0f} out+80 {db(c['source_id'],b+0.08):.0f}")
