# Learning State

Last updated: 2026-09-19

## Current Stage

- Curriculum: Week 0, environment preparation.
- Current task: decide whether to perform the first real push to GitHub.
- Next curriculum task after the push decision: publish the committed baseline only after explicit approval, then verify the remote branch.
- The dependency-manager choice is deferred to Week 2, after the student has learned the relevant concepts from the textbook.
- The textbook supports Weeks 1–4 in depth and selected material from Weeks 5 and 17–19; it is not restricted to Weeks 1–4.

## Completed and Verified

- Created a Git repository in this directory on the `master` branch.
- Created the first commit: `99b0ce5 chore: инициализация учебного проекта`.
- Verified that the working tree was clean immediately after that commit.
- Configured Git to display non-ASCII file names in readable form for this repository: `core.quotepath=false`.
- Configured the user's Git author identity on this PC as `Nevski47` with the email supplied by the user.
- Created `.gitattributes` to store text files in Git with LF line endings, so the history remains consistent across both Windows PCs.
- Created the directories `app/`, `tests/`, `evals/`, `docs/`, and `scripts/`.
- Created and activated `.venv` using Python's built-in `venv` module.
- Verified that the active interpreter is `.venv\Scripts\python.exe`.
- Created `.gitignore` that excludes virtual environments, Python bytecode, tool caches, and `.env` secrets while allowing `.env.example`.
- Configured the `origin` remote as `https://github.com/Nevski47/Project-AI.git`.
- Verified GitHub reachability with `git ls-remote origin` and exit code `0`; the remote repository is currently empty.
- Verified with `git push --dry-run origin master` that GitHub accepts the current credentials and would create the remote `master` branch; no data was uploaded.
- Created the transfer documents: `README.md`, `AGENTS.md`, this file, and `docs/DECISIONS.md`.
- Strengthened `AGENTS.md` with explicit pedagogical-integrity rules: evidence before completion, no automatic agreement, no premature solutions, and clear separation of facts from assumptions.

## Current PC Capabilities

| Capability | Status | Notes |
| --- | --- | --- |
| Python | Ready | Python 3.13.15 |
| Git | Ready | Git 2.55.0.windows.5 |
| Virtual environment | Ready | `.venv` is created |
| WSL2 | Unavailable | Installation requires administrator rights |
| Docker CLI | Installed | Docker 29.8.0 client is available |
| Docker Engine | Unavailable | Docker Desktop cannot start because virtualization support is not detected |

## Constraints

- The student works from two PCs. One has administrator rights; the current one does not.
- Do not require WSL or Docker for Week 0 or Week 1 Python work.
- Docker Desktop needs IT or system-administrator action to enable virtualization; do not attempt a workaround.
- Work through practical tasks one step at a time. Do not advance until the student provides a result and it is reviewed.
- Explain each step in Russian in enough detail to support learning.

## Current Repository Contents

- `Исправленный план обучения AI-инженерии на 52 недели.md` - source curriculum.
- `.gitignore` - local-file exclusion rules.
- `README.md` - project entry point.
- `AGENTS.md` - AI agent contract.
- `docs/HANDOFF.md` - concise transfer packet and first-response instructions for the next AI teaching agent.
- `docs/DECISIONS.md` - documented decisions.
- Project folders are empty; no application code, dependencies, `pyproject.toml`, tests, or lock file exist yet.

## GitHub Status

- The user has a GitHub profile: `Nevski47`.
- This local repository has `origin` configured as `https://github.com/Nevski47/Project-AI.git`.
- Read-only access to the remote is verified; push authentication and permission still require a separate dry-run check.

## Update Rules

After each verified learning step, update:

- the current task and next task;
- completed items;
- relevant environment changes or blockers;
- any decision that changes project direction.

Do not store secrets in this document.
