# Changelog

## [1.0.0] - 2026-10-16
### Added
- Initial release.
- `SKILL.md` playbook: verify → dry-run → secrets check → deploy.
- `scripts/preflight.sh` — dry-run size report + asset-leak detection.
- `scripts/check-secrets.sh` — tracked `.env`, `.dev.vars`, workflow secret prints.
- `references/wrangler-patterns.md` — the failure modes this catches.
