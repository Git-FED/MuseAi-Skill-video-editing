# muse-cname-guard

Refuse to ship a stray `CNAME` file that silently hijacks a domain.

## Who it's for
Anyone deploying to GitHub Pages (or any static host) who wants a guardrail
against a `CNAME` file quietly repointing the site.

## Install
1. Download the latest release.
2. Verify file hashes against `manifest.json:files`.
3. Drop the folder into `~/workspace/custom-skills/muse-cname-guard/`.

```bash
unzip muse-cname-guard-v1.0.0.zip -d ~/workspace/custom-skills/
```

## Quick example
```bash
$ bash scripts/check-cname.sh
OK: no CNAME file

$ touch CNAME && bash scripts/check-cname.sh
FORBIDDEN: CNAME file present at ./CNAME
NOTE: deleting the file does not clear the hosting provider's saved
      custom domain. Check that setting separately.
```

## What it will not do
- It will not delete the file for you.
- It will not claim the domain is unset just because the file is gone.

## Uninstall
Remove `~/workspace/custom-skills/muse-cname-guard/`.

## License
MIT — see [LICENSE](LICENSE).
