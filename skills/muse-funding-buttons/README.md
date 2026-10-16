# muse-funding-buttons

Plan funding surfaces by canonical handle — never a live checkout URL.

## Who it's for
Anyone with more than one funding path (sponsors, Patreon, Ko-fi, tips,
subscriptions, crypto) who wants a single plan instead of copy-pasted embeds
across N pages.

## Install
The skills are folders in the umbrella repository; individual release archives
are not published yet. Clone the repository, verify the manifests, then copy the
skill folder:

```bash
git clone https://github.com/Git-FED/fed-os-muse-skills.git
cd fed-os-muse-skills
make verify
mkdir -p ~/workspace/custom-skills
cp -r skills/muse-funding-buttons ~/workspace/custom-skills/
```

## Quick example
```bash
$ bash scripts/classify.sh "patreon:fedpromptly"
Premium
label: Patreon
gate: tiers

$ bash scripts/classify.sh "https://www.patreon.com/checkout/16145898/28759937?state=..."
RESOLVED: https://www.patreon.com/checkout/... -> (canonical handle)
RULE: checkout_urls — never-plan; resolve to canonical handle
```

## What it will not do
- It will not store or emit a client ID, publishable key, buy-button ID, widget
  id, image-button token, or merchant ID. See
  [`references/embeds.md`](references/embeds.md).
- It will not plan a live checkout URL.
- It will not gate a payment button behind an age check (see ADR 0004).
- It will not render HTML.

## Uninstall
Remove `~/workspace/custom-skills/muse-funding-buttons/`.

## License
MIT — see [LICENSE](LICENSE).
