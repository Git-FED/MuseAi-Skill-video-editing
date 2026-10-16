# Roadmap

## Current (v1.0.0)
- [x] Five production skill folders (video-editor, footer-layout, cname-guard,
      cloudflare-deploy, funding-buttons).
- [x] Shared skill-folder contract, manifest hashes, and local verification.
- [x] Per-skill release workflow templates for standalone repositories.
- [x] Public static landing site and GitHub Pages deployment.
- [x] Shared ruleset and pre-commit hooks.

## Next
- [ ] Decide whether to extract each skill into its own Git repository and
      activate its nested release workflow.
- [ ] Publish and document a trusted Minisign public key before asking consumers
      to rely on signed manifests.
- [ ] Decide whether releases should include skill-folder archives; the current
      templates publish only `manifest.json` and its signature.
- [ ] `muse-social-preview` — generate OG images from a template.
- [ ] `muse-skill-lint` — validate any skill folder against the contract.
- [ ] Sign and publish a `skills-index.json` so an installer can resolve versions.
- [ ] A `muse-skill-install` CLI that verifies hashes before installing a skill.

## Later
- [ ] Multi-skill bundles with a lockfile.
- [ ] A registry with per-skill provenance (who signed what, when).
- [ ] Server-side age-verification skill (real vendor, not a checkbox).

## Explicitly out of scope
- Shipping HTML inside skill folders.
- Storing any credential in a tracked file.
- Client-side "verification" that isn't verification.
