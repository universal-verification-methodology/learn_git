#!/usr/bin/env bash
# Track A demo for module02-git-graph (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-graph-XXXXXX")"
cd "$DEMO"
printf '%s\n' "# practice repo: $DEMO"
echo

GIT=(git -c user.email=demo@local -c user.name=Demo)

printf '%s\n' '$ git init'
git init -q
echo

printf '%s\n' '$ echo "first line" > notes.md'
echo "first line" > notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Add notes"'
"${GIT[@]}" commit -q -m "Add notes"
echo

printf '%s\n' '$ echo "second line" >> notes.md'
echo "second line" >> notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Update notes"'
"${GIT[@]}" commit -q -m "Update notes"
echo

printf '%s\n' '$ git log --oneline'
git log --oneline
echo

printf '%s\n' '$ git log --oneline --graph'
git log --oneline --graph
echo
