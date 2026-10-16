# Install

## Prerequisites
- `git`, `make`, `bash`, `jq`, and `sha256sum` (for verification)
- For specific skills:
  - `muse-video-editor` → `ffmpeg`, `ffprobe`
  - `muse-cloudflare-deploy` → `wrangler`, `node`

## Install a skill
The umbrella repository does not publish individual skill archives. Clone it,
verify its manifests, and copy the desired skill folder:

```bash
git clone https://github.com/Git-FED/fed-os-muse-skills.git
cd fed-os-muse-skills
make verify
mkdir -p ~/workspace/custom-skills
cp -r skills/muse-footer-layout ~/workspace/custom-skills/
```

Ask your Muse agent to use the skill by name.

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
