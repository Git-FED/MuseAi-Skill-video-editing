# Build

## There is no build step.

This is deliberate. The site is static HTML/CSS/JS served as-is. The skills are
folders read as-is. Nothing compiles, bundles, or transpiles.

That means:
- No `package.json`, no `node_modules`, no bundler.
- No `build.yml` — there is nothing to build. (If you find one, delete it.)
- The `Makefile` is a *task runner*, not a build. `make help` lists tasks.

## What "verify" means here
The closest thing to a build is verification:

```bash
make verify   # manifest hashes match the tree
make guard    # CNAME + secrets checks
make icons    # icon assets present, favicon referenced, ICO valid
make lint     # shellcheck + markdownlint, if installed
```

## Why this matters
The moment one skill has a build and another doesn't, the installer can no
longer assume a layout — so it either breaks or grows conditionals, and now
you're maintaining a package manager. "No build step" is what keeps
`drop it in ~/workspace/custom-skills/` true for skill number 50.
