#!/usr/bin/env bash
set -euo pipefail

FAIL=0

# 1. .env files must never be committed (except .env.example).
if git ls-files --error-unmatch >/dev/null 2>&1; then
  if git ls-files | grep -E '(^|/)\.env($|\.)' | grep -v '\.env\.example$' | grep -q .; then
    echo "CREDENTIAL_LEAK: .env file is tracked" >&2
    git ls-files | grep -E '(^|/)\.env($|\.)' | grep -v '\.env\.example$' >&2
    FAIL=1
  fi
fi

# 2. .wrangler/ must be gitignored.
if [ -f .gitignore ]; then
  grep -qxF '.wrangler/' .gitignore || { echo "WARN: .wrangler/ not gitignored" >&2; }
else
  echo "WARN: no .gitignore" >&2
fi

# 3. Workflows must never print secrets.
if [ -d .github/workflows ]; then
  if grep -rn 'secrets\.' .github/workflows 2>/dev/null | grep -Ei 'echo|printf|cat' | grep -q .; then
    echo "CREDENTIAL_LEAK: workflow prints a secret" >&2
    grep -rn 'secrets\.' .github/workflows | grep -Ei 'echo|printf|cat' >&2
    FAIL=1
  fi
fi

# 4. .dev.vars must not be tracked.
if git ls-files --error-unmatch >/dev/null 2>&1; then
  git ls-files | grep -qxF '.dev.vars' && { echo "CREDENTIAL_LEAK: .dev.vars is tracked" >&2; FAIL=1; }
fi

[ "$FAIL" -eq 0 ] && echo "OK: no tracked secrets" || exit 1
