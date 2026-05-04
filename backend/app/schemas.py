"""API request and response schemas."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


Sentiment = Literal["positive", "neutral", "negative"]


class FeedbackCreateRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=20_000)

    @field_validator("text")
    @classmethod
    def validate_text(cls, text: str) -> str:
        cleaned = text.strip()
        if not cleaned:
            raise ValueError("text must contain feedback")
        return cleaned


class ExtractionResult(BaseModel):
    sentiment: Sentiment
    themes: list[str] = Field(..., min_length=1, max_length=3)
    action_items: list[str] = Field(default_factory=list)

    @field_validator("themes")
    @classmethod
    def validate_themes(cls, themes: list[str]) -> list[str]:
        cleaned = [theme.strip() for theme in themes if theme.strip()]
        if not 1 <= len(cleaned) <= 3:
            raise ValueError("themes must contain 1 to 3 non-empty values")
        return cleaned

    @field_validator("action_items")
    @classmethod
    def validate_action_items(cls, action_items: list[str]) -> list[str]:
        return [item.strip() for item in action_items if item.strip()]


class FeedbackRecordResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    feedback_text: str
    sentiment: Sentiment
    themes: list[str]
    action_items: list[str]
    created_at: str


class FeedbackCreateResponse(BaseModel):
    records: list[FeedbackRecordResponse]


class ThemeFrequency(BaseModel):
    theme: str
    count: int


class SentimentTrendPoint(BaseModel):
    date: str
    positive: int = 0
    neutral: int = 0
    negative: int = 0


class DashboardResponse(BaseModel):
    total_feedback: int
    theme_frequencies: list[ThemeFrequency]
    sentiment_distribution: dict[Sentiment, int]
    sentiment_trend: list[SentimentTrendPoint]
    feedback: list[FeedbackRecordResponse]


class HealthResponse(BaseModel):
    status: Literal["ok"]
