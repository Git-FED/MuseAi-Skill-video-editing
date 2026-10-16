# Deployment

## The site
The site is static and lives in `site/`. There is no build step. GitHub Pages
serves `site/` directly via `.github/workflows/deploy.yml`.

Flow:
1. Push to `main` touching `site/**`.
2. `guard` job runs the fleet's safety checks (CNAME, secrets, icons).
3. `deploy` job uploads `site/` and publishes to Pages.

## A skill
Skills are not "deployed" — they are released.

1. Bump `version` in `manifest.json` and `CHANGELOG.md`.
2. Compute `sha256` for each file in `manifest.json:files`.
3. Commit, then tag `v<version>` (must match `manifest.json:version`).
4. `release.yml` verifies the tag, verifies hashes, signs the manifest with
   minisign, and uploads `manifest.json` + `manifest.json.minisig`.

Consumers download the release, verify hashes against `manifest.json:files`,
then drop the folder into `~/workspace/custom-skills/<skill-name>/`.

## Cloudflare (optional)
If the site is served from Cloudflare instead, run the preflight first:

```bash
bash skills/muse-cloudflare-deploy/scripts/preflight.sh
bash skills/muse-cloudflare-deploy/scripts/check-secrets.sh
```

Never commit `.wrangler/` or `.dev.vars`. Tokens live in the environment.

## The one rule
Credentials live server-side. A deploy pipeline never prints a secret, and a
tracked file never contains one.
