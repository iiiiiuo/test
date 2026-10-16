"""Series 2 rev 2 (giub, 2026-10-16): naming changes, applied only to Japanese string literals in work/s2/review_src_s2*.py and to work/s2/clip_meta.json."""
import re, glob, tokenize, io, json
M = [(r'Ralph(?! Lauren)', 'Ralph Lauren'), (r'Trump', 'トランプ'), (r'Warren Buffett', 'ウォーレンバフェット'), (r'BMF', 'Black Mafia Family'),
     (r"Denny's", 'デニーズ'), (r'Ukraine', 'ウクライナ'), (r'(?<!Good Morning )America', 'アメリカ'), (r'Pharrell', 'ファレルウィリアムズ'),
     (r'赤い帽子', 'トランプ支持者の赤の帽子')]
JP = re.compile('[ぁ-んァ-ヴ一-龯]')
tot = {a: 0 for a, _ in M}
def fix(s):
    for a, b in M:
        tot[a] += len(re.findall(a, s)); s = re.sub(a, b, s)
    return s
for f in sorted(glob.glob('work/s2/review_src_s2*.py')):
    src = open(f, encoding='utf-8').read(); lines = src.splitlines(keepends=True); offs = [0]
    for l in lines: offs.append(offs[-1] + len(l))
    ed = []
    for t in tokenize.generate_tokens(io.StringIO(src).readline):
        if t.type == tokenize.STRING and JP.search(t.string):
            s = fix(t.string)
            if s != t.string: ed.append((offs[t.start[0]-1] + t.start[1], offs[t.end[0]-1] + t.end[1], s))
    for st, en, s in reversed(ed): src = src[:st] + s + src[en:]
    open(f, 'w', encoding='utf-8').write(src)
m = json.load(open('work/s2/clip_meta.json'))
m = {k: {kk: fix(vv) for kk, vv in v.items()} for k, v in m.items()}
json.dump(m, open('work/s2/clip_meta.json', 'w'), indent=1, ensure_ascii=False)
print(tot)
