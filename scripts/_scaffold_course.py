#!/usr/bin/env python3
"""Scaffold courses/learn_git from syllabus (lab-driven + dual tracks)."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # courses/learn_git
COURSES = ROOT.parent
SRC = COURSES / "learn_unix_git"
DST = ROOT

LAB_BASE_LOCAL = "http://127.0.0.1:8080/tools"
LAB_BASE_LIVE = "https://universal-verification-methodology.github.io/learning/tools"
SANDBOX_URL = "https://github.com/universal-verification-methodology/unix-git-practice"
SHARED_IP_URL = "https://github.com/universal-verification-methodology/unix-git-shared-ip"

# (num, slug, kind, title, lab_id|None, status, source_example_dirs relative to learn_unix_git)
MODULES = [
    (0, "intro", "intro", "Welcome to Git for coursework", None, None, []),
    (1, "git-mental-model", "lab", "Git mental model", "git-mental-model", "S",
     ["module6/examples/concepts"]),
    (2, "git-graph", "lab", "Graph, stage, commit (playground)", "git-graph", "S",
     ["module6/examples/init_clone", "module6/examples/status_diff", "module6/examples/add_commit_log"]),
    (3, "gitignore-lab", "lab", ".gitignore patterns", "gitignore-lab", "S",
     ["module6/examples/gitignore"]),
    (4, "commit-message-lab", "lab", "Commit messages", "commit-message-lab", "S",
     ["module6/examples/add_commit_log"]),
    (5, "git-log-lab", "lab", "git log options", "git-log-lab", "S",
     ["module6/examples/log_options"]),
    (6, "git-undo-safe", "lab", "Safe undo", "git-undo-safe", "S",
     ["module6/examples/remote_undo"]),
    (7, "git-stash-lab", "lab", "Stash scenarios", "git-stash-lab", "S",
     ["module6/examples/stash"]),
    (8, "git-tags-lab", "lab", "Tags", "git-tags-lab", "S",
     ["module6/examples/tags"]),
    (9, "branch-strategy", "lab", "Branch naming", "branch-strategy", "S",
     ["module6/examples/branch_rename", "module7/examples/branching", "module7/examples/team_workflow"]),
    (10, "git-conflicts", "lab", "Merge conflicts", "git-conflicts", "S",
     ["module7/examples/conflicts", "module7/examples/merging"]),
    (11, "git-rebase-merge", "lab", "Rebase vs merge", "git-rebase-merge", "S",
     ["module7/examples/rebase", "module7/examples/merging"]),
    (12, "git-cherry-pick-lab", "lab", "Cherry-pick", "git-cherry-pick-lab", "S",
     ["module7/examples/cherry_pick"]),
    (13, "git-reflog", "lab", "Reflog recovery", "git-reflog", "S",
     ["module7/examples/reflog"]),
    (14, "blame-bisect", "lab", "Blame & bisect", "blame-bisect", "S",
     ["module7/examples/blame_bisect"]),
    (15, "remotes", "lab", "Remotes, PRs & submodules (concepts)", "remotes", "S",
     ["module7/examples/team_workflow", "module7/examples/submodules"]),
    (16, "remote-tracking", "lab", "Remote-tracking branches", "remote-tracking", "S",
     ["module7/examples/remote_branch"]),
    (17, "pr-review-lab", "lab", "PR review checklist", "pr-review-lab", "S",
     ["module7/examples/team_workflow"]),
    (18, "submodule-pitfalls", "lab", "Submodule pitfalls", "submodule-pitfalls", "S",
     ["module7/examples/submodules"]),
    (19, "template-clone", "lab", "Template-repo bootstrap", "template-clone", "S",
     ["module8/examples/template"]),
    (20, "submission-repro", "lab", "Submission reproducibility", "submission-repro", "S",
     ["module8/examples/submission", "module8/examples/end_to_end", "module8/examples/iterative"]),
    (21, "sandbox", "offline", "Live sandbox: clone → Make → PR", "unix-git-practice", None,
     ["module8/examples/end_to_end"]),
    (22, "wrap", "wrap", "Git path complete", None, None, []),
]


def mod_dir(num: int, slug: str) -> Path:
    return DST / f"module{num:02d}-{slug}"


def lab_urls(lab_id: str) -> tuple[str, str]:
    return (f"{LAB_BASE_LOCAL}/{lab_id}/index.html", f"{LAB_BASE_LIVE}/{lab_id}/")


def write_module_readme(
    num: int, slug: str, kind: str, title: str, lab_id: str | None, status: str | None
) -> None:
    d = mod_dir(num, slug)
    d.mkdir(parents=True, exist_ok=True)
    nn = f"{num:02d}"
    prev = next((m for m in MODULES if m[0] == num - 1), None)
    nxt = next((m for m in MODULES if m[0] == num + 1), None)

    nav = []
    if prev:
        nav.append(f"[← {prev[3]}](../module{prev[0]:02d}-{prev[1]}/README.md)")
    else:
        nav.append("← Start")
    nav.append("[Course README](../README.md)")
    if nxt:
        nav.append(f"[{nxt[3]} →](../module{nxt[0]:02d}-{nxt[1]}/README.md)")
    else:
        nav.append("End →")
    nav_line = " · ".join(nav)

    if kind == "intro":
        body = f"""# Module {nn}: {title}

**Kind:** `intro` · Dual-track course welcome

{nav_line}

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
3. Or use the live site: {LAB_BASE_LIVE}/

## How to move through modules

1. Read the module **README** (outcomes).
2. Pick a track (or both).
3. Check off **CHECKLIST.md**.
4. Optional: skim `outline.yaml` / `transcript.md` for upcoming slides & clips.

## Media (planned)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript stub | [transcript.md](transcript.md) |
| Slides / video | generate later with **module-slides** |

## Next

→ [Module 01: Git mental model](../module01-git-mental-model/README.md)
"""
    elif kind == "wrap":
        body = f"""# Module {nn}: {title}

**Kind:** `wrap`

{nav_line}

## You can now

- Explain the Git mental model (working tree → index → commit graph)
- Stage, commit, inspect history, and undo safely
- Branch, merge/rebase, and recover with reflog
- Use remotes, PR basics, and (when needed) submodules
- Bootstrap from a template and rehearse a reproducible submission

## Dual-track recap

If you mainly used **browser labs**, spend a short session on Track A for modules 02, 06, 10, and 15–21 so remotes and conflict resolution feel natural.  
If you mainly used **real Git**, skim any skipped browser labs for visual challenges.

## Next course

→ **learn_digital** or **learn_verilog** (syllabus ladder: [../../syllabus.md](../../syllabus.md#suggested-learning-ladder))  
Unix fluency: [`../learn_unix/`](../learn_unix/). Legacy combined path: [`../learn_unix_git/`](../learn_unix_git/).

## Checklist

- [ ] I completed Track A and/or Track B for the lab modules I care about
- [ ] I can stage, commit, and read `git log` / `git status` without guessing
- [ ] I have practiced at least once on [{SANDBOX_URL.split('/')[-1]}]({SANDBOX_URL}) (or my own fork)
"""
    elif kind == "offline":
        body = f"""# Module {nn}: {title}

**Kind:** `offline` · Activity: `{lab_id}` (live GitHub sandbox)

{nav_line}

## Outcomes

After this module you can **clone → Make → PR** on a real GitHub template without touching the curriculum tree.

## Practice surface (Track A only)

This module has **no browser lab**. Use the org sandbox:

1. Read [SANDBOX.md](../SANDBOX.md).
2. On GitHub: [unix-git-practice]({SANDBOX_URL}) → **Use this template**.
3. Clone with submodules, run `make test`, then open a practice PR on *your* fork.
4. Optional shared-IP pin: [{SHARED_IP_URL}]({SHARED_IP_URL}).

```bash
git clone --recurse-submodules https://github.com/<YOU>/unix-git-practice.git
cd unix-git-practice
make test
bash scripts/check_ready.sh
```

Explore-only (no push):

```bash
git clone --recurse-submodules \\
  {SANDBOX_URL}.git
```

## Track B

None — use earlier remotes / conflicts / blame labs if you need concept refreshers.

## Media (planned)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript stub | [transcript.md](transcript.md) |
| Slides / video | screen-capture of real toolchain (module-slides) |

## Files

```
module{nn}-{slug}/
├── README.md
├── CHECKLIST.md
├── EXAMPLES.md
├── outline.yaml
├── transcript.md
└── examples/       # local rehearsal notes (Track A)
```
"""
    else:
        assert lab_id and status
        local, live = lab_urls(lab_id)
        status_note = (
            "Shipped"
            if status == "S"
            else "Planned (Coming soon on tools index — use Track A until it ships)"
        )
        body = f"""# Module {nn}: {title}

**Kind:** `lab` · Primary lab: `{lab_id}` · **{status_note}**

{nav_line}

## Outcomes

After this module you can explain and practice the ideas taught by **`{lab_id}`**, in the browser and/or with real Git.

## Two tracks (pick one or both)

### Track A — Real Git (hands-on)

Work in a local practice repo using this module’s `examples/` (adapted from `learn_unix_git`).

1. Open [EXAMPLES.md](EXAMPLES.md) and run the “Try these” commands.
2. Complete [CHECKLIST.md](CHECKLIST.md) in `~/unix_practice/git_demo` (or your sandbox clone).
3. Optional self-check: `./scripts/module.sh {nn} --check` (from course root).

### Track B — Browser lab (online)

1. Local: [{local}]({local})
2. Live: [{live}]({live})
3. Load the **starter example**, then work challenges.
4. Check off the Track B items in [CHECKLIST.md](CHECKLIST.md).

> Concept labs are literacy tools — they do not replace real Git for remotes, PRs, and submissions.

## Media (planned)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript stub | [transcript.md](transcript.md) |
| Slides / video | generate later with **module-slides** |

## Files

```
module{nn}-{slug}/
├── README.md       # this file
├── CHECKLIST.md    # Track A + Track B checkboxes
├── EXAMPLES.md     # real-Git example index
├── outline.yaml    # slide / clip outline
├── transcript.md   # speakable stub
└── examples/       # hands-on trees (Track A)
```
"""
    (d / "README.md").write_text(body, encoding="utf-8")


def write_checklist(num: int, slug: str, kind: str, title: str, lab_id: str | None) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind == "intro":
        text = f"""# Module {nn} checklist — {title}

## Setup

- [ ] Terminal available (Linux / macOS / WSL2)
- [ ] `git --version` works
- [ ] Opened this repo at `courses/learn_git`
- [ ] Ran `./scripts/scaffold.sh` (or created `~/unix_practice/git_demo` yourself)
- [ ] Skimmed [SANDBOX.md](../SANDBOX.md) once
- [ ] Opened the [tools index]({LAB_BASE_LOCAL}/index.html) once (or live site)

## Mindset

- [ ] I understand Track A = real Git, Track B = browser lab
- [ ] I know I can do either track, or both
"""
    elif kind == "wrap":
        text = f"""# Module {nn} checklist — {title}

- [ ] Reviewed outcomes in [README.md](README.md)
- [ ] Ready for **learn_digital** / **learn_verilog** (or continue practicing weak modules)
"""
    elif kind == "offline":
        text = f"""# Module {nn} checklist — {title}

## Live sandbox (`{lab_id}`)

- [ ] Created a personal repo from the [unix-git-practice]({SANDBOX_URL}) template (or used explore-only clone)
- [ ] Cloned with `--recurse-submodules`
- [ ] Ran `make test` (or equivalent) successfully
- [ ] Opened a practice PR **on my fork** (optional if explore-only)
- [ ] Did **not** push student work into the curriculum course tree

## Done when

- [ ] I can describe clone → Make → PR without looking it up
"""
    else:
        text = f"""# Module {nn} checklist — {title}

## Track A — Real Git

- [ ] Worked through at least one example under `examples/` (see [EXAMPLES.md](EXAMPLES.md))
- [ ] Repeated the key commands in `~/unix_practice/git_demo` (or sandbox clone)
- [ ] Can explain the outcome in my own words

## Track B — Browser lab (`{lab_id}`)

- [ ] Opened the lab (local or live)
- [ ] Loaded the starter example
- [ ] Completed a few challenges (or noted the lab is still Coming soon)

## Done when

- [ ] I can do the task with real Git **or** I finished the browser challenges (preferably both)
"""
    (d / "CHECKLIST.md").write_text(text, encoding="utf-8")


def write_examples_md(num: int, slug: str, kind: str, title: str, copied: list[str]) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind not in ("lab", "offline"):
        (d / "EXAMPLES.md").write_text(
            f"# Module {nn} — no Track A example trees\n\nThis is an `{kind}` module. See [README.md](README.md).\n",
            encoding="utf-8",
        )
        return
    lines = [
        f"# Module {nn} examples — {title}",
        "",
        "Track A (real Git). Each folder was adapted from `learn_unix_git`.",
        "",
    ]
    if not copied:
        lines.append(
            "_No example trees copied yet — use the browser lab (if any) and your own `~/unix_practice/git_demo`._"
        )
    else:
        for name in copied:
            lines += [
                f"## `{name}/`",
                "",
                f"See [`examples/{name}/README.md`](examples/{name}/README.md) if present.",
                "",
                "**Try:**",
                "",
                "```bash",
                f"cd module{nn}-{slug}/examples/{name}",
                "ls -la",
                "```",
                "",
            ]
    (d / "EXAMPLES.md").write_text("\n".join(lines), encoding="utf-8")


def write_outline_transcript(num: int, slug: str, kind: str, title: str, lab_id: str | None) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    outline = f"""# Module {nn} outline
title: "{title}"
kind: {kind}
lab: {lab_id or "null"}
slides:
  - Course context / why this matters for coursework & delivery
  - Core idea (1 concept)
  - Track B: show lab starter (if lab module)
  - Track A: one real-Git demo
  - Common pitfalls
  - Your turn + quiz prompt
duration_minutes: 8
"""
    (d / "outline.yaml").write_text(outline, encoding="utf-8")
    if kind == "offline":
        show_b = "No browser lab — this clip is a screen capture of the live sandbox."
        show_a = f"Demo clone → Make → PR on `{lab_id}` (see SANDBOX.md)."
    else:
        show_b = (
            f"Open the browser lab, `{lab_id}`. Load the starter. Point at the UI."
            if lab_id
            else "Point at the course map / tools index."
        )
        show_a = "In a real terminal, demonstrate one command sequence from `examples/` or `~/unix_practice/git_demo`."
    transcript = f"""# Module {nn} transcript — {title}

> Stub for voiceover / clip. Expand when recording (module-slides).

## Hook

In coursework and delivery you will live in Git. This module: **{title}**.

## Teach

(3–5 sentences on the concept.)

## Show Track B

{show_b}

## Show Track A

{show_a}

## Your turn

Complete the checklist for at least one track. Then take the short quiz.
"""
    (d / "transcript.md").write_text(transcript, encoding="utf-8")


def copy_examples(num: int, slug: str, sources: list[str]) -> list[str]:
    if not sources:
        return []
    dest_ex = mod_dir(num, slug) / "examples"
    dest_ex.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    for rel in sources:
        src = SRC / rel
        if not src.exists():
            print(f"  skip missing {rel}")
            continue
        name = src.name
        dst = dest_ex / name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        copied.append(name)
    (dest_ex / "README.md").write_text(
        "# Examples\n\nTrack A trees for this module. See ../EXAMPLES.md.\n",
        encoding="utf-8",
    )
    return copied


def write_docs_index() -> None:
    docs = DST / "docs"
    docs.mkdir(exist_ok=True)
    rows = []
    for num, slug, kind, title, lab_id, status, _ in MODULES:
        lab = f"`{lab_id}`" if lab_id else "—"
        st = status or "—"
        rows.append(
            f"| {num:02d} | `{kind}` | [{title}](../module{num:02d}-{slug}/README.md) | {lab} | {st} |"
        )
    text = f"""# learn_git — module index

Lab-driven syllabus (pass 3). Full product syllabus: [../../syllabus.md](../../syllabus.md#2-learn_git).

| # | Kind | Module | Lab | Status |
|---|------|--------|-----|--------|
{chr(10).join(rows)}

## Dual tracks

See [TWO_TRACKS.md](TWO_TRACKS.md). Sandbox: [../SANDBOX.md](../SANDBOX.md).
"""
    (docs / "MODULES.md").write_text(text, encoding="utf-8")
    (docs / "TWO_TRACKS.md").write_text(
        f"""# Two learning tracks

## Track A — Real Git

Practice with real Git (Linux, macOS, or **WSL2** on Windows).

- Examples live under each `moduleNN-*/examples/`
- Scaffold: `./scripts/scaffold.sh` → `~/unix_practice/git_demo/`
- Live remotes / PR: [unix-git-practice]({SANDBOX_URL}) — see [SANDBOX.md](../SANDBOX.md)
- Self-check: `./scripts/module.sh NN --check`

Use this track when you need **fidelity**: real commits, remotes, conflicts, and submissions.

## Track B — Browser lab

Practice in the learning platform concept labs (no install).

- Local tools: {LAB_BASE_LOCAL}/
- Live: {LAB_BASE_LIVE}/
- Each lab module README links its primary lab id

Use this track for **intuition** and quick challenges. Planned labs show “Coming soon”; use Track A until they ship.

## Recommended path

1. **Track B** starter + a few challenges (5–10 min)
2. **Track A** examples + checklist (10–20 min)
3. Optional quiz / transcript review
4. Module 21 **offline** sandbox before wrap

Doing only one track is OK for self-study; later HDL/verification courses expect Track A comfort with remotes and PRs.
""",
        encoding="utf-8",
    )


def write_sandbox_md() -> None:
    text = f"""# Practice sandbox & browser labs

[![Sandbox](https://img.shields.io/badge/sandbox-unix--git--practice-orange)]({SANDBOX_URL})
[![Shared IP](https://img.shields.io/badge/submodule-unix--git--shared--ip-blue)]({SHARED_IP_URL})
[![Course](https://img.shields.io/badge/course-learn__git-0A9EDC)](README.md)

Course **examples** live in this repository. For **real GitHub remotes, pull requests, Make, and submodules**, use the org sandbox templates and (optionally) the companion browser platform.

## Why a separate sandbox?

| Surface | Safe for |
|---------|----------|
| **This repo (`learn_git`)** | Reading modules, local `examples/`, `module.sh` |
| **`unix-git-practice` template** | Student push, PR, submission rehearsal |
| **`unix-git-shared-ip`** | Submodule / shared-IP pin demos |
| **`platform/tools/`** | In-browser concept labs (no install) |

Pushing coursework into the curriculum tree would mix student noise with shared history. The template keeps those concerns apart.

## GitHub sandbox

| Repo | Role |
|------|------|
| [unix-git-practice]({SANDBOX_URL}) | Student **template** — Use this template, Make, PR |
| [unix-git-shared-ip]({SHARED_IP_URL}) | Shared library **submodule** at `external/shared-ip` |

```bash
# Writable copy: on GitHub click “Use this template”, then:
git clone --recurse-submodules https://github.com/<YOU>/unix-git-practice.git
cd unix-git-practice
make test
bash scripts/check_ready.sh
```

Explore-only clone of the org template:

```bash
git clone --recurse-submodules \\
  {SANDBOX_URL}.git
```

## Browser platform

If you have a checkout that includes `platform/`:

| Lab | Path |
|-----|------|
| Remotes / PR / submodule checklist | `platform/tools/remotes/` |
| Conflict resolver | `platform/tools/git-conflicts/` |
| Blame & bisect | `platform/tools/blame-bisect/` |
| All tools | `platform/tools/index.html` |

```bash
python -m http.server 8080 --directory platform
# → http://127.0.0.1:8080/tools/
```

## Where this fits

- Lab modules 01–20: examples + optional browser labs
- Module 21 (`offline`): full sandbox rehearsal
- Details also mirrored from legacy [`learn_unix_git/SANDBOX.md`](../learn_unix_git/SANDBOX.md)
"""
    (DST / "SANDBOX.md").write_text(text, encoding="utf-8")


def write_course_readme() -> None:
    landing_rows = []
    for num, slug, kind, title, lab_id, status, _ in MODULES:
        label = f"{num:02d} — {title}"
        landing_rows.append(f"| {label} | [module{num:02d}-{slug}](module{num:02d}-{slug}/README.md) |")

    lines = [
        "# learn_git",
        "",
        "[![GitHub](https://img.shields.io/badge/GitHub-learn__git-181717?logo=github)](https://github.com/universal-verification-methodology/learn_git)",
        "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](LICENSE)",
        "[![Role](https://img.shields.io/badge/role-Git%20submodule-orange)](https://github.com/universal-verification-methodology/learning)",
        "[![Parent](https://img.shields.io/badge/parent-learning%20monorepo-0A9EDC)](https://github.com/universal-verification-methodology/learning)",
        "[![Labs](https://img.shields.io/badge/labs-GitHub%20Pages-222?logo=githubpages)](https://universal-verification-methodology.github.io/learning/tools/)",
        "[![Domain](https://img.shields.io/badge/domain-Git%20%7C%20coursework%20%7C%20delivery-purple)](https://github.com/universal-verification-methodology/learn_git)",
        "",
        "**learn_git** is the open learning path for *Git for coursework through delivery*.",
        "",
        "Readers and students usually **open a module README** (or the live tools) or clone this public repo. Authors edit content here (or via the parent monorepo checkout), rebuild slides/audio with **module-slides** in the parent, and push; the parent repo only stores a pinned submodule commit.",
        "",
        "",
        "## Table of contents",
        "",
        "- [Contents](#contents)",
        "- [Browse or clone](#browse-or-clone)",
        "- [Consume from the parent](#consume-from-the-parent)",
        "- [Author: publish or update](#author-publish-or-update)",
        "- [Two learning tracks](#two-learning-tracks)",
        "- [Module landings](#module-landings)",
        "- [Browser labs](#browser-labs)",
        "- [License](#license)",
        "",
        "## Contents",
        "",
        "```text",
        "learn_git/",
        "├── README.md",
        "├── LICENSE              # CC BY 4.0",
        "├── SANDBOX.md           # unix-git-practice + shared-ip",
        "├── docs/",
        "│   ├── MODULES.md       # full module index (00–22)",
        "│   └── TWO_TRACKS.md    # Track A (real Git) vs Track B (browser)",
        "├── scripts/",
        "│   ├── scaffold.sh      # Track A practice repo",
        "│   └── module.sh        # per-module --check helpers",
        "├── module00-intro/",
        "├── module01-git-mental-model/",
        "│   ├── README.md",
        "│   ├── CHECKLIST.md",
        "│   ├── EXAMPLES.md",
        "│   ├── outline.yaml",
        "│   ├── transcript.md",
        "│   ├── examples/        # Track A",
        "│   └── (optional) slides.pptx / slides.pdf / video.mp4 / assets/",
        "├── …",
        "└── module22-wrap/",
        "```",
        "",
        "Videos and decks are optional per module. Generate with the **module-slides** skill (`.cursor/skills/module-slides/`) in the parent monorepo when ready.",
        "",
        "## Browse or clone",
        "",
        "- **Browser labs:** [https://universal-verification-methodology.github.io/learning/tools/](https://universal-verification-methodology.github.io/learning/tools/)",
        "- **Sandbox:** [SANDBOX.md](SANDBOX.md) · [unix-git-practice](" + SANDBOX_URL + ")",
        "- **Syllabus (parent):** [`syllabus.md` § learn_git](https://github.com/universal-verification-methodology/learning/blob/main/syllabus.md#2-learn_git)",
        "- **Clone this repo alone:**",
        "",
        "```bash",
        "git clone https://github.com/universal-verification-methodology/learn_git.git",
        "cd learn_git",
        "chmod +x scripts/*.sh",
        "./scripts/scaffold.sh          # Track A practice repo",
        "./scripts/module.sh 01 --check # optional env check for module 01",
        "```",
        "",
        "Then open [module00-intro/README.md](module00-intro/README.md).",
        "",
        "## Consume from the parent",
        "",
        "From a clone of the **learning** monorepo (lists this repo in `.gitmodules` when registered):",
        "",
        "```bash",
        "git clone --recurse-submodules \\",
        "  git@github.com:universal-verification-methodology/learning.git",
        "# or, if already cloned without submodules:",
        "git submodule update --init --recursive",
        "",
        "ls courses/learn_git",
        "```",
        "",
        "Working tree path in the parent: `courses/learn_git/` → this repository at a pinned commit.",
        "",
        "## Author: publish or update",
        "",
        "Edit inside the parent monorepo (recommended) or in a standalone clone of this repo.",
        "",
        "```bash",
        "# from the learning monorepo checkout",
        "cd courses/learn_git",
        "# … edit module README / CHECKLIST / EXAMPLES / transcript …",
        "",
        "# rebuild media from the parent (one module at a time):",
        "cd ../..",
        "# revise transcript.md, then:",
        "python .cursor/skills/module-slides/scripts/transcript_to_outline.py \\",
        "  courses/learn_git/moduleNN-slug",
        "bash .cursor/skills/module-slides/scripts/narrate_clips.sh \\",
        "  courses/learn_git/moduleNN-slug",
        "",
        "cd courses/learn_git",
        "git add -A",
        'git commit -m "Update learn_git modules"',
        "git push origin main",
        "```",
        "",
        "Then bump the pin in the **parent**:",
        "",
        "```bash",
        "cd /path/to/learning",
        "git add courses/learn_git",
        'git commit -m "Bump learn_git submodule"',
        "git push",
        "```",
        "",
        "See the skill `SKILL.md` for dual-track narration rules and the full PPTX → PDF → TTS → MP4 pipeline.",
        "",
        "## Two learning tracks",
        "",
        "Every **lab** module documents both tracks. Intro/wrap have no lab; module 21 is **offline** sandbox only. Details: [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md).",
        "",
        "| Track | Practice surface | Start here |",
        "|-------|------------------|------------|",
        "| **A — Real Git** | Local Git + `examples/` + sandbox | `./scripts/scaffold.sh` · [SANDBOX.md](SANDBOX.md) |",
        f"| **B — Browser lab** | Platform tools | [local tools]({LAB_BASE_LOCAL}/) · [live]({LAB_BASE_LIVE}/) |",
        "",
        "Recommended path: short Track B starter → Track A examples + checklist → module 21 sandbox → optional quiz / transcript review.",
        "",
        "## Module landings",
        "",
        "Full status table: **[docs/MODULES.md](docs/MODULES.md)**. Clusters: 00 intro · 01–08 model/commit/history · 09–14 branch/integrate/recover · 15–20 remotes/delivery · 21 sandbox · 22 wrap.",
        "",
        "| Module | Landing |",
        "|--------|---------|",
        *landing_rows,
        "",
        "## Browser labs",
        "",
        "By workflow (Track B): [git-mental-model](https://universal-verification-methodology.github.io/learning/tools/git-mental-model/) → [git-graph](https://universal-verification-methodology.github.io/learning/tools/git-graph/) → [gitignore-lab](https://universal-verification-methodology.github.io/learning/tools/gitignore-lab/) → [commit-message-lab](https://universal-verification-methodology.github.io/learning/tools/commit-message-lab/) → [git-log-lab](https://universal-verification-methodology.github.io/learning/tools/git-log-lab/) → [git-undo-safe](https://universal-verification-methodology.github.io/learning/tools/git-undo-safe/) → [git-stash-lab](https://universal-verification-methodology.github.io/learning/tools/git-stash-lab/) → [git-tags-lab](https://universal-verification-methodology.github.io/learning/tools/git-tags-lab/) → [branch-strategy](https://universal-verification-methodology.github.io/learning/tools/branch-strategy/) → [git-conflicts](https://universal-verification-methodology.github.io/learning/tools/git-conflicts/) → [git-rebase-merge](https://universal-verification-methodology.github.io/learning/tools/git-rebase-merge/) → [git-cherry-pick-lab](https://universal-verification-methodology.github.io/learning/tools/git-cherry-pick-lab/) → [git-reflog](https://universal-verification-methodology.github.io/learning/tools/git-reflog/) → [blame-bisect](https://universal-verification-methodology.github.io/learning/tools/blame-bisect/) → [remotes](https://universal-verification-methodology.github.io/learning/tools/remotes/) → [remote-tracking](https://universal-verification-methodology.github.io/learning/tools/remote-tracking/) → [pr-review-lab](https://universal-verification-methodology.github.io/learning/tools/pr-review-lab/) → [submodule-pitfalls](https://universal-verification-methodology.github.io/learning/tools/submodule-pitfalls/) → [template-clone](https://universal-verification-methodology.github.io/learning/tools/template-clone/) → [submission-repro](https://universal-verification-methodology.github.io/learning/tools/submission-repro/). All browser labs for this course are **shipped**. Module 21 is offline (`unix-git-practice`). See [all tools](https://universal-verification-methodology.github.io/learning/tools/) and each module README.",
        "",
        "## License",
        "",
        "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](LICENSE).",
        "",
        "Example trees were adapted from [`learn_unix_git`](https://github.com/universal-verification-methodology/learn_unix_git) (M6–8). Platform tools and the parent monorepo may carry additional notices.",
        "",
    ]
    (DST / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_scripts() -> None:
    scripts = DST / "scripts"
    scripts.mkdir(exist_ok=True)
    scaffold = r"""#!/usr/bin/env bash
# Create ~/unix_practice/git_demo for Track A Git exercises.
set -euo pipefail
BASE="${HOME}/unix_practice"
TARGET="${BASE}/git_demo"
mkdir -p "$BASE"
if [[ -d "$TARGET/.git" ]]; then
  echo "Already a Git repo: $TARGET"
else
  mkdir -p "$TARGET"
  (
    cd "$TARGET"
    git init -b main
    cat > README.md << 'EOF'
learn_git Track A practice repo
Use this directory for checklist exercises (not for curriculum PRs).
EOF
    cat > notes.md << 'EOF'
# Practice notes
EOF
    mkdir -p src tb build
    echo "placeholder" > build/output.tmp
    cat > .gitignore << 'EOF'
build/
*.log
*.tmp
EOF
    git add README.md notes.md .gitignore src tb
    git -c user.email="student@example.com" -c user.name="learn_git student" \
      commit -m "chore: initial practice repo"
  )
  echo "Created Git practice repo: $TARGET"
fi
ls -la "$TARGET"
git -C "$TARGET" status -sb || true
"""
    (scripts / "scaffold.sh").write_text(scaffold, encoding="utf-8")

    module_sh = r"""#!/usr/bin/env bash
# Generic module helper: ./scripts/module.sh NN [--check|--demo|--help]
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NN="${1:-}"
shift || true
if [[ -z "$NN" || "$NN" == "--help" ]]; then
  echo "Usage: $0 NN [--check|--demo|--help]"
  echo "  NN = module number, e.g. 01 or 1"
  exit 0
fi
NN="$(printf '%02d' "$((10#$NN))")"
MOD_DIR="$(find "$ROOT" -maxdepth 1 -type d -name "module${NN}-*" | head -1)"
if [[ -z "$MOD_DIR" ]]; then
  echo "No module directory for $NN"
  exit 1
fi
ACTION="${1:---check}"
case "$ACTION" in
  --check)
    echo "Module $NN self-check (Track A environment)"
    echo "Module dir: $MOD_DIR"
    command -v git >/dev/null && echo "[OK] git: $(git --version)" || echo "[FAIL] git missing"
    command -v bash >/dev/null && echo "[OK] bash"
    if [[ -d "$MOD_DIR/examples" ]]; then
      echo "[OK] examples present:"
      ls "$MOD_DIR/examples"
    else
      echo "[INFO] no examples/ (intro/wrap or pending)"
    fi
    if [[ -d "${HOME}/unix_practice/git_demo/.git" ]]; then
      echo "[OK] ~/unix_practice/git_demo is a Git repo"
    else
      echo "[INFO] run ./scripts/scaffold.sh to create ~/unix_practice/git_demo"
    fi
    ;;
  --demo)
    echo "Demo: open $MOD_DIR/EXAMPLES.md and README.md"
    echo "Browser lab link is in README (Track B), if any."
    echo "Sandbox: see $ROOT/SANDBOX.md"
    ;;
  *)
    echo "Unknown option: $ACTION"
    exit 1
    ;;
esac
"""
    (scripts / "module.sh").write_text(module_sh, encoding="utf-8")
    (scripts / "README.md").write_text(
        """# Scripts

| Script | Purpose |
|--------|---------|
| `scaffold.sh` | Create `~/unix_practice/git_demo` for Track A |
| `module.sh NN` | `--check` / `--demo` for module number `NN` |
| `_scaffold_course.py` | Regenerate course stubs from syllabus (authors) |

```bash
chmod +x scripts/*.sh
./scripts/scaffold.sh
./scripts/module.sh 01 --check
```
""",
        encoding="utf-8",
    )


def write_license() -> None:
    src = COURSES / "learn_unix" / "LICENSE"
    dst = DST / "LICENSE"
    if src.exists():
        text = src.read_text(encoding="utf-8").replace("learn_unix", "learn_git")
        dst.write_text(text, encoding="utf-8")
    else:
        dst.write_text(
            "Creative Commons Attribution 4.0 International (CC BY 4.0)\n\n"
            "Copyright (c) The learn_git contributors.\n\n"
            "https://creativecommons.org/licenses/by/4.0/\n",
            encoding="utf-8",
        )


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    write_license()
    write_course_readme()
    write_docs_index()
    write_sandbox_md()
    write_scripts()
    for num, slug, kind, title, lab_id, status, sources in MODULES:
        print(f"module{num:02d}-{slug} …")
        write_module_readme(num, slug, kind, title, lab_id, status)
        write_checklist(num, slug, kind, title, lab_id)
        copied = copy_examples(num, slug, sources) if kind in ("lab", "offline") else []
        write_examples_md(num, slug, kind, title, copied)
        write_outline_transcript(num, slug, kind, title, lab_id)
    print("Done:", DST)


if __name__ == "__main__":
    main()
