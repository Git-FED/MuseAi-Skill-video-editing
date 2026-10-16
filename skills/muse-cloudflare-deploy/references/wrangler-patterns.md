# Wrangler Patterns — the failure modes this skill catches

## Pages vs. Workers target confusion
`wrangler deploy` and `wrangler pages deploy` are different commands with
different config. A repo that means to publish a static site but runs
`wrangler deploy` will try to ship a Worker. Confirm the target in
`wrangler.toml` (`pages_build_output_dir` for Pages) before deploying.

## Auto-discovery picks the wrong directory
Wrangler infers the asset directory. If your build outputs to `dist/` but
wrangler looks at the repo root, it will upload the whole tree — including
`node_modules/`. Always pass an explicit output dir and inspect the dry-run.

## Dependency binaries shipped as static assets
`workerd`, `*.node`, and `*.wasm` files belong to the runtime, not to your
static bundle. If they appear in the dry-run output, the build is mis-scoped.
This skill fails the preflight on that condition.

## KV placeholder IDs and missing secrets
Placeholder KV namespace IDs (`"id": "your-kv-id"`) deploy fine but fail at
runtime. Missing secrets fail silently until the first request. Run
`wrangler secret list` and confirm the KV IDs resolve before deploying.

## Non-deterministic CI
A deploy that depends on a locally-installed wrangler version will drift. Pin
the version in CI (`npx wrangler@3.x`), not `latest`.

## The credential rule
`.wrangler/` holds local state and can hold tokens. `.dev.vars` holds local
secrets. Neither is ever committed. Workflows never print `${{ secrets.* }}`.
