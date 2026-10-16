# Security Policy

## Supported versions
| Version | Supported |
| --- | --- |
| 1.x | ✅ |

## Reporting a vulnerability
Open a private security advisory, or email security@fedpromptly.com.

## Scope
This skill reads the repository tree and looks for a `CNAME` file. It does not
write anything and does not touch the network. Anything that lets a crafted tree
evade the check is in scope.

## What this skill never does
- It never deletes files.
- It never reads, writes, or commits `.env*` files.
- It never contacts the network.
