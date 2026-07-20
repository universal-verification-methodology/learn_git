---
marp: true
title: Git mental model
paginate: true
---

# Git mental model

This module is the picture you keep in your head while you use Git

---

## Three places for your changes
- Git keeps three related views of a project
- The working tree is what you see and edit on disk
- The staging area, also called the index, is what you have prepared for the next snapshot
- HEAD is the last commit: the durable history you already recorded
- You move content forward with add, then commit
- You can move it back with restore when you need to undo a step safely

---

## Browser lab
![Git mental model lab starter](assets/lab-starter.png)

---

## Real Git practice
![Real shell — init, status, add, commit](assets/real-shell.png)

---

## Real Git practice — try these

```
# git --version — confirm Git is installed
git --version

# git init — create a new repository here
git init

# echo … > note.txt — create a file in the working tree
echo "notes" > note.txt

# git status — what is modified, staged, or untracked?
git status

# git add note.txt — copy the change into the staging area
git add note.txt

# git status — confirm it is staged for commit
git status

# git commit -m "…" — record a snapshot from what is staged
git commit -m "first snapshot"

# git log --oneline — show recent commits, one line each
git log --oneline

```

---

## Pitfalls to watch
- Do not treat the staging area as optional decoration, commit only records what you staged
- Do not confuse “saved in the editor” with “committed in Git.” And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load the starter and finish a few challenges
- On real Git, repeat status, add, and commit in your practice tree
- When you are ready, take the short quiz, then continue to the next module

