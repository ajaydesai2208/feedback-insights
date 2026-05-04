"""Tests for dashboard aggregation."""

from backend.app.dashboard import build_dashboard
from backend.app.models import FeedbackRecord


def test_dashboard_aggregation_counts_themes_sentiment_and_trend() -> None:
    records = [
        FeedbackRecord(
            id=1,
            feedback_text="Great search.",
            sentiment="positive",
            themes=["Search"],
            action_items=[],
            created_at="2026-05-04T10:00:00Z",
        ),
        FeedbackRecord(
            id=2,
            feedback_text="Search is slow. Add filters.",
            sentiment="negative",
            themes=["Search", "Filters"],
            action_items=["Add filters"],
            created_at="2026-05-04T11:00:00Z",
        ),
    ]

    dashboard = build_dashboard(records)

    assert dashboard.total_feedback == 2
    assert dashboard.sentiment_distribution == {
        "positive": 1,
        "neutral": 0,
        "negative": 1,
    }
    assert dashboard.theme_frequencies[0].theme == "Search"
    assert dashboard.theme_frequencies[0].count == 2
    assert dashboard.sentiment_trend[0].date == "2026-05-04"
    assert dashboard.sentiment_trend[0].positive == 1
    assert dashboard.sentiment_trend[0].negative == 1
