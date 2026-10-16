# muse-cloudflare-deploy

Preflight a Cloudflare Pages/Workers deploy before it leaks assets.

## Who it's for
Anyone deploying to Cloudflare who has ever shipped `node_modules` as a static
asset, or deployed to the wrong target, and wants a guardrail.

## Install
The skills are folders in the umbrella repository; individual release archives
are not published yet. Clone the repository, verify the manifests, then copy the
skill folder:

```bash
git clone https://github.com/Git-FED/fed-os-muse-skills.git
cd fed-os-muse-skills
make verify
mkdir -p ~/workspace/custom-skills
cp -r skills/muse-cloudflare-deploy ~/workspace/custom-skills/
```

## Quick example
```bash
$ bash scripts/preflight.sh
==> dry-run deploy to /tmp/tmp.XXXX
dry-run size: 2.1M
OK: preflight passed

$ bash scripts/check-secrets.sh
OK: no tracked secrets
```

## What it will not do
- It will not deploy unless both checks pass.
- It will not print a secret.
- It will not commit `.wrangler/` or `.dev.vars`.

## Uninstall
Remove `~/workspace/custom-skills/muse-cloudflare-deploy/`.

## License
MIT — see [LICENSE](LICENSE).
