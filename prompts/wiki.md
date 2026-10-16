# Prompt — wiki

Use this to generate the repository wiki from the source of truth.

---

Generate a wiki for the FED-OS Muse Skills fleet. Pull from, in order of
authority: each skill's `SKILL.md`, `manifest.json`, and `README.md`, then the
root `docs/`.

**Pages:**
1. **Home** — what the fleet is, the skill contract, the shared rules.
2. **Install** — mirror `docs/INSTALL.md`.
3. **Skills** — one page per skill: what it does, prerequisites, steps,
   never-assume rules, output, failure handling.
4. **Packages** — mirror `docs/DEPLOYMENT.md`; explain clone-and-copy
   installation, local manifest verification, and that nested release workflows
   are templates (not active here) and do not create ZIP archives.
5. **Security** — the no-credentials rule, how to report a leak.
6. **FAQ** — mirror `FAQ.md`.

**Rules:**
- Never invent behavior. If it isn't in the source, leave it out.
- Never paste a credential, key, or checkout URL into a wiki page.
- Reference platforms by canonical handle.
- Keep code blocks copy-pasteable.

**Output:** one Markdown file per page, under `wiki/`.
