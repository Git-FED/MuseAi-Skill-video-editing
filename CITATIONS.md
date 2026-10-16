# Citations & References

This file records where the ideas in this project come from, so that a reader can
check the reasoning rather than take it on faith. It is deliberately short: a
skill fleet should cite the things it actually leans on, not pad a bibliography.

## Standards and specifications

- **Semantic Versioning 2.0.0** — the version numbers in every `manifest.json`.
  <https://semver.org/spec/v2.0.0.html>
- **SHA-256 (FIPS 180-4)** — the hash algorithm used for `manifest.json:files`
  and verified by `scripts/verify-hashes.sh`.
  <https://csrc.nist.gov/publications/detail/fips/180/4/final>
- **minisign** — the signing tool referenced by the release workflow.
  <https://jedisct1.github.io/minisign/>
- **Web Content Accessibility Guidelines (WCAG) 2.2** — the source of the
  contrast, focus-visible, and reduced-motion requirements the site follows.
  <https://www.w3.org/TR/WCAG22/>
- **`prefers-reduced-motion`** — the media query the site uses to respect a user's
  motion preference.
  <https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion>
- **`rel="canonical"`** and link-handle conventions — the basis for the
  "canonical link, not checkout URL" rule.
  <https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls>

## Guidance on disclosure

- **U.S. Federal Trade Commission, "Native Advertising: A Guide for Businesses"**
  and the Endorsement Guides — the reason every paying link carries a plain-language
  disclosure.
  <https://www.ftc.gov/business-guidance/resources/native-advertising-guide-businesses>
- **FTC Endorsement Guides (16 CFR Part 255)** — the rule that a material
  connection must be disclosed clearly and conspicuously.
  <https://www.ftc.gov/legal-library/browse/rules/guides-concerning-use-endorsements-testimonials-advertising>

## Tools wrapped by skills

- **ffmpeg** — wrapped by `muse-video-editor`. <https://ffmpeg.org/>
- **jq** — used by `muse-footer-layout` and `muse-funding-buttons` to read
  reference JSON. <https://jqlang.github.io/jq/>
- **Wrangler** — referenced by `muse-cloudflare-deploy` for dry-run preflight.
  <https://developers.cloudflare.com/workers/wrangler/>

## Project-internal references

- [docs/adr/0001-one-repo-per-skill.md](docs/adr/0001-one-repo-per-skill.md)
- [docs/adr/0002-no-html-in-skill-repos.md](docs/adr/0002-no-html-in-skill-repos.md)
- [docs/adr/0003-no-live-credentials.md](docs/adr/0003-no-live-credentials.md)

## How to add a citation

If you introduce a claim, a rule, or a dependency, cite it here in the same pull
request. A rule with no source is a rule someone has to guess at, and this project
would rather show its work.
