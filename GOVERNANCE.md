# Governance

## Model
Benevolent maintainer. This is a small project with a clear contract; decisions
are made by the maintainer, in public, with an ADR when a decision changes the
contract.

## Roles
- **Maintainer** — reviews changes, maintains package versions and manifests,
  and manages the GitHub Pages deployment. See [MAINTAINERS.md](MAINTAINERS.md).
- **Contributor** — anyone who opens a PR that follows
  [CONTRIBUTING.md](CONTRIBUTING.md).

## How decisions are made
- Changes to the shared skill-folder contract are recorded in `docs/adr/`.
- Changes that add a credential surface follow
  [ADR 0003](docs/adr/0003-no-live-credentials.md).
- HTML inside a skill folder is out of scope under
  [ADR 0002](docs/adr/0002-no-html-in-skill-repos.md).

## Releases
The umbrella repository’s root GitHub Actions workflow deploys the static site
through Pages. Each skill folder also contains a `release.yml` template intended
for use after that folder is extracted into its own repository. Nested workflows
do not run from this umbrella repository.

When active in a standalone skill repository, the template checks the version
against the tag and verifies manifest hashes, signs `manifest.json` with
Minisign, and uploads the manifest and signature. It does not publish a skill ZIP.
The repository has not yet documented a trusted public-key distribution path;
consumers must not treat a signature as verified until they can obtain and trust
the matching public key independently. Run `make verify` for local hash checks.

## Changing governance
Open a PR against this file. One maintainer approval required.
