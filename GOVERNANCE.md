# Governance

## Model
Benevolent maintainer. This is a small project with a clear contract; decisions
are made by the maintainer, in public, with an ADR when a decision changes the
contract.

## Roles
- **Maintainer** — merges changes, cuts releases, signs manifests, holds the
  signing key. See [MAINTAINERS.md](MAINTAINERS.md).
- **Contributor** — anyone who opens a PR that follows
  [CONTRIBUTING.md](CONTRIBUTING.md).

## How decisions are made
- Anything that changes the 12-file contract → an ADR in `docs/adr/`.
- Anything that adds a credential surface → rejected, per
  [ADR 0003](docs/adr/0003-no-live-credentials.md).
- Anything that adds HTML to a skill repo → rejected, per
  [ADR 0002](docs/adr/0002-no-html-in-skill-repos.md).

## Releases
Tag-driven. The tag must match `manifest.json:version`. `release.yml` verifies
hashes and signs the manifest before publishing. A release that fails
verification does not ship.

## Changing governance
Open a PR against this file. One maintainer approval required.
