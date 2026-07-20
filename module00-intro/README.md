# Module 00: Welcome to Git for coursework

**Kind:** `intro` · Dual-track course welcome

← Start · [Course README](../README.md) · [Git mental model →](../module01-git-mental-model/README.md)

## What this course is

**learn_git** teaches Git for coursework through delivery using **two learning modes** on every lab module:

| Track | Where you practice | Best for |
|-------|--------------------|----------|
| **A — Real Git** | Local Git + sandbox template | Muscle memory, remotes, PRs you keep |
| **B — Browser lab** | Interactive lab on the learning platform | Concept literacy, no install, quick feedback |

You can do **A only**, **B only**, or **both** (recommended: B for intuition, then A for fidelity).

## Setup (Track A)

1. Open a terminal (WSL2 recommended on Windows).
2. Confirm `git --version` works.
3. Clone or open this repo and `cd` into `courses/learn_git`.
4. Run: `./scripts/scaffold.sh` to create `~/unix_practice/git_demo/`.
5. Optional: use the org template — see [SANDBOX.md](../SANDBOX.md).

## Setup (Track B)

1. Serve the platform: `python -m http.server 8080 --directory platform` (from monorepo root).
2. Open http://127.0.0.1:8080/tools/index.html
3. Or use the live site: https://universal-verification-methodology.github.io/learning/tools/

## How to move through modules

1. Read the module **README** (outcomes).
2. Pick a track (or both).
3. Check off **CHECKLIST.md**.
4. Optional: skim `outline.yaml` / `transcript.md` for upcoming slides & clips.

## Media

| Artifact | Path |
|----------|------|
| Transcript | [transcript.md](transcript.md) |
| Outline | [outline.yaml](outline.yaml) |
| Slides | [slides.pptx](slides.pptx) · [slides.pdf](slides.pdf) |
| Video | [video.mp4](video.mp4) |
| Quiz | [quiz.json](quiz.json) |

## Next

→ [Module 01: Git mental model](../module01-git-mental-model/README.md)
