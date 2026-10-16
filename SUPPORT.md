# Support

There are four ways to get help with FED-OS Muse Skills, in order of how fast
they usually are.

## 1. Read the docs first

Most questions are answered somewhere in this repository. The fastest path is
usually:

- [README.md](README.md) — what the project is and the skill contract
- [docs/INSTALL.md](docs/INSTALL.md) — getting a skill into a Muse agent
- [docs/BUILD.md](docs/BUILD.md) — packaging and release mechanics
- [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) — shipping the public site
- [FAQ.md](FAQ.md) — the questions people actually ask
- [usage.md](usage.md) — a worked, copy-pasteable walkthrough

## 2. Search the issues

Someone has probably hit the same wall. Search the open and closed issues before
opening a new one. If your problem is a bug, include the skill name, the version
from its `manifest.json`, and the exact command you ran.

## 3. Open an issue

Use the issue templates under `.github/ISSUE_TEMPLATE/`:

- **Bug report** — something a skill does wrong
- **Feature request** — a new skill or a new capability for an existing one
- **Custom** — anything that does not fit the two above

Please do not paste secrets, tokens, client IDs, or private URLs into an issue.
If a bug only reproduces with a credential, describe the shape of the credential
(what kind it is, where it is read from) rather than its value.

## 4. Security issues

Do **not** open a public issue for a security problem. Follow
[SECURITY.md](SECURITY.md) and report it privately. This matters more than usual
here, because this project's whole point is that it never ships live credentials —
so a report that a credential leaked is treated as a top-priority incident.

## What we can and cannot help with

We can help with anything in this repository: the skills, the scripts, the site,
the release workflow, and the shared rules.

We cannot help with problems inside third-party tools (`ffmpeg`, `jq`, `wrangler`,
a hosting provider's dashboard) beyond pointing you at the right place to ask. We
also cannot help you recover an account or a domain — that lives with the provider,
not with us.

## Funding the work

Support is free and always will be. If you want to fund it anyway, see
[.github/FUNDING.yml](.github/FUNDING.yml) and [PRICING.md](PRICING.md). Funding
never buys support priority, and it never changes what a skill is allowed to do.
