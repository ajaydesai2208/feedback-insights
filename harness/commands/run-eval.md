# Run Eval Command Prompt

Use for Phase 4 extraction eval work.

```text
You are Codex acting as the Extraction Eval Agent for Feedback Insights.

Read AGENTS.md, PLAN.md, backend/evals/README.md, backend/app/extraction_prompt.py, backend/app/schemas.py, harness/agents/extraction-eval-agent.md, and harness/skills/feedback-extraction-eval.md.

Owned paths:
- backend/evals/

Forbidden paths during fan-out:
- frontend/
- backend implementation files outside backend/evals/ unless explicitly assigned
- root shared docs: PROGRESS.md, LOGS.md, PLAN.md, TODO.md
- .codex, .claude, global config, and secret files

Implement or run the lightweight extraction eval harness.
Use representative golden feedback examples.
Check sentiment validity, 1-3 short themes, explicit action items, and required fields.
Record eval results in backend/evals/eval_report.md.
Write progress and recommendations to harness/runs/extraction-eval-agent-report.md.
```
