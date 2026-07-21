# Practice sandbox & browser labs

[![Sandbox](https://img.shields.io/badge/sandbox-unix--git--practice-orange)](https://github.com/universal-verification-methodology/unix-git-practice)
[![Shared IP](https://img.shields.io/badge/submodule-unix--git--shared--ip-blue)](https://github.com/universal-verification-methodology/unix-git-shared-ip)
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
| [unix-git-practice](https://github.com/universal-verification-methodology/unix-git-practice) | Student **template** — Use this template, Make, PR |
| [unix-git-shared-ip](https://github.com/universal-verification-methodology/unix-git-shared-ip) | Shared library **submodule** at `external/shared-ip` |

```bash
# Writable copy: on GitHub click “Use this template”, then:
git clone --recurse-submodules https://github.com/<YOU>/unix-git-practice.git
cd unix-git-practice
make test
bash scripts/check_ready.sh
```

Explore-only clone of the org template:

```bash
git clone --recurse-submodules \
  https://github.com/universal-verification-methodology/unix-git-practice.git
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
