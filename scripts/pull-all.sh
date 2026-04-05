#!/bin/bash
# Pull latest from all team repos under repos/
for repo in repos/A20-App-1*/; do
  [ -d "$repo/.git" ] || continue
  name=$(basename "$repo")
  echo -n "$name: "
  git -C "$repo" pull --ff-only --quiet 2>&1 || echo "⚠ pull failed"
  echo "✓"
done
