# Module 19 — Template-repo bootstrap

**Module id:** module19-template-clone  
**Lab:** template-clone  
**Tracks:** A · B

## Slide 1 — Template-repo bootstrap

Course labs often start from a template repository—not a blank folder. GitHub’s use this template gives you a writable copy with the right layout already in place. Your first job after clone is orientation: where is the RTL, where are testbenches and scripts, and is the working tree clean? This module bootstraps that habit before you touch real coursework repos.

## Slide 2 — Clone, map, status

Clone the template URL into a project folder, change into it, and list the top level. Expect directories like rtl, tb, scripts, and docs—plus a Makefile or README that explains how to build and test. Run status right away: you should be on main with a clean tree and origin pointing at your remote. Read gitignore and env example files so you know what not to commit. Map the layout before you write new code.

## Slide 3 — Browser lab

![Template clone lab starter](assets/lab-starter.png)

In the browser lab, load the starter example—your home directory is empty until you create a copy from the chip template. Look at the lab terminal, the layout tree, and the challenge panel above. Clone or use template, change into the project folder, inspect rtl and tb, then run status and remote. Use Check when you match a challenge. You do not need a full tour here—the lab itself guides the rest. Explore a few challenges, then come back for the real Git track.

## Slide 4 — Real Git practice

![Real shell — clone template and inspect](assets/real-shell.png)

In the real Git track, simulate a course template with rtl, tb, scripts, and docs. Clone it into a new project directory, list the layout, and confirm a clean status on main. Show the remote URL and branch so you know where push will go later.

```bash
# (setup) chip-template repo with rtl/, tb/, scripts/, docs/

# git clone <template-url> chip-lab — copy template into your workspace
git clone ../chip-template chip-lab

# cd chip-lab — work inside the new project
cd chip-lab

# ls -la — see top-level files and folders
ls -la

# ls rtl tb scripts docs — map source, tests, and tooling
ls rtl tb scripts docs

# cat README.md — read quick-start notes
cat README.md

# git status — confirm clean tree on main
git status

# git remote -v — see where origin points
git remote -v

# git branch — confirm current branch name
git branch
```

## Slide 5 — Pitfalls to watch

Clone into a fresh folder name—you do not want to nest a repo inside another by accident. If status is not clean immediately after clone, find out why before you start editing. Do not commit env files with secrets—copy from env example instead. And remember: the browser lab is for literacy—real assignments still need your GitHub template or sandbox clone with submodules if applicable.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, load the starter, bootstrap chip-lab, and run your first status. On real Git, clone a template tree and map rtl, tb, and scripts. When you are ready, take the short quiz, then continue to the next module on submission reproducibility.
