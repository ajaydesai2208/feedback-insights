"""Parse pasted feedback into individual entries."""

import csv
from io import StringIO


def parse_feedback_batch(raw_text: str) -> list[str]:
    text = raw_text.strip()
    if not text:
        return []

    csv_entries = _parse_csv_like(text)
    if len(csv_entries) > 1:
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

    entries: list[str] = []
    for row in rows:
        cleaned_cells = [cell.strip() for cell in row if cell.strip()]
        if not cleaned_cells:
            continue
        entries.extend(_feedback_cells(cleaned_cells))

    return _dedupe_preserving_order(entries)


def _feedback_cells(cells: list[str]) -> list[str]:
    if _looks_like_header(cells):
        return []
    if len(cells) == 1:
        return cells

    # CSV pastes often include id/source columns plus one longer feedback column.
    long_cells = [cell for cell in cells if len(cell.split()) >= 4]
    if long_cells:
        return long_cells
    return cells


def _looks_like_header(cells: list[str]) -> bool:
    header_terms = {"feedback", "comment", "comments", "text", "review", "message"}
    normalized = {cell.strip().lower().replace("_", " ") for cell in cells}
    return bool(normalized & header_terms)


def _dedupe_preserving_order(entries: list[str]) -> list[str]:
    seen: set[str] = set()
    unique_entries: list[str] = []
    for entry in entries:
        if entry in seen:
            continue
        seen.add(entry)
        unique_entries.append(entry)
    return unique_entries
