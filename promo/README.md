# Promotion Images

Four comical, simple promo images. Each one illustrates a single shared rule of
the fleet, because a rule you can laugh at is a rule you remember.

| File | Rule | Caption |
| --- | --- | --- |
| `promo-1-one-repo-per-skill.png` | One repo per skill | *One repo per skill. Not one drawer of everything.* |
| `promo-2-no-credentials.png` | No live credentials | *No credentials in the repo. The bouncer says no.* |
| `promo-3-canonical-links.png` | Canonical links only | *Canonical links only. Untangle the checkout URL.* |
| `promo-4-no-fake-gates.png` | No fake gates | *No fake gates. A checkbox is not a lock.* |

## How they were made

The illustrations are generated art (flat neon-on-dark cartoon style). The
captions are drawn on top with Pillow by `scripts/make-promos.py`, so the text is
always crisp and correct — generated art renders text unreliably, and a promo
image with garbled text is worse than no promo image.

To regenerate:

```bash
python3 scripts/make-promos.py
```

The script reads source art from `promo/_src-*.png`. If you want to swap the art,
drop new sources there and re-run.

## Usage

These are free to share under the project's MIT license. If you post them, a link
back to the repository is appreciated. If you edit them, please do not add claims
the project cannot back up — no "verified," no "secure," no "gated." The rules are
the point, and the rules are small on purpose.

## Accessibility

Each image carries its caption in visible text, not just in the art, so the meaning
survives when the image is described rather than seen. When you post one, reuse the
caption text as the alt text.
