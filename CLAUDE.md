# CLAUDE.md

Guidance for Claude when working in this repository. See also [AGENTS.md](AGENTS.md).

## Repo shape
- `skills/` — five self-contained skill folders following the shared contract.
- `site/` — static landing page (HTML/CSS/JS, favicon wired).
- `.github/` — issue templates, funding, and GitHub Pages deployment CI.
- `docs/` — ADRs and operational docs.
- `prompts/` — reusable generation prompts.
- `scripts/` — repo-level checks.

## Conventions
- Bash: `#!/usr/bin/env bash` + `set -euo pipefail`. Exit non-zero with a
  single-line stderr message. No color, no prompts, no progress bars.
- JSON: 2-space indent. `manifest.json` lists `files{}` (hashed) and
  `files_excluded{}` (docs) — they must not overlap.
- Markdown: keep it prose-first; lists only where they earn it.

## Guardrails (non-negotiable)
- No HTML/CSS/JS under `skills/`.
- No credentials in any tracked file.
- Canonical handles, not checkout URLs.
- Referral links get a disclosure line.
- Update hashes when executable content changes.

## Before you propose a change
```bash
make verify && make guard && make icons
```
