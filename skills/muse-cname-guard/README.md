# muse-cname-guard

Refuse to ship a stray `CNAME` file that silently hijacks a domain.

## Who it's for
Anyone deploying to GitHub Pages (or any static host) who wants a guardrail
against a `CNAME` file quietly repointing the site.

## Install
The skills are folders in the umbrella repository; individual release archives
are not published yet. Clone the repository, verify the manifests, then copy the
skill folder:

```bash
git clone https://github.com/Git-FED/fed-os-muse-skills.git
cd fed-os-muse-skills
make verify
mkdir -p ~/workspace/custom-skills
cp -r skills/muse-cname-guard ~/workspace/custom-skills/
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
