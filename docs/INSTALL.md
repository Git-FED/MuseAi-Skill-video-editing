# Install

## Prerequisites
- `bash`, `git`, `unzip`, `jq` (for verification)
- For specific skills:
  - `muse-video-editor` → `ffmpeg`, `ffprobe`
  - `muse-cloudflare-deploy` → `wrangler`, `node`

## Install a skill
1. Download the release for the skill:

   ```bash
   curl -LO https://example.org/fed-os-muse-skills/releases/download/v1.0.0/muse-footer-layout-v1.0.0.zip
   ```

2. Verify the file hashes against `manifest.json:files`:

   ```bash
   unzip -q muse-footer-layout-v1.0.0.zip -d /tmp/verify
   cd /tmp/verify/muse-footer-layout
   jq -r '.files | to_entries[] | "\(.value|sub("sha256:";"") )  \(.key)"' manifest.json | sha256sum -c -
   ```

3. Drop it in:

   ```bash
   mkdir -p ~/workspace/custom-skills
   cp -r /tmp/verify/muse-footer-layout ~/workspace/custom-skills/
   ```

4. Ask your Muse agent to use it by name.

## Run the site locally
No build needed:

```bash
python3 -m http.server 8080 --directory site
# open http://localhost:8080
```

## Uninstall
Remove the folder from `~/workspace/custom-skills/<skill-name>/`.

## Verify the whole fleet (contributors)
```bash
make verify
make guard
make icons
```
