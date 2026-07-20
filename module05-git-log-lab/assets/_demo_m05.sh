#!/usr/bin/env bash
# Track A demo for module05-git-log-lab (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-log-XXXXXX")"
cd "$DEMO"
printf '%s\n' "# practice repo: $DEMO"
echo

git init -q
git -c user.email=demo@local -c user.name=Demo checkout -b main -q 2>/dev/null || true

echo "notes v1" > notes.md
git add notes.md
git -c user.email=demo@local -c user.name=Demo commit -q -m "Add notes"

echo "notes v2" >> notes.md
git add notes.md
git -c user.email=demo@local -c user.name=Demo commit -q -m "Expand notes"

echo "readme" > README.md
git add README.md
git -c user.email=demo@local -c user.name=Demo commit -q -m "Add README"

printf '%s\n' '$ git log --oneline'
git log --oneline
echo

printf '%s\n' '$ git log --oneline -3'
git log --oneline -3
echo

printf '%s\n' '$ git log --oneline --graph --all'
git log --oneline --graph --all
echo

printf '%s\n' '$ git log --name-only -1'
git log --name-only -1
echo

printf '%s\n' '$ git log --oneline -- notes.md'
git log --oneline -- notes.md
echo
