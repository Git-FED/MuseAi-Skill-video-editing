# Summary

## What this is

FED-OS Muse Skills is an umbrella repository with five small, auditable skill
folders for AI Muse agents. Each folder centers on a `SKILL.md` playbook and a
`manifest.json`; read the package before installing it.

## The five skills

| Skill | Job |
| --- | --- |
| `muse-video-editor` | Turn a video into a 1080×1920 vertical cut with ffmpeg. |
| `muse-footer-layout` | Classify a link as Public / Premium / Private and say where it belongs. |
| `muse-cname-guard` | Fail the build if a `CNAME` file is present (domain-hijack guard). |
| `muse-cloudflare-deploy` | Dry-run preflight and asset-leak detection before a deploy. |
| `muse-funding-buttons` | Resolve a funding handle to a class, a label, and a gate rule. |

## Shared rules

Every skill follows the same core package shape: one folder per skill, no HTML in
skill folders, no live credentials, canonical links only, clear referral
disclosures, no fake gates, and verifiable file hashes.

## Integrity

Run `make verify` from the umbrella repository to compare package files against
the SHA-256 values recorded in each `manifest.json:files`. This checks local
consistency; it does not authenticate a publisher. Each skill carries a nested
release workflow template, but those workflows do not run from the umbrella. In a
standalone skill repository, a tagged release can publish a signed manifest and
signature—not a skill ZIP. A trusted public-key distribution path is still needed
before consumers can verify signatures.

## The public site

`site/` is a static, no-build-step landing page. It is accessibility-minded, with
visible keyboard focus, contrast-conscious text, reduced-motion support, a
`backdrop-filter` fallback, and a skip link. It is separate from the skill folders.

## License

MIT. See [LICENSE](LICENSE). The code is free; funding is optional and never
changes what the software does. See [PRICING.md](PRICING.md).

## Where to start

- New here? Read [README.md](README.md), then [usage.md](usage.md).
- Want to install a skill? [docs/INSTALL.md](docs/INSTALL.md).
- Want to ship the site? [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).
- Found a problem? [SUPPORT.md](SUPPORT.md). Security? [SECURITY.md](SECURITY.md).
