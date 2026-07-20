#!/usr/bin/env bash
# Track A demo for module19-template-clone (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

ROOT="$(mktemp -d "${TMPDIR:-/tmp}/git-tc-XXXXXX")"
cd "$ROOT"
printf '%s\n' "# practice sandbox: $ROOT"
echo

GIT=(git -c user.email=demo@local -c user.name=Demo)

mkdir -p chip-template/{rtl,tb,scripts,docs}
cd chip-template
git init -q
cat > README.md <<'EOF'
# Chip lab template

Quick start: make help
EOF
echo "module alu; endmodule" > rtl/alu.v
echo "module tb_alu; endmodule" > tb/tb_alu.v
cat > scripts/check_ready.sh <<'EOF'
#!/usr/bin/env bash
echo "ready-check ok"
EOF
chmod +x scripts/check_ready.sh
echo "build/" > .gitignore
echo "# notes" > docs/README.md
git add .
"${GIT[@]}" commit -q -m "template init"
"${GIT[@]}" branch -M main

cd "$ROOT"
printf '%s\n' '$ git clone ../chip-template chip-lab'
git clone -q chip-template chip-lab
echo

cd chip-lab
printf '%s\n' '$ cd chip-lab'
echo
pwd
echo

printf '%s\n' '$ ls -la'
ls -la
echo

printf '%s\n' '$ ls rtl tb scripts docs'
ls rtl tb scripts docs
echo

printf '%s\n' '$ cat README.md'
cat README.md
echo

printf '%s\n' '$ git status'
git status -sb
echo

printf '%s\n' '$ git remote -v'
git remote -v
echo

printf '%s\n' '$ git branch'
git branch
echo
