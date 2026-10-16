# Frequently Asked Questions

## What is a Muse skill, exactly?

A Muse skill is a small package that tells an AI agent how to do one job. In this
project, each package lives in a self-contained folder with a `SKILL.md`, a
`manifest.json` describing its requirements, a `README.md`, and any scripts or
references it actually uses. Skills produce plans or task-specific outputs; the
public landing site is separate from the skill folders.

## Why “one repository per skill”?

The design goal is for each skill to be independently readable, versioned, and
installable. Today, the five skill folders are staged together in this umbrella
repository. Each folder includes a release workflow template, but nested workflows
do not run from this umbrella. The current state and direction are in
[docs/adr/0001-one-repo-per-skill.md](docs/adr/0001-one-repo-per-skill.md).

## Why is there no HTML in the skill folders?

A skill that emits markup has quietly become a website generator, and a website
generator that ships in a “skill” is a website generator nobody reviews. Skills
produce plans. The public site in this repository is a separate, clearly labelled
thing. See [docs/adr/0002-no-html-in-skill-repos.md](docs/adr/0002-no-html-in-skill-repos.md).

## Does this project ship any credentials?

No. Not client IDs, not publishable keys, not buy-button IDs, not merchant IDs,
not OAuth `state` values, not `redirect_uri`s. Live credentials never belong in a
tracked file or a URL. Where a skill needs a secret, it reads it from the
environment at run time and the repository only ever contains an empty
`.env.example`. See [docs/adr/0003-no-live-credentials.md](docs/adr/0003-no-live-credentials.md).

## What is a “canonical link”?

A canonical link points at a platform by its stable handle — for example
`patreon: fedpromptly` — and lets the renderer resolve it to a real URL at the
moment it is shown. It is the opposite of pasting a live checkout URL, which can
carry a session, an amount, or a credential in its query string. Canonical links
are boring on purpose; boring links cannot leak.

## Why do some links say “referral”?

Because some of them pay the maintainer, and hiding that would be dishonest. Every
link that pays carries a machine-readable disclosure and a plain-language line
next to it. If a link does not pay, it does not say that. See the `_rules.referrals`
block in each skill's reference data.

## Is there an age gate?

No, and there is a reason. A checkbox that says “I am 18+” is not verification —
it is a checkbox. This project does not ship fake gates. If content genuinely
needs to be restricted, that has to happen on the server, and until it does, the
content is not shipped as “gated.” A client-side checkbox that claims to verify
anything is worse than no gate, because it lies.

## How do I install a skill?

See [docs/INSTALL.md](docs/INSTALL.md) and the worked example in
[usage.md](usage.md). Clone the umbrella repository, run `make verify`, copy the
chosen skill directory into your agent's skills folder, and point your agent at
`SKILL.md`.

## How do I check package hashes?

Run `make verify` from the repository root. It checks whether the files listed in
each `manifest.json:files` match their recorded SHA-256 values. This confirms
local package consistency, not publisher identity. A standalone skill repository
can use its nested workflow template to publish a signed manifest, but this
umbrella does not run those workflows. A trusted public key and verification
guide are also still needed before signatures can be relied on.

## Are skill ZIPs published?

No. The current release templates publish `manifest.json` and its Minisign
signature, not an archive of the skill folder. For now, install from the umbrella
repository using the clone-and-copy instructions.

## Can I use these skills commercially?

Yes. The code is MIT-licensed. See [LICENSE](LICENSE). Attribution is welcome but
not required by the license; the shared rules, however, are not optional if you
want to call your fork part of this fleet.

## Something in here is wrong or unsafe. What do I do?

If it is a security problem, report it privately per [SECURITY.md](SECURITY.md).
If it is a correctness problem, open an issue. Corrections are welcome.
