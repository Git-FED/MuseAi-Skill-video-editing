# Contributing

Thanks for helping build the fleet. This project has a strict shape on purpose —
read this before opening a PR.

## Ground rules
1. **No HTML in skill folders.** Plans, not markup.
2. **No credentials.** Ever. Not in a file, not in a URL.
3. **Canonical handles.** Reference platforms by handle, resolve at render time.
4. **Disclose referrals.** A link that pays you gets a disclosure line.
5. **Use the shared skill-folder contract.** New skills follow the shape in
   [docs/adr/0001](docs/adr/0001-one-repo-per-skill.md).

## Adding a skill
1. Create `skills/muse-<name>/` with the shared files listed in ADR 0001.
2. Write `SKILL.md` with: what it does → prerequisites → verify environment →
   steps → never assume → output → failure handling.
3. Fill `manifest.json`: `requires`, `capabilities`, `files{}`, `files_excluded{}`.
4. Add `references/` and `scripts/` only if the SKILL.md uses them.
5. Run `make verify && make guard && make icons`.

## Changing an existing skill
- Bump `version` in `manifest.json` and `CHANGELOG.md` when a package release is
  intended.
- Recompute `manifest.json:files` hashes for files listed in `files`.
- Verify the package with `make verify`.

Each skill contains a release workflow template. It is nested in the umbrella
repository, so GitHub does not run it here. When a skill is extracted into its
own repository, a `v<version>` tag can activate the template to verify and sign
the manifest. The template publishes `manifest.json` and its signature, not a
ZIP archive. Before relying on a published signature, the maintainer must provide
a trusted public key and verification instructions.

## Commit style
Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `security:`.

## Code of conduct
By participating you agree to [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
