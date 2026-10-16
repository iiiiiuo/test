#!/bin/bash
# usage: scripts/process_clips.sh [--render] Clip_XX ...   (framing+subs+render if --render, then source context + automated QA)
cd /home/user/test
R=0; [ "$1" = "--render" ] && { R=1; shift; }
for c in "$@"; do
  if [ $R = 1 ]; then
    python3 scripts/framing_s2.py $c || { echo "FAIL framing $c"; continue; }
    python3 scripts/build_subs_s2.py $c > /dev/null || { echo "FAIL subs $c"; continue; }
    python3 scripts/render_clip_s2.py $c || { echo "FAIL render $c"; continue; }
  fi
  [ -d work/b2/$c/qa ] && { rm -rf work/b2/$c/qa_prev; mv work/b2/$c/qa work/b2/$c/qa_prev; }; mkdir -p work/b2/$c/qa
  python3 scripts/source_context_s2.py $c && python3 scripts/qa_clip_s2.py $c || echo "FAIL qa $c"
done
echo BATCHDONE
