#!/usr/bin/env bash
# Create ~/unix_practice/git_demo for Track A Git exercises.
set -euo pipefail
BASE="${HOME}/unix_practice"
TARGET="${BASE}/git_demo"
mkdir -p "$BASE"
if [[ -d "$TARGET/.git" ]]; then
  echo "Already a Git repo: $TARGET"
else
  mkdir -p "$TARGET"
  (
    cd "$TARGET"
    git init -b main
    cat > README.md << 'EOF'
learn_git Track A practice repo
Use this directory for checklist exercises (not for curriculum PRs).
EOF
    cat > notes.md << 'EOF'
# Practice notes
EOF
    mkdir -p src tb build
    echo "placeholder" > build/output.tmp
    cat > .gitignore << 'EOF'
build/
*.log
*.tmp
EOF
    git add README.md notes.md .gitignore src tb
    git -c user.email="student@example.com" -c user.name="learn_git student" \
      commit -m "chore: initial practice repo"
  )
  echo "Created Git practice repo: $TARGET"
fi
ls -la "$TARGET"
git -C "$TARGET" status -sb || true
