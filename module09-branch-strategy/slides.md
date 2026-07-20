---
marp: true
title: Branch naming
paginate: true
---

# Branch naming

Branches let you isolate work, a lab feature, a bugfix, a submission, without destabilizing main

---

## Prefix, slug, then branch
- Use a typed prefix
- Branch from main after you have fetched the latest tip, not from random work in progress
- One concern per branch keeps reviews and merges readable

---

## Browser lab
![Branch naming lab starter](assets/lab-starter.png)

---

## Real Git practice
![Real shell — create and switch branches](assets/real-shell.png)

---

## Real Git practice — try these

```
# git init — create a new repository here
git init

# echo … > notes.md — create and commit on main
echo "v1" > notes.md
git add notes.md
git commit -m "Add notes"

# git branch -M main — name the default branch main
git branch -M main

# git branch — list branches; star marks current
git branch

# git checkout -b feature/readme-update — create and switch
git checkout -b feature/readme-update

# echo … >> notes.md — edit on the feature branch
echo "feature edit" >> notes.md

# git add notes.md — stage the change
git add notes.md

# git commit -m "Update notes on feature branch" — commit here
git commit -m "Update notes on feature branch"

# git checkout main — switch back to main
git checkout main

# git log --oneline --all — see both branch tips
git log --oneline --all

```

---

## Pitfalls to watch
- Do not use spaces or vague names like my branch
- Do not branch from a stale main when the team expects you to fetch first
- Delete merged feature branches so the list stays short
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load the starter and fix a few weak branch names until validation passes
- On real Git, create a feature branch, commit once, and switch back to main
- When you are ready

