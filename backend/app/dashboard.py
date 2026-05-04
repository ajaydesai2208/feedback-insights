"""Dashboard aggregation helpers."""

from collections import Counter, defaultdict

from backend.app.models import FeedbackRecord
from backend.app.schemas import DashboardResponse, SentimentTrendPoint, ThemeFrequency


SENTIMENTS = ("positive", "neutral", "negative")


def build_dashboard(records: list[FeedbackRecord]) -> DashboardResponse:
    theme_counts = Counter(theme for record in records for theme in record.themes)
    sentiment_counts = Counter(record.sentiment for record in records)

    trend_by_date: dict[str, Counter[str]] = defaultdict(Counter)
    for record in records:
        date = record.created_at[:10]
        trend_by_date[date][record.sentiment] += 1

    return DashboardResponse(
        total_feedback=len(records),
        theme_frequencies=[
            ThemeFrequency(theme=theme, count=count)
            for theme, count in theme_counts.most_common()
        ],
        sentiment_distribution={
            sentiment: sentiment_counts.get(sentiment, 0) for sentiment in SENTIMENTS
        },
        sentiment_trend=[
            SentimentTrendPoint(
                date=date,
                positive=counts.get("positive", 0),
                neutral=counts.get("neutral", 0),
                negative=counts.get("negative", 0),
            )
            for date, counts in sorted(trend_by_date.items())
        ],
        feedback=records,
    )
