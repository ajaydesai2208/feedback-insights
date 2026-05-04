"""SQLite database setup and persistence helpers."""

import json
import os
import sqlite3
from pathlib import Path
from typing import Iterable

from backend.app.models import FeedbackRecord
from backend.app.schemas import ExtractionResult


DEFAULT_DATABASE_PATH = Path(os.getenv("FEEDBACK_INSIGHTS_DB", "backend/feedback_insights.sqlite3"))


def connect(database_path: Path | str = DEFAULT_DATABASE_PATH) -> sqlite3.Connection:
    path = Path(database_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feedback_text TEXT NOT NULL,
            sentiment TEXT NOT NULL CHECK (sentiment IN ('positive', 'neutral', 'negative')),
            themes_json TEXT NOT NULL,
            action_items_json TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
        )
        """
    )
    connection.commit()


def create_feedback(
    connection: sqlite3.Connection,
    feedback_text: str,
    extraction: ExtractionResult,
) -> FeedbackRecord:
    cursor = connection.execute(
        """
        INSERT INTO feedback (feedback_text, sentiment, themes_json, action_items_json)
        VALUES (?, ?, ?, ?)
        """,
        (
            feedback_text,
            extraction.sentiment,
            json.dumps(extraction.themes),
            json.dumps(extraction.action_items),
        ),
    )
    connection.commit()
    record = get_feedback_by_id(connection, int(cursor.lastrowid))
    if record is None:
        raise RuntimeError("created feedback record could not be loaded")
    return record


def list_feedback(connection: sqlite3.Connection) -> list[FeedbackRecord]:
    rows = connection.execute(
        """
        SELECT id, feedback_text, sentiment, themes_json, action_items_json, created_at
        FROM feedback
        ORDER BY created_at DESC, id DESC
        """
    ).fetchall()
    return [_row_to_record(row) for row in rows]


def get_feedback_by_id(connection: sqlite3.Connection, record_id: int) -> FeedbackRecord | None:
    row = connection.execute(
        """
        SELECT id, feedback_text, sentiment, themes_json, action_items_json, created_at
        FROM feedback
        WHERE id = ?
        """,
        (record_id,),
    ).fetchone()
    if row is None:
        return None
    return _row_to_record(row)


def create_many_feedback(
    connection: sqlite3.Connection,
    extracted_feedback: Iterable[tuple[str, ExtractionResult]],
) -> list[FeedbackRecord]:
    return [
        create_feedback(connection, feedback_text, extraction)
        for feedback_text, extraction in extracted_feedback
    ]


def _row_to_record(row: sqlite3.Row) -> FeedbackRecord:
    return FeedbackRecord(
        id=row["id"],
        feedback_text=row["feedback_text"],
        sentiment=row["sentiment"],
        themes=json.loads(row["themes_json"]),
        action_items=json.loads(row["action_items_json"]),
        created_at=row["created_at"],
    )
