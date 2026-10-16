---
name: funding-buttons
description: Plan funding surfaces by canonical handle — never a live checkout URL
version: 1.0.0
---

## What it does
Takes a set of funding platforms and produces a plan: which surfaces to show,
in what order, with what label and gate. It references each platform by a
**canonical handle** (e.g. `patreon: fedpromptly`) and never stores or emits a
live checkout URL, client ID, publishable key, buy-button ID, or merchant ID.

## Prerequisites
- `bash` and `jq` on `PATH`
- `references/funding-links.json` present
- `references/embeds.md` present (why no embed HTML is ever stored here)

## Verify environment
Run before anything else:

    command -v jq && command -v bash

If either is missing, stop and report: `MISSING_DEP: jq`.

## Step-by-step
1. Confirm the reference data is present:

       test -f references/funding-links.json

2. For each platform handle, look up its plan entry:

       bash scripts/classify.sh "patreon:fedpromptly"

3. Assemble the plan in this order (recurring first, one-time last):
   1. GitHub Sponsors
   2. Patreon
   3. Ko-fi
   4. Buy Me a Coffee
   5. PayPal Subscription
   6. Stripe
   7. Crypto (NOWPayments)

4. For each entry emit: `label`, `handle`, `class`, `gate`, and `disclosure`
   (if any). Never emit a URL, key, or ID.

5. If a user hands you a live checkout URL, do **not** plan it. Resolve it to
   the canonical handle, plan that, and report
   `RESOLVED: <url> -> <handle>`.

## Never assume
- Never emit a client ID, publishable key, buy-button ID, or merchant ID into a
  plan. The plan references platforms by canonical handle only.
- Never place a live checkout URL in the plan. Canonical landing pages only.
- Never assume Patreon is retired just because it's absent from a given page.
  Reconcile against `references/funding-links.json` before emitting.
- Never gate a payment button behind an age check. Payment is not age-restricted
  content; if adult content exists, gate the content server-side, not the
  button.
- Never render HTML. The plan is data.
- Never store a widget id, buy-button ID, or image-button token. See
  `references/embeds.md` for why each platform's embed stays out of the repo.

## Output
A funding plan: ordered list of `{label, handle, class, gate, disclosure}`.
No URLs, no keys, no IDs, no HTML.

## Failure handling
- `classify.sh` returns `Unknown` → report `UNCLASSIFIED: <handle>`, halt.
- A live credential is detected in any tracked file → report
  `CREDENTIAL_LEAK: <path>`, halt.
- `references/funding-links.json` missing → report `MISSING_REF`, halt.
