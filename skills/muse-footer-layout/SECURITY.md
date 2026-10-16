# Security Policy

## Supported versions
| Version | Supported |
| --- | --- |
| 1.x | ✅ |

## Reporting a vulnerability
Open a private security advisory, or email security@fedpromptly.com.

## Scope
This skill reads `references/links.json` and classifies a URL string. It does
not execute anything from the input and does not touch the network. Anything
that lets a crafted input escape classification or inject into the plan is in
scope.

## Credential rule
This skill exists in part to keep credentials out of footers. If you find a
tracked file containing a client ID, publishable key, buy-button ID, merchant
ID, OAuth `state`, or `redirect_uri`, treat it as a leak: report
`CREDENTIAL_LEAK: <path>` and halt.

## What this skill never does
- It never reads, writes, or commits `.env*` files.
- It never contacts the network.
- It never stores credentials.
