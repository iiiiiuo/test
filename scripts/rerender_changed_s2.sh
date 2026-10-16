#!/bin/bash
# Rebuild subtitles for all non-frozen clips with the current build_subs.py; re-render+QA only clips whose subtitles
# or intervals changed since their last render. Frozen PASS clips (work/b2/frozen.json) are never rebuilt or re-rendered.
cd /home/user/test
frozen=$(python3 -c "import json;print(' '.join(json.load(open('work/b2/frozen.json'))))")
changed=()
for n in $(seq 22 39); do
  c=Clip_$n; [[ " $frozen " == *" $c "* ]] && continue
  python3 scripts/build_subs_s2.py $c > /dev/null || { echo "$c subs FAILED"; continue; }
  same=$(python3 -c "
import json,hashlib;m=json.load(open('work/b2/$c/source_manifest.json'));f=json.load(open('work/b2/$c/framing.json'))
s={x['clip_id']:x for x in json.load(open('work/s2/selected_clips.json'))}['$c']
iv=[(i['start_frame'],i['end_frame_excl']) for i in s['intervals']]
print(m['subtitles']['sha256']==hashlib.sha256(open('work/b2/$c/subtitles.ass','rb').read()).hexdigest()
      and iv==[(i['start_frame'],i['end_frame_excl']) for i in f['intervals']]
      and [(x['start_frame'],x['end_frame_excl']) for x in m['video_segments']]==iv
      and [p['crop'] for p in m['pieces']]==[dict(w=s_['w'],h=s_['h'],x=s_['x'],y=s_['y']) for i in f['intervals'] for s_ in i['shots']])")
  [ "$same" = True ] || changed+=($c)
done
echo "changed: ${changed[@]}"
[ ${#changed[@]} -gt 0 ] && scripts/render_only_s2.sh "${changed[@]}"
