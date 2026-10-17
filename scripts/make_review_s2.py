"""Series 2: build the Phase A human-review package from work/review_lines.json + work/s2/clips_def.json.
Outputs (repo and /mnt/project-files mirror): review/*.csv|md|json, work/source_timeline_ledger.json,
work/clip_candidates.json. Pure bookkeeping: no media is rendered."""
import json, csv, hashlib, math, os, shutil, io, datetime

ROOT = '/home/user/test'
SHARED = '/mnt/project-files'
defs = json.load(open(f'{ROOT}/work/s2/clips_def.json'))
lines = json.load(open(f'{ROOT}/work/s2/review_lines.json'))
meta = json.load(open(f'{ROOT}/work/s2/clip_meta.json'))
src = json.load(open(f'{ROOT}/work/sources.json'))

def frame_at(part, t):  # first frame whose pts >= t (CFR, pts = start_pts + i*1001, tb 1/24000)
    sp = src[part]['start_pts']
    return max(0, math.ceil((t * 24000 - sp) / 1001 - 1e-9))

def ts(t):
    m, s = divmod(t, 60); h, m = divmod(int(m), 60)
    return f'{h:d}:{int(m):02d}:{s:06.3f}'

order = sorted(defs, key=lambda c: (src[defs[c]['src']]['order'], defs[c]['iv'][0][0]))
final_ids = {c: f'Clip_{i:02d}' for i, c in enumerate(order, 22)}  # series 2 continues after Clip_21

clips = []
for c in order:
    d = defs[c]; part = d['src']; fid = final_ids[c]
    ivs = []
    for a, b in d['iv']:
        f0, f1 = frame_at(part, a), frame_at(part, b)
        ivs.append(dict(start_s=a, end_s=b, start_frame=f0, end_frame_excl=f1,
                        audio_start_sample_48k=round(a * 48000), audio_end_sample_48k_excl=round(b * 48000)))
    dur = sum(i['end_frame_excl'] - i['start_frame'] for i in ivs) * 1001 / 24000
    L = []
    for i, l in enumerate(lines[c], 1):
        L.append(dict(l, line_id=f'{fid}_L{i:03d}', cand_line=l['line_id']))
    clips.append(dict(clip_id=fid, candidate=c, title=d['title'], source_id=part,
                      source_file=src[part]['file'], intervals=ivs, est_duration_s=round(dur, 3), lines=L, **meta[c]))

# overlap check (same source, half-open frame intervals) across all selected clips
over = []
for i, a in enumerate(clips):
    for b in clips[i + 1:]:
        if a['source_id'] != b['source_id']: continue
        for x in a['intervals']:
            for y in b['intervals']:
                if max(x['start_frame'], y['start_frame']) < min(x['end_frame_excl'], y['end_frame_excl']):
                    over.append((a['clip_id'], b['clip_id']))
                if max(x['audio_start_sample_48k'], y['audio_start_sample_48k']) < min(x['audio_end_sample_48k_excl'], y['audio_end_sample_48k_excl']):
                    over.append((a['clip_id'], b['clip_id'], 'audio'))
# cross-series check against the 21 committed series-1 clips (ledger 'committed')
LEDGER = f'{ROOT}/work/source_timeline_ledger.json'
ledger = json.load(open(LEDGER))
for c in clips:
    for x in c['intervals']:
        for r in ledger['committed']:
            if r['source_id'] != c['source_id']: continue
            if max(x['start_frame'], r['start_frame']) < min(x['end_frame_excl'], r['end_frame_excl']):
                over.append((c['clip_id'], r['clip_id']))
            a0, a1 = r['audio_48k']
            if max(x['audio_start_sample_48k'], a0) < min(x['audio_end_sample_48k_excl'], a1):
                over.append((c['clip_id'], r['clip_id'], 'audio'))
assert not over, over
for c in clips:
    assert 60.0 <= c['est_duration_s'] < 120.0, (c['clip_id'], c['est_duration_s'])

def unc_level(u):
    if not u: return ''
    if u.startswith('LOW'): return 'LOW'
    if u.startswith('MEDIUM'): return 'MEDIUM'
    return 'NOTE'

for out in (ROOT, SHARED):
    os.makedirs(f'{out}/review/s2/approved', exist_ok=True)
    open(f'{out}/review/s2/approved/.keep', 'w').write('Approved files are written here only after explicit human approval.\n')

# --- CSV (UTF-8 with BOM, all fields quoted) ---
buf = io.StringIO()
w = csv.writer(buf, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
w.writerow(['clip_id', 'line_id', 'source_start', 'source_end', 'speaker', 'original_en', 'ja_draft', 'ja_final', 'context_note', 'uncertainty'])
for c in clips:
    for l in c['lines']:
        w.writerow([c['clip_id'], l['line_id'], f"{c['source_file']} {ts(l['start'])}", f"{c['source_file']} {ts(l['end'])}",
                    l['speaker'], l['en'], l['ja'], l['ja'], l['ctx'], l['unc']])
csv_bytes = ('\ufeff' + buf.getvalue()).encode('utf-8')
csv_sha = hashlib.sha256(csv_bytes).hexdigest()

# --- translations_review.md ---
md = ['# 翻訳レビュー 第2弾（閲覧用）', '',
      '> **このファイルは閲覧用です。編集しても正本には反映されません。**',
      '> 修正は `review/s2/translations_review.csv` の **`ja_final` 列だけ** に入力してください（`ja_draft` は比較用に残します）。', '',
      '- 英語原文は内部用の無修正テキストです。動画上の英語字幕では伏字（例: ni**a, f**k, s**t, b**ch）を適用します。日本語は伏字なしの意味から訳しています。',
      '- 話者ラベルの "Host" は番組ホスト（N.O.R.E. / DJ EFN）です。どちらかの特定は推定のため行っていません。',
      '- 「⚠」は確認が必要な行です（詳細は `translation_uncertainties.md`）。', '']
for c in clips:
    md += [f"## {c['clip_id']} — {c['title']}", '',
           f"- SOURCE: `{c['source_file']}` " + ', '.join(f"{ts(i['start_s'])}–{ts(i['end_s'])}" for i in c['intervals']),
           f"- 想定尺: {c['est_duration_s']:.1f} 秒",
           f"- 内容: {c['summary_ja']}",
           f"- Hook: {c['hook_ja']}", '',
           '| line_id | 時刻 | 話者 | Original English | Japanese Draft | Notes |', '|---|---|---|---|---|---|']
    for l in c['lines']:
        flag = '⚠ ' if unc_level(l['unc']) in ('LOW', 'MEDIUM') else ''
        note = ' / '.join(x for x in (l['ctx'], l['unc']) if x)
        cell = lambda t: t.replace('|', '\\|').replace('\n', '<br>')
        md.append(f"| {flag}{l['line_id']} | {ts(l['start'])} | {l['speaker']} | {cell(l['en'])} | {cell(l['ja'])} | {cell(note)} |")
    md.append('')
md_text = '\n'.join(md)

# --- clip_selection_summary.md ---
cs = ['# 採用予定クリップ一覧', '',
      f"SOURCE: 6 files (`part_1.mp4`, `part_2 2.mp4`, `part_3.mp4`–`part_6.mp4`), contiguous parts of one Drink Champs episode with Ye (Kanye West). All 1920x1080, 24000/1001 fps CFR.", '',
      '第2弾です。第1弾の21本（Clip_01〜Clip_21）で使った区間とはフレーム単位・音声サンプル単位で重なりません。第1弾で除外した区間（反ユダヤ的発言、特定人物への性的・犯罪的な主張、暴力的発言、誤情報）も引き続き使いません。', '',
      '| Clip | SOURCE 使用範囲 | 予定尺 | Topic | Hook |', '|---|---|---|---|---|']
for c in clips:
    rng = '<br>'.join(f"`{c['source_file']}` {ts(i['start_s'])}–{ts(i['end_s'])} (frames {i['start_frame']}–{i['end_frame_excl']})" for i in c['intervals'])
    cs.append(f"| {c['clip_id']} | {rng} | {c['est_duration_s']:.1f}s | {c['title']} | {c['hook_ja']} |")
cs += ['', '## クリップ別の採用理由', '']
for c in clips:
    cs += [f"### {c['clip_id']} — {c['title']}", '',
           f"- 採用理由: {c['why_ja']}", f"- 単体で成立する理由: {c['standalone_ja']}",
           f"- 編集: {c['edit_ja']}", f"- 他クリップとの重複: なし（フレーム単位・音声サンプル単位で検査済み）", '']
cs += ['## Overlap check', '', f"第2弾 {len(clips)} クリップ同士、および第1弾の確定21本との間で、同一ソース内のフレーム区間（半開区間）と 48kHz 音声サンプル区間の交差を総当たりで検査しました。交差数: **0**。スクリプト: `scripts/make_review.py`。", '']
cs_text = '\n'.join(cs)

# --- translation_uncertainties.md ---
um = ['# 翻訳・聞き取りの確認ポイント', '',
      '`line_id` で CSV の該当行を検索してください。LOW は聞き取り自体が不確か、MEDIUM は解釈・話者・固有名詞に複数候補がある行です。', '']
cnt = {'LOW': 0, 'MEDIUM': 0, 'NOTE': 0}
for lvl in ('LOW', 'MEDIUM', 'NOTE'):
    um += [f'## {lvl}', '']
    for c in clips:
        for l in c['lines']:
            if unc_level(l['unc']) == lvl:
                cnt[lvl] += 1
                um.append(f"- **{l['line_id']}** ({c['title']}, {ts(l['start'])}) — EN: \"{l['en']}\" — {l['unc']}")
    um.append('')
um_text = '\n'.join(um)

files = {'review/s2/translations_review2.md': md_text, 'review/s2/clip_selection_summary.md': cs_text, 'review/s2/translation_uncertainties.md': um_text}
for out in (ROOT, SHARED):
    open(f'{out}/review/s2/translations_review.csv', 'wb').write(csv_bytes)
    for k, v in files.items(): open(f'{out}/{k}', 'w', encoding='utf-8').write(v)

manifest = dict(
    status='AWAITING_TRANSLATION_APPROVAL', generated_at=datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ'),
    editable_file='review/s2/translations_review.csv', editable_column='ja_final',
    review_file_sha256=csv_sha, series=2, review_revision=2, revision_note='Series 2 rev 2 (giub 2026-10-16): Ralph Lauren, トランプ, ウォーレンバフェット, Black Mafia Family, デニーズ, ウクライナ, アメリカ, ファレルウィリアムズ, トランプ支持者の赤の帽子. Timing and line_ids unchanged.',
    sources={k: dict(file=v['file'], sha256=v['sha256']) for k, v in src.items()},
    clips=[dict(clip_id=c['clip_id'], candidate=c['candidate'], title=c['title'], source=c['source_file'],
                intervals=[{k: i[k] for k in ('start_frame', 'end_frame_excl', 'start_s', 'end_s')} for i in c['intervals']],
                est_duration_s=c['est_duration_s'], line_ids=[l['line_id'] for l in c['lines']]) for c in clips],
    line_count=sum(len(c['lines']) for c in clips), uncertain_counts=cnt,
    approval=dict(approved=False, approved_by=None, approved_at=None, note='Approval requires an explicit human message in the project thread. File edits alone are not approval.'))
for out in (ROOT, SHARED):
    json.dump(manifest, open(f'{out}/review/s2/approval_manifest.json', 'w'), indent=1, ensure_ascii=False)
json.dump(clips, open(f'{ROOT}/work/s2/selected_clips.json', 'w'), indent=1, ensure_ascii=False)
print('clips', len(clips), 'lines', manifest['line_count'], 'unc', cnt, 'csv', csv_sha[:12])
for c in clips: print(c['clip_id'], c['candidate'], c['est_duration_s'], c['title'])

# reservations for series 2 (released if a clip is rejected)
ledger['reservations'] = [r for r in ledger['reservations'] if r.get('series') != 2]
for c in clips:
    for i in c['intervals']:
        ledger['reservations'].append(dict(series=2, source_id=c['source_id'], clip_id=c['clip_id'], candidate=c['candidate'], status='RESERVED_AWAITING_APPROVAL',
            start_frame=i['start_frame'], end_frame_excl=i['end_frame_excl'], start_s=i['start_s'], end_s=i['end_s'],
            audio_48k=[i['audio_start_sample_48k'], i['audio_end_sample_48k_excl']]))
ledger['updated'] = manifest['generated_at']
tmp = LEDGER + '.tmp'; json.dump(ledger, open(tmp, 'w'), indent=1, ensure_ascii=False); os.replace(tmp, LEDGER)
