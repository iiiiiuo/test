import json, sys, importlib
sys.path.insert(0, 'work')
mods = [importlib.import_module(m) for m in sys.argv[1:]]
defs = json.load(open('work/clips_def.json'))
for m in mods:
    for cid, ents in m.CLIPS.items():
        auto = json.load(open(f'work/lines_auto/{cid}.json')); A = {a['n']: a for a in auto}
        used = [n for e in ents for n in e['nums']]
        missing = sorted(set(A) - set(used))
        prev = None; probs = []
        for i, e in enumerate(ents):
            s = e['s'] if e['s'] is not None else A[e['nums'][0]]['start']
            en = e['e'] if e['e'] is not None else A[e['nums'][-1]]['end']
            if prev is not None and s < prev - 0.01: probs.append(f'overlap at entry {i+1} ({s} < {prev})')
            if en <= s: probs.append(f'bad span entry {i+1}')
            prev = en
        print(cid, len(ents), 'missing auto lines:', missing, probs or '')
