#!/usr/bin/env bash
# Track A demo for module14-blame-bisect (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

DEMO="$(mktemp -d "${TMPDIR:-/tmp}/git-bb-XXXXXX")"
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

printf '%s\n' '$ git commit -m "init"'
"${GIT[@]}" commit -q -m "init"
echo

printf '%s\n' '$ echo "v2 ok" >> notes.md'
echo "v2 ok" >> notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "add v2"'
"${GIT[@]}" commit -q -m "add v2"
echo

printf '%s\n' '$ echo "BUG" >> notes.md'
echo "BUG" >> notes.md
echo

printf '%s\n' '$ git add notes.md'
git add notes.md
echo

printf '%s\n' '$ git commit -m "introduce bug"'
"${GIT[@]}" commit -q -m "introduce bug"
echo

cat > test_bug.sh <<'EOF'
#!/usr/bin/env bash
grep -q BUG notes.md && exit 1 || exit 0
EOF
chmod +x test_bug.sh

printf '%s\n' '$ git blame notes.md'
git blame notes.md
echo

printf '%s\n' '$ git bisect start'
"${GIT[@]}" bisect start
echo

printf '%s\n' '$ git bisect bad'
"${GIT[@]}" bisect bad
echo

printf '%s\n' '$ git bisect good HEAD~2'
"${GIT[@]}" bisect good HEAD~2
echo

printf '%s\n' '$ git bisect run ./test_bug.sh'
"${GIT[@]}" bisect run ./test_bug.sh
echo

printf '%s\n' '$ git bisect reset'
"${GIT[@]}" bisect reset
echo
