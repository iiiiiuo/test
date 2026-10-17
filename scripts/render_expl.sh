#!/bin/bash
# Re-render frozen PASS clips with the approved explanation row: frozen captions + Expl row (add_expl_frozen.py),
# existing framing.json, then source context + automated QA. Usage: scripts/render_expl.sh Clip_XX ...
cd /home/user/test
for c in "$@"; do
  n=$((10#${c#Clip_})); if [ $n -le 21 ]; then d=b; s=; else d=b2; s=_s2; fi
  python3 scripts/add_expl_frozen.py $c || { echo "FAIL subs $c"; continue; }
  python3 scripts/render_clip$s.py $c || { echo "FAIL render $c"; continue; }
  [ -d work/$d/$c/qa ] && { rm -rf work/$d/$c/qa_prev; mv work/$d/$c/qa work/$d/$c/qa_prev; }; mkdir -p work/$d/$c/qa
  python3 scripts/source_context$s.py $c && python3 scripts/qa_clip$s.py $c || echo "FAIL qa $c"
done
echo BATCHDONE
