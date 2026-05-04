"""Tests for batch feedback parsing."""

from backend.app.batch_parser import parse_feedback_batch


def test_single_feedback_entry() -> None:
    assert parse_feedback_batch("The export flow is confusing.") == [
        "The export flow is confusing."
    ]


def test_single_sentence_with_comma_and_but_stays_one_entry() -> None:
    feedback = (
        "The product is useful, but the dashboard is slow and we need export "
        "to CSV for weekly QA reviews."
    )

    assert parse_feedback_batch(feedback) == [feedback]


def test_multiple_lines_become_entries() -> None:
    raw_text = """
    Search is fast now.
    Please add bulk delete.

    Billing page times out.
    """

    assert parse_feedback_batch(raw_text) == [
        "Search is fast now.",
        "Please add bulk delete.",
        "Billing page times out.",
    ]


def test_empty_lines_are_ignored() -> None:
    raw_text = """

    Search is fast now.

    Please add bulk delete.

    """

    assert parse_feedback_batch(raw_text) == [
        "Search is fast now.",
        "Please add bulk delete.",
    ]


def test_csv_like_paste_with_feedback_column_becomes_entries() -> None:
    raw_text = """id,feedback
1,"The dashboard loads quickly and looks clear."
2,"Please add export to CSV for reports."
"""

    assert parse_feedback_batch(raw_text) == [
        "The dashboard loads quickly and looks clear.",
        "Please add export to CSV for reports.",
    ]


def test_csv_like_paste_without_header_joins_columns_per_row() -> None:
    raw_text = """1,Billing page times out
2,Please add export to CSV for reports
"""

    assert parse_feedback_batch(raw_text) == [
        "1 Billing page times out",
        "2 Please add export to CSV for reports",
    ]
