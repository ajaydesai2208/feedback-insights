# Progress

## 2026-05-04

### Structure

- Created the project-local file and folder structure for Feedback Insights.
- Added root docs, backend, frontend, eval, and harness placeholders.

### Harness

- Built the Codex-native project harness under `harness/`.
- Added role cards for Orchestrator, Backend Builder, Frontend Builder, Extraction Eval Agent, and Review Agent.
- Added reusable command prompts, project workflow playbooks, and `harness/runs/` reporting.

### Architecture

- Defined FastAPI + SQLite backend ownership.
- Defined React + TypeScript + Vite frontend ownership.
- Defined OpenAI extraction and eval harness contracts.
- Documented no-secret, no-global-config, and file ownership rules in `AGENTS.md`.

### Backend Swarm Branch

- Implemented backend parsing, schemas, SQLite persistence, FastAPI routes, OpenAI wrapper, dashboard aggregation, and backend tests.
- Added backend run/test documentation.

### Frontend Swarm Branch

- Implemented Vite React UI, feedback input, status states, dashboard components, searchable feedback table, and typed API client.
- Added frontend build workflow and package lockfile.

### Eval Swarm Branch

- Added golden feedback examples, eval runner, eval report, and eval documentation.
- Covered sentiment validity, theme extraction, action item intent, and malformed/provider failures.

### Fan-In

- Reconciled backend/frontend API contract mismatches.
- Aligned frontend types/components to backend response shape.
- Changed eval harness to reuse the app prompt and schema.
- Updated setup and verification documentation.

### Provider-Backed Verification

- Completed manual provider-backed `POST /feedback` smoke from a local PowerShell process with secrets kept out of the repo.
- Verified persisted rows and dashboard aggregation from provider-backed extraction.
- Ran provider-backed eval with `gpt-4o-mini`: 8 cases, 0 malformed outputs/provider failures.

### Security

- Confirmed no tracked secret values or generated dependency/cache/database artifacts.
- Narrowed local CORS, bounded feedback request size, strengthened prompt-injection guidance, and sanitized eval failure reporting.
- Confirmed generated SQLite artifacts are ignored and removed after verification.

### Final Docs

- Finalized README setup/verification instructions.
- Wrote final submission notes in `NOTES.md`.
- Moved remaining non-critical work into known limitations.

### Local Setup Improvement

- Added automatic loading of root `.env` values for the backend using `python-dotenv` with `override=False`.
- Kept terminal-provided environment variables as the higher-priority configuration source.
- Updated root and backend README setup instructions to lead with copying `.env.example` to `.env`.
- Added a focused settings test for `.env` loading and shell precedence.

### UX/API Dry-Run Fix

- Fixed batch parsing so one non-empty line remains one feedback entry, even when it contains commas or words like "but".
- Kept multiline input and CSV-ish row parsing for batch use cases.
- Added parser regression tests for natural-language commas, multiline batches, CSV feedback columns, and empty lines.

### Final Browser Dry Run

- Completed manual browser dry run with backend at `http://localhost:8000` and frontend at `http://localhost:5173`.
- Confirmed root `.env` support worked for backend startup.
- Submitted single feedback and a four-line multiline batch; records persisted and remained visible after refresh.
- Confirmed themes, sentiment distribution, trend over time, and searchable feedback table populated with sentiment, themes, action items, and timestamps.
- Observed one transient local "Failed to fetch" message during testing; backend records had persisted and refresh loaded them successfully.

### Reliability Fix

- Identified the transient browser fetch failure as a SQLite connection lifecycle bug: a connection yielded through FastAPI/Starlette threadpool handling could be used from a different thread.
- Changed routes to open and close request-scoped SQLite connections inside each handler operation.
- Added route tests for `POST /feedback` followed immediately by `GET /dashboard`, `GET /feedback`, and repeated read calls after inserts.

## Current Phase

Phase 6 complete. Ready for final review/submission.
