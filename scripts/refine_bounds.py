"""Phase B boundary corrections (critic Clip_01 finding + systematic audit of every boundary, work/b/boundary_check.json).
Each boundary moves to the quietest 20 ms point inside a hand-checked search window (between the last included word
and the first excluded word), snapped to the nearest frame boundary. Rewrites work/selected_clips.json (v1 kept)."""
import json, math, wave, numpy as np, shutil, os
ROOT = '/home/user/test'
W = {  # clip: [(interval index, 'start'|'end', lo, hi, reason)]
 'Clip_01': [(0, 'end', 1270.25, 1270.70, "last word 'ever' was cut")],
 'Clip_02': [(0, 'start', 1592.47, 1592.74, "start inside tail of 'one time.'; large-v3 span re-check: '...Jared one time. Yeah, it's so funny'"), (0, 'end', 1598.50, 1599.90, "excluded next sentence 'And 80%' started inside")],
 'Clip_03': [(0, 'start', 1749.00, 1749.15, 'start inside repeated "so so"'), (1, 'end', 1853.30, 1853.95, "critic: last line L015 (LOW) not heard as written ('Oh, s**t. Don't have ... Google maps'); end after 'That's crazy.'")],
 'Clip_05': [(0, 'end', 706.43, 706.74, "host 'put it.' was cut")],
 'Clip_06': [(1, 'end', 1216.60, 1216.80, "next 'I forgive' started at boundary")],
 'Clip_08': [(0, 'start', 1752.15, 1752.35, "previous word 'people' tail"), (0, 'end', 1832.98, 1833.20, "'together' / next 'You know'")],
 'Clip_09': [(0, 'end', 247.10, 247.32, "critic: ended on dangling 'But it's funny,' (next words 'he overlooked that easily' not in approved lines); end after 'got a couple hundred thousand back.'")],
 'Clip_11': [(0, 'end', 970.70, 970.84, "next sentence 'they have' started inside")],
 'Clip_12': [(0, 'end', 1092.55, 1092.95, "next words 'from us' started inside")],
 'Clip_13': [(0, 'end', 1474.15, 1474.45, "'that?' was cut")],
 'Clip_14': [(0, 'start', 343.05, 343.30, "previous word 'world' tail")],
 'Clip_16': [(0, 'end', 1884.90, 1885.62, "first word 'Puff' of Clip_17 straddled the shared boundary")],
 'Clip_17': [(0, 'start', 1884.90, 1885.62, 'shared boundary with Clip_16 (same point)'), (0, 'end', 1957.65, 1958.25, "excluded 'and I'll be honest' started inside")],
 'Clip_18': [(0, 'start', 1177.25, 1177.60, "previous word 'Vuitton' tail")],
 'Clip_19': [(0, 'start', 1738.60, 1739.15, "first word 'In' was cut")],
 'Clip_21': [(0, 'end', 1259.10, 1259.35, "excluded next 'so' started inside")],
}
src = json.load(open(f'{ROOT}/work/sources.json'))
P = f'{ROOT}/work/selected_clips.json'
if not os.path.exists(f'{ROOT}/work/selected_clips.v1.json'): shutil.copy(P, f'{ROOT}/work/selected_clips.v1.json')
clips = json.load(open(f'{ROOT}/work/selected_clips.v1.json'))
aud = {}
def quietest(sid, lo, hi):
    if sid not in aud:
        w = wave.open(f'{ROOT}/work/audio/{sid}.wav'); aud[sid] = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)
    x = aud[sid]; best = None
    for t in np.arange(lo, hi - 0.02 + 1e-9, 0.005):
        a = int(t * 16000); e = float(np.sqrt(np.mean(x[a:a + 320] ** 2)) + 1e-9)
        if best is None or e < best[0]: best = (e, t + 0.01)
    return best[1], 20 * math.log10(best[0] / 32768)
log = []
shared = {}
for c in clips:
    sp = src[c['source_id']]['start_pts']
    for k, kind, lo, hi, why in W.get(c['clip_id'], []):
        key = (c['source_id'], lo, hi)
        t, db = shared[key] if key in shared else quietest(c['source_id'], lo, hi)
        shared[key] = (t, db)
        f = round((t * 24000 - sp) / 1001)
        iv = c['intervals'][k]
        old = (iv['start_frame'], iv['end_frame_excl'])
        if kind == 'start': iv['start_frame'] = f; iv['start_s'] = round((sp + f * 1001) / 24000, 4)
        else: iv['end_frame_excl'] = f; iv['end_s'] = round((sp + f * 1001) / 24000, 4)
        iv['audio_start_sample_48k'] = round((sp + iv['start_frame'] * 1001) / 24000 * 48000)
        iv['audio_end_sample_48k_excl'] = round((sp + iv['end_frame_excl'] * 1001) / 24000 * 48000)
        log.append(dict(clip=c['clip_id'], interval=k, kind=kind, window=[lo, hi], cut_s=round(t, 3), cut_rms_dbfs=round(db, 1), frame=f, old_frames=old, reason=why))
    c['est_duration_s'] = round(sum(i['end_frame_excl'] - i['start_frame'] for i in c['intervals']) * 1001 / 24000, 3)
# zero-overlap + duration gates
for i, a in enumerate(clips):
    assert 60.0 <= a['est_duration_s'] < 120.0, (a['clip_id'], a['est_duration_s'])
    for b in clips[i + 1:]:
        if a['source_id'] != b['source_id']: continue
        for x in a['intervals']:
            for y in b['intervals']:
                assert not max(x['start_frame'], y['start_frame']) < min(x['end_frame_excl'], y['end_frame_excl']), (a['clip_id'], b['clip_id'])
                assert not max(x['audio_start_sample_48k'], y['audio_start_sample_48k']) < min(x['audio_end_sample_48k_excl'], y['audio_end_sample_48k_excl']), (a['clip_id'], b['clip_id'], 'audio')
# internal cuts: remove uncaptioned, low-confidence crosstalk that has no approved translation (CLAUDE.md: cut LOW material where coherent)
CUTS = {'Clip_04': [(0, (80.95, 81.30), (86.60, 86.82), "LOW lines L015-L017 (speaker/words unclear in all ASR passes; critic: caption is a guess) removed")],
        'Clip_03': [(1, (1824.85, 1825.20), (1825.95, 1826.20), "'Wait a second.' (heard in all passes, absent from the approved line L007, so it has no approved Japanese; critic Clip_03) removed")],
        'Clip_01': [(0, (1234.30, 1234.55), (1236.95, 1237.06), "host aside 'That was all... very good' (LOW, not in approved translation) between Ye's 'hop over...' and 'You know, we'll walk over'")]}
for c in clips:
    sp = src[c['source_id']]['start_pts']
    for k, wa, wb, why in CUTS.get(c['clip_id'], []):
        ta, _ = quietest(c['source_id'], *wa); tb, _ = quietest(c['source_id'], *wb)
        fa, fb = round((ta * 24000 - sp) / 1001), round((tb * 24000 - sp) / 1001)
        iv = c['intervals'][k]
        mk = lambda f0, f1: dict(start_s=round((sp + f0 * 1001) / 24000, 4), end_s=round((sp + f1 * 1001) / 24000, 4), start_frame=f0, end_frame_excl=f1,
                                 audio_start_sample_48k=round((sp + f0 * 1001) / 24000 * 48000), audio_end_sample_48k_excl=round((sp + f1 * 1001) / 24000 * 48000))
        c['intervals'][k:k + 1] = [mk(iv['start_frame'], fa), mk(fb, iv['end_frame_excl'])]
        c['est_duration_s'] = round(sum(i['end_frame_excl'] - i['start_frame'] for i in c['intervals']) * 1001 / 24000, 3)
        assert 60.0 <= c['est_duration_s'] < 120.0, c['est_duration_s']
        log.append(dict(clip=c['clip_id'], kind='internal_cut', removed_frames=[fa, fb], removed_s=[round(ta, 3), round(tb, 3)], reason=why))
json.dump(clips, open(P, 'w'), indent=1, ensure_ascii=False)
json.dump(log, open(f'{ROOT}/work/b/boundary_changes.json', 'w'), indent=1)
for l in log: print(l)
