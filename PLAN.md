# Build Plan

## Phase 1: Harness and Architecture

- Create project-local `AGENTS.md`, planning docs, and `harness/`.
- Define file ownership, fan-out/fan-in rules, and reporting paths.
- Keep global Codex runtime files out of the repo.

Status: complete.

## Phase 2: Backend Vertical Slice

- Implement batch parsing, schemas, SQLite persistence, FastAPI routes, OpenAI wrapper, and dashboard aggregation.
- Add focused backend tests.

Status: complete.

## Phase 3: Frontend Vertical Slice

- Implement the Vite React app shell, feedback input, status states, dashboard views, searchable table, and typed API client.
- Verify frontend build.

Status: complete.

## Phase 4: Eval Harness

- Add golden examples, eval runner, and eval report.
- Reuse the app extraction prompt and schema to avoid drift.

Status: complete.

## Phase 5: Fan-In Integration

- Reconcile backend/frontend API contracts.
- Fold specialist reports into shared project docs.
- Resolve integration issues without expanding scope.

Status: complete.

## Phase 6: Verification and Final Review

- Run backend tests, frontend build, provider-backed smoke, eval harness, browser dry run, and security review.
- Improve local setup with root `.env` loading.
- Fix browser dry-run reliability issue by tightening SQLite connection ownership.
- Finalize submission docs.

Status: complete.
