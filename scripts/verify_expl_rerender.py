"""Check that the explanation-row re-render changed nothing but the explanation row (and the approved rev 4 JA lines).

Compares each clip's current captions.json / framing.json (and the new manifest) with the frozen PASS version in git
(REF commit). Prints one line per clip: cut, crops, EN/JP captions identical or the differing line ids, plus the
explanation events now in subtitles.ass. Exit code 1 when anything other than the allowed lines differs.
Usage: python3 scripts/verify_expl_rerender.py [REF]
"""
import json, subprocess, sys, re

ROOT = '/home/user/test'
REF = sys.argv[1] if len(sys.argv) > 1 else '909eb4d'
ALLOWED = {'Clip_02_L006', 'Clip_06_L009', 'Clip_14_L010'}   # series 1 rev 4 JA edits approved by giub 2026-10-17


def at_ref(path):
    return json.loads(subprocess.run(['git', '-C', ROOT, 'show', f'{REF}:{path}'], capture_output=True, text=True, check=True).stdout)


bad = False
clips = [(f'Clip_{n:02d}', 'b') for n in range(1, 22)] + [(f'Clip_{n}', 'b2') for n in range(22, 40)]
for cid, d in clips:
    base = f'work/{d}/{cid}'
    cur_c, old_c = json.load(open(f'{ROOT}/{base}/captions.json')), at_ref(f'{base}/captions.json')
    cur_m = json.load(open(f'{ROOT}/{base}/source_manifest.json'))   # written by this render from framing.json
    cur_f, old_f = json.load(open(f'{ROOT}/{base}/framing.json')), at_ref(f'{base}/framing.json')
    seg = lambda m: [(s['start_frame'], s['end_frame_excl']) for s in m['video_segments']]
    key = lambda c: (c['line_id'], round(c['start'], 3), round(c['end'], 3), tuple(c['en']))
    fr = lambda f: [(i['start_frame'], i['end_frame_excl'], [(x['start'], x['end'], x['w'], x['h'], x['x'], x['y']) for x in i['shots']]) for i in f['intervals']]
    same_cut = fr(cur_f) == fr(old_f) and seg(cur_m) == [(i['start_frame'], i['end_frame_excl']) for i in old_f['intervals']]
    same_timing = [key(c) for c in cur_c['captions']] == [key(c) for c in old_c['captions']]
    jp_diff = sorted({c['line_id'] for c, o in zip(cur_c['captions'], old_c['captions']) if c['jp'] != o['jp']})
    expl = sum(1 for l in open(f'{ROOT}/{base}/subtitles.ass', encoding='utf-8') if l.startswith('Dialogue') and ',Expl,' in l)
    ok = same_cut and same_timing and set(jp_diff) <= ALLOWED
    bad |= not ok
    print(cid, 'OK ' if ok else 'BAD', 'cut/crops same' if same_cut else 'CUT CHANGED', '| EN+timing same' if same_timing else '| EN/TIMING CHANGED',
          '| JP changed:', ','.join(jp_diff) or 'none', '| expl lines', expl,
          '| render', cur_m['render']['sha256'][:12])
sys.exit(1 if bad else 0)
