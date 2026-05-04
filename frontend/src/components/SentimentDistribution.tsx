import type { SentimentDistributionItem } from "../types";

type SentimentDistributionProps = {
  distribution: SentimentDistributionItem[];
};

const SENTIMENTS = ["positive", "neutral", "negative"] as const;

export function SentimentDistribution({ distribution }: SentimentDistributionProps) {
  const counts = new Map(distribution.map((item) => [item.sentiment, item.count]));
  const total = distribution.reduce((sum, item) => sum + item.count, 0);

  if (total === 0) {
    return <p className="empty-state">No sentiment data yet.</p>;
  }

  return (
    <div className="distribution-list">
      {SENTIMENTS.map((sentiment) => {
        const count = counts.get(sentiment) ?? 0;
        const percent = Math.round((count / total) * 100);

        return (
          <div className="distribution-row" key={sentiment}>
            <div className="ranked-label">
              <span className={`sentiment sentiment-${sentiment}`}>{sentiment}</span>
              <strong>{count}</strong>
            </div>
            <div className="bar-track" aria-label={`${sentiment} ${percent}%`}>
              <span className={`fill-${sentiment}`} style={{ width: `${percent}%` }} />
            </div>
          </div>
        );
      })}
    </div>
  );
}
