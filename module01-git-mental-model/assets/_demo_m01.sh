#!/usr/bin/env bash
# Track A demo for module01-git-mental-model (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

printf '%s\n' '$ git --version'
git --version
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-mm-XXXXXX")"
cd "$DEMO"
printf '%s\n' "# practice repo: $DEMO"
echo

printf '%s\n' '$ git init'
git init
echo

printf '%s\n' '$ echo "notes" > note.txt'
echo "notes" > note.txt
echo

printf '%s\n' '$ git status'
git status
echo

printf '%s\n' '$ git add note.txt'
git add note.txt
echo

printf '%s\n' '$ git status'
git status
echo

printf '%s\n' '$ git commit -m "first snapshot"'
git -c user.email=demo@local -c user.name=Demo commit -m "first snapshot"
echo

printf '%s\n' '$ git log --oneline'
git log --oneline
echo
