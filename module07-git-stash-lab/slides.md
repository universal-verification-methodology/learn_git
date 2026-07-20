---
marp: true
title: Stash scenarios
paginate: true
---

# Stash scenarios

Sometimes you are mid-edit and need a clean tree, to switch branches, pull updates, or run a quick experiment

---

## Push, list, then pop or apply
- Stash push saves tracked dirty files and resets the working tree to match HEAD
- Stash list shows the stack, newest on top
- Stash pop applies the top entry and removes it from the stack
- By default stash does not include untracked files; add minus u when you need those too

---

## Browser lab
![Stash lab starter](assets/lab-starter.png)

---

## Real Git practice
![Real shell — stash push, list, pop](assets/real-shell.png)

---

## Real Git practice — try these

```
# git init — create a new repository here
git init

# echo … > notes.md — create and commit a tracked file
echo "v1" > notes.md
git add notes.md
git commit -m "Add notes"

# echo … >> notes.md — edit without committing
echo "wip draft" >> notes.md

# git status — see modified, not staged
git status

# git stash push -m "WIP notes" — save dirty tree, clean working tree
git stash push -m "WIP notes"

# git status — working tree should be clean
git status

# git stash list — show the stash stack
git stash list

# git stash pop — apply top stash and remove it
git stash pop

# git status — edits should be back
git status

```

---

## Pitfalls to watch
- Do not stash and forget, run stash list so old entries do not pile up
- Remember pop can conflict if the branch moved; apply is gentler while you are learning
- Untracked files need stash push with minus u
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load the starter and finish a push-then-pop challenge
- On real Git, stash, list, and pop in your practice tree
- When you are ready, take the short quiz, then continue to the next module on tags

