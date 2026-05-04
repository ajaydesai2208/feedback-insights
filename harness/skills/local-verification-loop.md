# Local Verification Loop

Project-specific workflow for checking Feedback Insights changes.

## Use When

- Implementing backend parser, schemas, database, routes, or dashboard aggregation.
- Implementing frontend components or API calls.
- Integrating eval harness changes.

## Loop

1. Name the behavior under test.
2. Pick the narrowest command that exercises it.
3. Run the command from the repo root.
4. Fix the closest cause of failure.
5. Repeat until the command passes or the blocker is explicit.
6. Record meaningful failures and decisions in `LOGS.md` during fan-in, or in `harness/runs/<agent>-report.md` during fan-out.

## Command Map

- Backend parser/schema/database: `python -m pytest backend/tests`
- Frontend build: `npm run build --prefix frontend`
- Eval harness: `python backend/evals/run_eval.py`

## Rules

- Do not run install commands unless the phase calls for dependency setup.
- Do not hide failed commands.
- Do not claim verification for code paths that were skipped.
