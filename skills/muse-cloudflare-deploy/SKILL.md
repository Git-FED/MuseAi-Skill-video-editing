---
name: cloudflare-deploy
description: Preflight a Cloudflare Pages/Workers deploy before it leaks assets
version: 1.0.0
---

## What it does
Runs a dry-run deploy and inspects what would actually be uploaded, so you catch
a mis-targeted build, an oversized bundle, or a dependency binary getting
shipped as a static asset — before it goes live.

## Prerequisites
- `wrangler` and `node` on `PATH`
- A `wrangler.toml` (or `wrangler.jsonc`) in the project root
- Cloudflare credentials available to `wrangler` (via env, not committed)

## Verify environment
Run before anything else:

    command -v wrangler && command -v node

If either is missing, stop and report: `MISSING_DEP: wrangler`.

## Step-by-step
1. Confirm the wrangler config exists:

       test -f wrangler.toml || test -f wrangler.jsonc

   If neither exists, report `MISSING_CONFIG: wrangler.toml`.

2. Confirm `.wrangler/` is gitignored (it holds local state and can hold tokens):

       test -f .gitignore && grep -qxF '.wrangler/' .gitignore || echo "WARN: .wrangler/ not gitignored"

3. Run the preflight (dry-run + upload inspection):

       bash scripts/preflight.sh

4. Run the secrets check:

       bash scripts/check-secrets.sh

5. Only if both pass, deploy:

       wrangler deploy

## Never assume
- Never assume `wrangler deploy` targets Pages when you meant Workers, or vice
  versa. Confirm the target in `wrangler.toml` before deploying.
- Never assume the build output directory is correct — wrangler auto-discovers
  and can pick the wrong one. Check the dry-run output path.
- Never assume `node_modules` and `workerd` binaries are excluded from a static
  asset upload. Inspect the dry-run.
- Never echo a secret. If any step prints `${{ secrets.* }}` or a token, treat
  it as a leak: report `CREDENTIAL_LEAK` and halt.
- Never commit `.wrangler/` or `.dev.vars`.

## Output
A dry-run size report, a list of any leaked binaries, and a pass/fail verdict.
No deploy happens unless both checks pass.

## Failure handling
- `wrangler` missing → report `MISSING_DEP: wrangler`, halt.
- Dry-run fails → surface wrangler's stderr verbatim, do not retry blindly.
- `ASSET_LEAK` → stop, fix the build, re-run. Do not deploy.
- `CREDENTIAL_LEAK` → rotate the credential, then re-run.
