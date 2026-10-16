"""List heard speech in a render that no caption covers (render ASR words outside every caption window)."""
import json, sys
ROOT = '/home/user/test'
out = {}
for cid in sys.argv[1:]:
    cap = json.load(open(f'{ROOT}/work/b2/{cid}/captions.json'))['captions']
    words = [w for s in json.load(open(f'{ROOT}/work/b2/{cid}/qa/render_asr.json'))['segments'] for w in s['words']]
    miss = [w for w in words if not any(c['start'] - 0.3 <= w['s'] <= c['end'] + 0.1 for c in cap)]
    g = []
    for w in miss:
        if g and w['s'] - g[-1][-1]['e'] < 1.0: g[-1].append(w)
        else: g.append([w])
    out[cid] = [dict(start=round(x[0]['s'], 2), end=round(x[-1]['e'], 2), text=''.join(w['w'] for w in x).strip()) for x in g]
    for u in out[cid]: print(cid, u)
json.dump(out, open(f'{ROOT}/work/b2/uncaptioned.json', 'w'), indent=1, ensure_ascii=False)
