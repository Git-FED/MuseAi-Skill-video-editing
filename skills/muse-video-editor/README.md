# muse-video-editor

Cut, caption, and assemble vertical video with ffmpeg.

## Who it's for
Anyone producing short-form vertical video who wants their Muse agent to do the
crop, scale, and encode without hand-holding.

## Install
The skills are folders in the umbrella repository; individual release archives
are not published yet. Clone the repository, verify the manifests, then copy the
skill folder:

```bash
git clone https://github.com/Git-FED/fed-os-muse-skills.git
cd fed-os-muse-skills
make verify
mkdir -p ~/workspace/custom-skills
cp -r skills/muse-video-editor ~/workspace/custom-skills/
```

## Quick example
Put a source file at `~/workspace/input/source.mp4`, then ask your Muse agent:

> Use the video-editor skill to make a 9:16 cut of source.mp4.

The agent verifies ffmpeg, probes the input, runs `scripts/cut.sh`, and writes
`~/workspace/output/final.mp4` (H.264, 1080x1920, AAC).

## What it will not do
- It will not overwrite an existing output without asking.
- It will not guess dimensions — it probes first.
- It will not run if `ffmpeg`/`ffprobe` are missing.

## Uninstall
Remove `~/workspace/custom-skills/muse-video-editor/`.

## License
MIT — see [LICENSE](LICENSE).
