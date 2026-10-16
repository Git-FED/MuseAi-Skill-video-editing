#!/usr/bin/env bash
set -euo pipefail

command -v wrangler >/dev/null 2>&1 || { echo "MISSING_DEP: wrangler" >&2; exit 2; }

DRY_DIR="$(mktemp -d)"
trap 'rm -rf "$DRY_DIR"' EXIT

echo "==> dry-run deploy to $DRY_DIR"
wrangler deploy --dry-run --outdir="$DRY_DIR" >/dev/null

SIZE="$(du -sh "$DRY_DIR" | cut -f1)"
echo "dry-run size: $SIZE"

# Fail if dependency binaries got swept into the static upload.
if find "$DRY_DIR" \( -name '*.node' -o -name 'workerd*' -o -name '*.wasm' \) -print -quit | grep -q .; then
  echo "ASSET_LEAK: dependency binary in upload" >&2
  find "$DRY_DIR" \( -name '*.node' -o -name 'workerd*' -o -name '*.wasm' \) -print >&2
  exit 1
fi

# Warn on a suspiciously large static bundle.
BYTES="$(du -sb "$DRY_DIR" | cut -f1)"
if [ "$BYTES" -gt 26214400 ]; then
  echo "WARN: dry-run exceeds 25MB ($SIZE) — check for node_modules in assets" >&2
fi

echo "OK: preflight passed"
