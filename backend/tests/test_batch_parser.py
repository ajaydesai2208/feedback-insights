"""Tests for batch feedback parsing."""

from backend.app.batch_parser import parse_feedback_batch


def test_single_feedback_entry() -> None:
    assert parse_feedback_batch("The export flow is confusing.") == [
        "The export flow is confusing."
    ]


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


def test_csv_like_paste_uses_feedback_cells() -> None:
    raw_text = """id,feedback
1,"The dashboard loads quickly and looks clear."
2,"Please add export to CSV for reports."
"""

    assert parse_feedback_batch(raw_text) == [
        "The dashboard loads quickly and looks clear.",
        "Please add export to CSV for reports.",
    ]
