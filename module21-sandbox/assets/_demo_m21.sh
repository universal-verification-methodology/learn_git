#!/usr/bin/env bash
# Track A demo for module21-sandbox (local unix-git-practice stand-in).
set -euo pipefail

echo '# real shell session (Track A)'
echo

ROOT="$(mktemp -d "${TMPDIR:-/tmp}/git-sbx-XXXXXX")"
cd "$ROOT"
printf '%s\n' "# practice sandbox: $ROOT"
echo

LEARNING="/mnt/d/proj/designs/learning"
TEMPLATE="$LEARNING/platform/sandbox/unix-git-practice"
if [[ ! -d "$TEMPLATE/.git" ]]; then
  echo "error: missing template at $TEMPLATE" >&2
  exit 1
fi

GIT=(git -c user.email=demo@local -c user.name=Demo -c protocol.file.allow=always)

printf '%s\n' '$ git clone --recurse-submodules <template> my-practice'
"${GIT[@]}" clone -q --recurse-submodules "file://$TEMPLATE" my-practice
echo

cd my-practice
printf '%s\n' '$ cd my-practice'
echo
pwd
echo

printf '%s\n' '$ ls src tb scripts external/shared-ip'
ls src tb scripts external/shared-ip
echo

printf '%s\n' '$ make test'
make test
echo

printf '%s\n' '$ bash scripts/check_ready.sh'
bash scripts/check_ready.sh
echo

printf '%s\n' '$ git checkout -b lab1'
"${GIT[@]}" checkout -q -b lab1
echo

printf '%s\n' '$ git status'
git status -sb
echo
