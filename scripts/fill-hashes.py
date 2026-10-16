#!/usr/bin/env python3
"""Fill manifest.json:files hashes with real SHA-256 values.

This script lets a maintainer commit a self-consistent, verifiable manifest
instead of a placeholder, so `scripts/verify-hashes.sh` passes on a fresh
checkout. Hashes provide consistency checks; they do not authenticate a publisher.

Usage:
    python3 scripts/fill-hashes.py
"""
from __future__ import annotations

import hashlib
import json
import os
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


def main():
    for manifest_path in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "manifest.json"))):
        skill_dir = os.path.dirname(manifest_path)
        with open(manifest_path, encoding="utf-8") as f:
            data = json.load(f)

        files = data.get("files", {})
        updated = 0
        for rel in list(files.keys()):
            target = os.path.join(skill_dir, rel)
            if not os.path.isfile(target):
                raise SystemExit(f"MISSING {rel} in {os.path.basename(skill_dir)}")
            files[rel] = sha256(target)
            updated += 1

        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        print(f"filled {updated} hashes in {os.path.relpath(manifest_path, ROOT)}")


if __name__ == "__main__":
    main()
