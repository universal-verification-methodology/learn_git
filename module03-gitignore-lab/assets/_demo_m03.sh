#!/usr/bin/env bash
# Track A demo for module03-gitignore-lab (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-gi-XXXXXX")"
cd "$DEMO"
printf '%s\n' "# practice repo: $DEMO"
echo

printf '%s\n' '$ git init'
git init
echo

printf '%s\n' '$ mkdir -p build'
mkdir -p build
echo

printf '%s\n' '$ touch build/output.tmp'
touch build/output.tmp
echo

printf '%s\n' '$ git status'
git status
echo

printf '%s\n' "$ printf 'build/\\n*.log\\n*.vcd\\n' > .gitignore"
printf 'build/\n*.log\n*.vcd\n' > .gitignore
echo

printf '%s\n' '$ cat .gitignore'
cat .gitignore
echo

printf '%s\n' '$ git status'
git status
echo

printf '%s\n' '$ ls build/output.tmp'
ls build/output.tmp
echo
