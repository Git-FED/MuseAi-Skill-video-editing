# Prompt — landing page

Use this to generate (or regenerate) the landing page. It is a *spec*, not a
mood board — it carries the accessibility constraints the first draft missed.

---

Build a single static landing page for "FED-OS Muse Skills" — a fleet of
one-repo-per-skill packages for AI Muse agents.

**Aesthetic:** dark "obsidian" base (#07070a) with neon cyan (#00f0ff) and
violet (#7000ff) accents. Glassmorphism cards. A subtle ambient mesh gradient
and a faint grid, both as fixed background layers.

**Structure:** sticky header (logo + nav) → hero (eyebrow, H1, lede, two CTAs)
→ skills grid (6 cards) → rules grid (6 cards) → install block → funding grid
→ footer (4 columns + disclosure + referral line).

**Hard constraints — do not skip these:**
- Respect `prefers-reduced-motion: reduce` — disable parallax, tilt, reveal
  transforms, and any particle motion; keep opacity transitions only.
- All text meets WCAG AA contrast (4.5:1 body, 3:1 large text). Violet accent
  must be lifted (use #a06bff on dark, not #7000ff) if used for text.
- `backdrop-filter` has a solid-color fallback via `@supports not`.
- Every interactive element has a visible `:focus-visible` state.
- Background/decorative layers keep `pointer-events: none` and `aria-hidden`.
- A skip-to-content link is the first focusable element.
- No credentials anywhere. Funding buttons resolve from canonical handles.
- Any referral link carries a plain-language disclosure line above/near it.

**Output:** `index.html`, `assets/css/main.css`, `assets/js/app.js`, plus
`favicon.svg`, `favicon.ico`, `logo.svg`, `social-preview.png`. No build step,
no framework, no external CDN except the fonts already in the system stack.

**Do not** inline live payment embeds, client IDs, or checkout URLs.
