#!/usr/bin/env bash
# Track A demo for module16-remote-tracking (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

ROOT="$(mktemp -d "${TMPDIR:-/tmp}/git-rt-XXXXXX")"
cd "$ROOT"
printf '%s\n' "# practice sandbox: $ROOT"
echo

GIT=(git -c user.email=demo@local -c user.name=Demo)

mkdir practice
cd practice

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

printf '%s\n' '$ git init --bare ../origin.git'
git init --bare -q "$ROOT/origin.git"
echo

printf '%s\n' '$ git remote add origin ../origin.git'
git remote add origin "$ROOT/origin.git"
echo

printf '%s\n' '$ git push -u origin main'
"${GIT[@]}" push -q -u origin main
git --git-dir="$ROOT/origin.git" symbolic-ref HEAD refs/heads/main
echo

printf '%s\n' '$ git clone ../origin.git ../teammate'
git clone -q -b main "$ROOT/origin.git" "$ROOT/teammate"
echo

cd "$ROOT/teammate"
printf '%s\n' '$ echo "v2 remote" >> README.md'
echo "v2 remote" >> README.md
echo

printf '%s\n' '$ git add README.md'
git add README.md
echo

printf '%s\n' '$ git commit -m "remote advance"'
"${GIT[@]}" commit -q -m "remote advance"
echo

printf '%s\n' '$ git push origin main'
"${GIT[@]}" push -q origin main
echo

cd "$ROOT/practice"
printf '%s\n' '$ git fetch origin'
"${GIT[@]}" fetch -q origin
echo

printf '%s\n' '$ git branch -r'
git branch -r
echo

printf '%s\n' '$ echo "local work" >> README.md'
echo "local work" >> README.md
echo

printf '%s\n' '$ git add README.md'
git add README.md
echo

printf '%s\n' '$ git commit -m "local commit"'
"${GIT[@]}" commit -q -m "local commit"
echo

printf '%s\n' '$ git branch -vv'
git branch -vv
echo

printf '%s\n' '$ git checkout -b feature-tmp'
"${GIT[@]}" checkout -q -b feature-tmp
echo

printf '%s\n' '$ git push -u origin feature-tmp'
"${GIT[@]}" push -q -u origin feature-tmp
echo

printf '%s\n' '$ git push origin --delete feature-tmp'
"${GIT[@]}" push -q origin --delete feature-tmp
echo

printf '%s\n' '$ git fetch origin'
"${GIT[@]}" fetch -q origin
echo

printf '%s\n' '$ git remote prune origin'
"${GIT[@]}" remote prune origin
echo

printf '%s\n' '$ git branch -r'
git branch -r
echo
