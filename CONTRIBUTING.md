# Contributing

Thanks for helping build the fleet. This project has a strict shape on purpose —
read this before opening a PR.

## Ground rules
1. **No HTML in skill repos.** Plans, not markup.
2. **No credentials.** Ever. Not in a file, not in a URL.
3. **Canonical handles.** Reference platforms by handle, resolve at render time.
4. **Disclose referrals.** A link that pays you gets a disclosure line.
5. **Keep the 12-file contract.** New skills copy the shape exactly.

## Adding a skill
1. Create `skills/muse-<name>/` with the contract from
   [docs/adr/0001](docs/adr/0001-one-repo-per-skill.md).
2. Write `SKILL.md` with: what it does → prerequisites → verify environment →
   steps → never assume → output → failure handling.
3. Fill `manifest.json`: `requires`, `capabilities`, `files{}`, `files_excluded{}`.
4. Add `references/` and `scripts/` only if the SKILL.md uses them.
5. Run `make verify && make guard && make icons`.

## Changing an existing skill
- Bump `version` in `manifest.json` and `CHANGELOG.md`.
- Recompute `manifest.json:files` hashes for any executable content you changed.
- The tag must match `manifest.json:version` or `release.yml` fails.

## Commit style
Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `security:`.

## Code of conduct
By participating you agree to [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
