"""Third subtitle row: Japanese term explanations (approved draft in review/glossary/glossary_draft_s{1,2}.json).

Shown below the English and Japanese rows for the whole time span of the line that first uses the term.
Used by build_subs.py (series 1) and build_subs_s2.py (series 2).
Style: Yu Gothic Bold, white, black outline and shadow, 36 pt, pitch 44, top 1170 (below the four-row EN+JA block
which ends at 1148). Wrapped to at most 3 lines of 760 px rendered ink width, measured with the same font.
"""
import json, re
from PIL import ImageFont

EXPL_FS, EXPL_PITCH, EXPL_TOP, EXPL_MAX_LINES, MAXW = 36, 44, 1170, 3, 760


def wrap_expl(text, font):
    """Greedy wrap: Latin words stay whole (joined by one space), Japanese breaks between any two characters."""
    lines, cur = [], ''
    for t in re.findall(r"[A-Za-z0-9'’.&\-]+|\S", text):
        sep = ' ' if cur and t[0].isalnum() and t[0].isascii() and cur[-1].isalnum() and cur[-1].isascii() else ''
        cand = cur + sep + t
        if cur and font.getlength(cand) > MAXW:
            lines.append(cur); cur = t
        else:
            cur = cand
    if cur:
        lines.append(cur)
    return lines


def expl_events(captions, glossary_path, clip_id):
    """Return [(start, end, [lines])] for the lines of this clip that have an explanation, in time order."""
    font = ImageFont.truetype('/home/user/test/work/fonts/YuGothB.ttc', EXPL_FS, index=0)
    gl = json.load(open(glossary_path, encoding='utf-8'))
    spans = {}
    for c in captions:
        s = spans.setdefault(c['line_id'], [c['start'], c['end']])
        s[0] = min(s[0], c['start']); s[1] = max(s[1], c['end'])
    events = []
    for line_id, (st, en) in sorted(spans.items(), key=lambda kv: kv[1][0]):
        text = gl.get(line_id)
        if not text:
            continue
        lines = wrap_expl(text, font)
        assert len(lines) <= EXPL_MAX_LINES, (clip_id, line_id, lines)
        events.append([st, en, lines])
    for a, b in zip(events, events[1:]):
        a[1] = min(a[1], b[0])   # never show two explanations at once
    return [tuple(e) for e in events]
