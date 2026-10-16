# ADR 0001 — One repository per skill

- Status: Accepted
- Date: 2026-10-16

## Context
The project maintains a fleet of skills for AI Muse agents. A skill is a folder
the agent reads and executes. Each skill is designed to be independently
installable and versioned. The current GitHub repository is an umbrella that
stages all five skill folders and the public landing site.

## Decision
Keep each skill self-contained in `skills/<skill-name>/` and maintain the shared
package contract. The intended production layout is one Git repository per skill.
Until extraction happens, this umbrella is the working source tree.

## Consequences
- Each skill folder has the same core files so consumers can install it on its
  own.
- Each folder includes a release workflow template; nested workflows do not run
  from the umbrella repository.
- In a standalone skill repository, the template can verify a version tag and
  hashes, sign the manifest, and publish the manifest plus its signature.
- Release templates do not create skill ZIPs, and consumers still need a trusted
  public-key distribution path to verify signatures.

## Current folder contract
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
