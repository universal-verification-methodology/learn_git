---
marp: true
title: PR review checklist
paginate: true
---

# PR review checklist

A pull request is more than a merge button, it is a review conversation

---

## Size, tests, hygiene, description
- Keep each PR to one concern so reviewers can hold the change in their head
- RTL or testbench edits should mention how you verified
- Hygiene means no wave dumps
- The description should explain what changed and how a reviewer can reproduce your result
- Approve when all four pass, comment for nits or missing context

---

## Browser lab
![PR review lab starter](assets/lab-starter.png)

---

## Real Git practice
![Real shell — review a feature branch diff](assets/real-shell.png)

---

## Real Git practice — try these

```
# git init — create a new repository here
git init

# echo … > README.md — first commit on main
echo "v1" > README.md
git add README.md
git commit -m "init"

# git branch -M main — name the default branch main
git branch -M main

# git checkout -b feature/readme-update — branch for the PR
git checkout -b feature/readme-update

# echo … >> README.md — one focused change
echo "feature note" >> README.md

# git add README.md — stage only the intended file
git add README.md

# git commit -m "feature: update README" — small, descriptive commit
git commit -m "feature: update README"

# git log main..HEAD --oneline — commits the PR would add
git log main..HEAD --oneline

# git diff main...HEAD — full diff a reviewer reads
git diff main...HEAD

# echo … >> README.md — address review feedback
echo "address review" >> README.md

# git add README.md — stage the fix
git add README.md

# git commit -m "address review: clarify README" — second commit on same branch
git commit -m "address review: clarify README"

# git diff main...HEAD — updated PR diff after push
git diff main...HEAD

# git checkout main — switch to integration branch
git checkout main

# git merge feature/readme-update — merge after approval
git merge feature/readme-update

# git log --oneline -3 — see merged history
git log --oneline -3

```

---

## Pitfalls to watch
- Do not approve mega-diffs that mix refactor with feature work, ask for a split
- Never merge secrets or generated waves even if the RTL change is correct
- A thin description on a risky fix deserves request changes, not a silent approve
- Draft or work-in-progress PRs get light comments, not the same bar as ready-to-merge
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load the starter and practice approve versus request changes on a few PRs
- On real Git, review a branch with log and diff before merging
- When you are ready

