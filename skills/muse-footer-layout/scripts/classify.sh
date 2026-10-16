#!/usr/bin/env bash
set -euo pipefail

URL="${1:?usage: classify.sh <url>}"
REF="$(dirname "$0")/../references/links.json"

test -f "$REF" || { echo "MISSING_REF: links.json" >&2; exit 2; }
command -v jq >/dev/null 2>&1 || { echo "MISSING_DEP: jq" >&2; exit 4; }

# 1. Hard rule: credential-bearing checkout / OAuth flows are never footer links.
if printf '%s' "$URL" | grep -Eqi 'patreon\.com/checkout|/oauth2/|response_type=code|state=|client_id='; then
  echo "Premium"
  echo "RULE: checkout_urls — never-footer; swap to canonical landing page" >&2
  exit 0
fi

# 2. Hard rule: third-party invite proxies.
if printf '%s' "$URL" | grep -Eqi 'preview\.|/server/|invite-proxy'; then
  echo "Public"
  echo "RULE: third_party_invite_proxies — resolve to canonical discord.gg/invite" >&2
  exit 0
fi

# 3. Exact-match lookup.
CLASS="$(jq -r --arg u "$URL" '.[$u].class // "Unknown"' "$REF")"
if [ "$CLASS" = "Unknown" ]; then
  echo "UNCLASSIFIED: $URL" >&2
  exit 3
fi

echo "$CLASS"

# 4. Surface disclosure obligation, if any.
DISC="$(jq -r --arg u "$URL" '.[$u].disclosure // empty' "$REF")"
[ -n "$DISC" ] && echo "DISCLOSURE: $DISC" >&2

exit 0
