# FED-OS Muse Skills

A fleet of **one-repo-per-skill** packages for AI Muse agents. Each skill is a
self-contained folder that a Muse agent reads, follows, and executes. No build
step, no package manager, no config — the `SKILL.md` does all the work.

This repository is the umbrella: it ships five production skills plus the public
landing site that presents them.

---

## What's in here

| Path | What it is |
| --- | --- |
| `skills/muse-video-editor/` | Cut, caption, and assemble vertical video with ffmpeg |
| `skills/muse-footer-layout/` | Classify links by visibility → public footer plan + gated list |
| `skills/muse-cname-guard/` | Refuse to ship a stray `CNAME` file that hijacks a domain |
| `skills/muse-cloudflare-deploy/` | Preflight a Cloudflare Pages/Workers deploy before it leaks assets |
| `skills/muse-funding-buttons/` | Plan funding surfaces by canonical handle — never a live checkout URL |
| `site/` | Static landing page (HTML + CSS + JS, favicon wired) |
| `.github/` | Issue templates, funding config, CI |
| `docs/` | Architecture decisions, roadmap, deploy/build/install notes |
| `prompts/` | Reusable generation prompts (landing page, social preview, wiki) |
| `scripts/` | Repo-level helper scripts |
| `promo/` | Comical, simple promotion images |

---

## The skill contract

Every skill folder is identical in shape. That sameness is the whole point — it
means the installer can assume a layout for skill number 1 and skill number 50.

```
<skill-name>/
├── SKILL.md            # the playbook the agent executes (the actual product)
├── manifest.json       # machine-readable ID, deps, capabilities, hashes
├── README.md           # human-facing install + usage
├── LICENSE             # MIT
├── SECURITY.md         # disclosure path
├── CHANGELOG.md        # version discipline
├── .gitignore
├── .github/
│   └── workflows/
│       └── release.yml # verify hashes → sign manifest → tag
├── references/         # data the SKILL.md reads (optional)
└── scripts/            # helper scripts the SKILL.md calls (optional)
```

If a file isn't load-bearing — if you can't say what breaks when it's removed —
it doesn't belong.

---

## Install a skill

1. Download the release for the skill you want.
2. Verify the file hashes against `manifest.json:files`.
3. Drop the folder into `~/workspace/custom-skills/<skill-name>/`.

```bash
# example
unzip muse-footer-layout-v1.0.0.zip -d ~/workspace/custom-skills/
```

Then ask your Muse agent to use it by name.

---

## The rules these skills encode

These are the guardrails the whole fleet shares. They came out of a long audit
of what *looks* like it belongs in a repo versus what actually does.

1. **No HTML in skill repos.** A skill's output is a *plan*, not markup.
2. **No live credentials, ever.** Client IDs, publishable keys, buy-button IDs,
   merchant IDs, OAuth `state`, and `redirect_uri` live server-side or in a
   gitignored `config.js` — never in a tracked file or a URL.
3. **Canonical links only.** Reference platforms by handle
   (`patreon: fedpromptly`), resolve to a live URL at render time.
4. **Disclose referrals.** Any link that pays you carries
   `"disclosure": "referral"` and a plain-language line above it.
5. **No fake gates.** A client-side "I am 18+" checkbox is not verification.
   Gate the content server-side or don't claim to gate at all.
6. **Hashes and signatures are enforced, not aspirational.** `release.yml`
   refuses to publish if `manifest.json:files` doesn't match the tree.

---

## Support

If these skills are useful and you want to try Muse itself, this is my referral
link:

- Join Muse: https://muse.ai/join — code `5F2V31`

*Disclosure: I receive a referral credit when someone signs up through this
link. It costs you nothing and doesn't change the price. The skills work
without it.*

---

## License

MIT — see [LICENSE](LICENSE).
