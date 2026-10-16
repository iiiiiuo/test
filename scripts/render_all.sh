#!/bin/bash
# framing + subtitles + render for each clip; skips stages whose outputs exist unless FORCE=1
cd /home/user/test
for i in $(seq -w 1 21); do
  c=Clip_$i
  [ -f work/b/$c/framing.json ] && [ -z "$FORCE" ] || python3 scripts/framing.py $c || echo "FAIL framing $c"
  python3 scripts/build_subs.py $c >/dev/null || echo "FAIL subs $c"
  python3 scripts/render_clip.py $c || echo "FAIL render $c"
done
echo ALLDONE
