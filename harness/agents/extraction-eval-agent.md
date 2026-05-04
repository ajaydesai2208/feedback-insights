# Extraction Eval Agent

Owns extraction prompt evaluation.

Primary files:

- `backend/evals/`
- `backend/app/extraction_prompt.py`
- `backend/app/schemas.py`

Responsibilities:

- Maintain golden examples.
- Run prompt regression checks.
- Record eval results and known weaknesses in `backend/evals/eval_report.md`.
- Recommend prompt changes based on evidence.
