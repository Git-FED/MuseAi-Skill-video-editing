#!/usr/bin/env bash
set -euo pipefail

# Fail if a CNAME file exists anywhere in the tree.
# A stray CNAME silently points GitHub Pages at a domain you may not control.

if find . -type f -iname 'CNAME' -print -quit | grep -q .; then
  PATH_FOUND="$(find . -type f -iname 'CNAME' -print -quit)"
  echo "FORBIDDEN: CNAME file present at $PATH_FOUND" >&2
  echo "NOTE: deleting the file does not clear the hosting provider's saved" >&2
  echo "      custom domain. Check that setting separately." >&2
  exit 1
fi

echo "OK: no CNAME file"
