# Security Policy

## Supported versions
| Version | Supported |
| --- | --- |
| 1.x | ✅ |

## Reporting a vulnerability
Open a private security advisory, or email security@fedpromptly.com.

## Scope
This skill reads `references/funding-links.json` and classifies a handle. It
does not execute anything from the input and does not touch the network.
Anything that lets a live credential reach the plan is in scope.

## Credential rule
This skill exists specifically to keep payment credentials out of plans. If you
find a tracked file containing a client ID, publishable key, buy-button ID,
merchant ID, OAuth `state`, or `redirect_uri`, treat it as a leak: report
`CREDENTIAL_LEAK: <path>` and halt. Rotate the credential in the provider
dashboard.

## What this skill never does
- It never stores or emits credentials.
- It never contacts the network.
- It never renders HTML.
