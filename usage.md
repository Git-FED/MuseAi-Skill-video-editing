# Usage

This is a worked walkthrough. It takes one skill — `muse-video-editor` — from a
fresh clone to a finished vertical video, and shows the shape every other skill
follows. Nothing here requires a credential, an account, or a network call.

## 1. Get the code

```bash
git clone https://github.com/Git-FED/fed-os-muse-skills.git
cd fed-os-muse-skills
```

## 2. Look before you run

Every skill is readable in one sitting. Read the playbook and the manifest first —
this is the point of keeping one self-contained folder per skill.

```bash
cat skills/muse-video-editor/SKILL.md
cat skills/muse-video-editor/manifest.json
```

The manifest tells you what the skill needs. For `muse-video-editor` it looks like
this (abbreviated):

```json
{
  "name": "muse-video-editor",
  "requires": { "bin": ["ffmpeg"], "env": [] }
}
```

`requires.bin` lists the external binaries. `requires.env` is empty — this skill
needs no secret. When a skill does need one, `requires.env` names the variable and
the repository only ships an empty `.env.example`.

## 3. Check the requirements

```bash
command -v ffmpeg || echo "install ffmpeg first"
```

If a binary is missing, install it with your package manager. The skill will not
try to install it for you, and it will not silently fall back to something else.

## 4. Verify the manifest hashes (optional but recommended)

Check the files in the current checkout against their recorded hashes:

```bash
make verify
```

This checks all skill folders listed in the repository's manifests. It confirms
file consistency, not publisher identity. Each skill folder carries a release
workflow template, but GitHub does not run nested workflows from this umbrella.
If extracted into a standalone repository, the template can sign a tagged
manifest; consumers still need a trusted public key to verify it. If anything
does not match, stop and investigate.

## 5. Run the skill's script directly

Each skill ships the small script its playbook describes. You can run it by hand to
see exactly what it does:

```bash
bash skills/muse-video-editor/scripts/cut.sh input.mp4 out/vertical.mp4
```

What happens:

1. It checks the input exists. If not, it exits `2` with `MISSING_INPUT`.
2. It runs `ffmpeg` to scale-and-crop to 1080×1920, H.264, AAC 128k.
3. If `ffmpeg` fails, it exits `1` with `FFMPEG_FAILED`.
4. If the output is empty, it exits `3` with `EMPTY_OUTPUT`.
5. On success it prints the output path and exits `0`.

The script never invents a success. If it cannot do the job, it says so and stops.

## 6. Let an agent use the skill

Point your Muse agent at the skill directory. The agent reads `SKILL.md` for the
plan, `manifest.json` for the requirements, and the `scripts/` directory for the
mechanics. The skill's job is to produce a **plan** and a decision — which cut,
which aspect ratio, which output — and then to run the boring, deterministic script
that carries it out.

## 7. Classify a link (a second skill, to show the pattern)

`muse-footer-layout` takes a URL and tells you how it should be treated in a footer:

```bash
bash skills/muse-footer-layout/scripts/classify.sh "https://patreon.com/checkout/abc123"
# Premium
# RULE: checkout_urls — never-footer; swap to canonical landing page
```

```bash
bash skills/muse-footer-layout/scripts/classify.sh "https://www.patreon.com/c/FEDpromptly"
# Premium
# DISCLOSURE: referral
```

The first URL is a live checkout — it is refused and told to become a canonical
landing page. The second is the canonical handle, and it carries its referral
disclosure. That is the rule in action: **canonical links only, disclose referrals.**

## 8. Where to go next

- [docs/INSTALL.md](docs/INSTALL.md) — installing a skill into an agent
- [docs/BUILD.md](docs/BUILD.md) — verification and repository checks
- [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) — shipping the public site
- [FAQ.md](FAQ.md) — the questions people actually ask
- [SUPPORT.md](SUPPORT.md) — how to get help

## A worked failure, on purpose

Run the classifier on a URL nobody has classified:

```bash
bash skills/muse-footer-layout/scripts/classify.sh "https://example.com/whatever"
# UNCLASSIFIED: https://example.com/whatever   (exit 3)
```

The tool does not guess. An unknown link is an unknown link, and it exits non-zero
so a pipeline can catch it. Every skill in this fleet behaves the same way: it
prefers a loud failure to a quiet guess.
