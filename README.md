# FED-OS Muse Skills

A fleet of self-contained skill packages for AI Muse agents. Each skill lives in
its own folder, follows a shared contract, and is ready to install on its own.
This umbrella repository contains five production skills and the static site
that presents them. No build step or package manager is required.

---

## What's in here

| Path | What it is |
| --- | --- |
| `skills/muse-video-editor/` | Cut, caption, and assemble vertical video with ffmpeg |
| `skills/muse-footer-layout/` | Classify links by visibility → public footer plan + gated list |
| `skills/muse-cname-guard/` | Refuse to ship a stray `CNAME` file that hijacks a domain |
| `skills/muse-cloudflare-deploy/` | Preflight a Cloudflare Pages/Workers deploy before it leaks assets |
| `skills/muse-funding-buttons/` | Plan funding surfaces by canonical handle — never a live checkout URL |
| `site/` | Multi-page static site: home, skills, field guide, community, and custom 404 |
| `.github/` | Issue templates, funding config, CI |
| `docs/` | Architecture decisions, roadmap, deploy/build/install notes |
| `prompts/` | Reusable generation prompts (landing page, social preview, wiki) |
| `scripts/` | Repo-level helper scripts |
| `promo/` | Coordinated promotion images |

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
├── references/         # data the SKILL.md reads (optional)
└── scripts/            # helper scripts the SKILL.md calls (optional)
```

If a file isn't load-bearing — if you can't say what breaks when it's removed —
it doesn't belong.

---

## Install a skill

The umbrella repository does not publish individual skill archives. Clone it,
verify the package manifests, and copy the folder you want:

```bash
git clone https://github.com/Git-FED/fed-os-muse-skills.git
cd fed-os-muse-skills
make verify
mkdir -p ~/workspace/custom-skills
cp -r skills/muse-footer-layout ~/workspace/custom-skills/
```

Then ask your Muse agent to use the skill by name.

---

## The rules these skills encode

These are the guardrails the whole fleet shares. They came out of a long audit
of what *looks* like it belongs in a repo versus what actually does.

1. **No HTML in skill repos.** A skill's output is a *plan*, not markup.
2. **No live credentials, ever.** Client IDs, publishable keys, buy-button IDs,
   merchant IDs, OAuth `state`, and `redirect_uri` are read from the environment
   when needed — never from a tracked file or a URL.
3. **Canonical links only.** Reference platforms by handle
   (`patreon: fedpromptly`), resolve to a live URL at render time.
4. **Disclose referrals.** Any link that pays you carries
   `"disclosure": "referral"` and a plain-language line above it.
5. **No fake gates.** A client-side "I am 18+" checkbox is not verification.
   Gate the content server-side or don't claim to gate at all.
6. **Hashes are checked.** `make verify` checks recorded file hashes against
   each skill's current contents.

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
