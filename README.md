# Feedback Insights

Local fullstack take-home project for Intryc AI.

The app will ingest batches of customer feedback, extract structured insights with the OpenAI API, store results in SQLite, and display dashboard summaries in a React frontend.

## Stack

- Frontend: React, TypeScript, Vite
- Backend: FastAPI, Python
- Database: SQLite
- LLM provider: OpenAI API
- Eval harness: lightweight prompt regression checks

## Status

Initial repo structure is in place. Application logic and dependencies have not been implemented yet.

## Planned Local Setup

Backend setup will be documented after dependencies are finalized.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
```

Frontend setup will be documented after dependencies are finalized.

```powershell
npm install --prefix frontend
npm run dev --prefix frontend
```

## Environment

Copy `.env.example` to `.env` when implementing the backend.

Required values will include:

- `OPENAI_API_KEY`
- `DATABASE_URL`

## Project Docs

- `AGENTS.md`: project-local Codex and agent workflow instructions
- `PLAN.md`: phased implementation plan
- `PROGRESS.md`: milestone tracker
- `TODO.md`: next implementation tasks
- `LOGS.md`: debugging and change log
- `NOTES.md`: final submission notes outline
- `harness/`: repo-local agent workflow docs
