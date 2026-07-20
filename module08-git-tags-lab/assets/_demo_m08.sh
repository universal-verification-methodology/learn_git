#!/usr/bin/env bash
# Track A demo for module08-git-tags-lab (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-tag-XXXXXX")"
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

printf '%s\n' '$ git tag v1.0'
git tag v1.0
echo

printf '%s\n' '$ git tag'
git tag
echo

printf '%s\n' '$ git show v1.0'
git show v1.0
echo

printf '%s\n' '$ git tag -a v1.0.0 -m "Release 1.0"'
git -c user.email=demo@local -c user.name=Demo tag -a v1.0.0 -m "Release 1.0"
echo

printf '%s\n' '$ git show v1.0.0'
git show v1.0.0
echo
