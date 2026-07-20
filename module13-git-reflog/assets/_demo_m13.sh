#!/usr/bin/env bash
# Track A demo for module13-git-reflog (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-rf-XXXXXX")"
cd "$DEMO"
printf '%s\n' "# practice repo: $DEMO"
echo

GIT=(git -c user.email=demo@local -c user.name=Demo)

printf '%s\n' '$ git init'
git init -q
echo

printf '%s\n' '$ echo "v1" > notes.md'
echo "v1" > notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "First"'
"${GIT[@]}" commit -q -m "First"
echo

printf '%s\n' '$ git branch -M main'
git branch -M main
echo

printf '%s\n' '$ echo "important" >> notes.md'
echo "important" >> notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Important work"'
"${GIT[@]}" commit -q -m "Important work"
echo

printf '%s\n' '$ git reflog'
git reflog
echo

printf '%s\n' '$ git reset --hard HEAD~1'
git reset --hard HEAD~1
echo

printf '%s\n' '$ git log --oneline'
git log --oneline
echo

printf '%s\n' '$ git reflog'
git reflog
echo

printf '%s\n' '$ git reset --hard HEAD@{1}'
git reset --hard HEAD@{1}
echo

printf '%s\n' '$ git log --oneline'
git log --oneline
echo
