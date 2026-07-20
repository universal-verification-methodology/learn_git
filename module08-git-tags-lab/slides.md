---
marp: true
title: Tags
paginate: true
---

# Tags

Tags mark a commit you want to find again, a release, a submission snapshot, or a known-good point for bisect

---

## Lightweight vs annotated
- A lightweight tag is simply a name pointing at a commit, quick for local milestones
- An annotated tag stores a message, tagger, and date, better for releases you share
- Use tag to list names, show to inspect one

---

## Browser lab
![Tags lab starter](assets/lab-starter.png)

---

## Real Git practice
![Real shell — lightweight and annotated tags](assets/real-shell.png)

---

## Real Git practice — try these

```
# git init — create a new repository here
git init

# echo … > notes.md — create and commit a tracked file
echo "v1" > notes.md
git add notes.md
git commit -m "Add notes"

# git tag v1.0 — lightweight tag on this commit
git tag v1.0

# git tag — list tag names
git tag

# git show v1.0 — inspect what the tag points to
git show v1.0

# git tag -a v1.0.0 -m "Release 1.0" — annotated tag with message
git tag -a v1.0.0 -m "Release 1.0"

# git show v1.0.0 — see tag message and commit
git show v1.0.0

```

---

## Pitfalls to watch
- Do not reuse a tag name for a different commit without deleting the old one first
- Do not assume push sends tags, use push with tags or push the tag name explicitly
- Prefer annotated tags for anything you publish
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser
- On real Git, tag, list, and show in your practice tree
- When you are ready, take the short quiz, then continue to the next module on branch naming

