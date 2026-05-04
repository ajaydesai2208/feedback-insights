"""Parse pasted feedback into individual entries."""

import csv
from io import StringIO


def parse_feedback_batch(raw_text: str) -> list[str]:
    text = raw_text.strip()
    if not text:
        return []

    csv_entries = _parse_csv_like(text)
    if csv_entries:
        return csv_entries

    line_entries = [line.strip() for line in text.splitlines() if line.strip()]
    if len(line_entries) > 1:
        return line_entries

    return [text]


def _parse_csv_like(text: str) -> list[str]:
    try:
        rows = list(csv.reader(StringIO(text)))
    except csv.Error:
        return []

    cleaned_rows = [[cell.strip() for cell in row] for row in rows]
    non_empty_rows = [
        [cell for cell in row if cell]
        for row in cleaned_rows
        if any(cell for cell in row)
    ]
    if not non_empty_rows:
        return []

    header_index = _feedback_header_index(non_empty_rows[0])
    if header_index is not None:
        entries = [
            _feedback_from_header_row(row, header_index)
            for row in non_empty_rows[1:]
        ]
        return _dedupe_preserving_order([entry for entry in entries if entry])

    has_multiple_columns = any(len(row) > 1 for row in non_empty_rows)
    if len(non_empty_rows) <= 1 or not has_multiple_columns:
        return []

    entries = [" ".join(row) for row in non_empty_rows]
    return _dedupe_preserving_order(entries)


def _feedback_header_index(cells: list[str]) -> int | None:
    header_terms = {"feedback", "comment", "comments", "text", "review", "message"}
    for index, cell in enumerate(cells):
        normalized = cell.strip().lower().replace("_", " ")
        if normalized in header_terms:
            return index
    return None


def _feedback_from_header_row(row: list[str], header_index: int) -> str:
    if header_index < len(row) and row[header_index]:
        return row[header_index]
    return " ".join(row)


def _dedupe_preserving_order(entries: list[str]) -> list[str]:
    seen: set[str] = set()
    unique_entries: list[str] = []
    for entry in entries:
        if entry in seen:
            continue
        seen.add(entry)
        unique_entries.append(entry)
    return unique_entries
