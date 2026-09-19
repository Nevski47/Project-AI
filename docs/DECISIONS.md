# Decision Log

This file contains concise Architecture Decision Records (ADRs) and learning-process decisions. Add a new record before changing an established architectural choice.

## ADR-001: One Long-Lived Repository

- Status: accepted
- Date: 2026-09-19
- Context: the 52-week plan requires one main project rather than a new repository for each technology.
- Decision: this repository will evolve from the Week 1 JSON-validation CLI into the broader AI Engineering project.
- Consequence: code is added incrementally to the existing structure; unrelated experimental repositories are avoided.

## ADR-002: Python Standard Library Virtual Environment

- Status: accepted
- Date: 2026-09-19
- Context: the project needs an isolated Python environment before dependencies are chosen.
- Decision: use `.venv`, created with `py -m venv .venv`.
- Consequence: project libraries are isolated from the system Python. The virtual environment is not committed to Git.

## ADR-003: Development Must Work Without WSL and Docker Initially

- Status: accepted
- Date: 2026-09-19
- Context: the current Windows PC has no administrator rights, WSL is not installed, and Docker Desktop cannot start because virtualization support is unavailable.
- Decision: continue Week 0 and Week 1 with Python and Git. Use the administrator-enabled PC later for WSL and Docker work if necessary.
- Consequence: current Python exercises cannot depend on Linux-only commands or containers.

## ADR-004: Explicit AI-Agent Handoff Documents

- Status: accepted
- Date: 2026-09-19
- Context: the student may transfer teaching to another AI agent at any time.
- Decision: maintain `AGENTS.md`, `docs/LEARNING_STATE.md`, and this decision log as the minimum transfer packet.
- Consequence: a new agent can recover the project context without relying on chat history and must preserve the one-step learning workflow.

## ADR-005: AGENTS.md Is the Single Source of Agent Rules

- Status: accepted
- Date: 2026-09-19
- Context: the project needs durable teaching rules such as one-step progression, evidence-based review, and no premature solutions.
- Decision: keep these rules in `AGENTS.md` rather than duplicate them in a separate `RULES.md` or `memory-bank/` file.
- Consequence: every new agent has one authoritative rules file to read, reducing the chance of contradictory instructions.

## ADR-006: Repository-Level Teaching Handoff

- Status: accepted
- Date: 2026-09-19
- Context: teaching may move between AI agents, and chat history is not a reliable project record.
- Decision: maintain `docs/HANDOFF.md` as a concise current transfer packet, supported by `AGENTS.md`, `docs/LEARNING_STATE.md`, and this decision log.
- Consequence: a new agent can identify the exact next verified task and the teaching constraints without consuming the prior conversation context.
