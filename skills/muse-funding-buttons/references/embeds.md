# Reference — funding embeds (why none are stored here)

This file is **data about embeds**, not an embed. It exists so that a skill asked
to "add the PayPal button, the Stripe button, the Ko-fi widget, and the Buy Me a
Coffee image button" has a correct answer that is not "paste the HTML".

## The rule
A funding surface is planned by **canonical handle**. The rendered button is
produced by the platform's own script or by the site's renderer, at render time,
from that handle. Nothing credential-bearing is ever stored in a tracked file.

```
handle  ->  renderer  ->  button
patreon:fedpromptly  ->  GitHub's own button  ->  [Sponsor]
```

## What each platform actually requires (and why it stays out of the repo)

| Platform | Looks like | Really is | Stored here? |
|---|---|---|---|
| PayPal | `client_id=BAA_...` in a `<script>` | a live OAuth client ID | **No** — server-side / `config.js` |
| PayPal plan | `P-4FD24238VX4902214NK2XP2Y` | a plan/merchant ID | **No** — server-side |
| Stripe | `pk_live_51UIdAG...` | a publishable key | **No** — render-time only |
| Stripe buy button | `buy_btn_1UJKaa...` | a buy-button ID | **No** — render-time only |
| Ko-fi | `W3T61ZU5TK` widget id | a per-account widget token | **No** — resolve from `ko-fi:fedpromptly` |
| Buy Me a Coffee | an `<img>` button with a token in the URL | a per-account image token | **No** — resolve from `bmc:fedpromptly` |
| NOWPayments | `iid=5997958570` | a merchant/invoice ID | **No** — server-side |

A publishable key is still a key. A buy-button ID is still a credential. A
widget id is still account-scoped. None of them belong in a plan, a README, a
footer, or a URL you can paste into a chat.

## The placeholder trap
A copy-pasted embed usually carries a placeholder — `YOUR_USERNAME`,
`data-kofi-id="YOUR_ID"`. Placeholders are safe *only if they never ship*. The
moment one ships, someone replaces it with a real value and commits it. So the
plan does not carry the embed at all; it carries the handle, and the renderer
owns the substitution.

## What a correct plan emits
```json
{ "label": "Ko-fi", "handle": "ko-fi:fedpromptly", "class": "Premium",
  "gate": "tips", "disclosure": null }
```
No `id`, no `src`, no `<script>`, no `<img>`.

## What a correct renderer does
1. Reads the handle from the plan.
2. Looks up the account-scoped token from a **gitignored** `config.js` (or a
   server endpoint).
3. Emits the platform's own script/button with that token, at render time.
4. Adds the referral disclosure line if `disclosure == "referral"`.

## Never
- Never store a client ID, publishable key, buy-button ID, widget id, or
  merchant ID in any tracked file.
- Never ship a placeholder that is expected to be edited in place.
- Never put a checkout URL (`/checkout/...`, `response_type=code`, `state=`) in
  a plan or a footer.
- Never gate a payment button behind an age check (see ADR 0004).
- Never render HTML from this skill. The plan is data; the site renders it.
