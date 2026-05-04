# Feedback Insights

Feedback Insights is a local full-stack take-home project for Intryc AI.

The app lets a single user paste customer feedback one at a time or in batch. The FastAPI backend calls the real OpenAI API to extract sentiment, themes, and explicit action items or feature requests. Results are stored in SQLite and shown in a React dashboard.

## Stack

- Frontend: React, TypeScript, Vite
- Backend: FastAPI, Python
- Database: SQLite
- LLM provider: OpenAI API
- Stretch: prompt eval harness

## Features

- Paste single or batch feedback
- Extract sentiment: `positive`, `neutral`, or `negative`
- Extract 1 to 3 short themes
- Extract only explicit action items or feature requests
- Persist original feedback and extraction results
- Show theme frequency, sentiment distribution, sentiment trend, and searchable feedback records

## Local Setup

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

The frontend defaults to `http://localhost:5173` and the backend defaults to `http://localhost:8000`.

## Verification

Backend tests:

```powershell
python -m pytest backend/tests
```

Backend import/startup validation:

```powershell
python -c "from fastapi.testclient import TestClient; from backend.app.main import app; client = TestClient(app); print(app.title)"
```

Frontend build and typecheck:

```powershell
npm run build --prefix frontend
```

Eval harness dry run:

```powershell
python backend/evals/run_eval.py
```

If `OPENAI_API_KEY` is not set, the eval harness writes a skipped report and exits without calling the provider.

## Project Docs

- `AGENTS.md`: project-local Codex behavior and architecture rules
- `PLAN.md`: phased build plan
- `PROGRESS.md`: milestone tracker
- `TODO.md`: role-based next tasks
- `LOGS.md`: debugging and change log
- `NOTES.md`: final submission notes outline
- `harness/`: repo-local agent workflow docs
