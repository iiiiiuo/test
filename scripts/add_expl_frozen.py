"""Add the approved term-explanation row to a frozen PASS clip without touching its EN/JP captions.

Usage: python3 scripts/add_expl_frozen.py Clip_XX
Base: the frozen captions.json / subtitles.ass committed at FROZEN_REF (their hashes match work/b{,2}/frozen.json).
Series 1 rev 4 (approved by giub 2026-10-17) changes three Japanese words; those captions are re-wrapped only when
the new wording no longer fits one 760 px (ink) line. Every other caption event is written byte-identical to the
frozen file (checked). Then the Expl style and events from scripts/expl_row.py are appended.
Outputs: work/b{,2}/<clip>/subtitles.ass, subtitles.srt, captions.json (+ "explanations").
"""
import hashlib, json, os, subprocess, sys
from PIL import ImageFont
sys.path.insert(0, '/home/user/test/scripts')
from expl_row import expl_events, EXPL_FS, EXPL_PITCH

ROOT = '/home/user/test'
FROZEN_REF = '909eb4d'
CLIP = sys.argv[1]
N = int(CLIP.split('_')[1])
D, GL = ('b', 's1') if N <= 21 else ('b2', 's2')
BASE = f'work/{D}/{CLIP}'
EN_FS, JP_FS, TOP, PITCH, MAXW, JP_K = 54, 50, 948, 50, 760, 0.753
F_JP = ImageFont.truetype(f'{ROOT}/work/fonts/YuGothB.ttc', JP_FS, index=0)
REV4 = {'Clip_02_L006': ('White House', 'ホワイトハウス'), 'Clip_06_L009': ('Clinton夫妻', 'クリントン夫妻'),
        'Clip_14_L010': ('バース', 'verse')}
STYLE_SUB = 'Style: Sub,Yu Gothic,50,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,2,8,60,60,950,1'
STYLE_EXPL = f'Style: Expl,Yu Gothic,{EXPL_FS},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,2,8,60,60,950,1'


def git(path):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{FROZEN_REF}:{path}'], capture_output=True, check=True).stdout


def ass_t(t):
    cs = int(round(t * 100)); h, cs = divmod(cs, 360000); m, cs = divmod(cs, 6000); s, cs = divmod(cs, 100)
    return f'{h}:{m:02d}:{s:02d}.{cs:02d}'


def srt_t(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'


def caption_events(c):
    ev, y = [], TOP
    for t in c['en']:
        ev.append(f"Dialogue: 0,{ass_t(c['start'])},{ass_t(c['end'])},Sub,,0,0,0,,{{\\an8\\pos(540,{y})\\fs{EN_FS}}}{t}"); y += PITCH
    for t in c['jp']:
        ev.append(f"Dialogue: 0,{ass_t(c['start'])},{ass_t(c['end'])},Sub,,0,0,0,,{{\\an8\\pos(540,{y})\\fs{JP_FS}}}{t}"); y += PITCH
    return ev


frozen_ass = git(f'{BASE}/subtitles.ass')
assert hashlib.sha256(frozen_ass).hexdigest() == json.loads(git(f'work/{D}/frozen.json'))[CLIP]['ass_sha256'], CLIP   # PASS record at FROZEN_REF
cap = json.loads(git(f'{BASE}/captions.json'))
frozen_lines = frozen_ass.decode('utf-8').rstrip('\n').split('\n')
head = frozen_lines[:frozen_lines.index('[Events]') + 2]
assert STYLE_SUB in head
regen = [e for c in cap['captions'] for e in caption_events(c)]
assert frozen_lines[len(head):] == regen, f'{CLIP}: frozen ASS is not reproducible from captions.json'

changed = []
for c in cap['captions']:
    if c['line_id'] in REV4:
        old, new = REV4[c['line_id']]
        if any(old in t for t in c['jp']):
            c['jp'] = [t.replace(old, new) for t in c['jp']]
            if len(c['jp']) == 1 and F_JP.getlength(c['jp'][0]) * JP_K > MAXW:
                parts = c['jp'][0].split('　')   # break at the full-width space nearest the middle
                k = min(range(1, len(parts)), key=lambda i: abs(F_JP.getlength('　'.join(parts[:i])) - F_JP.getlength('　'.join(parts[i:]))))
                c['jp'] = ['　'.join(parts[:k]), '　'.join(parts[k:])]
            assert all(F_JP.getlength(t) * JP_K <= MAXW for t in c['jp']) and len(c['en']) + len(c['jp']) <= 4, (CLIP, c)
            changed.append(c['line_id'])

events = [e for c in cap['captions'] for e in caption_events(c)]
expl = expl_events(cap['captions'], f'{ROOT}/review/glossary/glossary_draft_{GL}.json', CLIP, cap['total_s'])
blocks = [(c['start'], [f"{srt_t(c['start'])} --> {srt_t(c['end'])}", *c['en'], *c['jp'], '']) for c in cap['captions']]
for st, en, y, lines in expl:
    for t in lines:
        events.append(f"Dialogue: 0,{ass_t(st)},{ass_t(en)},Expl,,0,0,0,,{{\\an8\\pos(540,{y})\\fs{EXPL_FS}}}{t}"); y += EXPL_PITCH
    blocks.append((st, [f"{srt_t(st)} --> {srt_t(en)}", *lines, '']))
head = head[:head.index(STYLE_SUB) + 1] + [STYLE_EXPL] + head[head.index(STYLE_SUB) + 1:]
open(f'{ROOT}/{BASE}/subtitles.ass', 'w', encoding='utf-8').write('\n'.join(head + events) + '\n')
srt = []
for i, (_, b) in enumerate(sorted(blocks, key=lambda x: x[0]), 1):
    srt += [str(i), *b]
open(f'{ROOT}/{BASE}/subtitles.srt', 'w', encoding='utf-8').write('\n'.join(srt))
cap['explanations'] = [dict(start=st, end=en, top_y=y, lines=lines) for st, en, y, lines in expl]
cap['explanation_source'] = f'review/glossary/glossary_draft_{GL}.json'
if changed:
    cap['rev4_changed_lines'] = sorted(set(changed))
json.dump(cap, open(f'{ROOT}/{BASE}/captions.json', 'w'), indent=1, ensure_ascii=False)
print(CLIP, 'explanations', len(expl), 'rev4', sorted(set(changed)) or '-', 'max bottom', max([y + EXPL_PITCH * len(l) for _, _, y, l in expl] or [0]))
