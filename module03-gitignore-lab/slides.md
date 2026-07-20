---
marp: true
title: .gitignore patterns
paginate: true
---

# .gitignore patterns

Simulators and builds leave junk behind, logs, waveform dumps, object files, whole output folders

---

## Ignore means “do not track”
- A `.gitignore` file lives at the repo root and lists patterns
- Matching untracked paths disappear from status and will not be added by mistake
- Typical design patterns ignore a build directory, log files, and waveform dumps
- Remember: ignore rules apply to untracked files

---

## Browser lab
![.gitignore lab starter](assets/lab-starter.png)

---

## Real Git practice
![Real shell — status before and after .gitignore](assets/real-shell.png)

---

## Real Git practice — try these

```
# git init — create a new repository here
git init

# mkdir -p build — make a build output folder
mkdir -p build

# touch build/output.tmp — fake a generated file
touch build/output.tmp

# git status — see the untracked build output
git status

# printf … > .gitignore — ignore the build/ directory
printf 'build/\n*.log\n*.vcd\n' > .gitignore

# git status — build output should no longer appear
git status

```

---

## Pitfalls to watch
- Do not commit large regenerated files and then add ignore later
- Do not ignore your RTL or testbench sources by accident with a broad star pattern
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load the starter and finish a few challenges
- On real Git, copy or adapt the sample ignore file from this module’s examples into your
- When you are ready

