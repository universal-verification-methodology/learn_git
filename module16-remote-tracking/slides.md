---
marp: true
title: Remote-tracking branches
paginate: true
---

# Remote-tracking branches

Your laptop keeps local branches like main

---

## Fetch, track, compare
- Fetch downloads new commits and updates origin slash star refs only
- Pull is fetch plus integrate into your current branch, usually a merge
- Set upstream with push minus u or branch minus u so status and push know which remote
- Prune stale origin refs after branches are deleted on the host

---

## Browser lab
![Remote-tracking lab starter](assets/lab-starter.png)

---

## Real Git practice
![Real shell — fetch, branch refs, prune](assets/real-shell.png)

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

# git init --bare ../origin.git — bare remote (simulates GitHub)
git init --bare ../origin.git

# git remote add origin … — link the hosted copy
git remote add origin ../origin.git

# git push -u origin main — publish and set upstream tracking
git push -u origin main

# git clone ../origin.git ../teammate — second clone (teammate)
git clone ../origin.git ../teammate

# (in teammate) echo … >> README.md — push new commit to origin
# (in teammate) git push origin main

# git fetch origin — refresh origin/* without merging
git fetch origin

# git branch -r — list remote-tracking branches
git branch -r

# echo … >> README.md — local commit (now ahead of last fetch)
echo "local work" >> README.md

# git add README.md — stage the change
git add README.md

# git commit -m "local commit" — commit on main
git commit -m "local commit"

# git branch -vv — show upstream and ahead/behind hints
git branch -vv

# git push origin feature-tmp — publish a short-lived branch
git checkout -b feature-tmp
git push -u origin feature-tmp

# git push origin --delete feature-tmp — remove branch on remote
git push origin --delete feature-tmp

# git fetch origin — update refs after remote delete
git fetch origin

# git remote prune origin — drop stale origin/* refs
git remote prune origin

```

---

## Pitfalls to watch
- Fetch is safe
- Do not confuse origin slash main with your local main
- Prune only removes stale remote-tracking refs, not your local branches
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load the starter and clear a few ahead-or-behind challenges
- On real Git, run fetch, read branch minus v v, and prune a deleted remote branch
- When you are ready

