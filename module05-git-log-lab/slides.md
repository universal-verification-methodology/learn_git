---
marp: true
title: git log options
paginate: true
---

# git log options

History is only useful if you can read it

---

## Scan, graph, then zoom
- Start with oneline for a short hash plus subject
- Add a count like minus five when you only need the recent tip
- Use graph with all to sketch how branches meet
- When you need detail, name-only lists paths touched

---

## Browser lab
![git log lab starter](assets/lab-starter.png)

---

## Real Git practice
![Real shell — oneline, graph, and path filters](assets/real-shell.png)

---

## Real Git practice — try these

```
# git log --oneline — short hash plus subject for each commit
git log --oneline

# git log --oneline -3 — only the last three commits
git log --oneline -3

# git log --oneline --graph --all — compact history with branch shape
git log --oneline --graph --all

# git log --name-only -1 — paths touched by the latest commit
git log --name-only -1

# git log --oneline -- notes.md — commits that touched this path
git log --oneline -- notes.md

```

---

## Pitfalls to watch
- Do not confuse a path filter, two dashes then a path, with a branch name
- Remember that graph without oneline can be noisy on a long history
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load the starter and clear a few option challenges
- On real Git, practice oneline, a limit, graph, and a path filter in your practice tree
- When you are ready, take the short quiz, then continue to the next module on safe undo

