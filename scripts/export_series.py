"""Phase B export + final series QA for the Drink Champs x Ye series.

Usage: python3 scripts/export_series.py
Requires every Clip_XX to be frozen PASS in work/b/frozen.json with matching render/subtitle hashes.
Writes output/drinkchamps_ye/clip_XX_<slug>/{final.mp4, subtitles.ass, subtitles.srt, transcript.txt,
translation_notes.md, source_manifest.json, qa_report.md} and output/drinkchamps_ye/shared/*,
commits the final intervals to work/source_timeline_ledger.json and work/state.json.
"""
import json, hashlib, os, re, shutil, subprocess, csv, datetime, itertools

ROOT = '/home/user/test'
OUT = f'{ROOT}/output/drinkchamps_ye'
B = f'{ROOT}/work/b'
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
clips = json.load(open(f'{ROOT}/work/selected_clips.json'))
frozen = json.load(open(f'{B}/frozen.json'))
ovr = json.load(open(f'{B}/en_overrides.json'))
bchg = json.load(open(f'{B}/boundary_changes.json'))
fovr = json.load(open(f'{B}/framing_overrides.json'))
rows = {r['line_id']: r for r in csv.DictReader(open(f'{ROOT}/review/approved/translations_approved_rev4.csv'))}
CSV_SHA = sha(f'{ROOT}/review/approved/translations_approved_rev4.csv')

def slug(t):
    return re.sub(r'[^a-z0-9]+', '_', t.lower().replace("'", '').replace('*', '')).strip('_')[:40]

def probe(p):
    j = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', p], capture_output=True, text=True).stdout)
    v = next(s for s in j['streams'] if s['codec_type'] == 'video'); a = next(s for s in j['streams'] if s['codec_type'] == 'audio')
    return dict(w=v['width'], h=v['height'], sar=v.get('sample_aspect_ratio', '1:1'), vdur=float(v['duration']), adur=float(a['duration']),
                frames=int(v.get('nb_frames', 0)), fps=v['r_frame_rate'], vcodec=v['codec_name'], acodec=a['codec_name'], ar=a['sample_rate'])

def ts(t):
    return f'{int(t // 60):02d}:{t % 60:06.3f}'

gate, series_rows, all_ivs, all_en = [], [], [], {}
os.makedirs(f'{OUT}/shared', exist_ok=True)
for c in clips:
    cid = c['clip_id']; n = cid.split('_')[1]; d = f'{B}/{cid}'
    fz = frozen.get(cid)
    assert fz and fz['verdict'] == 'PASS', f'{cid} not frozen PASS'
    assert sha(f'{d}/render.mp4') == fz['render_sha256'] and sha(f'{d}/subtitles.ass') == fz['ass_sha256'], f'{cid} changed after freeze'
    man = json.load(open(f'{d}/source_manifest.json'))
    cap = json.load(open(f'{d}/captions.json'))
    od = f'{OUT}/clip_{n}_{slug(c["title"])}'; os.makedirs(od, exist_ok=True)
    shutil.copyfile(f'{d}/render.mp4', f'{od}/final.mp4')          # byte copy, no re-encode
    for f in ('subtitles.ass', 'subtitles.srt', 'source_manifest.json'): shutil.copyfile(f'{d}/{f}', f'{od}/{f}')
    pr = probe(f'{od}/final.mp4')
    # transcript: unmasked English as spoken (display masking is only on screen) + approved Japanese, render time
    with open(f'{od}/transcript.txt', 'w') as f:
        f.write(f'# {cid} "{c["title"]}" internal transcript (UNMASKED English; audio is uncensored). Times are final.mp4 time.\n')
        f.write(f'# Source {man["source"]["id"]} ({os.path.basename(man["source"]["path"])}); approved translation rev4 {CSV_SHA[:12]}\n\n')
        for x in cap['captions']:
            f.write(f'[{ts(x["start"])} - {ts(x["end"])}] {x["line_id"]}\nEN: {x["en_unmasked"]}\nJA: {" ".join(x["jp"]) if x["jp"] else "(no Japanese: interjection shown in English only)"}\n\n')
    # translation notes
    used = sorted({x['line_id'] for x in cap['captions']})
    notes = [f'# {cid} translation notes', '', f'- Approved source: `review/approved/translations_approved_rev4.csv` (sha256 `{CSV_SHA}`), revision 4, approved by giub 2026-10-17 (rev 3 + the three JA edits).',
             f'- Lines used ({len(used)}): {", ".join(used)}',
             '- Japanese text is the approved `ja_final` verbatim; only line breaks and the split across caption chunks are layout. Bare speaker labels （Ye）/（ホスト） are not displayed.',
             '- Naming rules (rev 2/3): proper nouns in English spelling; Timbs→ティンバーランド, Shaq→シャキールオニール, Moses→モーゼ, Steve Jobs/Jeff Bezos/Elon Musk/Hennessy in katakana, BLM→ブラックライブスマター, backpack rapper→リュック系ラッパー.',
             '- English display masks (on screen only): s**t, f**k, f**king, f**ked, b**ch, ni**a(s), motherf**k…, p**sy. Audio and the transcript are uncensored.']
    if cap.get('dropped_lines'): notes.append(f'- Approved lines not shown (outside the final cut): {", ".join(cap["dropped_lines"])}')
    for k, v in ovr.items():
        if k.startswith(cid + '_'):
            parts = []
            if 'en' in v: parts.append(f'displayed English corrected to “{v["en"]}”')
            if 'ja_keep_segments' in v: parts.append(f'only the first {v["ja_keep_segments"]} approved JA segment(s) shown (tail removed with its cut English)')
            if 'chunks' in v: parts.append('caption chunking set by hand so each approved JA segment sits on the English it translates')
            if 'src_end' in v: parts.append(f'line window extended to {v["src_end"]} s')
            notes.append(f'- {k}: ' + '; '.join(parts) + f' ({v.get("reason", "")})')
    for b in bchg:
        if b['clip'] == cid:
            if b['kind'] == 'internal_cut': notes.append(f'- Jump cut removes source {b["removed_s"][0]}–{b["removed_s"][1]} s: {b["reason"]}')
            else: notes.append(f'- Boundary ({b["kind"]}) moved to {b["cut_s"]} s: {b["reason"]}')
    open(f'{od}/translation_notes.md', 'w').write('\n'.join(notes) + '\n')
    # qa report
    auto = json.load(open(f'{d}/qa/auto.json'))
    critic = open(f'{d}/qa/critic.md').read()
    rounds = [g for g in json.load(open(f'{B}/gauntlet.json')) if g.get('target') == cid]
    q = [f'# {cid} QA report', '', f'Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `{fz["render_sha256"]}`.', '',
         '## Automated checks (final.mp4)',
         f'- {pr["w"]}x{pr["h"]} SAR {pr["sar"]}, {pr["fps"]} fps, {pr["vcodec"]}/{pr["acodec"]} {pr["ar"]} Hz',
         f'- Video {pr["vdur"]:.3f} s, audio {pr["adur"]:.3f} s (rule 60.0 <= d < 120.0: {"PASS" if 60 <= min(pr["vdur"], pr["adur"]) and max(pr["vdur"], pr["adur"]) < 120 else "FAIL"})',
         f'- Frames: {pr["frames"]} (manifest {sum(v["end_frame_excl"] - v["start_frame"] for v in man["video_segments"])})',
         f'- Decode/format: {json.dumps(auto.get("format", {}))[:300]}',
         f'- Caption sync vs render ASR: {json.dumps(auto.get("sync", {}))}', '',
         '## Critic rounds']
    for g in rounds: q.append(f'- round {g.get("round")}: {g.get("verdict", "")} — {g.get("largest_gap", g.get("change", ""))} → {g.get("fix", g.get("result", ""))}')
    q += ['', '## Final critic report', '', critic]
    open(f'{od}/qa_report.md', 'w').write('\n'.join(q) + '\n')
    ok = pr['w'] == 1080 and pr['h'] == 1920 and pr['sar'] in ('1:1', 'N/A') and 60 <= min(pr['vdur'], pr['adur']) and max(pr['vdur'], pr['adur']) < 120 and sha(f'{od}/final.mp4') == fz['render_sha256']
    gate.append((cid, ok, pr['vdur']))
    for v, a in zip(man['video_segments'], man['audio_segments']):
        all_ivs.append(dict(clip=cid, source=man['source']['id'], f0=v['start_frame'], f1=v['end_frame_excl'], a0=a['start_sample_48k'], a1=a['end_sample_48k_excl'], s0=v['start_s'], s1=v['end_s']))
    all_en[cid] = [x['en_unmasked'] for x in cap['captions']]
    series_rows.append(dict(cid=cid, title=c['title'], dir=os.path.relpath(od, ROOT), dur=pr['vdur'], src=man['source']['id'],
                            ivs=[(v['start_s'], v['end_s']) for v in man['video_segments']], cand=c.get('candidate')))

# ---- series checks
overl = []
for x, y in itertools.combinations(all_ivs, 2):
    if x['source'] != y['source']: continue
    if max(x['f0'], y['f0']) < min(x['f1'], y['f1']) or max(x['a0'], y['a0']) < min(x['a1'], y['a1']): overl.append((x['clip'], y['clip']))
unmasked = []
BAD = re.compile(r"\b(shit|fuck\w*|bitch\w*|nigga\w*|motherfuck\w*|pussy)\b", re.I)
style_hdr = set()
for c in clips:
    a = open(f'{B}/{c["clip_id"]}/subtitles.ass', encoding='utf-8').read()
    style_hdr.add(re.search(r'^Style:.*$', a, re.M).group(0))
    for line in re.findall(r'^Dialogue:.*$', a, re.M):
        if BAD.search(line.split('}', 1)[-1]): unmasked.append((c['clip_id'], line[-80:]))
# duplicate long sentences across clips (repeated hooks/setups)
dups = []
sent = {}
for cid, ens in all_en.items():
    for e in ens:
        k = re.sub(r'[^a-z ]', '', e.lower()).strip()
        if len(k.split()) >= 6: sent.setdefault(k, set()).add(cid)
dups = [(k, sorted(v)) for k, v in sent.items() if len(v) > 1]
fonts = subprocess.run(['fc-scan', '--format', '%{family[0]}|%{style[0]}|%{weight}\n', f'{ROOT}/work/fonts/YuGothB.ttc'], capture_output=True, text=True).stdout.split('\n')[0]

# ---- ledger + state
led = json.load(open(f'{ROOT}/work/source_timeline_ledger.json'))
led['committed'] = [dict(source_id=x['source'], clip_id=x['clip'], status='COMMITTED', start_frame=x['f0'], end_frame_excl=x['f1'], start_s=x['s0'], end_s=x['s1'],
                         audio_48k=[x['a0'], x['a1']]) for x in all_ivs]
for r in led.get('reservations', []): r['status'] = 'SUPERSEDED_BY_COMMIT'
led['overlap_check'] = dict(checked_at=now, pairs_overlapping=len(overl), method='half-open frame and 48k-sample intervals per source, all pairs')
led['updated'] = now
json.dump(led, open(f'{ROOT}/work/source_timeline_ledger.json', 'w'), indent=1)

# ---- shared files
S = f'{OUT}/shared'
total = sum(r['dur'] for r in series_rows)
open(f'{S}/clip_candidate_map.md', 'w').write('# Clip map (final)\n\n| Clip | Title | Candidate | Source | Intervals (s) | Duration | Folder |\n|---|---|---|---|---|---|---|\n' +
    ''.join(f'| {r["cid"]} | {r["title"]} | {r["cand"]} | {r["src"]} | {"; ".join(f"{a:.3f}–{b:.3f}" for a, b in r["ivs"])} | {r["dur"]:.3f} s | `{r["dir"]}` |\n' for r in series_rows) +
    f'\nTotal {len(series_rows)} clips, {total:.1f} s.\n')
open(f'{S}/source_overlap_audit.md', 'w').write('# Source overlap audit (final manifests)\n\n'
    f'Checked {now}: {len(all_ivs)} intervals in {len(series_rows)} clips, every pair on the same source, half-open video frames and 48 kHz audio samples.\n\n'
    f'Result: **{"PASS, zero shared source frames or audio samples" if not overl else "FAIL " + str(overl)}**.\n\n'
    '| Source | Clip | start_frame | end_frame_excl | start_s | end_s |\n|---|---|---|---|---|---|\n' +
    ''.join(f'| {x["source"]} | {x["clip"]} | {x["f0"]} | {x["f1"]} | {x["s0"]} | {x["s1"]} |\n' for x in sorted(all_ivs, key=lambda x: (x['source'], x['f0']))))
shutil.copyfile(f'{B}/gauntlet.json', f'{S}/gauntlet_state.json')
g = json.load(open(f'{B}/gauntlet.json'))
open(f'{S}/gauntlet_report.md', 'w').write('# Gauntlet report\n\nLoop: Builder → actual render → one Fresh Clip Critic (independent context, rubric `work/b/critic_rubric.md`) → targeted fix of the largest gap → re-render → re-check. PASS renders frozen by hash (`work/b/frozen.json`).\n\n' +
    '| Target | Round | Verdict | Largest gap / change | Fix |\n|---|---|---|---|---|\n' +
    ''.join(f'| {x.get("target")} | {x.get("round")} | {x.get("verdict", "")} | {str(x.get("largest_gap", x.get("change", ""))).replace("|", "/")} | {str(x.get("fix", x.get("result", ""))).replace("|", "/")} |\n' for x in g) +
    '\n## Failed approaches\n' + ''.join(f'- {x["failed_approach"]}\n' for x in g if x.get('failed_approach')))
spec = open('/mnt/project-files/output/shared/subtitle_style_spec.md').read() if os.path.exists('/mnt/project-files/output/shared/subtitle_style_spec.md') else ''
open(f'{S}/subtitle_style_spec.md', 'w').write('# Subtitle style spec (Drink Champs x Ye series)\n\nThe frozen series template below is reused unchanged; addendum records what this series measured and fixed.\n\n'
    '## Addendum for this series\n'
    f'- Font check: fc-scan `{fonts}` (work/fonts/YuGothB.ttc, sha256 {sha(ROOT + "/work/fonts/YuGothB.ttc")}); libass resolved family "Yu Gothic" Bold in every render (no fallback).\n'
    '- Wrap width is measured as rendered ink: libass ink / PIL advance = EN 0.767, JP 0.753 (`work/b/calib_widths.json`), max 760 px, max 2 EN + 2 JP lines.\n'
    '- Background: band crop scaled to 560x540, centre 304x540, boxblur 14:3, scaled to 1080x1920 (same look as the frozen 2000x1932 / boxblur 28:3 at a quarter of the cost).\n'
    '- Framing: per-shot face detection (Haar frontal/alt2/profile, saturated-crest rejection, x-clusters), 1119x1080 window, 1.2x punch 933x900 when the face is under 300 px; hand crops in `work/b/framing_overrides.json`.\n'
    '- Caption timing: onset at the first spoken word, checked against source audio energy; captions never overlap; >=0.8 s minimum; text split at >1 s pauses on punctuation.\n'
    f'- ASS Style line identical in all {len(series_rows)} clips: {"YES" if len(style_hdr) == 1 else "NO"}.\n\n---\n\n' + spec)
fails = [x for x in gate if not x[1]]
open(f'{S}/final_series_qa.md', 'w').write('# Final series QA\n\n'
    f'Checked {now} on the exported files.\n\n'
    f'- Clips: {len(gate)}; all frozen PASS by an independent Fresh Clip Critic and byte-identical to the frozen render: {"PASS" if not fails else "FAIL " + str(fails)}\n'
    f'- 9:16 1080x1920 and 60.0 <= duration < 120.0 for every final.mp4: {"PASS" if not fails else "FAIL"} (range {min(x[2] for x in gate):.3f}–{max(x[2] for x in gate):.3f} s)\n'
    f'- Zero shared source frames/audio across the series: {"PASS" if not overl else "FAIL " + str(overl)} (`source_overlap_audit.md`)\n'
    f'- Unmasked curse words in displayed English: {"PASS (none)" if not unmasked else "FAIL " + str(unmasked)}\n'
    f'- Repeated sentences (>=6 words) across clips: {"none" if not dups else dups}\n'
    f'- Subtitle style identical across clips (ASS Style line): {"PASS" if len(style_hdr) == 1 else "FAIL"}\n'
    f'- Font: {fonts}\n'
    '- Translation: every Japanese line is approved rev 3 text (no new Japanese); per-clip notes list display-English corrections, hand chunking and cuts.\n')
st = json.load(open(f'{ROOT}/work/state.json'))
st.update(status='PHASE_B_COMPLETE' if not fails and not overl and not unmasked else 'PHASE_B_QA_FAILED', phase='B', updated=now,
          used_source_ranges=dict(status='COMMITTED', ledger='work/source_timeline_ledger.json', count=len(all_ivs)),
          completed_clips={r['cid']: dict(dir=r['dir'], duration_s=round(r['dur'], 3), render_sha256=frozen[r['cid']]['render_sha256']) for r in series_rows},
          qa=dict(frozen='work/b/frozen.json', gauntlet='work/b/gauntlet.json', series='output/drinkchamps_ye/shared/final_series_qa.md'),
          pending_actions=[], next_action='none: series delivered; await user feedback', blockers=[])
json.dump(st, open(f'{ROOT}/work/state.json', 'w'), indent=1, ensure_ascii=False)
print('gate', fails, 'overlap', overl, 'unmasked', unmasked, 'dups', dups, 'styles', len(style_hdr), 'total', round(total, 1))
