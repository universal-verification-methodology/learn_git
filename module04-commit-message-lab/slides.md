---
marp: true
title: Commit messages
paginate: true
---

# Commit messages

A commit is a snapshot; the message is how humans find it later

---

## Subject first, why next
- Why you did it, and how to check it, for example, which make target or testbench to run
- The log becomes a readable story, not a pile of filenames

---

## Browser lab
![Commit message lab starter](assets/lab-starter.png)

---

## Real Git practice
![Real shell — commit with a clear message](assets/real-shell.png)

---

## Real Git practice — try these

```
# git init — create a new repository here
git init

# echo … > notes.md — create a file in the working tree
echo "lab notes" > notes.md

# git add notes.md — stage the new file
git add notes.md

# git commit -m "…" — record with an imperative subject
git commit -m "Add lab notes"

# echo … >> notes.md — append a second line
echo "reset polarity fixed in TB" >> notes.md

# git add notes.md — stage the update
git add notes.md

# git commit -m "…" — explain why in the subject
git commit -m "Note TB reset polarity fix"

# git log --oneline — show short hash plus subject
git log --oneline

```

---

## Pitfalls to watch
- Do not end the subject with a period, and do not paste a whole diff into the subject line
- Avoid past-tense “Added” when style calls for imperative “Add.” And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load the starter and rewrite a few weak messages until the checks pass
- On real Git, make two small commits with subjects you would be willing to show a teammate
- When you are ready

