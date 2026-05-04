# Feedback Insights Agent Guide

Project-local instructions for Codex and any repo-local agent workflow.

## Project Goal

Build a local Feedback Insights app for the Intryc AI take-home.

- Frontend: React, TypeScript, Vite
- Backend: FastAPI, Python
- Database: SQLite
- LLM provider: OpenAI API
- Stretch: small eval harness for the extraction prompt
- Scope: local only, no auth, no deployment, no Docker unless later needed

## Architecture

- `backend/app/main.py` owns the FastAPI app and route wiring.
- `backend/app/db.py` owns SQLite connection and persistence helpers.
- `backend/app/models.py` owns database models or row-shape definitions.
- `backend/app/schemas.py` owns API request and response schemas.
- `backend/app/services.py` owns application orchestration.
- `backend/app/llm.py` owns OpenAI API interaction.
- `backend/app/extraction_prompt.py` owns prompt text and extraction schema guidance.
- `backend/app/batch_parser.py` owns batch feedback parsing.
- `backend/app/dashboard.py` owns dashboard aggregation logic.
- `frontend/src/api.ts` owns HTTP calls.
- `frontend/src/types.ts` owns shared frontend types.
- `frontend/src/components/` owns focused UI components.
- `backend/evals/` owns prompt regression data and eval scripts.
- `harness/` documents repo-local agent workflows only.

## Implementation Rules

- Keep the first implementation as a thin vertical slice.
- Prefer simple functions and explicit names over abstractions.
- Keep backend logic testable without running the server.
- Keep frontend components small and data-driven.
- Do not introduce auth, deployment, Docker, or external services beyond OpenAI unless requested.
- Do not create global Codex, Claude, or editor configuration.
- Keep generated logs and planning artifacts project-local.

## Verification Commands

Use the narrowest command that validates the change.

Planned backend checks:

```powershell
python -m pytest backend/tests
```

Planned backend run command:

```powershell
uvicorn backend.app.main:app --reload
```

Planned frontend checks:

```powershell
npm run build --prefix frontend
```

Planned frontend run command:

```powershell
npm run dev --prefix frontend
```

Planned eval command:

```powershell
python backend/evals/run_eval.py
```

Do not run package installs until dependencies are intentionally added.

## Swarm Coordination

Use subagents only when work is separable.

- Orchestrator: keeps scope, plan, and integration order clear.
- Backend builder: owns `backend/app/` and backend tests.
- Frontend builder: owns `frontend/src/` and frontend config.
- Extraction eval agent: owns `backend/evals/` and prompt regression checks.
- Review agent: checks correctness, missing tests, and scope drift.

When multiple agents edit code, each agent must have explicit file ownership. Agents must not rewrite files owned by another agent without coordination.

## Progress Tracking

- Update `PLAN.md` when phase scope changes.
- Update `PROGRESS.md` after meaningful milestones.
- Update `TODO.md` when next steps change.
- Update `LOGS.md` with debugging notes, failed commands, and important decisions.
- Keep `NOTES.md` as draft structure for final submission notes until the app is complete.
