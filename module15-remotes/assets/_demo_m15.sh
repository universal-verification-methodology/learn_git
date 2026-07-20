#!/usr/bin/env bash
# Track A demo for module15-remotes (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

ROOT="$(mktemp -d "${TMPDIR:-/tmp}/git-remotes-XXXXXX")"
cd "$ROOT"
printf '%s\n' "# practice sandbox: $ROOT"
echo

GIT=(git -c user.email=demo@local -c user.name=Demo -c protocol.file.allow=always)

mkdir practice shared-lib
cd practice

printf '%s\n' '$ git init'
git init -q
echo

printf '%s\n' '$ echo "practice v1" > README.md'
echo "practice v1" > README.md
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

printf '%s\n' '$ git init --bare ../origin.git'
git init --bare -q "$ROOT/origin.git"
echo

printf '%s\n' '$ git remote add origin ../origin.git'
git remote add origin "$ROOT/origin.git"
echo

printf '%s\n' '$ git push -u origin main'
"${GIT[@]}" push -q -u origin main
echo

printf '%s\n' '$ git checkout -b lab1'
"${GIT[@]}" checkout -q -b lab1
echo

printf '%s\n' '$ echo "lab1 change" >> README.md'
echo "lab1 change" >> README.md
echo

printf '%s\n' '$ git add README.md'
git add README.md
echo

printf '%s\n' '$ git commit -m "lab1: update README"'
"${GIT[@]}" commit -q -m "lab1: update README"
echo

printf '%s\n' '$ git push -u origin lab1'
"${GIT[@]}" push -q -u origin lab1
echo

printf '%s\n' '$ git remote -v'
git remote -v
echo

cd "$ROOT/shared-lib"
git init -q
echo "shared v1" > VERSION
git add VERSION
"${GIT[@]}" commit -q -m "lib init"

cd "$ROOT/practice"
printf '%s\n' '$ git submodule add ../shared-lib external/shared-ip'
"${GIT[@]}" submodule add -q "file://$ROOT/shared-lib" external/shared-ip
echo

printf '%s\n' '$ git submodule status'
git submodule status
echo
