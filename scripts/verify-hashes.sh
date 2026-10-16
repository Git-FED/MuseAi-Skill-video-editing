#!/usr/bin/env bash
set -euo pipefail

# Verify each skill's manifest.json:files hashes against the working tree.
# Placeholders ("sha256:<fill-at-release>") are skipped with a notice.

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FAIL=0
CHECKED=0

for manifest in "$ROOT"/skills/*/manifest.json; do
  [ -f "$manifest" ] || continue
  skill_dir="$(dirname "$manifest")"
  skill_name="$(basename "$skill_dir")"

  while IFS=$'\t' read -r path expected; do
    [ -n "$path" ] || continue
    if [ "$expected" = "sha256:<fill-at-release>" ]; then
      echo "SKIP  $skill_name/$path (placeholder)"
      continue
    fi
    file="$skill_dir/$path"
    if [ ! -f "$file" ]; then
      echo "MISSING  $skill_name/$path" >&2
      FAIL=1
      continue
    fi
    actual="sha256:$(sha256sum "$file" | cut -d' ' -f1)"
    if [ "$actual" != "$expected" ]; then
      echo "MISMATCH $skill_name/$path" >&2
      echo "  expected $expected" >&2
      echo "  actual   $actual" >&2
      FAIL=1
    else
      CHECKED=$((CHECKED + 1))
    fi
  done < <(jq -r '.files | to_entries[] | "\(.key)\t\(.value)"' "$manifest")

  # Ensure files{} and files_excluded don't overlap.
  overlap="$(jq -r '((.files|keys) - ((.files|keys) - (.files_excluded // []))) | .[]' "$manifest" 2>/dev/null || true)"
  [ -n "$overlap" ] && { echo "OVERLAP  $skill_name: $overlap in both files{} and files_excluded{}" >&2; FAIL=1; }
done

if [ "$FAIL" -eq 0 ]; then
  echo "OK: $CHECKED hashes verified"
else
  exit 1
fi
