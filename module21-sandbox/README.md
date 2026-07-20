# Module 21: Live sandbox: clone → Make → PR

**Kind:** `offline` · Activity: `unix-git-practice` (live GitHub sandbox)

[← Submission reproducibility](../module20-submission-repro/README.md) · [Course README](../README.md) · [Git path complete →](../module22-wrap/README.md)

## Outcomes

After this module you can **clone → Make → PR** on a real GitHub template without touching the curriculum tree.

## Practice surface (Track A only)

This module has **no browser lab**. Use the org sandbox:

1. Read [SANDBOX.md](../SANDBOX.md).
2. On GitHub: [unix-git-practice](https://github.com/universal-verification-methodology/unix-git-practice) → **Use this template**.
3. Clone with submodules, run `make test`, then open a practice PR on *your* fork.
4. Optional shared-IP pin: [https://github.com/universal-verification-methodology/unix-git-shared-ip](https://github.com/universal-verification-methodology/unix-git-shared-ip).

```bash
git clone --recurse-submodules https://github.com/<YOU>/unix-git-practice.git
cd unix-git-practice
make test
bash scripts/check_ready.sh
```

Explore-only (no push):

```bash
git clone --recurse-submodules \
  https://github.com/universal-verification-methodology/unix-git-practice.git
```

## Track B

None — use earlier remotes / conflicts / blame labs if you need concept refreshers.

## Media

| Artifact | Path |
|----------|------|
| Transcript | [transcript.md](transcript.md) |
| Outline | [outline.yaml](outline.yaml) |
| Slides | [slides.pptx](slides.pptx) · [slides.pdf](slides.pdf) |
| Video | [video.mp4](video.mp4) |
| Quiz | [quiz.json](quiz.json) |

## Files

```
module21-sandbox/
├── README.md
├── CHECKLIST.md
├── EXAMPLES.md
├── outline.yaml
├── transcript.md
└── examples/       # local rehearsal notes (Track A)
```
