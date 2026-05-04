import { useMemo, useState } from "react";
import type { FeedbackRecord } from "../types";

type FeedbackTableProps = {
  records: FeedbackRecord[];
};

export function FeedbackTable({ records }: FeedbackTableProps) {
  const [query, setQuery] = useState("");
  const normalizedQuery = query.trim().toLowerCase();
  const filteredRecords = useMemo(() => {
    if (!normalizedQuery) {
      return records;
    }

    return records.filter((record) =>
      [
        record.feedback_text,
        record.sentiment,
        record.themes.join(" "),
        record.action_items.join(" "),
        record.created_at,
      ]
        .join(" ")
        .toLowerCase()
        .includes(normalizedQuery),
    );
  }, [normalizedQuery, records]);

  return (
    <section className="panel feedback-table-section">
      <div className="section-heading">
        <div>
          <h2>Feedback records</h2>
          <p>{records.length === 0 ? "No records yet." : `${filteredRecords.length} of ${records.length} shown`}</p>
        </div>
        <input
          aria-label="Search feedback records"
          type="search"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search feedback, themes, action items"
        />
      </div>

      {filteredRecords.length === 0 ? (
        <p className="empty-state">{records.length === 0 ? "Submit feedback to populate the table." : "No records match the search."}</p>
      ) : (
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Feedback</th>
                <th>Sentiment</th>
                <th>Themes</th>
                <th>Action items</th>
                <th>Created</th>
              </tr>
            </thead>
            <tbody>
              {filteredRecords.map((record) => (
                <tr key={record.id}>
                  <td>{record.feedback_text}</td>
                  <td>
                    <span className={`sentiment sentiment-${record.sentiment}`}>{record.sentiment}</span>
                  </td>
                  <td>{record.themes.length > 0 ? record.themes.join(", ") : "None"}</td>
                  <td>{record.action_items.length > 0 ? record.action_items.join(", ") : "None"}</td>
                  <td>{formatTimestamp(record.created_at)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  );
}

function formatTimestamp(value: string) {
  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return value;
  }

  return new Intl.DateTimeFormat(undefined, {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(date);
}
