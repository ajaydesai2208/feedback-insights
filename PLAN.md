# Implementation Plan

## Phase 0: Project Structure

- Create project-local docs and folder structure.
- Add placeholder backend, frontend, eval, and harness files.
- Avoid dependency installation and application logic.

## Phase 1: Backend Thin Slice

- Define request and response schemas.
- Implement batch parsing for pasted feedback.
- Add SQLite persistence.
- Add FastAPI routes for ingesting feedback and reading dashboard data.
- Add focused backend tests.

## Phase 2: LLM Extraction

- Draft extraction prompt and structured output format.
- Add OpenAI client wrapper.
- Handle missing API key and local error states clearly.
- Add schema validation tests.

## Phase 3: Frontend Thin Slice

- Build feedback input flow.
- Build dashboard view with table and charts.
- Add status and error states.
- Connect frontend to backend API.

## Phase 4: Eval Harness

- Add golden feedback examples.
- Run extraction prompt checks.
- Record eval findings in `backend/evals/eval_report.md`.

## Phase 5: Final Review

- Run backend tests, frontend build, and eval harness.
- Update README and submission notes.
- Do a final scope and quality review.
