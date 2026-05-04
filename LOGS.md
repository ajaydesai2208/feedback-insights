# Logs

Simple debugging and change log for commands, failures, fixes, and decisions.

## Format

```text
### YYYY-MM-DD: Short Title

Context:
- What was being changed or verified.

Commands:
- Exact commands run, if any.

Result:
- Pass, fail, skipped, or blocked.

Decision:
- Any important implementation or workflow decision.

Follow-up:
- Remaining work or owner.
```

## Entries

### 2026-05-04: Initial Structure

Context:
- Created the Feedback Insights project scaffold.

Commands:
- No dependency installation commands were run.

Result:
- Project-local docs, backend placeholders, frontend placeholders, eval placeholders, and harness docs exist.

Decision:
- Use `harness/` as the committed project-local agent workflow instead of global runtime config.

Follow-up:
- Complete Phase 1 documentation refinement, then start the backend vertical slice.

### 2026-05-04: Fan-In Integration

Context:
- Integrated merged Backend Builder, Frontend Builder, and Eval Agent work.

Commands:
- `python -m pytest backend/tests`
- `python -c "from fastapi.testclient import TestClient; from backend.app.main import app; client = TestClient(app); print(app.title)"`
- `npm run build --prefix frontend`
- `npm install --prefix frontend`
- `npm run build --prefix frontend`
- `python backend/evals/run_eval.py`

Result:
- Backend tests passed: 9 tests.
- Backend import/startup validation passed and printed `Feedback Insights API`.
- Initial frontend build failed because local frontend dependencies were not installed and `tsc` was unavailable.
- `npm install --prefix frontend` completed, with 2 moderate npm audit findings reported.
- Frontend build/typecheck passed after installing committed dependencies.
- Eval dry run passed in skipped mode because `OPENAI_API_KEY` is not set.

Decision:
- Kept backend API response fields as the canonical contract: `id`, `feedback_text`, `sentiment`, `themes`, `action_items`, and `created_at`.
- Updated frontend types and components to consume backend response shapes directly.
- Kept `sentiment_distribution` as the backend object shape instead of converting it to a frontend-only array.
- Reused `backend/app/extraction_prompt.py` and `backend/app/schemas.py` from the eval harness to avoid prompt/schema drift.
- Standardized local database configuration on `FEEDBACK_INSIGHTS_DB`.

Follow-up:
- Run provider-backed manual smoke test with a real `OPENAI_API_KEY`.
- Decide whether to address npm audit findings without broad package churn.
- Complete final review and write `NOTES.md` under 500 words.
