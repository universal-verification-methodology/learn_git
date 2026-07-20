#!/usr/bin/env bash
# Track A demo for module10-git-conflicts (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-conf-XXXXXX")"
cd "$DEMO"
printf '%s\n' "# practice repo: $DEMO"
echo

GIT=(git -c user.email=demo@local -c user.name=Demo)

printf '%s\n' '$ git init'
git init -q
echo

printf '%s\n' '$ echo "shared" > notes.md'
echo "shared" > notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Initial"'
"${GIT[@]}" commit -q -m "Initial"
echo

printf '%s\n' '$ git branch -M main'
git branch -M main
echo

printf '%s\n' '$ git checkout -b feature/conflict-test'
git checkout -q -b feature/conflict-test
echo

printf '%s\n' '$ echo "Line from feature" > notes.md'
echo "Line from feature" > notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Change on feature"'
"${GIT[@]}" commit -q -m "Change on feature"
echo

printf '%s\n' '$ git checkout main'
git checkout -q main
echo

printf '%s\n' '$ echo "Line from main" > notes.md'
echo "Line from main" > notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Change on main"'
"${GIT[@]}" commit -q -m "Change on main"
echo

printf '%s\n' '$ git merge feature/conflict-test'
set +e
"${GIT[@]}" merge --no-edit feature/conflict-test 2>&1
merge_rc=$?
set -e
echo

printf '%s\n' '$ cat notes.md'
cat notes.md
echo

printf '%s\n' '$ echo "Resolved line" > notes.md'
echo "Resolved line" > notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "Resolve merge conflict"'
"${GIT[@]}" commit -q -m "Resolve merge conflict"
echo

printf '%s\n' '$ git log --oneline --graph --all'
git log --oneline --graph --all
echo
