# Security Policy

## Supported versions
| Version | Supported |
| --- | --- |
| 1.x | ✅ |

## Reporting a vulnerability
Open a private security advisory on the repository, or email
security@fedpromptly.com. Do not open a public issue for anything that could be
exploited before a fix ships.

Please include: the skill name and version, a minimal reproduction, and the
impact you believe it has.

## Scope
This skill executes `ffmpeg`/`ffprobe` on files you provide. It reads from
`~/workspace/input` and writes to `~/workspace/output`. Anything that lets it
read or write outside those paths, or execute arbitrary commands from a crafted
media file, is in scope.

## What this skill never does
- It never reads, writes, or commits `.env*` files.
- It never contacts the network.
- It never stores credentials of any kind.
