# Backend

FastAPI backend for Feedback Insights.

## Setup

```powershell
python -m pip install -r backend/requirements.txt
$env:OPENAI_API_KEY = "your-api-key"
```

Optional environment variables:

- `OPENAI_MODEL`: defaults to `gpt-4o-mini`
- `FEEDBACK_INSIGHTS_DB`: defaults to `backend/feedback_insights.sqlite3`

## Run

```powershell
uvicorn backend.app.main:app --reload
```

The API defaults to `http://localhost:8000`.

## Endpoints

- `GET /health`: returns service status.
- `POST /feedback`: accepts `{ "text": "..." }`, parses single, multiline, or CSV-ish pasted feedback, extracts insights with OpenAI, persists records, and returns created records.
- `GET /feedback`: returns persisted feedback records.
- `GET /dashboard`: returns theme frequencies, sentiment distribution, sentiment trend, and feedback records.

`POST /feedback` returns `503` when `OPENAI_API_KEY` is missing and does not use a production stub.

## Test

```powershell
python -m pytest backend/tests
```
