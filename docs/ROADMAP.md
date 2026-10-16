# Roadmap

## Shipped (v1.0.0)
- [x] Five production skills (video-editor, footer-layout, cname-guard,
      cloudflare-deploy, funding-buttons).
- [x] The 12-file skill contract, enforced by `release.yml`.
- [x] Public landing site with favicon and accessible neon/glass design.
- [x] Shared ruleset + pre-commit hooks.

## Next (v1.1)
- [ ] `muse-social-preview` — generate OG images from a template.
- [ ] `muse-skill-lint` — validate any skill folder against the contract.
- [ ] Sign + publish a `skills-index.json` so the installer can resolve versions.
- [ ] A `muse-skill-install` CLI that verifies hashes before dropping a skill in.

## Later (v2.0)
- [ ] Multi-skill bundles with a lockfile.
- [ ] A registry with per-skill provenance (who signed what, when).
- [ ] Server-side age-verification skill (real vendor, not a checkbox).

## Explicitly out of scope
- Shipping HTML inside skill repos.
- Storing any credential in a tracked file.
- Client-side "verification" that isn't verification.
