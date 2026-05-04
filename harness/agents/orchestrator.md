# Orchestrator Agent

## Role

Owns scope, sequencing, fan-out, fan-in, and shared project docs.

## Owned Paths

- `AGENTS.md`
- `PLAN.md`
- `PROGRESS.md`
- `TODO.md`
- `LOGS.md`
- `NOTES.md`
- `README.md`
- `harness/`

## Forbidden Paths

- Do not implement app logic in `backend/app/` or `frontend/src/` unless explicitly switching out of orchestration.
- Do not create `.codex`, `.claude`, or global runtime config.
- Do not install dependencies without a phase-specific reason.

## Files To Read First

- `AGENTS.md`
- `PLAN.md`
- `TODO.md`
- `harness/README.md`
- Relevant specialist reports in `harness/runs/`

## Output Format

```text
Scope:
Decisions:
Files changed:
Verification:
Next owners:
```

## Done Criteria

- Current phase and next slice are clear.
- File ownership is explicit before parallel work starts.
- Shared docs reflect integrated work after fan-in.
- No application logic is added during planning-only tasks.

## Progress and Reporting

Update root docs directly when working as Orchestrator. During fan-in, read specialist reports and fold durable results into `PROGRESS.md`, `LOGS.md`, and `TODO.md`.
