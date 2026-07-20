# Module 12 — Cherry-pick

**Module id:** module12-git-cherry-pick-lab  
**Lab:** git-cherry-pick-lab  
**Tracks:** A · B

## Slide 1 — Cherry-pick

Sometimes you want one commit from another branch—not the whole merge. Cherry-pick copies that commit’s changes onto your current branch as a new commit with a new hash. Use it for a single bugfix on main, a backport to a release branch, or any selective apply.

## Slide 2 — Find the commit, then pick it

On the source branch, use log to find the short hash you need. Check out the target branch, then cherry-pick that hash. Git replays the diff; if it applies cleanly, you get a fresh commit. If not, resolve conflicts, stage, and cherry-pick continue—or abort to undo the attempt.

## Slide 3 — Browser lab

![Cherry-pick lab starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge card, the branch and commit list, and the cherry-pick, continue, and abort buttons. Load the starter example, select a commit, and try a clean pick versus a conflict case. Use Check when you think a challenge is done. You do not need a full tour here—the lab itself guides the rest. Explore a few challenges, then come back for the real Git track.

## Slide 4 — Real Git practice

![Real shell — log, cherry-pick one commit onto main](assets/real-shell.png)

In the real Git track, create main with a base commit, then make a feature branch with one extra commit you want elsewhere. Log the feature branch to copy the hash, switch to main, and cherry-pick that commit. Show log again—you should see the same change idea on main as a new commit, while the original stays on the feature branch.

```bash
# git init — create a new repository here
git init

# echo … > notes.md — base commit on main
echo "base" > notes.md
git add notes.md
git commit -m "Base"
git branch -M main

# git checkout -b feature/fix — branch for the commit to copy
git checkout -b feature/fix
echo "hotfix" > fix.txt
git add fix.txt
git commit -m "Add hotfix on feature"

# git log --oneline feature/fix — find the commit hash
git log --oneline feature/fix

# git checkout main — target branch for the pick
git checkout main

# git cherry-pick <hash> — apply that commit onto main
git cherry-pick feature/fix

# git log --oneline --all — see the new commit on main
git log --oneline --all
```

## Slide 5 — Pitfalls to watch

Cherry-pick creates a duplicate commit—fine for a fix, confusing if you later merge the whole branch. Avoid picking merge commits unless you know parent selection. If conflicts appear, finish with continue or abort—do not leave a half-finished pick. And remember: the browser lab is for literacy—real backports still need the same careful hash choice in a real repo.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, load the starter and complete a clean pick and a conflict recovery. On real Git, cherry-pick one commit from a feature branch onto main. When you are ready, take the short quiz, then continue to the next module on reflog recovery.
