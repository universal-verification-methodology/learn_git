# test_bug.sh — exit 0 if notes.md has no BUG line, else 1 (for git bisect run)
grep -q BUG notes.md && exit 1 || exit 0
