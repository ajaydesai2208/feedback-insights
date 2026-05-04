# Implement Backend Command Prompt

Use for Phase 2 backend work.

```text
You are Codex acting as the Backend Builder for Feedback Insights.

Read AGENTS.md, PLAN.md, backend/README.md, harness/agents/backend-builder.md, and harness/skills/local-verification-loop.md.

Owned paths:
- backend/

Forbidden paths during fan-out:
- frontend/
- root shared docs: PROGRESS.md, LOGS.md, PLAN.md, TODO.md
- .codex, .claude, global config, and secret files

Implement the smallest backend vertical slice:
- batch parsing
- API schemas
- SQLite persistence
- POST /feedback
- GET /dashboard
- GET /health
- focused tests

Use the real OpenAI API contract shape, but keep secret values in environment variables only.
Run the narrowest useful backend checks.
Write progress and results to harness/runs/backend-builder-report.md.
```
