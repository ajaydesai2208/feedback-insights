"""Tests for extraction schema validation."""

import pytest
from pydantic import ValidationError

from backend.app.schemas import ExtractionResult


def test_valid_extraction_schema() -> None:
    extraction = ExtractionResult(
        sentiment="negative",
        themes=["Billing", "Performance"],
        action_items=["Fix invoice download timeout"],
    )

    assert extraction.sentiment == "negative"
    assert extraction.themes == ["Billing", "Performance"]
    assert extraction.action_items == ["Fix invoice download timeout"]


def test_rejects_invalid_sentiment() -> None:
    with pytest.raises(ValidationError):
        ExtractionResult(sentiment="mixed", themes=["Billing"], action_items=[])


def test_rejects_empty_themes() -> None:
    with pytest.raises(ValidationError):
        ExtractionResult(sentiment="neutral", themes=[], action_items=[])
