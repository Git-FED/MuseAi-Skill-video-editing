# Security Policy

## Supported versions
| Version | Supported |
| --- | --- |
| 1.x | ✅ |

## Reporting a vulnerability
Open a private security advisory on the repository, or email
security@fedpromptly.com. Do not open a public issue for anything exploitable
before a fix ships.

Include: affected skill and version, a minimal reproduction, and impact.

## The credential rule
No client ID, publishable key, buy-button ID, merchant ID, OAuth `state`, or
`redirect_uri` is ever stored in a tracked file or a URL. If you find one,
treat it as a leak:

1. Report `CREDENTIAL_LEAK: <path>`.
2. Rotate the credential in the provider dashboard.
3. Remove it from history, not just the working tree.

## What the fleet never does
- It never commits `.env`, `.wrangler/`, or `.dev.vars`.
- It never prints a secret in a workflow.
- It never ships HTML inside a skill repo.
- It never claims a client-side checkbox verifies age.

## Enforced by
- `.pre-commit-config.yaml` — rejects tracked `.env` and OAuth params.
- `skills/muse-cloudflare-deploy/scripts/check-secrets.sh` — CI secrets scan.
- `skills/muse-cname-guard/scripts/check-cname.sh` — stray-domain guard.
