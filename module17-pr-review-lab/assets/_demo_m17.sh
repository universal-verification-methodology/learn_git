#!/usr/bin/env bash
# Track A demo for module17-pr-review-lab (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-pr-XXXXXX")"
cd "$DEMO"
printf '%s\n' "# practice repo: $DEMO"
echo

GIT=(git -c user.email=demo@local -c user.name=Demo)

printf '%s\n' '$ git init'
git init -q
echo

printf '%s\n' '$ echo "v1" > README.md'
echo "v1" > README.md
echo

printf '%s\n' '$ git add README.md'
git add README.md
echo

printf '%s\n' '$ git commit -m "init"'
"${GIT[@]}" commit -q -m "init"
echo

printf '%s\n' '$ git branch -M main'
"${GIT[@]}" branch -M main
echo

printf '%s\n' '$ git checkout -b feature/readme-update'
"${GIT[@]}" checkout -q -b feature/readme-update
echo

printf '%s\n' '$ echo "feature note" >> README.md'
echo "feature note" >> README.md
echo

printf '%s\n' '$ git add README.md'
git add README.md
echo

printf '%s\n' '$ git commit -m "feature: update README"'
"${GIT[@]}" commit -q -m "feature: update README"
echo

printf '%s\n' '$ git log main..HEAD --oneline'
git log main..HEAD --oneline
echo

printf '%s\n' '$ git diff main...HEAD'
git diff main...HEAD
echo

printf '%s\n' '$ echo "address review" >> README.md'
echo "address review" >> README.md
echo

printf '%s\n' '$ git add README.md'
git add README.md
echo

printf '%s\n' '$ git commit -m "address review: clarify README"'
"${GIT[@]}" commit -q -m "address review: clarify README"
echo

printf '%s\n' '$ git diff main...HEAD'
git diff main...HEAD
echo

printf '%s\n' '$ git checkout main'
"${GIT[@]}" checkout -q main
echo

printf '%s\n' '$ git merge feature/readme-update'
"${GIT[@]}" merge -q feature/readme-update
echo

printf '%s\n' '$ git log --oneline -3'
git log --oneline -3
echo
