---
marp: true
title: Submission reproducibility
paginate: true
---

# Submission reproducibility

Before you push or zip a lab, ask: can a grader reproduce your result from a clean checkout?

---

## Clean, root, log, push
- Run status and confirm build artifacts and logs are gitignored, not accidentally staged
- Remove local secrets and scratch files graders should never see
- Run demo or test scripts from the repository root so relative paths match the README
- Capture stdout and stderr with tee into run dot log so reviewers see what you saw
- Then push and verify on the host that only the right files and commits appear

---

## Browser lab
![Submission reproducibility lab starter](assets/lab-starter.png)

---

## Real Git practice
![Real shell — clean tree, run from root, capture log](assets/real-shell.png)

---

## Real Git practice — try these

```
# git status — see tracked vs ignored files before submit
git status

# cat .gitignore — confirm build/, logs/, and .env are excluded
cat .gitignore

# bash scripts/run_demo.sh — run the demo from repo root
bash scripts/run_demo.sh

# bash scripts/run_demo.sh 2>&1 | tee run.log — capture stdout and stderr
bash scripts/run_demo.sh 2>&1 | tee run.log

# tail run.log — verify the log captured success output
tail run.log

# git log --oneline -3 — confirm recent commits look right
git log --oneline -3

# git push origin main — publish when checks pass (needs remote)
git push origin main

```

---

## Pitfalls to watch
- Running scripts from a subdirectory breaks relative paths, check pwd first
- Never commit env files with real tokens; copy from env example instead
- A dirty tree with surprise untracked files means you might zip or push the wrong snapshot
- Capture the log only after a successful root run
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load the starter and get to ready with a clean tree and run dot log
- On real Git, practice status, root run, and log capture before push
- Pull request

