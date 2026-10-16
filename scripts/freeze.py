"""Freeze PASS clips: python3 scripts/freeze.py Clip_XX ... (records render+subtitle hashes and critic path in work/b/frozen.json)."""
import json, hashlib, sys
p = 'work/b/frozen.json'; fz = json.load(open(p))
for c in sys.argv[1:]:
    h = lambda f: hashlib.sha256(open(f'work/b/{c}/{f}', 'rb').read()).hexdigest()
    m = json.load(open(f'work/b/{c}/source_manifest.json'))
    assert m['render']['sha256'] == h('render.mp4') and m['subtitles']['sha256'] == h('subtitles.ass'), c
    assert open(f'work/b/{c}/qa/critic.md').read().lstrip().startswith('VERDICT: PASS'), c
    fz[c] = dict(render_sha256=h('render.mp4'), verdict='PASS', critic=f'work/b/{c}/qa/critic.md', ass_sha256=h('subtitles.ass'))
    print('frozen', c)
json.dump(fz, open(p, 'w'), indent=1)
