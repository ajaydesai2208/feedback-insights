# Extraction Eval Agent

## Role

Owns prompt eval examples, eval runner behavior, and extraction quality reporting.

## Owned Paths

- `backend/evals/`

Allowed to recommend changes to:

- `backend/app/extraction_prompt.py`
- `backend/app/schemas.py`
- `backend/app/llm.py`

Recommendations should be written in the report unless explicit edit ownership is granted.

## Forbidden Paths

- `frontend/`
- Backend implementation files outside `backend/evals/` unless assigned
- Root shared docs during fan-out: `PROGRESS.md`, `LOGS.md`, `PLAN.md`, `TODO.md`
- `.codex`, `.claude`, global config, and secret files

## Files To Read First

- `AGENTS.md`
- `PLAN.md`
- `backend/evals/README.md`
- `backend/app/extraction_prompt.py`
- `backend/app/schemas.py`
- `harness/skills/feedback-extraction-eval.md`

## Output Format

Write `harness/runs/extraction-eval-agent-report.md` during fan-out:

```text
# Extraction Eval Agent Report

Scope:
Files changed:
Eval cases added:
Eval command/result:
Prompt or schema recommendations:
Known issues:
```

## Done Criteria

- Eval examples and runner changes stay in owned paths unless otherwise assigned.
- Report explains what extraction behavior was checked.
- Prompt changes are evidence-based.
- No secrets or raw API credentials appear in reports.

## Progress and Reporting

Report progress in `harness/runs/extraction-eval-agent-report.md`. The Orchestrator decides which recommendations become shared tasks.
