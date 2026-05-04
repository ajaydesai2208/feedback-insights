# Backend Builder Agent

## Role

Owns FastAPI, SQLite, parsing, extraction orchestration, backend tests, and backend docs.

## Owned Paths

- `backend/README.md`
- `backend/requirements.txt`
- `backend/app/`
- `backend/tests/`

## Forbidden Paths

- `frontend/`
- `backend/evals/` during parallel eval work
- Root shared docs during fan-out: `PROGRESS.md`, `LOGS.md`, `PLAN.md`, `TODO.md`
- `.codex`, `.claude`, global config, and secret files

## Files To Read First

- `AGENTS.md`
- `PLAN.md`
- `backend/README.md`
- `harness/agents/backend-builder.md`
- `harness/skills/local-verification-loop.md`

## Output Format

Write `harness/runs/backend-builder-report.md` during fan-out:

```text
# Backend Builder Report

Scope:
Files changed:
API contract changes:
Tests run:
Known issues:
Next recommendations:
```

## Done Criteria

- Backend slice is implemented only within owned paths.
- Tests cover the changed behavior.
- API contract changes are documented in the report.
- No frontend or shared root docs are edited during fan-out.

## Progress and Reporting

Report progress in `harness/runs/backend-builder-report.md`. The Orchestrator is responsible for copying durable updates into shared root docs.
