#!/bin/bash
# Full-source 9:16 render: no cuts/speed change; spatial reframe + EN/JP subtitle burn-in only.
# The source MP4 has an edit list that hides 139 pre-roll video frames (pts < 0). FFmpeg 6.1 + libdav1d
# still outputs them (restamped 0..4.6 s), so they are dropped with select n>=139; the remaining
# 1528 frames keep their original pts 0..50.951 s.
set -e
RUN=full_source_translation_20261027_070832
SRC=/mnt/project-files/uploads/hearth/9980dadf-4de0-426e-b4a6-ac3142fd829d
WK=/mnt/project-files/work/runs/$RUN; OUT=${1:-$WK/render.mp4}; ASS=${2:-/mnt/project-files/output/runs/$RUN/subtitles.ass}
D=$(dirname "$0")
X=$(python3 "$D/framing.py" "$WK/framing.json")
cp "$ASS" "$WK/subs_render.ass"
ffmpeg -v error -y -c:v libdav1d -i "$SRC" -filter_complex \
"[0:v]select='gte(n\,139)',crop=1119:1080:'$X':0,setsar=1,split[a][b];\
[a]scale=1080:1042:flags=lanczos[fg];\
[b]scale=2000:1932,crop=1080:1920,boxblur=28:3[bg];\
[bg][fg]overlay=0:438,subtitles=$WK/subs_render.ass:fontsdir=$WK/fonts,format=yuv420p[v]" \
-map "[v]" -map 0:a -c:v libx264 -preset slow -crf 18 -fps_mode passthrough \
-c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
