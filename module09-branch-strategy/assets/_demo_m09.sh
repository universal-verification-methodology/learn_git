#!/usr/bin/env bash
# Track A demo for module09-branch-strategy (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-br-XXXXXX")"
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

printf '%s\n' '$ git branch -M main'
git branch -M main
echo

printf '%s\n' '$ git branch'
git branch
echo

printf '%s\n' '$ git checkout -b feature/readme-update'
git checkout -b feature/readme-update
echo

printf '%s\n' '$ echo "feature edit" >> notes.md'
echo "feature edit" >> notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Update notes on feature branch"'
git -c user.email=demo@local -c user.name=Demo commit -q -m "Update notes on feature branch"
echo

printf '%s\n' '$ git checkout main'
git checkout main
echo

printf '%s\n' '$ git log --oneline --all'
git log --oneline --all
echo
