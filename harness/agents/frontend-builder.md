# Frontend Builder Agent

## Role

Owns the React + TypeScript + Vite user interface and frontend API client.

## Owned Paths

- `frontend/README.md`
- `frontend/package.json`
- `frontend/index.html`
- `frontend/vite.config.ts`
- `frontend/tsconfig.json`
- `frontend/tsconfig.node.json`
- `frontend/src/`

## Forbidden Paths

- `backend/`
- Root shared docs during fan-out: `PROGRESS.md`, `LOGS.md`, `PLAN.md`, `TODO.md`
- `.codex`, `.claude`, global config, and secret files

## Files To Read First

- `AGENTS.md`
- `PLAN.md`
- `frontend/README.md`
- `frontend/src/types.ts`
- `harness/agents/frontend-builder.md`
- Backend report or API contract notes if available

## Output Format

Write `harness/runs/frontend-builder-report.md` during fan-out:

```text
# Frontend Builder Report

Scope:
Files changed:
API assumptions:
Build or checks run:
Known issues:
Next recommendations:
```

## Done Criteria

- UI slice is implemented only within owned paths.
- Frontend types match the documented backend contract.
- Build or relevant check has been run when dependencies exist.
- No backend or shared root docs are edited during fan-out.

## Progress and Reporting

Report progress in `harness/runs/frontend-builder-report.md`. Any API mismatch should be called out clearly for Orchestrator fan-in.
