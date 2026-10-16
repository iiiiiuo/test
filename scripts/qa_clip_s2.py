"""Automated evidence for one rendered clip (no judgement of meaning).

Usage: python3 scripts/qa_clip.py Clip_XX -> work/b2/<clip>/qa/{auto.json, sheet_*.jpg, render_asr.json, sync.txt}
Checks: probe/decode, exact durations, 9:16 + SAR, frame count vs manifest, subtitle bounds, masking scan,
render-audio ASR vs caption text/timing (A/V + subtitle sync evidence), frame sheets at openings/endings/longest captions/shot changes.
"""
import json, sys, subprocess, os, re, hashlib, difflib
from PIL import Image

ROOT = '/home/user/test'
CLIP = sys.argv[1]
B = f'{ROOT}/work/b2/{CLIP}'; Q = f'{B}/qa'; os.makedirs(Q, exist_ok=True)
R = f'{B}/render.mp4'
man = json.load(open(f'{B}/source_manifest.json'))
cap = json.load(open(f'{B}/captions.json'))
res = dict(clip=CLIP, render_sha256=hashlib.sha256(open(R, 'rb').read()).hexdigest())

def probe(sel, entries):
    o = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', sel, '-count_packets', '-show_entries', entries, '-of', 'json', R],
                       capture_output=True, text=True, check=True).stdout
    return json.loads(o)['streams'][0]
v = probe('v:0', 'stream=width,height,sample_aspect_ratio,display_aspect_ratio,r_frame_rate,nb_read_packets,duration,start_time:stream_side_data')
a = probe('a:0', 'stream=sample_rate,nb_read_packets,duration,start_time')
# last video packet end
pk = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'packet=pts_time,duration_time', '-of', 'csv=p=0', R],
                    capture_output=True, text=True).stdout.split()
ends = [float(x.split(',')[0]) + float(x.split(',')[1]) for x in pk if ',' in x]
apk = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'a:0', '-show_entries', 'packet=pts_time,duration_time', '-of', 'csv=p=0', R],
                     capture_output=True, text=True).stdout.split()
aends = [float(x.split(',')[0]) + float(x.split(',')[1]) for x in apk if ',' in x]
exp_frames = sum(s['end_frame_excl'] - s['start_frame'] for s in man['video_segments'])
dec = subprocess.run(['ffmpeg', '-v', 'error', '-i', R, '-f', 'null', '-'], capture_output=True, text=True)
vdur, adur = max(ends) - float(v['start_time']), max(aends) - float(a['start_time'])
res['format'] = dict(width=v['width'], height=v['height'], sar=v.get('sample_aspect_ratio'), fps=v['r_frame_rate'],
                     video_frames=int(v['nb_read_packets']), expected_frames=exp_frames, video_duration_s=round(vdur, 6),
                     audio_duration_s=round(adur, 6), v_start=v['start_time'], a_start=a['start_time'],
                     rotation=v.get('side_data_list'), decode_errors=dec.stderr.strip()[:500])
res['format']['PASS'] = (v['width'], v['height']) == (1080, 1920) and v.get('sample_aspect_ratio') in ('1:1', None) \
    and int(v['nb_read_packets']) == exp_frames and 60.0 <= vdur < 120.0 and 60.0 <= adur < 120.0 and not dec.stderr.strip() \
    and abs(vdur - adur) < 0.05

# subtitles
ass = open(f'{B}/subtitles.ass', encoding='utf-8').read()
ev = re.findall(r'^Dialogue: 0,([\d:.]+),([\d:.]+),Sub,,0,0,0,,\{[^}]*\\pos\(540,(\d+)\)\\fs(\d+)\}(.*)$', ass, re.M)
def secs(t): h, m, s = t.split(':'); return int(h) * 3600 + int(m) * 60 + float(s)
bad_mask = [e[4] for e in ev if re.search(r'\b(fuck|shit|bitch|nigga|pussy)', e[4], re.I)]
res['subtitles'] = dict(events=len(ev), captions=len(cap['captions']), max_end=max(secs(e[1]) for e in ev),
                        beyond_video=[e for e in ev if secs(e[1]) > vdur + 0.01], unmasked_hits=bad_mask,
                        captions_without_jp=[c['line_id'] for c in cap['captions'] if not c['jp']],
                        max_lines=max(len(c['en']) + len(c['jp']) for c in cap['captions']))

# render-audio ASR (turbo) for sync evidence
wav = f'{Q}/render16k.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', R, '-ac', '1', '-ar', '16000', wav], check=True)
if not os.path.exists(f'{Q}/render_asr.json'):
    subprocess.run(['python3', f'{ROOT}/scripts/transcribe.py', '/root/models/turbo', wav, f'{Q}/render_asr.json', '4'], check=True,
                   capture_output=True)
os.remove(wav)
words = [w for s in json.load(open(f'{Q}/render_asr.json'))['segments'] for w in s['words']]
norm = lambda t: re.sub(r"[^a-z0-9']", '', t.lower())
ct = []
for i, c in enumerate(cap['captions']):
    for tk in c['en_unmasked'].split(): ct.append((norm(tk), i))
sm = difflib.SequenceMatcher(None, [x[0] for x in ct], [norm(w['w']) for w in words], autojunk=False)
offs, inside = [], 0
matched = 0
for blk in sm.get_matching_blocks():
    for k in range(blk.size):
        ci = ct[blk.a + k][1]; w = words[blk.b + k]; c = cap['captions'][ci]; matched += 1
        if c['start'] - 0.25 <= w['s'] <= c['end'] + 0.05: inside += 1
        if k == 0 or True: offs.append(w['s'] - c['start'])
first_word_off = []
for i, c in enumerate(cap['captions']):
    idx = [j for j, x in enumerate(ct) if x[1] == i]
    for blk in sm.get_matching_blocks():
        if blk.size and blk.a <= idx[0] < blk.a + blk.size:
            first_word_off.append(round(words[blk.b + idx[0] - blk.a]['s'] - c['start'], 3)); break
res['sync'] = dict(caption_tokens=len(ct), asr_words=len(words), matched=matched, match_ratio=round(matched / max(1, len(ct)), 3),
                   matched_words_inside_their_caption=round(inside / max(1, matched), 3),
                   caption_onset_vs_first_word_s=dict(n=len(first_word_off), median=sorted(first_word_off)[len(first_word_off) // 2] if first_word_off else None,
                                                      max_abs=max(map(abs, first_word_off)) if first_word_off else None))
with open(f'{Q}/sync.txt', 'w') as f:
    for c in cap['captions']:
        ws = [w['w'] for w in words if c['start'] - 0.1 <= w['s'] < c['end']]
        f.write(f"{c['start']:7.2f}-{c['end']:6.2f} SUB: {' / '.join(c['en'])}  ||  {' / '.join(c['jp'])}\n               HEARD: {''.join(ws).strip()}\n")

# frame sheets: opening, ending, longest-caption midpoints, shot changes (+3 frames), each labelled
fps = 24000 / 1001
times = [0.05, 1.0, vdur - 1.0, vdur - 0.08]
longest = sorted(cap['captions'], key=lambda c: -sum(len(x) for x in c['en'] + c['jp']))[:4]
times += [(c['start'] + c['end']) / 2 for c in longest]
off = 0
for s in man['video_segments']:
    off_frames = 0
pf = 0
shot_starts = []
acc = 0
for seg in man['video_segments']:
    for p in man['pieces']:
        if seg['start_frame'] <= p['start_frame'] < seg['end_frame_excl'] and p['start_frame'] > seg['start_frame']:
            shot_starts.append((acc + p['start_frame'] - seg['start_frame'] + 3) / fps)
    if acc: shot_starts.append((acc + 2) / fps)  # interval join
    acc += seg['end_frame_excl'] - seg['start_frame']
times += shot_starts[:8]
times = sorted(set(round(t, 2) for t in times if 0 <= t < vdur))
imgs = []
for t in times:
    p = f'{Q}/f_{t:07.2f}.png'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t}', '-i', R, '-frames:v', '1', p], check=True)
    imgs.append((t, p))
cols = 4
for n0 in range(0, len(imgs), 8):
    chunk = imgs[n0:n0 + 8]
    W = Image.new('RGB', (cols * 405, ((len(chunk) + cols - 1) // cols) * 720), 'black')
    for i, (t, p) in enumerate(chunk):
        im = Image.open(p).resize((405, 720)); W.paste(im, ((i % cols) * 405, (i // cols) * 720))
    W.save(f'{Q}/sheet_{n0 // 8 + 1}.jpg', quality=88)
res['frames'] = dict(times=times, sheets=sorted(x for x in os.listdir(Q) if x.startswith('sheet_')), full_res=[p for _, p in imgs])
json.dump(res, open(f'{Q}/auto.json', 'w'), indent=1, ensure_ascii=False)
print(CLIP, 'format', res['format']['PASS'], 'vdur', res['format']['video_duration_s'], 'adur', res['format']['audio_duration_s'],
      'sync', res['sync']['match_ratio'], res['sync']['matched_words_inside_their_caption'], res['sync']['caption_onset_vs_first_word_s'],
      'unmasked', len(bad_mask))
