#!/usr/bin/env bash
# Track A demo for module20-submission-repro (session frame for slides).
set -euo pipefail

echo '# real shell session (Track A)'
echo

ROOT="$(mktemp -d "${TMPDIR:-/tmp}/git-sr-XXXXXX")"
cd "$ROOT"
printf '%s\n' "# practice sandbox: $ROOT"
echo

GIT=(git -c user.email=demo@local -c user.name=Demo)

mkdir -p chip-lab/{rtl,scripts,build,logs}
cd chip-lab
git init -q
cat > .gitignore <<'EOF'
build/
logs/
*.log
.env
EOF
echo "module alu; endmodule" > rtl/alu.v
cat > scripts/run_demo.sh <<'EOF'
#!/usr/bin/env bash
echo "demo ok"
EOF
chmod +x scripts/run_demo.sh
echo "SECRET=local-only" > .env
echo "junk" > build/out.vvp
git add .gitignore rtl scripts/run_demo.sh
"${GIT[@]}" commit -q -m "init lab sources"
"${GIT[@]}" branch -M main

git init --bare -q "$ROOT/origin.git"
git remote add origin "$ROOT/origin.git"
"${GIT[@]}" push -q -u origin main
git --git-dir="$ROOT/origin.git" symbolic-ref HEAD refs/heads/main

printf '%s\n' '$ git status'
git status -sb
echo

printf '%s\n' '$ cat .gitignore'
cat .gitignore
echo

printf '%s\n' '$ bash scripts/run_demo.sh'
bash scripts/run_demo.sh
echo

printf '%s\n' '$ bash scripts/run_demo.sh 2>&1 | tee run.log'
bash scripts/run_demo.sh 2>&1 | tee run.log
echo

printf '%s\n' '$ tail run.log'
tail run.log
echo

printf '%s\n' '$ git log --oneline -3'
git log --oneline -3
echo

printf '%s\n' '$ git push origin main'
"${GIT[@]}" push -q origin main
echo
