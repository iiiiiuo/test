"""List captions whose first word is heard >1 s away from the caption onset (render ASR vs captions)."""
import json, re, difflib, sys
for c in sys.argv[1:]:
    cap = json.load(open(f'work/b/{c}/captions.json'))['captions']
    r = json.load(open(f'work/b/{c}/qa/render_asr.json'))
    words = [w for s in r['segments'] for w in s['words']] if isinstance(r, dict) else r
    norm = lambda t: re.sub(r"[^a-z0-9']", '', t.lower())
    ct = [(norm(t), i) for i, x in enumerate(cap) for t in x['en_unmasked'].split()]
    sm = difflib.SequenceMatcher(None, [x[0] for x in ct], [norm(w['w']) for w in words], autojunk=False)
    for i, x in enumerate(cap):
        j0 = next(j for j, y in enumerate(ct) if y[1] == i)
        for b in sm.get_matching_blocks():
            if b.size and b.a <= j0 < b.a + b.size:
                o = words[b.b + j0 - b.a]['s'] - x['start']
                if abs(o) > 1.0: print(c, f"{x['start']:.2f}", f"off={o:+.2f}", x['en_unmasked'][:50])
                break
