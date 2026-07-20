# Module 18 — Submodule pitfalls

**Module id:** module18-submodule-pitfalls  
**Lab:** submodule-pitfalls  
**Tracks:** A · B

## Slide 1 — Submodule pitfalls

A submodule embeds another repository at a pinned commit—the parent stores a gitlink, not a copy of every file. That design is powerful for shared RTL or verification libraries, but it comes with sharp edges. Clone without init and the folder looks empty. Checkout inside the submodule is usually detached at the pinned SHA. Bump the library without committing the parent and teammates still get the old pin. This module teaches those pitfalls before they bite your chip repo.

## Slide 2 — Init, detached HEAD, pin bumps

After a normal clone, run submodule update init recursive—or clone with recurse submodules in one step. Inside the submodule, detached HEAD is normal: the parent chose a specific commit, not a branch tip. To move the pin, update the submodule checkout, then stage and commit the path in the parent so the gitlink changes. Push the submodule commit to its remote first if needed, then push the parent. Two repos, two push steps—easy to forget one.

## Slide 3 — Browser lab

![Submodule pitfalls lab starter](assets/lab-starter.png)

In the browser lab, load the starter example—you have cloned the chip repo but the vendor library folder is still empty. Look at three pitfall cards—forgotten init, detached HEAD, and pin updates—the repo tree, and the challenge panel above. Run init, inspect detached state, bump the pin, and commit the parent. Use Check when your scenario matches the challenge. You do not need a full tour here—the lab itself guides the rest. Work a few challenges, then come back for the real Git track.

## Slide 4 — Real Git practice

![Real shell — init, detached HEAD, bump pin](assets/real-shell.png)

In the real Git track, build a parent repo with a library submodule pinned at an older commit. Clone the parent without initializing submodules and show the empty vendor path. Run submodule update init, read the library file, and show detached HEAD inside the submodule. Advance the library, check out the new SHA in the submodule, then commit the parent so the pin moves.

```bash
# (setup) parent repo pins vendor/dv-lib at lib v1

# git clone <parent> fresh-clone — clone without submodules populated
git clone file://…/parent fresh-clone

# ls vendor/dv-lib — empty until init
ls vendor/dv-lib

# git submodule status — minus prefix means not initialized
git submodule status

# git submodule update --init --recursive — populate submodule checkout
git submodule update --init --recursive

# cat vendor/dv-lib/VERSION — library files appear
cat vendor/dv-lib/VERSION

# cd vendor/dv-lib — enter the submodule
cd vendor/dv-lib

# git status — detached HEAD at the pinned commit
git status

# git fetch — see newer library commits
git fetch

# git checkout <new-sha> — move submodule to newer pin candidate
git checkout <new-sha>

# cd ../.. — back to parent repo root
cd ../..

# git add vendor/dv-lib — stage the new gitlink
git add vendor/dv-lib

# git commit -m "Bump dv-lib pin" — parent records the new pin
git commit -m "Bump dv-lib pin"

# git submodule status — verify pin moved
git submodule status
```

## Slide 5 — Pitfalls to watch

An empty vendor or external folder after clone almost always means forgotten init—not a missing remote. Do not commit only inside the submodule and stop; the parent must record the new SHA. Detached HEAD inside a submodule is expected until you deliberately switch a branch for development. CI should clone with recurse submodules or run init in the build script. And remember: the browser lab is for literacy—real shared IP still needs disciplined pin bumps and pushes on both repos.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, load the starter and fix init, detached HEAD, and pin-update scenarios. On real Git, clone, init, inspect status inside the submodule, and bump the parent pin. When you are ready, take the short quiz, then continue to the next module on template-repo bootstrap.
