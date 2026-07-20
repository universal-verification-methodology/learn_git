#!/usr/bin/env bash
# Track A demo for module06-git-undo-safe (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-undo-XXXXXX")"
cd "$DEMO"
printf '%s\n' "# practice repo: $DEMO"
echo

printf '%s\n' '$ git init'
git init -q
echo

printf '%s\n' '$ echo "v1" > notes.md'
echo "v1" > notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Add notes"'
git -c user.email=demo@local -c user.name=Demo commit -q -m "Add notes"
echo

printf '%s\n' '$ echo "draft line" >> notes.md'
echo "draft line" >> notes.md
echo

printf '%s\n' '$ git status'
git status
echo

printf '%s\n' '$ git restore notes.md'
git restore notes.md
echo

printf '%s\n' '$ echo "draft line" >> notes.md'
echo "draft line" >> notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git restore --staged notes.md'
git restore --staged notes.md
echo

printf '%s\n' '$ git status'
git status
echo
