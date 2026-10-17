"""Third subtitle row: Japanese term explanations (approved drafts in review/glossary/glossary_draft_s{1,2}.json).

Shown below the English and Japanese rows. Used by build_subs.py (series 1) and build_subs_s2.py (series 2).
Timing: starts with the first caption of the line whose JA (or EN) shows one of the explained terms (line start if
none matches); held to the end of the line, at least long enough to read (~0.13 s per character + 1 s), never past
the next explanation or the clip end.
Placement: one fixed top per explanation, 22 px below the tallest EN+JA block on screen during its span, so the row
never jumps while it is shown (top 1170 when that block has four rows).
Style: Yu Gothic Bold 36, white, black outline 3 / shadow 2 (same family and treatment as the frozen EN/JA style),
pitch 44. Each explained term starts on its own line; lines wrap at 760 px ink width (see wrap_part); at most
4 lines (bottom <= 1346, inside the sharp band that ends at 1480).
"""
import json, re
from PIL import ImageFont

EXPL_FS, EXPL_PITCH, EXPL_GAP, EXPL_MAX_LINES, MAXW = 36, 44, 22, 4, 760
TOP, PITCH = 948, 50
FONT = '/home/user/test/work/fonts/YuGothB.ttc'
BREAK_AFTER = set('、。：）」』／・')
OPEN = set('（「『')
LINE_COST = 150   # an extra line beats splitting a katakana word (300), not a kanji compound (80)


def _tokens(text):
    return re.findall(r"[A-Za-z0-9'’.&\-]+|\S| ", text)


def _cls(ch):
    o = ord(ch[0])
    if 0x3040 <= o <= 0x309F: return 'h'
    if 0x30A0 <= o <= 0x30FF: return 'k'
    if 0x4E00 <= o <= 0x9FFF: return 'K'
    if ch[0].isascii() and ch[0].isalnum(): return 'L'
    return 'p'


def _break_cost(a, b):
    """Cost of a line break between tokens a | b (lower is better; None = forbidden)."""
    if b == ' ' or b in BREAK_AFTER or a in OPEN: return None   # break after a space, never before it
    if a in BREAK_AFTER: return 0
    ca, cb = _cls(a), _cls(b)
    if ca == 'h': return 30 if cb == 'h' else 5          # after a particle / okurigana
    if ca == cb == 'k': return 300                       # inside a katakana word
    if ca == cb == 'K': return 80                        # inside a kanji compound
    if ca == cb == 'L': return 250                      # between two Latin words (names, titles): worse than an extra line
    if 'L' in (ca, cb): return 20
    return 40


def wrap_part(text, font):
    """Wrap one term's explanation at the cheapest break points (DP); every extra line costs LINE_COST.

    Latin words stay whole; breaks prefer Japanese punctuation and particle boundaries, avoid splitting katakana
    words and kanji compounds, never put closing punctuation at a line start, and avoid a short orphan last line.
    """
    toks = [t for t in _tokens(text)]
    n = len(toks)
    width = lambda i, j: font.getlength(''.join(toks[i:j]).strip())
    INF = (10 ** 9, float('inf'), None)
    best = [INF] * (n + 1); best[0] = (0, 0.0, None)
    for j in range(1, n + 1):
        for i in range(j):
            if best[i][0] >= 10 ** 9: continue
            w = width(i, j)
            if w > MAXW and j - i > 1: continue
            if i > 0:
                c = _break_cost(toks[i - 2] if toks[i - 1] == ' ' and i > 1 else toks[i - 1], toks[i])
                if c is None: continue
            else:
                c = 0
            cost = best[i][1] + c + (LINE_COST if i > 0 else 0)
            if j < n: cost += ((MAXW - w) / 100) ** 2          # raggedness of a non-last line
            elif i > 0 and w < 0.35 * MAXW: cost += (0.35 * MAXW - w) / 3   # short orphan last line
            cand = (best[i][0] + 1, cost, i)
            if cand[1] < best[j][1]: best[j] = cand
    cuts, j = [], n
    while j > 0:
        i = best[j][2]; cuts.append((i, j)); j = i
    return [''.join(toks[i:j]).strip() for i, j in reversed(cuts) if ''.join(toks[i:j]).strip()]


def wrap_expl(text, font):
    out = []
    for part in text.split('／'):
        out += wrap_part(part, font)
    return out


def _terms(text):
    names = []
    for part in text.split('／'):
        name = part.split('：')[0]
        names += [n for n in re.split(r'[・、]', re.sub(r'[『』「」]', '', name)) if n]
    return [n.lower() for n in names]


def expl_events(captions, glossary_path, clip_id, total):
    """Return [(start, end, top_y, [lines])] for this clip's explained lines, in time order."""
    font = ImageFont.truetype(FONT, EXPL_FS, index=0)
    gl = json.load(open(glossary_path, encoding='utf-8'))
    by_line = {}
    for c in captions:
        by_line.setdefault(c['line_id'], []).append(c)
    events = []
    for line_id, caps in by_line.items():
        text = gl.get(line_id)
        if not text:
            continue
        lines = wrap_expl(text, font)
        assert len(lines) <= EXPL_MAX_LINES, (clip_id, line_id, lines)
        terms = _terms(text)
        hit = next((c for c in caps if any(t in (''.join(c['jp']) + ' ' + c['en_unmasked']).lower() for t in terms)), caps[0])
        st = hit['start']
        en = max(max(c['end'] for c in caps), st + 1.0 + 0.13 * len(text))
        events.append([st, min(en, total), lines])
    events.sort(key=lambda e: e[0])
    for a, b in zip(events, events[1:]):
        a[1] = min(a[1], b[0] - 0.02)   # never show two explanations at once
    out = []
    for st, en, lines in events:
        rows = max([len(c['en']) + len(c['jp']) for c in captions if c['start'] < en and c['end'] > st] or [0])
        out.append((st, en, TOP + PITCH * rows + EXPL_GAP, lines))
    return out
