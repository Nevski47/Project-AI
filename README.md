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

1. `AGENTS.md`
2. `docs/LEARNING_STATE.md`
3. `docs/DECISIONS.md`
4. this file

The agent must continue from the current learning step, not jump ahead. The student completes one step before the next is given.

## Local Environment

Python 3.13 is used through a local virtual environment.

Activate it in PowerShell from the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
```

The project does not yet have dependencies, a package manager configuration, or runnable code. Commands for installation, tests, linting, and type checking will be added when those tools are deliberately introduced.

## Repository Status

The current practical stage is Week 0, environment preparation. The detailed and authoritative progress record is in `docs/LEARNING_STATE.md`.
