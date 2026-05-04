# Feedback Extraction Eval

Project-specific playbook for the OpenAI extraction prompt.

## Extraction Target

Each feedback entry must produce:

- `sentiment`: `positive`, `neutral`, or `negative`
- `themes`: 1 to 3 short strings
- `action_items`: explicit action items or feature requests only

## Golden Data

Keep examples in `backend/evals/golden_feedback.json`.

Include cases for:

- clear positive praise
- clear negative complaint
- mixed or neutral feedback
- multiple themes
- explicit feature request
- no explicit action item

## Eval Checks

- Required fields are present.
- Sentiment label is valid.
- Theme count is between 1 and 3.
- Themes are short and relevant.
- Action items are explicit, not invented.

## Reporting

Record run results in `backend/evals/eval_report.md`.

During parallel work, write recommendations to `harness/runs/extraction-eval-agent-report.md`. Do not edit shared root docs during fan-out.

## Prompt Change Rule

Change the prompt only when an eval failure shows a specific weakness. Record the before/after reason in the eval report.
