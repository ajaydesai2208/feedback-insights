# TODO

## Orchestrator

- Run Phase 6 final review.
- Fold any final review findings into `LOGS.md` and `PROGRESS.md`.
- Write final `NOTES.md` under 500 words after verification is complete.

## Backend Builder

- Perform a real `POST /feedback` smoke test with `OPENAI_API_KEY` set.
- Confirm the default SQLite file path is acceptable for local review.
- Add route-level success tests with a mocked extraction function if time allows.

## Frontend Builder

- Smoke test the UI against the running backend in a browser.
- Confirm empty, loading, success, and OpenAI-missing-key error states are clear.
- Decide whether to address the 2 moderate npm audit findings without broad dependency churn.

## Eval Agent

- Run provider-backed eval with `OPENAI_API_KEY` set.
- Review `backend/evals/eval_report.md` for prompt weaknesses.
- Adjust prompt only if eval evidence supports a specific change.

## Review Agent

- Review final implementation for take-home fit, missing tests, stale docs, secret handling, and setup clarity.
- Verify no auth, Docker, deployment, queues, Redis, CI/CD, or large UI library slipped in.
- Lead with findings and keep fixes scoped.
