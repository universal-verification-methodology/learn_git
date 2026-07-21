# learn_git

[![GitHub](https://img.shields.io/badge/GitHub-learn__git-181717?logo=github)](https://github.com/universal-verification-methodology/learn_git)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](LICENSE)
[![Role](https://img.shields.io/badge/role-Git%20submodule-orange)](https://github.com/universal-verification-methodology/learning)
[![Parent](https://img.shields.io/badge/parent-learning%20monorepo-0A9EDC)](https://github.com/universal-verification-methodology/learning)
[![Labs](https://img.shields.io/badge/labs-GitHub%20Pages-222?logo=githubpages)](https://universal-verification-methodology.github.io/learning/tools/)
[![Domain](https://img.shields.io/badge/domain-Git%20%7C%20coursework%20%7C%20delivery-purple)](https://github.com/universal-verification-methodology/learn_git)

**learn_git** is the open learning path for *Git for coursework through delivery*.

Readers and students usually **open a module README** (or the live tools) or clone this public repo. Authors edit content here (or via the parent monorepo checkout), rebuild slides/audio with **module-slides** in the parent, and push; the parent repo only stores a pinned submodule commit.


## Table of contents

- [Contents](#contents)
- [Browse or clone](#browse-or-clone)
- [Consume from the parent](#consume-from-the-parent)
- [Author: publish or update](#author-publish-or-update)
- [Two learning tracks](#two-learning-tracks)
- [Module landings](#module-landings)
- [Browser labs](#browser-labs)
- [License](#license)

## Contents

```text
learn_git/
├── README.md
├── LICENSE              # CC BY 4.0
├── SANDBOX.md           # unix-git-practice + shared-ip
├── docs/
│   ├── MODULES.md       # full module index (00–22)
│   └── TWO_TRACKS.md    # Track A (real Git) vs Track B (browser)
├── scripts/
│   ├── scaffold.sh      # Track A practice repo
│   └── module.sh        # per-module --check helpers
├── module00-intro/
├── module01-git-mental-model/
│   ├── README.md
│   ├── CHECKLIST.md
│   ├── EXAMPLES.md
│   ├── outline.yaml
│   ├── transcript.md
│   ├── examples/        # Track A
│   └── (optional) slides.pptx / slides.pdf / video.mp4 / assets/
├── …
└── module22-wrap/
```

Videos and decks are optional per module. Generate with the **module-slides** skill (`.cursor/skills/module-slides/`) in the parent monorepo when ready.

## Browse or clone

- **Browser labs:** [https://universal-verification-methodology.github.io/learning/tools/](https://universal-verification-methodology.github.io/learning/tools/)
- **Sandbox:** [SANDBOX.md](SANDBOX.md) · [unix-git-practice](https://github.com/universal-verification-methodology/unix-git-practice)
- **Syllabus (parent):** [`syllabus.md` § learn_git](https://github.com/universal-verification-methodology/learning/blob/main/syllabus.md#2-learn_git)
- **Clone this repo alone:**

```bash
git clone https://github.com/universal-verification-methodology/learn_git.git
cd learn_git
chmod +x scripts/*.sh
./scripts/scaffold.sh          # Track A practice repo
./scripts/module.sh 01 --check # optional env check for module 01
```

Then open [module00-intro/README.md](module00-intro/README.md).

## Consume from the parent

From a clone of the **learning** monorepo (lists this repo in `.gitmodules` when registered):

```bash
git clone --recurse-submodules \
  git@github.com:universal-verification-methodology/learning.git
# or, if already cloned without submodules:
git submodule update --init --recursive

ls courses/learn_git
```

Working tree path in the parent: `courses/learn_git/` → this repository at a pinned commit.

## Author: publish or update

Edit inside the parent monorepo (recommended) or in a standalone clone of this repo.

```bash
# from the learning monorepo checkout
cd courses/learn_git
# … edit module README / CHECKLIST / EXAMPLES / transcript …

# rebuild media from the parent (one module at a time):
cd ../..
# revise transcript.md, then:
python .cursor/skills/module-slides/scripts/transcript_to_outline.py \
  courses/learn_git/moduleNN-slug
bash .cursor/skills/module-slides/scripts/narrate_clips.sh \
  courses/learn_git/moduleNN-slug

cd courses/learn_git
git add -A
git commit -m "Update learn_git modules"
git push origin main
```

Then bump the pin in the **parent**:

```bash
cd /path/to/learning
git add courses/learn_git
git commit -m "Bump learn_git submodule"
git push
```

See the skill `SKILL.md` for dual-track narration rules and the full PPTX → PDF → TTS → MP4 pipeline.

## Two learning tracks

Every **lab** module documents both tracks. Intro/wrap have no lab; module 21 is **offline** sandbox only. Details: [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md).

| Track | Practice surface | Start here |
|-------|------------------|------------|
| **A — Real Git** | Local Git + `examples/` + sandbox | `./scripts/scaffold.sh` · [SANDBOX.md](SANDBOX.md) |
| **B — Browser lab** | Platform tools | [local tools](http://127.0.0.1:8080/tools/) · [live](https://universal-verification-methodology.github.io/learning/tools/) |

Recommended path: short Track B starter → Track A examples + checklist → module 21 sandbox → optional quiz / transcript review.

## Module landings

Full status table: **[docs/MODULES.md](docs/MODULES.md)**. Clusters: 00 intro · 01–08 model/commit/history · 09–14 branch/integrate/recover · 15–20 remotes/delivery · 21 sandbox · 22 wrap.

| Module | Landing |
|--------|---------|
| 00 — Welcome to Git for coursework | [module00-intro](module00-intro/README.md) |
| 01 — Git mental model | [module01-git-mental-model](module01-git-mental-model/README.md) |
| 02 — Graph, stage, commit (playground) | [module02-git-graph](module02-git-graph/README.md) |
| 03 — .gitignore patterns | [module03-gitignore-lab](module03-gitignore-lab/README.md) |
| 04 — Commit messages | [module04-commit-message-lab](module04-commit-message-lab/README.md) |
| 05 — git log options | [module05-git-log-lab](module05-git-log-lab/README.md) |
| 06 — Safe undo | [module06-git-undo-safe](module06-git-undo-safe/README.md) |
| 07 — Stash scenarios | [module07-git-stash-lab](module07-git-stash-lab/README.md) |
| 08 — Tags | [module08-git-tags-lab](module08-git-tags-lab/README.md) |
| 09 — Branch naming | [module09-branch-strategy](module09-branch-strategy/README.md) |
| 10 — Merge conflicts | [module10-git-conflicts](module10-git-conflicts/README.md) |
| 11 — Rebase vs merge | [module11-git-rebase-merge](module11-git-rebase-merge/README.md) |
| 12 — Cherry-pick | [module12-git-cherry-pick-lab](module12-git-cherry-pick-lab/README.md) |
| 13 — Reflog recovery | [module13-git-reflog](module13-git-reflog/README.md) |
| 14 — Blame & bisect | [module14-blame-bisect](module14-blame-bisect/README.md) |
| 15 — Remotes, PRs & submodules (concepts) | [module15-remotes](module15-remotes/README.md) |
| 16 — Remote-tracking branches | [module16-remote-tracking](module16-remote-tracking/README.md) |
| 17 — PR review checklist | [module17-pr-review-lab](module17-pr-review-lab/README.md) |
| 18 — Submodule pitfalls | [module18-submodule-pitfalls](module18-submodule-pitfalls/README.md) |
| 19 — Template-repo bootstrap | [module19-template-clone](module19-template-clone/README.md) |
| 20 — Submission reproducibility | [module20-submission-repro](module20-submission-repro/README.md) |
| 21 — Live sandbox: clone → Make → PR | [module21-sandbox](module21-sandbox/README.md) |
| 22 — Git path complete | [module22-wrap](module22-wrap/README.md) |

## Browser labs

By workflow (Track B): [git-mental-model](https://universal-verification-methodology.github.io/learning/tools/git-mental-model/) → [git-graph](https://universal-verification-methodology.github.io/learning/tools/git-graph/) → [gitignore-lab](https://universal-verification-methodology.github.io/learning/tools/gitignore-lab/) → [commit-message-lab](https://universal-verification-methodology.github.io/learning/tools/commit-message-lab/) → [git-log-lab](https://universal-verification-methodology.github.io/learning/tools/git-log-lab/) → [git-undo-safe](https://universal-verification-methodology.github.io/learning/tools/git-undo-safe/) → [git-stash-lab](https://universal-verification-methodology.github.io/learning/tools/git-stash-lab/) → [git-tags-lab](https://universal-verification-methodology.github.io/learning/tools/git-tags-lab/) → [branch-strategy](https://universal-verification-methodology.github.io/learning/tools/branch-strategy/) → [git-conflicts](https://universal-verification-methodology.github.io/learning/tools/git-conflicts/) → [git-rebase-merge](https://universal-verification-methodology.github.io/learning/tools/git-rebase-merge/) → [git-cherry-pick-lab](https://universal-verification-methodology.github.io/learning/tools/git-cherry-pick-lab/) → [git-reflog](https://universal-verification-methodology.github.io/learning/tools/git-reflog/) → [blame-bisect](https://universal-verification-methodology.github.io/learning/tools/blame-bisect/) → [remotes](https://universal-verification-methodology.github.io/learning/tools/remotes/) → [remote-tracking](https://universal-verification-methodology.github.io/learning/tools/remote-tracking/) → [pr-review-lab](https://universal-verification-methodology.github.io/learning/tools/pr-review-lab/) → [submodule-pitfalls](https://universal-verification-methodology.github.io/learning/tools/submodule-pitfalls/) → [template-clone](https://universal-verification-methodology.github.io/learning/tools/template-clone/) → [submission-repro](https://universal-verification-methodology.github.io/learning/tools/submission-repro/). All browser labs for this course are **shipped**. Module 21 is offline (`unix-git-practice`). See [all tools](https://universal-verification-methodology.github.io/learning/tools/) and each module README.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](LICENSE).

Example trees were adapted from [`this course`](https://github.com/universal-verification-methodology/this course) (M6–8). Platform tools and the parent monorepo may carry additional notices.
