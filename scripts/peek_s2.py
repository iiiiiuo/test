"""Builder helper: ASR words + 40 ms dBFS around a source time. peek_s2.py SRC ASRID T [span]"""
import json, sys, wave, numpy as np, glob
src, aid, t = sys.argv[1], sys.argv[2], float(sys.argv[3]); sp = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
for f in sorted(glob.glob(f'work/asr/{aid}*.json')):
    ws = [x for s in json.load(open(f))['segments'] for x in s['words']]
    print(f.split('/')[-1], ' '.join(f"{x['s']:.2f}{x['w']}" for x in ws if t - sp - 0.5 < x['s'] < t + sp))
w = wave.open(f'work/audio/{src}.wav'); sr = w.getframerate(); ch = w.getnchannels(); a = t - sp
w.setpos(int(a * sr)); x = np.frombuffer(w.readframes(int(sr * 2 * sp)), np.int16).astype(float).reshape(-1, ch).mean(1) / 32768; n = int(sr * 0.04)
print(' | '.join(f"{a + i / sr:.2f}:{20 * np.log10(np.sqrt(np.mean(x[i:i + n] ** 2)) + 1e-9):.0f}" for i in range(0, len(x) - n + 1, n)))
