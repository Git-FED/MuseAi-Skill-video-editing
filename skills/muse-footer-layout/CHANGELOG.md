# Changelog

## [1.0.0] - 2026-10-16
### Added
- Initial release.
- `SKILL.md` playbook: verify → classify → bucket → emit plan.
- `references/links.json` — 21 entries plus `_rules` (checkout, proxy, referral).
- `references/footer-layout.md` — human-readable source of truth.
- `scripts/classify.sh` — URL → visibility class, with rule short-circuits.
- Hard rules: no checkout/OAuth URLs, no Matrix in footer, referral disclosure.
