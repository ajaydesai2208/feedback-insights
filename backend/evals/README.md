# Extraction Evals

Lightweight prompt eval harness for the feedback extraction contract.

## Files

- `golden_feedback.json`: representative feedback examples with expected sentiment, themes, and action item intent.
- `run_eval.py`: runs each golden example against the OpenAI API when `OPENAI_API_KEY` is available.
- `eval_report.md`: generated report from the latest eval run.

## Run

```powershell
python backend/evals/run_eval.py
```

The runner uses `OPENAI_MODEL` when set. Otherwise it defaults to `gpt-4o-mini`.

If `OPENAI_API_KEY` is missing, the script exits cleanly, writes a skipped report, and prints instructions for rerunning with a key.

## Checks

- Required fields are present: `sentiment`, `themes`, and `action_items`.
- Sentiment is one of `positive`, `neutral`, or `negative`.
- Sentiment exact match is calculated against the golden example.
- Theme overlap is a simple token overlap score against expected themes.
- Action item intent checks whether expected customer requests appear in extracted action items.
- Malformed outputs and provider failures are recorded in `eval_report.md`.

The metrics are intentionally small and explainable. Use failures to guide prompt/schema changes after backend integration.
