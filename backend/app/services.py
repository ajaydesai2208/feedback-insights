"""Application service orchestration."""

import sqlite3

from backend.app.batch_parser import parse_feedback_batch
from backend.app.db import create_many_feedback
from backend.app.llm import extract_feedback_insights
from backend.app.models import FeedbackRecord


def ingest_feedback_batch(connection: sqlite3.Connection, raw_text: str) -> list[FeedbackRecord]:
    entries = parse_feedback_batch(raw_text)
    extracted = [(entry, extract_feedback_insights(entry)) for entry in entries]
    return create_many_feedback(connection, extracted)
