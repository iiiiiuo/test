"""Auto-segment candidate clip speech into review lines from cached ASR words.
Output: work/lines_auto/<clip>.json (line_id, start, end, text_large, text_turbo, agree, minp)."""
import json, re, os, sys
from difflib import SequenceMatcher
defs = json.load(open('work/clips_def.json'))
os.makedirs('work/lines_auto', exist_ok=True)
def words(path):
    d = json.load(open(path)); out = []
    for s in d['segments']:
        for w in s['words']: out.append(dict(w=w['w'].strip(), s=w['s'], e=w['e'], p=w['p']))
    return out
norm = lambda t: re.sub(r"[^a-z0-9' ]", "", t.lower()).split()
only = sys.argv[1:]
for cid, c in defs.items():
    if only and cid not in only: continue
    L = []
    for a in c['asr']:
        L += words(f'work/asr/{a}.large.json')
    L.sort(key=lambda w: w['s'])
    # dedupe overlapping windows
    ded = []
    for w in L:
        if ded and w['s'] < ded[-1]['e'] - 0.05: continue
        ded.append(w)
    T = words(f"work/asr/{c['src']}.turbo.json")
    lines = []
    for (a, b) in c['iv']:
        ws = [w for w in ded if w['s'] >= a - 0.05 and w['e'] <= b + 0.15]
        if not ws:  # no large-v3 coverage for this interval: fall back to turbo words
            ws = [dict(w, p=min(w['p'], 0.39)) for w in T if w['s'] >= a - 0.05 and w['e'] <= b + 0.15]
        cur = []
        for i, w in enumerate(ws):
            if cur and (w['s'] - cur[-1]['e'] > 0.6 or len(cur) >= 11 or
                        (re.search(r'[.?!]$', cur[-1]['w']) and len(cur) >= 3)):
                lines.append(cur); cur = []
            cur.append(w)
        if cur: lines.append(cur)
    out = []
    for n, l in enumerate(lines, 1):
        s, e = l[0]['s'], l[-1]['e']
        tl = ' '.join(w['w'] for w in l)
        tt = ' '.join(w['w'] for w in T if w['s'] >= s - 0.3 and w['e'] <= e + 0.3)
        ag = SequenceMatcher(None, norm(tl), norm(tt)).ratio()
        out.append(dict(n=n, start=round(s, 2), end=round(e, 2), text=tl, turbo=tt, agree=round(ag, 2), minp=min(w['p'] for w in l)))
    json.dump(out, open(f'work/lines_auto/{cid}.json', 'w'), indent=0, ensure_ascii=False)
    tot = sum(b - a for a, b in c['iv'])
    print(f"## {cid} {c['title']} dur={tot:.1f}s lines={len(out)}")
    for o in out:
        flag = '' if o['agree'] >= 0.75 and o['minp'] >= 0.4 else f"   <<T: {o['turbo']}  (ag={o['agree']} p={o['minp']})"
        print(f"{o['n']:02d} {o['start']:.2f}-{o['end']:.2f} {o['text']}{flag}")
