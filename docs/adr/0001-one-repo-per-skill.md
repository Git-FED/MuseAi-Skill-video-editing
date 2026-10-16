# ADR 0001 — One repo per skill

- Status: Accepted
- Date: 2026-10-16

## Context
We are building a fleet of skills for AI Muse agents. A skill is a folder the
agent reads and executes. We could ship all skills in one monorepo, or one repo
per skill.

## Decision
One repo per skill, each with its own release and its own version tag.

## Consequences
- Every skill repo is identical in shape, so the installer can assume a layout.
- A change to one skill cannot break another.
- Each skill can be versioned and signed independently.
- Cost: more repos to maintain. Mitigated by a strict, shared file contract.

## The contract
```
<skill-name>/
├── SKILL.md
├── manifest.json
├── README.md
├── LICENSE
├── SECURITY.md
├── CHANGELOG.md
├── .gitignore
├── .github/workflows/release.yml
├── references/   (optional)
└── scripts/      (optional)
```
If a file isn't load-bearing, it doesn't belong.
