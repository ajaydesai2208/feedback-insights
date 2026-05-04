# Feedback Insights

Feedback Insights is a local full-stack take-home project for Intryc AI.

The app will let a single user paste customer feedback one at a time or in batch. The backend will call the real OpenAI API to extract sentiment, themes, and explicit action items or feature requests. Results will be stored in SQLite and shown in a React dashboard.

## Planned Stack

- Frontend: React, TypeScript, Vite
- Backend: FastAPI, Python
- Database: SQLite
- LLM provider: OpenAI API
- Stretch: prompt eval harness

## Planned Features

- Paste single or batch feedback
- Extract sentiment: `positive`, `neutral`, or `negative`
- Extract 1 to 3 short themes
- Extract explicit action items or feature requests
- Persist original feedback and extraction results
- Show theme frequency, sentiment distribution, sentiment trend, and searchable feedback records

## Current Status

The repository scaffold and project-local harness docs are being prepared. Application logic and dependencies are not implemented yet.

## Local Setup

Final setup commands will be added after backend and frontend dependencies are intentionally introduced.

## Project Docs

- `AGENTS.md`: project-local Codex behavior and architecture rules
- `PLAN.md`: phased build plan
- `PROGRESS.md`: milestone tracker
- `TODO.md`: role-based next tasks
- `LOGS.md`: debugging and change log
- `NOTES.md`: final submission notes outline
- `harness/`: repo-local agent workflow docs
