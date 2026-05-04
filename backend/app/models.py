"""Internal persisted data shapes."""

from dataclasses import dataclass


Sentiment = str


@dataclass(frozen=True)
class FeedbackRecord:
    id: int
    feedback_text: str
    sentiment: Sentiment
    themes: list[str]
    action_items: list[str]
    created_at: str
