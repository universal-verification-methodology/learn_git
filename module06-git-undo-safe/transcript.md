# Module 06 — Safe undo

**Module id:** module06-git-undo-safe  
**Lab:** git-undo-safe  
**Tracks:** A · B

## Slide 1 — Safe undo

You will edit the wrong file, stage too early, or want to back out of a local mistake. Safe undo means knowing which command touches the working tree, the staging area, or history—and choosing the gentle one first. This module practices restore and unstage before you reach for hard reset or force push.

## Slide 2 — Restore before reset

To drop unstaged edits in a tracked file, use restore on that path—it rewinds the working tree to match the index or last commit. To unstage without losing your edits, use restore with staged—the file stays changed on disk but leaves the staging area. Soft reset moves HEAD back while keeping your staged work; mixed reset also unstages. Hard reset throws away local changes—save that for when you truly mean it.

## Slide 3 — Browser lab

![Safe Git undo lab starter](assets/lab-starter.png)

In the browser lab, look at three pieces: the challenge card, the three-layers diagram, and the undo-action buttons—unstage, restore, and soft reset. Load the starter example, try one safe action, and watch which layer moves. Use Check when you think a challenge is done. You do not need a full tour here—the lab itself guides the rest. Explore a few challenges, then come back for the real Git track.

## Slide 4 — Real Git practice

![Real shell — restore and unstage](assets/real-shell.png)

In the real Git track, create a tiny repo with one committed notes file. Edit the file without staging, run status to see the modification, then restore to discard those unstaged edits. Edit again, stage with add, run status to see it staged, then restore with staged to unstage while keeping your text on disk. Status should show modified but not staged—that is the safe habit when you clicked add too soon.

```bash
# git init — create a new repository here
git init

# echo … > notes.md — create and commit a tracked file
echo "v1" > notes.md
git add notes.md
git commit -m "Add notes"

# echo … >> notes.md — edit without staging
echo "draft line" >> notes.md

# git status — see modified, not staged
git status

# git restore notes.md — discard unstaged edits
git restore notes.md

# echo … >> notes.md — edit again
echo "draft line" >> notes.md

# git add notes.md — stage the change
git add notes.md

# git restore --staged notes.md — unstage, keep edits on disk
git restore --staged notes.md

# git status — modified but not staged
git status
```

## Slide 5 — Pitfalls to watch

Do not confuse unstage with discard—restore staged keeps your edits; plain restore does not. Avoid reset hard until you have tried restore and soft or mixed reset. And remember: the browser lab is for literacy—never force-push shared history because a concept lab let you click a dangerous button.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, load the starter and practice unstage versus restore on a few challenges. On real Git, repeat restore and restore staged in your practice tree. When you are ready, take the short quiz, then continue to the next module on stash scenarios.
