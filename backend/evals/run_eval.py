"""Run a lightweight eval for feedback extraction quality."""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EVAL_DIR = Path(__file__).resolve().parent
REPO_ROOT = EVAL_DIR.parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from backend.app.extraction_prompt import EXTRACTION_SYSTEM_PROMPT
from backend.app.schemas import ExtractionResult

GOLDEN_PATH = EVAL_DIR / "golden_feedback.json"
REPORT_PATH = EVAL_DIR / "eval_report.md"
VALID_SENTIMENTS = {"positive", "neutral", "negative"}
DEFAULT_MODEL = "gpt-4o-mini"
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "for",
    "from",
    "in",
    "into",
    "is",
    "it",
    "of",
    "on",
    "one",
    "or",
    "our",
    "the",
    "to",
    "us",
    "with",
}


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    sentiment_match: bool
    sentiment_valid: bool
    theme_overlap: float
    action_intent_score: float
    malformed: bool
    error: str | None
    expected: dict[str, Any]
    actual: dict[str, Any] | None


def main() -> int:
    examples = load_golden_examples()
    api_key = os.environ.get("OPENAI_API_KEY")
    model = os.environ.get("OPENAI_MODEL", DEFAULT_MODEL)

    if not api_key:
        message = (
            "OPENAI_API_KEY is not set. Skipping provider-backed eval. "
            "Set OPENAI_API_KEY and rerun: python backend/evals/run_eval.py"
        )
        write_skipped_report(examples, message, model)
        print(message)
        return 0

    try:
        from openai import OpenAI
    except ImportError:
        message = (
            "The openai Python package is not installed. Install backend dependencies, "
            "then rerun: python backend/evals/run_eval.py"
        )
        write_skipped_report(examples, message, model)
        print(message)
        return 1

    client = OpenAI(api_key=api_key)
    results = [run_case(client, model, example) for example in examples]
    write_eval_report(results, model)

    failures = sum(1 for result in results if result.error or result.malformed)
    print(f"Wrote {REPORT_PATH}")
    print(f"Evaluated {len(results)} cases with {failures} malformed outputs/provider failures.")
    return 1 if failures else 0


def load_golden_examples() -> list[dict[str, Any]]:
    with GOLDEN_PATH.open("r", encoding="utf-8") as file:
        examples = json.load(file)

    if not isinstance(examples, list) or not examples:
        raise ValueError("golden_feedback.json must contain a non-empty list of examples.")

    return examples


def run_case(client: Any, model: str, example: dict[str, Any]) -> CaseResult:
    expected = example["expected"]

    try:
        actual = extract_feedback(client, model, example["feedback"])
        malformed_error = validate_output_shape(actual)
        malformed = malformed_error is not None
        return CaseResult(
            case_id=example["id"],
            sentiment_match=actual.get("sentiment") == expected["sentiment"],
            sentiment_valid=actual.get("sentiment") in VALID_SENTIMENTS,
            theme_overlap=theme_overlap(expected.get("themes", []), actual.get("themes", [])),
            action_intent_score=action_intent_score(
                expected.get("action_item_intents", []),
                actual.get("action_items", []),
            ),
            malformed=malformed,
            error=malformed_error,
            expected=expected,
            actual=actual,
        )
    except Exception as exc:  # Keep provider failure reports sanitized.
        return CaseResult(
            case_id=example["id"],
            sentiment_match=False,
            sentiment_valid=False,
            theme_overlap=0.0,
            action_intent_score=0.0,
            malformed=False,
            error=f"{type(exc).__name__}: provider or parsing failure",
            expected=expected,
            actual=None,
        )


def extract_feedback(client: Any, model: str, feedback: str) -> dict[str, Any]:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
            {"role": "user", "content": feedback},
        ],
        response_format={"type": "json_object"},
        temperature=0,
    )
    content = response.choices[0].message.content
    if not content:
        raise ValueError("OpenAI response did not include message content.")
    parsed = json.loads(content)
    if not isinstance(parsed, dict):
        raise ValueError("OpenAI response JSON must be an object.")
    return parsed


def validate_output_shape(actual: dict[str, Any]) -> str | None:
    try:
        parsed = ExtractionResult.model_validate(actual)
    except Exception as exc:
        return f"Invalid extraction shape: {exc}"

    if any(len(theme.split()) > 5 for theme in parsed.themes):
        return "themes must be short strings."

    return None


def theme_overlap(expected_themes: list[str], actual_themes: list[str]) -> float:
    if not expected_themes:
        return 1.0

    matched = 0
    for expected_theme in expected_themes:
        expected_tokens = tokenize(expected_theme)
        if any(expected_tokens & tokenize(actual_theme) for actual_theme in actual_themes):
            matched += 1

    return matched / len(expected_themes)


def action_intent_score(expected_intents: list[str], actual_items: list[str]) -> float:
    if not expected_intents:
        return 1.0 if not actual_items else 0.0

    matched = 0
    for expected_intent in expected_intents:
        expected_tokens = tokenize(expected_intent)
        if any(token_overlap_ratio(expected_tokens, tokenize(actual_item)) >= 0.3 for actual_item in actual_items):
            matched += 1

    return matched / len(expected_intents)


def token_overlap_ratio(expected_tokens: set[str], actual_tokens: set[str]) -> float:
    if not expected_tokens:
        return 0.0
    return len(expected_tokens & actual_tokens) / len(expected_tokens)


def tokenize(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", value.lower())
        if token not in STOPWORDS and len(token) > 1
    }


def write_skipped_report(examples: list[dict[str, Any]], message: str, model: str) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# Eval Report",
        "",
        f"Generated: {now}",
        f"Model: `{model}`",
        "Status: skipped",
        "",
        "## Reason",
        "",
        message,
        "",
        "## Golden Cases",
        "",
        f"Loaded {len(examples)} golden examples from `golden_feedback.json`.",
    ]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_eval_report(results: list[CaseResult], model: str) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    count = len(results)
    sentiment_matches = sum(1 for result in results if result.sentiment_match)
    malformed = sum(1 for result in results if result.malformed)
    failures = sum(1 for result in results if result.error and not result.malformed)
    average_theme_overlap = sum(result.theme_overlap for result in results) / count
    average_action_score = sum(result.action_intent_score for result in results) / count

    lines = [
        "# Eval Report",
        "",
        f"Generated: {now}",
        f"Model: `{model}`",
        "Status: completed",
        "",
        "## Summary",
        "",
        f"- Cases: {count}",
        f"- Sentiment exact match: {sentiment_matches}/{count}",
        f"- Average theme overlap: {average_theme_overlap:.2f}",
        f"- Average action intent score: {average_action_score:.2f}",
        f"- Malformed outputs: {malformed}",
        f"- Provider failures: {failures}",
        "",
        "## Case Results",
        "",
        "| Case | Sentiment | Theme overlap | Action intent | Malformed/failure |",
        "| --- | --- | ---: | ---: | --- |",
    ]

    for result in results:
        problem = result.error or ("malformed" if result.malformed else "")
        sentiment_status = "pass" if result.sentiment_match else "fail"
        lines.append(
            f"| `{result.case_id}` | {sentiment_status} | "
            f"{result.theme_overlap:.2f} | {result.action_intent_score:.2f} | {problem} |"
        )

    lines.extend(["", "## Notes", ""])
    lines.append("Theme overlap is token-based and intentionally approximate.")
    lines.append("Action intent scoring checks whether expected request intent appears in extracted action items.")
    lines.append("Failures here should guide prompt/schema changes; this runner does not edit app prompts.")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Eval setup failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(1)
