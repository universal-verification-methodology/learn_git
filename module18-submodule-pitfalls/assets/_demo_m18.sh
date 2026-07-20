#!/usr/bin/env bash
# Track A demo for module18-submodule-pitfalls (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

ROOT="$(mktemp -d "${TMPDIR:-/tmp}/git-sm-XXXXXX")"
cd "$ROOT"
printf '%s\n' "# practice sandbox: $ROOT"
echo

GIT=(git -c user.email=demo@local -c user.name=Demo -c protocol.file.allow=always)

mkdir shared-lib parent
cd shared-lib
git init -q
echo "v1" > VERSION
git add VERSION
"${GIT[@]}" commit -q -m "lib v1"
V1=$("${GIT[@]}" rev-parse HEAD)
echo "v2" >> VERSION
git add VERSION
"${GIT[@]}" commit -q -m "lib v2"
"${GIT[@]}" branch -M main
echo "v3" >> VERSION
git add VERSION
"${GIT[@]}" commit -q -m "lib v3"
V3=$("${GIT[@]}" rev-parse HEAD)

cd "$ROOT/parent"
git init -q
echo "chip top" > README.md
git add README.md
"${GIT[@]}" commit -q -m "init"
"${GIT[@]}" branch -M main
"${GIT[@]}" submodule add -q "file://$ROOT/shared-lib" vendor/dv-lib
cd vendor/dv-lib
git checkout -q "$V1"
cd ../..
git add vendor/dv-lib
"${GIT[@]}" commit -q -m "Pin dv-lib at v1"

cd "$ROOT"
printf '%s\n' '$ git clone <parent> fresh-clone'
git clone -q "file://$ROOT/parent" fresh-clone
echo

cd fresh-clone
printf '%s\n' '$ ls vendor/dv-lib'
ls vendor/dv-lib
echo

printf '%s\n' '$ git submodule status'
git submodule status
echo

printf '%s\n' '$ git submodule update --init --recursive'
"${GIT[@]}" submodule update --init --recursive -q
echo

printf '%s\n' '$ cat vendor/dv-lib/VERSION'
cat vendor/dv-lib/VERSION
echo

cd vendor/dv-lib
printf '%s\n' '$ git status'
git status -sb
echo

printf '%s\n' '$ git fetch'
"${GIT[@]}" fetch -q
echo

printf '%s\n' "$ git checkout $V3"
git checkout -q "$V3"
echo

cd "$ROOT/fresh-clone"
printf '%s\n' '$ git add vendor/dv-lib'
git add vendor/dv-lib
echo

printf '%s\n' '$ git commit -m "Bump dv-lib pin"'
"${GIT[@]}" commit -q -m "Bump dv-lib pin"
echo

printf '%s\n' '$ git submodule status'
git submodule status
echo
