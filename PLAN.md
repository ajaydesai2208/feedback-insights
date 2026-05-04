# Build Plan

## Phase 1: Harness and Architecture

- Refine project-local `AGENTS.md`, planning docs, and `harness/`.
- Define file ownership, fan-out/fan-in rules, and reporting paths.
- Keep backend and frontend app logic as placeholders.
- Confirm no global Codex or Claude runtime files are committed.

Exit criteria:

- Root docs explain scope, workflow, and next steps.
- Harness docs are usable as reusable Codex prompts and role guides.

## Phase 2: Backend Vertical Slice

- Add backend dependencies intentionally.
- Implement batch parsing for pasted feedback.
- Define API schemas and extraction result shapes.
- Add SQLite schema setup and persistence helpers.
- Implement `POST /feedback`, `GET /dashboard`, and `GET /health`.
- Add focused backend tests for parsing, validation, persistence, and dashboard aggregation.

Exit criteria:

- Backend tests pass.
- Backend can ingest feedback and return dashboard data locally.

## Phase 3: Frontend Vertical Slice

- Add frontend dependencies intentionally.
- Implement Vite React shell.
- Build feedback input, status states, dashboard cards/charts, and searchable table.
- Connect to backend API contract.
- Keep UI local-only and simple.

Exit criteria:

- Frontend build passes.
- User can paste feedback and inspect extracted dashboard data through the UI.

## Phase 4: Eval Harness

- Add representative golden feedback examples.
- Implement eval runner for extraction prompt behavior.
- Track required fields, sentiment validity, theme quality, and action item extraction.
- Record results in `backend/evals/eval_report.md`.

Exit criteria:

- Eval command runs locally.
- Report describes current prompt strengths, failures, and next prompt adjustments.

## Phase 5: Fan-In Integration

- Merge specialist work into one coherent branch.
- Reconcile API and frontend type contracts.
- Fold specialist reports from `harness/runs/` into `PROGRESS.md`, `LOGS.md`, and `TODO.md`.
- Fix integration issues without expanding scope.

Exit criteria:

- Backend, frontend, and eval paths agree on shared contracts.
- Shared docs reflect the current state.

## Phase 6: Final Review and Docs

- Run backend tests, frontend build, and eval harness.
- Review for take-home fit, secret handling, local setup clarity, and scope creep.
- Finalize README setup instructions.
- Write `NOTES.md` under 500 words.

Exit criteria:

- Verification results are recorded.
- Final notes and README are ready for submission.
