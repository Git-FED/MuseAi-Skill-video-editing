# AGENTS.md

Instructions for AI agents (Muse, Claude, others) working in this repo.

## What this repo is
A fleet of one-repo-per-skill packages for Muse agents, plus the static site
that presents them.

## The rules you must follow here
1. **No HTML in skill repos.** A skill's output is a plan, not markup. If a task
   asks for HTML, it belongs in `site/`, not `skills/`.
2. **No live credentials.** Never write a client ID, publishable key,
   buy-button ID, merchant ID, OAuth `state`, or `redirect_uri` into a tracked
   file or a URL. Use canonical handles.
3. **Canonical links only.** Reference platforms by handle
   (`patreon: fedpromptly`); resolve to a URL at render time.
4. **Disclose referrals.** Any link that pays the author carries
   `"disclosure": "referral"` and a plain-language line.
5. **No fake gates.** A client-side "I am 18+" checkbox is not verification.
6. **Verifiable hashes.** If you change a file listed in a skill manifest,
   update `manifest.json:files` and run `make verify`.

## How to add a skill
Follow the shared folder contract in `docs/adr/0001-one-repo-per-skill.md` and
keep the shape identical. Run `make verify && make guard && make icons` before
proposing.

## How to run the checks
```bash
make verify   # hashes
make guard    # CNAME + secrets
make icons    # favicon present in every page
```

## Never
- Never commit `.env`, `.wrangler/`, or `.dev.vars`.
- Never print a secret in a workflow.
- Never delete a `CNAME` file silently — report it.
