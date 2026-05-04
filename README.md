# Feedback Insights

Feedback Insights is a local full-stack take-home project for Intryc AI. It lets one user paste customer feedback one at a time or in batch, sends each feedback entry to the OpenAI API for structured extraction, stores the original feedback and extraction in SQLite, and displays the results in a React dashboard.

## What It Does

- Parses single, multiline, or CSV-ish pasted feedback.
- Extracts sentiment: `positive`, `neutral`, or `negative`.
- Extracts 1 to 3 short themes.
- Extracts explicit action items or feature requests only.
- Persists feedback and extraction results to SQLite.
- Shows ranked themes, sentiment distribution, sentiment trend, and a searchable feedback table.
- Includes a lightweight extraction eval harness as the stretch goal.

## Stack

- Frontend: React, TypeScript, Vite
- Backend: FastAPI, Python
- Database: SQLite
- LLM provider: OpenAI API
- Eval harness: Python script using the same app prompt/schema contract

## Local Setup

From a fresh clone, run these commands from the repository root.

Install backend dependencies:

```powershell
python -m pip install -r backend/requirements.txt
```

Install frontend dependencies:

```powershell
npm install --prefix frontend
```

Set environment variables:

```powershell
$env:OPENAI_API_KEY = "your-api-key"
$env:OPENAI_MODEL = "gpt-4o-mini"
$env:FEEDBACK_INSIGHTS_DB = "backend/feedback_insights.sqlite3"
$env:VITE_API_BASE_URL = "http://localhost:8000"
```

Run the backend:

```powershell
uvicorn backend.app.main:app --reload
```

Run the frontend in another terminal:

```powershell
npm run dev --prefix frontend
```

Open the Vite URL, usually `http://localhost:5173`.

## Environment Variables

- `OPENAI_API_KEY`: required for `POST /feedback` and provider-backed evals.
- `OPENAI_MODEL`: optional, defaults to `gpt-4o-mini`.
- `FEEDBACK_INSIGHTS_DB`: optional, defaults to `backend/feedback_insights.sqlite3`.
- `VITE_API_BASE_URL`: optional, defaults to `http://localhost:8000`.

Do not commit `.env` or real API keys. `.env.example` contains safe placeholders only.

## Backend Commands

```powershell
python -m pytest backend/tests
python -c "from fastapi.testclient import TestClient; from backend.app.main import app; print(app.title)"
uvicorn backend.app.main:app --reload
```

## Frontend Commands

```powershell
npm install --prefix frontend
npm run dev --prefix frontend
npm run build --prefix frontend
```

## Eval Harness

Run the extraction eval:

```powershell
python backend/evals/run_eval.py
```

If `OPENAI_API_KEY` is missing, the eval exits gracefully and writes a skipped report. With provider access, it writes aggregate results to `backend/evals/eval_report.md`.

## Project Structure

```text
backend/          FastAPI app, SQLite persistence, OpenAI wrapper, tests, evals
frontend/         React + TypeScript + Vite app
harness/          Project-local Codex-native agent workflow docs and run reports
AGENTS.md         Project-local coding and coordination rules
PLAN.md           Phased build plan
PROGRESS.md       Iteration and verification timeline
LOGS.md           Debugging, verification, and security review log
TODO.md           Final limitations and polish items
NOTES.md          Final submission notes
```

## Agentic Workflow Docs

This repo uses `AGENTS.md` and `harness/` as the project-local agentic coding harness. The harness documents the Orchestrator, Backend Builder, Frontend Builder, Extraction Eval Agent, and Review/Fan-in roles, plus reusable commands and run reports under `harness/runs/`.

## Known Limitations

- No auth, deployment, Docker, queues, Redis, or CI/CD by design.
- `npm install` reports 2 moderate audit findings; they were not force-fixed to avoid broad dependency churn.
- Route-level success tests with mocked extraction would be useful future polish.
- The eval harness is intentionally lightweight and uses approximate scoring for themes/action intent.
