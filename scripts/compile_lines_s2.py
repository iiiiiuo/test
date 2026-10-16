"""Resolve authored review entries into timed lines snapped to ASR word boundaries.
Writes work/s2/review_lines.json and prints a side-by-side check (authored EN vs ASR words in span)."""
import json, sys, importlib, re
sys.path.insert(0, 'work/s2')
defs = json.load(open('work/s2/clips_def.json'))
def words(cid):
    c = defs[cid]; L = []
    for a in c['asr']:
        d = json.load(open(f'work/asr/{a}.large.json'))
        L += [dict(w=w['w'].strip(), s=w['s'], e=w['e']) for s in d['segments'] for w in s['words']]
    L.sort(key=lambda w: w['s']); out = []
    for w in L:
        if out and w['s'] < out[-1]['e'] - 0.05: continue
        out.append(w)
    iv = c['iv']
    T = json.load(open(f"work/asr/{c['src']}.turbo.json"))
    TW = [dict(w=w['w'].strip(), s=w['s'], e=w['e']) for s in T['segments'] for w in s['words']]
    res = []
    for a, b in iv:
        ws = [w for w in out if w['s'] >= a - 0.05 and w['e'] <= b + 0.15]
        if not ws: ws = [w for w in TW if w['s'] >= a - 0.05 and w['e'] <= b + 0.15]
        res += ws
    return res
mods = [importlib.import_module(m) for m in sys.argv[1:]] if len(sys.argv) > 1 else []
allc = {}
for m in mods: allc.update(m.CLIPS)
result = {}
for cid, ents in allc.items():
    A = {a['n']: a for a in json.load(open(f'work/s2/lines_auto/{cid}.json'))}
    W = words(cid)
    def snap_s(t): return min(W, key=lambda w: abs(w['s'] - t))['s']
    nz = lambda t: re.sub(r"[^a-z0-9 ]", "", t.lower().replace("'", "")).split()
    NW = [nz(w['w'])[0] if nz(w['w']) else '' for w in W]
    def find(phrase, after):
        ph = nz(phrase)
        for i in range(len(W)):
            if W[i]['s'] < after - 0.01: continue
            if NW[i:i + len(ph)] == ph: return i, i + len(ph) - 1
        raise SystemExit(f'{cid}: anchor not found: {phrase!r} after {after}')
    spans = []; bound = 0; pre_e = {}
    for i, e in enumerate(ents):
        if isinstance(e['s'], str): s = W[find(e['s'], bound)[0]]['s']
        elif e['s'] is not None: s = snap_s(e['s'])
        else: s = A[e['nums'][0]]['start']
        spans.append([s, None]); bound = s
        if isinstance(e['e'], str):
            pre_e[i] = W[find(e['e'], s)[1]]['e']; bound = pre_e[i] - 0.02
    for i, e in enumerate(ents):
        if i in pre_e:
            end = pre_e[i]
        elif e['e'] is not None:
            end = min(W, key=lambda w: abs(w['e'] - e['e']))['e']
        else:
            end = A[e['nums'][-1]]['end']
            if i + 1 < len(ents) and spans[i + 1][0] < end:
                prev = [w for w in W if w['e'] <= spans[i + 1][0] + 0.01]
                end = prev[-1]['e'] if prev else end
        spans[i][1] = end
    lines = []
    for i, (e, (s, en)) in enumerate(zip(ents, spans), 1):
        asr = ' '.join(w['w'] for w in W if w['s'] >= s - 0.01 and w['e'] <= en + 0.01)
        lines.append(dict(line_id=f'{cid}_L{i:03d}', start=round(s, 2), end=round(en, 2), speaker=e['spk'], en=e['en'], ja=e['ja'], ctx=e['ctx'], unc=e['unc'], asr=asr))
    result[cid] = lines
    print(f'## {cid}')
    for l in lines:
        bad = '' if l['end'] > l['start'] else '  !!SPAN'
        print(f"{l['line_id']} {l['start']:.2f}-{l['end']:.2f}{bad}\n   EN : {l['en']}\n   ASR: {l['asr']}")
old = {}
try: old = json.load(open('work/s2/review_lines.json'))
except Exception: pass
old.update(result)
json.dump(old, open('work/s2/review_lines.json', 'w'), indent=1, ensure_ascii=False)
