# TODO — Catch-all audit ("just in case we missed anything on this list add it")

## Audit the catch-all list from the transcript
- [x] FUNDING.yml — confirmed correct (canonical handles, no credentials)
- [x] Ko-fi embed (YOUR_USERNAME placeholder) — reconciled as references/embeds.md, not HTML
- [x] Neon-glassmorphism master prompt — confirmed in prompts/landing-page.md
- [x] Age-verification gate — added docs/adr/0004-no-fake-gates.md
- [x] PayPal + Stripe embeds — added references/embeds.md explaining credential prohibition
- [x] Social preview — confirmed present
- [x] Favicon — confirmed present + wired (SVG/ICO/apple-touch/PNG)
- [x] Portfolio tree — confirmed site/data/portfolio.json
- [x] Ko-fi widget W3T61ZU5TK / BMC image button — confirmed NOT added as embeds; documented why
- [x] Four emails — added careers@fedpromptly.com to footer + index (all four now present)
- [x] build.yml — confirmed intentionally omitted; noted in docs/BUILD.md + CHANGELOG

## Add missing items in corrected form
- [x] Create docs/adr/0004-no-fake-gates.md
- [x] Create skills/muse-funding-buttons/references/embeds.md
- [x] Add careers@fedpromptly.com wherever emails are listed
- [x] Note build.yml omission (docs/BUILD.md already + CHANGELOG)

## Repackage & verify
- [x] Re-run scripts/validate_icons.sh
- [x] Re-run scripts/verify-hashes.sh (16 hashes verified)
- [x] Re-create fed-os-muse-skills.zip
- [x] Verify zip integrity + file count (123 files, ZIP OK)
- [x] complete with attachments + live URL
