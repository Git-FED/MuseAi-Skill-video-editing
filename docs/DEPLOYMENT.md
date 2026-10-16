# Deployment

## The site
The site is static and lives in `site/`. There is no build step. GitHub Pages
serves `site/` directly via the root workflow at `.github/workflows/deploy.yml`.

Flow:
1. Push to `main` touching `site/**` or the deployment workflow.
2. The `guard` job checks for a stray CNAME, tracked secrets, and required site
   assets.
3. The `deploy` job uploads `site/` and publishes it to Pages.

## Skills
The skills are maintained as folders under `skills/` in this umbrella repository.
Each folder includes `.github/workflows/release.yml`, but GitHub does not run a
workflow from a nested folder. These files are templates for use after extracting
a skill into its own Git repository.

For local installation, clone this repository, run `make verify`, and copy the
chosen folder into `~/workspace/custom-skills/<skill-name>/`. Individual release
ZIPs are not currently published.

In a standalone skill repository, pushing a `v<version>` tag activates the
included template. It checks the tag against `manifest.json:version`, verifies
listed hashes, signs `manifest.json` with Minisign, and attaches the manifest and
`.minisig` signature to a GitHub release. It requires the repository secret
`MINISIGN_SECRET_KEY` and installs Minisign on the runner. It does not package or
upload the skill folder as a ZIP. A trusted public key and consumer verification
instructions still need to be published before signatures can be relied on.

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
