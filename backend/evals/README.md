# Extraction Evals

Lightweight eval harness for the feedback extraction prompt.

Planned workflow:

1. Store representative examples in `golden_feedback.json`.
2. Run the extraction prompt against those examples.
3. Compare required fields, sentiment labels, themes, and summary quality.
4. Record results in `eval_report.md`.
