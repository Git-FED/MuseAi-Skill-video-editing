# Changelog

## [1.0.0] - 2026-10-16
### Added
- Initial release.
- `SKILL.md` playbook: verify → classify handle → assemble ordered plan.
- `references/funding-links.json` — 8 handles plus `_rules` (checkout, referral).
- `references/embeds.md` — why PayPal/Stripe/Ko-fi/BMC embeds and widget ids are
  never stored; handles resolve to buttons at render time.
- `scripts/classify.sh` — handle → class/label/gate, with checkout-URL resolution.
- Rules: no credentials in plans, canonical handles only, no age-gated payment.
