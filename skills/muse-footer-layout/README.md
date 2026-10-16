# muse-footer-layout

Classify links by visibility and produce a public footer plan plus a gated list.
No HTML is generated — the output is a structured plan.

## Who it's for
Anyone maintaining a public-facing footer for a Muse agent, site, or community
that has a mix of public, member-only, and private links.

## Install
1. Download the latest release.
2. Verify file hashes against `manifest.json:files`.
3. Drop the folder into `~/workspace/custom-skills/muse-footer-layout/`.

```bash
unzip muse-footer-layout-v1.0.0.zip -d ~/workspace/custom-skills/
```

## Quick example
```bash
$ bash scripts/classify.sh "https://www.fedpromptly.org"
Public

$ bash scripts/classify.sh "https://matrix.to/#/#fed-os:matrix.org"
Private

$ bash scripts/classify.sh "https://muse.ai/join"
Public
DISCLOSURE: referral
```

Ask the Muse agent: *"Build the public footer plan and gated list for FED-OS."*
It returns two sections — **Public footer** and **Gated** — and routes the
Matrix link through a gate spec instead of the footer.

## What it will not do
- It will not put a private or internal link in the footer.
- It will not put a checkout/OAuth URL anywhere — it resolves to the canonical
  landing page.
- It will not treat a referral link as an ordinary link; it flags the
  disclosure obligation.
- It will not generate HTML.

## Uninstall
Remove `~/workspace/custom-skills/muse-footer-layout/`.

## License
MIT — see [LICENSE](LICENSE).
