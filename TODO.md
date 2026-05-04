# TODO

## Orchestrator

- Finish Phase 1 doc refinement.
- Confirm the repo has no global Codex or Claude runtime folders.
- Create the first backend implementation prompt with explicit file ownership.
- During fan-in, update `PROGRESS.md`, `LOGS.md`, and this file from specialist reports.

## Backend Builder

- Add backend dependencies when Phase 2 starts.
- Implement batch parsing and tests first.
- Define request and response schemas.
- Implement SQLite setup and persistence.
- Implement `POST /feedback`, `GET /dashboard`, and `GET /health`.
- Add tests for parsing, schema validation, persistence, and dashboard aggregation.

## Frontend Builder

- Add frontend dependencies when Phase 3 starts.
- Implement the Vite React app shell.
- Build feedback input and status states.
- Build dashboard views for themes, sentiment distribution, trend, and feedback list.
- Connect `frontend/src/api.ts` to backend routes.
- Verify the frontend build.

## Eval Agent

- Expand `backend/evals/golden_feedback.json` with realistic examples.
- Implement `backend/evals/run_eval.py`.
- Score required fields, sentiment labels, themes, and action items.
- Record findings in `backend/evals/eval_report.md`.
- Report prompt/schema recommendations without editing shared docs during fan-out.

## Review Agent

- Review after fan-in.
- Check correctness, missing tests, secret handling, and stale docs.
- Verify local setup instructions once implementation exists.
- Lead with findings and only make scoped fixes if assigned.
