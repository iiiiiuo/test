"""Diagnose clip boundaries and uncaptioned speech from the source (16 kHz wav + ASR words + approved line spans)."""
import json, wave, numpy as np, sys
ROOT = '/home/user/test'
clips = json.load(open(f'{ROOT}/work/selected_clips.json'))
defs = json.load(open(f'{ROOT}/work/clips_def.json'))
WAV = {'part_1': 'part_1', 'part_2_2': 'part_2_2', 'part_3': 'part_3', 'part_4': 'part_4', 'part_5': 'part_5', 'part_6': 'part_6'}
cache = {}
def audio(sid):
    if sid not in cache:
        w = wave.open(f'{ROOT}/work/audio/{WAV[sid]}.wav'); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
        cache[sid] = x
    return cache[sid]
def rms_db(sid, t0, t1):
    x = audio(sid); a, b = int(t0 * 16000), int(t1 * 16000)
    seg = x[max(0, a):max(a + 1, b)]
    return 20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9)
def words(c):
    W = []
    for r in defs[c['candidate']].get('asr') or [c['candidate']]:
        try: W += [w for s in json.load(open(f'{ROOT}/work/asr/{r}.large.json'))['segments'] for w in s['words']]
        except FileNotFoundError: pass
    T = [w for s in json.load(open(f"{ROOT}/work/asr/{c['source_id']}.turbo.json"))['segments'] for w in s['words']]
    return sorted(W, key=lambda w: w['s']), T
out = {}
for c in clips:
    sid = c['source_id']; W, T = words(c)
    # speech level reference: 90th percentile of 50 ms RMS inside the clip
    lv = [rms_db(sid, t, t + 0.05) for iv in c['intervals'] for t in np.arange(iv['start_s'], iv['end_s'], 0.05)]
    ref = np.percentile(lv, 90); floor = np.percentile(lv, 10)
    rep = dict(ref_db=round(float(ref), 1), floor_db=round(float(floor), 1), boundaries=[], uncaptioned=[])
    for iv in c['intervals']:
        for kind, t in (('start', iv['start_s']), ('end', iv['end_s'])):
            prof = [round(float(rms_db(sid, t + d, t + d + 0.05)) - ref, 1) for d in np.arange(-0.4, 0.4, 0.05)]
            # words straddling or just outside the boundary
            near = [(w['w'].strip(), round(w['s'], 2), round(w['e'], 2)) for w in (W or T) if t - 0.8 < w['e'] and w['s'] < t + 0.8]
            rep['boundaries'].append(dict(kind=kind, t=t, rel_db=prof, near=near))
    # uncaptioned: ASR words inside intervals but outside every line span (+-0.3 s)
    spans = [(l['start'] - 0.3, l['end'] + 0.3) for l in c['lines']]
    for src_words, name in ((W, 'large'), (T, 'turbo')):
        miss = [w for w in src_words if any(iv['start_s'] <= w['s'] < iv['end_s'] for iv in c['intervals'])
                and not any(a <= w['s'] <= b for a, b in spans)]
        if miss:
            groups = []
            for w in miss:
                if groups and w['s'] - groups[-1][-1]['e'] < 1.0: groups[-1].append(w)
                else: groups.append([w])
            rep['uncaptioned'] += [dict(asr=name, start=round(g[0]['s'], 2), end=round(g[-1]['e'], 2), text=''.join(x['w'] for x in g).strip()) for g in groups]
    out[c['clip_id']] = rep
json.dump(out, open(f'{ROOT}/work/b/boundary_check.json', 'w'), indent=1, default=float)
for k, r in out.items():
    print('==', k, 'ref', r['ref_db'], 'floor', r['floor_db'])
    for b in r['boundaries']:
        inside = b['rel_db'][:8] if b['kind'] == 'end' else b['rel_db'][8:]
        outside = b['rel_db'][8:] if b['kind'] == 'end' else b['rel_db'][:8]
        print(f"  {b['kind']:5} {b['t']:.2f} inside {inside[-3:] if b['kind']=='end' else inside[:3]} outside {outside[:4] if b['kind']=='end' else outside[-4:]} near {b['near'][-3:] if b['kind']=='end' else b['near'][:3]}")
    for u in r['uncaptioned']: print('  UNCAP', u)
