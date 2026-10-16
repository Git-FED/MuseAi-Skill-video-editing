# ADR 0003 — No live credentials, canonical links only

- Status: Accepted
- Date: 2026-10-16

## Context
A checkout URL was pasted into a public repo. It carried a Patreon OAuth
`client_id`, a single-use `state` token, and a `redirect_uri`. A funding page
carried a live PayPal `client_id`, a Stripe `pk_live_` key, a buy-button ID, and
a NOWPayments merchant ID. Each of these looks like a link and behaves like a
credential.

## Decision
1. No live credentials in any tracked file or URL. Client IDs, publishable
   keys, buy-button IDs, merchant IDs, OAuth `state`, and `redirect_uri` live
   server-side or in a gitignored `config.js`.
2. Reference platforms by **canonical handle** (`patreon: fedpromptly`), and
   resolve to a live URL at render time.
3. A checkout URL is never a footer link and never a plan entry. Resolve it to
   the canonical landing page.
4. `.env.example` may contain only empty values.

## Consequences
- Rotating a credential is a one-line change in one place, not N pages.
- `.pre-commit-config.yaml` rejects tracked `.env` files and OAuth params.
- `check-secrets.sh` fails CI if a workflow prints a secret.

## The test
A footer link must be **public, stable, and credential-free**. A checkout URL is
none of the three.
