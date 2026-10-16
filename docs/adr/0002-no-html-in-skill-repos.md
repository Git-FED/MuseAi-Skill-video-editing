# ADR 0002 — No HTML in skill repos

- Status: Accepted
- Date: 2026-10-16

## Context
A skill's job is to produce a *plan* or a *file artifact* (a video, a
classification, a pass/fail). It is tempting to also ship the rendered HTML a
skill is "about" — a footer, a landing page, a button.

## Decision
Skill repos contain no HTML, CSS, or JS. A skill's output is a plan, not markup.
Rendered surfaces live in a separate site repo.

## Consequences
- Skills stay portable and renderer-agnostic.
- No skill carries an XSS surface or a credential-bearing embed.
- The `.pre-commit-config.yaml` hook `no-html-in-skill-repos` enforces this.
- A skill that needs to describe markup describes it in `references/`, as data.

## Anti-pattern this prevents
A "footer" skill that ships `components/footer.html` with a live checkout URL
inside it. The skill should emit the footer *plan*; the site renders it.
