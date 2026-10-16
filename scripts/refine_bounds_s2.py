"""Series 2 Phase B boundary refinement. Each interval boundary moves to the quietest 20 ms point between the last included
word and the first excluded word (large-v3 word times; window widened to 0.15 s when the words touch), snapped to a frame.
Hand windows in W override the automatic one; CUTS removes internal spans. Rewrites work/s2/selected_clips.json (v1 kept)."""
import json, math, wave, numpy as np, shutil, os
ROOT = '/home/user/test'
W = {'Clip_27': [(0, 'start', 657.98, 658.06, "start in dip before 'uh because' (critic r2: opened inside 'Because')"),
                (0, 'end', 724.86, 724.94, "end in dip after 'manner' (critic r2: cut while 'manner' sounding), before 'what'")],
     'Clip_25': [(0, 'start', 1108.10, 1108.40, "start before 'And I' onset (energy rises 1108.48; critic r1 note: first word trimmed)")],
     'Clip_24': [(1, 'start', 1487.15, 1487.22, "start at 'since' (critic r1: uncaptioned 'I ain't gonna lie, I've been' before it)")],
     'Clip_30': [(0, 'start', 51.62, 51.78, "start in the gap between 'is,' and 'this is the thing' (critic r1: 51.47 opened on uncaptioned 'thing is')"),
                 (0, 'end', 146.30, 146.44, "end after 'each other', before the trailing 'and'")],
     'Clip_23': [(0, 'end', 1143.08, 1143.14, "end after 'fit in' (energy to 1143.05, critic r1), before 'okay'"),
                   (1, 'end', 1197.24, 1197.30, "end after 'about.' (energy to ~1197.22, critic r1), before 'That's a girl part'")],
     'Clip_26': [(1, 'end', 1949.60, 1949.88, "end after 'I love the respect', before the host's 'yeah'")],
     'Clip_31': [(1, 'start', 220.70, 220.80, "start in dip before 'And think about this' (energy check: old start in continuous audio)"),
                 (1, 'end', 232.72, 232.80, "end in dip after 'world.' (energy: 'world' sounds 232.46-232.70), before 'we sat there'")],
     'Clip_34': [(0, 'end', 1737.17, 1737.24, "end after 'right now.' (energy to ~1737.17), before 'Yeah'")],
     'Clip_39': [(0, 'start', 1443.42, 1443.54, "start in dip before 'And so' onset (energy rises 1443.56)")]}  # clip: [(interval index, 'start'|'end', lo, hi, reason)]
CUTS = {'Clip_35': [(0, (638.36, 638.44), (641.46, 641.56), "jump cut removes repeated, unapproved 'This is a race, I've been trying to tell you that' (critic r1: 1.8 s uncaptioned)")],
        'Clip_34': [(0, (1717.55, 1718.50), (1720.08, 1720.18), "remove uncaptioned, unapproved interjection 'You're transcending' (critic r1: 2.2 s uncaptioned speech)")]}  # clip: [(interval index, (lo, hi) cut start window, (lo, hi) cut end window, reason)]
src = json.load(open(f'{ROOT}/work/sources.json'))
defs = json.load(open(f'{ROOT}/work/s2/clips_def.json'))
P = f'{ROOT}/work/s2/selected_clips.json'
if not os.path.exists(f'{ROOT}/work/s2/selected_clips.v1.json'): shutil.copy(P, f'{ROOT}/work/s2/selected_clips.v1.json')
clips = json.load(open(f'{ROOT}/work/s2/selected_clips.v1.json'))
ledger = json.load(open(f'{ROOT}/work/source_timeline_ledger.json'))
aud = {}
def quietest(sid, lo, hi):
    if sid not in aud:
        w = wave.open(f'{ROOT}/work/audio/{sid}.wav'); aud[sid] = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)
    x = aud[sid]; best = None
    for t in np.arange(lo, max(lo + 0.005, hi - 0.02) + 1e-9, 0.005):
        a = int(t * 16000); e = float(np.sqrt(np.mean(x[a:a + 320] ** 2)) + 1e-9)
        if best is None or e < best[0]: best = (e, t + 0.01)
    return best[1], 20 * math.log10(best[0] / 32768)
def words(cid):
    L = [w for r in defs[cid]['asr'] for s in json.load(open(f'{ROOT}/work/asr/{r}.large.json'))['segments'] for w in s['words']]
    return sorted(L, key=lambda w: w['s'])
def mkiv(sp, f0, f1):
    return dict(start_s=round((sp + f0 * 1001) / 24000, 4), end_s=round((sp + f1 * 1001) / 24000, 4), start_frame=f0, end_frame_excl=f1,
                audio_start_sample_48k=round((sp + f0 * 1001) / 24000 * 48000), audio_end_sample_48k_excl=round((sp + f1 * 1001) / 24000 * 48000))
occ = [(r['source_id'], r['start_s'], r['end_s'], r['clip_id']) for r in ledger['committed']] + \
      [(c['source_id'], i['start_s'], i['end_s'], c['clip_id']) for c in clips for i in c['intervals']]
def clamp(cid, sid, kind, lo, hi, a, b):  # never reach into another clip's interval
    for s_, x0, x1, oc in occ:
        if s_ != sid or oc == cid: continue
        if kind == 'end' and x0 >= b - 0.01: hi = min(hi, x0 - 0.001)
        if kind == 'start' and x1 <= a + 0.01: lo = max(lo, x1 + 0.001)
    return lo, hi
log = []
for c in clips:
    sid = c['source_id']; sp = src[sid]['start_pts']; ws = words(c['candidate'])
    hand = {(k, kind): (lo, hi, why) for k, kind, lo, hi, why in W.get(c['clip_id'], [])}
    new = []
    for k, iv in enumerate(c['intervals']):
        a, b = iv['start_s'], iv['end_s']
        inside = [w for w in ws if w['e'] > a + 0.02 and w['s'] < b - 0.02]
        res = {}
        for kind in ('start', 'end'):
            if (k, kind) in hand: lo, hi, why = hand[(k, kind)]
            elif kind == 'start':
                first = inside[0]; prev = [w for w in ws if w['e'] <= first['s'] + 0.01 and w is not first]
                lo = prev[-1]['e'] if prev else first['s'] - 0.3; hi = first['s']; why = f"auto: between '{prev[-1]['w'].strip() if prev else ''}' and '{first['w'].strip()}'"
            else:
                last = inside[-1]; nxt = [w for w in ws if w['s'] >= last['e'] - 0.01 and w is not last]
                lo = last['e']; hi = nxt[0]['s'] if nxt else last['e'] + 0.3; why = f"auto: between '{last['w'].strip()}' and '{nxt[0]['w'].strip() if nxt else ''}'"
            if hi - lo < 0.15: lo, hi = (lo, lo + 0.15) if kind == 'start' else (hi - 0.15, hi)  # whisper glues onsets: widen into the included word, never into the excluded one
            hi = min(hi, lo + 1.0) if kind == 'end' else hi; lo = max(lo, hi - 1.0) if kind == 'start' else lo
            lo, hi = clamp(c['clip_id'], sid, kind, lo, hi, a, b)
            t, db = quietest(sid, lo, hi)
            res[kind] = round((t * 24000 - sp) / 1001)
            log.append(dict(clip=c['clip_id'], interval=k, kind=kind, window=[round(lo, 3), round(hi, 3)], cut_s=round(t, 3), cut_rms_dbfs=round(db, 1), reason=why))
        new.append(mkiv(sp, res['start'], res['end']))
    for k, wa, wb, why in CUTS.get(c['clip_id'], []):
        ta, _ = quietest(sid, *wa); tb, _ = quietest(sid, *wb)
        fa, fb = round((ta * 24000 - sp) / 1001), round((tb * 24000 - sp) / 1001)
        iv = new[k]; new[k:k + 1] = [mkiv(sp, iv['start_frame'], fa), mkiv(sp, fb, iv['end_frame_excl'])]
        log.append(dict(clip=c['clip_id'], kind='internal_cut', removed_frames=[fa, fb], removed_s=[round(ta, 3), round(tb, 3)], reason=why))
    c['intervals'] = new
    c['est_duration_s'] = round(sum(i['end_frame_excl'] - i['start_frame'] for i in new) * 1001 / 24000, 3)
# gates: duration, zero overlap within series 2 and against committed series 1
for i, a in enumerate(clips):
    assert 60.0 <= a['est_duration_s'] < 120.0, (a['clip_id'], a['est_duration_s'])
    for x in a['intervals']:
        assert x['start_frame'] < x['end_frame_excl']
        for r in ledger['committed']:
            if r['source_id'] == a['source_id']:
                assert not max(x['start_frame'], r['start_frame']) < min(x['end_frame_excl'], r['end_frame_excl']), (a['clip_id'], r['clip_id'])
    for b in clips[i + 1:]:
        if a['source_id'] != b['source_id']: continue
        for x in a['intervals']:
            for y in b['intervals']:
                assert not max(x['start_frame'], y['start_frame']) < min(x['end_frame_excl'], y['end_frame_excl']), (a['clip_id'], b['clip_id'])
                assert not max(x['audio_start_sample_48k'], y['audio_start_sample_48k']) < min(x['audio_end_sample_48k_excl'], y['audio_end_sample_48k_excl']), (a['clip_id'], b['clip_id'], 'audio')
json.dump(clips, open(P, 'w'), indent=1, ensure_ascii=False)
os.makedirs(f'{ROOT}/work/b2', exist_ok=True)
json.dump(log, open(f'{ROOT}/work/b2/boundary_changes.json', 'w'), indent=1)
for l in log: print(l['clip'], l.get('interval'), l['kind'], l.get('window'), l.get('cut_s'), l.get('cut_rms_dbfs'), l['reason'])
for c in clips: print(c['clip_id'], c['est_duration_s'])
