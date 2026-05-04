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

### 2026-05-04: Verification Checkpoint

Context:
- Ran a Windows-friendly verification pass after fan-in integration.

Commands:
- `python -m pip install -r backend/requirements.txt`
- `npm install --prefix frontend`
- `python -m pytest backend/tests`
- `python -c "from fastapi.testclient import TestClient; from backend.app.main import app; client = TestClient(app); print(app.title)"`
- `npm run build --prefix frontend`
- `python -c "import tempfile; from pathlib import Path; from backend.app.db import connect, initialize_database; path=Path(tempfile.gettempdir())/'feedback_insights_verify.sqlite3'; conn=connect(path); initialize_database(conn); tables=conn.execute('select name from sqlite_master where type='table' and name='feedback'').fetchall(); conn.close(); path.unlink(missing_ok=True); print('sqlite initialized' if tables else 'sqlite missing table')"`
- `python backend/evals/run_eval.py`
- Local uvicorn health check on `127.0.0.1:8765`
- Local API persistence/dashboard smoke using a temporary SQLite database and mocked extraction
- `git check-ignore -v .env backend/.venv/ __pycache__/ .pytest_cache/ frontend/node_modules/ frontend/dist/ backend/feedback_insights.sqlite3`
- Filename-only secret scans for OpenAI key patterns

Result:
- No committed OpenAI key pattern was found in `HEAD`.
- A secret-like value was found in `.env.example` during verification and was removed without logging the value.
- Required ignore checks passed for `.env`, `backend/.venv/`, `__pycache__/`, `.pytest_cache/`, `frontend/node_modules/`, `frontend/dist/`, and SQLite database files.
- Backend dependencies installed cleanly in the current Python environment.
- Frontend dependencies installed cleanly, with 2 moderate npm audit findings still reported.
- Backend tests passed: 9 tests.
- Backend import/startup validation passed.
- Uvicorn started locally and `GET /health` returned `ok`.
- SQLite initialization passed using a temporary database outside the repo.
- Mocked API smoke verified `POST /feedback`, `GET /feedback`, and `GET /dashboard` response shapes and aggregation.
- Frontend build/typecheck passed.
- Eval harness exited gracefully in skipped mode because `OPENAI_API_KEY` is not present in the current shell.
- Provider-backed API smoke and provider-backed eval were skipped because `OPENAI_API_KEY` is not present.
- A generated ignored SQLite database was removed after verification.

Decision:
- Keep `.env.example` blank for secrets and use only safe example values.
- Keep SQLite database files ignored and out of the working tree.
- Do not run `npm audit fix --force` during verification because it would create broad dependency churn.

Follow-up:
- Run provider-backed `POST /feedback` smoke and provider-backed eval when `OPENAI_API_KEY` is available.
- Rotate any real OpenAI key that may have been copied into `.env.example` before this verification pass.
- Complete final review and final submission notes.

### 2026-05-04: Provider-Backed Verification Attempt

Context:
- Re-ran verification after provider-backed `POST /feedback` smoke and provider-backed eval were requested.
- Historical note: this Codex-process visibility issue was superseded by the later manual provider-backed verification entry.

Commands:
- Checked whether `OPENAI_API_KEY` is visible without printing the value.
- `git check-ignore -v .env backend/.venv/ __pycache__/ .pytest_cache/ frontend/node_modules/ frontend/dist/ backend/feedback_insights.sqlite3`
- Filename-only secret scan for OpenAI key patterns.
- `python -m pip install -r backend/requirements.txt`
- `npm install --prefix frontend`
- `python -m pytest backend/tests`
- `npm run build --prefix frontend`
- `python -c "from fastapi.testclient import TestClient; from backend.app.main import app; print(app.title)"`
- SQLite initialization one-off using a temporary database.
- Local uvicorn health check on `127.0.0.1:8765`.
- `python backend/evals/run_eval.py`
- Local API persistence/dashboard smoke using a temporary SQLite database and mocked extraction.

Result:
- `OPENAI_API_KEY` is not visible to this verification process.
- Secret-pattern filename scan found no matches.
- Required ignore patterns passed.
- Backend dependencies installed cleanly.
- Frontend dependencies installed cleanly, with 2 moderate npm audit findings still reported.
- Backend tests passed: 9 tests.
- Frontend build/typecheck passed.
- Backend import validation passed.
- SQLite initialization passed.
- Uvicorn health check passed.
- Eval harness exited gracefully in skipped mode because `OPENAI_API_KEY` is not visible.
- Mocked API smoke passed for `POST /feedback`, `GET /feedback`, and `GET /dashboard`.
- Provider-backed `POST /feedback` smoke and provider-backed eval did not run in the Codex process because the key was not visible there. They were later completed manually; see the manual provider-backed verification entry below.

Decision:
- Do not write or source any secret from repo files.
- Treat the Codex key visibility failure as a process issue, not an app failure.

Follow-up:
- Manual provider-backed verification was completed later from a PowerShell process where the key was visible.

### 2026-05-04: Provider Key Visibility Recheck

Context:
- Attempted to run only the remaining provider-backed verification checks after `OPENAI_API_KEY` was expected to be loaded before Codex launch.
- Historical note: this Codex-process visibility issue was superseded by the later manual provider-backed verification entry.

Commands:
- Checked whether `OPENAI_API_KEY` is visible without printing the value.
- Repeated the key visibility check with an escalated shell.
- Checked for generated SQLite database files.
- Removed generated ignored SQLite database file from `backend/`.

Result:
- `OPENAI_API_KEY` is still not visible to the Codex shell process.
- Provider-backed `POST /feedback` smoke test did not run in the Codex process.
- Provider-backed eval harness did not run in the Codex process.
- Generated ignored SQLite database was removed before finishing.

Decision:
- Do not write or source secrets from repository files.
- Treat the repeated Codex visibility failure as a process issue, not an app failure.

Follow-up:
- Manual provider-backed verification was completed later from a PowerShell process where the key was visible.

### 2026-05-04: Manual Provider-Backed Verification

Context:
- Provider-backed verification was completed manually from a PowerShell process where `OPENAI_API_KEY` was visible.
- Codex previously could not see the variable because it was running in a different command process. That was a tooling/process visibility issue, not an app failure.

Commands:
- `python backend/evals/run_eval.py`
- FastAPI `TestClient` smoke against `backend.app.main:app` using the actual `POST /feedback` request schema.

Result:
- Provider-backed eval wrote `backend/evals/eval_report.md`.
- Eval harness evaluated 8 cases with 0 malformed outputs/provider failures using `gpt-4o-mini`.
- Provider-backed `POST /feedback` returned 201.
- Smoke input was sanitized customer feedback about product usefulness, slow dashboard behavior, and CSV export for weekly QA reviews.
- Batch parsing split the input into 2 persisted records.
- First persisted record: positive sentiment, `product usefulness` theme, no action items.
- Second persisted record: negative sentiment, `slow dashboard` and `CSV export request` themes, action item for adding CSV export for weekly QA reviews.
- `GET /dashboard` returned 200 with `total_feedback: 2`.
- Dashboard sentiment distribution included positive 1, neutral 0, negative 1.
- Dashboard trend was populated for 2026-05-04.
- Dashboard theme frequencies were populated.
- Generated SQLite artifacts were removed after verification and are ignored by `.gitignore`.

Decision:
- Mark provider-backed `POST /feedback` smoke and provider-backed eval as passed manually.
- Keep secrets out of repo files, logs, reports, and command output.

Follow-up:
- Final review and final submission notes remain.
- Remaining risks are npm audit's 2 moderate findings and optional route-level success tests with mocked extraction.

### 2026-05-04: Security Review

Context:
- Reviewed repository for committed secrets, generated artifacts, environment handling, CORS, prompt injection risk, input handling, eval logging, and unnecessary dependency risk.

Commands:
- `git status --short`
- Filename-only `git grep` checks for secret-like patterns.
- `git ls-files` checks for tracked generated/cache/database paths.
- Working-tree artifact scan for SQLite, cache, `node_modules`, and `dist` files.
- `python -m pytest backend/tests`
- `python -c "from fastapi.testclient import TestClient; from backend.app.main import app; print(app.title)"`
- `npm run build --prefix frontend`
- `python backend/evals/run_eval.py`

Result:
- No tracked `sk-` secret-like values were found.
- `OPENAI_API_KEY=` appears only in `.env.example` with a blank value.
- `api_key` references are limited to environment reads in the OpenAI wrapper/eval harness and a missing-key test.
- No tracked `node_modules`, `dist`, `__pycache__`, `.venv`, `.pytest_cache`, SQLite database, or cache artifacts were found.
- `.gitignore` covers `.env`, `backend/.venv/`, `__pycache__/`, `.pytest_cache/`, `frontend/node_modules/`, `frontend/dist/`, and SQLite database files.
- Backend tests passed: 9 tests.
- Backend import validation passed.
- Frontend build/typecheck passed.
- Eval dry run exited gracefully when the key was not visible to this process.
- Generated ignored SQLite database was removed after review.

Fixes:
- Narrowed CORS methods to `GET` and `POST`, and request headers to `Content-Type`.
- Added a 20,000 character maximum to the feedback request body.
- Strengthened the extraction prompt to treat customer feedback as untrusted data and ignore instructions inside feedback.
- Sanitized eval harness provider/parsing failure text so provider exceptions are not written verbatim to the eval report.

Decision:
- Do not add auth, Docker, deployment, CI, queues, Redis, or extra infrastructure for this local take-home.
- Do not force npm audit fixes because that would create broad dependency churn.

Follow-up:
- Remaining risks are npm audit's 2 moderate findings and optional route-level success tests with mocked extraction.

### 2026-05-04: Final Documentation

Context:
- Finalized submission-facing documentation after implementation, fan-in, provider-backed verification, and security review.

Commands:
- Documentation read pass over root docs, harness docs, run reports, backend docs, frontend docs, and eval docs.

Result:
- `README.md` now includes project overview, setup, environment variables, commands, eval harness, project structure, workflow docs, and known limitations.
- `NOTES.md` was written as the final under-500-word submission note.
- `PROGRESS.md` now shows the full iteration from structure through final docs.
- `TODO.md` now lists only known limitations and future polish.
- Harness run reports now include fan-in resolution notes for backend/frontend contract alignment and eval prompt/schema reuse.
- Final submission review reran backend tests and frontend build successfully, then removed the generated ignored SQLite database file.

Decision:
- Keep hooks minimal/skipped for this scope; documented commands, owned paths, run reports, and verification loops were sufficient.

Follow-up:
- Final submission review.

### 2026-05-04: Root Env Loading

Context:
- Improved local setup so reviewers can copy `.env.example` to a root `.env`, add their own OpenAI key, and start the backend without separately exporting shell variables.

Commands:
- `python -m pytest backend/tests`
- `npm run build --prefix frontend`
- `python -c "from fastapi.testclient import TestClient; from backend.app.main import app; print(app.title)"`
- Checked whether `OPENAI_API_KEY` is visible without printing the value.
- `git status --short`
- `git grep -n "sk-" .`
- `git grep -n "OPENAI_API_KEY=" .`
- `git check-ignore -v .env`
- Checked for generated SQLite files and removed the generated ignored SQLite database.

Result:
- Added backend root `.env` loading via `python-dotenv` with `override=False`.
- Shell-provided environment variables still take precedence over `.env` values.
- Updated root README and backend README setup flow.
- Added a focused settings test for `.env` loading behavior.
- Backend tests passed: 10 tests.
- Frontend build/typecheck passed.
- Backend import/startup validation passed.
- `.env` is ignored by git.
- `OPENAI_API_KEY` was not visible to the shell but was visible after backend root `.env` loading.
- Provider-backed smoke using the key loaded from ignored `.env` passed: `POST /feedback` returned 201, persisted 2 records, and dashboard data was populated.
- A local ignored `.env` exists and was not read or modified.
- Temporary/generated SQLite databases were removed after verification.

Decision:
- Keep configuration local and simple; no new infrastructure or secret files are committed.

Follow-up:
- None for root `.env` setup.
