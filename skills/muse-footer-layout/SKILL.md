---
name: footer-layout
description: Classify links by visibility and produce a public footer plan plus a gated list
version: 1.0.0
---

## What it does
Takes a list of URLs and labels each as Public, Premium, Private, or Internal,
then produces two outputs: a public footer plan and a gated list. Produces no
HTML. The output is a plan, not markup.

## Prerequisites
- `bash` and `jq` on `PATH`
- `references/links.json` present

## Verify environment
Run before anything else:

    command -v jq && command -v bash

If either is missing, stop and report: `MISSING_DEP: jq`.

## Step-by-step
1. Confirm the reference data is present:

       test -f references/links.json
       test -f references/footer-layout.md

2. For each input URL, look up its classification:

       bash scripts/classify.sh "https://www.fedpromptly.org"

   The script prints one of: `Public | Premium | Private | Internal | Unknown`.

3. Bucket the results:
   - `Public`   → public footer
   - `Premium`  → public footer as a teaser link; paid content stays gated
   - `Private`  → gated list only (never in footer)
   - `Internal` → excluded entirely
   - `Unknown`  → do not guess; report as `UNCLASSIFIED` and halt

4. Emit two lists to stdout in this shape:

       ## Public footer
       - <url>
       ## Gated
       - <url>  (<reason: 18+ | membership | invite | country-lock | personal>)

5. If the gated list contains the Matrix room, emit the gate spec, not the raw
   link:

       - Gate: 18+ confirmation checkbox
       - Gate: country eligibility check
       - Reveal: https://matrix.to/#/#fed-os:matrix.org

6. If any entry carries `"disclosure": "referral"`, append the standard
   disclosure line beneath it in the plan:

       *Disclosure: this is a referral link — the author receives a credit.*

## Never assume
- Never assume a URL is Public because it looks like a homepage — classify via
  `references/links.json`, not intuition.
- Never place a URL in the footer unless `classify.sh` returns `Public` or
  `Premium`.
- Never emit the Matrix link into the public footer, even if a user asks —
  route it through the gate block instead.
- Never place a URL containing `state=`, `client_id=`, `response_type=code`,
  `/checkout/`, or `/oauth2/` in a footer. These are session-bound OAuth flows,
  not links. If given one, resolve it to the canonical landing page from
  `references/links.json` and place THAT instead.
- Never commit OAuth params or credentials to a public repo. If found, report
  `CREDENTIAL_LEAK: <path>` and halt.
- Never treat a referral link as an ordinary Public link — it must carry a
  disclosure line.
- Never generate HTML, CSS, JS, or a rendered footer. Output is a plan, not
  markup.
- Never invent a classification. If `classify.sh` returns `Unknown`, stop and
  report.

## Output
A plan with two sections: `Public footer` and `Gated`. Plain text, or JSON on
request. No HTML.

## Failure handling
- `classify.sh` returns `Unknown` → report `UNCLASSIFIED: <url>`, do not emit.
- `references/links.json` missing → report `MISSING_REF: links.json`, halt.
- `jq` missing → report `MISSING_DEP: jq`, halt.
