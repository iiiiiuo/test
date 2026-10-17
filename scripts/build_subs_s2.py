"""Build phrase-level bilingual captions (ASS + SRT) for one clip from the APPROVED translation CSV.

Usage: python3 scripts/build_subs.py Clip_XX
Inputs : work/s2/selected_clips.json, review/s2/approved/translations_approved_s2_rev2.csv, work/asr/*.json
Outputs: work/b2/<clip>/subtitles.ass, subtitles.srt, captions.json
Style  : frozen spec output/shared/subtitle_style_spec.md (Yu Gothic Bold, EN 54 / JP 50, top 948, pitch 50, width 760).
Japanese text is the approved ja_final verbatim except removal of bare speaker labels （Ye）/（ホスト）.
"""
import csv, json, re, sys, os, difflib, math
from PIL import ImageFont
sys.path.insert(0, '/home/user/test/scripts')
from expl_row import expl_events, EXPL_FS, EXPL_PITCH

ROOT = '/home/user/test'
CLIP = sys.argv[1]
APPROVED = f'{ROOT}/review/s2/approved/translations_approved_s2_rev2.csv'
FONT = f'{ROOT}/work/fonts/YuGothB.ttc'
EN_FS, JP_FS, MAXW, TOP, PITCH = 54, 50, 760, 948, 50
F_EN = ImageFont.truetype(FONT, EN_FS, index=0)
F_JP = ImageFont.truetype(FONT, JP_FS, index=0)
FPS_NUM, FPS_DEN = 24000, 1001

clips = {c['clip_id']: c for c in json.load(open(f'{ROOT}/work/s2/selected_clips.json'))}
clip = clips[CLIP]
defs = json.load(open(f'{ROOT}/work/s2/clips_def.json'))
src = json.load(open(f'{ROOT}/work/sources.json'))
rows = [r for r in csv.DictReader(open(APPROVED, encoding='utf-8-sig')) if r['clip_id'] == CLIP]
lines = {l['line_id']: l for l in clip['lines']}
sp = src[clip['source_id']]['start_pts']

def ft(f):  # source time of frame f
    return (sp + f * 1001) / 24000

# output timeline mapping (frame-exact)
segs, acc = [], 0.0
for iv in clip['intervals']:
    a, b = ft(iv['start_frame']), ft(iv['end_frame_excl'])
    segs.append((a, b, acc)); acc += b - a
TOTAL = acc

def to_out(t):
    for a, b, o in segs:
        if a - 1e-6 <= t <= b + 1e-6:
            return o + min(max(t, a), b) - a
    # between intervals: snap to nearest boundary
    best = min(segs, key=lambda s: min(abs(t - s[0]), abs(t - s[1])))
    a, b, o = best
    return o + (0 if abs(t - a) < abs(t - b) else b - a)

# ---- ASR words for timing ----
runs = defs[clip['candidate']].get('asr') or [clip['candidate']]
W = []
for r in runs:
    p = f'{ROOT}/work/asr/{r}.large.json'
    if os.path.exists(p):
        for s in json.load(open(p))['segments']:
            W += s['words']
turbo = [w for s in json.load(open(f"{ROOT}/work/asr/{clip['source_id']}.turbo.json"))['segments'] for w in s['words']]
W.sort(key=lambda w: w['s'])

import wave, numpy as np
_w = wave.open(f"{ROOT}/work/audio/{clip['source_id']}.wav"); _sr = _w.getframerate()
_x = np.frombuffer(_w.readframes(_w.getnframes()), np.int16).astype(np.float32)
def _db(t, d=0.1):
    a = max(0, int(t * _sr)); seg = _x[a:a + int(d * _sr)]
    return 20 * math.log10(float(np.sqrt(np.mean(seg ** 2))) + 1) if len(seg) else 0
# speech level of this clip's span: median of the louder half of 100 ms windows; "silent" = 8 dB below it
_span = [_db(t) for a, b, _ in segs for t in np.arange(a, b, 0.1)]
SPEECH_DB = float(np.median(sorted(_span)[len(_span) // 2:])); SIL_DB = SPEECH_DB - 8
def speech_onset(t, limit):
    """t if speech fills most of the 0.5 s after it, else the first point where speech starts (before limit)."""
    if sorted(_db(t + 0.1 * k) for k in range(1, 6))[2] >= SIL_DB: return t   # median of 100 ms windows (skips the previous word's tail)
    u = t + 0.1
    while u < limit + 0.1:
        if min(_db(u), _db(u + 0.1), _db(u + 0.2)) >= SIL_DB: return min(max(t, u - 0.05), limit)   # >=0.3 s of speech, not a blip
        u += 0.02
    return max(t, limit - 0.15)   # no clear speech before the next word: the word is spoken with it

def norm(t):
    return re.sub(r"[^a-z0-9']", '', t.lower())

# ---- masking (reference-derived, displayed English only) ----
MASK = [(r'\bmotherfuck', 'motherf**k'), (r'\bfucking\b', 'f**king'), (r'\bfuckin\b', 'f**kin'), (r'\bfucked\b', 'f**ked'),
        (r'\bfuck', 'f**k'), (r'\bshit', 's**t'), (r'\bbitch', 'b**ch'), (r'\bniggas\b', 'ni**as'), (r'\bnigga\b', 'ni**a'),
        (r'\bpussy\b', 'p**sy')]
def mask(t):
    for a, b in MASK:
        t = re.sub(a, lambda m: (b[0].upper() + b[1:]) if m.group(0)[0].isupper() else b, t, flags=re.I)
    return t

def clean_en(en, ja):
    """Remove speaker labels; keep a host interjection only if the Japanese translates it (parenthetical present)."""
    keep_paren = '（' in ja and not re.search(r'（(Ye|ホスト)）', ja)
    def rep(m):
        inner = m.group(1).strip()
        mm = re.match(r'^(Ye|Host):\s*(.*)$', inner)
        if mm:
            body = mm.group(2)
            if not body:
                return ' | '
            return f' | {body} | ' if keep_paren else ' '
        return m.group(0)
    en = re.sub(r'\(([^)]*)\)', rep, en)
    en = re.sub(r'\s+—\s+', ' | ', en)
    en = re.sub(r'\s+', ' ', en).replace('| |', '|').strip(' |')
    return en

def clean_ja(ja):
    return [s for s in (re.sub(r'^（(Ye|ホスト)）', '', x).strip() for x in ja.split('\n')) if s]

# libass ink width / PIL advance width, measured on the actual render (work/b2/calib_widths.json)
EN_K, JP_K = 0.767, 0.753
def wen(t): return F_EN.getlength(t) * EN_K
def wjp(t): return F_JP.getlength(t) * JP_K

def is_name_join(a, b):
    """True when a break between tokens a|b would split a capitalised name such as 'Kool | G Rap'."""
    return bool(re.match(r"^[A-Z0-9]", a)) and bool(re.match(r"^[A-Z0-9]", b)) and a not in ('I',) and not re.search(r'[,.?!;:]$', a)

def wrap_en(tokens):
    """One line if it fits; else the most balanced 2-line split, preferring punctuation, never splitting names."""
    if wen(' '.join(tokens)) <= MAXW or len(tokens) == 1: return [' '.join(tokens)]
    best = None
    for i in range(1, len(tokens)):
        a, b = ' '.join(tokens[:i]), ' '.join(tokens[i:])
        wa, wb = wen(a), wen(b)
        if max(wa, wb) > MAXW: continue
        score = abs(wa - wb) + (400 if is_name_join(tokens[i - 1], tokens[i]) else 0) - (120 if re.search(r'[,.?!;:]$', tokens[i - 1]) else 0) \
                + (150 if len(tokens) - i == 1 or i == 1 else 0)
        if best is None or score < best[0]: best = (score, i)
    if best is None:  # cannot fit in 2 lines
        lines, cur = [], []
        for tk in tokens:
            if cur and wen(' '.join(cur + [tk])) > MAXW: lines.append(' '.join(cur)); cur = [tk]
            else: cur.append(tk)
        return lines + [' '.join(cur)]
    i = best[1]
    return [' '.join(tokens[:i]), ' '.join(tokens[i:])]

BREAK_AFTER = set('はがをにでともてらし、。？！」』')
NO_START = set('ぁぃぅぇぉっゃゅょゎァィゥェォッャュョー、。？！）」』”')
def wrap_jp_seg(s):
    if wjp(s) <= MAXW: return [s]
    best = None
    for i in range(2, len(s) - 1):
        if s[i] in NO_START: continue
        a, b = s[:i], s[i:]
        if wjp(a) > MAXW: break
        score = abs(wjp(a) - wjp(b)) - (60 if s[i - 1] in BREAK_AFTER else 0)
        if best is None or score < best[0]: best = (score, i)
    i = best[1] if best else len(s) // 2
    return wrap_jp_seg(s[:i]) + wrap_jp_seg(s[i:])

def jp_lines(segs_):
    """Pack JP phrase segments into display lines (join adjacent short segments when they fit)."""
    out = []
    for s in segs_:
        for piece in wrap_jp_seg(s):
            if out and wjp(out[-1] + '　' + piece) <= MAXW and len(segs_) > 2:
                out[-1] = out[-1] + '　' + piece
            else:
                out.append(piece)
    return out

def time_tokens(tokens, t0, t1):
    """Assign onset times to display tokens by aligning to ASR words in [t0,t1]."""
    a = [norm(t) for t in tokens]
    # primary ASR pass = the one whose words match more of the line (large-v3 by default; turbo when it hears more)
    nm = lambda L: sum(bl.size for bl in difflib.SequenceMatcher(None, a, [norm(w['w']) for w in L], autojunk=False).get_matching_blocks())
    wl = [w for w in W if t0 - 0.3 <= w['s'] <= t1 + 0.1]; wt = [w for w in turbo if t0 - 0.3 <= w['s'] <= t1 + 0.1]
    ws = wt if nm(wt) > nm(wl) + 1 else wl
    b = [norm(w['w']) for w in ws]
    times = [None] * len(tokens); ends = [None] * len(tokens)
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            times[blk.a + k] = ws[blk.b + k]['s']; ends[blk.a + k] = ws[blk.b + k]['e']
    # interpolate missing onsets by character position
    known = [(i, t) for i, t in enumerate(times) if t is not None]
    pts = [(-1, t0)] + known + [(len(tokens), t1)]
    for i in range(len(tokens)):
        if times[i] is None:
            lo = max(p for p in pts if p[0] < i); hi = min(p for p in pts if p[0] > i)
            times[i] = lo[1] + (hi[1] - lo[1]) * (i - lo[0]) / (hi[0] - lo[0])
    # The two ASR passes sometimes disagree; for a word that occurs once in the line and matched in both, a disagreement
    # >0.8 s takes the later onset (critic Clip_04: large-v3 put "Bad Bunny" 1.8 s early; turbo matched the audio).
    ws2 = [w for w in (turbo if ws and ws[0] in W else W) if t0 - 0.3 <= w['s'] <= t1 + 0.1]
    for blk in difflib.SequenceMatcher(None, a, [norm(w['w']) for w in ws2], autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            i2 = blk.a + k
            if times[i2] is not None and a.count(a[i2]) == 1 and 0.8 < ws2[blk.b + k]['s'] - times[i2] < 3.0:
                times[i2] = ws2[blk.b + k]['s']
    # A word (no trailing punctuation) whose next ASR word starts >0.8 s later had its onset glued to the previous
    # word's end (critic Clip_02 L014: laughter in the gap defeats the energy check): move it just before the next word.
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            jb = blk.b + k
            if jb + 1 < len(ws) and ws[jb + 1]['s'] - ws[jb]['s'] > 0.8 and not re.search(r'[,.?!;:…]$', tokens[blk.a + k]):
                times[blk.a + k] = max(ws[jb]['s'], ws[jb + 1]['s'] - 0.12 - 0.07 * len(a[blk.a + k]))
    # Whisper sometimes glues a word's onset to the previous word's end (critic Clip_06: "I like both" 2.4 s early).
    # Check the source audio: an onset followed by silence moves to where speech actually resumes (before the next word).
    # Unmatched (interpolated or clamped-to-line-start) onsets get the same check.
    for i in range(len(times)):
        nxt = next((times[k] for k in range(i + 1, len(times)) if times[k] > times[i] + 0.3), min(times[i] + 3, t1))
        times[i] = speech_onset(times[i], nxt)
    for i in range(1, len(times)):
        times[i] = max(times[i], times[i - 1])
    times = [min(max(t, t0), t1) for t in times]
    last_end = max([e for e in ends if e is not None] or [t1])
    global FIRST_MATCHED; FIRST_MATCHED = ends[0] is not None
    # speech heard (either ASR) before the matched first word means the line starts earlier: begin there
    # (only words after the previous line's last matched word: earlier ones belong to that line, critic Clip_06)
    pre = [w['s'] for w in W + turbo if max(t0 - 0.3, PREV_END) <= w['s'] < times[0] - 0.3 and norm(w['w']) not in a[:2]]
    if pre:
        times[0] = speech_onset(max(min(pre), t0 - 0.3), times[0] + 0.3)
        FIRST_MATCHED = True
    global ENDS; ENDS = ends
    global PREV_END; PREV_END = max([PREV_END] + [e - 0.05 for e in ends if e is not None])
    return times, min(max(last_end, times[-1]), t1 + 0.3)

PREV_END = -1e9

def best_split(n_tokens, widths, k, forced, soft):
    """DP: split token sequence into k contiguous chunks, balanced width, preferring punctuation, honouring forced breaks."""
    total = sum(widths); target = total / k
    pre = [0]
    for w in widths: pre.append(pre[-1] + w)
    INF = float('inf')
    dp = [[INF] * (n_tokens + 1) for _ in range(k + 1)]; bk = [[0] * (n_tokens + 1) for _ in range(k + 1)]
    dp[0][0] = 0
    for j in range(1, k + 1):
        for e in range(1, n_tokens + 1):
            for s in range(j - 1, e):
                if dp[j - 1][s] == INF: continue
                if any(f for f in forced if s < f < e): continue  # forced break inside chunk
                w = pre[e] - pre[s]
                c = dp[j - 1][s] + ((w - target) / target) ** 2
                if e < n_tokens:
                    c += 0 if e in forced else (0.15 if e in soft else 0.9)
                    if 0 < e < n_tokens and is_name_join(TOK[e - 1], TOK[e]): c += 3
                if c < dp[j][e]: dp[j][e] = c; bk[j][e] = s
    if dp[k][n_tokens] == INF: return None
    cuts, e = [], n_tokens
    for j in range(k, 0, -1):
        s = bk[j][e]; cuts.append((s, e)); e = s
    return cuts[::-1]

# English transcript corrections found in Phase B QA (display English only; approved Japanese unchanged)
_ovp = f'{ROOT}/work/b2/en_overrides.json'
EN_OVR = {k: v['en'] for k, v in json.load(open(_ovp)).items() if 'en' in v} if os.path.exists(_ovp) else {}
OVR = json.load(open(_ovp)) if os.path.exists(_ovp) else {}
CHUNKS = {k: v['chunks'] for k, v in json.load(open(_ovp)).items() if 'chunks' in v} if os.path.exists(_ovp) else {}
JA_KEEP = {k: v['ja_keep_segments'] for k, v in json.load(open(_ovp)).items() if 'ja_keep_segments' in v} if os.path.exists(_ovp) else {}
captions = []
dropped = []
for r in rows:
    l = lines[r['line_id']]
    if 'src_end' in OVR.get(r['line_id'], {}): l = dict(l, end=OVR[r['line_id']]['src_end'])   # line window extended to cover added display words
    ov = sum(max(0, min(l['end'], b) - max(l['start'], a)) for a, b, _ in segs)
    if ov < 0.3 * max(0.01, l['end'] - l['start']):
        dropped.append(r['line_id']); continue   # line removed by an editorial cut (outside all used intervals)
    en = clean_en(EN_OVR.get(r['line_id'], r['original_en']), r['ja_final'])
    ja = clean_ja(r['ja_final'])
    if r['line_id'] in JA_KEEP: ja = ja[:JA_KEEP[r['line_id']]]   # approved segments only; tail dropped with its cut English
    parts = en.split(' | ')
    tokens, forced = [], set()
    for p in parts:
        if tokens: forced.add(len(tokens))
        tokens += p.split()
    soft = {i + 1 for i, t in enumerate(tokens) if re.search(r'[,.?!;:…]$', t) or t.endswith('...')}
    times, tend = time_tokens(tokens, l['start'], l['end'])
    # est. spoken end of each token: ASR end, but never more than a typical word length after its onset
    est_end = lambda k: min(ENDS[k] if ENDS[k] is not None else times[k] + 9, times[k] + 0.15 + 0.08 * len(norm(tokens[k])))
    # a pause of >1.0 s inside a line is a forced chunk break, so text is not shown seconds before it is spoken;
    # the break snaps to the nearest punctuation boundary within two tokens (critics Clip_04 "Stadium. Bad Bunny", Clip_05)
    for k in range(1, len(tokens)):
        if times[k] - est_end(k - 1) > 1.0:
            cand = [b for b in range(max(1, k - 2), min(len(tokens), k + 2)) if b in soft]
            if cand:
                b = min(cand, key=lambda b: abs(b - k))
                # no fragment captions: each side of the break keeps at least 3 words
                if all(abs(b - f) >= 3 for f in forced | {0, len(tokens)}) or re.search(r'[.?!]$', tokens[b - 1]): forced.add(b)
    widths = [wen(t + ' ') for t in tokens]
    global TOK; TOK = tokens
    jw = [wjp(s) for s in ja]
    if r['line_id'] in CHUNKS:
        # hand-checked EN chunking with the approved JP segments placed on the chunk where they are spoken
        # (critics 10/15/18/19/20: width-based JP distribution put JP on the wrong moment); [] = EN-only interjection
        spec = CHUNKS[r['line_id']]; assert sum(n for n, _ in spec) == len(tokens), (r['line_id'], tokens)
        cuts, s0 = [], 0
        for n, _ in spec: cuts.append((s0, s0 + n)); s0 += n
        groups = [[ja[i] for i in idx] for _, idx in spec]
        for (s_, e_), g_ in zip(cuts, groups):
            assert len(wrap_en(tokens[s_:e_])) <= 2 and len(jp_lines(g_)) <= 2, (r['line_id'], tokens[s_:e_], g_)
    else:
     k = max(len(parts), math.ceil(sum(widths) / (MAXW * 1.75)), 1)
     while True:
         cuts = best_split(len(tokens), widths, k, forced, soft)
         if cuts is None: k += 1; continue
         # distribute JP segments monotonically by matching cumulative fractions
         enfr = [(pre := sum(widths[:e])) / sum(widths) for s, e in cuts]
         m = len(ja); groups = [[] for _ in cuts]
         cum = 0
         for i, s in enumerate(ja):
             mid = (cum + jw[i] / 2) / sum(jw); cum += jw[i]
             gi = next(j for j, f in enumerate(enfr) if mid <= f + 1e-9)
             groups[gi].append(s)
         # ensure no empty JP group when enough segments: borrow from neighbours
         for gi in range(len(groups)):
             if not groups[gi]:
                 if gi > 0 and len(groups[gi - 1]) > 1: groups[gi].insert(0, groups[gi - 1].pop())
                 elif gi + 1 < len(groups) and len(groups[gi + 1]) > 1: groups[gi].append(groups[gi + 1].pop(0))
         ok = True
         for (s, e), g in zip(cuts, groups):
             if len(wrap_en(tokens[s:e])) > 2 or len(jp_lines(g)) > 2: ok = False
         if ok or k >= len(tokens): break
         k += 1
     # inherit JP for empty groups (JP phrase spans two EN chunks)
     for gi in range(len(groups)):
         if not groups[gi] and gi > 0: groups[gi] = list(groups[gi - 1])
     for gi in range(len(groups) - 1, -1, -1):
         if not groups[gi] and gi + 1 < len(groups): groups[gi] = list(groups[gi + 1])
    for ci, ((s, e), g) in enumerate(zip(cuts, groups)):
        st = times[s]   # first-token onsets are energy-checked in time_tokens (critic Clip_05: line start was 2.5 s early)
        en_ = times[cuts[ci + 1][0]] if ci + 1 < len(cuts) else tend
        if ci + 1 < len(cuts) and ENDS[e - 1] is not None:
            en_ = min(en_, max(ENDS[e - 1] + 0.2, st + 0.3))   # don't hold a chunk over a long pause before the next one
        captions.append(dict(line_id=r['line_id'], src_start=st, src_end=en_,
                             en=wrap_en([mask(t) for t in tokens[s:e]]), en_unmasked=' '.join(tokens[s:e]), jp=jp_lines(g) if g else []))

# a fragment (<=2 words shown <0.6 s) merges into the next caption of the same line when it shares its Japanese
# or the previous one's (critic Clip_03 "yeah," 0.28 s)
i = 0
while i + 1 < len(captions):
    c, n = captions[i], captions[i + 1]
    short = to_out(n['src_start']) - to_out(c['src_start']) < 0.6 and len(c['en_unmasked'].split()) <= 2
    no_own_jp = i > 0 and c['jp'] == captions[i - 1]['jp']   # its Japanese is only inherited, so nothing is lost
    toks = (c['en_unmasked'] + ' ' + n['en_unmasked']).split()
    if short and ((c['line_id'] == n['line_id'] and c['jp'] == n['jp']) or no_own_jp) and len(wrap_en(toks)) <= 2:
        n.update(src_start=c['src_start'], en_unmasked=' '.join(toks), en=wrap_en([mask(t) for t in toks]))
        del captions[i]; continue
    i += 1

# output timing: onset at first word, hold <=0.5 s after, never overlapping next, min 0.8 s
for c in captions:
    c['start'] = to_out(c['src_start']); c['end'] = to_out(c['src_end']) + 0.5
for i, c in enumerate(captions):
    nxt = captions[i + 1]['start'] if i + 1 < len(captions) else TOTAL
    c['end'] = min(c['end'], nxt - 0.02, TOTAL)
    if c['end'] - c['start'] < 0.8:
        c['end'] = min(c['start'] + 0.8, nxt - 0.02, TOTAL)
    # close tiny gaps (<0.3 s) to avoid flicker
    if nxt - c['end'] < 0.3 and i + 1 < len(captions): c['end'] = nxt - 0.02
    c['start'] = max(c['start'], 0.0)
assert all(c['end'] > c['start'] for c in captions), [c for c in captions if c['end'] <= c['start']]

def ass_t(t):
    cs = int(round(t * 100)); h, cs = divmod(cs, 360000); m, cs = divmod(cs, 6000); s, cs = divmod(cs, 100)
    return f'{h}:{m:02d}:{s:02d}.{cs:02d}'
def srt_t(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'

out = os.environ.get('SUBS_OUT', f'{ROOT}/work/b2/{CLIP}'); os.makedirs(out, exist_ok=True)
ass = ['[Script Info]', 'ScriptType: v4.00+', 'PlayResX: 1080', 'PlayResY: 1920', 'WrapStyle: 2', 'ScaledBorderAndShadow: yes', '',
       '[V4+ Styles]',
       'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',
       'Style: Sub,Yu Gothic,50,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,2,8,60,60,950,1', '',
       'Style: Expl,Yu Gothic,36,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,2,8,60,60,950,1', '',
       '[Events]', 'Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
srt = []
blocks = []   # (start, srt text) for captions and explanations, written in time order
for c in captions:
    y = TOP
    for t in c['en']:
        ass.append(f"Dialogue: 0,{ass_t(c['start'])},{ass_t(c['end'])},Sub,,0,0,0,,{{\\an8\\pos(540,{y})\\fs{EN_FS}}}{t}"); y += PITCH
    for t in c['jp']:
        ass.append(f"Dialogue: 0,{ass_t(c['start'])},{ass_t(c['end'])},Sub,,0,0,0,,{{\\an8\\pos(540,{y})\\fs{JP_FS}}}{t}"); y += PITCH
    blocks.append((c['start'], [f"{srt_t(c['start'])} --> {srt_t(c['end'])}", *c['en'], *c['jp'], '']))
# third row: approved Japanese term explanation under the EN + JA block (see scripts/expl_row.py)
for st, en_, y, lines in expl_events(captions, f'{ROOT}/review/glossary/glossary_draft_s2.json', CLIP, TOTAL):
    for t in lines:
        ass.append(f"Dialogue: 0,{ass_t(st)},{ass_t(en_)},Expl,,0,0,0,,{{\\an8\\pos(540,{y})\\fs{EXPL_FS}}}{t}"); y += EXPL_PITCH
    blocks.append((st, [f"{srt_t(st)} --> {srt_t(en_)}", *lines, '']))
for i, (_, b) in enumerate(sorted(blocks, key=lambda x: x[0]), 1):
    srt += [str(i), *b]
open(f'{out}/subtitles.ass', 'w', encoding='utf-8').write('\n'.join(ass) + '\n')
open(f'{out}/subtitles.srt', 'w', encoding='utf-8').write('\n'.join(srt))
json.dump(dict(clip=CLIP, total_s=TOTAL, segments=segs, dropped_lines=dropped, captions=captions), open(f'{out}/captions.json', 'w'), indent=1, ensure_ascii=False)
print(CLIP, 'captions', len(captions), 'total', round(TOTAL, 3), 'max EN lines', max(len(c['en']) for c in captions),
      'max JP lines', max(len(c['jp']) for c in captions), 'no-JP', sum(1 for c in captions if not c['jp']), 'dropped', dropped)
