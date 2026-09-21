# AI Engineering Learning Project

This repository is a long-lived practical project for the 52-week AI Engineering learning plan.
It starts with a JSON validation CLI and will evolve into an AI-enabled backend service.

The curriculum source is [Исправленный план обучения AI-инженерии на 52 недели.md](<Исправленный план обучения AI-инженерии на 52 недели.md>).

## Project Structure

- `app/` - application source code.
- `tests/` - automated tests.
- `evals/` - AI evaluation cases and runners.
- `docs/` - learning state, decisions, and technical documentation.
- `scripts/` - helper scripts.
- `AGENTS.md` - mandatory instructions for AI agents working in this repository.

## Start Here

Before making any change, an AI agent must read these files in order:

1. `docs/HANDOFF.md`
2. `AGENTS.md`
3. `docs/LEARNING_STATE.md`
4. `docs/DECISIONS.md`
5. this file

The agent must continue from the current learning step, not jump ahead. The student completes one step before the next is given.

## Local Environment

Python 3.13 is used through a local virtual environment.

Activate it in PowerShell from the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
```

The project does not yet have external dependencies, a package manager configuration, tests, linting, or type checking. Those tools will be added when they are deliberately introduced in the curriculum.

## Current Prototype

`app/main.py` is an introductory JSON-processing prototype. It reads `Members.json` from the repository root, validates employee fields `id`, `firstName`, and `lastName`, skips invalid employee records, and prints a cleaned result without `salary`.

Run it from the repository root:

```powershell
.\.venv\Scripts\python.exe .\app\main.py
```

The current prototype is intentionally limited: it has no command-line file argument, automated tests, or handling for malformed JSON. These are future learning tasks.

## Repository Status

The current practical stage is Week 1, Python and a first JSON-validation prototype. The detailed and authoritative progress record is in `docs/LEARNING_STATE.md`.
