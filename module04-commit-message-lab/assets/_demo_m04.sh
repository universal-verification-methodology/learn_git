#!/usr/bin/env bash
# Track A demo for module04-commit-message-lab (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-cm-XXXXXX")"
cd "$DEMO"
printf '%s\n' "# practice repo: $DEMO"
echo

printf '%s\n' '$ git init'
git init
echo

printf '%s\n' '$ echo "lab notes" > notes.md'
echo "lab notes" > notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Add lab notes"'
git -c user.email=demo@local -c user.name=Demo commit -m "Add lab notes"
echo

printf '%s\n' '$ echo "reset polarity fixed in TB" >> notes.md'
echo "reset polarity fixed in TB" >> notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Note TB reset polarity fix"'
git -c user.email=demo@local -c user.name=Demo commit -m "Note TB reset polarity fix"
echo

printf '%s\n' '$ git log --oneline'
git log --oneline
echo
