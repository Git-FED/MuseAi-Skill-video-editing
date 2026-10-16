# Summary

## What this is

FED-OS Muse Skills is a fleet of small, auditable packages that teach an AI Muse
agent how to do one job each. Every skill follows the same shape — a `SKILL.md`
playbook, a `manifest.json`, a `README.md`, and a `scripts/` directory — so that
you can read a skill in one sitting and decide whether to trust it before you run
it.

## The five skills

| Skill | Job |
| --- | --- |
| `muse-video-editor` | Turn a video into a 1080×1920 vertical cut with ffmpeg. |
| `muse-footer-layout` | Classify a link as Public / Premium / Private and say where it belongs. |
| `muse-cname-guard` | Fail the build if a `CNAME` file is present (domain-hijack guard). |
| `muse-cloudflare-deploy` | Dry-run preflight and asset-leak detection before a deploy. |
| `muse-funding-buttons` | Resolve a funding handle to a class, a label, and a gate rule. |

## The six shared rules

Every skill obeys the same six rules. They are the reason the fleet is coherent
rather than a pile of scripts.

1. **One repo per skill.** One playbook, one manifest, one changelog, one release.
2. **No HTML in skill repos.** A skill's output is a plan, not markup.
3. **No live credentials.** Not client IDs, not publishable keys, not buy-button
   IDs, not merchant IDs, not OAuth `state` or `redirect_uri`. Secrets are read
   from the environment; the repo ships only an empty `.env.example`.
4. **Canonical links only.** Reference platforms by handle (`patreon: fedpromptly`)
   and resolve at render time. Never paste a live checkout URL.
5. **Disclose referrals.** Any link that pays the author carries
   `"disclosure": "referral"` and a plain-language line next to it.
6. **No fake gates.** A client-side "I am 18+" checkbox is not verification. Gate
   server-side or do not claim to gate.

## Integrity

Releases verify the SHA-256 hashes listed in `manifest.json:files` and sign the
manifest. You can re-check the hashes yourself with
`scripts/verify-hashes.sh`. A hash mismatch is a stop condition, not a warning.

## The public site

`site/` is a static, no-build-step landing page. It is accessible (WCAG-minded:
focus-visible, contrast, `prefers-reduced-motion`, a `backdrop-filter` fallback, a
skip link) and it wires a favicon three ways — SVG, ICO, and `apple-touch-icon`.
It is deliberately separate from the skill repos: the site is a website, and the
skills are plans.

## License

MIT. See [LICENSE](LICENSE). The code is free; funding is optional and never
changes what the software does. See [PRICING.md](PRICING.md).

## Where to start

- New here? Read [README.md](README.md), then [usage.md](usage.md).
- Want to install a skill? [docs/INSTALL.md](docs/INSTALL.md).
- Want to ship the site? [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).
- Found a problem? [SUPPORT.md](SUPPORT.md). Security? [SECURITY.md](SECURITY.md).
