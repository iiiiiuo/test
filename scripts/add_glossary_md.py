"""Add draft Japanese term explanations (review/glossary/glossary_draft_*.json) to the Notes column of translations_review.md.
Idempotent: an existing 【解説（草案）】 entry is replaced. Explanations are a draft for a third subtitle row under EN + JA."""
import json, re, sys
HEAD = ('- **【解説（草案）】** は、字幕に出てくる用語の日本語解説の草案です（Notes欄の先頭）。確認後、動画では英語字幕・日本語字幕の下に3段目の字幕として表示する予定です。'
        '各クリップで初めて出てくる用語にだけ付けています。原本: `review/glossary/{g}`')
for md, g in [('review/translations_review.md', 'glossary_draft_s1.json'), ('review/s2/translations_review.md', 'glossary_draft_s2.json')]:
    gl = json.load(open(f'review/glossary/{g}'))
    out, n = [], 0
    for line in open(md).read().split('\n'):
        m = re.match(r'\| (?:⚠ )?(Clip_\d+_L\d+) \|', line)
        if m:
            cells = line.split(' | ')
            last = cells[-1].rstrip(' |')
            last = re.sub(r'^【解説（草案）】[^<]*(<br>)?', '', last)
            if m.group(1) in gl:
                last = f"【解説（草案）】{gl[m.group(1)]}" + (f"<br>{last}" if last else ''); n += 1
            line = ' | '.join(cells[:-1] + [last]) + ' |'
        out.append(line)
    t = '\n'.join(out)
    t = re.sub(r'\n- \*\*【解説（草案）】\*\*[^\n]*', '', t)
    i = t.index('\n\n## ')
    t = t[:i] + '\n' + HEAD.format(g=g) + t[i:]
    open(md, 'w').write(t); print(md, n, 'explanations')
