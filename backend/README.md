# Backend

FastAPI backend for Feedback Insights.

## Setup

From the repository root:

```powershell
python -m pip install -r backend/requirements.txt
Copy-Item .env.example .env
```

Edit `.env` and add your own OpenAI key. The expected variable names and safe defaults are shown in `.env.example`.

The backend automatically loads the root `.env` file without overriding shell-provided environment variables.

Alternative terminal-only setup:

```powershell
$env:OPENAI_API_KEY = "your-api-key"
$env:OPENAI_MODEL = "gpt-4o-mini"
$env:FEEDBACK_INSIGHTS_DB = "backend/feedback_insights.sqlite3"
```

## Run

```powershell
uvicorn backend.app.main:app --reload
```

The API defaults to `http://localhost:8000`.

## Endpoints

- `GET /health`: returns service status.
- `POST /feedback`: accepts `{ "text": "..." }`, preserves each non-empty line as one feedback entry, parses CSV-ish rows, extracts insights with OpenAI, persists records, and returns created records.
- `GET /feedback`: returns persisted feedback records.
- `GET /dashboard`: returns theme frequencies, sentiment distribution, sentiment trend, and feedback records.

`POST /feedback` returns `503` when `OPENAI_API_KEY` is missing and does not use a production stub.

## Test

```powershell
python -m pytest backend/tests
```
