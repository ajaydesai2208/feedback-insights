"""OpenAI client wrapper for feedback extraction."""

import json
import os

from openai import OpenAI, OpenAIError
from pydantic import ValidationError

from backend.app.extraction_prompt import EXTRACTION_SYSTEM_PROMPT
from backend.app.schemas import ExtractionResult
from backend.app.settings import load_local_environment


load_local_environment()


class LLMConfigurationError(RuntimeError):
    pass


class LLMProviderError(RuntimeError):
    pass


class LLMOutputError(RuntimeError):
    pass


def extract_feedback_insights(feedback_text: str) -> ExtractionResult:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise LLMConfigurationError("OPENAI_API_KEY is not set")

    client = OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": EXTRACTION_SYSTEM_PROMPT},
                {"role": "user", "content": feedback_text},
            ],
        )
    except OpenAIError as exc:
        raise LLMProviderError("OpenAI extraction request failed") from exc

    content = response.choices[0].message.content
    if not content:
        raise LLMOutputError("OpenAI returned an empty extraction response")

    try:
        payload = json.loads(content)
    except json.JSONDecodeError as exc:
        raise LLMOutputError("OpenAI returned invalid JSON") from exc

    try:
        return ExtractionResult.model_validate(payload)
    except ValidationError as exc:
        raise LLMOutputError("OpenAI returned an invalid extraction shape") from exc
