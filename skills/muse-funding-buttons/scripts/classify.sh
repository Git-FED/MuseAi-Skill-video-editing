#!/usr/bin/env bash
set -euo pipefail

HANDLE="${1:?usage: classify.sh <handle|url>}"
REF="$(dirname "$0")/../references/funding-links.json"

test -f "$REF" || { echo "MISSING_REF: funding-links.json" >&2; exit 2; }
command -v jq >/dev/null 2>&1 || { echo "MISSING_DEP: jq" >&2; exit 4; }

# 1. Hard rule: a live checkout URL or embedded key is never planned.
if printf '%s' "$HANDLE" | grep -Eqi 'patreon\.com/checkout|/oauth2/|response_type=code|state=|client_id=|buy_btn_|pk_live_|pk_test_'; then
  echo "RESOLVED: $HANDLE -> (canonical handle)"
  echo "RULE: checkout_urls — never-plan; resolve to canonical handle" >&2
  exit 0
fi

# 2. Exact-match lookup by handle.
CLASS="$(jq -r --arg h "$HANDLE" '.[$h].class // "Unknown"' "$REF")"
if [ "$CLASS" = "Unknown" ]; then
  echo "UNCLASSIFIED: $HANDLE" >&2
  exit 3
fi

LABEL="$(jq -r --arg h "$HANDLE" '.[$h].label // ""' "$REF")"
GATE="$(jq -r --arg h "$HANDLE" '.[$h].gate // "none"' "$REF")"

echo "$CLASS"
echo "label: $LABEL"
echo "gate: $GATE"

DISC="$(jq -r --arg h "$HANDLE" '.[$h].disclosure // empty' "$REF")"
[ -n "$DISC" ] && echo "DISCLOSURE: $DISC" >&2

exit 0
