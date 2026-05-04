# Verify Project Command Prompt

Use during fan-in and before final review.

```text
You are Codex verifying Feedback Insights after integration.

Read AGENTS.md, PLAN.md, LOGS.md, TODO.md, and specialist reports in harness/runs/.

Run only documented verification commands that are relevant to implemented code:
- python -m pytest backend/tests
- npm run build --prefix frontend
- python backend/evals/run_eval.py

If a command cannot run because dependencies are not installed or the phase is not implemented, say so clearly.
Fix only scoped issues tied to failed verification.
Update LOGS.md with commands, results, and follow-up.
```
