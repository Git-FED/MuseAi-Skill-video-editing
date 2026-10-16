# ADR 0004 — No fake gates

- Status: Accepted
- Date: 2026-10-16

## Context
A page asked visitors to confirm they were 18+ with a client-side checkbox
before revealing content. The checkbox set a cookie and unhid a `div`. It looked
like a gate. It was decoration: the content was already in the HTML, the
"verification" ran in the browser the visitor controls, and clearing storage or
reading source defeated it in one step.

A fake gate is worse than no gate, because it is a claim. It tells a visitor,
a platform, and a regulator that a check happened when none did. For
age-restricted content that is a compliance statement you cannot back up.

## Decision
1. A gate must be **enforced server-side** (or by a third party that actually
   verifies identity/age). A client-side checkbox is not a gate.
2. If content is genuinely age-restricted, gate the **content** at the edge, not
   the **button**. Never hide a payment button behind an age check — payment is
   not age-restricted content.
3. If no real enforcement exists, do not render a gate. Ship a plain notice
   ("This page is intended for adults") with no false claim of verification.
4. A gate never blocks a funding, support, or contact surface. Those are not
   restricted content.
5. No gate may be the only thing standing between a visitor and a credential,
   a checkout URL, or a download that should itself be access-controlled.

## Consequences
- The site ships no client-side age gate. The word "verified" appears nowhere it
  is not literally true.
- Age-restricted content, if it ever exists, is gated by the host (Cloudflare,
  a membership wall), not by a checkbox we wrote.
- `muse-funding-buttons` refuses to plan a payment button behind an age check.
- Reviewers can grep for `18+`, `age`, and `verify` and expect a server-side
  control or a plain notice — never a cookie-setting script.

## The test
A gate must **actually stop** the thing it claims to stop, for a visitor who
controls their own browser. A checkbox that unhides a `div` stops nothing. If
you can defeat it with `view-source`, it is not a gate — it is a claim you
cannot defend.
