#!/usr/bin/env bash
set -euo pipefail

IN="${1:?usage: cut.sh <input> <output>}"
OUT="${2:?usage: cut.sh <input> <output>}"

[ -f "$IN" ] || { echo "MISSING_INPUT: $IN" >&2; exit 2; }

mkdir -p "$(dirname "$OUT")"

ffmpeg -hide_banner -loglevel error -y -i "$IN" \
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" \
  -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p \
  -c:a aac -b:a 128k \
  "$OUT" || { echo "FFMPEG_FAILED: $IN" >&2; exit 1; }

[ -s "$OUT" ] || { echo "EMPTY_OUTPUT: $OUT" >&2; exit 3; }

echo "$OUT"
