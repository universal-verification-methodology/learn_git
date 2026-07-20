#!/usr/bin/env bash
# Track A demo for module11-git-rebase-merge (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-rb-XXXXXX")"
cd "$DEMO"
printf '%s\n' "# practice repo: $DEMO"
echo

GIT=(git -c user.email=demo@local -c user.name=Demo)

printf '%s\n' '$ git init'
git init -q
echo

printf '%s\n' '$ echo "base" > notes.md'
echo "base" > notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Base"'
"${GIT[@]}" commit -q -m "Base"
echo

printf '%s\n' '$ git branch -M main'
git branch -M main
echo

printf '%s\n' '$ git checkout -b feature/update'
git checkout -q -b feature/update
echo

printf '%s\n' '$ echo "feature" >> notes.md'
echo "feature only" > feature.txt
echo

printf '%s\n' '$ git add feature.txt'
git add feature.txt
echo

printf '%s\n' '$ git commit -m "Feature work"'
"${GIT[@]}" commit -q -m "Feature work"
echo

printf '%s\n' '$ git checkout main'
git checkout -q main
echo

printf '%s\n' '$ echo "main update" >> notes.md'
echo "main update" >> notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Main moved forward"'
"${GIT[@]}" commit -q -m "Main moved forward"
echo

printf '%s\n' '$ git checkout feature/update'
git checkout -q feature/update
echo

printf '%s\n' '$ git rebase main'
"${GIT[@]}" rebase main
echo

printf '%s\n' '$ git log --oneline --graph --all'
git log --oneline --graph --all
echo
