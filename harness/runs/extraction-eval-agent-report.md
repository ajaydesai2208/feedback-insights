# Extraction Eval Agent Report

Scope:
- Built the standalone prompt eval harness for the planned feedback extraction contract.
- Stayed within `backend/evals/` plus this assigned run report.
- Did not edit `backend/app/extraction_prompt.py` because backend app files are owned by another parallel branch.

Files changed:
- `backend/evals/golden_feedback.json`
- `backend/evals/run_eval.py`
- `backend/evals/README.md`
- `backend/evals/eval_report.md`
- `harness/runs/extraction-eval-agent-report.md`

Eval cases added:
- 8 golden examples covering positive feedback, negative feedback, neutral feedback, mixed feedback, feature request, support/process complaint, product usability issue, and CX/customer-success style feedback.

Eval command/result:
- `python backend/evals/run_eval.py`
- Result: exited 0 because `OPENAI_API_KEY` is not set; wrote `backend/evals/eval_report.md` with `Status: skipped` and rerun instructions.
- `python -m py_compile backend/evals/run_eval.py`
- Result: passed syntax compilation. Removed the generated `backend/evals/__pycache__` artifact afterward.

Prompt or schema recommendations:
- Keep extraction output to `sentiment`, `themes`, and `action_items`.
- Require `themes` to contain 1 to 3 short concrete strings.
- Require `action_items` to include explicit customer requests only and return an empty list when no request is present.
- Treat mixed feedback as `neutral` unless the overall tone is clearly positive or negative.

Known issues:
- The backend prompt and schema are placeholders in this branch, so `run_eval.py` carries a local eval prompt for now.
- Provider-backed scoring requires `OPENAI_API_KEY` and the `openai` Python package.
