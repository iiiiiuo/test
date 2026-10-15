"""Rev 3 (user request 2026-10-15): specific Japanese renderings. Applied only to string literals containing Japanese."""
import re, glob, tokenize, io
M = [('Timbs','ティンバーランド'),('Shaq','シャキールオニール'),('Moses','モーゼ'),('Steve Jobs','スティーブ・ジョブズ'),
     ('Ralph Lauren、Jobs','Ralph Lauren、ジョブズ'),('Jeff Bezos','ジェフ・ベゾス'),('Bezos','ベゾス'),('Elon','イーロン'),
     ('Hennessy','ヘネシー'),('BLM','ブラックライブスマター'),('バックパック系ラッパー','リュック系ラッパー'),('バックパックっぽくない','リュック系っぽくない')]
JP = re.compile('[ぁ-んァ-ヴ一-龯]')
tot = {a: 0 for a, _ in M}
for f in sorted(glob.glob('work/review_src_*.py')):
    src = open(f, encoding='utf-8').read()
    lines = src.splitlines(keepends=True)
    offs = [0]
    for l in lines: offs.append(offs[-1] + len(l))
    edits = []
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        if tok.type == tokenize.STRING and JP.search(tok.string):
            s = tok.string
            for a, b in M:
                tot[a] += s.count(a); s = s.replace(a, b)
            if s != tok.string:
                st = offs[tok.start[0] - 1] + tok.start[1]; en = offs[tok.end[0] - 1] + tok.end[1]
                edits.append((st, en, s))
    for st, en, s in reversed(edits): src = src[:st] + s + src[en:]
    open(f, 'w', encoding='utf-8').write(src)
print(tot)
