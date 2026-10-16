# Changelog

## [1.0.0] - 2026-10-16
### Added
- Initial release.
- `SKILL.md` playbook: verify → probe → cut → confirm.
- `scripts/cut.sh` — scale/crop to 1080x1920, H.264/AAC, `-crf 20`.
- `manifest.json` with `requires`, `capabilities`, and file hashes checked by
  the umbrella repository's `make verify` command.
