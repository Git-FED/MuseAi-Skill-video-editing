---
name: cname-guard
description: Refuse to ship a stray CNAME file that silently hijacks a domain
version: 1.0.0
---

## What it does
Scans a repository for a `CNAME` file before it ships. A stray `CNAME` silently
points GitHub Pages at a domain you may not control. This skill finds it and
stops the release.

## Prerequisites
- `bash` and `find` on `PATH`

## Verify environment
Run before anything else:

    command -v find && command -v bash

If either is missing, stop and report: `MISSING_DEP: find`.

## Step-by-step
1. Run the check from the repository root:

       bash scripts/check-cname.sh

2. If the script exits non-zero, report `FORBIDDEN: CNAME file present` and stop
   the release. Do not delete the file silently — surface the path to the user.

3. If the script exits zero, report `OK: no CNAME file`.

## Never assume
- Never assume deleting a `CNAME` file clears a hosting provider's saved custom
  domain. The file and the account setting are separate. Report the file; do not
  claim the domain is unset.
- Never assume a repo with no `CNAME` file is safe — check the hosting
  provider's saved domain setting separately.
- Never auto-delete a `CNAME` file. Report it and let the owner decide.

## Output
One line: `OK: no CNAME file` or `FORBIDDEN: CNAME file present at <path>`.

## Failure handling
- `find` missing → report `MISSING_DEP: find`, halt.
- A `CNAME` file found → exit non-zero, print its path, halt the release.
