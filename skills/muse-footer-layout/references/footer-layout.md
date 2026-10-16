# Footer Layout — Source of Truth (human-readable)

This file is the human-readable mirror of `links.json`. Keep them in sync; the
release hash check will expose drift.

## Visibility classes

| Class | Meaning | Footer? |
| --- | --- | --- |
| Public | Anyone can open it, no login to see it | Yes |
| Premium | The landing page is public, the content behind it is paid | Yes, as a teaser link |
| Private | Invite / personal / gated | No — gated list only |
| Internal | Not for the public at all | No — excluded |

## Recommended public footer (order matters)

1. Explore Ecosystem — https://www.fedpromptly.org
2. Storefront — https://www.jabburr.com/fed-os
3. Articles — https://substack.com/@fedpromptly
4. Blog Post — https://fedpromptly.wordpress.com/
5. GitFed Blog — https://gitfed.substack.com/
6. Developers — https://discord.gg/Jm4XStx4Pf *(public invite; private channels gated)*
7. Social Media — https://bsky.app/profile/fed-os.bsky.social
8. Friends — https://facebook.com/fedpromptly
9. Advertisement / X — https://x.com/Fedpromptly
10. Artwork — https://www.deviantart.com/fedpromptly
11. Tips / Donations — https://buymeacoffee.com/fedpromptly
12. Contact — contact@fedpromptly.com
13. Support — support@fedpromptly.com
14. Business — business@fedpromptly.com
15. Careers — careers@fedpromptly.com *(only if hiring)*

## Footer teasers (Premium — landing page public, content gated)

- Join FED-OS Membership — https://www.fedpromptly.com/aid *(gate: membership)*
- Whop — https://whop.com/fedpromptly/ *(gate: paid-products)*
- Patreon — https://www.patreon.com/c/FEDpromptly *(gate: tiers)*

## Gated (never in the public footer)

- Personal Substack — https://substack.com/@gitfed *(reason: personal)*
- Private Matrix — https://matrix.to/#/#fed-os:matrix.org
  - Gate: 18+ confirmation checkbox
  - Gate: country eligibility check
  - Countries: Canada, Switzerland, Russia, Iran, Somalia, Turkmenistan
  - Reveal only after both gates pass.

## Hard rules

- A footer link must be **public, stable, and credential-free**. A checkout URL
  is none of the three.
- Never place a URL containing `state=`, `client_id=`, `response_type=code`,
  `/checkout/`, or `/oauth2/` in a footer. Resolve it to the canonical landing
  page instead.
- A referral link is Public *for visibility* but carries a disclosure
  obligation. It is not an ordinary footer link.
- Deleting a `CNAME` file does **not** clear a hosting provider's saved custom
  domain. The file and the account setting are separate.
