# Module 15 — Remotes, PRs & submodules

**Module id:** module15-remotes  
**Lab:** remotes  
**Tracks:** A · B

## Slide 1 — Remotes, PRs & submodules

Local Git is only half the story. A remote is a named link to a hosted copy—usually called origin—where you push branches and open pull requests for review. Submodules let one repo pin another repo’s commit inside a path, which is common for shared RTL or verification IP. This module connects those ideas to how you will submit labs and collaborate on real projects.

## Slide 2 — Push, review, embed

Add a remote with a URL, push your branch with upstream tracking so later pushes are simple, then open a pull request that proposes merging your branch into main. Reviewers read the diff, you push more commits to the same branch if needed, and merge when it is approved. A submodule records a gitlink—the path plus an exact commit—not a casual copy of files. After cloning a repo with submodules, you must initialize them or those folders stay empty.

## Slide 3 — Browser lab

![Remotes lab — quiz and live checklist](assets/lab-starter.png)

In the browser lab, look at three pieces: the concept quiz at the top, the numbered live GitHub checklist, and the sandbox repo links in the banner. Work a few quiz questions to lock in vocabulary—origin, upstream push, submodule init. Then read the checklist steps for clone with submodules, lab branch, push, and opening a pull request. You do not need a full tour here—the lab itself guides the rest. Explore the quiz and skim the steps, then come back for the real Git track.

## Slide 4 — Real Git practice

![Real shell — remote, push, submodule](assets/real-shell.png)

In the real Git track, simulate a hosted remote with a bare repository on disk. Commit on main, add the bare repo as origin, and push main upstream. Create a lab branch, commit, and push that branch too. List remotes to see fetch and push URLs. Then add a small library repo as a submodule and show submodule status so you see the pinned commit.

```bash
# git init — create a new repository here
git init

# echo … > README.md — first commit on default branch
echo "practice v1" > README.md
git add README.md
git commit -m "init"

# git branch -M main — name the default branch main
git branch -M main

# git init --bare ../origin.git — bare remote (simulates GitHub)
git init --bare ../origin.git

# git remote add origin … — link the hosted copy
git remote add origin ../origin.git

# git push -u origin main — publish main and set upstream
git push -u origin main

# git checkout -b lab1 — branch for lab work
git checkout -b lab1

# echo … >> README.md — edit on the lab branch
echo "lab1 change" >> README.md

# git add README.md — stage the change
git add README.md

# git commit -m "lab1: update README" — commit on lab1
git commit -m "lab1: update README"

# git push -u origin lab1 — publish lab branch with upstream
git push -u origin lab1

# git remote -v — show remote names and URLs
git remote -v

# git submodule add … external/shared-ip — pin another repo
git submodule add ../shared-lib external/shared-ip

# git submodule status — show pinned submodule commit
git submodule status
```

## Slide 5 — Pitfalls to watch

Do not force-push shared default branches like main. After clone, run submodule init if embedded folders are empty. A pull request is for review and visibility—the merge still happens on the host or after someone pulls and merges locally. And remember: the browser lab is for literacy—real coursework still needs your fork or template repo on GitHub and the live checklist steps.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, clear a few quiz items and read the live GitHub steps end to end. On real Git, practice push with upstream and inspect a submodule status line. When you are ready, take the short quiz, then continue to the next module on remote-tracking branches.
