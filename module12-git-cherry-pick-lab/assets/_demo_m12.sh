#!/usr/bin/env bash
# Track A demo for module12-git-cherry-pick-lab (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-cp-XXXXXX")"
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

printf '%s\n' '$ git checkout -b feature/fix'
git checkout -q -b feature/fix
echo

printf '%s\n' '$ echo "hotfix" > fix.txt'
echo "hotfix" > fix.txt
echo

printf '%s\n' '$ git add fix.txt'
git add fix.txt
echo

printf '%s\n' '$ git commit -m "Add hotfix on feature"'
"${GIT[@]}" commit -q -m "Add hotfix on feature"
PICK_HASH=$("${GIT[@]}" rev-parse HEAD)
echo

printf '%s\n' '$ git log --oneline feature/fix'
git log --oneline feature/fix
echo

printf '%s\n' '$ git checkout main'
git checkout -q main
echo

printf '%s\n' "$ git cherry-pick ${PICK_HASH:0:7}"
"${GIT[@]}" cherry-pick "$PICK_HASH"
echo

printf '%s\n' '$ git log --oneline --all'
git log --oneline --all
echo
