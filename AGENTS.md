# Feedback Insights Agent Guide

Project-local operating guide for Codex work in this repository.

## Project Goal

Build a local full-stack app for the Intryc AI Fullstack Engineer take-home.

Feedback Insights lets one user paste customer feedback one at a time or in batch, extracts structured insights with the real OpenAI API, stores the original feedback and extraction in SQLite, and shows a dashboard of trends and searchable records.

## Stack

- Frontend: React, TypeScript, Vite
- Backend: FastAPI, Python
- Database: SQLite
- LLM provider: OpenAI API
- Stretch: small eval harness for extraction prompt quality
- Excluded unless later justified: auth, deployment, Docker

## Architecture

- `backend/app/main.py`: FastAPI app, route wiring, CORS setup.
- `backend/app/schemas.py`: API request and response contracts.
- `backend/app/db.py`: SQLite connection, schema setup, persistence helpers.
- `backend/app/models.py`: internal persisted record shapes.
- `backend/app/batch_parser.py`: split pasted batch input into feedback entries.
- `backend/app/extraction_prompt.py`: extraction instructions and output contract.
- `backend/app/llm.py`: OpenAI API client wrapper and error handling.
- `backend/app/services.py`: ingestion orchestration across parser, LLM, and database.
- `backend/app/dashboard.py`: theme, sentiment, trend, and list aggregation.
- `frontend/src/api.ts`: HTTP calls to backend.
- `frontend/src/types.ts`: frontend types matching API schemas.
- `frontend/src/components/`: focused UI components.
- `backend/evals/`: golden examples, eval runner, eval report.
- `harness/`: committed project-local agent workflow docs.

## File Ownership

- Orchestrator owns root planning docs and `harness/`.
- Backend Builder owns `backend/`.
- Frontend Builder owns `frontend/`.
- Eval Agent owns `backend/evals/` and may propose prompt/schema changes through a report.
- Review Agent reads all paths but should only edit when explicitly assigned a small fix.

During parallel work, specialists must write progress to `harness/runs/<agent>-report.md`. They must not edit shared root files such as `PROGRESS.md`, `LOGS.md`, `PLAN.md`, or `TODO.md` during fan-out. The Orchestrator updates shared docs during fan-in.

## Coding Conventions

- Prefer small functions, explicit names, and early returns.
- Keep backend logic testable without starting the server.
- Keep frontend components typed and data-driven.
- Do not add abstractions until repeated behavior makes them useful.
- Do not install packages until the relevant phase needs them.
- Do not create `.codex`, `.claude`, or global runtime config.
- Keep comments for non-obvious contracts, parsing rules, or external API boundaries.

## API Contract

Planned local backend base URL: `http://localhost:8000`.

Initial endpoint shape:

- `POST /feedback`: accepts raw feedback text or batch text, returns created records with extraction results.
- `GET /dashboard`: returns theme frequencies, sentiment distribution, sentiment trend, and feedback list data.
- `GET /health`: returns local service health.

Keep response fields stable once frontend work starts. If a backend contract changes, update `frontend/src/types.ts`, tests, README notes, and relevant harness report.

## OpenAI Extraction Contract

For each feedback entry, extract:

- `sentiment`: one of `positive`, `neutral`, `negative`
- `themes`: 1 to 3 short theme strings
- `action_items`: explicit action items or feature requests only

The OpenAI wrapper must:

- Read the API key from environment configuration.
- Avoid logging secrets or full provider payloads with credentials.
- Validate model output before persistence.
- Return useful local errors for missing API key, invalid model output, and provider failures.

## SQLite Persistence

Persist both source and extraction data.

Expected stored fields:

- unique id
- original feedback text
- sentiment
- themes
- action items
- created timestamp
- raw extraction metadata only if it is safe and useful

Use SQLite for local development. Keep schema setup simple and reproducible.

## Verification Commands

Do not run install commands until dependencies are intentionally added.

Planned backend tests:

```powershell
python -m pytest backend/tests
```

Planned backend server:

```powershell
uvicorn backend.app.main:app --reload
```

Planned frontend build:

```powershell
npm run build --prefix frontend
```

Planned frontend dev server:

```powershell
npm run dev --prefix frontend
```

Planned eval:

```powershell
python backend/evals/run_eval.py
```

Record failed commands and important fixes in `LOGS.md`.

## Swarm Coordination

Use one Orchestrator and bounded specialist agents.

- Use parallelism only when owned paths do not overlap.
- Assign explicit owned and forbidden paths before fan-out.
- Specialists report to `harness/runs/<agent>-report.md`.
- Orchestrator performs fan-in, resolves conflicts, and updates root docs.
- Review Agent runs after integration, not during overlapping implementation.
- Do not run a swarm for small single-file work.

## No-Secret Rules

- Never commit `.env` or API keys.
- Keep `.env.example` safe and blank.
- Do not paste provider secrets into logs, reports, or eval outputs.
- If an error includes a secret-bearing value, summarize it instead of copying it.
