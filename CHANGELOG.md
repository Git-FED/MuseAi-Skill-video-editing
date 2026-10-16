# Changelog

All notable changes to the FED-OS Muse Skills fleet are documented here.
This project adheres to [Semantic Versioning](https://semver.org/) and
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed
- Replaced the promotion set and social preview with coordinated, optimized
  artwork; the asset script now preserves the hand-finished social card.
- Replaced the placeholder release downloads with the repository's actual
  clone-and-copy installation flow.
- Removed injected third-party scripts from the static site and its fragments.

### Added
- `docs/adr/0004-no-fake-gates.md` — a client-side age checkbox is not
  verification; gate content server-side, never a payment button.
- `skills/muse-funding-buttons/references/embeds.md` — why PayPal/Stripe/Ko-fi/
  Buy Me a Coffee embeds and widget ids are never stored; handles resolve to
  buttons at render time.
- `careers@fedpromptly.com` added to the visible footer and landing contact list
  (all four public addresses now present).

### Notes
- `build.yml` is intentionally absent — see `docs/BUILD.md` ("there is nothing
  to build").

## [1.0.0] - 2026-10-16

### Added
- `muse-video-editor` — vertical video cut + caption skill (ffmpeg).
- `muse-footer-layout` — link visibility classifier and footer planner.
- `muse-cname-guard` — refuses to ship a stray `CNAME` file.
- `muse-cloudflare-deploy` — preflight for Pages/Workers deploys.
- `muse-funding-buttons` — funding plan by canonical handle, never a live URL.
- Public landing site (`site/`) with favicon, accessible neon/glass design.
- Per-skill manifests that record file hashes, checked with `make verify`.
- Shared ruleset: no HTML in skill repos, no live credentials, canonical links
  only, referral disclosure, no fake gates, enforced hashes.

### Security
- `.env.example` may contain only empty values.
- Local `config.js` files are gitignored; `.env.example` contains no live values.
- No OAuth `state`, `client_id`, `redirect_uri`, publishable keys, buy-button
  IDs, or merchant IDs are stored in any tracked file.

[Unreleased]: https://github.com/Git-FED/fed-os-muse-skills/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/Git-FED/fed-os-muse-skills/releases/tag/v1.0.0
