import type { SentimentTrendItem } from "../types";

type SentimentTrendProps = {
  trend: SentimentTrendItem[];
};

export function SentimentTrend({ trend }: SentimentTrendProps) {
  if (trend.length === 0) {
    return <p className="empty-state">No trend data yet.</p>;
  }

  return (
    <div className="trend-list">
      {trend.map((item) => {
        const total = item.positive + item.neutral + item.negative;

        return (
          <div className="trend-row" key={item.date}>
            <span>{formatDate(item.date)}</span>
            <div className="stacked-bar" aria-label={`${item.date}: ${total} feedback entries`}>
              <span className="fill-positive" style={{ width: `${percentage(item.positive, total)}%` }} />
              <span className="fill-neutral" style={{ width: `${percentage(item.neutral, total)}%` }} />
              <span className="fill-negative" style={{ width: `${percentage(item.negative, total)}%` }} />
            </div>
            <strong>{total}</strong>
          </div>
        );
      })}
    </div>
  );
}

function percentage(value: number, total: number) {
  if (total === 0) {
    return 0;
  }

  return (value / total) * 100;
}

function formatDate(value: string) {
  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return value;
  }

  return new Intl.DateTimeFormat(undefined, { month: "short", day: "numeric" }).format(date);
}
