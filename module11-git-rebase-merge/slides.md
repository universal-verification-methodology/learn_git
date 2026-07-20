---
marp: true
title: Rebase vs merge
paginate: true
---

# Rebase vs merge

Two branches diverged, now you want them together

---

## When to pick which
- Nobody else has built on your commits
- Merge when integrating into a shared branch
- Never rebase commits others are using

---

## Browser lab
![Rebase vs merge chooser starter](assets/lab-starter.png)

---

## Real Git practice
![Real shell — rebase feature onto main](assets/real-shell.png)

---

## Real Git practice — try these

```
# git init — create a new repository here
git init

# echo … > notes.md — base commit on main
echo "base" > notes.md
git add notes.md
git commit -m "Base"
git branch -M main

# git checkout -b feature/update — start feature work
git checkout -b feature/update
echo "feature only" > feature.txt
git add feature.txt
git commit -m "Feature work"

# git checkout main — main moves forward separately
git checkout main
echo "main update" >> notes.md
git add notes.md
git commit -m "Main moved forward"

# git checkout feature/update — return to your branch
git checkout feature/update

# git rebase main — replay feature commits on latest main
git rebase main

# git log --oneline --graph --all — see linear replayed history
git log --oneline --graph --all

```

---

## Pitfalls to watch
- Do not rebase main or any branch teammates share without agreement
- After you rebase a branch you already pushed
- Merge is fine when you want to preserve the exact integration moment
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load the starter and justify a few rebase versus merge picks
- On real Git, rebase a feature branch onto main and read the graph
- When you are ready, take the short quiz, then continue to the next module on cherry-pick

