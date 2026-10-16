#!/usr/bin/env bash
set -euo pipefail

# Validate that the site's icon assets exist and that every HTML page
# references a favicon. Fails the build if a page ships without one.

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SITE="$ROOT/site"
FAIL=0

required=(
  "assets/images/logo.svg"
  "assets/images/favicon.svg"
  "assets/images/favicon.png"
  "assets/images/favicon.ico"
  "assets/images/social-preview.jpg"
)

for f in "${required[@]}"; do
  if [ -f "$SITE/$f" ]; then
    echo "OK    $f"
  else
    echo "MISSING  $f" >&2
    FAIL=1
  fi
done

# Every HTML page must reference a favicon.
for page in "$SITE"/*.html; do
  [ -f "$page" ] || continue
  if grep -qi 'rel="icon"' "$page"; then
    echo "OK    $(basename "$page") references a favicon"
  else
    echo "NO_FAVICON  $(basename "$page")" >&2
    FAIL=1
  fi
done

# Favicon.ico must be a real ICO (magic bytes 00 00 01 00).
if [ -f "$SITE/assets/images/favicon.ico" ]; then
  if [ "$(od -An -N4 -tx1 "$SITE/assets/images/favicon.ico" | tr -d ' \n')" = "00000100" ]; then
    echo "OK    favicon.ico has valid ICO magic bytes"
  else
    echo "BAD_ICO  favicon.ico is not a valid ICO" >&2
    FAIL=1
  fi
fi

[ "$FAIL" -eq 0 ] && echo "OK: icons validated" || exit 1
