# Logs

Concise record of the implementation issues, fixes, and verification results that matter for walkthrough.

## 2026-05-04: Bootstrap and Harness

Context:
- Created the Feedback Insights repo structure and project-local Codex-native harness.

Result:
- Added `AGENTS.md`, planning docs, backend/frontend/eval scaffolds, and `harness/` role, command, skill, and run-report docs.
- Kept global runtime config such as `.codex` and `.claude` out of the repo.

## 2026-05-04: Fan-In Integration

Context:
- Integrated Backend Builder, Frontend Builder, and Extraction Eval Agent work.

Issue:
- Frontend/backend contract mismatch surfaced during fan-in: frontend expected different feedback field names and sentiment distribution shape.

Fix:
- Kept backend response shape canonical.
- Updated frontend types/components to use `feedback_text`, numeric `id`, and the backend `sentiment_distribution` object.
- Changed eval harness to reuse the app extraction prompt and Pydantic schema instead of carrying a separate prompt path.

Verification:
- Backend tests passed.
- Frontend build passed.
- Eval harness ran in skipped mode when no provider key was visible to the command process.

## 2026-05-04: Provider-Backed Verification

Context:
- Provider-backed verification was completed manually from a local PowerShell process where the OpenAI key was visible.

Result:
- `POST /feedback` returned 201 using the real OpenAI provider path.
- Persisted records were returned by `GET /feedback`.
- `GET /dashboard` returned populated theme frequency, sentiment distribution, and trend data.
- `python backend/evals/run_eval.py` evaluated 8 cases with 0 malformed outputs/provider failures.
- No secret values were written to repo files or logs.

## 2026-05-04: Security Review

Context:
- Reviewed repo for committed secrets, generated artifacts, environment handling, CORS, prompt injection risk, input handling, eval logging, and dependency risk.

Fixes:
- Narrowed CORS methods and headers for the local frontend.
- Added a 20,000 character maximum to the feedback request body.
- Strengthened prompt guidance so customer feedback is treated as untrusted data.
- Sanitized eval provider/parsing failure text.

Verification:
- No tracked secret-like values were found.
- `.env` and SQLite files are ignored.
- Backend tests and frontend build passed.

## 2026-05-04: Root Env Loading

Context:
- Reviewer setup is smoother if a root `.env` copied from `.env.example` works automatically.

Fix:
- Added `python-dotenv` support with `override=False`.
- Backend loads root `.env` without overriding shell-provided environment variables.
- Added a focused settings test for `.env` loading and shell precedence.

Verification:
- Backend tests passed.
- Frontend build passed.
- Backend import/startup validation passed.
- Provider-backed smoke using the key loaded from ignored `.env` passed.

## 2026-05-04: Batch Parser Dry-Run Fix

Context:
- Browser dry run showed a single feedback sentence with a comma and "but" was split into multiple records.

Fix:
- Parser now preserves one non-empty line as one feedback entry.
- Multiline input remains batch input.
- CSV-ish rows remain batch input.

Verification:
- Added parser tests for natural-language commas, multiline input, CSV-ish input, and empty lines.
- Backend tests passed.
- Frontend build passed.

## 2026-05-04: SQLite Connection Ownership Fix

Context:
- Browser dry run surfaced a SQLite connection ownership issue during immediate post-submit refresh.
- Records persisted, but immediate `GET /dashboard` or `GET /feedback` could fail with a SQLite thread error.

Root cause:
- A SQLite connection yielded through FastAPI/Starlette sync handling could be used across worker-thread boundaries.

Fix:
- Routes now open, initialize, use, and close SQLite connections inside each handler operation.
- This keeps the local demo path smooth without adding SQLAlchemy or changing the user-facing DB path.

Verification:
- Added route tests for `POST /feedback` followed immediately by `GET /dashboard`, `POST /feedback` followed immediately by `GET /feedback`, and repeated reads after inserts.
- `python -m pytest backend/tests` passed with 16 tests.
- `npm run build --prefix frontend` passed.
- Backend import/startup validation passed.

## 2026-05-04: Final Browser Dry Run

Context:
- Manual browser dry run after setup, parser, provider, and reliability fixes.

Result:
- Backend health was green.
- Frontend loaded at `http://localhost:5173`.
- Root `.env` startup worked.
- Single feedback and four-line batch submissions worked.
- Refresh showed persisted records.
- Themes, sentiment distribution, trend, and searchable feedback table populated.

## 2026-05-04: Final Docs

Result:
- `NOTES.md` finalized under 500 words.
- `PROGRESS.md` cleaned into a project timeline.
- `TODO.md` reduced to final completion checklist and non-critical future polish.
