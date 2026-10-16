# Security Policy

## Supported versions
| Version | Supported |
| --- | --- |
| 1.x | ✅ |

## Reporting a vulnerability
Open a private security advisory, or email security@fedpromptly.com.

## Scope
This skill runs `wrangler` in dry-run mode and inspects the output. It reads
repository files and writes only to a temp directory. Anything that lets a
crafted project exfiltrate a secret, or deploy despite a failed check, is in
scope.

## Credential rule
Cloudflare tokens live in the environment (`CLOUDFLARE_API_TOKEN`), never in a
tracked file. `.wrangler/` and `.dev.vars` are never committed. If a workflow
prints a secret, treat it as a leak.

## What this skill never does
- It never echoes a secret.
- It never commits `.wrangler/` or `.dev.vars`.
- It never deploys when a check fails.
